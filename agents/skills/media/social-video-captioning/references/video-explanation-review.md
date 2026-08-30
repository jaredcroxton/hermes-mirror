# Video explanation review

Use when Jared sends a recorded explanation and asks whether he explained it correctly, whether he is wrong, or how to tighten the explanation. This is not a caption-writing task, but it uses the same direct video inspection and transcript grounding workflow.

## Workflow

1. Inspect the real file before judging.
   - Run `ffprobe` to get duration, streams, frame rate, and dimensions.
   - Create a contact sheet with `ffmpeg` so you can see the visual context and any slide/whiteboard support.
2. Transcribe the audio.
   - Extract mono 16 kHz audio with `ffmpeg` if needed.
   - Use an available local transcription tool such as `hyperframes transcribe` or `whisper-cli`.
   - If `whisper-cli` fails because the default model path is missing, look for an existing local Whisper model and rerun with `-m <model-path>` rather than stopping.
3. If slides are present, crop or sample frames around key moments and inspect slide text only if it is legible.
4. Review the explanation at three levels:
   - factual accuracy
   - clarity for a non-technical audience
   - overclaiming or language that creates false certainty
5. Answer directly.
   - Start with the verdict: right, wrong, or mostly right.
   - Name the one phrase to change.
   - Give Jared a cleaner replacement script he can say out loud.

## Style for Jared

Keep the response short and useful. Do not give a production critique unless he asks. He wants to know whether the explanation is correct and how to tighten it.

## Example pattern

Verdict:

> You explain the core idea correctly.

Tighten:

> Avoid saying “ensures”. That sounds like a guarantee. Say “checks and improves before it comes back”.

Replacement:

> “Prompting is me going back and forth with ChatGPT. Loop engineering is where I design a workflow so the AI does the work, checks it against the spec, fixes the gaps, then brings it back to me.”
