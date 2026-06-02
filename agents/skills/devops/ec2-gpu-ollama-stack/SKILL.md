---
name: ec2-gpu-ollama-stack
description: Cost-controlled AWS EC2 GPU trials for Ollama local-model inference with Hermes agents.
version: 1.0.0
author: Brock / PerformOS
created_by: agent
tags: [aws, ec2, gpu, ollama, hermes, private-cloud, cost-control]
---

# EC2 GPU Ollama Stack

Use this when Jared wants to test or explain running Ollama and Hermes on an AWS GPU server, especially for a large local model such as a 19 GB Ollama model.

## Operating judgement

Do not overbuild the stack before proving the model.

Best first trial:

1. Use **one EC2 GPU instance only**.
2. Run **Ollama and Hermes on the same server**.
3. Keep Ollama private on `127.0.0.1:11434`.
4. Test one model, one Hermes profile, and one Telegram bot.
5. Stop the instance when finished.
6. Add Lightsail later only if a separate always-on control layer is needed.

## Product-language distinction

Use the right label:

- **Local appliance:** model runs on a Mac or server physically at the client site.
- **Private cloud:** model runs on a dedicated cloud GPU server.
- **Hybrid:** Lightsail or another control layer manages a client-site appliance or EC2 GPU model server.

Do not call EC2 GPU “local to the client office.” It is local only to the AWS server.

## Recommended trial shape

For Jared's 19 GB Ollama model, the preferred test instance is:

- **Instance:** `g6.2xlarge`
- **AMI:** Deep Learning OSS Nvidia Driver AMI GPU PyTorch 2.11 (Ubuntu 24.04)
- **AMI search path:** AWS Marketplace AMIs, not Quick Start. Search "Deep Learning OSS Nvidia Driver AMI GPU PyTorch". Pick the **Ubuntu** result (not Amazon Linux). Quick Start may show Ubuntu 26.04 — that does NOT have NVIDIA drivers pre-installed.
- **AMI ID (us-east-1):** `ami-09343c2dd0ee54c92`
- **Storage:** 200 GB minimum if editable; accept larger AMI-required volumes if needed
- **Inbound security:** SSH only, source set to **My IP**
- **Do not open:** Ollama port `11434`
- **File systems:** None

If AWS exposes `g6f.2xlarge` with 8 vCPU, 32 GiB memory, and GPU at materially lower pricing, it can be used for a cost test, but confirm GPU details before launch.

## Region choice

For first proof:

- Prefer **US East, N. Virginia** if AWS restricts a new account to starter regions or if cost matters most.
- Prefer **Sydney** when testing Australian client latency or data-residency positioning.

New AWS accounts may not allow Sydney or GPU launch immediately. If AWS says the region is being validated, do not keep relaunching. Use an allowed starter region or wait for validation.

## Cost-control pattern

Do not start with 24/7 monthly operation.

Run test windows:

1. Four-hour install test
2. Eight-hour quality test
3. 72-hour stability test only if quality passes
4. Monthly always-on only after the model feels sellable

For a scheduled trial window, calculate:

```text
hourly_price × hours_per_day × days
```

Jared's discussed window was **7:00 am to 10:30 pm Sydney time**, which is 15.5 hours per day.

## Launch checklist

Before launch, verify:

- AMI: Deep Learning AMI with CUDA
- Architecture: x86 64-bit for G6
- Instance family: starts with `g6`, not `m`, `t`, `c`, or `r`
- Instance type: preferably `g6.2xlarge`
- SSH: **My IP**, not Anywhere
- HTTP/HTTPS: unchecked unless a dashboard is intentionally being exposed
- Ollama port `11434`: not exposed publicly
- Storage: not a tiny 1 GiB root unless the AMI clearly provisions a separate usable boot/root volume
- File systems: None

## Storage: mount the big secondary volume

The Deep Learning AMI ships with a small root volume (~30 GB) and a large secondary LVM volume (~420 GB) that is NOT auto-mounted. The root volume fills up fast when pulling Docker images and models.

Always mount the secondary volume before installing anything substantial:

```bash
# Find the secondary disk
lsblk

# Check if already formatted (expected: ext4 on /dev/vg.01/lv_ephemeral)
sudo blkid /dev/vg.01/lv_ephemeral

# Mount and persist
sudo mkdir -p /data
sudo mount /dev/vg.01/lv_ephemeral /data
echo '/dev/vg.01/lv_ephemeral /data ext4 defaults,nofail 0 2' | sudo tee -a /etc/fstab
```

## Ollama model storage relocation

Ollama stores models in `~/.ollama` by default. On the Deep Learning AMI, that is `/home/ubuntu/.ollama` on the 30 GB root volume. Multiple models quickly fill this to 100%. Move model storage to the data volume:

