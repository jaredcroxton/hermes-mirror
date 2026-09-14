# Brev Cloud Instance Pattern

Session reference: 13 June 2026 — full NemoClaw Hermes deployment on MASSEDCOMPUTE L40S via Brev.

## Instance selection

- **Provider:** MASSEDCOMPUTE (via Shadeform) on Brev
- **GPU:** NVIDIA L40S, 48GB VRAM
- **RAM:** 128GB advertised, 70GB actual (brev console shows 128GB, `free -h` shows 70GB — Brev may reserve memory)
- **Storage:** 625GB SSD
- **CPUs:** 22 vCPUs (Intel Xeon Platinum 8452Y)
- **OS:** Ubuntu 22.04.5 LTS, kernel 6.8.0-90-generic
- **Docker:** 29.1.5, CDI GPU support detected
- **Cost:** $1.06/hr USD (~A$1.60/hr AUD)
- **Limitation:** "No stop/start" — data lost on stop. Ephemeral instance.
- **Region:** Des Moines, IA, USA
- **IP:** 216.81.248.17 (example — changes per spin-up)

## Access flow

### Primary: JupyterLab via Brev secure tunnel

1. Instance creates a JupyterLab secure link: `https://jupyter-<id>.brevlab.com/lab`
2. URL is protected by NVIDIA SSO — user must be signed into NVIDIA in Chrome
3. From JupyterLab: File → New → Terminal → full shell on the instance
4. User is `shadeform@shadecloud`, home directory at `/home/shadeform`

### Fallback: SSH tunnel from Mac

SSH password auth is disabled by default. Enable it:

```bash
sudo sed -i 's/^PasswordAuthentication no/PasswordAuthentication yes/' /etc/ssh/sshd_config
sudo sed -i 's/^#PasswordAuthentication yes/PasswordAuthentication yes/' /etc/ssh/sshd_config
echo -e 'temppass\ntemppass' | sudo passwd shadeform
sudo systemctl restart sshd
```

Then from Mac:
```bash
ssh -o StrictHostKeyChecking=no shadeform@<instance-ip>
```

### Port forwarding via Brev console

The "Share a Service" feature in Brev Console only works for pre-configured ports (8888 for Jupyter). The "Expose Port(s)" field under "Using Ports" may be blocked by the cloud provider ("This cloud provider doesn't allow the modifications of ports"). When blocked, use SSH tunnels instead.

## Cleanup when done

```bash
# Inside sandbox: /exit
# Then exit back to host

# Destroy sandbox (keep gateway for faster next onboard):
nemoclaw hermes destroy
# Type 'yes'
# Press Enter to keep gateway

# Then in Brev console: Stop instance
```

## Key timings

- Instance spin-up: 2.5 minutes
- Docker pull of hermes-sandbox-base image: 3-8 minutes (cloud — fast; macOS fails)
- Onboarding wizard: ~5 minutes of user interaction
- Total end-to-end: ~15 minutes from spin-up to live sandbox
