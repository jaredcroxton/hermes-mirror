# Brev Cloud NemoClaw Hermes Onboarding Flow

Full interactive onboarding prompt sequence as of June 2026, running on a Brev MASSEDCOMPUTE L40S cloud instance via Jupyter Terminal.

## Pre-condition

Instance is running. Terminal access via Jupyter Lab (`https://jupyter-<id>.brevlab.com/lab` → Terminal). Docker and GPU confirmed with `nvidia-smi && docker --version`.

## Step 1: Download and run installer

```bash
curl -fsSL https://www.nvidia.com/nemoclaw.sh | bash
```

This runs steps 1/8 through 8/8 of the installer. It installs the CLI, starts the OpenShell gateway, and drops into the interactive onboarding wizard.

## Step 2: Firewall fix (cloud-only)

If step 2/8 fails with:

```
Sandbox containers cannot reach the gateway at host.openshell.internal:8080
```

Run:

```bash
sudo ufw allow from 172.18.0.0/16 to 172.18.0.1 port 8080 proto tcp
nemoclaw onboard
```

## Step 3: Stale gateway fix

If onboarding reports port 8080 blocked by a stale openshell PID:

```bash
sudo kill <PID>
sleep 2
nemoclaw onboard
```

## Step 4: Inference provider

```
Choose [1]:
```

Type `1` (NVIDIA Endpoints).

## Step 5: API key

```
NVIDIA API key:
```

Paste the `nvapi-*` key. The installer stages it in process memory only — nothing written to disk.

## Step 6: Model selection

```
Cloud models:
    1) Nemotron 3 Super 120B (nvidia/nemotron-3-super-120b-a12b)
    ...
Choose model [1]:
```

Type `1` (Nemotron 3 Super 120B). This is NVIDIA's flagship and the best model for validating the full NemoClaw inference path.

## Step 7: Sandbox name

```
Sandbox name (1-63 characters, ...) [my-assistant]:
```

Type a meaningful name, e.g. `hermes-sandbox`. Must be lowercase, letters/numbers/hyphens only.

## Step 8: Configuration review

```
Apply this configuration? [Y/n]:
```

Type `y` or press Enter.

## Step 9: Brave Web Search

```
Enable Brave Web Search? [y/N]:
```

Type `n` or press Enter. Not needed for validation.

If Enter alone does not skip, leave the API key prompt blank and press Enter.

## Step 10: Messaging channels

```
Available messaging channels:
    [1] ○ telegram
    [2] ○ discord
    ...
Press 1-5 to toggle, Enter when done:
```

Press Enter (none selected). Not needed for sandbox validation.

## Step 11: Resource profile

```
Resource profiles:
    1) creator
    2) gamer
    ...
    6) No profile (OpenShell defaults)
Choose [6]:
```

Press Enter (option 6, no profile). Inference is cloud-routed, so resource caps are not needed for validation.

## Step 12: Verification

After onboarding completes:

```bash
nemohermes list
nemohermes hermes-sandbox status
nemohermes hermes-sandbox dashboard-url --quiet
curl -sf http://127.0.0.1:8642/health
```

Then open the dashboard URL in the browser. On a Brev instance, the dashboard is accessible via the "Share a Service" port-forward URL, not `localhost` directly.
