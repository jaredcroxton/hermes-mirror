# Telegram specialist bot wiring and verification notes

## Durable lesson

A BotFather token only proves the Telegram bot identity exists. A specialist agent is not live until the profile gateway can read the profile-local `.env`, connect Telegram polling, and answer or receive a real chat.

## Correct sequence

1. Put the BotFather token in the specialist profile `.env`, not the default profile:

```bash
TELEGRAM_BOT_TOKEN=REDACTED
TELEGRAM_ALLOWED_USERS=8647481186
```

2. If the bot should send cron or home-channel messages back to Jared after he starts the chat, set:

```bash
TELEGRAM_HOME_CHANNEL=8647481186
```

3. Verify token validity before gateway restart:

```bash
curl -s "https://api.telegram.org/bot$TELEGRAM_BOT_TOKEN/getMe" | python3 -m json.tool
```

Expected: `ok: true` and the expected username.

4. Restart the profile gateway:

```bash
hermes --profile <profile> gateway restart
```

5. Check the profile gateway log for:

```text
Connected to Telegram (polling mode)
✓ telegram connected
Gateway running with 1 platform(s)
```

6. Ask the user to open the bot and press **Start** if a proactive send fails with:

```text
Bad Request: chat not found
```

This is normal for a brand-new bot. Telegram will not let the bot message a user until the user has initiated the chat.

## Reporting standard

Separate the status clearly:

- Token valid via getMe
- Profile gateway connected
- User has or has not pressed Start
- End-to-end reply confirmed or still pending

Do not claim the Telegram bot is fully live until the final end-to-end message path is proven.
