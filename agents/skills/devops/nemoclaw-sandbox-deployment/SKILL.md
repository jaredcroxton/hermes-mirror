---
name: nemoclaw-sandbox-deployment
description: Deploy NemoClaw sandboxes for Hermes Agent on cloud GPU instances or local hardware. Covers Brev cloud selection, sandbox build, SSH tunneling, dashboard access, and common pitfalls.
triggers:
  - "deploy NemoClaw"
  - "build sandbox"
  - "nemoclaw onboard"
  - "NemoClaw Hermes install"
  - "sandbox dashboard"
  - "Brev instance for Hermes"
  - "cloud GPU sandbox"
---

# NemoClaw Sandbox Deployment

Deploy NemoClaw sandboxes for Hermes Agent on cloud GPU instances (Brev) or local DGX/ASUS hardware.

## Correct quickstart command (as of 13 June 2026)

The documented, supported path from NVIDIA:

```bash
export NEMOCLAW_AGENT=hermes && curl -fsSL https://www.nvidia.com/nemoclaw.sh | bash
```

This single command installs the NemoHermes CLI, runs `nemohermes onboard` interactively, builds the sandbox, and starts the Hermes Agent. Do NOT run separate `nemoclaw onboard` commands after the quickstart.

## Hermes vs OpenClaw identity

The sandbox reports `Agent: OpenClaw v2026.5.16` in status output. Ignore this — the actual agent runtime inside is **Hermes Agent v0.14.0**. The `openclaw tui` command does not exist inside the sandbox. Use `hermes` to start the chat TUI.

The `NEMOCLAW_AGENT=hermes` env var configures the CLI wrapper branding as "NemoHermes" but the underlying sandbox agent runtime is currently OpenClaw-branded infrastructure running Hermes. This is a known branding inconsistency in the alpha.

## Dashboard caveat

The `nemohermes hermes dashboard-url` command consistently fails with "Could not retrieve the dashboard auth token." This was tested repeatedly on a fresh Brev L40S instance (13 June 2026) and never succeeded. The dashboard may technically exist at port 18789 but auth token retrieval is unreliable. For now, the chat TUI (`nemoclaw hermes connect` → `hermes`) is the most reliable interaction method. The API at port 8642 works.

## Cloud instance selection (Brev)

For testing/validation on Brev:
- **MASSEDCOMPUTE L40S** — cheapest option, best specs: NVIDIA L40S 48GB VRAM, 128GB RAM (shows as ~70GB usable), 22 CPUs, 625GB SSD, ~$1.06/hr USD
- Avoid instances with "No stop/start" if you need pause/resume
- Pre-release instances are fine for testing

## Sandbox build flow

1. Spin up Brev instance with VM Mode w/ Jupyter (MASSEDCOMPUTE L40S, ~$1.06/hr)
2. **Important:** Use `brev shell <instance-name>`, NOT `brev exec`. The onboard wizard requires a real TTY. `brev exec` pipes stdin and the wizard will stall or fail with stale-state errors.
3. Run the quickstart: `export NEMOCLAW_AGENT=hermes && curl -fsSL https://www.nvidia.com/nemoclaw.sh | bash`
4. The quickstart auto-runs `nemohermes onboard` interactively. Navigate the wizard:
   - **Resume/fresh:** Type `f` if prompted about a previous failed session
   - **Provider:** `1` (NVIDIA Endpoints)
   - **API key:** Paste your NVIDIA key
   - **Model:** `6` for GPT-OSS 120B, or `1` for Nemotron 3 Super 120B
   - **Sandbox name:** Accept default `hermes`
   - **Apply:** `y`
   - **Messaging:** Press Enter to skip (or toggle channels)
   - **Resource profile:** `6` (OpenShell defaults)
   - **Policy tier:** Restricted (recommended)
   - **Policy presets:** Select at minimum: github, local-inference, nous-code, nous-web, npm, telegram
