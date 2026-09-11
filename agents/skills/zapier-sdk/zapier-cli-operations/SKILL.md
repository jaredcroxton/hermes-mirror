---
name: zapier-cli-operations
description: Use when setting up, authenticating, auditing, or exploring Zapier SDK CLI connections and actions before writing production TypeScript SDK code. Covers login, package setup, connection inventory, app action discovery, and safe live-test decisions.
---

# Zapier CLI Operations

Use this skill when the task is to configure or inspect Zapier access from the terminal, especially before building an integration or agent tool with the Zapier SDK.

This is the operator-facing companion to the broader `zapier-sdk` skill. It focuses on CLI discovery and verification.

## When to use

- User asks to install or authenticate Zapier SDK/CLI.
- User asks what Zapier apps are connected.
- User asks whether Gmail, Calendar, Sheets, Slack, or another app is ready to use through Zapier.
- User asks to inspect app actions or required inputs before coding.
- User asks to run a one-off Zapier action from the terminal.

## Setup check

From the relevant project or working directory:

```bash
npx zapier-sdk --version
```

If not installed:

```bash
npm install @zapier/zapier-sdk
npm install -D @zapier/zapier-sdk-cli @types/node typescript tsx
```

Authenticate:

```bash
npx zapier-sdk login
```

If browser login succeeds, verify with a low-risk read:

```bash
npx zapier-sdk list-connections --owner me --json
```

## Connection inventory workflow

Use JSON output, not prose output, when auditing connections:

```bash
npx zapier-sdk list-connections --owner me --json 2>/dev/null
```

Read the returned `data` array.

Key fields:

- `id`: connection ID to pass into SDK or CLI actions.
- `title`: connected account label, often an email address.
- `app_key`: exact app key exposed by Zapier, for example `GoogleSheetsV2CLIAPI`, `GoogleCalendarCLIAPI`, `GoogleMailV2CLIAPI`.
- `implementation_id`: app key plus version.
- `is_expired`: may appear as a string, for example `"false"`, not a boolean.
- `permissions.use`: whether the connection can be used.

Do not claim there are more pages or hidden connections unless the CLI response exposes pagination or a cursor. If the `data` array has three records, say there are three records.

## Action discovery workflow

List actions for the exact app key found in the connection inventory:

```bash
npx zapier-sdk list-actions GoogleSheetsV2CLIAPI
npx zapier-sdk list-actions GoogleCalendarCLIAPI
npx zapier-sdk list-actions GoogleMailV2CLIAPI
```

If the user names an app that is not connected, do not run a live action test. State the missing connection and skip the test.

## Safe live-test rule

Before running a write action:

1. Confirm the target app has a non-expired connection.
2. Discover the action and its required inputs.
3. Show the exact side effect, for example draft creation, row append, calendar event creation, or message send.
4. Get approval unless the user has already explicitly authorised that exact side effect.

For Gmail, create drafts rather than sending emails unless the user explicitly asks to send.

## Output style for Jared

When reporting a connection audit to Jared:

- Lead with the count and readiness.
- Use bullets or compact key-value lines, not long explanations.
- Name missing connections plainly, for example `No Slack connection is present, so I skipped the Slack DM test.`
- Include only commands that are useful next steps.

## References

- `references/local-connection-audit.md` — concise session-derived pattern for auditing local Zapier SDK CLI connections.
