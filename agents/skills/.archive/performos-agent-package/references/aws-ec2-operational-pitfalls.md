# EC2 Operational Pitfalls — Ollama + Hermes on AWS GPU

Captured 02 June 2026 from the PerformOS AgentOS EC2 proof session.

## Pitfall 1: Root disk fills to 100%

**Symptom:** SSH works but commands fail. `df -h /` shows 100%. Instance becomes unstable.

**Root cause:** Ollama models (8-9 GB each) download to `/home/ubuntu/.ollama` by default, which is on the small root volume (30 GB). Docker images, apt cache, and logs compound the problem.

**Fix:**
1. Identify what is eating space: `du -sh /home/ubuntu/.ollama /var/lib/docker /var/log /tmp`
2. Move Ollama models to the data volume: `sudo mv /home/ubuntu/.ollama /data/ollama-models`
3. Symlink back: `sudo ln -s /data/ollama-models /home/ubuntu/.ollama`
4. But the ollama service user (`ollama`) cannot access `/home/ubuntu/` — see Pitfall 2
5. Set `OLLAMA_MODELS=/data/ollama-models` in a systemd drop-in instead: `/etc/systemd/system/ollama.service.d/override.conf`

**Prevention:** Always set OLLAMA_MODELS to the data volume BEFORE pulling models. The Deep Learning AMI gives you a 400+ GB ephemeral NVMe at `/data`. Use it.

## Pitfall 2: Ollama service user cannot access ubuntu's home

**Symptom:** `ollama list` shows no models even though `/home/ubuntu/.ollama/models/` has blobs. `ollama pull` re-downloads models that already exist.

**Root cause:** The ollama systemd service runs as user `ollama`. `/home/ubuntu/` has permissions 750. The ollama user cannot traverse it. Even a symlink at `/home/ubuntu/.ollama` is invisible to the ollama user.

**Fix:**
1. Create a systemd drop-in: `/etc/systemd/system/ollama.service.d/override.conf`
2. Add: `[Service]\nEnvironment="OLLAMA_MODELS=/data/ollama-models"`
3. Fix ownership: `sudo chown -R ollama:ollama /data/ollama-models`
4. Reload and restart: `sudo systemctl daemon-reload && sudo systemctl restart ollama`

**Do NOT:** symlink from `/home/ubuntu/.ollama` to `/data/ollama-models`. It will not work for the ollama service user.

## Pitfall 3: Double-nested model directories after file moves

**Symptom:** After moving model files, `ollama list` returns empty. The directory structure has `blobs/blobs/` and `manifests/manifests/` nesting.

**Root cause:** The original `.ollama` directory contains `models/blobs/` and `models/manifests/`. When you copy the CONTENTS of `.ollama` to a new location, you get the `models/` subdirectory too. When OLLAMA_MODELS points to that location, it expects `blobs/` and `manifests/` at the top level, not inside another `models/` directory.

**Fix:**
1. `sudo mv /data/ollama-models/models/blobs /data/ollama-models/blobs`
2. `sudo mv /data/ollama-models/models/manifests /data/ollama-models/manifests`
3. `sudo rmdir /data/ollama-models/models`
4. Repeat for any additional nesting levels
5. Restart ollama

**Prevention:** When moving ollama model storage, move the CONTENTS of `.ollama/` to the new location, not the directory itself. Target structure: `OLLAMA_MODELS/blobs/` and `OLLAMA_MODELS/manifests/`.

## Pitfall 4: Models lost during storage migration need re-pulling

**Symptom:** After fixing directory structure, some models appear but others are missing from `ollama list`.

**Root cause:** Manifest files or blobs for specific models were lost or corrupted during the move. Ollama only lists models with complete manifests.

**Fix:** Simply `ollama pull <model>` for any missing models. The pull is smart — if blobs already exist for that model, it only downloads what is missing. In practice, a "lost" phi4:14b (9.1 GB) re-downloads the full 9.1 GB because the manifest was the missing piece.

## Pitfall 5: Web UI JavaScript calls localhost from the browser

**Symptom:** Chat UI loads but every message returns "Connection lost" or times out. Server-side `curl localhost:11434` works fine.

**Root cause:** The HTML/JS is served from the EC2 but runs in the USER's browser. `fetch('http://localhost:11434/...')` resolves to the USER's laptop, not the EC2. Ollama is not running on the user's laptop.

**Fix:** Do NOT serve a static HTML file that calls Ollama directly from the browser. Instead, build a Python backend proxy:
1. Single Python server that serves the HTML on GET `/` AND proxies POST `/api/chat` to Ollama on localhost
2. JavaScript calls `/api/chat` (same origin, no CORS issues)
3. Python backend handles the Ollama call server-side
4. Pre-load the model at server startup with a warm-up request so first user query is fast

**Pattern:**
```python
class Handler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':  # serve HTML
            ...
        elif self.path == '/health':  # health check
            ...
    
    def do_POST(self):
        if self.path == '/api/chat':  # proxy to Ollama
            payload = json.dumps({...}).encode()
            req = urllib.request.Request('http://localhost:11434/v1/chat/completions', ...)
            with urllib.request.urlopen(req, timeout=120) as resp:
                ...
```

## Pitfall 6: Port 11434 left open creates a zombie ollama process

**Symptom:** After `systemctl stop ollama` or crashes, `systemctl start ollama` fails with "address already in use." The restart counter climbs into the hundreds.

**Root cause:** A previous ollama process is still bound to port 11434. systemd cannot start a new one. The old process may be orphaned from an earlier `ollama serve` run without systemd.

**Fix:**
1. `sudo fuser -k 11434/tcp` — kill whatever is on the port
2. `sudo systemctl restart ollama` — fresh start
3. Verify: `systemctl is-active ollama`

## Quick reference: full recovery sequence

```bash
# 1. Check root disk
df -h /

# 2. Move models to data volume
sudo mkdir -p /data/ollama-models
sudo systemctl stop ollama
sudo mv /home/ubuntu/.ollama/* /data/ollama-models/  # contents only, not the dir itself
sudo rm -rf /home/ubuntu/.ollama

# 3. Fix double-nesting if needed
find /data/ollama-models -type d  # check for models/models/ or blobs/blobs/
# Flatten if nested

# 4. Configure ollama to use data volume
sudo mkdir -p /etc/systemd/system/ollama.service.d
echo '[Service]
Environment="OLLAMA_MODELS=/data/ollama-models"' | sudo tee /etc/systemd/system/ollama.service.d/override.conf
sudo chown -R ollama:ollama /data/ollama-models

# 5. Start ollama
sudo systemctl daemon-reload
sudo systemctl start ollama

# 6. Verify and re-pull lost models
ollama list
ollama pull phi4:14b  # or whatever is missing

# 7. Serve via backend proxy, never static HTML
# Use ap-server.py pattern: serves HTML + proxies /api/chat to ollama
```
