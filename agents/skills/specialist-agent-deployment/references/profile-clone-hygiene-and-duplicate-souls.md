# Profile clone hygiene and duplicate SOUL cleanup

Use this after cloning a specialist profile from `default` or another always-on agent, and when the Obsidian Agents vault contains duplicate SOUL files for the same specialist.

## Why this matters

Cloning with `--clone-all` can copy more than the specialist needs:

- Telegram home channel from the parent profile
- Email IMAP/SMTP credentials
- Google Chat platform config
- Cron jobs from the parent profile
- Session dumps and runtime history

A new specialist can appear to work while silently inheriting the wrong jobs or platforms. Treat profile creation as incomplete until this hygiene pass is done.

## Post-clone hygiene checklist

After `hermes profile create <profile> --clone-all`:

1. Symlink the profile SOUL to the canonical Obsidian SOUL.
2. Remove inherited platform credentials the new specialist should not own:
   - `TELEGRAM_HOME_CHANNEL`
   - `EMAIL_ADDRESS`
   - `EMAIL_PASSWORD`
   - `EMAIL_IMAP_HOST`
   - `EMAIL_SMTP_HOST`
   - `EMAIL_ALLOWED_USERS`
3. Add only the new specialist's own Telegram bot token and Jared allowlist.
4. Disable cloned platforms in profile `config.yaml` unless explicitly wanted:
   - `platforms.google_chat.enabled: false`
   - `platforms.email.enabled: false`
   - `platforms.telegram.enabled: true`
5. Clear cloned cron jobs unless the user explicitly asked this specialist to inherit them:
   - set `~/.hermes/profiles/<profile>/cron/jobs.json` to `{ "jobs": [] }`
6. Restart the profile gateway.
7. Verify the gateway runs with only the intended platform.

## Verification commands

Use these checks before saying the agent is live:

```bash
hermes profile list | grep <profile>
readlink ~/.hermes/profiles/<profile>/SOUL.md
hermes --profile <profile> chat -q 'Reply with only your name and scope.' --quiet
hermes --profile <profile> gateway status
tail -n 80 ~/.hermes/profiles/<profile>/logs/gateway.log
```

Look for:

- `Connected to Telegram (polling mode)`
- `✓ telegram connected`
- `Gateway running with 1 platform(s)` when Telegram-only is intended

## Telegram first-contact pitfall

A BotFather token and `getMe` success prove the bot identity exists. They do not prove the user has pressed **Start** in the bot chat. If proactive send fails with `chat not found`, ask Jared to open the bot and press **Start**, then test again.

## Duplicate SOUL file workflow

When Jared notices two SOUL files for the same specialist:

1. Check which file the live profile actually uses:
   ```bash
   readlink ~/.hermes/profiles/<profile>/SOUL.md
   ```
2. Compare the candidate files by size, modification date, and core rules.
3. Do not blindly adopt the larger file. Older rich SOUL files often contain stale delivery rules.
4. Keep the active canonical file unless the user approves a merge.
5. Merge useful sections into the active canonical file, remove contradictory rules, then restart the profile gateway.
6. Archive the duplicate only after the active agent passes an identity and output-contract probe.

## Example lesson

Leo_Leadership was cloned from default. The profile initially inherited email, Google Chat, and parent cron jobs, including Brock's morning CEO check-in. The correct fix was to remove inherited email and Google Chat config, clear cron jobs, and run Leo as Telegram-only.

Lara had two SOUL files. The live profile pointed to `lara-learningdesign-soul.md`, while `Lara_Learningdesign.md` was much richer but had stale Google Sheet-only delivery rules. The right move was not automatic replacement. It was controlled merge into the active canonical file.