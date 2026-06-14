# Brev Cloud SSH Workflow for NemoClaw Hermes

When local MacBook Docker cannot pull the hermes-sandbox-base image, use a Brev cloud instance as the runtime and the MacBook as the control surface.

## Instance Selection

Pick the cheapest GPU instance with ≥32GB RAM:

**Recommended (June 2026):** MASSEDCOMPUTE L40S
- 48GB VRAM, 128GB RAM, 22 CPUs, 625GB SSD
- $1.06/hr USD (~A$1.60/hr)
- Deploys in ~2.5 minutes
- Warning: "No stop/start" — data lost on stop. Treat as disposable test instance.

## Workflow

1. User signs into `https://brev.nvidia.com`
2. User creates instance: VM Mode w/ Jupyter, no launchable, no setup script
3. Instance deploys → Brev console shows SSH command
4. User sends SSH command to Brock
5. Brock SSHs in and runs full NemoHermes install:
   ```bash
   export NEMOCLAW_AGENT=hermes
   curl -fsSL https://www.nvidia.com/nemoclaw.sh | bash
   ```
6. Brock configures NVIDIA Endpoints provider with `nvidia/nemotron-3-super-120b-a12b`
7. Brock verifies sandbox creation, dashboard URL, and API health
8. User accesses dashboard via SSH port forward or public tunnel

## SSH Port Forward for Dashboard Access

```bash
ssh -L 18789:localhost:18789 -L 8642:localhost:8642 ubuntu@<brev-ip>
```

Then open `http://localhost:18789/` on the MacBook.

## Key Difference from Local Install

- No Docker Desktop memory limits
- No GHCR arm64 pull issues
- Native Linux Docker daemon
- ~4-minute full install vs hours of stalled pulls on MacBook
