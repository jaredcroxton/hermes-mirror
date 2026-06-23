# Hermes mirror backup hardening

Use this when running scheduled backups into `jaredcroxton/hermes-mirror` or any similar GitHub mirror of Hermes profiles, skills, souls, and config.

## Durable lesson

When copying `~/.hermes/skills` with `rsync -a`, external symlinks can be mirrored as symlinks rather than actual content. In this session, `agents/skills/zapier-sdk` was a symlink to `/Users/jc/.agents/skills/zapier-sdk`; the first backup committed a repository symlink, then a follow-up replaced it with real copied files.

## Safer pattern

0. **Detect symlinks in the source skills tree BEFORE copying.** `rsync -a` will fail if a symlink-to-directory replaces a previously-copied real directory — `unlinkat: Directory not empty`. Pre-flight detection avoids this:
   ```bash
   python3 - <<'PY'
from pathlib import Path
root = Path('/Users/jc/.hermes/skills')
for p in root.rglob('*'):
    if p.is_symlink():
        print(f'{p.relative_to(root)} -> {p.resolve()} exists={p.resolve().exists()}')
PY
   ```
1. If symlinks found, resolve them individually before the main copy. For each symlinked skill dir, copy the real target with `cp -r -L`, then rsync the rest excluding the already-resolved dir:
   ```bash
   rm -rf /tmp/hermes-mirror-backup/agents/skills/zapier-sdk
   cp -r -L /Users/jc/.hermes/skills/zapier-sdk /tmp/hermes-mirror-backup/agents/skills/zapier-sdk
   rsync -a --exclude='zapier-sdk' /Users/jc/.hermes/skills/ /tmp/hermes-mirror-backup/agents/skills/
   ```
   If no symlinks exist, a straight `rsync -a` is safe.
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

## Stale clone pitfall (cron workspace reuse)

When a cron job reuses a fixed workspace path (e.g. `/tmp/hermes-mirror-backup`) across runs, the common `clone || pull` pattern fails silently if the repo exists but has lost its `origin` remote. The clone half sees an existing directory and exits non-zero; the pull half then fails with "origin does not appear to be a git repository." The workspace looks present but is disconnected.

**Fix:** Before any pull-based reuse, verify `origin` exists. If absent, `rm -rf` and fresh clone.

```bash
cd /tmp/hermes-mirror-backup
if ! git remote get-url origin >/dev/null 2>&1; then
  cd /tmp && rm -rf /tmp/hermes-mirror-backup
  git clone https://github.com/jaredcroxton/hermes-mirror.git hermes-mirror-backup
  cd /tmp/hermes-mirror-backup
else
  git pull origin main
fi
```

For cron jobs where a fresh clone is cheap (small repo, no local-only state), prefer always cloning fresh — it's simpler and avoids this entire class of failure.

## Secret scan after redaction

After running sed-based redaction, always verify with a positive scan before committing:

```bash
grep -rI "apify_api_\|sk-\|ghp_\|github_pat_\|xox[baprs]-\|AIza" . --exclude-dir=.git 2>/dev/null || true
```

Matches in documentation files (showing the redaction regex itself) are harmless. Matches in `.yaml` config files are a problem — re-check the redaction step.

**Expected harmless matches in skills directory:** The `.curator_backups/` and `.archive/` subdirectories under `agents/skills/` contain old cron job prompts and reference docs that include literal `apify_api_` and other token-pattern strings as examples. These are not live secrets. When scanning, either exclude these directories or manually verify that matches are only in `.json` backup files and `.md` reference/docs — never in `.yaml` config files.

## Verification checks

```bash
cd /tmp/hermes-mirror-backup
find agents/skills -type l -print
git status --porcelain
git rev-parse --short HEAD
```

A clean final run should report no unexpected symlinks, no `.env`, no `state.db`, no residual token patterns, and a clean working tree after push.
