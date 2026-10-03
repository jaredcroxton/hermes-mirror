---
name: render-folder-watchers
description: Use when Jared leaves a video, reel, audio, or image render running and wants Hermes to watch a local folder, then post finished media back into Telegram or another origin chat.
version: 1.0.0
author: Brock / Hermes
license: MIT
metadata:
  hermes:
    tags: [media, renders, telegram, cron, watchdog, video]
---

# Render Folder Watchers

Use this when Jared leaves a render running in Claude, HyperFrames, Remotion, ffmpeg, or another creative tool and wants the finished media sent back to Telegram for phone review.

The pattern is a script-only watcher, not an agent loop.

## Core workflow

1. Confirm or infer the render folder and expected filename.
2. Write a small watcher script under `~/.hermes/scripts/`.
3. The script scans for completed media files and stays silent when nothing is ready.
4. Schedule it with `cronjob(no_agent=True, deliver="origin")`.
5. When a file is complete, the script prints a message with `MEDIA:/absolute/path`.
6. Telegram receives the media file natively.

## When to use

- Jared says he is leaving the laptop.
- A renderer will drop files into a local folder later.
- Jared wants to view the result on his phone.
- The deliverable is a file path, especially `.mp4`, `.mov`, `.png`, `.jpg`, `.wav`, `.mp3`, or `.ogg`.

## Script requirements

The watcher script should:

- watch the exact folder Jared provided
- prefer an expected target filename if known
- fall back to new media files in the folder when acceptable
- keep a sent-file state JSON under `~/.hermes/scripts/`
- wait until the file is old enough before sending
- check file size is stable across two stats
- ignore tiny incomplete files
- print nothing when no new completed file exists
- print `MEDIA:/absolute/path` when ready

## Stability check

Use both age and size stability checks before posting:

```python
MIN_AGE_SECONDS = 20
stat1 = path.stat()
if time.time() - stat1.st_mtime < MIN_AGE_SECONDS:
    continue

time.sleep(2)
stat2 = path.stat()
if stat1.st_size != stat2.st_size:
    continue

if stat2.st_size < 1024 * 100:
    continue
```

## Cron shape

Use script-only cron so there is no model cost while waiting:

```python
cronjob(
    action="create",
    name="Watch render folder",
    schedule="every 2m",
    repeat=60,
    deliver="origin",
    script="watch_render_folder.py",
    no_agent=True,
    prompt="Watch the render folder and deliver new completed media files to the origin chat. Stay silent when no file is present."
)
```

For `no_agent=True`, empty stdout means silent. Non-empty stdout is delivered verbatim. That is the watchdog pattern.

## Output format

When ready, stdout should be short:

```text
Render ready: creator-lab-jev-reel.mp4
MEDIA:/Users/jc/path/to/creator-lab-jev-reel.mp4
```

## Verification

For video dimensions, use `ffprobe`:

```bash
ffprobe -v error -select_streams v:0 -show_entries stream=width,height,duration -of json "file.mp4"
```

A standard vertical reel should normally be `1080x1920` or another 9:16 equivalent.

## Pitfalls

- Do not post while the renderer is still writing. Use age and size stability checks.
- Do not treat missing files as an error. Stay silent.
- Do not hard-code chat IDs unless Jared explicitly asks for a different destination. Use `deliver="origin"` by default.
- Do not repost the same file repeatedly. Keep a sent-file state list.
- Do not expose secrets or credentials in cron prompts, state files, or stdout.

## Example watcher skeleton

```python
from pathlib import Path
import json
import time

RENDER_DIR = Path('/path/to/renders')
STATE_FILE = Path('/Users/jc/.hermes/scripts/.watch_render_state.json')
TARGET_NAME = 'final.mp4'
MIN_AGE_SECONDS = 20

state = {"sent": []}
if STATE_FILE.exists():
    try:
        state = json.loads(STATE_FILE.read_text())
    except Exception:
        state = {"sent": []}

sent = set(state.get('sent', []))

if not RENDER_DIR.exists():
    raise SystemExit(0)

candidates = []
target = RENDER_DIR / TARGET_NAME
if target.exists():
    candidates.append(target)

for path in sorted(RENDER_DIR.glob('*.mp4'), key=lambda p: p.stat().st_mtime):
    if path not in candidates:
        candidates.append(path)

now = time.time()
for path in candidates:
    resolved = str(path.resolve())
    if resolved in sent:
        continue
    try:
        stat1 = path.stat()
        if now - stat1.st_mtime < MIN_AGE_SECONDS:
            continue
        time.sleep(2)
        stat2 = path.stat()
        if stat1.st_size != stat2.st_size:
            continue
        if stat2.st_size < 1024 * 100:
            continue
    except FileNotFoundError:
        continue

    sent.add(resolved)
    STATE_FILE.write_text(json.dumps({"sent": sorted(sent)}, indent=2))
    print(f"Render ready: {path.name}\nMEDIA:{resolved}")
    raise SystemExit(0)

STATE_FILE.write_text(json.dumps({"sent": sorted(sent)}, indent=2))
```
