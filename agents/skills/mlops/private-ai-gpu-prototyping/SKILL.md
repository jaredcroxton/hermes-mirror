---
name: private-ai-gpu-prototyping
description: Use when Jared wants to test or explain a private cloud/local AI stack using Ollama, Hermes, EC2 GPU, Lightsail, or client-site hardware. Covers low-cost trial design, AWS EC2 GPU launch checks, cost control, and plain-English product positioning.
version: 1.0.0
author: Brock / PerformOS
created_by: agent
tags: [ollama, ec2, gpu, lightsail, private-cloud, local-ai, performos, aws]
---

# Private AI GPU Prototyping

## Trigger

Use this when Jared asks about:

- running Ollama locally or in AWS
- testing a large local model on EC2 GPU
- comparing Lightsail, EC2 GPU, and client-site Mac options
- setting up a private cloud AI stack for PerformOS
- sizing infrastructure for a 19 GB Ollama model
- keeping cloud testing cheap before committing to monthly spend
- interpreting AWS EC2 launch screenshots for GPU AI testing
- handling new AWS account GPU quota blockers and region restrictions
- storing AWS, EC2, Telegram, and Hermes trial secrets safely during prototyping

## Core judgement

Keep the product story clean:

- **Lightsail** = control layer, dashboards, monitoring, gateways, support, lightweight workloads.
- **EC2 GPU** = private cloud model brain for Ollama and heavier inference.
- **Client-site Mac** = local appliance story for clients who want processing in their office.

Do not blur these. Jared needs the commercial positioning as much as the technical answer.

## Recommended first trial stack

For Jared's first private-cloud Ollama proof:

1. Use **one EC2 GPU server only**.
2. Put **Ollama, the model, Hermes, and one Telegram test bot on the same instance**.
3. Do not add Lightsail until the model performance is proven.
4. Stop the instance when finished testing.

Preferred test instance:

- `g6.2xlarge` if available and affordable
- Deep Learning Base AMI with Single CUDA
- x86 64-bit
- 200 GB storage minimum, but AWS Deep Learning AMIs may add more storage by default
- SSH allowed from **My IP**, not Anywhere
- no inbound rule for Ollama port `11434`

If a cheaper GPU family such as `g6f.2xlarge` appears, check that it genuinely includes a GPU before recommending launch.

## Low-cost testing sequence

Use a staged test. Do not start with a full month.

1. **Four-hour install test**
   - prove GPU is available
   - install Ollama
   - pull the model
   - run one prompt
   - connect Hermes to local Ollama

2. **Eight-hour quality test**
   - test real PerformOS tasks
   - test one agent profile
   - test Telegram if needed
   - judge speed and answer quality

3. **72-hour stability test**
   - only if the quality test passes
   - keep model warm
   - test restarts, logs, and basic health checks

## AWS launch checklist

Before launch, confirm:

- Region matches the test goal. Sydney for Australian-client realism. US East for cheaper proof testing.
- New accounts may only allow launch in US East N. Virginia, US East Ohio, or US West Oregon at first. Do not fight this for the first proof. Use US East N. Virginia if Sydney is blocked.
- AMI is a GPU-ready Deep Learning AMI or equivalent. In US East, **Deep Learning OSS Nvidia Driver AMI GPU PyTorch Ubuntu** is a good option.
- Instance type starts with `g`, such as `g6.2xlarge`. Avoid `m`, `t`, `c`, and `r` for the Ollama GPU test.
- It shows GPU capability, ideally NVIDIA L4 or equivalent with enough GPU memory.
- SSH source is **My IP**.
- HTTP and HTTPS are unchecked unless there is a specific dashboard or web app to expose.
- No inbound Ollama port is opened.
- Storage is large enough for the AMI, Ollama, model files, Hermes, packages, and logs. Do not launch with a 1 GiB root volume just because the form allows it.
- File systems such as EFS, FSx, and S3 Files are not added for the first test.
- A key pair exists before launch. For Jared on Mac, use RSA and `.pem`.

## New AWS account GPU quota blocker

If launch fails with a vCPU quota error for G instances, the account likely has GPU quota set to zero. Route Jared to:

```text
Service Quotas → AWS services → Amazon Elastic Compute Cloud → Running On-Demand G and VT instances
```

For one `g6.2xlarge`, request at least **8 vCPUs**. Prefer **16 vCPUs** because it is still modest and gives room for testing. If AWS asks for justification, say it is a short private AI inference proof-of-concept using Ollama and the instance will be stopped when not actively testing.

## User data startup script

For GPI instances with the Deep Learning AMI, use this `#!/bin/bash` user data script to auto-install Ollama on first boot:

```bash
#!/bin/bash
# Auto-install Ollama on first boot
curl -fsSL https://ollama.com/install.sh | sh
# Pull a lightweight test model
ollama pull llama3.2:3b
```

