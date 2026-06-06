---
name: n8n-local-operations
description: Use when installing, running, importing, exporting, or debugging Jared's local n8n instance and workflows on macOS.
version: 1.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [n8n, workflows, local, macos, automation]
    related_skills: []
---

# n8n Local Operations

## Overview

This umbrella covers the whole local n8n lifecycle on Jared's Mac: install/startup, health checks, workflow import/export, debugging, and credential reconnection. Treat workflow JSON as an artifact to preserve unless the user explicitly asks for refactoring.

## When to Use

- Install or launch n8n locally, usually on port 5678.
- Import workflow JSON into the local instance.
- Export, debug, or repair existing workflows.
- Connect or reconnect Gmail/OAuth credentials in n8n.

## Setup and startup

- Prefer the documented local install path (npm/npx as available on the machine).
- Start long-running n8n as a tracked background process and verify `/healthz` or the UI before continuing.
- Record the exact port and profile/home path used.

## Workflow import/export

- Import as-is first. Do **not** rewrite node structure or expression syntax unless validation fails and the fix is obvious.
- Keep a timestamped copy of the original workflow JSON before modifying it.
- Use n8n CLI import/export where possible; note that REST API auth is not always available on the local instance.

## Debugging

- Check n8n process logs, workflow activation state, missing credentials, and node-level errors.
- Credential reconnection is often a UI step; surface it clearly if it cannot be automated.
- If Gmail/OAuth is involved, distinguish n8n credentials from Hermes Google Workspace credentials.

## Verification Checklist

- [ ] n8n process is running and reachable.
- [ ] Workflow import/export command returned success.
- [ ] Credentials needed by activated nodes are present or explicitly flagged.
- [ ] A test execution or dry-run evidence was captured when available.
