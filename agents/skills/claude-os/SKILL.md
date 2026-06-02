---
name: claude-os
description: "Connects Hermes to Claude OS — the operator dashboard at localhost:9119. Read sessions, memory, integrations, kanban, dream history."
version: 1.0.0
---

# Claude OS

Use this skill when the user mentions:
- my dashboard
- Claude OS
- second brain
- operator
- what did my Dream say

## Purpose

Connect Hermes to the Claude OS operator dashboard running on loopback at `localhost:9119`.

These endpoints are loopback-only. Use them locally.

## First-run setup

The dashboard ships empty. Populate it before reviewing:

1. `cd ~/code/claude-os && bun run setup` — one-time scan that populates `src/data/live-data.json`
2. `bun run dev` — starts the dashboard (defaults to port 8081, may run on 9119)
3. `bun run scripts/aggregate.ts` — re-scan after new sessions

Without running setup, the dashboard shows zero data across all pages: 0 sessions, 0 agents, 0 workspaces, 0 skills.

## Known dashboard gaps (as of June 2026)

Several routes return 404 because they are not yet built:
- **home** — no root landing page
- **skills-studio** — skill inventory UI not implemented
- **agents** — agent list page not implemented
- **kanban** — kanban board not connected to Hermes kanban.db
- **platforms** — messaging platform config not built
- **coding** — Claude Code workspace browser not built
- **activity** — live agent activity feed not built

Working routes: memory, planner, network, models, providers, gateway, classroom, settings, sessions, workspaces.

The **gateway** page is the heartbeat — if it shows "Stopped" with 0 active agents, nothing else will populate. Start the Hermes gateway first.

## Agent network population

The `/network` page reads from `~/.claude-os/agents/`. To populate it:
1. Create an `agent.json` per profile in `~/.claude-os/agents/<agent-name>/`
2. Define handoff edges: which agents route to which
3. Run the aggregator to pick up new agents

Brock orchestrates all others. Bob, Lara, Harry, Sam, Polly, Nelly, Serge, and Mira report to Brock.

## Endpoints to call

- `GET http://localhost:9119/__live-data` for full state
- `GET http://localhost:9119/__hermes_status`
- `GET http://localhost:9119/__hermes_sessions`
- `GET http://localhost:9119/__hermes_memory`
- `GET http://localhost:9119/__hermes_pantheon`

## Notes

- The endpoints already enforce loopback-only access.
- Use these endpoints to read dashboard state, sessions, memory, integrations, kanban, and dream history.
- Start with `__live-data` when the user wants the broadest operator view.
