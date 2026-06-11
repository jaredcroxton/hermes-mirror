# Hermes mirror backup hardening

Use this when running scheduled backups into `jaredcroxton/hermes-mirror` or any similar GitHub mirror of Hermes profiles, skills, souls, and config.

## Durable lesson

When copying `~/.hermes/skills` with `rsync -a`, external symlinks can be mirrored as symlinks rather than actual content. In this session, `agents/skills/zapier-sdk` was a symlink to `/Users/jc/.agents/skills/zapier-sdk`; the first backup committed a repository symlink, then a follow-up replaced it with real copied files.

## Safer pattern

1. Copy skills with normal excludes for state and secrets.
2. Detect symlinks under the copied skill tree before committing:
   ```bash
   cd /tmp/hermes-mirror-backup
   find agents/skills -type l -print
   ```
3. For each symlink, inspect whether the source target exists and should be mirrored:
   ```bash
   python3 - <<'PY'
from pathlib import Path
root = Path('/Users/jc/.hermes/skills')
for p in root.rglob('*'):
    if p.is_symlink():
        print(f'{p.relative_to(root)} -> {p.resolve()} exists={p.resolve().exists()}')
PY
   ```
4. If the target is a real skill directory, replace the mirror symlink with a real directory copy. Preserve the same secret and state excludes.
5. Run the secret scan after resolving symlinks and before committing.
6. Verify the final tree has no blocked files, no residual token patterns, and no accidental external symlinks.

## Verification checks

```bash
cd /tmp/hermes-mirror-backup
find agents/skills -type l -print
git status --porcelain
git rev-parse --short HEAD
```

A clean final run should report no unexpected symlinks, no `.env`, no `state.db`, no residual token patterns, and a clean working tree after push.
