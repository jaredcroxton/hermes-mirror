# Multi-profile Telegram outage recovery

Use this when Jared says several Telegram agents are silent or asks to "fix Telegram" across the specialist ecosystem.

## Trigger
- Multiple profile-backed Telegram bots do not reply.
- `hermes profile list` shows many gateways stopped.
- Some gateway service definitions are stale after a Hermes install or update.
- Telegram connects, but profile probes fail with provider authentication errors.

## Recovery sequence

1. **Start with gateway state, not provider debugging**
   ```bash
   hermes profile list
   hermes gateway status || true
   for p in bobbuilder harryhr laralearning nellynotebook pollyperformos samstudynerd; do
     hermes --profile "$p" gateway status || true
   done
   ```

2. **Check recent gateway logs for Telegram-specific errors**
   ```bash
   for log in ~/.hermes/logs/gateway.log ~/.hermes/profiles/*/logs/gateway.log; do
     [ -f "$log" ] || continue
     echo "### $log ###"
     grep -iE 'telegram|failed|error|exception|unauthorized|conflict|poll|webhook|token|forbidden' "$log" | tail -30 || true
   done
   ```

3. **Verify profile-local Telegram wiring without exposing tokens**
   - Parse each profile `.env`.
   - Confirm `TELEGRAM_BOT_TOKEN` exists in each profile, not only default.
   - Confirm `TELEGRAM_ALLOWED_USERS` exists.
   - Call Telegram `getMe` for each token and report only bot username and a short token hash.
   - Check for duplicate token hashes across profiles. Duplicate hashes usually mean two running gateways are fighting over one bot.

4. **Restart stopped or stale gateways**
   ```bash
   hermes gateway start
   for p in atticuscounsel bobbuilder harryhr laralearning nellynotebook pollyperformos samstudynerd sergeseo; do
     hermes --profile "$p" gateway start || true
   done
   hermes profile list
   ```
   `Boot-out failed: 3: No such process` and `Could not find service ...` are usually harmless when the command then refreshes the launchd definition and starts the service.

5. **If Jared suspects stale model/session state, verify actual config and hard-refresh gateways**
   `hermes profile list` is useful, but the model column can lag or hide profile-local config drift. Inspect the actual `config.yaml` values before changing anything: `model.provider`, `model.default`, and `model.base_url` for default plus every specialist profile. Then restart every relevant gateway so cached model/session state is dropped.

   ```bash
   hermes profile list
   hermes auth list || true

   # Inspect actual config files, not just the profile-list model column.
   python3 - <<'PY'
   from pathlib import Path
   import yaml
   root = Path.home()/'.hermes'
   profiles = ['default'] + [p.name for p in sorted((root/'profiles').iterdir()) if p.is_dir()]
   for p in profiles:
       home = root if p == 'default' else root/'profiles'/p
       cfg = home/'config.yaml'
       data = yaml.safe_load(cfg.read_text()) if cfg.exists() else {}
       m = (data or {}).get('model', {}) or {}
       print(p, m.get('provider'), m.get('default'), m.get('base_url'))
   PY

   # Hard refresh gateways so cached model/session state is dropped.
   for p in default atticuscounsel bobbuilder harryhr laralearning miracreative nellynotebook piperpromptops pollyperformos samstudynerd sergeseo; do
     if [ "$p" = default ]; then hermes gateway restart || hermes gateway start || true
     else hermes --profile "$p" gateway restart || hermes --profile "$p" gateway start || true
     fi
   done
   ```

   This pattern matters when the user says the agents "haven't been refreshed" or points to models. Do not assume the earlier gateway start fixed cached model state.

6. **Probe profile brains after gateways are running and refreshed**
   ```bash
   hermes --profile <profile> chat -q "Reply exactly <profile>_OK" --quiet
   ```
   A gateway can be connected to Telegram while the profile brain still fails due to provider credentials. Run probes after restart, not before, when cached model state is suspected.

7. **Fix profile-local provider credential drift**
   If only some DeepSeek profiles fail with 401 while the default profile succeeds, compare whether those profiles have a different `DEEPSEEK_API_KEY` value. Profiles do not inherit default `.env` values.

   Safe fix pattern:
   - Back up the profile `.env`.
   - Replace only the stale profile `DEEPSEEK_API_KEY` with the working default profile value.
   - Set profile `.env` permissions to `0600`.
   - Restart the affected profile gateway.
   - Re-run the profile brain probe.

8. **Final verification**
   - `hermes profile list` shows every intended profile gateway `running`.
   - Recent logs show `Connected to Telegram (polling mode)` and `✓ telegram connected`.
   - Recent Telegram/model error scan has no current Telegram errors, provider 401s, `model returned empty`, or API timeout failures.
   - Direct probes return the requested exact OK string after the gateway refresh.

## Reporting standard
Give Jared the cause and the concrete result, not a long terminal transcript:
- what was broken
- what was fixed
- which agents are now running
- anything outside Telegram left unresolved, e.g. an email IMAP credential error

## Pitfalls
- Do not treat a successful CLI profile probe as proof Telegram is live. The gateway may still be stopped.
- Do not stop after `gateway start` when Jared says it may be model-related or "not refreshed". Inspect actual profile config, restart the gateways, then probe again so cached model/session state is cleared.
- Do not trust `hermes profile list` alone for model diagnosis. Use profile `config.yaml` as the source of truth for provider/model/base_url.
- Do not expose Telegram tokens or API keys in the final answer. Use usernames and short hashes only for diagnostics.
- Do not chase old Telegram errors if a later log shows clean reconnect and current probes pass.
- Do not record environment-specific details like current PIDs, exact timestamps, or one-off session IDs in the skill.
