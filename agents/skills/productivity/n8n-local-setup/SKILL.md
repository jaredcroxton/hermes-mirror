---
name: n8n-local-setup
description: Install, launch, and manage n8n locally on macOS. Import workflows from JSON. Covers npm install, startup, health check, workflow import via CLI, and Gmail OAuth connection.
version: 1.0.0
author: Brock / PerformOS
tags: [n8n, automation, workflow, gmail, npm, localhost]
---

# n8n Local Setup

## Trigger

Use when Jared asks to:
- install n8n locally
- start n8n
- import a workflow JSON into n8n
- connect Gmail to n8n
- build automation workflows replacing the old Zapier MCP approach

## Installation

```bash
npm install -g n8n
```

Expect 2,000+ packages. npm peer dependency warnings are cosmetic — n8n works despite them. The install takes ~60 seconds.

## Startup

```bash
n8n start
```

Runs on `http://localhost:5678`. Health check: `curl http://localhost:5678/healthz` returns `{"status":"ok"}`.

First launch prompts for an owner account (email + password). This is a one-time setup.

**Do NOT** use `&` backgrounding in foreground terminal — use `terminal(background=true)` for the long-lived server process.

## Workflow import

Import a JSON workflow file via CLI (bypasses the web UI auth requirement):

```bash
n8n import:workflow --input="/path/to/workflow.json"
```

This works immediately after install — no owner account required for CLI import. The workflow appears on the canvas when the user opens `http://localhost:5678` and logs in.

## Gmail connection

n8n has a native Gmail node with OAuth. In the n8n editor:
1. Add a Gmail node
2. Click "Connect account"
3. Authenticate via Google OAuth
4. Connection persists — no rotating tokens, no mcporter bridge

This replaces the deprecated Zapier MCP pattern entirely.

## Common workflow sources

| Source | How to get |
|---|---|
| n8n community | `n8n.io/workflows` — browse and download |
| In-editor templates | Click `+` in top bar, browse by category |
| n8n AI builder | Type what you want, it generates the workflow |
| Telegram/shared JSON | Save the pasted JSON to a `.json` file, then CLI import |

## Long-running n8n (background)

For a persistent n8n server that outlasts the terminal session:

```bash
nohup n8n start > /tmp/n8n.log 2>&1 &
```

Check it is still alive: `curl http://localhost:5678/healthz`

## Relationship to Hermes

n8n is a workflow automation engine. Hermes is an AI agent runtime. They serve different purposes:
- **n8n:** "When X happens, do Y." Scheduled, triggered, event-driven.
- **Hermes:** "Answer this question, research this topic, build this thing." Conversational, tool-using, reasoning.

n8n can call Hermes (via webhook or API), and Hermes can trigger n8n workflows. But they are separate systems.

## Pitfalls

- n8n is large (~2,200 packages). First install takes patience.
- Port 5678 must be free. If something else is on it, n8n fails silently — check with `lsof -i :5678`.
- The web UI auth is separate from CLI import. You can import workflows via CLI before creating the owner account.
- npm peer dependency warnings are noisy but harmless during install.
- **Import from Clipboard may not be available** on all n8n versions. Import from File is more reliable.
- **Do not try to reconstruct large JSON workflows from chat.** If Jared pastes raw JSON in Telegram, save it to a temp file (`/tmp/workflow.json`) then use CLI import. Reconstructing 25KB+ JSON in terminal is error-prone.

## Positioning

n8n replaces Zapier for local workflow automation. Key advantage: native OAuth connections (Gmail, Calendar, Sheets) with no rotating tokens. The n8n Gmail node connects once and stays connected.

Zapier MCP was removed 02 Jun 2026. n8n is the replacement path for all automation workflows.
