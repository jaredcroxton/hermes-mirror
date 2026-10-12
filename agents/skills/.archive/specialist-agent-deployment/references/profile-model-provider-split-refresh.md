# Profile model/provider split and gateway refresh

Use this when Jared asks to move a subset of profile-backed agents from one provider to another, while keeping some profiles on a different model.

## Durable pattern

1. **Confirm exact target model/provider before rollout.** Probe the candidate from a known-working profile:
   ```bash
   hermes chat -q "Reply exactly OWL_OK" --provider openrouter -m "openrouter/owl-alpha" --quiet
   hermes chat -q "Reply exactly OPENAI_OK" --provider openai-codex -m "gpt-5.5" --quiet
   ```

2. **Define the split explicitly.** Do not infer from bot names. Example split:
   - OpenAI Codex: `default`, `bobbuilder`, `piperpromptops`
   - OpenRouter Owl Alpha: every previous DeepSeek specialist profile

3. **For key-based providers, copy the provider key into each profile-local `.env`.** Profiles do not inherit default `.env` keys. For OpenRouter, copy `OPENROUTER_API_KEY` from `~/.hermes/.env` into each target profile if missing.

4. **Set config, not just keys.** The profile `config.yaml` must change:
   ```bash
   hermes --profile <profile> config set model.default "openrouter/owl-alpha"
   hermes --profile <profile> config set model.provider "openrouter"
   hermes --profile <profile> config set model.base_url ""
   ```
   Clearing `model.base_url` matters when leaving DeepSeek. A stale `https://api.deepseek.com/v1` base URL can keep routing calls through the wrong endpoint.

5. **For OpenAI Codex profiles, use OAuth provider config only.** No API key or base URL:
   ```bash
   hermes --profile <profile> config set model.default "gpt-5.5"
   hermes --profile <profile> config set model.provider "openai-codex"
   hermes --profile <profile> config set model.base_url ""
   ```

6. **Restart every affected gateway.** Model config is cached by live gateways:
   ```bash
   hermes --profile <profile> gateway restart
   ```
   Use `hermes gateway restart` for the default profile.

7. **Verify the actual profile list and direct reply probes.**
   ```bash
   hermes profile list
   hermes --profile <profile> chat -q "Reply exactly <profile>_OK" --quiet
   ```
   A single timeout can be transient. Retry once before treating it as a failed migration. Capture the retry result, not just the first failure.

8. **Scan recent logs for provider or Telegram errors.** Look for 401s, `authentication fails`, stale DeepSeek base URL behaviour, Telegram conflicts, or model-empty warnings.

## Pitfalls

- `hermes profile list` can show the desired model only after config changes, but the Telegram gateway may still run the old cached model until restarted.
- Copying an API key is not enough. `model.provider`, `model.default`, and stale `model.base_url` are the routing controls.
- OpenRouter models require the OpenRouter key in the profile-local `.env`; OpenAI Codex uses OAuth in `auth.json` and does not need a profile API key.
- Do not capture transient one-off probe timeouts as durable provider failures. Retry once and use the final result.
