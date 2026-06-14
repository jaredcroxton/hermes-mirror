---
name: nemoclaw-hermes-setup
description: "Install, configure, and uninstall NVIDIA NemoClaw with Hermes Agent sandboxes on macOS. Covers provider selection, non-interactive onboarding, Docker prerequisites, common pitfalls, and the Brev cloud escape hatch."
version: 1.0.0
author: Brock
license: MIT
platforms: [macos, linux]
---

# NemoClaw Hermes Setup

Install and configure NVIDIA NemoClaw with the Hermes Agent inside an OpenShell sandbox. Use this skill when Jared wants to set up, test, or remove a Hermes sandbox via NemoClaw — whether on a MacBook (control layer) or a dedicated AI appliance (DGX Spark / cloud instance).

## Quick Reference

| What | Command |
|------|---------|
| Install NemoHermes | `curl -fsSL https://www.nvidia.com/nemoclaw.sh \| bash && nemoclaw onboard --agent hermes` |
| List sandboxes | `nemoclaw list` |
| API health (Hermes) | `curl -sf http://127.0.0.1:8642/health` |
| Connect terminal | `nemoclaw <name> connect` |
| Hermes status (inside sandbox) | `hermes status` |
| Hermes interactive chat (inside sandbox) | `hermes` |
| Pair Telegram (inside sandbox) | `hermes pairing list` then `hermes pairing approve telegram <CODE>` |
| Logs | `nemoclaw <name> logs --tail 50` |
| Destroy sandbox | `nemoclaw <name> destroy` |
| Uninstall NemoClaw | See Clean Uninstall section |
| Dashboard URL | OpenClaw only: `nemoclaw <name> dashboard-url --quiet`. Hermes has no web dashboard — use API (port 8642) or Telegram bot. |

## Prerequisites

### Docker Desktop

- Docker Desktop or Colima must be running.
- **macOS:** Start Docker Desktop from Applications before running the installer.
- **Memory:** Allocate at least **12GB** to Docker Desktop. 8GB is too little for Hermes sandbox builds and will stall.
- **Disk:** 20GB minimum; 40GB recommended.

### Inference Provider

NemoHermes supports these providers during onboarding:

| Provider | Label in wizard | Auth |
|----------|----------------|------|
| `build` | NVIDIA Endpoints | `NVIDIA_API_KEY` (nvapi-*) |
| `openai` | OpenAI | `OPENAI_API_KEY` |
| `anthropic` | Anthropic | `ANTHROPIC_API_KEY` |
| `gemini` | Google Gemini | `GEMINI_API_KEY` |
| `hermesProvider` | Hermes Provider | OAuth or API key |
| `ollama` | Local Ollama | none (localhost) |
| `custom` | OpenAI-compatible endpoint | `COMPATIBLE_API_KEY` |

### Provider selection rules

- **NVIDIA Endpoints (`build`)** is the recommended provider for NemoHermes. It routes through `https://integrate.api.nvidia.com/v1` and uses the `nvapi-*` key format. Default model: `nvidia/nemotron-3-super-120b-a12b`.
- **Hermes Provider is currently broken** inside NemoClaw sandboxes. OAuth browser approval completes, but credential preparation fails with: `session_key_minting_retired: Hermes Agent session key minting has been retired. Please update Hermes Agent to the latest version and sign in again.`
- **Ollama** works but is not recommended for NemoHermes. It installs via Homebrew, pulls a local model, but does not exercise the cloud inference path NemoClaw was designed for. Use only as a fallback smoke test.

## Non-Interactive Onboarding

Skip the wizard prompts for CI or scripted installs:

```bash
export NEMOCLAW_NON_INTERACTIVE=1
export NEMOCLAW_ACCEPT_THIRD_PARTY_SOFTWARE=1
export NEMOCLAW_FRESH=1
export NEMOCLAW_PROVIDER=build
export NEMOCLAW_MODEL='nvidia/nemotron-3-super-120b-a12b'
export NEMOCLAW_SANDBOX_NAME='hermes-agent'
export NEMOCLAW_RESOURCE_PROFILE=default
export NEMOCLAW_IGNORE_RUNTIME_RESOURCES=1
export NVIDIA_API_KEY='nvapi-...'
nemoclaw onboard --agent hermes
```

Key env vars:

