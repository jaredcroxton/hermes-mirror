---
name: nemoclaw-hermes-deployment
description: Deploy NemoClaw sandboxes with Hermes Agent on cloud GPU instances (Brev, DGX Spark, or any Ubuntu/Docker host). Covers onboarding, firewall, SSH access, Telegram pairing, API endpoints, sandbox isolation model, and common pitfalls.
---

# NemoClaw Hermes Agent Deployment

Deploy a NemoClaw sandbox running Hermes Agent on a cloud GPU instance. Proven on Brev MASSEDCOMPUTE L40S (128GB RAM, 48GB VRAM) with NVIDIA Nemotron 120B via NVIDIA Endpoints.

## Trigger conditions

- User wants to spin up NemoClaw with Hermes (not OpenClaw) on a cloud GPU instance
- User is deploying on Brev, DGX Spark, or any Ubuntu/Docker host with an NVIDIA GPU
- User needs a sandboxed Hermes Agent reachable via Telegram or API
- User asks "install NemoClaw", "set up Hermes sandbox", "NemoClaw onboard"

## Prerequisites

- Ubuntu 22.04+ with Docker installed and running
- NVIDIA GPU with drivers and CDI support (verified via `nvidia-smi`)
- 64GB+ RAM recommended (70GB tested)
- 500GB+ disk for sandbox images
- Port 8080 available for OpenShell gateway
- Outbound internet for Docker pulls and API calls

## Official quickstart command (13 June 2026)

The documented, supported install path per NVIDIA docs is:

```bash
export NEMOCLAW_AGENT=hermes && curl -fsSL https://www.nvidia.com/nemoclaw.sh | bash
```

This installs the NemoHermes CLI (v0.0.55+), OpenShell CLI, and launches the interactive `nemohermes onboard` wizard. The env var is respected — it builds a Hermes sandbox.

For non-interactive acceptance of third-party software:
```bash
curl -fsSL https://www.nvidia.com/nemoclaw.sh | NEMOCLAW_AGENT=hermes NEMOCLAW_ACCEPT_THIRD_PARTY_SOFTWARE=1 bash
```

**However**, the onboard wizard STILL needs interactive input (provider, model, API key). Use `brev shell`, not `brev exec`, for the quickstart. `brev exec` cannot handle the wizard prompts.

## Full deployment workflow

### 1. Access the instance

Brev instances provide Jupyter Lab via secure tunnel. Open the `brevlab.com` URL in the user's browser. From Jupyter, open a Terminal.

Alternatively, enable SSH access (see references/ssh-access.md).

### 2. Install NemoClaw

```bash
curl -fsSL https://www.nvidia.com/nemoclaw.sh | bash
```

### 3. First onboard attempt (expect firewall block)

```bash
nemoclaw onboard --agent hermes
```

The preflight check will fail at step 2 with:
```
✗ Sandbox containers cannot reach the gateway at host.openshell.internal:8080
```

### 4. Fix firewall

```bash
sudo ufw allow from 172.18.0.0/16 to 172.18.0.1 port 8080 proto tcp
```

### 5. Re-onboard (expect stale gateway)

```bash
nemoclaw onboard --agent hermes
```

If a stale gateway process blocks port 8080:
```bash
sudo kill <PID>
sleep 2
nemoclaw onboard --agent hermes
```

### 6. Choose inference provider

Select **NVIDIA Endpoints** (option 1). The user must provide their NVIDIA API key.

**Model choice matters for Hermes.** As of June 2026:
- **Nemotron 3 Super 120B** (`nvidia/nemotron-3-super-120b-a12b`) — works reliably with Hermes tool descriptions
- **GPT-OSS 120B** (`openai/gpt-oss-120b`) — known to fail with HTTP 400 ToolDescription validation errors in Hermes

If GPT-OSS was selected during onboarding, switch post-install:
```bash
nemohermes inference set --model nvidia/nemotron-3-super-120b-a12b --provider nvidia-prod --sandbox hermes --no-verify
```

### 7. Skip or configure messaging

- Skip Brave Search (Hermes Agent does not support it yet)
- Skip messaging channels unless Telegram is needed
- If Telegram: toggle it on, paste bot token from @BotFather
- Accept "Reply only when @mentioned" for group chats

### 8. Accept defaults

