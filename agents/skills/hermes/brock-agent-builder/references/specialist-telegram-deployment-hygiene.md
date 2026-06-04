# Specialist Telegram deployment hygiene

Use this when a newly built profile-backed specialist agent receives a BotFather token and Jared asks to make the bot operational.

## Durable lesson

A cloned specialist profile can inherit platform credentials from the default profile or another agent. Before calling the bot live, make the profile platform-specific.

For a Telegram-only specialist bot:

1. Store the BotFather token only in the target profile `.env` as `TELEGRAM_BOT_TOKEN`.
2. Copy or set `TELEGRAM_ALLOWED_USERS` and `TELEGRAM_HOME_CHANNEL` if Jared's Telegram ID is known.
3. Lock the profile `.env` to `0600`.
4. Verify the token with Telegram `getMe` before starting the gateway.
5. Set BotFather-visible metadata if useful: name, short description, description, commands.
6. Remove inherited email credentials from the profile `.env` and `config.yaml` unless Jared explicitly wants that specialist reachable by email.
7. Restart the profile gateway and verify `hermes profile list` shows the profile gateway as `running`.
8. Inspect recent gateway logs and confirm the expected platform count. A Telegram-only specialist should show one platform, not Telegram plus inherited email.
9. Ask Jared to press Start in Telegram and send a real identity probe.

## Why this matters

A bot can be correctly connected to Telegram while also silently connecting to inherited Gmail credentials. That is not a token failure. It is profile-clone hygiene. Clean the unwanted platform credentials before declaring the specialist deployed.

## Final reply pattern

Do not repeat the token. Report:

- token stored securely
- getMe verified
- metadata set
- gateway running
- inherited platform credentials removed if applicable
- exact Telegram test message for Jared

Add a short security note if the token was pasted into chat: it works now, but regenerating in BotFather later is the maximum-security option.