| Variable | Purpose |
|----------|---------|
| `NEMOCLAW_NON_INTERACTIVE=1` | Skip all prompts |
| `NEMOCLAW_ACCEPT_THIRD_PARTY_SOFTWARE=1` | Accept license |
| `NEMOCLAW_FRESH=1` | Discard any failed previous onboarding |
| `NEMOCLAW_PROVIDER` | `build`, `openai`, `anthropic`, `gemini`, `hermes-provider`, `ollama`, `custom` |
| `NEMOCLAW_MODEL` | Exact model ID (e.g. `nvidia/nemotron-3-super-120b-a12b`) |
| `NEMOCLAW_SANDBOX_NAME` | 1-63 chars, lowercase, hyphens allowed |
| `NEMOCLAW_RESOURCE_PROFILE` | `default`, `creator`, `gamer`, `game-developer`, `developer`, `custom` |
| `NEMOCLAW_IGNORE_RUNTIME_RESOURCES=1` | Suppress under-provisioned runtime warning |

## Interactive Onboarding Quick-Skip Guide

When running NemoHermes interactively (non-CI), use these defaults. On a fresh machine the official quickstart is still valid:

```bash
export NEMOCLAW_AGENT=hermes
curl -fsSL https://www.nvidia.com/nemoclaw.sh | bash
```

If the installer has already installed `nemohermes` and a retry is needed, do **not** keep rerunning the full curl installer. Use the installed CLI directly:

```bash
export PATH="/home/shadeform/.local/bin:$PATH"
export NEMOCLAW_AGENT=hermes
nemohermes onboard --fresh
```

| Prompt | Action | Reason |
|--------|--------|--------|
| License / third-party notice | Type the full word `yes` | `y` cancels the installer |
| Resume or fresh | Type `f` | Avoids failed-session state |
| Inference provider | Type `1` (NVIDIA Endpoints) | Cloud inference, no local model needed |
| API key | Paste `nvapi-...` | Staged in process memory only, not written to disk |
| Model | Type `1` (Nemotron 3 Super 120B) | NVIDIA model with working Hermes tool compatibility |
| Sandbox name | Type lowercase hyphenated name like `my-assistant` | No spaces or capitals. `My assistant` is invalid |
| Apply configuration | Type `y` | Messaging prompts come after this |
| Messaging channels | Press `1`, then Enter | This toggles Telegram on. Pressing Enter first skips Telegram |
| Telegram bot token | Paste BotFather token | OpenShell masks it; Hermes sees `openshell:resolve:env:TELEGRAM_BOT_TOKEN` |
| Reply only when @mentioned? | Type `Y` | Good default for business/group-chat use |
| Telegram User ID | Enter the correct numeric user ID | This controls who can DM the bot |
| Resource profiles | Type `6` then Enter (no profile) | Sandbox uses cloud inference, doesn't need resource caps. Blank Enter can fail |
| Policy tier | Balanced for normal use; Restricted for governance stress tests only | Balanced avoids unnecessary friction while preserving useful controls |
| Policy presets | Ensure Telegram, NVIDIA, nous-code, nous-web, github, npm as needed | Match the agent's required external services |

### Hermes agent selection

The current official quickstart uses `NEMOCLAW_AGENT=hermes` with the installer. Use that path first because it matches NVIDIA's docs and the Patrick Moorhead / NVIDIA walkthrough. If using the lower-level CLI directly and an `--agent hermes` flag is available in the installed version, it is also acceptable.

Evidence of the correct Hermes build:
- Dockerfile uses: `COPY agents/hermes/plugin/`, `COPY agents/hermes/generate-config.ts`, `COPY agents/hermes/start.sh`
- Config generated: `/sandbox/.hermes/config.yaml` with Hermes schema
- Entrypoint: `["/usr/local/bin/nemoclaw-start"]`
- Terminal access shows the `hermes` command inside the sandbox

**If you already onboarded with the wrong command or bad Telegram details**, destroy and rebuild:

```bash
nemohermes <sandbox-name> destroy
export NEMOCLAW_AGENT=hermes
nemohermes onboard --fresh
```

For the full Brev clean-retry prompt flow, see `references/brev-nemohermes-clean-onboarding-2026-06-14.md`.

## Common Pitfalls

### 1. Docker pull stalls on GHCR image

