# NemoHermes cloud deployment (Brev / massedcompute / remote GPU)

Use this reference when deploying NemoClaw Hermes on a remote cloud instance (Brev, massedcompute, EC2 GPU, DGX cloud) and accessing the dashboard remotely.

## The one command that starts everything

```bash
export NEMOCLAW_AGENT=hermes
curl -fsSL https://www.nvidia.com/nemoclaw.sh | bash
```

Then:
```bash
nemoclaw onboard --agent hermes
```

Do NOT run `nemoclaw onboard` without `--agent hermes`. Without the flag, you get an OpenClaw sandbox even if the sandbox name is "hermes." The `--agent hermes` flag builds the Hermes-specific sandbox image with `agents/hermes/Dockerfile` baked in.

## Key commands (host side)

```bash
nemohermes list                          # List sandboxes
nemohermes <name> status                 # Sandbox status
nemohermes <name> dashboard-url --quiet  # Dashboard URL
nemohermes <name> logs --follow          # Tail logs
nemohermes <name> connect                # SSH into sandbox
nemohermes <name> destroy                # Destroy sandbox
nemoclaw gateway destroy                 # Full gateway teardown
```

`nemohermes` is the Hermes-specific alias for `nemoclaw`. Use it for all Hermes sandbox operations.

## Expected ports after successful onboard

| Port | Service | Access |
|------|---------|--------|
| 18789 | Hermes web dashboard | Browser |
| 8642 | OpenAI-compatible API | Programmatic |
| 8080 | OpenShell gateway (internal) | Host only |

## Dashboard access on cloud instances

The Hermes dashboard runs on port 18789 inside the Docker sandbox container. It does NOT auto-forward to the host on cloud instances the way it does on macOS with Docker Desktop.

### CLI check first

```bash
nemohermes <sandbox-name> dashboard-url --quiet
```

If this returns `http://127.0.0.1:18789/`, the dashboard is running inside the container. The challenge is bridging it to your local browser.

### Method A: Brev Share a Service (preferred when available)

In the Brev console → Share a Service → add port 18789. Brev generates a `brevlab.com` URL with NVIDIA SSO.

**Caveat:** Some cloud providers (massedcompute) block additional port exposure. If "This cloud provider doesn't allow the modifications of ports" appears, use Method B.

### Method B: SSH port forwarding (when direct SSH works)

```bash
ssh -N -L 18789:127.0.0.1:18789 user@<instance-ip>
```

Then open `http://127.0.0.1:18789/` locally.

**Pre-requisite:** Password authentication must be enabled. On fresh cloud instances:
```bash
sudo sed -i 's/^PasswordAuthentication no/PasswordAuthentication yes/' /etc/ssh/sshd_config
sudo systemctl restart sshd
echo -e 'temppass\ntemppass' | sudo passwd <user>
```

### Method C: socat bridge (when SSH forwarding fails)

When the instance has Docker bridge networking and the sandbox is at `172.18.0.2`:

**Inside the sandbox** (`nemohermes <name> connect`):
```bash
hermes dashboard --insecure --tui &
```
The `--insecure` flag binds to `0.0.0.0` instead of `127.0.0.1`, making it reachable from the Docker host. `--tui` enables the in-browser chat tab.

**On the host:**
```bash
socat TCP-LISTEN:18789,bind=127.0.0.1,fork,reuseaddr TCP:172.18.0.2:18789 &
```

Then SSH tunnel port 18789 as in Method B.

## Onboarding choices (cloud instance)

| Prompt | Choose | Why |
|--------|--------|-----|
| Inference provider | 1 (NVIDIA Endpoints) | Use cloud models, not local |
| Model | 1 (Nemotron 3 Super 120B) | Flagship, good for testing |
| Sandbox name | hermes (Enter) | Default is fine |
| Brave Search | Skip (Enter) | Not needed for testing |
| Messaging | Skip or 1 for Telegram | Optional |
| Resource profile | 4 (developer, 75%) or 6 (no profile) | 6 is simpler |
| Policy tier | Balanced (Enter) | Good default |

## Jupyter terminal as access method

When SSH password auth is disabled and you cannot modify sshd_config, the Brev Jupyter URL provides a terminal. Open the Jupyter URL (from Brev console → Open Notebook), then File → New → Terminal. This is a shell directly on the cloud instance.

## Common failures and fixes

### Port 8080 blocked by stale openshell process
```bash
sudo kill $(pgrep -f openshell)
nemoclaw onboard --agent hermes
```

### Gateway stale after destroy
```bash
nemoclaw gateway destroy  # Type 'yes' when prompted
nemoclaw onboard --agent hermes
```

### `nemohermes dashboard-url` returns nothing or "not applicable"
The dashboard may not have been started. Connect to sandbox and run:
```bash
hermes dashboard --insecure --tui &
```

### "error while attempting to bind on address: address already in use"
Dashboard is already running inside the container. Kill the old process first:
```bash
hermes dashboard --stop
hermes dashboard --insecure --tui &
```

## Clean slate restart

When networking or port forwarding becomes tangled and you want a fresh start:

```bash
sudo kill $(pgrep -f openshell) 2>/dev/null
docker rm -f $(docker ps -aq) 2>/dev/null
docker system prune -a -f --volumes
rm -rf ~/.local/state/nemoclaw ~/.nemoclaw ~/.local/share/openshell
rm -f ~/.local/bin/nemohermes ~/.local/bin/nemoclaw ~/.local/bin/openshell*
```

Then reinstall from `curl -fsSL https://www.nvidia.com/nemoclaw.sh | bash`.

Or, on Brev: Stop → Delete the instance, spin a new one. Fresh OS, fresh Docker, zero stale state.

## What works vs what is alpha

**Works in cloud:**
- Sandbox builds on GPU (L40S verified)
- GPU passthrough (nvidia-smi, CUDA)
- API endpoint (8642) responds correctly
- Nemotron 120B via NVIDIA Endpoints
- Terminal chat (`hermes` from inside sandbox)
- Network policy isolation

**Alpha/rough:**
- Dashboard auto-forwarding to host
- `nemohermes dashboard-url` for Hermes sandboxes (works for OpenClaw, inconsistent for Hermes)
- Telegram pairing inside sandbox (needs host-side config)
- Port exposure through cloud provider restrictions

## Business demo recommendation

For client demos today, run Hermes natively on a MacBook Pro 128GB. Dashboard at `http://127.0.0.1:9119` just works. No Docker bridge. No port forwarding. No Brev limitations. The cloud sandbox is the deployment architecture story for production, not the demo unit.
