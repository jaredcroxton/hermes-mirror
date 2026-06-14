# NemoHermes macOS with NVIDIA Endpoints

Session-derived notes from a MacBook NemoClaw Hermes onboarding attempt.

## Core lesson

A local dashboard URL is not proof that the dashboard exists. `http://127.0.0.1:18789/` only loads after the Hermes sandbox has been created and the dashboard port forward is running.

If only OpenShell is running on port `8080`, the sandbox is not ready yet.

## Observed state pattern

Working components:

- `nemohermes` installed
- `nemoclaw` installed
- `openshell` installed
- Docker Desktop running
- OpenShell gateway listening on `127.0.0.1:8080`

Incomplete components:

- no registered NemoHermes sandbox
- no process listening on `18789`
- no process listening on `8642`
- no dashboard to load
- no API health endpoint to verify

## Commands that identified the issue

```bash
nemohermes list

docker ps --format 'table {{.Names}}\t{{.Status}}\t{{.Ports}}\t{{.Image}}'

lsof -nP -iTCP:18789 -sTCP:LISTEN || true
lsof -nP -iTCP:8642 -sTCP:LISTEN || true
lsof -nP -iTCP:8080 -sTCP:LISTEN || true

curl -sS -m 3 -I http://127.0.0.1:18789/ || true
curl -sS -m 3 http://127.0.0.1:8642/health || true
```

## Port meanings

- `18789`: Hermes dashboard
- `8642`: Hermes OpenAI-compatible API
- `8080`: OpenShell gateway

If `8080` is up but `18789` and `8642` are closed, OpenShell is running but Hermes is not yet serving.

## NVIDIA Endpoints path

For a MacBook test, NVIDIA Endpoints are cleaner than local Ollama when the goal is to prove NemoClaw and Hermes sandboxing.

Required environment variable:

```bash
NVIDIA_API_KEY
```

Docs describe NVIDIA Endpoints as routing to models hosted on `build.nvidia.com`. During onboarding, choose:

```text
1) NVIDIA Endpoints
```

If the key is missing, do not continue guessing. State that `NVIDIA_API_KEY` must be added first.

## Clean restart pattern

If onboarding stalls during sandbox creation and no sandbox exists, kill stale onboarding and stale image pulls before restarting.

```bash
pkill -f 'docker pull ghcr.io/nvidia/nemoclaw/hermes-sandbox-base' 2>/dev/null || true
pkill -f 'nemohermes onboard' 2>/dev/null || true
```

Then rerun:

```bash
export NEMOCLAW_AGENT=hermes
nemohermes onboard
```

Choose NVIDIA Endpoints if `NVIDIA_API_KEY` is present.

## Verification gate

Do not report success until all of these have passed:

```bash
nemohermes list
nemohermes <sandbox-name> status
nemohermes <sandbox-name> dashboard-url --quiet
curl -sf http://127.0.0.1:8642/health
```

Then open the dashboard and confirm it renders.

## Communication pattern for Jared

Use this wording:

- `18789` is not loading because the sandbox did not finish creating.
- The URL is right, but the service is not running yet.
- The better next path is NVIDIA Endpoints, not local Ollama, for this MacBook proof.
- Add `NVIDIA_API_KEY`, then rerun onboarding and choose NVIDIA Endpoints.