The Hermes sandbox base image (`ghcr.io/nvidia/nemoclaw/hermes-sandbox-base:v0.0.55`) is ~1.3GB compressed with a 1.1GB single layer. On macOS with Docker Desktop, this pull frequently stalls without completing — even with adequate memory.

**Symptoms:**
- `docker pull` hangs at "Pulling fs layer" for 10+ minutes
- `skopeo copy` stalls on the large layer
- Local `docker build` stalls at `npm ci`

**Fix:** Do not chase the local pull. Use NVIDIA Brev (`https://brev.nvidia.com`) to spin up a cloud instance. Run NemoHermes there. The MacBook remains the control surface.

### 2. Docker memory too low

Docker Desktop defaults for macOS may allocate only 8GB. Hermes sandbox builds need more.

**Symptoms:**
- Onboarding warns: "Container runtime under-provisioned: 10 vCPU / 7.8 GiB detected"
- Build stalls without error at npm/uv layers
- Docker disk stops growing

**Fix:** Docker Desktop → Settings → Resources → Advanced → Memory: **12GB** → Apply & Restart.

### 3. Resource profile selection fails on blank input

In interactive mode, pressing Enter at the resource profile prompt without choosing a number causes: `Invalid resource profile selection ''. Choose a number from 1 to 6.`

**Fix:** Set `NEMOCLAW_RESOURCE_PROFILE=default` in non-interactive mode. In interactive mode, type `6` (or the desired number) then Enter.

### 4. Hermes Provider OAuth retired

Choosing Hermes Provider → Nous Portal OAuth → browser approval succeeds, but credential setup fails.

**Fix:** Use NVIDIA Endpoints (`build`) provider instead.

### 5. Port 8642 (API) not responding — Hermes sandbox

The Hermes API is on port 8642 only. There is no web dashboard on port 18789 for Hermes sandboxes.

**OpenClaw sandboxes** (without `--agent hermes`): Port 18789 serves the OpenClaw Gateway Dashboard. Port 8642 is not used.

**Hermes sandboxes** (with `--agent hermes`): Port 8642 serves the OpenAI-compatible API. Port 18789 is not used.

These ports are only active after a sandbox is created. If `nemoclaw list` shows no sandboxes, neither port will respond.

**Fix:** Complete onboarding through step 8/8. Verify with `nemoclaw list`. Then test port 8642: `curl -sf http://127.0.0.1:8642/health`.

## Clean Uninstall

Remove everything NemoClaw installed, including dependencies:

```bash
# Kill processes
pkill -f openshell-gateway
pkill -f ollama-auth-proxy
pkill -f 'ollama serve'

# Remove binaries
rm -f ~/.local/bin/nemohermes ~/.local/bin/nemoclaw ~/.local/bin/openshell* \
      ~/.npm-global/bin/nemoclaw ~/.npm-global/bin/nemohermes

# Remove npm packages
npm uninstall -g nemoclaw

# Remove state and source
rm -rf ~/.local/state/nemoclaw ~/.nemoclaw \
       ~/.local/share/openshell ~/.ollama

# Remove Ollama if installed
brew uninstall --ignore-dependencies ollama

# Remove skopeo if installed
brew uninstall --ignore-dependencies skopeo

# Clean Docker (including anonymous volumes)
docker system prune -a -f --volumes

# Clean installer artifacts
rm -rf ~/Desktop/hermes_builds/nemoclaw-install
```

### 6. Brev "No stop/start" instances lose data on stop

Some Brev pre-release instances (notably MASSEDCOMPUTE) carry a "No stop/start" warning. These instances cannot be paused — when stopped, they are destroyed and all data is lost. This is fine for short validation sessions but fatal for multi-session work.

**Fix:** Treat these as disposable test instances only. Do not leave important state on them. For multi-session work, use a Brev instance without the "No stop/start" flag, or migrate to a DGX Spark / dedicated appliance.

### 7. Cloud firewall blocks Docker bridge to OpenShell gateway

On cloud instances (Brev, AWS, etc.), the host firewall may block the Docker bridge network from reaching the OpenShell gateway on port 8080. Preflight checks pass because Docker and the GPU are fine, but sandbox creation fails at step 2/8.

**Symptoms:**
- Preflight checks all pass (Docker, GPU, memory, ports)
- Error: `Sandbox containers cannot reach the gateway at host.openshell.internal:8080 (172.18.0.1:8080)`
- Installer suggests: `sudo ufw allow from 172.18.0.0/16 to 172.18.0.1 port 8080 proto tcp`

