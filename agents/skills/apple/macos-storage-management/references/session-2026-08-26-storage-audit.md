# Session example: macOS storage audit on 26 August 2026

## Scenario

Jared's Mac was critically full. Initial `df -h /` showed only about 115 to 120 MB free on a 460 GB disk. He asked what was using storage because he had built many unused apps.

## High-signal findings

Top-level home scan showed:

- `~/Documents`: 116 GB
- `~/Desktop`: 56 GB
- `~/Borumi Projects`: 51 GB
- `~/Library`: 59 GB
- `~/Models`: 15 GB
- `~/.cache`: 16 GB
- `~/.hermes`: 10 GB
- `~/.gemini`: 7.3 GB
- `~/.npm-global`: 5.7 GB
- `~/.npm`: 4.7 GB

Key deletion approved by Jared:

- `~/Models/Qwen3.8-27B-GGUF`: 15 GB local model file, `Qwen3.8-27B-Q4_K_M.gguf`
- `~/Library/Containers/com.docker.docker/Data/vms`: 16 GB Docker Desktop VM data

After deletion, disk space improved from about 114 MB free to about 31 GB free.

## Docker explanation used

Docker Desktop VM data can contain:

- images
- containers
- build cache
- volumes
- local databases
- Supabase local data
- n8n local data
- app test state

In the session Docker was not running, so container/image names could not be inspected. The correct behaviour was to explain the risk and ask for approval rather than starting Docker or deleting silently.

## `Documents/New project` analysis

`~/Documents/New project` was 115 GB.

Breakdown:

- `.git`: 89 GB
- `videos`: 26 GB
- `profile-pictures`: 18 MB
- `assets`: 5.5 MB
- `postiz-app`: 67 MB
- `tortoise-hare-deck`: 100 MB
- other files were small

Git checks showed:

- no commits
- no remote
- current branch had no commits
- all visible files were untracked
- `git count-objects -vH` reported about 65.40 GiB of garbage
- `.git/objects/pack` was about 74 GB

Conclusion: recommend deleting only `~/Documents/New project/.git`, not the working files. This would remove Git tracking/history while preserving visible files.

## Separating important project files from waste

Jared said he definitely needed the Josh/Cobra motorbike/lever work. Search terms used:

- cobra
- motorbike
- motor
- bike
- lever
- Josh
- parts

Findings showed Josh/Cobra projects were mainly outside `Documents/New project`:

- `~/Desktop/Josh APP`: 97 MB, modified 24 August 2026
- `~/Desktop/cluade/cobra-parts-store`: 561 MB, modified 23 May 2026
- `~/Desktop/cobra-parts-store`: 205 MB, modified 8 June 2026

Inside `Documents/New project`, the only lever matches were thumbnails under recent video folders:

- `videos/local-trail-trial-a`
- `videos/local-trail-trial-b`
- `videos/downloading-local-ai-trial-a`

Lesson: before deleting a large folder, search for the user's named keepers across Home. Do not rely on the large folder path alone.

## Useful commands from the session

Top-level audit:

```bash
df -h /
du -xhd 1 "$HOME" 2>/dev/null | sort -h
```

Project folder audit:

```bash
du -sh "$HOME/Documents/New project"
du -xhd 2 "$HOME/Documents/New project" 2>/dev/null | sort -h | tail -40
```

Git state audit:

```bash
git -C "$HOME/Documents/New project" status --short
git -C "$HOME/Documents/New project" remote -v
git -C "$HOME/Documents/New project" --no-pager log --oneline --decorate --date=short --pretty=format:'%ad %h %s' -12
git -C "$HOME/Documents/New project" count-objects -vH
du -xhd 2 "$HOME/Documents/New project/.git" 2>/dev/null | sort -h | tail -40
```

Docker read-only audit:

```bash
du -xhd 2 "$HOME/Library/Containers/com.docker.docker" 2>/dev/null | sort -h | tail -50
du -xhd 2 "$HOME/Library/Application Support/Docker Desktop" 2>/dev/null | sort -h | tail -30
command -v docker >/dev/null && docker system df 2>&1 || printf 'docker command not available or daemon not running\n'
ps aux | grep -i '[d]ocker' | head -20
```

Approval-based deletion that was run:

```bash
rm -rf "$HOME/Models/Qwen3.8-27B-GGUF"
rm -rf "$HOME/Library/Containers/com.docker.docker/Data/vms"
df -h /
```

## Pitfall from Hermes runtime

When disk was critically full, Hermes terminal wrapper emitted `No space left on device` while trying to write temp snapshot/cwd files. This did not invalidate the command's main output, but it signals the machine needs immediate safe space recovery before deep multi-step operations.
