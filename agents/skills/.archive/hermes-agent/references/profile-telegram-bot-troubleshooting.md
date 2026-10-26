# Profile Telegram Bot Troubleshooting

Use this when a newly-created BotFather bot exists but does not reply.

## Core concept

A Telegram bot token only creates the bot identity. It does not make the agent answer. The profile needs either:

1. The standard Hermes profile gateway running for that profile, preferred, or
2. A custom polling/webhook handler, only when the gateway path is unavailable.

## Preferred path

1. Confirm profile name:
   ```bash
   hermes profile list
   ```
2. Put the bot token in the profile-specific `.env`, not the default profile:
   ```bash
   echo 'TELEGRAM_BOT_TOKEN=...' >> ~/.hermes/profiles/<profile>/.env
   ```
3. Restrict to Jared's Telegram user ID:
   ```bash
   echo 'TELEGRAM_ALLOWED_USERS=8647481186' >> ~/.hermes/profiles/<profile>/.env
   ```
4. Start/restart the profile gateway:
   ```bash
   hermes --profile <profile> gateway restart
   ```
5. Send a real Telegram test message before saying it is live.

## Common miswire in Jared's stack

When Jared wants one bot per specialist agent, treat the setup as **one token per profile**.

Do not leave a specialist bot token only in the default `~/.hermes/.env` and assume the profile bot will answer. That creates a mixed architecture:

- default profile token exists
- specialist profile gateway is stopped or missing its own token
- BotFather bot identity exists, but the specialist bot stays silent

Diagnosis pattern:
- `hermes --profile <profile> gateway status` shows the specialist gateway is not running
- `~/.hermes/profiles/<profile>/.env` has `TELEGRAM_ALLOWED_USERS` but no active `TELEGRAM_BOT_TOKEN`
- the default `~/.hermes/.env` may still contain a different working bot token

Fix pattern:
- move or add the correct BotFather token into `~/.hermes/profiles/<profile>/.env`
- keep `TELEGRAM_ALLOWED_USERS` in that same profile `.env`
- restart that profile gateway
- verify the token belongs to the intended specialist bot before claiming success

## If using a custom handler

Avoid these failure modes:

- Wrong profile spelling. Jared's profiles commonly omit underscores, e.g. `atticuscounsel`, not `atticus_counsel`.
- Stale Hermes CLI flags. Use:
  ```bash
  hermes -p <profile> chat -q "test message" --quiet
  ```
  Do not use `--once` or `--no-color`.
- Markdown parse failures. Send plain text unless output is escaped.
- Environment variables not loaded in background processes. Start with `source ~/.zshrc && python3 handler.py` or put secrets in the profile `.env` instead.

## Behaviour standard for Jared

If tool access is available, do not keep asking Jared to run commands. Make the config changes, restart the process, and verify. Jared should only need to test the final Telegram message if external interaction is unavoidable.
