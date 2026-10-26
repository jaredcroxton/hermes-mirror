# macOS machine migration prep checklist

Use this when Jared asks to move Hermes from one Mac to another (e.g. MacBook Air → Mac mini). Captures the state snapshot, what moves, what gets set up fresh, and the two-user privacy guard.

## Phase 1: Snapshot current state

Run a single grouped probe on the source machine:

```bash
echo '=== HERMES VERSION ===' && hermes --version
echo '=== PROFILES ===' && hermes profile list
echo '=== GATEWAY STATUS ===' && hermes gateway status 2>&1 || true
echo '=== CRON JOBS ===' && hermes cron list 2>&1
echo '=== DISK USAGE ===' && du -sh ~/.hermes/
echo '=== SKILLS COUNT ===' && ls ~/.hermes/skills/ 2>/dev/null | wc -l
echo '=== MCP SERVERS ===' && hermes mcp list 2>&1
```

This gives you: version, profile count + running/stopped, gateway PIDs, cron schedule, disk footprint, skill library size, and MCP integrations.

## Phase 2: Confirm destination specs

Ask Jared for the Mac mini specs before advising:

- Chip (M1 / M2 / M4 / M4 Pro)
- RAM
- Storage
- macOS version

Use `references/profile-gateway-capacity.md` to decide how many gateways the new machine can support side by side. Do not assume all nine gateways will run on a base M1 with 8 GB.

## Phase 3: Set up user account on destination

1. Jared's account set up first. Prefer the same shortname (`jc`) to keep paths identical.
2. Wife's account set up separately afterward.
3. Do not install Hermes until Jared's account is ready.

## Phase 4: What transfers

| Item | Path | Notes |
|------|------|-------|
| Skills | `~/.hermes/skills/` | Copy whole directory |
| Profiles | `~/.hermes/profiles/` | Copy; sanitise `.env` files on a shared machine |
| Auth | `~/.hermes/auth.json` | OAuth tokens for openai-codex and other providers |
| Config | `~/.hermes/config.yaml` | Main config |
| Secrets | `~/.hermes/.env` | API keys; review before copying to a shared machine |
| Cron jobs | SQLite db rows | Jobs need re-creation or full DB copy |
| Sessions | `~/.hermes/sessions/` | Optional; can start fresh |
| Memory | SQLite db | Optional; can start fresh |

## Phase 5: What gets set up fresh on the destination

1. **Install Hermes** (if not already): `curl -fsSL https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh | bash`
2. **Restore files** from backup into `~/.hermes/`
3. **Reinstall gateway service:** `hermes gateway install` then `hermes gateway start`
4. **Start profile gateways:** `hermes --profile <name> gateway start` for each desired profile
5. **Recreate cron jobs** — capture the three schedules from Phase 1 output and recreate via `cronjob` tool or `hermes cron create`

## Phase 6: Two-user privacy guard

On a shared Mac, macOS enforces the isolation:

- Each user has their own home folder (`/Users/jc/` and `/Users/wifename/`)
- Default permissions on home folders are `700` — other users cannot read them
- Hermes runs as Jared's user and cannot cross into the wife's account
- `.env` and `auth.json` stay inside `~/.hermes/` under Jared's home

No special Hermes config needed. Verify in **System Settings → Users & Groups** that accounts are separate and File Sharing is not enabled between home folders.

## Pitfalls

- Do not assume the destination Mac can run all profiles. Always probe specs first.
- If Jared's account shortname differs on the new machine, profile paths and config references can break. Prefer identical shortnames.
- The gateway LaunchAgent plist is machine-specific. Do not copy it — let `hermes gateway install` create a fresh one.
- OAuth tokens in `auth.json` may need a fresh login on the new machine if bound to a different keychain or macOS user identity.
