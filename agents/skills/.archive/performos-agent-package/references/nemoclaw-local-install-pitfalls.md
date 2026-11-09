# NemoClaw Hermes — Local Install Pitfalls and Cloud Workaround

Captured 13 June 2026 from the MacBook install attempt and Brev cloud instance setup.

## The problem: Docker Desktop on macOS arm64 cannot pull the sandbox image

The NemoClaw Hermes quickstart (`nemohermes onboard`) attempts to pull `ghcr.io/nvidia/nemoclaw/hermes-sandbox-base:v0.0.55`. On macOS arm64 with Docker Desktop, this consistently fails.

Three approaches were tried. All failed:

1. **`docker pull`** — timed out at 600 seconds on a 1.1GB layer. Docker Desktop arm64 networking path to GHCR is the bottleneck.
2. **`skopeo copy` to Docker daemon** — stalled on the same large blob layer. Killed with exit 143.
3. **`docker build` from `agents/hermes/Dockerfile.base`** — stalled at npm install step even with Docker Desktop memory increased to 12GB. Killed with exit 130.

**Host specs at time of attempt:** macOS 26.4.1 arm64, 24GB RAM, 238GB free disk, Docker Desktop 26.x.

Root cause: the GHCR image is too large for the Docker Desktop arm64 pull path on this hardware. Memory is not the bottleneck — transfer speed and image size are.

## The working workaround: Brev GPU cloud instance

Use a Brev GPU cloud instance instead of local MacBook:

1. Spin up a Brev instance at `https://brev.nvidia.com`
2. Recommended instance type: **MASSEDCOMPUTE L40S** — 48GB VRAM, 128GB RAM, 22 CPUs, 625GB SSD, ~$1.06 USD/hr
3. The instance runs native Linux Docker — no arm64 translation layer, no GHCR pull issues
4. Use **NVIDIA cloud endpoints** for inference (`nvidia/nemotron-3-super-120b-a12b`), not local Ollama

## Brev CLI is dead — use Jupyter terminal instead

As of June 2026, the Brev CLI install paths no longer work:

- `curl -sL https://raw.githubusercontent.com/brevdev/brev-cli/main/install.sh | sh` — returns 404
- `brew install brevdev/tap/brev` — GitHub repository not found

**Fallback access method:**

1. In the Brev console, under the running instance, find the **Jupyter** service on port 8888
2. Click the secure URL (format: `https://jupyter-<id>.brevlab.com/lab`)
3. It opens Jupyter Lab through NVIDIA SSO — the user must be signed into NVIDIA in their browser
4. In Jupyter Lab, click **Terminal** (Launcher → Terminal or File → New → Terminal)
5. This gives a shell directly on the cloud instance — root access, native Docker, full GPU

From the Jupyter terminal, run the NemoClaw Hermes install normally:
```bash
curl -fsSL https://www.nvidia.com/nemoclaw.sh | bash
export NEMOCLAW_AGENT=hermes
nemohermes onboard
```

## Cleanup after failed local install

If a local MacBook install was attempted and partially completed, clean up:

```bash
# Kill running processes
pkill -f nemohermes
pkill -f openshell-gateway
pkill -f ollama-auth-proxy

# Remove binaries
rm -f ~/.local/bin/nemohermes ~/.local/bin/nemoclaw ~/.local/bin/openshell ~/.local/bin/openshell-gateway

# Uninstall npm global
npm uninstall -g nemoclaw

# Remove state directories
rm -rf ~/.local/state/nemoclaw ~/.nemoclaw ~/.local/share/openshell ~/.ollama

# Uninstall Homebrew packages (ollama, skopeo)
brew uninstall ollama skopeo

# Prune all Docker images, containers, and build cache
docker system prune -a -f --volumes

# Remove install source directory
rm -rf ~/Desktop/hermes_builds/nemoclaw-install
```

Do NOT uninstall Docker Desktop — it is likely a pre-existing user install, not installed for NemoClaw.

## Key architectural decision

For testing NemoClaw: **Brev cloud instance with NVIDIA endpoints, not local MacBook.**

For production AgentOS: **DGX Spark or MacBook Pro 128GB as dedicated headless appliance, not the daily-driver laptop.**

The MacBook Air (24GB) is not powerful enough to serve as both daily driver and NemoClaw host. The MacBook Pro M5 Max 128GB or DGX Spark are the serious options.