**Fix:**
```bash
sudo ufw allow from 172.18.0.0/16 to 172.18.0.1 port 8080 proto tcp
```
Then rerun `nemoclaw onboard`. The firewall rule is idempotent — running it again on retry does no harm.

### 8. Stale gateway process from failed prior onboarding

If a previous onboarding run failed partway through, a stale openshell process or user service may keep listening on the gateway port and block the next attempt.

**Symptoms:**
- Onboarding reports: `Port 8080 is not available. Blocked by: openshell (PID NNNNN)` or the same on port 8081
- The previous gateway is marked as stale: `Existing OpenShell Docker-driver gateway is stale`
- Killing one PID works briefly, then a new PID appears on the same port

**Fix sequence:**
```bash
systemctl --user stop openclaw-gateway.service 2>/dev/null
systemctl --user disable openclaw-gateway.service 2>/dev/null
sudo killall openshell openshell-gateway 2>/dev/null
sudo lsof -i :8080
```

If a PID still appears:
```bash
sudo kill -9 <PID>
```

If port 8080 keeps respawning, switch to 8081 and open the matching firewall rule:
```bash
export NEMOCLAW_AGENT=hermes
export NEMOCLAW_GATEWAY_PORT=8081
sudo ufw allow from 172.18.0.0/16 to 172.18.0.1 port 8081 proto tcp
nemohermes onboard --fresh
```

**Important retry rule:** after `nemohermes` is installed, do not keep rerunning `curl | bash`. The installer's upgrade stage can start the gateway, then onboarding sees that same gateway as a port conflict. Retry with `nemohermes onboard --fresh` directly.

### 9. Hermes sandbox has NO web dashboard (OpenClaw difference)

When using `--agent hermes`, the sandbox does NOT expose an OpenClaw-style web dashboard on port 18789. Running:

```bash
nemoclaw hermes dashboard-url --quiet
```

Returns:

```text
dashboard-url is not applicable for sandbox 'hermes': it uses the 'hermes' agent,
which does not expose an OpenClaw dashboard URL.
```

**What Hermes exposes instead:**

| Interface | Port | How to access |
|-----------|------|---------------|
| Hermes web dashboard | 9119 | Only inside sandbox. On cloud instances, NOT forwarded to host. |
| OpenAI-compatible API | 8642 | `curl http://127.0.0.1:8642/v1/chat/completions` or any OpenAI client pointed at this base URL |
| Telegram bot | via api.telegram.org | Configured during onboarding. Requires `hermes pairing approve telegram <CODE>` inside the sandbox. |
| Interactive shell | via `nemoclaw hermes connect` | Drops into `sandbox@<container-id>:~$` for CLI access. Type `hermes` to start chat. |

**Critical port note:** The Hermes web dashboard is at port **9119**, not 18789 (18789 is OpenClaw only). On cloud instances with Docker bridge networking, the dashboard binds to `127.0.0.1` inside the container by default. Use `--insecure` to bind to `0.0.0.0`, making it reachable via a `socat` bridge from the host. This flow is proven working:

**Inside the sandbox:**
```bash
nemoclaw hermes connect
hermes dashboard --insecure --tui &
```

**On the host:**
```bash
SANDBOX=$(docker ps --format '{{.Names}}' | grep openshell-hermes)
SANDBOX_IP=$(docker inspect "$SANDBOX" --format '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}')
socat TCP-LISTEN:9119,bind=127.0.0.1,fork,reuseaddr TCP:$SANDBOX_IP:9119 &
```

**From local Mac:**
```bash
ssh -o StrictHostKeyChecking=no -L 9119:127.0.0.1:9119 shadeform@<instance-ip>
```
Then open `http://127.0.0.1:9119` in Chrome. On a local macOS machine (no Docker bridge), skip the socat step — the dashboard is directly reachable at `http://127.0.0.1:9119`.

**To verify Hermes is alive (API test):**

```bash
curl -s http://127.0.0.1:8642/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer test" \
  -d '{"model": "nvidia/nemotron-3-super-120b-a12b", "messages": [{"role": "user", "content": "Say hello"}]}'
```

A successful response confirms the Hermes agent, model, and inference route are all working.

**To verify Hermes status (inside sandbox):**

```bash
nemoclaw hermes connect
hermes status
```

