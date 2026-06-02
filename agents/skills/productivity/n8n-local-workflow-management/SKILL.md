---
name: n8n-local-workflow-management
description: Import, export, and debug n8n workflows on Jared's local Mac instance (port 5678). Covers CLI import format requirements, REST API auth gap, and credential reconnection.
---

# n8n Local Workflow Management

Manage n8n workflows running on Jared's local Mac at `http://localhost:5678`. Use when Jared pastes a raw workflow JSON and asks to import it, or when debugging n8n import/export issues.

## Trigger

- Jared pastes a raw n8n workflow JSON and asks to import it
- Jared asks "put this into n8n" or "give me a localhost link"
- n8n import fails and needs debugging
- Workflows need exporting for backup or sharing

## Architecture

### Step 1: Check n8n is running

```bash
curl -s http://localhost:5678/healthz
```

Expected: `{"status":"ok"}`. If not running, start with `n8n start` or `npx n8n`.

### Step 2: Normalise the workflow JSON

Raw workflow JSON shared by users (pasted into chat) is almost always MISSING the top-level fields n8n's import CLI requires. The import will fail with `SQLITE_CONSTRAINT: NOT NULL constraint failed: workflow_entity.id` without these.

**Required top-level fields to add:**

```json
{
  "id": "<unique-slug>",
  "updatedAt": "2026-06-02T08:00:00.000Z",
  "createdAt": "2026-06-02T08:00:00.000Z",
  "description": "<one-line summary>",
  "active": false,
  "isArchived": false,
  "name": "...",
  "nodes": [...],
  "connections": {...},
  "settings": {...}
}
```

The `id` field must be a unique string. Use a recognisable slug (e.g. `Ag3nt1cV1b3L1nk3d1n`). Timestamps use ISO 8601 format. Keep `active: false` on import — let Jared activate manually.

### Step 3: Import via CLI (not REST API)

The n8n REST API (`/rest/workflows`) returns `Unauthorized` without a session cookie. The CLI works locally without auth:

```bash
n8n import:workflow --input=/tmp/workflow.json
```

### Step 4: Verify and share the URL

After successful import, the workflow is available at:

```
http://localhost:5678/workflow/<id>
```

Share this URL directly. The workflow opens in the n8n editor.

### Step 5: Flag credential gaps

Imported workflows with placeholder credentials (e.g. `"credential-id"`) will show disconnected nodes. Always scan the JSON before import and flag which credential types need reconnection:

- OpenAI API (`openAiApi`)
- LinkedIn OAuth2 (`linkedInOAuth2Api`)
- Any other service credentials

Tell Jared explicitly which nodes need credentials reconnected before the workflow can run.

## Exporting workflows

To see the correct import format, export an existing workflow first:

```bash
n8n export:workflow --all --pretty --output=/tmp/n8n-export.json
```

This produces an array of workflow objects with all required fields. Use this as a reference for the expected import shape.

## Pitfalls

- **REST API returns `{"status":"error","message":"Unauthorized"}`.** Do not try `curl -X POST /rest/workflows` even with correct JSON — it needs a browser session cookie that the CLI does not require. Always use `n8n import:workflow` CLI.
- **Missing top-level `id` field.** Raw shared JSON almost never includes `id`, `updatedAt`, `createdAt`, `description`, `active`, or `isArchived`. Add them or the import fails with `NOT NULL constraint failed: workflow_entity.id`.
- **`n8n import:workflow` produces `SQLITE_CONSTRAINT: NOT NULL constraint failed: workflow_entity.id`.** This means the JSON is missing required top-level fields (see Step 2 above). Add `id`, `updatedAt`, `createdAt`, then retry.
- **n8n binary location.** It lives at `/Users/jc/.npm-global/bin/n8n`. If `n8n` is not found, use the full path or check that `~/.npm-global/bin` is in `$PATH`.
- **Workflow already exists.** If you import a workflow with an `id` that already exists in the database, n8n WILL overwrite it silently. Choose unique slugs to avoid accidentally clobbering existing work.
