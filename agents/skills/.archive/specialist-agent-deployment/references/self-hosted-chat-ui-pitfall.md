# Self-Hosted Chat UI: localhost Pitfall

## The problem

When serving a chat UI (HTML/JS) from an EC2 instance or remote server, JavaScript `fetch()` calls to `http://localhost:11434` fail silently. The browser's `localhost` is the user's laptop, not the server. Ollama is running on the server but the browser cannot reach it.

## Symptoms

- Chat UI loads but every message returns "Connection lost" or times out
- Browser console shows `ERR_CONNECTION_REFUSED` or `net::ERR_CONNECTION_TIMED_OUT`
- Ollama is confirmed running on the server (`ollama ps` works via SSH)
- Direct `curl` to the Ollama endpoint from the server works fine

## The fix: Backend proxy

Serve the chat UI AND proxy API calls from the same origin. The Python server handles both:

```
Browser → https://server:8090/ (serves HTML)
Browser → https://server:8090/api/chat (proxied to Ollama)
                                     ↓
                              http://localhost:11434/v1/chat/completions
```

The JavaScript calls `/api/chat` (same origin, no CORS issue). The Python backend forwards to Ollama on the server's localhost.

## Working server pattern (Python http.server)

```python
class Handler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            # Serve the chat UI HTML
            self.send_response(200)
            self.send_header('Content-Type', 'text/html')
            self.end_headers()
            self.wfile.write(HTML.encode())

    def do_POST(self):
        if self.path == '/api/chat':
            # Proxy to Ollama
            length = int(self.headers.get('Content-Length', 0))
            body = self.rfile.read(length)
            req = json.loads(body)
            
            payload = json.dumps({
                "model": MODEL,
                "messages": messages,
                "stream": False
            }).encode()
            
            ollama_req = urllib.request.Request(OLLAMA_URL, data=payload)
            with urllib.request.urlopen(ollama_req, timeout=120) as resp:
                data = json.loads(resp.read())
            
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(data).encode())
```

## Never do this

- Do NOT open Ollama port 11434 to the public internet in the security group
- Do NOT hardcode the server's public IP in the JavaScript (IP changes on stop/start unless Elastic IP)
- Do NOT use a static file server (`python3 -m http.server`) for interactive chat — it cannot proxy API calls and the browser-side `localhost` call will fail

## Model pre-loading

Ollama unloads models from GPU when idle. The first query after idle can take 5-15 seconds as the model loads. The Python server should pre-warm the model at startup:

```python
# Pre-warm: load model so first user query is instant
warm = json.dumps({
    "model": MODEL,
    "messages": [{"role": "user", "content": "ping"}],
    "stream": False,
    "options": {"num_predict": 5}
}).encode()
req = urllib.request.Request(OLLAMA_URL, data=warm)
urllib.request.urlopen(req, timeout=60)
```
