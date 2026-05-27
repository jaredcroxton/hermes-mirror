# Specialist-agent governance cleanup and routing registry

Use this when Jared asks to clean up the Hermes specialist-agent ecosystem, move profile-local SOUL files into Obsidian, remove stale duplicate profiles, or create a routing registry.

## Pattern used successfully

1. Inspect profiles and SOUL source of truth:

```bash
hermes profile list
python - <<'PY'
from pathlib import Path
profiles = ['bobbuilder','nellynotebook','laralearning','samstudynerd','pollyperformos','harryhr']
for name in profiles:
    d = Path('/Users/jc/.hermes/profiles') / name
    s = d / 'SOUL.md'
    print(name, 'exists=', d.exists(), 'soul=', s.exists(), 'symlink=', s.is_symlink(), 'target=', s.resolve() if s.exists() else '')
PY
```

2. If a rich profile-local SOUL is more current than the Obsidian version, back up the Obsidian file first, then promote the profile SOUL into Obsidian.

3. Replace profile `SOUL.md` with a symlink to the canonical Obsidian SOUL.

4. Remove stale duplicate profiles only after confirming they have no SOUL/config/env worth preserving.

5. Create or update:

`/Users/jc/Desktop/Obsidian/Agents/Agent Registry.md`

Include for each agent:

- role
- profile
- alias
- Telegram bot
- SOUL path
- runtime state
- handoff rule
- quality/review gates

6. Verify:

```bash
hermes profile list
readlink /Users/jc/.hermes/profiles/<profile>/SOUL.md
```

Restart any running profile gateway whose SOUL/config changed.

## Governance rule

SOUL files hold identity, boundaries, decision rules, output contracts, and quality gates.

Skills hold repeatable procedures.

Obsidian is the canonical source for important agent SOUL files.

## Pitfall

Do not assume a profile should be started as a Telegram gateway until its profile-local `.env` has a unique `TELEGRAM_BOT_TOKEN`. Reusing another agent's token causes bot identity confusion and polling conflict.

## Obsidian SOUL folder cleanup: duplicate and fork detection

When the Obsidian Agents folder accumulates duplicate files, forked versions, patch notes, and mislocated non-SOUL files, use this detection workflow before deleting anything.

### Step one. Identify all files

```bash
python - <<'PY'
from pathlib import Path
p = Path('/Users/jc/Desktop/Obsidian/Agents')
files = sorted(p.glob('*.md'))
print(f'{len(files)} files')
for f in files:
    print(f'{f.name:<48} {f.stat().st_size:>8}')
PY
```

### Step two. Check suspected duplicates for identical content

```bash
python - <<'PY'
from pathlib import Path
pairs = [
 ('Harry_Hr-Soul.md', 'harry-hr-soul.md'),
 ('Atticus_Governance Soul.md', 'Atticus_Governance-Soul.md'),
 ('lara-learningdesign-soul.md', 'Lara_Learningdesign.md'),
]
base = Path('/Users/jc/Desktop/Obsidian/Agents')
for a,b in pairs:
    ca = (base/a).read_text()
    cb = (base/b).read_text()
    identical = ca == cb
    print(f'{a} vs {b}: {"IDENTICAL" if identical else "DIFFERENT"} ({(base/a).stat().st_size} vs {(base/b).stat().st_size})')
PY
```

### Step three. Decision rules

- **Identical content, different filenames**: delete the non-standard one. Keep the filename that matches the naming convention (capitalised, hyphenated, e.g. `Harry_Hr-Soul.md`).
- **Different content**: the larger file is usually the richer version Claude expanded. Keep the larger one. Check the Agent Registry to confirm which path is canonical, then update the Registry after deletion.
- **Non-SOUL files** like test runbooks, update notes, or patch fragments: move them to the correct Obsidian folder (Tests, Archive, etc.) or delete if stale.

### Step four. Update the Agent Registry

After deletions, fix any stale SOUL paths in the Registry and add entries for newly created agents. Bump the date. Use `patch` for surgical edits.

### Example: clean run

```bash
AGENTS=/Users/jc/Desktop/Obsidian/Agents
rm "$AGENTS/harry-hr-soul.md"           # identical duplicate
rm "$AGENTS/lara-learningdesign-soul.md"  # thinner fork
rm "$AGENTS/Atticus_Governance Soul.md"  # thinner fork
rm "$AGENTS/brock-soul-update.md"        # stale patch note
mv "$AGENTS/bob-v3-test-runbook.md" /Users/jc/Desktop/Obsidian/Tests/
```

## Post-Claude deployment pack cleanup

When Claude creates a deployment pack for a new agent, it often places templates, runbooks, and build briefs directly in the Agents folder alongside SOUL files. This clutters the folder immediately. The Agents folder should contain exactly one file per agent.

### Detection

After any Claude JIT session that produces a new agent:

```bash
ls -1 /Users/jc/Desktop/Obsidian/Agents/ | grep -v 'Soul\|Soul.md\|Registry'
```

Files that do not contain "Soul" in the name are candidates for moving.

### Move pattern

Templates → vault-specific folder (e.g. `/Users/jc/Desktop/Obsidian/SEO/templates/`)
Runbooks → vault root (e.g. `/Users/jc/Desktop/Obsidian/SEO/`)
Test runbooks → `/Users/jc/Desktop/Obsidian/Tests/`

```bash
mkdir -p /Users/jc/Desktop/Obsidian/SEO/templates
mv /Users/jc/Desktop/Obsidian/Agents/Serge_SEO-Bob-Build-Brief-Template.md /Users/jc/Desktop/Obsidian/SEO/templates/
mv /Users/jc/Desktop/Obsidian/Agents/Serge_SEO-Polly-Consultation-Template.md /Users/jc/Desktop/Obsidian/SEO/templates/
mv /Users/jc/Desktop/Obsidian/Agents/Serge_SEO-Deployment-Runbook.md /Users/jc/Desktop/Obsidian/SEO/
```

### Post-move soul review

After moving templates, review the SOUL file for four common Claude-caused issues:

1. **Stale file paths.** Templates referenced at old Agents-folder paths. Update to new vault paths.
2. **Redundant sections.** Claude often duplicates the same rules in both "Hard lines" and a separate "What X should never do" section. Consolidate into one.
3. **Cadence contradictions.** Claude may write "no proactive cadence" then immediately list monthly tasks. Fix the contradiction.
4. **Consultation pattern errors.** Claude may design a handoff that requires Jared to manually carry prompts between agents like a courier, even when both agents have Telegram bots. Rewrite to reflect the actual agent-to-agent path.

Use `patch` for surgical fixes. Do not rewrite the whole SOUL.