# Social video caption trials reference

Captured from a session where Jared sent two short vertical talking-head videos and asked for two caption trials for both.

## Proven pattern

1. `ffprobe` each video to check duration, aspect ratio, and audio stream.
2. Generate a contact sheet rather than watching frame-by-frame first:

```bash
ffmpeg -y -i "$video" -vf "fps=1,scale=232:-1,tile=4x4" -frames:v 1 /tmp/video_sheet.jpg
```

3. Use vision on the contact sheet to extract:
   - setting
   - subject
   - on-screen text
   - gestures
   - emotional tone
   - argument arc

4. Transcribe audio when present:

```bash
hyperframes transcribe --engine auto --model base.en --language en --json -d /tmp "$video"
```

5. Reconstruct the core argument from both visuals and transcript.
6. Draft two different caption angles per video.

## Good caption angles for Jared's short social clips

- **Contrarian:** The industry is asking the wrong question.
- **Everyday frustration:** Dishes, chores, admin, fatigue, repeated work.
- **Simple demand:** People do not want more thinking tools. They want boring work removed.
- **Commercial implication:** The opportunity is not replacing human thought. It is removing low-value work around it.

## Output standard

Keep it clean and directly usable. For two videos:

```markdown
Inspected both. Video two is stronger. Cleaner hook. Better structure.

## Video 1: [working title]

### Caption trial one
...

### Caption trial two
...

## Video 2: [working title]

### Caption trial one
...

### Caption trial two
...
```

## Common fixes

- If transcript has small ASR errors, correct them from visible captions and context.
- If the visual overlays already contain the hook, do not repeat the exact hook unless it strengthens the post.
- If one version is clearly stronger, name it once and move on.