- Sandbox name: `hermes` (press Enter)
- Resource profile: 6 (no profile — OpenShell defaults)
- Policy tier: Balanced (press Enter)
- Policy presets: accept defaults (npm, pypi, huggingface, brew, telegram if enabled)

### 9. Build completes

The sandbox build takes 3-8 minutes on cloud GPU. Successful output:
```
Hermes is ready
Sandbox:  hermes
Model:    nvidia/nemotron-3-super-120b-a12b
```

## Accessing the sandbox

### API endpoint (port 8642)
```
http://127.0.0.1:8642/v1
```
OpenAI-compatible. Test with:
```bash
curl -s http://127.0.0.1:8642/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer test" \
  -d '{"model": "nvidia/nemotron-3-super-120b-a12b", "messages": [{"role": "user", "content": "Hello"}]}'
```

### Terminal access
```bash
nemoclaw hermes connect
```

### SSH tunnel from local machine
```bash
ssh -L 8642:127.0.0.1:8642 user@<instance-ip>
```

## Sandbox isolation model

The NemoClaw sandbox is deeply locked down. This is by design.

**Inside the sandbox you CANNOT:**
- Use `sudo` (not installed)
- Install pip packages system-wide (externally-managed-environment)
- Run `hermes doctor` or `hermes setup` (blocked — "NemoClaw manages sandbox config from the host for integrity checks")
- Access the host filesystem
- Modify network policies

**Inside the sandbox you CAN:**
- Run `hermes status` (read-only)
- Run `hermes pairing list/approve/revoke/clear-pending`
- Access the API on port 8642
- Use `pipx` if installed (usually not)
- Run curl to allowed domains (telegram.org, pypi.org, huggingface.co, etc.)

**Configuration changes must be done from the host:**
```bash
nemoclaw onboard --resume
```

## Telegram in the sandbox (alpha gap)

The `nemohermes onboard` wizard, even when Telegram is toggled on during the messaging step, does not reliably configure Telegram in the Hermes agent sandbox. The bot token and chat ID need to be injected at the **Open Shell gateway layer** as environment variables — the agent cannot configure this from inside the sandbox.

### Enterprise pattern (from NVIDIA/Neutron Labs livestream, June 2026)

Johnny from Nous Research demoed the enterprise path: a **custom onboarding script** that:

1. Injects API tokens as Open Shell environment variables (masked inside sandbox, substituted at egress)
2. Pre-configures messaging policies (telegram, discord) programmatically
3. Creates user sandboxes in parallel
4. The agent never sees real tokens — `echo $GITHUB_TOKEN` inside sandbox shows an Open Shell placeholder

This is the NemoClaw blueprint approach — the interactive `nemohermes onboard` wizard is a starter tool. Production deployment uses custom scripts.

See `references/nvidia-nous-livestream-insights.md` for the full breakdown.

### Quick Telegram workaround

For testing, configure the bot token manually inside the sandbox `.env`:

1. Connect: `nemoclaw hermes connect`
2. Check current config: `cat /sandbox/.hermes/.env`
3. Add Telegram token and chat ID as env vars
4. Restart gateway from host: `nemoclaw hermes restart`

## Dashboard access (Hermes — alpha gap, June 2026)

The quickstart-installed NemoHermes is documented to expose a dashboard on port **18789** (per `manifest.yaml`). However, `nemohermes hermes dashboard-url` consistently fails with:

```
Could not retrieve the dashboard auth token for sandbox 'hermes'.
```

This is a known alpha issue. The web dashboard layer is not mature for the Hermes agent path (OpenClaw sandboxes with the same quickstart DO expose a working dashboard). For now, access Hermes via:

- **TUI**: `nemoclaw hermes connect` then `hermes`
- **API**: port 8642 (`http://127.0.0.1:8642/v1`)

Port forward 18789 is still worth setting up (`brev port-forward keen-tomato-jackal -p 18789:18789`) — the dashboard may become reachable in future releases without a rebuild.

## Common errors and fixes

