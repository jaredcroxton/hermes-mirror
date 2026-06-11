# Profile-backed agents with separate Telegram bots

Use this when a user has multiple Hermes profiles (specialist agents) and wants each one reachable as its own Telegram bot.

## Pattern

Each specialist agent needs its own:

- BotFather bot and token
- Hermes profile (`~/.hermes/profiles/<profile>/`)
- `TELEGRAM_BOT_TOKEN` in that profile's `.env`
- Optional `TELEGRAM_ALLOWED_USERS` / `TELEGRAM_HOME_CHANNEL` in that profile's `.env`
- Running gateway service for that profile

Do not reuse the same Telegram bot token across multiple running profiles. If profiles share a token, polling/gateway ownership conflicts and identity confusion can happen.

## Token handling when the user pastes a BotFather token

If the user pastes a BotFather token in chat while asking you to wire up a profile bot, treat it as a live secret:

1. Store it immediately in the target profile's `.env` as `TELEGRAM_BOT_TOKEN`, replacing any existing token line and avoiding duplicates.
2. Set restrictive `TELEGRAM_ALLOWED_USERS` and `TELEGRAM_HOME_CHANNEL` if the user's Telegram ID is known from the current setup.
3. Lock profile `.env` permissions to `0600`.
4. Verify with `getMe`, but never print the token back in tool output summaries or final replies.
5. If the token was posted into a persistent/shared channel, tell the user they may regenerate it in BotFather for maximum security after setup is verified.

## Manual setup workflow

1. Confirm profile and gateway status:

```bash
hermes profile show <profile>
<alias> gateway status
```

If the profile does not exist yet, create it first and give it a friendly wrapper alias:

```bash
hermes profile create <profile> --clone --no-alias
hermes profile alias <profile> --name <alias>
hermes profile show <profile>
```

Then edit `~/.hermes/profiles/<profile>/SOUL.md` with the specialist identity/persona before starting the gateway.

2. Ask the user to create a fresh bot in `@BotFather` with `/newbot` and provide the resulting token.

3. Store the token in the profile-local `.env`, not in global config and not in a public repo:

```text
~/.hermes/profiles/<profile>/.env
TELEGRAM_BOT_TOKEN=<botfather-token>
TELEGRAM_ALLOWED_USERS=<user-telegram-id>
TELEGRAM_HOME_CHANNEL=<user-telegram-id>
```

If replacing a cloned placeholder token, replace the existing `TELEGRAM_BOT_TOKEN=` line and avoid duplicate token lines.

4. Verify the token before starting the gateway:

```bash
python - <<'PY'
import json, urllib.request
from pathlib import Path
p = Path.home()/'.hermes/profiles/<profile>/.env'
token = next(line.split('=', 1)[1].strip() for line in p.read_text().splitlines() if line.startswith('TELEGRAM_BOT_TOKEN='))
with urllib.request.urlopen(f'https://api.telegram.org/bot{token}/getMe', timeout=20) as r:
    data = json.load(r)
print({'ok': data.get('ok'), 'username': data.get('result',{}).get('username'), 'first_name': data.get('result',{}).get('first_name')})
PY
```

5. Start and verify the profile gateway. Some launchd/service starts report success before `hermes profile list` catches up, so verify twice if needed:

```bash
<alias> gateway start
sleep 3
hermes profile list
<alias> gateway status
# If the profile still shows stopped, wait a few seconds and check again before treating it as failed.
sleep 5
hermes profile list
```

6. Optionally set BotFather-visible bot metadata through Telegram Bot API after `getMe` succeeds. Keep this generic and non-secret; never print or commit the token:

```bash
python - <<'PY'
import json, urllib.parse, urllib.request
from pathlib import Path
p = Path.home()/'.hermes/profiles/<profile>/.env'
token = next(line.split('=', 1)[1].strip() for line in p.read_text().splitlines() if line.startswith('TELEGRAM_BOT_TOKEN='))
base = f'https://api.telegram.org/bot{token}/'

def post(method, data):
    body = urllib.parse.urlencode(data).encode()
    with urllib.request.urlopen(base + method, data=body, timeout=20) as r:
        return json.load(r)

print(post('setMyShortDescription', {'short_description': '<short one-line purpose>'}).get('ok'))
print(post('setMyDescription', {'description': '<longer bot description>'}).get('ok'))
print(post('setMyCommands', {'commands': json.dumps([
    {'command': 'help', 'description': 'Show available Hermes commands'},
    {'command': 'new', 'description': 'Start a fresh session'},
    {'command': 'status', 'description': 'Show session status'},
])}).get('ok'))
PY
```

7. Ask the user to open `t.me/<bot_username>`, press Start, and send `Who are you?`.

## Profile rename / alias cleanup

If the user changes the specialist agent name:

```bash
hermes profile rename <oldprofile> <newprofile>
hermes profile alias <newprofile> --name <preferred_alias>
```

Then update the profile's `SOUL.md` with the new identity, profile name, and alias. Remove stale wrapper scripts only after checking they point to the old profile. Verify with:

```bash
<preferred_alias> chat -q 'Reply with only your name and profile alias.' -Q
```

## Security notes

- Tokens pasted into chat should be treated as exposed; offer to regenerate in BotFather for maximum security.
- Never mirror tokens or user IDs into public repos.
- Keep specialist bots restricted with `TELEGRAM_ALLOWED_USERS` when possible.
- Redact tokens from logs and final replies.
