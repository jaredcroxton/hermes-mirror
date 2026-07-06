---
name: hermes-mirror-backup
description: Daily backup of the Hermes agent ecosystem (souls, profiles, skills, config, memory) to the GitHub mirror repo at github.com/jaredcroxton/hermes-mirror. Use for cron-driven or manual ecosystem backups.
---

# Hermes Mirror Backup

Backup the full Hermes agent ecosystem to the GitHub mirror repository. Covers agent souls, profile configs, skills directory, Hermes config files, and memory exports. Secrets are redacted before commit.

## When to use

- Scheduled daily backup (cron)
- Manual pre-upgrade ecosystem snapshot
- Any time the agent ecosystem state should be preserved to git

## Workflow

### 1. Clone fresh (never reuse a stale directory)

The fallback `clone || pull` pattern fails silently when the target directory exists but is not a git repo. Always remove first.

```bash
rm -rf /tmp/hermes-mirror-backup
cd /tmp && git clone https://github.com/jaredcroxton/hermes-mirror.git hermes-mirror-backup
```

### 2. Ensure directory structure

```bash
mkdir -p /tmp/hermes-mirror-backup/agents/souls
mkdir -p /tmp/hermes-mirror-backup/agents/profiles
mkdir -p /tmp/hermes-mirror-backup/agents/skills
mkdir -p /tmp/hermes-mirror-backup/config
mkdir -p /tmp/hermes-mirror-backup/memory
```

### 3. Copy agent souls

```bash
cp /Users/jc/Desktop/Obsidian/Agents/*.md /tmp/hermes-mirror-backup/agents/souls/
```

### 4. Copy agent profile configs

Seven profiles. Copy `config.yaml` only — never `state.db` or `.env`.

```bash
for profile in bobbuilder laralearning samstudynerd pollyperformos harryhr atticuscounsel nellynotebook; do
  mkdir -p /tmp/hermes-mirror-backup/agents/profiles/$profile
  cp /Users/jc/.hermes/profiles/$profile/config.yaml /tmp/hermes-mirror-backup/agents/profiles/$profile/
done
```

### 5. Copy skills directory

```bash
cp -r /Users/jc/.hermes/skills/. /tmp/hermes-mirror-backup/agents/skills/
```

### 6. Copy Hermes config files

The active config file is `AGENTS.md`, not `CLAUDE.md`. The filename `CLAUDE.md` appears in older documentation but the actual file shipped with Hermes is `AGENTS.md`.

```bash
cp /Users/jc/.hermes/config.yaml /tmp/hermes-mirror-backup/config/
cp /Users/jc/.hermes/hermes-agent/AGENTS.md /tmp/hermes-mirror-backup/config/
cp /Users/jc/Desktop/Obsidian/agent-startup.md /tmp/hermes-mirror-backup/config/
```

### 7. Redact secrets

Strip Apify API tokens from all YAML files. Verify no tokens remain before committing.

```bash
cd /tmp/hermes-mirror-backup
find . \( -name "*.yaml" -o -name "*.yml" \) -exec sed -i '' 's/apify_api_[a-zA-Z0-9]\{30,\}/REDACTED_APIFY_TOKEN/g' {} \;
# Verify no live tokens remain in config files only (ignore .md/.json doc examples)
find . \( -name "*.yaml" -o -name "*.yml" \) -exec grep -l "apify_api_" {} \; 2>/dev/null | grep -v REDACTED
# Should produce no output — if it does, stop and investigate
```

### 8. Update memory export

```bash
echo "Last automated backup: $(date '+%d %B %Y %H:%M')" >> /tmp/hermes-mirror-backup/memory/memory-export.md
```

### 9. Commit and push if changes exist

```bash
cd /tmp/hermes-mirror-backup
if [ -n "$(git status --porcelain)" ]; then
  git add -A
  git commit -m "Daily backup — $(date '+%d %B %Y')"
  git push origin main
fi
```

## Pitfalls

- **Stale non-git directory:** The pattern `git clone X || (cd X && git pull)` fails when the directory exists but is not a git repo. Always `rm -rf` first for cron safety.
- **Wrong config filename:** The Hermes development guide is `AGENTS.md`, not `CLAUDE.md`. The latter appears in some older documentation but does not exist on disk. Copy `AGENTS.md` instead.
- **Leaked tokens:** The Apify token regex `apify_api_[a-zA-Z0-9]{30,}` must be verified with a follow-up grep. Silent failures on the sed command (e.g., no matches) are not evidence of clean output — always grep-check after redaction.
- **False-positive grep matches:** The `apify_api_` pattern appears in documentation files (`.md` reference docs, `.curator_backups/` JSON archives, the skill's own SKILL.md) as literal examples, not live secrets. When scanning, scope the verification grep to `.yaml` and `.yml` files only. Matches in `.md`, `.json`, or `.tar.gz` files under `agents/skills/` are expected and harmless.

## What NOT to include

- `state.db` — contains session data, excluded by `.gitignore`
- `.env` — contains API keys, excluded by `.gitignore`
- Any file with unredacted API keys or tokens
