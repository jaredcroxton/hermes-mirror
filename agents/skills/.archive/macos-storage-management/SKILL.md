---
name: macos-storage-management
description: "Use when diagnosing, explaining, or safely freeing disk space on Jared's Mac, especially when old app builds, local models, Docker data, videos, Git garbage, node_modules, .next builds, or developer caches are consuming storage."
version: 1.0.0
author: Brock / Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [macos, storage, cleanup, developer-projects, docker, models, git, caches]
    related_skills: [apple-ecosystem, macos-computer-use]
---

# macOS Storage Management

## Trigger

Use this skill when Jared asks what is using Mac storage, why disk space is full, or whether old builds/apps/projects can be deleted.

Common Jared phrasing:
- "what is using all my storage"
- "I built lots of apps I never use"
- "can we delete this"
- "what data is in Docker"
- "what else is in here"

## Operating stance

Storage cleanup has real deletion risk. Move in two modes:

1. **Read-only audit first.** Use `du`, `df`, `find`, `stat`, Git read-only commands, and Docker read-only commands where available.
2. **Delete only after explicit approval.** Be precise about paths. Do not bundle personal/project deletion into a generic clean.

For Jared, keep the explanation plain and direct. Say what is safe, what is risky, and what the likely recovery is.

## Standard read-only audit

Start with current disk pressure:

```bash
df -h /
du -xhd 1 "$HOME" 2>/dev/null | sort -h
```

Then inspect common developer and app-build storage:

```bash
for p in \
  "$HOME/Desktop" \
  "$HOME/Documents" \
  "$HOME/Downloads" \
  "$HOME/Models" \
  "$HOME/.cache" \
  "$HOME/.npm" \
  "$HOME/.npm-global" \
  "$HOME/.bun" \
  "$HOME/.hermes" \
  "$HOME/.gemini" \
  "$HOME/Library/Caches" \
  "$HOME/Library/Application Support" \
  "$HOME/Library/Containers" \
  "$HOME/Library/Group Containers"; do
  [ -e "$p" ] && du -sh "$p" 2>/dev/null || true
done
```

Find common rebuildable app-build folders:

```bash
find "$HOME" -xdev -maxdepth 4 -type d \
  \( -name node_modules -o -name .next -o -name dist -o -name build -o -name .turbo -o -name .vercel -o -name target -o -name .venv -o -name venv -o -name DerivedData \) \
  -prune -print0 2>/dev/null | xargs -0 du -sh 2>/dev/null | sort -h | tail -60
```

Find large files:

```bash
find "$HOME" -xdev -maxdepth 5 -type f -size +500M -print0 2>/dev/null | xargs -0 ls -lh 2>/dev/null
```

## How to classify cleanup targets

### Usually safe after approval

These are rebuildable or disposable if Jared is not actively using the project:
- `.next`
- `dist`
- `build`
- `.turbo`
- old `node_modules`
- npm/npx cache
- Yarn cache
- pip/uv cache
- Playwright/Puppeteer browser caches
- Homebrew download cache
- old local model files Jared no longer uses

### Needs a specific warning

- `~/Library/Containers/com.docker.docker/Data/vms`: Docker Desktop VM disk. Can contain Docker images, containers, volumes, local databases, Supabase local data, n8n local data, and app test state. If Docker is not running, say you cannot inspect container names, but explain the risk clearly.
- `~/Models/*.gguf`: local model files. Deleting does not break apps generally, but removes that model until re-downloaded.
- `~/Library/Application Support/<app>`: app data, not just cache.
- video project folders and exports.
- `.git` folders.

### Treat `.git` folders carefully

A very large `.git` folder can be more valuable or more disposable depending on state.

Read-only checks:

```bash
git -C "$PROJECT" status --short
git -C "$PROJECT" remote -v
git -C "$PROJECT" --no-pager log --oneline --decorate --date=short --pretty=format:'%ad %h %s' -12
git -C "$PROJECT" count-objects -vH
du -xhd 2 "$PROJECT/.git" 2>/dev/null | sort -h | tail -40
```

Decision logic:
- If there are commits and/or remotes, do not delete `.git` casually.
- If there are no commits, no remote, everything is untracked, and `git count-objects` shows huge `size-garbage`, the `.git` folder is likely failed Git garbage. Recommend deleting only `.git`, not the working files.
- Explain that deleting `.git` removes Git tracking/history but leaves visible files intact.

## Docker inspection pattern

Read-only first:

```bash
du -xhd 2 "$HOME/Library/Containers/com.docker.docker" 2>/dev/null | sort -h | tail -50
du -xhd 2 "$HOME/Library/Application Support/Docker Desktop" 2>/dev/null | sort -h | tail -30
command -v docker >/dev/null && docker system df 2>&1 || printf 'docker command not available or daemon not running\n'
ps aux | grep -i '[d]ocker' | head -20
```

If Docker is not running, do not start it without permission. Jared manages his own infrastructure.

## Deletion discipline

Before deleting, say exactly what will be removed and what it means. Then wait for explicit approval.

After deletion, verify:

```bash
df -h /
[ ! -e "$PATH" ] && echo "Deleted: $PATH" || echo "Still exists: $PATH"
du -sh "$PARENT" 2>/dev/null || true
```

## Pitfalls

1. **Do not delete whole project folders just because they are old.** First search for Jared-named keepers, client names, or known key terms.
2. **Do not assume `Documents/New project` contains the project Jared cares about.** Search across Home for likely names before recommending deletion.
3. **Do not treat Docker data as cache.** It may contain local databases and volumes.
4. **Do not start Docker, Ollama, n8n, or services just to inspect storage unless Jared explicitly approves.**
5. **When the disk is critically full, terminal state writes may fail with `No space left on device`.** Free a safe large item first, then continue deeper diagnostics.

## Response format Jared responds to

Use short sections:

- what is using space
- what it is
- risk if deleted
- recommended action
- space likely freed

Ask for one approval at a time when deletion risk differs. Example: approve model deletion separately from Docker VM deletion if the risk profile differs.

## Reference notes

See `references/session-2026-08-26-storage-audit.md` for a worked example involving local model deletion, Docker VM data, a massive failed `.git` folder, and separating Josh/Cobra project files from unrelated storage waste.
