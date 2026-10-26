# Obsidian Agent Vault Cleanup

The Obsidian Agents folder (`/Users/jc/Desktop/Obsidian/Agents/`) accumulates clutter from Claude adding files, creating forks, and leaving stale patch notes. Clean it periodically.

## Cleanup rules

### One SOUL per agent

The Agents folder should contain exactly one file per named agent. No forks. No duplicates. No patch notes.

### Duplicates (identical content)

If two files are byte-identical, delete one. Keep the one with the canonical naming convention (Title_Case-Soul.md).

### Forks (different content, same agent)

If two files claim to be the same agent's SOUL but differ, keep the richer one (larger file size, more detail). Delete the smaller.

### Non-SOUL files

Move, do not delete:
- Test runbooks → `/Users/jc/Desktop/Obsidian/Tests/`
- Deployment runbooks → `/Users/jc/Desktop/Obsidian/SEO/` (for Serge) or appropriate vault folder
- Templates → appropriate subfolder (e.g. `/SEO/templates/`)
- Patch notes (`brock-soul-update.md`) → delete if applied, archive if pending

## Pattern

```python
from pathlib import Path
from collections import defaultdict

p = Path('/Users/jc/Desktop/Obsidian/Agents')
files = sorted(p.glob('*.md'))

# Group by base name (strip -Soul, Soul, etc.)
# Compare sizes, flag duplicates and forks
```

## After cleanup

Update `Agent Registry.md`:
1. Fix any stale SOUL paths
2. Bump the date
3. Add any missing agents

## Canonical naming convention

- `Agent_Name-Soul.md` for most agents
- `Atticus_Counsel Soul.md` (space, no hyphen — legacy, kept)
- `Polly_PerformOS.md` (no Soul suffix — legacy, kept)
- `lara-learningdesign-soul.md` (lowercase — was the fork, deleted)
