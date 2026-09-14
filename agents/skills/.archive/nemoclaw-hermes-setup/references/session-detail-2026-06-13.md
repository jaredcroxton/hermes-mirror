# NemoClaw Hermes Setup — Session Detail

Date: 13 June 2026
Installer version: v0.0.55
Hermes sandbox base image: ghcr.io/nvidia/nemoclaw/hermes-sandbox-base:v0.0.55

## Hardware Tested

- MacBook Air M5, 24GB RAM, macOS 26.4.1, arm64
- Docker Desktop 4.69.0, 10 vCPU allocated
- Docker memory: 7.75GB (too low) → 11.67GB (adequate)

## Install Path Walkthrough

The `curl | bash` bootstrap script pulls from `https://github.com/NVIDIA/NemoClaw.git`, clones the `lkg` ref, then runs `scripts/install.sh`.

After install, binaries land at:
- `~/.local/bin/nemohermes` (shell wrapper → npm global bin)
- `~/.npm-global/bin/nemohermes` (Node.js symlink)
- `~/.npm-global/lib/node_modules/nemoclaw/bin/nemohermes.js`
- State at `~/.local/state/nemoclaw/`
- Source at `~/.nemoclaw/source/`

## NVIDIA Endpoints Model Catalog

Verified 121 models at `https://integrate.api.nvidia.com/v1/models`. Key models for NemoHermes:

| Model ID | Label |
|----------|-------|
| `nvidia/nemotron-3-super-120b-a12b` | Nemotron 3 Super 120B (default) |
| `nvidia/nemotron-3-nano-omni-30b-a3b-reasoning` | Nemotron 3 Nano Omni 30B |
| `z-ai/glm-5.1` | GLM-5 |
| `minimaxai/minimax-m2.7` | MiniMax M2.7 |
| `moonshotai/kimi-k2.6` | Kimi K2.6 |
| `openai/gpt-oss-120b` | GPT-OSS 120B |
| `deepseek-ai/deepseek-v4-pro` | DeepSeek V4 Pro |

## Provider Config in NemoClaw Source

The NemoClaw `providers.js` maps onboarding option 1 → `build` → provider name `nvidia-prod` → endpoint `https://integrate.api.nvidia.com/v1` → credential env `NVIDIA_API_KEY`.

## Docker Daemon Check

```bash
docker info --format 'OSType={{.OSType}} Architecture={{.Architecture}} CPUs={{.NCPU}} Memory={{.MemTotal}}'
docker ps --format '{{.Names}} {{.Status}}' | head -5
nemohermes list
```

## Brev Escape Hatch

When Docker pulls or builds stall on macOS, use NVIDIA Brev:

1. Go to `https://brev.nvidia.com`
2. Sign in with NVIDIA account
3. Open running instance or launch new
4. Find Connect → SSH → copy command
5. Send SSH command to Brock

Brock will SSH in and complete the NemoHermes install on the cloud instance where Docker and GHCR access are fast.
