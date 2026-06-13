# Brev L40S Working Deploy — 13 June 2026

Full working deployment of NemoHermes sandbox on Brev cloud GPU.

## Instance

- **Name:** keen-tomato-jackal
- **Provider:** MASSEDCOMPUTE L40S
- **GPU:** NVIDIA L40S, 48GB VRAM
- **RAM:** 70GB usable (128GB provisioned)
- **Disk:** 614GB (574GB free)
- **Docker:** 29.1.5
- **CUDA:** 13.0
- **Cost:** ~$1.06/hr

## Working quickstart

```bash
brev shell keen-tomato-jackal
export NEMOCLAW_AGENT=hermes && curl -fsSL https://www.nvidia.com/nemoclaw.sh | bash
```

## Wizard choices

- Provider: 1 (NVIDIA Endpoints)
- Model: 6 (openai/gpt-oss-120b)
- Sandbox name: hermes (default)
- Messaging: skipped
- Resource profile: 6 (OpenShell defaults)
- Policy: Restricted
- Presets: github, local-inference, nous-code, nous-web, npm, telegram

## Build output

- 47 Dockerfile steps, 4.7s total
- Full build: 451s
- GPU passthrough: verified (nvidia-smi, CUDA, proc write)
- Policies: 7 revisions applied
- Dashboard: "Dashboard is live" reported but auth token retrieval failed

## First connection

```bash
nemoclaw hermes connect
# Inside sandbox:
hermes
```

Agent output: Hermes Agent v0.14.0 (2026.5.16), 22 tools, 82 skills, model gpt-oss-120b via NVIDIA Endpoints.

## Known failures observed

- `nemohermes dashboard-url` → "Sandbox 'dashboard-url' does not exist"
- `nemohermes hermes dashboard-url` → "Could not retrieve the dashboard auth token"
- `openclaw tui` inside sandbox → "command not found"
- `nemoclaw hermes status` reports `Agent: OpenClaw v2026.5.16` but agent is Hermes

## Firewall rule (one-time per instance)

```bash
sudo ufw allow from 172.18.0.0/16 to 172.18.0.1 port 8080 proto tcp
```

## Stale process cleanup

```bash
sudo killall openshell openshell-gateway 2>/dev/null
```
