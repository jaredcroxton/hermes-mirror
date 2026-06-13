---
name: nemoclaw-hermes-deploy
description: Deploy Hermes Agent inside an NVIDIA NemoClaw OpenShell sandbox — cloud GPU instances (Brev, MASSEDCOMPUTE), interactive onboarding, policy configuration, model selection, dashboard access, and TUI chat.
triggers:
  - NemoClaw
  - nemoclaw
  - nemohermes
  - OpenShell sandbox
  - brev cloud GPU instance
  - "deploy Hermes in a sandbox"
  - "NVIDIA sandbox"
  - "sandbox dashboard"
  - "nemoclaw onboard"
  - "nemohermes onboard"
---

# NemoClaw Hermes Sandbox Deployment

Deploy Hermes Agent inside an NVIDIA NemoClaw OpenShell sandbox on a cloud GPU instance (Brev, MASSEDCOMPUTE, or similar). Covers quickstart install, interactive onboarding, policy configuration, model switching, dashboard access, and terminal chat.

## Prerequisites

- Cloud GPU instance with Docker, NVIDIA drivers, and CUDA (Brev L40S or better recommended)
- 48GB+ VRAM, 64GB+ RAM, 500GB+ disk
- `brev` CLI installed and authenticated (`brew install brev && brev login`)
- NVIDIA API key from https://build.nvidia.com/settings/api-keys (starts with `nvapi-`)

## Quickstart (interactive — the correct path)

The quickstart is interactive and MUST be run in a real terminal, never through `brev exec` (which has no TTY).

1. Open a shell on the instance:
   ```
   brev shell <instance-name>
   ```

2. Run the quickstart:
   ```
   export NEMOCLAW_AGENT=hermes && curl -fsSL https://www.nvidia.com/nemoclaw.sh | bash
   ```

3. During onboarding:
   - **Provider:** Choose `1` for NVIDIA Endpoints
   - **Model:** Choose `1` for Nemotron 3 Super 120B (nvidia/nemotron-3-super-120b-a12b)
   - **Sandbox name:** Accept `hermes` or name it
   - **Policy tier:** Restricted (for enterprise demo) or Balanced (for normal use)
   - **Presets:** Enable at minimum: `github`, `local-inference`, `nous-code`, `nous-web`

4. The sandbox builds in 3-8 minutes (first run) or faster (cached).

## Non-interactive install (for scripted/headless use)

```
curl -fsSL https://www.nvidia.com/nemoclaw.sh | NEMOCLAW_AGENT=hermes NEMOCLAW_ACCEPT_THIRD_PARTY_SOFTWARE=1 bash
```

Non-interactive onboarding requires passing all config via flags/env vars. See `nemohermes onboard --help`.

## Chatting with the agent

1. Connect to the sandbox:
   ```
   nemoclaw hermes connect
   ```

2. Inside the sandbox, run:
   ```
   hermes
   ```
   NOT `openclaw tui` — that binary doesn't exist inside the Hermes sandbox. The agent binary is `/usr/local/bin/hermes`.

3. For dark theme:
   ```
   HERMES_TUI_THEME=dark hermes
   ```

## Agent runtime reality

The `NEMOCLAW_AGENT=hermes` flag configures the CLI wrapper name (`nemohermes`) and selects the Hermes agent Dockerfile. But `nemoclaw hermes status` will report `Agent: OpenClaw v2026.x.x`. This is cosmetic — the actual agent inside the sandbox IS Hermes (v0.14.0+). The OpenClaw version number is the NemoClaw platform version, not the agent runtime.

## Dashboard access

The dashboard is on port 18789 inside the sandbox. Access it via port-forward:

```
brev port-forward <instance-name> -p 18789:18789
```

Then open `http://localhost:18789` in browser.

`nemohermes dashboard-url` requires the sandbox name: `nemohermes hermes dashboard-url`. Token retrieval may fail — the TUI (`hermes` command) is the reliable interface. The dashboard is secondary.

## Model switching

Change the model after onboarding:

```
nemohermes inference set --model nvidia/nemotron-3-super-120b-a12b --provider nvidia-prod --sandbox hermes --no-verify
```

Use `--no-verify` if the credential verification fails mid-session (common on cloud instances).

## Model compatibility

- **nvidia/nemotron-3-super-120b-a12b** — recommended. Full tool support, no validation errors.
- **openai/gpt-oss-120b** — avoid. Known to reject Hermes tool descriptions with `ToolDescription validation error: Input should be a valid string [type=string_type, input_value=None]`.
- Other NVIDIA Endpoints models may vary — test tool compatibility early.

## Common failures and fixes

### Port 8080 blocked by stale openshell process
```
sudo killall openshell openshell-gateway
```
Or kill by PID: `sudo kill <PID>`

### Firewall blocks container-to-gateway traffic
```
sudo ufw allow from 172.18.0.0/16 to 172.18.0.1 port 8080 proto tcp
```

### Onboarding fails with "Previous onboarding session failed"
Run with `--fresh`:
```
nemohermes onboard --fresh
```

### "Could not retrieve the dashboard auth token"
The dashboard token endpoint is unreliable. Use the TUI (`hermes`) instead. Dashboard may still work at `http://localhost:18789` with the port-forward active — try it directly.

### brev exec can't run interactive commands
`brev exec` has no TTY. Use `brev shell` for any command that needs user input. `brev exec` is fine for non-interactive commands (`nvidia-smi`, `docker --version`, `df -h`).

### Hermes TUI frozen
Press `Ctrl+C` twice, or `Ctrl+D`. Reconnect with `nemoclaw hermes connect` and restart `hermes`.

## Policy presets reference

When selecting policies during onboarding:
- **Restricted** — nothing enabled by default. Toggle presets manually.
- **Balanced** — sensible defaults pre-selected.
- **Open** — broad network access.

Enterprise demos: use Restricted with selective presets to show governance capability.

## Cleanup

To fully remove from a cloud instance:
```
sudo killall openshell openshell-gateway 2>/dev/null
docker rm -f $(docker ps -aq) 2>/dev/null
docker system prune -a -f --volumes 2>/dev/null
rm -rf ~/.local/state/nemoclaw ~/.nemoclaw ~/.local/share/openshell
```
