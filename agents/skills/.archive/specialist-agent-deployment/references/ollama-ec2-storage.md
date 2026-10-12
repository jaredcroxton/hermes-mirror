# Ollama EC2 Storage Management

## Root disk filling

Ollama models download to `~/.ollama` by default. On EC2 AMIs with small root volumes (30 GB common), a single 9 GB model plus 2-5 GB of other models quickly fills the disk. 100% root = service failure.

## Move models to data volume

EC2 GPU instances include ephemeral NVMe storage (g6.2xlarge has 412 GB at `/data`). Models should live there, not on root.

**Complete move sequence (tested June 2026):**

```bash
# 1. Stop ollama
sudo systemctl stop ollama

# 2. Move models to data volume
sudo mv /home/ubuntu/.ollama /data/ollama-models

# 3. Set OLLAMA_MODELS env var via systemd drop-in
sudo mkdir -p /etc/systemd/system/ollama.service.d
echo '[Service]
Environment="OLLAMA_MODELS=/data/ollama-models"' | sudo tee /etc/systemd/system/ollama.service.d/override.conf

# 4. Fix ownership (ollama service runs as ollama user)
sudo chown -R ollama:ollama /data/ollama-models

# 5. Reload and restart
sudo systemctl daemon-reload
sudo systemctl restart ollama
```

## Double-nesting pitfall

When models are moved from an existing `.ollama` directory, the structure can end up double-nested:

```
/data/ollama-models/blobs/blobs/   ← WRONG
/data/ollama-models/manifests/manifests/   ← WRONG
```

Ollama expects:
```
/data/ollama-models/blobs/
/data/ollama-models/manifests/registry.ollama.ai/
```

**Fix:** Move inner directories up one level and remove empty parents.

```bash
sudo mv /data/ollama-models/blobs/blobs/* /data/ollama-models/blobs/
sudo rmdir /data/ollama-models/blobs/blobs
sudo mv /data/ollama-models/manifests/manifests/* /data/ollama-models/manifests/
sudo rmdir /data/ollama-models/manifests/manifests
```

## Ollama service user permissions

The systemd service runs as user `ollama`, not `ubuntu`. The `ollama` user cannot traverse `/home/ubuntu` if permissions are restrictive (750 or 700). Do not symlink from `/home/ubuntu/.ollama` — use the `OLLAMA_MODELS` environment variable via systemd drop-in instead.

## Port conflict after restart

After stopping ollama, a leftover process may hold port 11434. The systemd service will crash-loop with "address already in use."

```bash
sudo fuser -k 11434/tcp
sudo systemctl restart ollama
```

## Verifying

```bash
ollama list           # models should appear
df -h /               # root should be under 80%
systemctl is-active ollama   # should return "active"
```
