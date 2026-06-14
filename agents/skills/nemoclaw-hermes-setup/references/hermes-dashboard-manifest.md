# Hermes Dashboard — Manifest Evidence

## Source
`NVIDIA/NemoClaw` repo, `agents/hermes/manifest.yaml`

## Dashboard configuration (confirmed)
- **Type:** `ui`
- **Label:** "Dashboard"
- **Port:** 18789 (exposed via socat inside the sandbox container)
- **Auth:** session-based, Bearer token via `API_SERVER_KEY`
- **Mechanism:** NemoClaw prebakes dashboard assets, launches `hermes dashboard` inside the sandbox, then exposes it on port 18789 through socat

## CLI gap
`nemoclaw hermes dashboard-url --quiet` returns "not applicable" because the CLI looks for an OpenClaw-specific endpoint path. The Hermes dashboard exists but the CLI does not know how to generate a URL for it.

## Verified: 13 June 2026
- Sandbox build: `nemoclaw onboard --agent hermes`
- Container: `openshell-hermes-*`
- Dashboard confirmed running inside container at port 18789
- `hermes dashboard` inside sandbox returns `http://127.0.0.1:9119` (Hermes web UI port)
- Port 18789 is the socat-bridged external port for the dashboard
