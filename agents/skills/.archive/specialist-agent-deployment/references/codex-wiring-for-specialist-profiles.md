# Codex wiring for profile-backed specialist agents

Use this when Jared wants a specialist Telegram bot/profile to run on OpenAI Codex while keeping other provider keys available for domain-specific setup work.

## Core distinction

A specialist can use Codex as its everyday chatbot brain while still keeping provider keys such as `NVIDIA_API_KEY` in the profile-local `.env` for domain tasks. Example: Neo_NemoClaw can answer through Codex but still guide NVIDIA NemoClaw setup and tell the user to choose Nemotron in the sandbox wizard.

Do not collapse these layers:

- **Specialist profile model:** the model used by the Telegram bot/profile itself.
- **Target sandbox model:** the model selected inside the system the specialist is helping configure.

## Standard config

```bash
hermes --profile <profile> config set model.provider openai-codex
hermes --profile <profile> config set model.default gpt-5.5
# Clear any stale provider endpoint inherited from DeepSeek, OpenRouter, Ollama, or local experiments.
# OpenAI Codex uses the provider's OAuth route, not a profile-specific base_url.
hermes --profile <profile> config set model.base_url "" || true
```

For an all-agent rollout, probe the exact provider/model on the default profile before touching specialist profiles:

```bash
hermes chat -q "Reply exactly OK" --provider openai-codex -m "gpt-5.5" --quiet
```

## Auth handling

OpenAI Codex uses OAuth credentials in `auth.json`, not an API key in `.env`. Profiles are isolated. For a broad rollout, copy the verified default `auth.json` into each affected profile after backing up the old one, then set file mode `0600`. If a direct profile probe fails because Codex auth is missing, do the same targeted copy:

```bash
cp ~/.hermes/profiles/<profile>/auth.json ~/.hermes/profiles/<profile>/auth.json.bak 2>/dev/null || true
cp ~/.hermes/auth.json ~/.hermes/profiles/<profile>/auth.json
chmod 600 ~/.hermes/profiles/<profile>/auth.json
```

## Restart the live Telegram gateway

A CLI probe can pass while the Telegram gateway is still running with cached old provider config. Restart the profile gateway and verify the logs.

Preferred:

```bash
hermes --profile <profile> gateway restart
```

If Hermes refuses because the command is being run from inside a gateway process, restart the target service/process only. Match the target profile, kill it, then start again:

```bash
PID=$(hermes --profile <profile> gateway status 2>/dev/null | awk '/"PID" =/{gsub(/[^0-9]/,"",$3); print $3; exit}')
[ -n "$PID" ] && kill "$PID"
sleep 3
hermes --profile <profile> gateway start
```

Then verify:

```bash
hermes --profile <profile> gateway status
tail -30 ~/.hermes/profiles/<profile>/logs/gateway.log
```

Look for:

```text
Connected to Telegram (polling mode)
✓ telegram connected
```

## Verification standard

Run both probes:

```bash
hermes chat -q "Reply exactly BROCK_CODEX_OK" --quiet
hermes --profile <profile> chat -q "Reply exactly <PROFILE>_CODEX_OK" --quiet
```

For bulk rollouts, verify every profile with a bounded direct probe and record pass/fail by profile. Do not let one slow profile hide the result for the rest of the fleet. A small Python wrapper with `subprocess.run(..., timeout=75)` is a portable way to bound each probe while still continuing through the profile list.

For a Telegram bot, also send a real message to the bot after restart. The profile brain probe is necessary but not sufficient for live transport.

## Common pitfall

If the Telegram bot footer or error still mentions the old provider after a successful CLI probe, the gateway has stale runtime state. Restart the gateway and check logs before changing model config again.