```bash
# Stop Ollama first
sudo systemctl stop ollama

# Move models to data volume
sudo mv /home/ubuntu/.ollama /data/ollama-models

# The ollama service runs as user 'ollama', not 'ubuntu'.
# It cannot see /home/ubuntu/.ollama (directory permissions).
# Use a systemd drop-in file to set OLLAMA_MODELS:
sudo mkdir -p /etc/systemd/system/ollama.service.d
cat << 'EOF' | sudo tee /etc/systemd/system/ollama.service.d/override.conf
[Service]
Environment="OLLAMA_MODELS=/data/ollama-models"
EOF

# Fix ownership so ollama user can read/write
sudo chown -R ollama:ollama /data/ollama-models

# Reload and restart
sudo systemctl daemon-reload
sudo systemctl start ollama
```

**Pitfall:** The moved directory may have nested `models/` subdirectories (`blobs/blobs/`, `manifests/manifests/`). Flatten after moving:

```bash
# Check for double-nesting
find /data/ollama-models -maxdepth 3 -type d

# If blobs/blobs/ exists, flatten
sudo mv /data/ollama-models/blobs/blobs/* /data/ollama-models/blobs/ 2>/dev/null
sudo rmdir /data/ollama-models/blobs/blobs 2>/dev/null
sudo mv /data/ollama-models/manifests/manifests/* /data/ollama-models/manifests/ 2>/dev/null
sudo rmdir /data/ollama-models/manifests/manifests 2>/dev/null
```

**Verification:** `ollama list` should show all models. If empty, check `OLLAMA_MODELS` is set in the service environment (`sudo cat /proc/$(pgrep ollama)/environ | tr '\0' '\n'`).

## Docker on the big volume

Docker fills `/var/lib/docker` on the small root volume. After mounting `/data`, move Docker's data root AND containerd's root:

```bash
sudo systemctl stop docker docker.socket containerd
sudo mkdir -p /data/docker /data/containerd

# Move existing data (if any)
sudo rsync -aP /var/lib/docker/ /data/docker/ 2>/dev/null
sudo rsync -aP /var/lib/containerd/ /data/containerd/ 2>/dev/null

# Point Docker to /data
echo '{"data-root":"/data/docker"}' | sudo tee /etc/docker/daemon.json

# Point containerd to /data
sudo bash -c 'cat > /etc/containerd/config.toml' << 'CEOF'
root = "/data/containerd"
CEOF

# Clean root volume and restart
sudo rm -rf /var/lib/docker/* /var/lib/containerd/*
sudo systemctl start containerd docker
```

Pitfall: Docker's `data-root` alone is not enough. `containerd` has its own root directory. Both must move or Docker image extraction fails with "no space left on device."

## Open WebUI for visual demo

For a ChatGPT-style browser interface that runs on the EC2 and connects to local Ollama:

```bash
docker run -d --network host --name open-webui \
  -v /data/open-webui:/app/backend/data \
  -e OLLAMA_BASE_URL=http://127.0.0.1:11434 \
  ghcr.io/open-webui/open-webui:main
```

The container takes ~30 seconds to initialize before port 8080 serves. Open the security group inbound rule for TCP port 8080 from My IP before accessing `http://<public-ip>:8080`.

This gives a visual demo layer that proves the private AI stack to clients without needing a Telegram bot or Hermes gateway.

## Setup commands once connected

Use the actual AMI's package manager and shell, but the basic path is:

```bash
# Check GPU
nvidia-smi

# Mount secondary volume (see Storage section above)

# Install Ollama
curl -fsSL https://ollama.com/install.sh | sh

# Pull and test model
ollama pull <model-name>
ollama run <model-name>

# Install Hermes (includes Python 3.11, uv, Node.js, Playwright)
curl -fsSL https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh | bash

# Reload shell and verify Hermes
source ~/.bashrc
~/.local/bin/hermes --version

# Point Hermes at local Ollama
hermes config set model.base_url http://127.0.0.1:11434/v1
hermes config set model.default <model-name>
hermes config set model.api_key ollama

# Verify end-to-end
hermes chat -q "Reply exactly OK" --quiet
```

## Verification commands

After launch, check real server state:

```bash
nvidia-smi
lsblk
df -h
free -h || vmstat 1 5
curl http://127.0.0.1:11434/api/tags
```

Then run a real quality prompt, not just “hello.” Test:

- strategic recommendation
- document summary
- sales email draft
- training outline
- two or three near-concurrent requests

For Open WebUI verification:

```bash
docker ps --filter name=open-webui --format '{{.Status}}'
curl -s -o /dev/null -w '%{http_code}' http://localhost:8080
```

## Pitfalls