This shows: model, provider, API key status, messaging platform configuration, gateway PID, active sessions, and scheduled jobs.

**To pair Telegram after onboarding:**

The bot token is configured during onboarding, and the bot will poll the Telegram API and receive messages (visible in `nemoclaw hermes logs --tail 50`). However, the bot will not respond until your Telegram account is paired.

```bash
nemoclaw hermes connect
hermes pairing list                  # Check for pending pairings
```

The user sends `/pair` to the bot on Telegram. If the bot does not register the `/pair` command and `hermes pairing list` shows "No pairing data found", the pairing config may need host-side setup via `nemoclaw onboard --resume`.

If a pairing code appears:
```bash
hermes pairing approve telegram <CODE>
```

After pairing, the bot will respond to messages. The `hermes pairing` commands are:
- `list` — Show pending and approved users
- `approve <platform> <code>` — Approve a pairing code
- `revoke <USER>` — Revoke a user's access
- `clear-pending` — Clear all pending codes

Note: `hermes telegram pair` is NOT a valid command. The pairing system uses `hermes pairing` with subcommands, not `hermes telegram`.

**Cloud instance access for Hermes (not dashboard, but API + shell):**

When running on a Brev cloud instance, forward port 8642 for API access and connect for shell:

```bash
# On local Mac:
ssh -o StrictHostKeyChecking=no -L 8642:127.0.0.1:8642 shadeform@<instance-ip>
```

Then from the SSH session:
```bash
nemoclaw hermes connect   # interactive shell
# Or from local Mac directly:
curl http://127.0.0.1:8642/v1/chat/completions ...
```

The Telegram bot works without port forwarding — it polls `api.telegram.org` from inside the sandbox. After pairing, messages flow through regardless of where you access the bot from.

### 9a. Dashboard URL is localhost-only on cloud instances (OpenClaw sandboxes only)

This pitfall applies to **OpenClaw** sandboxes, not Hermes. OpenClaw sandboxes (`nemoclaw onboard` without `--agent hermes`) expose a web dashboard at port 18789. `nemoclaw <name> dashboard-url --quiet` returns `http://127.0.0.1:18789/...`.

**What does NOT work:**
- Opening `http://127.0.0.1:18789/` in your local Chrome
- `pip install localtunnel && lt --port 18789` — the `localtunnel` package is not available via pip on Brev instances
- `./ngrok http 18789` — ngrok v3 requires a verified account and authtoken; not usable without signup

**Fix A: Brev "Share a Service" (try first)**

Some providers allow it. Some do not.

1. Go to the **Brev Console** tab in Chrome (the tab labeled "Console | Brev").
2. Scroll to **"Share a Service"**. If a service already exists for port 8888 (Jupyter), look for an **"Add"** or **"+"** button to add another.
3. Add a new service with port `18789`.
4. If successful, Brev generates a public `brevlab.com` URL. Open that URL.

**Provider limitation:** The MASSEDCOMPUTE (shadeform) provider shows "This cloud provider doesn't allow the modifications of ports" in the "Using Ports" section and may block adding new shared services beyond the pre-provisioned Jupyter one. If "Share a Service" does not show an Add button or refuses the port, fall through to Fix B.

**Fix B: SSH tunnel from local Mac (reliable fallback)**

This works on ANY cloud instance regardless of provider port restrictions.

On the cloud instance (via Jupyter Terminal), enable password authentication and set a password:

```bash
sudo sed -i 's/^PasswordAuthentication no/PasswordAuthentication yes/' /etc/ssh/sshd_config
sudo sed -i 's/^#PasswordAuthentication yes/PasswordAuthentication yes/' /etc/ssh/sshd_config
echo -e '<password>\n<password>' | sudo passwd shadeform
sudo systemctl restart sshd
```

On the local Mac terminal:

```bash
ssh -o StrictHostKeyChecking=no -L 18789:127.0.0.1:18789 shadeform@<instance-ip>
```

Enter the password. Once connected, open Chrome on the Mac and go to:

```
http://127.0.0.1:18789/
```

Use the full tokenized URL from `nemoclaw hermes-sandbox dashboard-url --quiet` if the dashboard requires authentication. The SSH tunnel forwards the remote port 18789 to the local machine — Chrome sees it as localhost.

