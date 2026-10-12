# Cross-machine specialist agent host migration

Use when Jared wants to move the live Hermes and Claude Code agent ecosystem from one Mac to another, usually to protect MacBook battery life or make a Mac mini the always-on host.

## Core principle

Move the operating layer, not just skills.

For Jared's setup this usually means copying:

- `~/.hermes` for Hermes config, profiles, skills, memories, sessions, auth, cron, kanban, and gateway state
- `~/.claude` for Claude Code global skills, agents, and local Claude config
- `~/Desktop/Obsidian/Agents/` for canonical specialist SOUL files
- `~/Desktop/Obsidian/PerformOS/` for PerformOS context files
- `~/Desktop/cluade/.agents/skills/` when Claude global skills are symlinks to this canonical install
- `~/Desktop/hermes_builds/` for local build artefacts if needed
- `~/.config/gh/` and `~/.vercel/` if Bob will deploy from the new host

## Safe sequence

1. Prepare the target Mac.
   - Plug it into power.
   - Put it on the same network.
   - Enable System Settings → General → Sharing → Remote Login.
   - Confirm the SSH target, for example `jc@Mac-mini.local`.

2. Copy first, do not cut over yet.
   - Use `rsync -aH --info=progress2` so symlinks, file modes, and profile folders survive.
   - Make backups on the target before overwriting existing `~/.hermes` or `~/.claude`.

3. Verify the target.
   - `hermes doctor`
   - `hermes profile list`
   - `hermes skills list`
   - `hermes chat -q "Reply exactly MINI_OK" --quiet`
   - `hermes --profile bobbuilder chat -q "Reply exactly BOB_MINI_OK" --quiet`

4. Cut over only after verification.
   - Stop gateways on the old Mac first.
   - Start only the default gateway and Bob on the new Mac initially.
   - Keep specialist gateways stopped unless needed.

5. Keep a rollback script.
   - Stop gateways on the target.
   - Restart default and Bob gateways on the original Mac.

## Critical pitfall

Do not run the same Telegram bot token on both machines. Pick one live agent host. Running the same profile gateway on both hosts can cause duplicate replies or silent routing issues.

## 8GB Mac mini operating model

For an 8GB Mac mini, recommend:

- Always-on: default Hermes gateway
- On demand: Bob gateway and one specialist at a time
- Avoid: all profile gateways, local Ollama models, heavy browser automation, and multiple Claude Code builds in parallel

## User-facing framing

Keep instructions simple and staged:

1. Turn on Remote Login.
2. Confirm the Mac mini address.
3. Run the migration script.
4. Verify Hermes and Bob.
5. Cut over only when clean.

Jared prefers one step at a time and a rollback path.