| Error | Fix |
|-------|-----|
| Port 8080 blocked by stale openshell process | `sudo kill <PID>` |
| Firewall blocking sandbox→gateway | `sudo ufw allow from 172.18.0.0/16 to 172.18.0.1 port 8080 proto tcp` |
| Installs OpenClaw instead of Hermes | The `export NEMOCLAW_AGENT=hermes` env var DOES work. The agent runtime inside every sandbox is OpenClaw — the CLI wrapper naming (NemoHermes vs NemoClaw) is cosmetic. Inside the sandbox, run `hermes` not `openclaw tui`. |
| Dashboard not reachable on cloud | Use `hermes dashboard --insecure --tui &` inside sandbox, then `socat` bridge from host (see Web dashboard access section) |
| `nemohermes dashboard-url` returns "Sandbox does not exist" | Must include sandbox name: `nemohermes hermes dashboard-url` |
| `nemohermes hermes dashboard-url` returns \"Could not retrieve the dashboard auth token\" | This is a known alpha issue (June 2026). The Hermes agent path does not consistently expose a dashboard. OpenClaw sandboxes do. Access Hermes via TUI (`nemoclaw hermes connect`) or API (port 8642). |
| GPT-OSS 120B model returns HTTP 400 (ToolDescription validation error) | Switch to Nemotron: `nemohermes inference set --model nvidia/nemotron-3-super-120b-a12b --provider nvidia-prod --sandbox hermes --no-verify` |
| Inference set verification fails with SSL/connection error mid-session | Use `--no-verify` flag to skip endpoint verification |
| `nemohermes onboard --fresh` still blocked by stale openshell on port 8080 | `sudo killall openshell openshell-gateway` then retry. The process may have respawned under a new PID. |
| `pip install` blocked | Sandbox is locked. Use host for package installs |
| ngrok requires auth | Use SSH tunnel instead |
| Brev "Expose Port" blocked by provider | Use SSH tunnel from local machine |
| `brev exec` hangs on interactive prompt | Use `brev shell` instead — `brev exec` cannot handle the onboard wizard |
| Previous onboarding session failed | `nemohermes onboard --fresh` or type `f` when prompted |
| Telegram bot not responding | Check `nemoclaw hermes logs --tail 50`; bot may need restart |
| `hermes pairing` shows "No pairing data found" inside sandbox | NemoClaw manages config from host. Run `nemoclaw onboard --resume` from host to configure Telegram pairing. On a local Hermes install (not sandbox), `hermes pairing` works directly. |
| Dashboard bridge: `ERR_CONNECTION_REFUSED` on Mac | SSH tunnel died or lost port. Reconnect with `ssh -L 9119:...`. Check `lsof -i :9119` on Mac and cloud host for stale listeners. |
| Dashboard bridge: `ERR_EMPTY_RESPONSE` | socat bridge stale or dashboard process died. Kill old socat, restart dashboard inside container, re-bridge. |
| `bind [127.0.0.1]:9119: Address already in use` during SSH login | Old SSH tunnel holding port 9119 on the cloud host. `kill $(pgrep -f "ssh.*9119")` on the host first, then reconnect. |
| `openshell forward start 9119 hermes` fails with "Port already in use" | A stale socat or SSH tunnel holds the port. `lsof -i :9119 -sTCP:LISTEN` to find the PID, kill it, retry. |
| Dashboard process dies on SSH disconnect | The `&` backgrounded process inherits the SSH session. Use `nohup` or `docker exec ... bash -c 'nohup hermes dashboard ... &'` for durability. |

## Destroying and rebuilding

```bash
nemoclaw hermes destroy
# Type 'yes' to confirm
# Press Enter to keep the gateway (faster rebuild)
nemoclaw onboard --agent hermes
```

## Cost context

Brev MASSEDCOMPUTE L40S: $1.06/hr USD (~A$1.60/hr). A full test session (2-4 hours) costs A$3-7. Shut down when not in use — no stop/start on some instance types.

## Curator note — skill overlap

Five NemoClaw skills exist as of June 2026: `nemoclaw-hermes-deployment` (this one), `nemoclaw-hermes-setup` (macOS), `nemoclaw-hermes-deploy` (cloud GPU), `nemoclaw-hermes-operations` (operations), `nemoclaw-sandbox-deployment` (sandbox deployment). These overlap significantly. Consolidate into one or two skills when the dust settles.

## Related references

- `references/nvidia-nous-livestream-insights.md` — NVIDIA Neutron Labs livestream (June 2026) with Nous Research demoing the enterprise NemoClaw Hermes deployment pattern
- `references/ssh-access.md` — SSH access setup for Brev instances
- `references/brev-cloud-instance-pattern.md` — Brev cloud instance provisioning details
