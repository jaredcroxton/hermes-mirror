# Brev Port Forwarding Pattern

## Basic forward

```bash
brev port-forward <instance-name> -p <local_port>:<remote_port>
```

Examples:
```bash
# Dashboard (if available)
brev port-forward keen-tomato-jackal -p 18789:18789

# Hermes API
brev port-forward keen-tomato-jackal -p 8642:8642
```

## Finding your instance name

```bash
brev ls --json | python3 -c "import sys,json; d=json.load(sys.stdin); [print(i.get('name','')) for i in d.get('workspaces',[])]"
```

Or just: `brev ls`

## Port forward lifecycle

- The forward runs in the foreground and blocks the terminal
- Ctrl+C stops it
- The forward is transient — it dies when the terminal closes
- `http://localhost:<local_port>` is accessible in the browser on the Mac while the forward is running

## When port sharing fails

Brev's "Share a Service" feature is provider-dependent. If the provider blocks port modifications (common with MASSEDCOMPUTE/shadeform), fall back to:

```bash
# On the cloud instance (via brev shell or Jupyter terminal):
sudo sed -i 's/^PasswordAuthentication no/PasswordAuthentication yes/' /etc/ssh/sshd_config
sudo systemctl restart sshd
echo -e 'temppass\ntemppass' | sudo passwd shadeform

# On local Mac:
ssh -o StrictHostKeyChecking=no -L 18789:127.0.0.1:18789 shadeform@<instance-ip>
```

Use a one-time temp password. Delete the instance when done.

## CLI availability

The `brev` CLI is only available on the Mac. It is NOT available on the cloud instance shell. Do not try `brev exec` or `brev shell` from inside the cloud instance terminal.

## Jupyter Terminal as SSH alternative

When the Brev CLI SSH command is unavailable or the Access tab doesn't show a direct SSH command:
1. In Brev console, find the Jupyter URL under "Share a Service"
2. Open it in Chrome (must be signed into NVIDIA/Brev)
3. Click Terminal under the Launcher
4. This gives a shell directly on the cloud instance