**Finding the Brev Console tab:** In a session with many Chrome tabs, the Brev Console tab may be buried. Look for a tab with a green Brev/NVIDIA favicon titled "Console | Brev" or "famous-aqua-..." (the instance name). It is the same tab where the instance was created.

### 10. SSH password authentication disabled on cloud instances

Most Brev cloud instances have `PasswordAuthentication no` in `/etc/ssh/sshd_config`. Direct `ssh shadeform@<ip>` fails with `Permission denied (publickey)` even after setting a password.

**Symptoms:**
- `ssh shadeform@<ip>` returns `Permission denied (publickey)`
- Password prompt never appears

**Fix (run from Jupyter Terminal):**
```bash
sudo sed -i 's/^PasswordAuthentication no/PasswordAuthentication yes/' /etc/ssh/sshd_config
sudo sed -i 's/^#PasswordAuthentication yes/PasswordAuthentication yes/' /etc/ssh/sshd_config
echo -e '<password>\n<password>' | sudo passwd shadeform
sudo systemctl restart sshd
```
Then SSH with the password from the local Mac.

### 12. Sandbox is locked down — no pip, no sudo, no pipx

The OpenShell sandbox is a hardened container. It intentionally blocks system-level package installation:

- `pip3 install <pkg>` fails with `externally-managed-environment` (PEP 668)
- `pipx` is not installed
- `sudo` does not exist
- `apt` is not available

**Why:** This is the sandbox security model working as designed. You cannot swap agent runtimes after the sandbox is built. If OpenClaw was baked into the Docker image, you cannot manually `pip install hermes-agent` to replace it.

**The only correct path:** Rebuild the sandbox from scratch with the right agent flag:

```bash
nemoclaw <sandbox> destroy
nemoclaw onboard --agent hermes
```

Do not waste time trying to install packages inside a running sandbox. The `--agent hermes` flag at build time selects `agents/hermes/Dockerfile` which bakes Hermes into the image. Post-build modification is not supported.

### 14. Gateway restart and stop operations take 10+ minutes

Inside the sandbox, `hermes gateway restart` can time out with `Timeout - denying command`. Following up with `hermes gateway stop` also triggers a long-running operation — the progress bar may show 11 minutes total with several minutes remaining at 15% completion. These are not hangs or freezes; they are slow Docker container lifecycle operations inside the OpenShell sandbox.

**Symptoms:**
- `hermes gateway restart` shows `Timeout - denying command` followed by `hermes gateway restart 60.0s [error]`
- `hermes gateway stop` shows a progress bar: `[ | ] 15% 11m 0s total, 7m 35s remaining`
- The terminal appears stuck but the operation is still running

**Fix:** Let the operation complete. Do not kill it, do not Ctrl+C, do not open another terminal to force-kill the process. Premature termination can leave the gateway in an inconsistent state requiring a full sandbox destroy and rebuild. If the gateway stop completes normally, the sandbox can be restarted with `nemoclaw <name> restart` from the host.

`nemoclaw <sandbox> connect` drops you into an interactive shell inside the sandbox container. The prompt changes to `sandbox@<container-id>:~$`. After this point, all commands run inside the sandbox — they have access to sandbox-local files, processes, and Python/pip installations.

**Common trap:** Running a command chain that exits or fails silently drops you back to the host shell (`shadeform@shadecloud:~$`). A `kill` command targeting a sandbox process from the host will fail with `No such process`. A `which openclaw` on the host will find nothing even though `/usr/local/bin/openclaw` exists inside the sandbox.

**Symptoms:**
- `kill <PID>` returns `bash: kill: (<PID>) - No such process` when the PID exists inside the sandbox
- `which openclaw` returns nothing on the host but the process is visible from inside the sandbox
- Commands referencing sandbox paths or processes fail unexpectedly

**Fix:** Always check the prompt. If it says `shadeform@shadecloud:~$`, you are on the host. Run `nemoclaw <sandbox> connect` again to re-enter the sandbox. Inside the sandbox, the prompt is `sandbox@<container-id>:~$`.

The `nemoclaw <sandbox> connect` command does not accept `--` to pass inline commands to the sandbox shell. This syntax works in Docker (`docker exec <container> -- <cmd>`) but not in NemoClaw.

**Symptoms:**
- `nemoclaw hermes-sandbox connect -- bash -c 'openclaw dashboard'` fails with: `Unknown flag for connect: --`
- The `--probe-only` flag is the only supported option.

