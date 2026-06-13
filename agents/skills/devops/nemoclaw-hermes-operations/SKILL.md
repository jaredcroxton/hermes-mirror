---
name: nemoclaw-hermes-operations
description: Operate NVIDIA NemoClaw with Hermes Agent on macOS or NVIDIA hosts, including onboarding, inference provider selection, sandbox verification, and dashboard/API troubleshooting.
version: 1.0.0
author: Brock / Hermes Agent
license: MIT
platforms: [macos, linux]
metadata:
  hermes:
    tags: [nemoclaw, hermes, openshell, nvidia, sandbox, inference, docker]
---

# NemoClaw Hermes Operations

Use this skill when Jared asks to install, configure, verify, or troubleshoot NVIDIA NemoClaw running Hermes Agent inside an OpenShell sandbox.

## What this skill covers

- NemoHermes onboarding on macOS or Linux
- Docker Desktop or Colima preflight checks
- Choosing an inference provider
- Switching from local Ollama to NVIDIA Endpoints
- Understanding why the Hermes dashboard does not load
- Verifying the sandbox, dashboard, and API endpoint
- Keeping the MacBook as a learning sandbox and the DGX Spark as the serious AgentOS reference appliance

## Operating frame for Jared

Use this positioning:

- MacBook install = learning sandbox and proof.
- DGX Spark install = real AgentOS reference appliance.
- NVIDIA cloud endpoint = good first inference path on the laptop.
- Local Ollama = fallback or smoke test, not the strategic path for AgentOS.

## Before running onboarding

1. Confirm Docker is running.

```bash
docker version --format 'Client={{.Client.Version}} Server={{.Server.Version}}'
docker info --format 'OSType={{.OSType}} Architecture={{.Architecture}} CPUs={{.NCPU}} Memory={{.MemTotal}}'
```

2. Confirm NemoHermes commands if already installed.

```bash
command -v nemohermes || true
command -v nemoclaw || true
command -v openshell || true
nemohermes --version 2>/dev/null || true
```

3. Check whether any stale onboarding or image pull is still running.

```bash
ps aux | grep -iE 'nemohermes onboard|docker pull ghcr.io/nvidia/nemoclaw/hermes|openshell|ollama' | grep -v grep || true
```

4. Check existing sandbox state.

```bash
nemohermes list || true
docker ps --format 'table {{.Names}}\t{{.Status}}\t{{.Ports}}\t{{.Image}}' || true
```

## Recommended laptop inference path

For Jared's MacBook test, prefer NVIDIA Endpoints over local Ollama if an NVIDIA API key is available.

Why:

- It removes local model pressure from the MacBook.
- It tests NemoClaw and Hermes sandboxing, not MacBook inference capacity.
- It aligns with the DGX Spark and AgentOS architecture.
- It keeps the laptop as the control surface and sandbox host.

Required environment variable:

```bash
export NVIDIA_API_KEY="<redacted>"
```

If persisting it, put it in the appropriate env file, not in chat or notes:

```bash
printf 'NVIDIA_API_KEY=%s\n' '<redacted>' >> ~/.hermes/.env
```

Do not expose the actual key in replies, memory, skill updates, logs, or handoffs.

## Onboarding command

Always use the `--agent hermes` flag. Do NOT use `export NEMOCLAW_AGENT=hermes` — it only affects the sandbox name, not the runtime.

```bash
nemoclaw onboard --agent hermes
```

If installing from the bootstrap script first:

```bash
curl -fsSL https://www.nvidia.com/nemoclaw.sh | bash
nemoclaw onboard --agent hermes
```

During provider selection, choose:

```text
1) NVIDIA Endpoints
```

Then select a Nemotron model from the NVIDIA endpoint catalog. For first proof, prefer a serious NVIDIA model over a tiny local model.

## Dashboard troubleshooting

**Critical port distinction:** The OpenClaw build uses port 18789 for its dashboard. The Hermes Agent build does NOT expose a dashboard on 18789. Hermes uses port **9119** for its web dashboard and port **8642** for its OpenAI-compatible API. The `nemoclaw hermes dashboard-url --quiet` command returns an error on Hermes sandboxes: "does not expose an OpenClaw dashboard URL." This is expected — Hermes does not have an externally forwarded dashboard.

The Hermes dashboard at `http://127.0.0.1:9119` is only reachable **inside** the sandbox container. Docker bridge networking does not forward it to the host by default. On cloud instances this means you need an SSH tunnel into the sandbox (not just the host), or a `socat` bridge on the host — but `socat` is fragile here because the dashboard binds to `127.0.0.1` inside the container, not `0.0.0.0`. The cleanest path: run `hermes` interactively inside the sandbox via `nemoclaw hermes connect`, or use the API at port 8642.

