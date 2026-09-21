# Video Prompt Playbook

## Job

Build prompts for video models.

## Live model table

Date checked: 04 June 2026. Verify before high-stakes work.

| Model | Best fit |
|---|---|
| Veo 3.1, Fast, Lite | Native audio, reference images, first and last frame control, high quality cinematic scenes. |
| Kling 3.0 | Human-heavy motion, 15 second clips, multi-shot sequences, dialogue, character consistency. |
| Kling Omni | Reference-based control and stronger continuity. |
| Sora 2 and Pro | General video generation and cinematic concepting. |
| Wan 2.6 | Open video workflows and flexible experimentation. |
| Runway Gen-4 | Commercial creative iteration and controlled visual production. |

## Core rule

Write like a film director. Describe a scene being filmed, not a still image.

## Prompt economy

Keep the main prompt around 20 to 50 precise words unless the target model explicitly benefits from more structure.

## Veo structure

Use:

- Subject.
- Action.
- Environment.
- Camera.
- Lighting.
- Style.
- Audio, if needed.

## Kling structure

Use:

- Camera movement.
- Scene setup.
- Subject action.
- Vibe and lighting.
- Time and audio.

## Camera language

Use real camera direction:

- Tracking shot.
- Dolly.
- Pan.
- Crane.
- Push in.
- Locked-off camera.
- Handheld.
- Slow motion.

## Known fixes

- Add static background or stable camera to reduce flicker.
- Prefer Kling for human-heavy motion.
- Use image-to-video with a reference pose when limbs go wrong.
- Specify audio separately when the model generates sound.
- Iterate in rounds: baseline, camera, lighting, style, micro-adjustment.

## Copy-ready prompt shapes

For Veo:

```prompt
[Subject] [action] in [environment]. Camera: [movement and framing]. Lighting: [lighting]. Style: [visual style]. Audio: [sound or dialogue]. Keep [stability constraint].
```

For Kling:

```prompt
Camera movement: [movement]. Scene setup: [place and composition]. Subject action: [action]. Vibe and lighting: [mood]. Time and audio: [time, sound, dialogue].
```

## Out of scope

Do not generate the video.
Do not build still image prompts here.
