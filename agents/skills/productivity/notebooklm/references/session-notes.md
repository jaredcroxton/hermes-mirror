# NotebookLM Session Notes

## Login Fix for notebooklm-py (macOS)

**Symptom:** `notebooklm login` fails with `TargetClosedError`.

**Fix (tested 31 May 2026, macOS 26.4.1, notebooklm-py 0.6.0):**

```bash
cd /tmp && UV_TOOL_DIR=$HOME/.local/share/uv/tools uv tool install "notebooklm-py[browser]" --force
$HOME/.local/share/uv/tools/notebooklm-py/bin/python -m playwright install chromium
notebooklm login --fresh
```

Use `--fresh` to clear a corrupted persistent browser profile.

## Audio + Video Generation Pattern

1. Create notebook, add sources, wait for source processing
2. `notebooklm generate audio "..." --json` and `notebooklm generate video "..." --json`
3. Wait with `notebooklm artifact wait <id> -n <notebook_id>`
4. Download with `notebooklm download audio/video`
5. Deliver via Telegram MEDIA tag

Audio takes 10-20 min. Video takes 15-45 min. Do not poll in main conversation.

## Video Rate Limit: Artifact Removed from Server

**Symptom:** `artifact wait` reports "artifact was removed from the list by the server."

**Cause:** Google daily quota exceeded. The artifact vanishes from `artifact list`.

**Fix:** Wait 30-60 min. Generate videos one at a time, not in parallel. Fallback: use NotebookLM web UI.

**Do NOT:** Retry immediately in a loop.

## Telegram Media Upload Limit

Files over ~3-5MB fail to upload via `send_message` MEDIA tag (gateway HTTP timeout, not Telegram API limit). Compress audio with ffmpeg `-b:a 32k -ar 22050` to get under 3MB before sending. For large files, tell user the Desktop path instead.
