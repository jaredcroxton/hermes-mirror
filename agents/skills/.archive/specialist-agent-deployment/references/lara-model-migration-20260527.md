# Lara Model Migration — 27 May 2026

## Symptoms

- `Provider authentication failed` on gateway start
- Gateway loads but agent cannot respond to any message
- Profile config shows `model.default: gpt-5.4` with `model.provider: openai-codex`

## Root cause

openai-codex OAuth token expired or gpt-5.4 model unavailable through that provider. The profile was configured before the migration to DeepSeek.

## Fix applied

```bash
hermes --profile laralearning config set model.default "deepseek-v4-pro"
hermes --profile laralearning config set model.provider "deepseek"
hermes --profile laralearning config set model.base_url "https://api.deepseek.com/v1"
grep -q 'DEEPSEEK_API_KEY' ~/.hermes/profiles/laralearning/.env || grep 'DEEPSEEK_API_KEY' ~/.hermes/.env >> ~/.hermes/profiles/laralearning/.env
hermes --profile laralearning gateway restart
```

## Verification

Gateway status shows loaded. Agent responds to identity probe via CLI or Telegram. The model migration itself completes without restarting the gateway service.

## Other profiles on gpt-5.4 / openai-codex

Check all profiles for the same issue:
```bash
grep -r "gpt-5.4\|openai-codex" ~/.hermes/profiles/*/config.yaml
```

Any profile still on gpt-5.4/openai-codex is at risk of the same silent timeout. Migrate preemptively to DeepSeek using the same three config changes above.
