# Specialist verification: profile brain vs live transport

## Purpose

Use this when reviewing whether a specialist agent is truly live.

A specialist can have a correct soul and working local profile but still not be live on Telegram or another transport. Treat these as separate checks.

## Verification layers

### 1. Soul/source-of-truth check

Confirm the canonical soul file exists and the profile points to it.

Prefer a symlink from:

`~/.hermes/profiles/<profile>/SOUL.md`

To:

`/Users/jc/Desktop/Obsidian/Agents/<Agent>-Soul.md`

Do not assume the link. Check it.

### 2. Props/support library check

If the soul references supporting files, confirm those files exist before saying the agent has its full brain.

Typical examples:

- `agent-architecture.md`
- `workflow.md`
- schema files
- prompt templates
- style profiles

### 3. Local profile brain check

Run an identity probe through the profile, not the gateway:

```bash
hermes --profile <profile> chat -q "Who are you? Reply in two short sentences." --quiet
```

If this works, the local profile brain is functional.

### 4. Gateway/transport check

Start or restart the profile gateway and inspect status/logs.

```bash
hermes --profile <profile> gateway restart
hermes --profile <profile> gateway status
```

Then inspect the profile gateway log for platform connection errors.

### 5. End-to-end live check

Only call the bot live when the transport has connected and an actual message round-trip succeeds.

## Reporting language

Use precise status:

- **Soul ready** means the canonical instructions are in place.
- **Profile brain works** means the local `hermes --profile ... chat` probe succeeded.
- **Gateway loaded** means the launchd/system service is running.
- **Live on Telegram** means Telegram connected and replied end to end.

Do not collapse these into one "live" claim.

## Common pitfall

A cloned or specialist profile may have its own `.env`. The default profile can have working platform credentials while the specialist profile does not. Put transport credentials in the profile-local `.env` and restart that profile gateway.

Do not save or quote live tokens in handoffs, logs, packages, or skill references.
