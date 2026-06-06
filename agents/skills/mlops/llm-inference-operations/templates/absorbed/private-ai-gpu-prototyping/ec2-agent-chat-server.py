#!/usr/bin/env python3
"""Agent chat server — serves branded chat UI and proxies API calls to Ollama.
Template for client-facing agent interfaces. Replace the four config constants below.

Pattern: Browser → :PORT (public) → Python server → localhost:11434 (Ollama)
  GET /      → serves HTML with agent branding
  POST /api/chat → proxies to Ollama v1/chat/completions (same-origin, no CORS)
  GET /health    → health check endpoint
"""
import http.server
import json
import urllib.request
import urllib.error

# === CONFIG — replace these per agent ===
PORT = 8090
OLLAMA_URL = "http://localhost:11434/v1/chat/completions"
MODEL = "phi4:14b"
SYSTEM_PROMPT = """You are [AGENT NAME], the [ROLE] for [CLIENT]. Write a detailed system prompt here with brand context, markets, products, and voice."""

# === HTML — replace with branded page per client ===
HTML = r"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>[AGENT] - [Client]</title>
<style>
/* Paste branded CSS here */
</style>
</head>
<body>
<header><h1>[AGENT NAME]</h1></header>
<div class="chat" id="chat"></div>
<form id="form">
<input type="text" id="input" placeholder="Ask anything..." autofocus>
<button type="submit">Send</button>
</form>
<script>
// Paste chat JavaScript here — key pattern:
// fetch('/api/chat', {method:'POST', body:JSON.stringify({messages})})
// NOT fetch('http://localhost:11434/...')
</script>
</body>
</html>"""


class Handler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/' or self.path == '/agent.html':
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
        pass  # quiet


if __name__ == '__main__':
    # Pre-warm model so first user query is fast
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
    print(f"Serving on port {PORT}")
    server.serve_forever()
