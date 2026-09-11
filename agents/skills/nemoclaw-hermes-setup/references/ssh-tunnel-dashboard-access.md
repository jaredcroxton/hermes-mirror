# SSH Tunnel Dashboard Access for NemoClaw on Brev Cloud Instances

When Brev's "Share a Service" is blocked by the cloud provider (e.g. MASSEDCOMPUTE/shadeform), the SSH tunnel is the reliable fallback for accessing the NemoClaw dashboard at port 18789.

## Prerequisites

- Cloud instance is running and reachable via SSH (check: `ssh -o ConnectTimeout=5 shadeform@<ip> echo ok`)
- Jupyter Terminal access on the instance (to enable password auth)
- Instance IP address (e.g. `216.81.248.17`)

## Full workflow

### Step 1: Enable password auth on the instance

Run from Jupyter Terminal on the instance:

```bash
sudo sed -i 's/^PasswordAuthentication no/PasswordAuthentication yes/' /etc/ssh/sshd_config
sudo sed -i 's/^#PasswordAuthentication yes/PasswordAuthentication yes/' /etc/ssh/sshd_config
echo -e 'performos123\nperformos123' | sudo passwd shadeform
sudo systemctl restart sshd
```

### Step 2: Open SSH tunnel from local Mac

```bash
ssh -o StrictHostKeyChecking=no -L 18789:127.0.0.1:18789 shadeform@216.81.248.17
```

Password: REDACTED

### Step 3: Get the dashboard URL

In a separate session (or before opening the tunnel), get the full tokenized URL from the instance:

```bash
nemoclaw hermes-sandbox dashboard-url --quiet
```

Output format: `http://127.0.0.1:18789/#token=<long-token-string>`

### Step 4: Open in Chrome

On the local Mac, open Chrome and navigate to the tokenized URL. The SSH tunnel forwards `127.0.0.1:18789` on the Mac to `127.0.0.1:18789` on the cloud instance.

## Troubleshooting

| Symptom | Cause | Fix |
|---------|-------|-----|
| `Permission denied (publickey)` | Password auth still disabled | Re-run step 1, verify with `sudo grep PasswordAuthentication /etc/ssh/sshd_config` |
| `Connection refused` on port 18789 | Sandbox not running | Run `nemoclaw hermes-sandbox status` on the instance |
| Dashboard shows "Auth required" | Token missing | Use the full tokenized URL, not just `http://127.0.0.1:18789/` |
| SSH connection drops when lid closed | Mac sleep | Use `caffeinate` or Amphetamine to keep Mac awake |

## Why this works when Brev port sharing doesn't

- Brev "Share a Service" relies on the cloud provider allowing port modifications
- MASSEDCOMPUTE/shadeform explicitly blocks this
- SSH tunneling bypasses Brev entirely — it's a direct TCP connection between your Mac and the instance
- The `-L 18789:127.0.0.1:18789` flag tells SSH: "forward my local port 18789 to the remote's port 18789"
