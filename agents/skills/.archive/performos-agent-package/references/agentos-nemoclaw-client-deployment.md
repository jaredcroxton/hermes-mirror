# AgentOS NemoClaw Sandbox — Client Deployment Reference

Prepared 14 June 2026 after cloud-instance validation (Brev NVIDIA L40S GPU, 128GB RAM) and three NVIDIA/YouTube deep-dives.

## Strategic framing

NemoClaw is infrastructure. AgentOS is the product layer on top.

| NVIDIA/Nous builds | AgentOS builds |
|---|---|
| OpenShell sandbox runtime | Agent profiles (Brock, Lara, Bob, Harry, etc.) |
| Network policies and token masking | Industry-specific skill libraries |
| Inference routing (NVIDIA Endpoints) | Client onboarding automation |
| OpenShell container lifecycle | Team dashboards and audit UI |
| Hermes Agent (raw) | Managed agent operations |

## Client-facing language

"Your private AI team runs inside an NVIDIA-hardened secure environment. Every agent action is governed by network policies you control. Tokens are masked — the agents never see your API keys. Every session, every tool call, every policy change is logged and auditable."

## Onboarding flow for a client

1. **Discovery call** — map client roles, workflows, data sources, compliance needs
2. **Policy design** — define approved egress targets per sandbox
3. **Agent profile selection** — which AgentOS profiles the client gets (CEO Advisor, HR, L&D, Builder, etc.)
4. **Sandbox creation** — automated via AgentOS onboarding script
5. **Tool connection** — MCP tokens for Gmail, Calendar, CRM, internal systems
6. **Governance walkthrough** — dashboard, audit trail, policy management
7. **Go-live** — agents active inside controlled sandboxes

## Three-layer audit for clients

What the client operations manager sees:

| Layer | What it shows | Source |
|---|---|---|
| Gateway logs | Every egress attempt, ALLOW/DENY, token substitution | `nemoclaw hermes logs` |
| Session history | Every prompt, response, tool call, skill, memory write | Hermes session DB |
| Policy audit | Versioned, hashed, every change logged | `nemoclaw hermes status` |

## Deployment model options

1. **Brev GPU cloud** (testing/proof only) — $1.06/hr L40S, good for validation
2. **Client-site MacBook Pro M5 Max 128GB** — portable demo + local inference
3. **NVIDIA DGX Spark** — reference appliance for serious local deployment
4. **AWS EC2 GPU** — private cloud with GPU, dedicated instance

## Current limitations (June 2026)

- Dashboard URL doesn't work for Hermes sandbox path (OpenClaw only)
- No multi-tenant dashboard yet (August/September target per Chris Murphy)
- "Delightful UX" targeted for June/July
- Local macOS install broken (Docker Desktop arm64 pull timeout)
- Wizard is single-user; enterprise needs custom scripts

## What the demo proves

- Hermes Agent runs inside OpenShell sandbox with GPU passthrough
- Network policies gate all egress in real time (hot-swappable)
- Tokens are masked inside sandbox — agent never sees real credentials
- Session history and audit trail are complete
- Multi-user sandboxes work in parallel
- Telegram bot attachment works through the wizard (press 1 at messaging step)

## Next steps for AgentOS

- Build the automated onboarding script (env vars, policy injection, profile seeding)
- Design the client audit dashboard (wrap gateway logs, session DB, policy versions)
- Package agent profiles as injectable artifacts into sandbox builds
- Wait for NemoClaw multi-tenant dashboard (Aug/Sep target)
- Position as "private AI team inside NVIDIA-hardened sandboxes"
