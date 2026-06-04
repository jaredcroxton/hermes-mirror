# Global profile local-model trial

Use this when Jared wants to switch Brock and the specialist profiles to a local Ollama model to reduce API cost or test private inference.

## User workflow correction

If Jared says to switch everyone to a local model, do not treat the provider change as the first action. His expected sequence is:

1. Back up the current profile state to GitHub first.
2. Then change the model/provider settings.
3. Restart affected gateways.
4. Verify each profile responds.
5. Keep a clear restore path.

If approval blocks a backup command, stop and ask Jared to approve that exact operation. Do not proceed to the model switch without the backup.

## Safe backup boundary

Mirror the durable profile layer only:

- `config.yaml`, with secrets redacted
- `SOUL.md`
- profile-local `skills/`, `docs/`, `templates/`, `scripts/` where present
- `.env.example` with variable names only
- `hermes profile list` output before the switch
- restore notes

Never push:

- `.env`
- `auth.json`
- sessions
- logs
- memories
- kanban databases
- SQLite databases
- caches
- raw API tokens or OAuth credentials

Prefer a private repo named like `hermes-profile-backup` or a per-agent mirror repo set if Jared has already established that structure.

## Local Ollama config pattern

For default profile:

```bash
hermes config set model.provider custom
hermes config set model.base_url http://localhost:11434/v1
hermes config set model.default gemma4:e4b
hermes config set model.api_key ollama
```

For specialist profiles:

```bash
hermes --profile <profile> config set model.provider custom
hermes --profile <profile> config set model.base_url http://localhost:11434/v1
hermes --profile <profile> config set model.default gemma4:e4b
hermes --profile <profile> config set model.api_key ollama
```

Then restart live gateways:

```bash
hermes --profile <profile> gateway restart
```

For the default profile gateway:

```bash
hermes gateway restart
```

## Verification pattern

1. Confirm Ollama is serving:
   ```bash
   curl -s http://localhost:11434/v1/models
   ```
2. Confirm the target model name appears exactly as downloaded, for example `gemma4:e4b`.
3. Run a direct probe per profile:
   ```bash
   hermes --profile <profile> chat -q "Reply exactly LOCAL_OK" --quiet
   ```
4. For Telegram-backed profiles, check live transport after gateway restart. CLI success alone does not prove Telegram is using the new runtime.

## Restore pattern

Use the pre-switch profile list and backed-up configs to restore each profile's prior provider/model. Then restart gateways and probe again.
