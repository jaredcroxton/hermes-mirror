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