5. Build takes 3-8 minutes (451s observed on L40S)
6. Connect: `nemoclaw hermes connect` then inside sandbox run `hermes`

### Onboarding wizard attaches to /dev/tty

The quickstart prints: `[INFO] Installer stdin is piped; attaching the usage notice to /dev/tty…` and then `[INFO] Installer stdin is piped; attaching onboarding to /dev/tty…`. This means the wizard bypasses stdin and writes directly to the terminal. Piping answers via `printf` or `yes` will NOT work. You MUST use an interactive shell (`brev shell` or direct SSH).

## Common pitfalls

### `brev exec` hangs or fails on interactive wizard

`brev exec` does not support interactive prompts. The quickstart's `nemohermes onboard` step requires a TTY. If you use `brev exec`, the wizard will either stall waiting for input that never arrives, or the quickstart will detect piped stdin and fail with "Interactive third-party software acceptance requires a TTY."

**Fix:** Always use `brev shell <instance-name>` for the full quickstart. Use `brev exec` only for non-interactive commands like `nemoclaw hermes status` or `docker --version`.

### "Previous onboarding session failed" after interrupted install

The quickstart stores onboarding state. After a timeout or Ctrl+C interrupt, the next run sees stale state and prompts "Resume the failed session, or start fresh? [R/f]".

**Fix:** Type `f` for fresh. If that prompt is not presented (because stdin is piped), run directly: `nemohermes onboard --fresh`.

### Stale OpenShell processes blocking port 8080

After a failed or interrupted onboard, stale `openshell` processes hold port 8080. The next onboard attempt fails with:
```
Port 8080 is not available. Blocked by: openshell (PID XXXXX)
```
Each failed attempt spawns a new stale process with a new PID. Killing one PID is not enough — the next attempt will hit the next stale process.

**Fix:** Kill all stale processes at once:
```bash
sudo killall openshell openshell-gateway 2>/dev/null
```
Then re-run the quickstart. Do NOT try to kill individual PIDs one at a time — the loop will exhaust you.

## Port forwarding for API access

The Hermes API at port 8642 is the most reliable access method. Port-forward from the Brev instance:

```bash
brev port-forward <instance-name> -p 8642:8642
```

Then access at `http://localhost:8642/v1`.

## What works today

- Sandbox builds on cloud GPU ✅
- Hermes runs inside sandbox (`hermes` command, not `openclaw tui`) ✅
- NVIDIA GPT-OSS 120B and Nemotron 120B respond via API ✅
- GPU passthrough (nvidia-smi, CUDA, proc write) ✅
- Network policies and firewall ✅
- Terminal chat TUI ✅
- OpenAI-compatible API at port 8642 ✅
- `nemoclaw hermes connect` → `hermes` chat path ✅
- `brev port-forward` for port 18789 ✅

## What is alpha-rough

- `nemohermes hermes dashboard-url` consistently fails — auth token retrieval is unreliable
- Dashboard at port 18789 may exist but cannot be reliably authenticated
- `nemoclaw hermes status` reports `Agent: OpenClaw` but the agent is Hermes
- Telegram pairing needs host-side config workaround
- The quickstart MUST run in an interactive TTY (`brev shell` or direct SSH); piping fails
- Each failed onboard attempt leaves a stale OpenShell process on port 8080

## References

- `references/brev-l40s-working-deploy-20260613.md` — full working transcript from 13 June 2026
- `references/hermes-dashboard-manifest.md` — manifest.yaml analysis for dashboard port

## MacBook Pro vs DGX Spark for deployment

For PerformOS/AgentOS demos:
- **MacBook Pro M5 Max 128GB** — better for client demos. Portable. Hermes runs natively (no Docker bridge). Dashboard at `http://127.0.0.1:9119` works directly. Show agents, models, skills. Use as demo unit.
- **DGX Spark / ASUS Ascent GX10** — better for dedicated production appliance. Headless. Always-on. NemoClaw sandbox on bare metal.

Recommended first buy: MacBook Pro for demos. DGX Spark later for production.
