# Hermes API + Telegram Operations (NemoClaw Sandbox)

How to interact with a Hermes Agent sandbox after `nemoclaw onboard --agent hermes` completes. Covers the two access paths: OpenAI-compatible API on port 8642 and Telegram bot.

Last verified: 13 June 2026 on Brev MASSEDCOMPUTE L40S instance, Hermes Agent, NVIDIA Nemotron 120B.

## API access (port 8642)

### Health check

```bash
curl -sf http://127.0.0.1:8642/health
```

### Chat completion

```bash
curl -s http://127.0.0.1:8642/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer *** \
  -d '{"model": "nvidia/nemotron-3-super-120b-a12b", "messages": [{"role": "user", "content": "Say hello and confirm you are Hermes."}]}'
```

A successful response confirms:
- Hermes Agent runtime is alive
- Inference route is working (provider → model)
- OpenShell sandbox networking is healthy
- GPU passthrough is active (if using local GPU)

Expected response shape:

```json
{
    "id": "chatcmpl-...",
    "object": "chat.completion",
    "model": "nvidia/nemotron-3-super-120b-a12b",
    "choices": [{
        "index": 0,
        "message": {
            "role": "assistant",
            "content": "..."
        },
        "finish_reason": "stop"
    }],
    "usage": {...}
}
```

### Remote access (cloud instance)

From local Mac, forward port 8642:

```bash
ssh -o StrictHostKeyChecking=no -L 8642:127.0.0.1:8642 shadeform@<instance-ip>
```

Then `curl http://127.0.0.1:8642/v1/chat/completions ...` from the Mac terminal.

## Telegram bot

### Bot token setup (during onboarding)

During `nemoclaw onboard --agent hermes`, toggle Telegram (`1`) at the messaging channels prompt. Enter the bot token from @BotFather. These rules apply:

- The token is staged in process memory and registered with the gateway — nothing is written to disk.
- At the "Reply only when @mentioned?" prompt, accept `Y` to prevent group-chat noise. Direct messages are unaffected.
- After onboarding, the bot polls `api.telegram.org` from inside the sandbox. Firewall rules must allow this (Balanced policy preset includes Telegram by default).

### Pairing (required after onboarding)

The bot is configured but won't respond until you pair your Telegram account:

```bash
nemoclaw hermes connect
hermes telegram pair
```

This outputs a pairing code. Send that code to the bot on Telegram. After pairing, the bot responds to your messages.

### Verification

Inside the sandbox:

```bash
hermes status
```

Look for:

```
◆ Messaging Platforms
  Telegram      ✓ configured
```

And under Gateway:

```
◆ Gateway Service
  Status:       ✓ running
  PID(s):       <number>
```

If the bot is polling but not responding, check logs:

```bash
nemoclaw hermes logs --tail 50
```

Look for `ALLOWED POST http://api.telegram.org:443/bot[CREDENTIAL]/getUpdates` entries — these confirm the bot is connected and polling. If these appear but the bot doesn't reply, the account is not paired — run `hermes telegram pair`.

## CLI access (inside sandbox)

```bash
nemoclaw hermes connect
```

Prompt changes to `sandbox@<container-id>:~$`. From here:

```bash
hermes status     # full agent diagnostics
hermes doctor     # detailed health check
hermes telegram pair  # pair Telegram account
hermes setup      # reconfigure
```

To exit: `exit` or Ctrl+D. Returns to host prompt.

## Port summary (Hermes vs OpenClaw)

| Port | Hermes (`--agent hermes`) | OpenClaw (default) |
|------|---------------------------|---------------------|
| 8080 | OpenShell gateway | OpenShell gateway |
| 8642 | Hermes OpenAI API | Not used |
| 18789 | Not used | OpenClaw Gateway Dashboard |

## Quick verification flow (Hermes sandbox)

```bash
# 1. Confirm sandbox exists
nemoclaw list

# 2. Enter sandbox
nemoclaw hermes connect

# 3. Check Hermes status
hermes status

# 4. Test API (from host or separate terminal)
curl -s http://127.0.0.1:8642/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer *** \
  -d '{"model": "nvidia/nemotron-3-super-120b-a12b", "messages": [{"role": "user", "content": "Ping"}]}'

# 5. Check Telegram
hermes telegram pair   # if not paired yet

# 6. Check logs
nemoclaw hermes logs --tail 20
```
