# Bulk Profile Model Migration

Full pattern for migrating all specialist Hermes profiles to one provider/model at once. Captured from the 17 June 2026 openai-codex → deepseek-v4-pro migration across 13 profiles.

## Trigger

Jared says "update all models to <provider/model>" or "switch everyone to DeepSeek Pro."

## Sequence

### 1. Probe the target model

```bash
hermes --profile default chat -q "Reply exactly PROBE_OK" -m deepseek-v4-pro --provider deepseek --quiet 2>&1
```

Do not proceed if this fails. The model name and provider must resolve.

### 2. Verify the API key and note its fingerprint

```bash
python3 -c "
import os
env_path = os.path.expanduser('~/.hermes/.env')
with open(env_path) as f:
    for line in f:
        if 'DEEPSEEK_API_KEY=*** in line:
            val = line.strip().split('=',1)[1]
            print(f'Key length: {len(val)}, ends: ...{val[-4:]}')
            break
"
```

Remember the last-4 characters. Every profile must match.

### 3. Audit every profile .env for the key VALUE

Do NOT just check key presence with `grep -q`. That passes profiles with stale/different keys from prior experiments.

```bash
DEFAULT_KEY=$(grep 'DEEPSEEK_API_KEY' ~/.hermes/.env | cut -d= -f2)

for profile_dir in ~/.hermes/profiles/*/; do
  name=$(basename "$profile_dir")
  env_file="${profile_dir}.env"
  if [ -f "$env_file" ]; then
    key=$(grep 'DEEPSEEK_API_KEY' "$env_file" 2>/dev/null | cut -d= -f2)
    if [ -n "$key" ]; then
      if [ "$key" = "$DEFAULT_KEY" ]; then
        echo "  $name: MATCH"
      else
        echo "  $name: MISMATCH — fixes needed"
      fi
    else
      echo "  $name: NO KEY — will need copy"
    fi
  fi
done
```

### 4. Update all profile configs

Use a script to update `model.default`, `model.provider`, and `model.base_url` in every profile `config.yaml`. Skip profiles on local/custom models (e.g. `localgemma` on `gemma4:e4b`).

For each profile:

```bash
hermes --profile <name> config set model.default "deepseek-v4-pro"
hermes --profile <name> config set model.provider "deepseek"
hermes --profile <name> config set model.base_url "https://api.deepseek.com/v1"
```

Or edit `config.yaml` directly for speed across many profiles.

### 5. Fix any mismatched keys

Copy the working key from the default `.env` into any profile `.env` that had a different value:

```bash
DEFAULT_KEY=$(grep 'DEEPSEEK_API_KEY' ~/.hermes/.env | cut -d= -f2)
sed -i '' "s|DEEPSEEK_API_KEY=*** ~/.hermes/profiles/<name>/.env
```

### 6. Restart all running gateways

`hermes gateway restart` can fail on launchd-managed services with "Stop it with: hermes gateway stop" instead of restarting. Fall back:

```bash
hermes --profile <name> gateway stop
sleep 2
hermes --profile <name> gateway start
```

Wait a few seconds after start for launchd to register the process before probing.

### 7. Verify every profile

```bash
for profile in <list>; do
  result=$(hermes --profile "$profile" chat -q "Reply exactly ${profile}_OK" --quiet 2>&1)
  if echo "$result" | grep -q "${profile}_OK"; then
    echo "$profile: PASS"
  elif echo "$result" | grep -q "Error\|401\|auth"; then
    echo "$profile: FAIL — $result"
  else
    echo "$profile: CHECK — $result"
  fi
done
```

A 401 response means the key is still wrong or the gateway didn't restart cleanly. Check the key value directly in the profile `.env` and force a gateway stop/start cycle.

### 8. Report

List: profiles updated, skipped (and why), key mismatches found and fixed, verification results, any profiles with gateways still stopped.

## Pitfalls

- **Key presence ≠ key correctness.** Six profiles in the 17 June 2026 migration already had `DEEPSEEK_API_KEY=*** entries with different/stale keys. They passed `grep -q` but failed at runtime with 401.
- **Launchd `restart` can silently fail.** If `hermes gateway restart` returns "Stop it with: hermes gateway stop" instead of "✓ Service restarted," the gateway did not restart. Do a manual stop/start cycle.
- **`hermes profile list` may show `stopped` briefly after start.** Wait 5 seconds and check again before treating it as a failure.
- **CLI probes work even when Telegram is broken.** A passing CLI probe does not prove the Telegram gateway loaded the new config. Verify with `hermes profile list` that the gateway column shows `running`.
- **Don't migrate non-API profiles.** Leave local model profiles (`gemma4:e4b`, etc.) alone.