**Fix:** Use `nemoclaw <sandbox> connect` to drop into an interactive sandbox shell, then run commands directly. Or use `docker exec <sandbox-container> <cmd>` directly if the container name is known.

## Model Compatibility & Switching

Change the model after onboarding:

```bash
nemohermes inference set --model nvidia/nemotron-3-super-120b-a12b --provider nvidia-prod --sandbox hermes --no-verify
```

Use `--no-verify` if credential verification fails mid-session (common on cloud instances).

### Model compatibility matrix

| Model | Status | Notes |
|-------|--------|-------|
| `nvidia/nemotron-3-super-120b-a12b` | ✅ Recommended | Full tool support, no validation errors |
| `openai/gpt-oss-120b` | ❌ Avoid | Rejects Hermes tool descriptions: `ToolDescription validation error: Input should be a valid string [type=string_type, input_value=None]` |
| Other NVIDIA Endpoints models | ⚠️ Test early | Tool compatibility varies; validate before relying |

## Policy Presets Reference

When selecting policies during onboarding:

- **Restricted** — nothing enabled by default. Toggle presets manually. Use for enterprise demos to show governance capability.
- **Balanced** — sensible defaults pre-selected. Good for normal use.
- **Open** — broad network access.

Enterprise demos: use Restricted with selective presets (at minimum: `github`, `local-inference`, `nous-code`, `nous-web`).

## Sandbox Isolation Model

The NemoClaw sandbox is a hardened container by design. **Configuration changes must be done from the host.**

**Inside the sandbox you CANNOT:**
- Use `sudo` (not installed)
- Install pip packages system-wide (`externally-managed-environment`)
- Run `hermes doctor` or `hermes setup` (blocked — NemoClaw manages config from host)
- Access the host filesystem
- Modify network policies

**Inside the sandbox you CAN:**
- Run `hermes status` (read-only)
- Run `hermes pairing list/approve/revoke/clear-pending`
- Access the API on port 8642
- Use `pipx` if installed (usually not)
- Run curl to allowed domains (telegram.org, pypi.org, huggingface.co, etc.)

**Reconfigure from host:** `nemoclaw onboard --resume`

**Agent runtime identity:** The sandbox reports `Agent: OpenClaw v2026.x.x` in status output — this is cosmetic. The actual agent inside is Hermes (v0.14.0+). Use `hermes`, not `openclaw tui`.

## Brev Instance Selection

For testing NemoClaw Hermes with NVIDIA cloud endpoints, the best value option (as of June 2026):

| Provider | GPU | RAM | CPUs | Storage | Price | Notes |
|----------|-----|-----|------|---------|-------|-------|
| MASSEDCOMPUTE (shadeform) | L40S 48GB VRAM | 128GB | 22 | 625GB SSD | $1.06/hr | "No stop/start" — data lost on stop. Fastest spin-up (~2.5 min). |

At ~A$1.60/hr AUD equivalent, even a four-hour validation session costs under A$7. This is the cheapest path to validate the NemoClaw Hermes sandbox before buying dedicated hardware.

**What to pick:** VM Mode w/ Jupyter (clean Linux + GPU). No launchable, no Docker template, no setup script needed.

**Note on advertised vs actual RAM:** Brev may show 128GB RAM but the instance may report ~70GB. This is normal — some RAM is reserved for the GPU and system. 70GB is still more than enough for NemoClaw Hermes testing.

### Jupyter Terminal: SSH Alternative

When the Brev CLI SSH command is not available (CLI install may be down, or the Access tab does not show a direct SSH command), use Jupyter Lab's built-in terminal instead:

1. In the Brev console, under **Share a Service**, find the Jupyter URL (e.g. `https://jupyter-<id>.brevlab.com/lab`). It should show as "Healthy".
2. Open it in a browser that is already signed into NVIDIA (Chrome where you are logged into Brev).
3. Click **Terminal** under the Launcher (or File → New → Terminal).
4. This gives you a shell directly on the cloud instance. Run the full NemoHermes installer from here.

This is the most reliable access path when the Brev CLI is unavailable or the instance does not expose direct SSH.

## Architecture Decision

**MacBook = control surface, not runtime.**

NemoClaw sandboxes are designed for machines with fast Docker image access and 12GB+ memory. The MacBook Air can run the CLI, manage sandboxes over SSH to a cloud instance, and build controls. The actual sandbox runtime belongs on:

