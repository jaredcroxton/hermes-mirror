# EC2 API Proxy Server Template

Deployable Python server that serves an HTML chat UI and proxies API calls to a local Ollama instance. Single file, zero dependencies beyond Python stdlib.

## When to use

- Web chat UI served from EC2 calls Ollama/Hermes on `localhost`
- Do not want to expose the API port (11434) in the security group
- Want same-origin requests (no CORS issues, no public API exposure)
- Ollama model needs pre-warming to avoid first-query timeouts

## Server template

```python
#!/usr/bin/env python3
"""Single-file server: serves HTML UI + proxies API calls to Ollama."""
import http.server
import json
import urllib.request
import urllib.error

PORT = 8090
API_URL = "http://localhost:11434/v1/chat/completions"
MODEL = "phi4:14b"

SYSTEM_PROMPT = """Your system prompt here."""

HTML = r"""Your HTML here. JavaScript calls /api/chat (same origin)."""

class Handler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/' or self.path == '/index.html':
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
                api_req = urllib.request.Request(API_URL, data=payload,
                    headers={"Content-Type": "application/json"})
                with urllib.request.urlopen(api_req, timeout=120) as resp:
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
    # Pre-warm model: one short query so first user request is instant
    print("Pre-loading model...")
    try:
        warm = json.dumps({
            "model": MODEL,
            "messages": [{"role": "user", "content": "ping"}],
            "stream": False,
            "options": {"num_predict": 5}
        }).encode()
        req = urllib.request.Request(API_URL, data=warm,
            headers={"Content-Type": "application/json"})
        urllib.request.urlopen(req, timeout=60)
        print("Model ready.")
    except Exception as e:
        print(f"Warm-up note: {e}")

    server = http.server.HTTPServer(('0.0.0.0', PORT), Handler)
    print(f"Serving on port {PORT}")
    server.serve_forever()
```

## Frontend JavaScript pattern

```javascript
// CORRECT — same-origin, no CORS
const resp = await fetch('/api/chat', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({ messages: conversation })
});

// WRONG — localhost resolves to client browser, not server
const resp = await fetch('http://localhost:11434/v1/chat/completions', { ... });
```

## Deployment on EC2

```bash
# Copy to server
scp -i key.pem ap-server.py ubuntu@<ip>:/home/ubuntu/

# Kill old server on port 8090
ssh -i key.pem ubuntu@<ip> 'kill $(lsof -t -i:8090) 2>/dev/null'

# Start new server (background, survives SSH disconnect)
ssh -i key.pem ubuntu@<ip> 'nohup python3 /home/ubuntu/ap-server.py > /tmp/ap-server.log 2>&1 &'

# Verify
ssh -i key.pem ubuntu@<ip> 'curl -s http://localhost:8090/health'
```

## Pitfalls

1. **`localhost` in JS resolves to client.** Always use same-origin proxy endpoints.
2. **Ollama idle unload causes first-query timeout.** Always pre-warm the model at server startup.
3. **SSH `pkill`/`pgrep` unreliable over SSH.** Use `kill $(lsof -t -i:PORT)` for port-based process management.
4. **nohup output buffering.** Python may not flush stdout immediately with nohup. Check the process exists with `ps aux | grep`, not just log output.