**On a local macOS machine** (no Docker bridge barrier): the dashboard should be directly accessible. If not, diagnose in this order:

```text
http://127.0.0.1:9119
```

1. Check whether the sandbox exists.

```bash
nemohermes list
```

If it says no sandboxes are registered, the dashboard cannot load yet.

2. Check whether anything is listening on the expected ports.

```bash
lsof -nP -iTCP:9119 -sTCP:LISTEN || true
lsof -nP -iTCP:8642 -sTCP:LISTEN || true
lsof -nP -iTCP:18789 -sTCP:LISTEN || true
lsof -nP -iTCP:8080 -sTCP:LISTEN || true
```

Expected ports for a **Hermes Agent** sandbox:

- `9119` = Hermes web dashboard (only accessible inside sandbox on cloud)
- `8642` = OpenAI-compatible Hermes API
- `8080` = OpenShell gateway

Port `18789` is the **OpenClaw** dashboard — it will be empty on a Hermes sandbox.

If only `8080` is listening, OpenShell is up but the Hermes sandbox/dashboard is not ready.

3. Probe directly.

```bash
curl -sS -m 3 -I http://127.0.0.1:9119/ || true
curl -sS -m 3 http://127.0.0.1:8642/health || true
```

4. Check dashboard availability. For Hermes Agent sandboxes, the OpenClaw-style URL is not exposed:

```bash
nemohermes <sandbox-name> dashboard-url --quiet
```

**On a cloud instance (Brev):** `127.0.0.1:18789` only works on the instance itself. Opening it locally gives `ERR_CONNECTION_REFUSED`. Try these in order:

1. **Brev "Share a Service"** — in the Brev Console, add port `18789` as a shared service. Some providers (notably MASSEDCOMPUTE/shadeform) block port modifications and this will not work.

2. **SSH tunnel (reliable fallback)** — enable password auth on the instance, then tunnel from your local Mac:
   ```bash
   # On cloud instance (Jupyter Terminal):
   sudo sed -i 's/^PasswordAuthentication no/PasswordAuthentication yes/' /etc/ssh/sshd_config
   echo -e 'mypass\nmypass' | sudo passwd shadeform
   sudo systemctl restart sshd
   ```
   ```bash
   # On local Mac:
   ssh -L 18789:127.0.0.1:18789 shadeform@<instance-ip>
   ```
   Then open `http://127.0.0.1:18789/` in Chrome. Works on all providers.

3. `localtunnel` (`pip install localtunnel`) does not work on Brev instances — the package is not available. `ngrok` requires a verified account and auth token.

For full detail see `nemoclaw-hermes-setup`, pitfall 9.

## Common onboarding pitfalls

### Pitfall 1: Stale gateway process blocking port 8080

If onboarding exits with:

```text
!! Port 8080 is not available.
   Blocked by: openshell (PID XXXXX)
```

Kill the stale process and retry. This happens every time a previous `nemoclaw onboard` ran and the gateway was not cleanly destroyed.

```bash
sudo kill <PID>
sleep 2
nemoclaw onboard --agent hermes
```

### Pitfall 2: Wrong agent installed (OpenClaw instead of Hermes)

If `NEMOCLAW_AGENT=hermes` was used as an environment variable instead of the `--agent hermes` flag, the sandbox WILL be named "hermes" but OpenClaw WILL be installed inside it. Symptoms: dashboard at port 18789 shows an OpenClaw login screen, `openclaw` command exists inside the sandbox, `hermes` command is absent.

Fix: destroy the sandbox and rebuild with the correct flag.

```bash
nemoclaw hermes-sandbox destroy
# Type 'yes' to confirm, then press Enter to keep the gateway for faster rebuild
nemoclaw onboard --agent hermes
```

### Pitfall 3: Docker bridge blocks dashboard access (cloud only)

On cloud instances, the dashboard binds to `127.0.0.1` inside the container by default. Use `--insecure` to bind to `0.0.0.0`, then bridge with `socat`:

**Inside sandbox:** `hermes dashboard --insecure --tui &`
**On host:** `socat TCP-LISTEN:9119,bind=127.0.0.1,fork,reuseaddr TCP:<sandbox-ip>:9119 &`
**From Mac:** `ssh -L 9119:127.0.0.1:9119 shadeform@<ip>` then open `http://127.0.0.1:9119`

This is NOT an issue on a local macOS install where the dashboard is directly reachable at `http://127.0.0.1:9119`.

### Pitfall 4: Gateway restart can take 11+ minutes

