#!/usr/bin/env python3
"""
Deployable template: single-file Python HTTP server that serves an agent chat
HTML page and proxies API calls to Ollama on localhost.

Copy to EC2, edit the three config variables at the top, then run:
  nohup python3 server.py > /tmp/agent-server.log 2>&1 &

Architecture:
  Browser → :PORT (public) → Python server → localhost:11434 (Ollama)
    GET /  → serves HTML
    POST /api/chat → proxies to Ollama v1/chat/completions

Why: JavaScript fetch('http://localhost:11434') in a browser page served
from EC2 resolves to the USER's laptop, not the EC2. The proxy pattern
keeps all API calls same-origin.
"""

import http.server
import json
import urllib.request
import urllib.error

# ── Config (edit these three) ──────────────────────────────────────────
PORT = 8090
OLLAMA_URL = "http://localhost:11434/v1/chat/completions"
MODEL = "phi4:14b"
# ───────────────────────────────────────────────────────────────────────

SYSTEM_PROMPT = """You are [AGENT NAME], the [ROLE] for [COMPANY].
[Full SOUL.md context goes here — markets, products, voice, operating principles.]"""

HTML = r"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>[AGENT NAME] - [COMPANY]</title>
<style>
*,*::before,*::after{box-sizing:border-box;margin:0;padding:0}
:root{
--bg:#0A0A0A;--surface:#111111;--border:#1E1E1E;--primary:#F0F0F5;--secondary:#9CA3AF;
--accent:#C8A951;--radius:12px;--transition:200ms ease;
--font:'Inter',system-ui,-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif}
html{background:var(--bg);color:var(--primary);font-family:var(--font);font-size:15px;line-height:1.6;-webkit-font-smoothing:antialiased}
body{display:flex;flex-direction:column;height:100vh;max-width:720px;margin:0 auto;padding:0 20px}
header{padding:24px 0 16px;border-bottom:1px solid var(--border);flex-shrink:0}
header h1{font-size:24px;font-weight:700;letter-spacing:-.3px}
header h1 span{color:var(--accent)}
header p{color:var(--secondary);font-size:13px;margin-top:4px}
.badge{display:inline-block;background:var(--accent);color:#0A0A0A;font-size:10px;font-weight:700;padding:3px 8px;border-radius:20px;letter-spacing:.5px;margin-left:8px;vertical-align:middle}
.chat{flex:1;overflow-y:auto;padding:20px 0;display:flex;flex-direction:column;gap:16px}
.msg{max-width:85%;padding:14px 18px;border-radius:var(--radius);line-height:1.55;font-size:14px;animation:fadeIn .3s ease}
.msg.user{align-self:flex-end;background:var(--accent);color:#0A0A0A;border-bottom-right-radius:4px}
.msg.agent{align-self:flex-start;background:var(--surface);border:1px solid var(--border);border-bottom-left-radius:4px}
.msg.error{align-self:flex-start;background:#3B1111;border:1px solid #7F1D1D;color:#FCA5A5}
@keyframes fadeIn{from{opacity:0;transform:translateY(8px)}to{opacity:1;transform:translateY(0)}}
form{flex-shrink:0;padding:16px 0 24px;display:flex;gap:10px}
form input{flex:1;background:var(--surface);border:1px solid var(--border);color:var(--primary);padding:12px 16px;border-radius:10px;font-family:var(--font);font-size:14px;outline:none;transition:border var(--transition)}
form input:focus{border-color:var(--accent)}
form input::placeholder{color:var(--secondary);opacity:.5}
form button{background:var(--accent);color:#0A0A0A;border:none;padding:12px 20px;border-radius:10px;font-family:var(--font);font-size:14px;font-weight:600;cursor:pointer;transition:all var(--transition);white-space:nowrap}
form button:hover{filter:brightness(1.1)}
form button:disabled{opacity:.4;cursor:not-allowed}
.status{text-align:center;padding:8px;color:var(--secondary);font-size:11px;flex-shrink:0}
.status.connected{color:#22C55E}
</style>
</head>
<body>
<header>
<h1>[AGENT NAME] <span>[COMPANY]</span> <span class="badge">AGENT</span></h1>
<p>[One-line description of the agent]</p>
</header>
<div class="chat" id="chat">
<div class="msg agent">
[Intro message from the agent.]
</div>
</div>
<div class="status" id="status">ready</div>
<form id="form">
<input type="text" id="input" placeholder="Ask [AGENT NAME] anything..." autofocus autocomplete="off">
<button type="submit" id="btn">Send</button>
</form>
<script>
const chat=document.getElementById('chat');
const status=document.getElementById('status');
const input=document.getElementById('input');
const form=document.getElementById('form');
const btn=document.getElementById('btn');
let conver=[{role:'system',content:document.querySelector('.msg.agent').textContent.replace(/\\n/g,' ')}];

function addMsg(role,text,isErr){
const d=document.createElement('div');
d.className='msg '+role+(isErr?' error':'');
d.textContent=text;
chat.appendChild(d);
chat.scrollTop=chat.scrollHeight;
return d;
}

form.addEventListener('submit',async(e)=>{
e.preventDefault();
const text=input.value.trim();
if(!text)return;
input.value='';
addMsg('user',text);
const loadDiv=addMsg('agent','Thinking...');
btn.disabled=true;
status.textContent='processing...';
status.className='status';
try{
const resp=await fetch('/api/chat',{
method:'POST',
headers:{'Content-Type':'application/json'},
body:JSON.stringify({messages:[...conver,{role:'user',content:text}]})
});
if(!resp.ok)throw new Error('Server error: '+resp.status);
const data=await resp.json();
loadDiv.remove();
const reply=data.choices[0].message.content;
addMsg('agent',reply);
conver.push({role:'user',content:text},{role:'assistant',content:reply});
status.textContent='ready';
status.className='status connected';
}catch(err){
loadDiv.remove();
addMsg('agent','Connection lost. Is Ollama running?',true);
status.textContent='error — retrying...';
status.className='status';
console.error(err);
}
btn.disabled=false;
});
</script>
</body>
</html>"""

class Handler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/' or self.path.endswith('.html'):
            self.send_response(200)
            self.send_header('Content-Type', 'text/html; charset=utf-8')
            self.end_headers()
            self.wfile.write(HTML.encode())
        elif self.path == '/health':
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({"status": "ok"}).encode())
        else:
            self.send_response(404)
            self.end_headers()

    def do_POST(self):
        if self.path == '/api/chat':
            length = int(self.headers.get('Content-Length', 0))
            body = self.rfile.read(length)
            req = json.loads(body)
            payload = json.dumps({
                "model": MODEL,
                "messages": [{"role": "system", "content": SYSTEM_PROMPT}] + req.get("messages", []),
                "stream": False,
                "options": {"temperature": 0.7, "num_predict": 1024}
            }).encode()
            try:
                ollama_req = urllib.request.Request(OLLAMA_URL, data=payload, headers={
                    "Content-Type": "application/json"
                })
                with urllib.request.urlopen(ollama_req, timeout=120) as resp:
                    data = json.loads(resp.read())
                self.send_response(200)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps(data).encode())
            except urllib.error.URLError as e:
                self.send_response(502)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({"error": str(e)}).encode())
        else:
            self.send_response(404)
            self.end_headers()

    def log_message(self, format, *args):
        pass  # quiet logs

if __name__ == '__main__':
    # Pre-warm: load the model so first user query is instant.
    # Without this, Ollama unloads the model when idle, and the first
    # query triggers a 10-30 second load that exceeds browser timeouts.
    print("Pre-loading model...")
    try:
        warm = json.dumps({
            "model": MODEL,
            "messages": [{"role": "user", "content": "ping"}],
            "stream": False,
            "options": {"num_predict": 5}
        }).encode()
        req = urllib.request.Request(OLLAMA_URL, data=warm, headers={"Content-Type": "application/json"})
        urllib.request.urlopen(req, timeout=60)
        print("Model ready.")
    except Exception as e:
        print(f"Warm-up note: {e}")

    server = http.server.HTTPServer(('0.0.0.0', PORT), Handler)
    print(f"Agent server running on port {PORT}")
    server.serve_forever()
