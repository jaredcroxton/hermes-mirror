# Switching a Profile to DeepSeek

When agents on `gpt-5.4` via `openai-codex` start timing out, switch them to `deepseek-v4-pro`. This is a per-profile operation.

## When to switch

- Non-streaming API call times out after 300s+ with no response
- `WARNING agent.conversation_loop: API call failed after 3 retries` in error log
- Gateway log shows curator review threads stuck for 30+ minutes
- OpenAI Codex endpoint is unresponsive for a specific profile but working for others

## Steps

```bash
# 1. Set the model and provider
hermes --profile <name> config set model.default "deepseek-v4-pro"
hermes --profile <name> config set model.provider "deepseek"  
hermes --profile <name> config set model.base_url "https://api.deepseek.com/v1"

# 2. Copy the API key from default .env if not present
grep -q 'DEEPSEEK_API_KEY' ~/.hermes/profiles/<name>/.env || \
  grep 'DEEPSEEK_API_KEY' ~/.hermes/.env >> ~/.hermes/profiles/<name>/.env

# 3. Restart the gateway
hermes --profile <name> gateway restart

# 4. Verify with one-shot probe
hermes --profile <name> chat -q "Reply exactly <NAME>_OK" --quiet 2>&1
```

## Verification

- Gateway status shows `✓ Gateway service is loaded`
- One-shot probe returns the expected response within 60s
- No timeout errors in `~/.hermes/profiles/<name>/logs/gateway.error.log`

## Profiles switched (as of 26 May 2026)

- default (Brock): deepseek-v4-pro
- bobbuilder (Bob): deepseek-v4-pro
- pollyperformos (Polly): deepseek-v4-pro
- sergeseo (Serge): deepseek-v4-pro

Remaining profiles (atticuscounsel, harryhr, laralearning, nellynotebook, samstudynerd) are still on gpt-5.4 and may time out when activated.

## Pitfall

- `DEEPSEEK_API_KEY` lives in `~/.hermes/.env` only. Cloned profiles may not inherit it. Always check and copy.
- DeepSeek can return empty when context is overloaded. Keep prompts concise.
- Vision tool fails on DeepSeek (`unknown variant image_url`). Use text-based review for visual outputs.