`hermes gateway restart` can time out. Stopping the gateway (`hermes gateway stop`) can also take 10+ minutes. Let it complete. Do not kill it mid-operation.

### Pitfall 5: Cloud provider blocks port modifications

Some Brev providers (notably MASSEDCOMPUTE/shadeform) block the "Expose Port" feature. "Share a Service" only works for ports already configured at instance creation. The SSH tunnel fallback is the reliable path for these providers.

### Pitfall 6: Sandbox image pull timeout

If onboarding stops at:

```text
[6/8] Creating sandbox
```

and the dashboard does not load, likely the sandbox image pull or build has not completed.

Check for image pulls:

```bash
ps aux | grep -i 'docker pull ghcr.io/nvidia/nemoclaw/hermes-sandbox-base' | grep -v grep || true
docker images | grep -i 'nemoclaw\\|hermes' || true
```

If a stale pull is stuck and you need to restart cleanly:

```bash
pkill -f 'docker pull ghcr.io/nvidia/nemoclaw/hermes-sandbox-base' 2>/dev/null || true
pkill -f 'nemohermes onboard' 2>/dev/null || true
```

Then rerun onboarding with the intended provider.

### Pitfall 7: Gateway stop/restart can take 10+ minutes

Inside the sandbox, `hermes gateway restart` times out after 60s with `Timeout - denying command`. `hermes gateway stop` triggers a progress bar showing 11+ minute total duration. Do NOT kill the process — let it complete. Premature termination leaves the gateway in an inconsistent state requiring a full sandbox destroy and rebuild.

```text
[6/8] Creating sandbox
```

and the dashboard does not load, likely the sandbox image pull or build has not completed.

Check for image pulls:

```bash
ps aux | grep -i 'docker pull ghcr.io/nvidia/nemoclaw/hermes-sandbox-base' | grep -v grep || true
docker images | grep -i 'nemoclaw\|hermes' || true
```

If a stale pull is stuck and you need to restart cleanly:

```bash
pkill -f 'docker pull ghcr.io/nvidia/nemoclaw/hermes-sandbox-base' 2>/dev/null || true
pkill -f 'nemohermes onboard' 2>/dev/null || true
```

Then rerun onboarding with the intended provider.

## Verification checklist

Only tell Jared it is working after these pass:

```bash
nemoclaw hermes connect
# Inside sandbox:
hermes
# Should start interactive chat with Nemotron model
```

API verification from the host:

```bash
curl -s http://127.0.0.1:8642/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer test" \
  -d '{"model": "nvidia/nemotron-3-super-120b-a12b", "messages": [{"role": "user", "content": "Say hello"}]}'
```

## Interactive terminal use

Once inside the sandbox (`nemoclaw hermes connect`), type `hermes` to start an interactive chat session. Type `/exit` to leave the chat, then `exit` to return to the host shell.

The `hermes` command only exists inside the sandbox. On the host, `hermes` is not found — that is expected.

## Telegram pairing

The bot token is configured during onboarding. The bot polls Telegram and receives messages (confirm via `nemoclaw hermes logs --tail 50`). It will not respond until paired:

```bash
nemoclaw hermes connect
hermes pairing list
```

If the user has sent `/pair` to the bot and a code appears:

```bash
hermes pairing approve telegram <CODE>
```

If `hermes pairing list` shows "No pairing data found" despite sending `/pair`, the pairing config may need host-side setup. Exit the sandbox and run:

```bash
exit
nemoclaw onboard --resume
```

The `hermes pairing` subcommands are: `list`, `approve <platform> <code>`, `revoke <USER>`, `clear-pending`. Note: `hermes telegram pair` is NOT valid — the correct command is `hermes pairing`.

## Messaging guidance

For Jared, be direct:

- If `18789` fails, say the dashboard service is not running yet, not that the URL is wrong.
- If there is no sandbox, say the install is incomplete.
- If an NVIDIA key is missing, say the next step is to add `NVIDIA_API_KEY`.
- Do not bury the user in installation theory. Give the current state, the cause, and the next action.

## References

- See `references/nemohermes-macos-nvidia-endpoints.md` for the session-derived troubleshooting pattern, port meanings, and NVIDIA endpoint setup notes.
- See `references/brev-cloud-ssh-workflow.md` for Brev cloud instance access patterns.
- For cloud instance onboarding (Brev Jupyter Terminal access, firewall fixes, interactive prompt flow), see the sister skill `nemoclaw-hermes-setup` — it covers the full cloud install path including the Jupyter Terminal SSH alternative, `ufw` firewall fix, stale gateway cleanup, and step-by-step interactive prompts.