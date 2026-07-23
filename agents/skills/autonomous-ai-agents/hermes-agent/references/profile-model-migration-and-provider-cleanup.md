# Profile model migration and provider cleanup

Use this when Jared asks to move all specialist agents to a different model/provider or remove a provider such as Grok/xAI from the stack.

## Key lesson

Do not bulk-change every profile to a model name before verifying that the active provider/account can actually access it. A model can appear plausible but fail at runtime with HTTP 404 or unsupported-model errors.

## Safe sequence

1. Check current profile state:
   ```bash
   hermes profile list
   hermes status --all
   hermes auth list
   ```

2. Identify available auth. For Jared's current no-extra-API-cost ChatGPT path, the working provider is usually `openai-codex`, not OpenAI API key access.

3. Probe candidate models before rollout:
   ```bash
   for m in gpt-5.4 gpt-5.3-codex gpt-5 gpt-5-mini; do
     echo "Testing $m"
     hermes chat -q "Reply exactly OK" --provider openai-codex -m "$m" --quiet 2>&1 | head -20
     echo "---"
   done
   ```

4. Only after one model replies successfully, apply it:
   ```bash
   profiles="atticuscounsel bobbuilder harryhr laralearning nellynotebook pollyperformos samstudynerd"
   hermes config set model.default "gpt-5.4"
   hermes config set model.provider "openai-codex"
   for p in $profiles; do
     hermes --profile "$p" config set model.default "gpt-5.4"
     hermes --profile "$p" config set model.provider "openai-codex"
   done
   ```

5. Restart gateways/handlers and verify with direct profile tests:
   ```bash
   hermes --profile bobbuilder chat -q "Reply exactly BOB_OK" --quiet
   hermes --profile pollyperformos chat -q "Reply exactly POLLY_OK" --quiet
   ```

## Removing Grok/xAI links

Search active configs and auth files:
```bash
grep -Rni "grok\|xai" ~/.hermes/config.yaml ~/.hermes/profiles/*/config.yaml ~/.hermes/auth.json ~/.hermes/profiles/*/auth.json 2>/dev/null || true
```

Places where Grok/xAI may remain after changing `model.default`:
- profile `model.provider: xai-oauth`
- profile `model.base_url: https://api.x.ai/v1`
- `auxiliary.image_gen.provider: xai`
- `auxiliary.image_gen.model: grok-2-image`
- `providers.xai` or `providers.xai-oauth`
- `tts.xai`
- `x_search.model: grok-...`
- `platform_toolsets` containing `x_search`
- `plugins.enabled` containing `image_gen/xai`
- `auth.json` provider or credential pool entries for `xai-oauth`

Back up files before programmatic cleanup. After cleanup, grep again and run profile direct tests.

## Pitfalls

- `gpt-5.5` can fail with HTTP 404 under a team/account even if it looks like a valid future model name. Verify first.
- A ChatGPT/Codex subscription route is not the same as an OpenAI API key route. If there is no `OPENAI_API_KEY`, prefer `openai-codex` only if `hermes auth list` shows valid OpenAI Codex OAuth.
- Profile-local `auth.json` files can have stale or consumed Codex tokens. If main profile works and specialist profiles fail with missing/consumed Codex credentials, copy a cleaned main `auth.json` into profile auth files after backing up, removing unwanted provider entries such as `xai-oauth`.
- `hermes profile list` gateway status can lag behind live processes. Confirm with process checks or direct profile queries before declaring a gateway dead.
- `hermes profile list` model column can show stale data. Always verify the actual model with `hermes config` (default) or `hermes --profile <name> config` (per-profile) before making claims about which model an agent is running. The config file is the source of truth.
- For Atticus, the custom Telegram handler is separate from standard profile gateway status. Restart the handler separately.

## DeepSeek provider: single-profile switch pitfall

When moving a single profile to DeepSeek (or any API-key provider), the API key must be copied into that profile's own `.env`. The default `.env` key is not inherited.

```bash
# Verify the key exists in default
grep DEEPSEEK_API_KEY ~/.hermes/.env

# Copy it into the target profile
echo "DEEPSEEK_API_KEY=REDACTED" >> ~/.hermes/profiles/<profile>/.env
```

Symptom of missing key: HTTP 401 with `'Your api key: ****ired is invalid'`. The gateway may still show as running but direct profile queries will fail. The fix is always the same: copy the key into the profile `.env` and restart the gateway.

This pitfall does not apply to OAuth providers (openai-codex, github-copilot) whose tokens live in `auth.json` and are shared globally.

## DeepSeek provider: silent-stop on large-context workflows

DeepSeek can return empty after multiple tool calls when the context window is heavily loaded. The model does not error — it just stops responding. This is most visible in build-orchestration agents like Bob_Builder that load multiple skills, delegate sub-agents, and run tool-heavy workflows.

Symptoms:
- Model returns empty after a sequence of tool calls
- `⚠️ Model returned empty after tool calls — nudging to continue` in logs
- Sub-agent timeouts (Dexter at 600s) when the orchestrator is on DeepSeek

Fix: for build-orchestration and other heavy-context agents, prefer gpt-5.4 via openai-codex. DeepSeek is fine for short queries and single-job specialist agents (Harry, Nelly, Serge). It is unreliable for agents that load many skills and delegate sub-agents in a single session.

```bash
# Switch a build agent back to gpt-5.4
hermes --profile bobbuilder config set model.default "gpt-5.4"
hermes --profile bobbuilder config set model.provider "openai-codex"
hermes --profile bobbuilder gateway restart
```

## OpenAI Codex timeout → DeepSeek migration

When openai-codex itself becomes unresponsive (not a DeepSeek issue — the reverse direction). A profile on gpt-5.4/openai-codex times out with no response. The curator-review background thread hangs. The gateway starts clean but the agent cannot answer any message.

Symptoms:
- CLI probe: `[Command timed out after 60s]`
- Error log: `Non-streaming API call timed out after 1953s with no response (threshold: 300s)`
- Error log: `Non-streaming API call stale for 3653s`
- Error log: `API call failed after 3 retries. ... provider=openai-codex model=gpt-5.4`
- Gateway shutdown: `signal=SIGTERM` after curator-review thread exhausts retries

The curator-review background thread is usually the first thing to break. When it hangs, the whole gateway becomes unresponsive even though it shows as loaded.

Fix: switch the profile to DeepSeek.

```bash
hermes --profile <profile> config set model.default "deepseek-v4-pro"
hermes --profile <profile> config set model.provider "deepseek"
hermes --profile <profile> config set model.base_url "https://api.deepseek.com/v1"
grep -q 'DEEPSEEK_API_KEY' ~/.hermes/profiles/<profile>/.env || grep 'DEEPSEEK_API_KEY' ~/.hermes/.env >> ~/.hermes/profiles/<profile>/.env
hermes --profile <profile> gateway restart
```

Pitfall: the 401 key error after switching to DeepSeek means the API key was not copied into the profile `.env`. The fix is always the same.
