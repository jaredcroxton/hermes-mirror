# Batch Pack-Agent Deployment (CREW Pattern)

Proven 28 June 2026. Deploy 14 profile-backed specialist agents in one batch — each with domain-specific skills, locked delegation, and stripped inherited credentials.

## When to use

Deploying a fleet of profile-backed agents that share a common pattern:
- Each profile gets a specific subset of skills
- Profiles never route to each other directly
- An orchestrator profile routes work via Kanban
- No Telegram, email, or cron inheritance from default

## The pattern

### 1. Create all profiles in batch

```bash
for name in pack-core pack-sales pack-marketing pack-ops pack-hr \
  pack-finance pack-support pack-docs pack-training pack-web-design \
  pack-infrastructure pack-design-standards pack-design-styles pack-animation; do
    hermes profile create "$name" --clone-from default
done
```

### 2. Strip inherited credentials

Cloned profiles inherit Telegram tokens, email config, and cron jobs from default. These must be removed before any profile gateway starts:

```bash
for profile in pack-core pack-sales pack-marketing pack-ops pack-hr \
  pack-finance pack-support pack-docs pack-training pack-web-design \
  pack-infrastructure pack-design-standards pack-design-styles pack-animation; do
    sed -i '' '/^TELEGRAM_/d' ~/.hermes/profiles/$profile/.env
    sed -i '' '/^EMAIL_/d' ~/.hermes/profiles/$profile/.env
    sed -i '' '/^GMAIL_/d' ~/.hermes/profiles/$profile/.env
    sed -i '' '/^SMTP_/d' ~/.hermes/profiles/$profile/.env
    rm -f ~/.hermes/profiles/$profile/cron/state.json
done
```

### 3. Install per-profile skills

Each profile gets only its domain skills. Clear existing crew skills first:

```bash
# Map source directories to profile names
declare -A PACK_MAP
PACK_MAP["01-core"]="pack-core"
# ... (one entry per pack)

for pack_dir in ~/crew-skill-packs/packs/*/; do
    pack_name=$(basename "$pack_dir")
    profile="${PACK_MAP[$pack_name]}"
    rm -rf ~/.hermes/profiles/$profile/skills/crew-*
    for skill_dir in "$pack_dir"crew-*/; do
        [ -d "$skill_dir" ] || continue
        skill_name=$(basename "$skill_dir")
        cp -r "$skill_dir" ~/.hermes/profiles/$profile/skills/"$skill_name"
        # Path fix for Claude Code → Hermes
        sed -i '' 's|.claude/crew-state/|~/.hermes/crew-state/|g' \
          ~/.hermes/profiles/$profile/skills/"$skill_name"/SKILL.md
    done
done
```

### 4. Lock delegation

These agents are workers. They must never spawn sub-agents or route to other profiles:

```bash
for profile in pack-core pack-sales pack-marketing pack-ops pack-hr \
  pack-finance pack-support pack-docs pack-training pack-web-design \
  pack-infrastructure pack-design-standards pack-design-styles pack-animation; do
    sed -i '' 's/max_spawn_depth: [0-9]*/max_spawn_depth: 0/' \
      ~/.hermes/profiles/$profile/config.yaml
    sed -i '' 's/max_concurrent_children: [0-9]*/max_concurrent_children: 0/' \
      ~/.hermes/profiles/$profile/config.yaml
done
```

### 5. Write SOUL files

Each profile needs a SOUL.md with identity, domain, skill list, and operating rules.
Template: `crew-gold-standard-build/references/crew-pack-agent-soul-templates.md`

### 6. Verify

```bash
# Count profiles
hermes profile list | grep -c 'pack-'

# Check skills per profile
for p in pack-*; do
  echo -n "$p: "
  ls ~/.hermes/profiles/$p/skills/crew-* 2>/dev/null | wc -l
done

# Verify delegation locked
for p in pack-*; do
  echo -n "$p spawn_depth: "
  grep 'max_spawn_depth' ~/.hermes/profiles/$p/config.yaml
done
```

## Orchestrator profile (separate)

The orchestrator (e.g. Brock) gets its own profile with:
- Full ecosystem map in SOUL.md
- Kanban tools enabled
- Gateway for Telegram
- No delegation locking (it needs to spawn Kanban tasks)

## Pitfalls

- **Glob pattern: directories, not files.** If skills are in `crew-*/SKILL.md` format, use `crew-*/` not `crew-*.md`.
- **Delegation locking before gateway start.** A locked profile can't spawn workers, but the Kanban dispatcher spawns the profile as a worker — that's fine. The lock prevents the profile from spawning ITS OWN sub-agents.
- **API key isolation.** If switching providers, remember profile `.env` files don't inherit from default. Copy API keys explicitly.
- **Gateway only for orchestrator.** Worker profiles receiving Kanban cards don't need gateways. Only the orchestrator needs a gateway for Telegram.
