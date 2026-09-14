# Video explanation fact-checking

Use when Jared sends a short social video and asks whether the explanation, claims, or CTA are true and safe to publish.

## Outcome

Give a publish-readiness verdict. Do not only summarise the video.

## Workflow

1. **Inspect the file.** Confirm duration, dimensions, file size, audio stream, and creation/modified date when the script uses time language like "today", "this month", or "last month".

```bash
ffprobe -v error -show_entries format=duration:stream=index,codec_type,codec_name,width,height,avg_frame_rate -of json "$video"
stat -f 'Birth: %SB%nModified: %Sm' -t '%d %B %Y %H:%M:%S %Z' "$video"
```

2. **Transcribe the audio.** Use the available local transcription route. If `hyperframes transcribe` is not available, extract audio with `ffmpeg` and use `whisper-cli` or another installed transcriber.

```bash
OUT="/tmp/video_factcheck"
mkdir -p "$OUT"
ffmpeg -y -v error -i "$video" -vn -ac 1 -ar 16000 "$OUT/audio.wav"
whisper-cli -m "/path/to/ggml-model.bin" -f "$OUT/audio.wav" -l en -osrt -otxt -oj -of "$OUT/transcript" -np
```

3. **Create visual grounding.** Make a contact sheet for on-screen claims, charts, captions, URLs, model names, badges, and caveats.

```bash
ffmpeg -y -v error -i "$video" -vf "fps=1/5,scale=270:-1,tile=5x4:padding=8:margin=8:color=white" -frames:v 1 "$OUT/contact_sheet.jpg"
```

For small text, extract key frames and crop the app/browser area.

4. **Extract claims from both tracks.** Spoken claims and on-screen claims often differ. Capture exact wording for:

- URLs and brand names
- model names and parameter counts
- speeds, benchmark numbers, chart legends
- acquisition claims and whether they say announced, agreed, closed, bought, or purchased
- dates and relative date language
- revenue, funding, valuation, and multiples
- caveats such as self-reported, prototype, not independently measured, beta, or no paying customers

5. **Verify against primary sources first.** Use company sites, official newsroom posts, investor-relations releases, API metadata, live product pages, and original source articles before secondary commentary.

6. **Classify every material claim.** Use:

- checks out
- partly true, but needs safer wording
- wrong
- opinion or prediction, not fact
- not independently verified

## Publish-safety pitfalls

- Do not confuse model version with parameter count. Example: Llama 3.1 8B means version 3.1 and 8 billion parameters.
- Do not turn "announced a definitive agreement to acquire" into "purchased" unless the acquisition has closed.
- Do not treat a live demo's speed badge as an independent benchmark. Label it as service-reported unless separately verified.
- Check relative date language against the file creation date or intended publication date.
- Verify CTA status live. A workshop or event can be real but stale, sold out, or already ended.
- Watch transcription errors on domain names and company names. Confirm visually and by opening the URL.

## Default answer shape

```markdown
No/Yes/Mostly. [One-line verdict.]

## What checks out
- ...

## What needs fixing
- ...

## Safer script line
[replacement wording]

Verdict: [publish, publish after edits, or do not publish as worded]
```

Keep it lean. Jared wants the answer, not the full audit trail, unless he asks for sources.
