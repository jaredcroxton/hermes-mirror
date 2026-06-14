---
name: nemoclaw-master-reference
description: Expert reference for NemoClaw Hermes install, dashboard, Telegram, policy, multi-user setup. Based on all three NVIDIA streams.
---

# NemoClaw Master Reference

## Three Videos Analyzed

1. **Nemotron Labs Demo** (pgQDbRMa2Eg) — Johnny (Nous) + Karan (Nous) + Chris (NVIDIA). Custom onboarding scripts, token masking, policy hot-swap, multi-user (Alice/Bob), PR workflow, skill creation.
2. **Patrick Moorhead DGX Spark** (nCy5Hpg-ozU) — Exact step-by-step install with local Ollama + Nemotron 3 Super on DGX Spark. Telegram setup via wizard, dashboard URL, pairing flow.
3. **Chris Murphy Roadmap** (E9e8gZKjnTY) — NemoClaw PM. Alpha status, Hermes experimental, "delightful UX" June/July, multi-tenant Aug/Sep, Apache 2 open source.

## Architecture Truth

- NemoClaw = OpenShell (sandbox runtime) + agent (OpenClaw or Hermes) + installer + policies
- When `NEMOCLAW_AGENT=hermes` is set, the quickstart builds OpenClaw base with Hermes as experimental agent type inside
- Status will show "Agent: OpenClaw v2026.5.16" even with NEMOCLAW_AGENT=hermes — that's correct
- `hermes` command inside sandbox launches Hermes TUI; `openclaw tui` launches OpenClaw (if installed)
- NemoClaw is a REFERENCE ARCHITECTURE, not a product. Apache 2. Partners build products on top.

## Install Flow (Cloud Endpoints)

```bash
export NEMOCLAW_AGENT=hermes && curl -fsSL https://www.nvidia.com/nemoclaw.sh | bash
```

Wizard answers for cloud:
- Resume/fresh: **f**
- Provider: **1** (NVIDIA Endpoints)
- API key: paste key
- Model: **1** (Nemotron 3 Super 120B) — NOT 6 (GPT-OSS 120B has tool validation bug)
- Sandbox name: **hermes** (or custom)
- Apply: **y**
- Messaging: **Press 1** (toggles Telegram ON), then Enter
- Bot token: paste
- Chat ID: paste (8647481186 for Jared)
- Resource profile: **6** (no profile)
- Policy tier: **Balanced** (not Restricted for first test)
- Policy presets: toggle github, nous-web, nous-code, npm, telegram

## Install Flow (Local Ollama/DGX Spark)

Same as above but:
- Provider: **7** (Ollama)
- Model: Nemotron 3 Super (must be pulled first: `ollama pull nemotron:latest`)
- Docker GPU runtime must be configured first (DGX Spark specific)
- Ollama must listen on 0.0.0.0: `OLLAMA_HOST=0.0.0.0`

## Telegram Setup (Two Methods)

### Method A: Wizard (Patrick's way)
Press 1 at messaging step. Paste bot token. Paste chat ID. Works immediately after sandbox build.

### Method B: Pairing (post-install)
```bash
nemoclaw hermes connect
openclaw pairing
# Message bot on Telegram → get pairing code
openclaw pairing approve telegram <code>
```

## Dashboard Access

For OpenClaw sandboxes:
```bash
nemoclaw dashboard-url  # Gives http://127.0.0.1:18789/#token=...
# Port-forward to access from other machines:
openshell forward start --background 18789
```

For Hermes sandboxes:
- `nemohermes hermes dashboard-url` may return nothing (known alpha gap)
- Hermes API on port 8642: `http://127.0.0.1:8642/v1`
- Hermes Desktop (Electron) available for personal use WITHOUT sandbox

## Token Masking (Enterprise Path)

Custom onboarding script pattern:
```bash
nemoclaw hermes create \
  --name alice \
  --env GITHUB_TOKEN="***" \
  --env TELEGRAM_BOT_TOKEN="***" \
  --policy policy.yaml
```

Inside sandbox: `echo $GITHUB_TOKEN` shows `openshell_***` placeholder
At egress: OpenShell substitutes real token IF policy allows the connection

## Common Errors

1. **Port 8080 blocked**: `sudo kill <PID>` stale openshell process
2. **GPT-OSS 120B tool validation error**: Switch to Nemotron 120B (model 1)
3. **SSL record layer failure**: Temporary sandbox network hiccup, retries work
4. **API call HTTP 400**: Wrong model. Use Nemotron, not GPT-OSS.
5. **Dashboard URL not found**: Hermes agent doesn't expose dashboard the same way as OpenClaw (alpha gap)

## Key Quotes

- Karan: "This is the prototype and beginning of an enterprise solution for Hermes"
- Chris Murphy: "We're still alpha... Jensen asked us to deliver a delightful user experience"
- Johnny: "It gets better as you use it. Skills become reusable assets."
- Patrick: "Three ways to interact: terminal UI, web dashboard, Telegram"

## Roadmap (from Chris Murphy)

- April/May 2026: Core hardening, Hermes experimental, supported platforms
- June/July 2026: Delightful user experience, GUI installer, local inference optimizations
- August/September 2026: Multi-tenant backends, enterprise features, agent-to-agent communication

## For AgentOS Strategy

- NemoClaw is infrastructure, not product. This is GOOD for PerformOS.
- Position: "PerformOS builds on NVIDIA's open NemoClaw reference architecture"
- Wait for June/July "delightful UX" milestone before client demos
- Hermes inside NemoClaw is experimental — expect rough edges until at least June
- Enterprise multi-tenant doesn't arrive until Aug/Sep — don't promise it yet
