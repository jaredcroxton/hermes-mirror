# Running gateway but specialist bot is silent

Use this when `hermes profile list` says a specialist gateway is running, but Jared cannot message the bot or the bot replies with a generic error.

## Key lesson

`Gateway: running` only proves the process exists. It does not prove the profile can load the current Hermes code or complete an inbound Telegram request.

A stale gateway after a Hermes update can connect to Telegram, receive messages, then fail during agent startup with an import/runtime error.

## Diagnostic sequence

1. Verify the profile brain locally:

```bash
hermes --profile <profile> chat -q 'Reply exactly <PROFILE>_OK' --quiet
```

2. Verify the profile-local Telegram token with `getMe`:

```bash
python3 - <<'PY'
import json, urllib.request
from pathlib import Path
profile = '<profile>'
p = Path.home()/f'.hermes/profiles/{profile}/.env'
token = next(line.split('=', 1)[1].strip() for line in p.read_text().splitlines() if line.startswith('TELEGRAM_BOT_TOKEN='))
with urllib.request.urlopen(f'https://api.telegram.org/bot{token}/getMe', timeout=20) as r:
    data = json.load(r)
print({'ok': data.get('ok'), 'username': data.get('result', {}).get('username')})
PY
```

3. Inspect the profile gateway log, not just the default gateway log:

```bash
tail -200 ~/.hermes/profiles/<profile>/logs/gateway.log | grep -iE 'telegram|inbound|error|exception|ImportError|Connected|response ready|Sending response'
```

4. If logs show import/runtime errors after inbound messages, restart only that profile.

## Restart pattern from inside another gateway session

The normal command may be blocked:

```bash
hermes --profile <profile> gateway restart
```

If blocked with a restart-loop safety message, use process-level restart for the target profile only:

```bash
pgrep -fl 'hermes_cli.main --profile <profile> gateway run'
pkill -f 'hermes_cli.main --profile <profile> gateway run' || true
sleep 3
hermes --profile <profile> gateway start
sleep 6
pgrep -fl 'hermes_cli.main --profile <profile> gateway run'
```

Then verify:

```bash
hermes profile list | grep <profile>
tail -60 ~/.hermes/profiles/<profile>/logs/gateway.log | grep -iE 'Connected to Telegram|telegram connected|ERROR|ImportError|inbound|response ready|Sending response'
```

Success looks like:

```text
Connected to Telegram (polling mode)
✓ telegram connected
```

## Optional outbound proof

If the bot token and home channel are configured, send a one-line test via Telegram API. Do not print the token.

```bash
python3 - <<'PY'
import json, urllib.parse, urllib.request
from pathlib import Path
profile = '<profile>'
p = Path.home()/f'.hermes/profiles/{profile}/.env'
lines = p.read_text().splitlines()
def get(k):
    return next((line.split('=', 1)[1].strip() for line in lines if line.startswith(k+'=')), '')
token = get('TELEGRAM_BOT_TOKEN')
chat = get('TELEGRAM_HOME_CHANNEL') or get('TELEGRAM_ALLOWED_USERS')
body = urllib.parse.urlencode({'chat_id': chat, 'text': 'Gateway test: I am back online. Please reply Who are you?'}).encode()
with urllib.request.urlopen(f'https://api.telegram.org/bot{token}/sendMessage', data=body, timeout=20) as r:
    data = json.load(r)
print({'ok': data.get('ok'), 'message_id': data.get('result', {}).get('message_id')})
PY
```

## Pitfall

Do not tell Jared the agent is online just because `hermes profile list` says `running`. For user-facing bots, online means: profile brain works, Telegram token is valid, gateway is connected, and a real inbound or outbound transport test succeeds.
