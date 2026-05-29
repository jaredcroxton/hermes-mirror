# NotebookLM Session Notes

## Login Fix for notebooklm-py (macOS)

**Symptom:** `notebooklm login` fails with `playwright._impl._errors.TargetClosedError: BrowserType.launch_persistent_context: Target, context or browser has been closed`.

**Root cause:** Playwright not installed, or stale Chromium binary incompatible with current macOS version.

**Fix (tested 31 May 2026, macOS 26.4.1, notebooklm-py 0.6.0):**

```bash
# 1. Reinstall with browser extra
cd /tmp && UV_TOOL_DIR=$HOME/.local/share/uv/tools uv tool install "notebooklm-py[browser]" --force

# 2. Install Playwright's Chromium
$HOME/.local/share/uv/tools/notebooklm-py/bin/python -m playwright install chromium

# 3. Login with --fresh if persistent profile is corrupted
notebooklm login --fresh
```

**If login still fails with "browser closed":** Use `notebooklm login --fresh` to clear the cached browser profile. The stale profile can cause immediate closure.

**Version check:** Run `notebooklm --version` before and after to confirm upgrade took effect.

## Audio + Video Generation Pattern (Course Content)

**Use case:** Jared requests a podcast (audio) and video from a course week's NotebookLM notebook. Deliver both via Telegram.

**Pattern:**
1. Identify the correct NotebookLM notebook (check `notebooklm list`)
2. Verify sources are loaded and status=ready
3. Generate audio: `notebooklm generate audio "Focus on [key themes]" --json` -> capture artifact_id
4. Generate video: `notebooklm generate video "Focus on [key themes]" --json` -> capture artifact_id
5. Wait for both: `notebooklm artifact wait <audio_id>` and `notebooklm artifact wait <video_id>`
6. Download: `notebooklm download audio ./podcast.mp3 -a <audio_id>` and `notebooklm download video ./explainer.mp4 -a <video_id>`
7. Deliver via Telegram: send_message with MEDIA:/path/to/file in message body

**Notes:**
- Audio format: use `--format deep-dive` for detailed lectures, `--format brief` for summaries
- Video style: `--style whiteboard` or `--style classic` for educational content
- Check `notebooklm artifact list` to confirm COMPLETED status before downloading
- Generation is NOT instant (10-45 min). Use subagent pattern or notify_on_complete for long waits.
- Auth can expire mid-session. If `notebooklm list` returns auth error, re-run `notebooklm login --fresh` immediately.