- **Free-tier EC2 is not enough.** Free-tier or low-cost `m`, `t`, `c`, or `r` instances are CPU servers and do not prove the Ollama GPU stack.
- **Windows is the wrong default.** Use Ubuntu or a Deep Learning AMI. Windows adds driver friction, licensing cost, and setup complexity.
- **Lightsail is optional for the first test.** It is useful later as a control layer, but it is not required to run Ollama or Hermes.
- **Do not expose Ollama publicly.** Keep `11434` bound/private. Hermes can call it over `127.0.0.1` when both run on the same EC2 instance.
- **Do not optimise storage into failure.** A 1 GiB root volume is unsafe unless the AMI clearly provides another usable root/working volume. For a serious test, use 100 to 200 GiB root or accept the AMI's required large volume.
- **Stop is not terminate.** Stop the instance between tests to stop compute charges while keeping the disk. Terminate only when finished with the build.
- **EC2 Instance Connect often fails on first launch.** The browser-based SSH client in the AWS console can error with "Failed to connect to your instance." Fall back to local terminal SSH with the `.pem` key file: `ssh -i ~/Downloads/<key>.pem ubuntu@<public-ip>`. This is more reliable.
- **GPU reality for g6.2xlarge.** AWS docs may reference T4 GPUs, but actual g6.2xlarge instances in us-east-1 ship with NVIDIA L4 GPUs (23 GB VRAM, newer architecture, CUDA 13.2). This is an upgrade, not a downgrade. Adjust model size expectations accordingly — an L4 handles 13B models comfortably.
- **First model pull is slow even on GPU.** When pulling a model via user data script, the model is downloaded but not yet loaded into GPU VRAM. The first inference call will load it (10-30 seconds). Subsequent calls are instant. Test with `curl http://localhost:11434/api/generate` to verify readiness.
- **Ollama models fill the small root volume.** The Deep Learning AMI root volume is only ~30 GB. Ollama stores models in `/home/ubuntu/.ollama` by default. Multiple models (phi4:14b at 9.1 GB + llama3.1:8b at 4.9 GB) quickly fill the root disk to 100%, causing service failures. Move model storage to the data volume BEFORE pulling models. See **Ollama model storage relocation** below.
- **The ollama systemd service runs as user `ollama`, not `ubuntu`.** The ollama service cannot access `/home/ubuntu/.ollama` due to directory permissions on `/home/ubuntu` (mode 750). Its own home is `/usr/share/ollama/.ollama`. When relocating model storage, use a systemd drop-in file to set `OLLAMA_MODELS` rather than symlinking in ubuntu's home directory — the symlink will be invisible to the ollama service user.
- **Directory nesting breaks model discovery.** When moving models from one location to another, the internal `models/` subdirectory inside Ollama's storage creates double-nesting: `blobs/blobs/` and `manifests/manifests/`. After moving, flatten the structure so `blobs/` and `manifests/` sit directly inside the target directory. Verify with `find <target> -maxdepth 3 -type d`.
- **Leftover Ollama process blocks restart.** If `ollama serve` was started manually (e.g. during testing), the systemd service fails with `bind: address already in use` on port 11434. Kill the leftover process with `sudo fuser -k 11434/tcp` before restarting the service.
- **Docker image extraction fails on root volume.** The root volume is only ~30 GB. Docker images for Open WebUI exceed this. Mount the secondary 420 GB LVM volume first, then move both Docker's data-root AND containerd's root to it (see Storage section). Moving only Docker's data-root is insufficient — containerd has its own storage path.
- **Open WebUI takes 30+ seconds to be ready.** After `docker run`, the container needs ~30 seconds to initialize its database before port 8080 responds. `docker ps` shows "health: starting" during this time. Wait for "healthy" before testing with curl.
- **"Connection lost. Is Ollama running?" loop (agent chat page).** The browser chat page shows this in a loop. Diagnose in order: (1) Model not pre-loaded — Ollama unloads models from GPU when idle, and the first query after idle triggers a 10-30 second load that exceeds browser fetch timeouts. Fix: pre-warm the model in the Python proxy server startup before `serve_forever()`. (2) JavaScript `fetch` pointing at `localhost:11434` — resolves to user's machine, not EC2. Fix: use `/api/chat` same-origin proxy pattern. (3) Ollama service actually crashed — check `systemctl is-active ollama` and `sudo journalctl -u ollama --no-pager -n 5`. (4) Model lost during storage move — `ollama list` shows it missing, `curl localhost:11434/api/chat` returns "model not found". Fix: re-pull the model and verify it shows in `ollama list`.
- **Models vanish after storage relocation.** If `ollama list` shows fewer models after moving storage, the directory structure was nested during the move. Flatten `blobs/blobs/` and `manifests/manifests/` into direct children of the target directory. If models still missing after flattening, re-pull — the blobs may have silently not copied correctly during the timed-out move.

## Quota check before launch

New AWS accounts start with 0 vCPUs for GPU instances. Always check before attempting launch:

1. AWS console → search **Service Quotas**
2. Left sidebar → **AWS services**
3. Find or search **Amazon Elastic Compute Cloud (Amazon EC2)**
4. In the quota list, search **G and VT**
5. Select **Running On-Demand G and VT instances**
6. Check **Applied account-level quota value** — must be at least 8 for `g6.2xlarge`
7. If 0, request increase with justification: "Short proof-of-concept AI inference workload using Ollama on one g6.2xlarge instance. Instance will be stopped when not actively testing."

## User data startup script

When launching the EC2 instance, paste this into the **User data** field under Advanced details to auto-install Ollama on first boot:

```bash
#!/bin/bash
# Auto-install Ollama on first boot
curl -fsSL https://ollama.com/install.sh | sh
# Pull a lightweight test model
ollama pull llama3.2:3b
```

For production or heavier testing, replace `llama3.2:3b` with `llama3.1:8b` or the target model.

## Ollama API verification

After SSH in, verify Ollama is running and can serve inference:

```bash
# Check server process
pgrep -a ollama

# Check GPU visible to Ollama
nvidia-smi --query-gpu=utilization.gpu,memory.used --format=csv,noheader

# Test API directly
curl -s http://localhost:11434/api/generate \
  -d '{"model":"llama3.2:3b","prompt":"Say hello","stream":false}' \
  | python3 -c 'import sys,json; d=json.load(sys.stdin); print(d.get("response","NO RESPONSE"))'
```

## Supporting references

- `references/aws-ec2-gpu-ollama-trial-notes.md` captures session-specific pricing, screenshots, and launch decisions from Jared's first EC2 GPU/Ollama trial path.

## Agent deployment: private AI team on EC2

After the base stack is running (Ollama + Hermes), deploy named specialist agents as Hermes profiles. This is the core delivery mechanism for the AgentOS $4,999/month package.

### Profile creation pattern

```bash
# Create a profile
hermes profile create <agent-name> --clone

# Copy the specialist SOUL to the profile
cp /path/to/<agent>-soul.md ~/.hermes/profiles/<agent-name>/SOUL.md

# Wire profile to Ollama (same endpoint, correct model)
cd ~/.hermes/profiles/<agent-name>
python3 -c "
import yaml
with open('config.yaml') as f:
    c = yaml.safe_load(f)
c['model']['default'] = '<model>'
c['model']['provider'] = 'custom'
c['model']['base_url'] = 'http://localhost:11434/v1'
yaml.dump(c, open('config.yaml','w'), default_flow_style=False, sort_keys=False, width=120)
"
```

### Model selection for agent work

**Critical distinction:** Ollama serves a language model — it predicts text. It does not provide an agent runtime. A model alone has no tools, no file system, no browser, and no memory. It can ONLY generate text. When a model responds with "Here is how you could..." instead of actually doing the thing, that is the correct behaviour of a raw model. To get an agent that acts (runs commands, opens browsers, writes files, deploys dashboards), the model must be routed through Hermes, which provides the tool runtime. A model behind a chat UI with a system prompt is a chatbot. A model behind Hermes with tools, skills, and profiles is an agent.

Not all models handle system prompts equally well on local GPU:

- **phi4:14b** — best choice for agent work on L4 GPU (23GB VRAM). Handles system prompts, SOUL context, and multi-turn conversations reliably. ~9GB download.
- **llama3.1:8b** — lighter, faster, but unreliable with long system prompts. Hallucinates context. Use for simple tasks or quick tests.
- **llama3.2:3b** — too small for serious agent work. Use only for API verification.

### Agent chat HTML page (client-facing)

When a client needs a branded browser interface for a specific agent, build a self-contained HTML page served from a Python backend proxy. Do NOT have the browser JavaScript call Ollama's API directly — `fetch('http://localhost:11434')` resolves to the client's machine, not the EC2. The page loads but all API calls fail silently or time out.

**Architecture:**
```
Browser ──► :8090 (public) ──► Python server ──► :11434 (localhost, Ollama)
               │                      │
               GET / → HTML           POST /api/chat → Ollama API
```

**The Python server must do three things:**
1. Serve the HTML on GET /
2. Proxy POST /api/chat to Ollama on localhost (same-origin, no CORS issues)
3. Pre-warm the model at startup (send a ping through Ollama API before `serve_forever()`) — otherwise the first user query triggers a 10-30 second model load that exceeds browser timeouts and causes "Connection lost" loops

**Serve command:**
```bash
nohup python3 /home/ubuntu/ap-server.py > /tmp/ap-server.log 2>&1 &
```

See `references/ec2-proxy-server-template.py` for a complete deployable template.

**Single monolithic HTML file** with inline CSS/JS, embeds the agent's system prompt (SOUL summary) as initial conversation context. Design matches client brand colors. The JavaScript calls `/api/chat` (same origin), NOT `http://localhost:11434`.