Paste into the User data field (under Advanced details). No other startup config needed for first test.

## Step-by-step pacing

When walking Jared through AWS console screens or EC2 terminal commands, use ONE instruction per turn. Show only the next step. Never dump multiple steps at once.

Signals: Jared says "step by step", "don't rush", "don't give me a lot of information at once", or "you are losing me."

Good: "Click where it says **AWS services** in the left sidebar."
Bad: "Click AWS services, then search for EC2, then click the quota name, then..."

Let him confirm each step with a screenshot or message before moving to the next.

**Correction (2 Jun 2026):** When explaining Docker, containerd, LVM volumes, and disk mounts, do NOT dump the full technical pipeline. Jared said "you are losing me." Keep it to one action per turn with minimal explanation. Let the terminal output speak for itself. The user does not need to understand Docker internals to deploy Open WebUI.

When a client-facing agent interface is needed, do not explain the full architecture. Just say "here is the URL" and let them use it.

**Correction (2 Jun 2026, disk cleanup):** When Jared says "talk me through" a fix, do exactly that — one step at a time with clear before/after. Show what is using the space, explain the single action, then show the result. Do not chain multiple commands or explain all possible outcomes upfront.

## Cost-control rules

Always frame EC2 as hourly until Jared deliberately chooses always-on.

- Stop the instance when not testing.
- Do not terminate until the trial is fully finished, because termination deletes the server.
- Watch storage and snapshots. They can still cost money after compute is stopped.
- Set AWS billing alerts early.
- Test performance first, architecture second.

## Hermes plus Ollama pattern

When Ollama and Hermes live on the same EC2 server:

```text
Telegram or dashboard
↓
Hermes on EC2
↓
Ollama local API
↓
GPU model
↓
Hermes response back to user
```

Ollama should stay private:

```text
http://127.0.0.1:11434/v1
```

Do not expose Ollama publicly unless there is proper VPN, firewalling, authentication, and a deliberate security design.

## Secrets pattern for trials

Use Bitwarden as the master vault, not as an open vault connected to the agent. Agents get only the specific key needed for a specific task.

Recommended pattern:

```text
Bitwarden master vault
↓
manual copy or controlled deploy script
↓
Hermes .env or profile .env
↓
Hermes uses only that secret
```

For early trials, prefer manual copy over Bitwarden CLI automation. Store AWS account details, EC2 key-pair notes, Telegram bot tokens, Hermes provider keys, GitHub tokens, and recovery codes in Bitwarden. Do not ask Jared for or store Bitwarden master passwords, AWS root passwords, recovery codes, or full-vault access in an agent session.

## Positioning language

For AWS-hosted GPU:

**PerformOS Private Cloud AI Team**

For client-site hardware:

**PerformOS Managed Local Appliance**

Avoid calling AWS EC2 GPU a local appliance. It is private cloud, not physically local to the client.

## AgentOS client deployment pattern (full stack)

When Jared is building a real client deployment (not just a quick test), the full stack runs entirely on one EC2 GPU instance:

```
EC2 GPU instance (g6.2xlarge, L4 GPU)
├── Ollama (GPU model serving on localhost:11434)
├── Hermes (agents, gateway, Telegram connectivity)
├── Open WebUI (ChatGPT-style browser interface on port 8080)
└── Docker containers (Open WebUI runs in Docker)
```

Key rule: **nothing runs on Jared's Mac.** The EC2 is the client's complete private AI server. Jared SSHs in once to configure, then hands the client a URL and a Telegram bot. No desktop, no software installs, no Mac.

Full deployment sequence:

1. Launch EC2 GPU instance (g6.2xlarge with Deep Learning AMI)
2. Mount ephemeral volume if available (see Mounting ephemeral volumes section)
3. Install Ollama, pull model (llama3.1:8b minimum for tool calling)
4. Install Hermes, configure to use Ollama as OpenAI-compatible provider
5. Install Open WebUI via Docker
6. Open port 8080 from security group (My IP for testing, later to client's IP)
7. Configure Telegram bot credentials in Hermes .env
8. Start Hermes gateway service
9. Client receives: browser URL + Telegram bot link

## Mounting ephemeral volumes on EC2

Deep Learning AMIs often include an ephemeral NVMe volume (e.g. 419GB at /dev/nvme1n1) that is pre-formatted as ext4 inside an LVM logical volume. The root volume is typically only 30GB — too small for Docker images, Ollama models, and Open WebUI.

Mount sequence:

```bash
# Find the volume
lsblk -f | grep nvme1n1
# Mount LVM logical volume
sudo mkdir -p /data
sudo mount /dev/vg.01/lv_ephemeral /data
df -h /data
```

Docker data-root relocation (required — Open WebUI Docker build exceeds root capacity):

```bash
sudo systemctl stop docker
sudo mkdir -p /data/docker /data/containerd
sudo rsync -aP /var/lib/docker/ /data/docker/
# Configure Docker data-root
echo '{"data-root":"/data/docker"}' | sudo tee /etc/docker/daemon.json
# Relocate containerd root too
sudo systemctl stop containerd
sudo rsync -aP /var/lib/containerd/ /data/containerd/
# Write minimal containerd config
sudo bash -c 'cat > /etc/containerd/config.toml << EOF
root = "/data/containerd"
EOF'
sudo systemctl start containerd docker
```

## Hermes config for local Ollama

When Hermes shares the same EC2 with Ollama, configure it as a custom OpenAI-compatible provider:

```yaml
model:
  default: "llama3.1:8b"
  provider: "custom"
  base_url: "http://localhost:11434/v1"
```

Do NOT use `provider: ollama` or `provider: auto` — these route differently. Use `provider: custom` with the explicit `base_url`.

The Ollama v1 API is compatible with OpenAI chat completions. Hermes tool calling works with llama3.1:8b and above. llama3.2:3b does NOT support function calling reliably — models must be 8B+ for proper tool use.

## Model selection for agent workloads

- **llama3.2:3b (2GB)** — fast, works for chat, but does NOT support tool calling. Use for Open WebUI only, not Hermes agents. Will not respond to function calls — Hermes chat returns tool JSON instead of text.
- **llama3.1:8b (4.9GB)** — minimum viable agent model. Supports tool calling. Good for basic agent work, Telegram bots, file ops. BUT: system-prompt-heavy agent work (SOUL.md context) often results in hallucination on 8B models. The model may ignore or confabulate the system prompt.
- **phi4:14b (~14GB)** — better reasoning, fits on L4 (23GB VRAM) with headroom. Handles system prompts and SOUL context reliably. Recommended for production agent use.
- **llama3.1:70b (~40GB)** — too large for L4. Needs A10G or A100.

On the g6.2xlarge L4 (23GB VRAM), the sweet spot is 8B-14B models. Keep at least 2GB VRAM free for CUDA overhead.

**Verification pattern:** After pulling a model, test it directly via Ollama API before configuring Hermes. Use curl to the `/v1/chat/completions` endpoint. Verify the model responds with coherent text, not tool JSON or empty responses. Then configure Hermes and test with a simple identity probe.

## Agent soul creation pattern (for client deployments)

When building a specialist agent for a specific business (e.g. AP for Accor Plus):

1. **Scrape the business website** using Firecrawl to extract branding, products, markets, and key facts. Use `formats: ["markdown"]` with `onlyMainContent: true`.

2. **Write the SOUL.md** with these sections:
   - Who the agent is (identity statement)
   - Full business context (scraped facts, numbers, markets, products)
   - How the agent operates (decision-making principles)
   - Key leadership context (who it advises, what they do)
   - Voice and tone

3. **Upload to EC2** and create a Hermes profile:
   ```bash
   scp soul.md ec2:/home/ubuntu/
   hermes profile create <name> --clone
   cp soul.md ~/.hermes/profiles/<name>/SOUL.md
   ```

4. **Configure the profile** to use local Ollama:
   ```python
   c['model']['default'] = 'llama3.1:8b'
   c['model']['provider'] = 'custom'
   c['model']['base_url'] = 'http://localhost:11434/v1'
   ```

5. **Create a browser interface** if the agent needs a visual chat page (see Browser agent interface pattern).

## Browser agent interface pattern

For agents that need a visual chat page without Open WebUI, serve both the HTML and a backend proxy from a single Python server. Do NOT have browser JavaScript call Ollama's API directly — `fetch('http://localhost:11434')` resolves to the client's machine, not the EC2. The page loads but all API calls fail silently.

**Architecture:**
```
Browser → :8090 (public) → Python server → localhost:11434 (Ollama)
  GET /      → serves HTML
  POST /api/chat → proxies to Ollama v1/chat/completions
```

**The Python server must:**
1. Serve the HTML on GET /
2. Proxy POST /api/chat to Ollama (same-origin, no CORS)
3. Pre-warm the model at startup — otherwise the first user query triggers a 10-30 second model load that exceeds browser timeouts

**Serve command:**
```bash
nohup python3 /home/ubuntu/<agent>-server.py > /tmp/<agent>-server.log 2>&1 &
```

See `templates/ec2-agent-chat-server.py` for a complete deployable template. Replace MODEL, PORT, SYSTEM_PROMPT, and HTML per agent.

**The HTML** must include the full system prompt from SOUL.md as the first message in the conversation array. Design matches client brand colors. The JavaScript calls `/api/chat` (same origin), NOT `http://localhost:11434`.

## Open WebUI Docker install

```bash
docker run -d --network host --name open-webui \
  -v /data/open-webui:/app/backend/data \
  -e OLLAMA_BASE_URL=http://127.0.0.1:11434 \
  ghcr.io/open-webui/open-webui:main
```

Runs on port 8080. First user to create an account becomes admin. Open port 8080 in security group for access.

## Client handover

When deployment is complete and tested, the client receives exactly two things:

1. **A URL** — Open WebUI chat interface at their domain or the EC2 public IP:8080
2. **A Telegram bot** — the bot handle they message for agent access

Nothing else. No login credentials. No AWS console access. No terminal. No key files. The EC2 runs 24/7 under PerformOS management.

## Plain-English explanation pattern

When Jared asks what EC2 GPU is, explain it like this:

- Lightsail is a regular rented office computer in the cloud.
- EC2 GPU is a rented workstation or gaming PC in the cloud.
- The GPU is the muscle that makes local AI models respond faster.
- EC2 gives you a server to build on, but AWS charges while it is running.

## Ollama model storage on separate volumes

When the root volume is small (30 GB typical on Deep Learning AMIs) and Ollama pulls large models, the root fills. Move models to the ephemeral data volume.

**The sequence that works:**

```bash
# 1. Stop ollama
sudo systemctl stop ollama

# 2. Move models to data volume
sudo mv /home/ubuntu/.ollama /data/ollama-models

# 3. Symlink for the ubuntu user
sudo ln -s /data/ollama-models /home/ubuntu/.ollama
sudo chown -R ubuntu:ubuntu /data/ollama-models

# 4. Fix the SERVICE user — THIS IS THE TRAP
# The ollama systemd service runs as user 'ollama', not 'ubuntu'.
# The ollama user cannot traverse /home/ubuntu/ (permission denied).
# Symlink in /home/ubuntu/.ollama is INVISIBLE to the service.
# Fix: set OLLAMA_MODELS in a systemd drop-in
sudo mkdir -p /etc/systemd/system/ollama.service.d
echo '[Service]
Environment="OLLAMA_MODELS=/data/ollama-models"' | sudo tee /etc/systemd/system/ollama.service.d/override.conf
sudo chown -R ollama:ollama /data/ollama-models
sudo systemctl daemon-reload
sudo systemctl start ollama
```

**Common traps:**
- Double-nesting: after `mv`, the structure may be `/data/ollama-models/models/blobs/` instead of `/data/ollama-models/blobs/`. Flatten with `mv /data/ollama-models/models/* /data/ollama-models/ && rmdir /data/ollama-models/models`.
- Leftover process: if `systemctl stop` leaves a zombie ollama on port 11434, kill with `sudo fuser -k 11434/tcp`.
- Models disappear: after moving and restarting, `ollama list` may show empty. Check `OLLAMA_MODELS` env var is actually set: `sudo cat /proc/$(pgrep -f "ollama serve")/environ | tr '\0' '\n' | grep OLLAMA`.
- Lost models: if a model disappears after relocation (common with phi4:14b), just `ollama pull <model>` again. Blobs may be cached but manifests were pointing to old paths.

## Chat UI behind Ollama is NOT a Hermes agent

A web page with a system prompt calling Ollama's chat API can TALK. It cannot ACT.

| Architecture | Tools | Result |
|---|---|---|
| HTML → Ollama directly | None | "Here is how you could..." |
| HTML → proxy → Ollama | None | Same — just a chat UI |
| Hermes runtime → Ollama | Terminal, browser, files, web, memory | Actually does the work |

Do not let Jared believe a branded chat page is a deployed agent. To get a real agent, route through Hermes runtime with tool access. The model (Ollama or cloud) provides reasoning. The runtime provides hands. Both are required.

## Pitfalls

- Do not recommend the free-tier EC2 instance for a 19 GB Ollama model. It is usually CPU-only and too small.
- Do not let Jared launch SSH as `Anywhere 0.0.0.0/0` if **My IP** is available.
- Do not open port `11434` to the internet.
- Do not add Lightsail before the EC2 GPU model performance is proven.
- Do not overbuild dashboards, support systems, or multi-agent profiles before confirming the model runs well.
- Do not treat monthly price as the first decision. First test hourly for a few hours.
- Do not move Ollama model storage without setting OLLAMA_MODELS for the systemd service user. The ubuntu user symlink is invisible to the ollama service user.
- Do not ship a branded chat page and call it a deployed agent. A chat UI behind Ollama is a chatbot, not an agent. Hermes runtime is required for tools.

## Reference

See `references/aws-ec2-gpu-ollama-trial.md` for the detailed session-derived trial pattern, screenshot interpretation notes, quota workflow, Bitwarden secret-handling pattern, and cost framing.