- **Brev cloud instance** for testing and demos
- **DGX Spark** (or equivalent NVIDIA appliance) for the long-term AgentOS reference architecture

Do not spend time fighting Docker image pulls on the MacBook. Escalate to Brev early.

## Hardware Decision: MacBook Pro vs DGX Spark

For PerformOS/AgentOS demos:

- **MacBook Pro M5 Max 128GB** — better for client demos. Portable. Hermes runs natively (no Docker bridge). Dashboard at `http://127.0.0.1:9119` works directly. Show agents, models, skills. Use as demo unit.
- **DGX Spark / ASUS Ascent GX10** — better for dedicated production appliance. Headless. Always-on. NemoClaw sandbox on bare metal.

Recommended first buy: MacBook Pro for demos. DGX Spark later for production.

## What Works Today vs Alpha-Rough

### ✅ Working (June 2026)

- Sandbox builds on cloud GPU
- Hermes runs inside sandbox (`hermes` command, not `openclaw tui`)
- NVIDIA GPT-OSS 120B and Nemotron 120B respond via API
- GPU passthrough (nvidia-smi, CUDA, proc write)
- Network policies and firewall
- Terminal chat TUI
- OpenAI-compatible API at port 8642
- `nemoclaw hermes connect` → `hermes` chat path
- `brev port-forward` for port 18789

### ⚠️ Alpha-rough

- `nemohermes hermes dashboard-url` consistently fails — auth token retrieval is unreliable
- Dashboard at port 18789 may exist but cannot be reliably authenticated
- `nemoclaw hermes status` reports `Agent: OpenClaw` but the agent is Hermes
- Telegram pairing needs host-side config workaround
- The quickstart MUST run in an interactive TTY; piping fails
- Each failed onboard attempt leaves a stale OpenShell process on port 8080
- `brev exec` cannot run interactive prompts — use `brev shell` always
- Gateway restart/stop can take 10+ minutes — do not interrupt

## Cost Context

Brev MASSEDCOMPUTE L40S: **$1.06/hr USD** (~A$1.60/hr). A full test session (2-4 hours) costs A$3-7. Shut down when not in use — some instance types have no stop/start.

## Messaging Guidance for Operators

When communicating state to the user, be direct:

- If port 18789 fails: say the dashboard service is not running yet, not that the URL is wrong.
- If there is no sandbox: say the install is incomplete.
- If an NVIDIA key is missing: say the next step is to add `NVIDIA_API_KEY`.
- Do not bury the user in installation theory. Give current state → cause → next action.

## References

- `references/hermes-api-telegram-ops.md` — Hermes sandbox operations: API access on port 8642, Telegram pairing, `hermes status` diagnostics, port summary (Hermes vs OpenClaw), and quick verification flow.
- `references/session-detail-2026-06-13.md` — Full session transcript: model catalog, Docker daemon check script, Brev escape hatch pattern, provider source code paths.
- `references/brev-cloud-onboarding-flow.md` — Step-by-step interactive onboarding prompt sequence for Brev cloud instances via Jupyter Terminal.
- `references/ssh-tunnel-dashboard-access.md` — Complete SSH tunnel workflow for dashboard access when Brev port sharing is blocked.
- `references/brev-l40s-working-deploy-20260613.md` — Full working transcript from a successful Brev L40S deployment (13 June 2026).
- `references/hermes-dashboard-manifest.md` — manifest.yaml analysis for dashboard port.
- `references/nvidia-nous-livestream-insights.md` — NVIDIA Neutron Labs livestream (June 2026) with Nous Research demoing the enterprise deployment pattern.
- `references/ssh-access.md` — SSH access setup for Brev instances.
- `references/brev-cloud-instance-pattern.md` — Brev cloud instance provisioning details.
- `references/nemohermes-macos-nvidia-endpoints.md` — Session-derived troubleshooting pattern for macOS + NVIDIA Endpoints.
- `references/brev-cloud-ssh-workflow.md` — Brev cloud instance access patterns via SSH.
- `references/brev-nemohermes-clean-onboarding-2026-06-14.md` — clean retry flow for Brev/cloud onboarding: license `yes`, direct `nemohermes onboard --fresh`, 8081 gateway fallback, Telegram toggle, correct model and user ID prompts.
