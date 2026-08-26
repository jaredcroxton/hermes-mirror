---
name: social-video-captioning
description: Use when Jared sends short social videos and asks for captions, caption trials, post copy, hooks, or variants. Covers direct video inspection, transcript grounding, and punchy caption drafting for A/B tests.
---

# social-video-captioning

Use this skill when Jared sends one or more short videos and asks for captions, caption trials, post copy, hooks, or options for testing.

## Operating rule

Do not ask Jared to describe attached videos. Inspect them directly.

The job is not to summarise the video. The job is to create usable captions that match the video's argument and are ready to post or test.

## Workflow

1. **Inspect the file first.** Use `ffprobe` to confirm duration, dimensions, and whether audio exists.
2. **Create visual grounding.** Make a contact sheet with `ffmpeg` at roughly one frame per second. Identify the subject, setting, on-screen text, gestures, mood, and visual hook.
3. **Transcribe when audio exists.** Use `hyperframes transcribe` so the caption reflects what is actually said, not what the frames imply.
4. **Draft distinct trials.** If Jared says he is testing captions, produce genuinely different angles, not tiny rewrites.
5. **Keep the output lean.** Give the captions. Only add a short strategic note if one version is clearly stronger.

## Jared's default social-caption style

- Punchy.
- Active voice.
- Short lines.
- Opinionated.
- Human, not corporate.
- No em dashes.
- No long setup.
- No explaining the process.

## Default output shape

For two videos, use:

```markdown
## Video 1: [short working title]

### Caption trial one
[caption]

### Caption trial two
[caption]

## Video 2: [short working title]

### Caption trial one
[caption]

### Caption trial two
[caption]
```

If one video is stronger, say it plainly in one line.

## Useful commands

```bash
ffprobe -v error -show_entries format=duration,size:stream=index,codec_type,codec_name,width,height,r_frame_rate -of json "$video"
ffmpeg -y -i "$video" -vf "fps=1,scale=232:-1,tile=4x4" -frames:v 1 /tmp/video_sheet.jpg
hyperframes transcribe --engine auto --model base.en --language en --json -d /tmp "$video"
```

## Pitfalls

- Do not rely only on the contact sheet when the video has speech.
- Do not over-polish into brand manifesto copy unless Jared asks for that.
- Do not give ten variants when he asked for two trials.
- Do not make the caption a literal transcript. Use the transcript to find the argument, then write the post.
- When Jared pushes back on caption framing as too generic, stop expanding the concept and simplify the mechanics. For AI/folder/markdown explainer posts, the core mechanic is: AI only uses what enters its context window; folders organise the source material; markdown is plain text with headings the AI can parse; retrieval pulls the relevant sections into the answer. Avoid "business brain" language unless he asks for a strategic frame.
- When Jared asks whether HyperFrames is the best local editing software for creator reels, do not oversell it as a universal editor. Position it as a repeatable production engine, not the easiest manual timeline editor. CapCut Desktop, DaVinci Resolve, Final Cut Pro, or Premiere are better for hands-on cuts and finishing polish; HyperFrames is better for reusable 9:16 systems with captions, PiP, screenshots, proof cards, and batch variation.
- For AI creator reels in the style of a YouTube Short with talking head, proof screens, and cinematic b-roll, recommend the practical stack: HeyGen for face/avatar source, Higgsfield for pattern-interrupt b-roll, HyperFrames for composition/render, and CapCut or DaVinci only as a final polish bench.

## References

- `references/social-video-caption-trials.md` for the detailed inspection and drafting pattern.
