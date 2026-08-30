---
name: ai-video-scene-rebuilds
description: Use when rebuilding a reference video into AI-generated clips with Seedance, Higgsfield, or similar tools, especially when Jared wants himself inserted into the scene.
---

# AI Video Scene Rebuilds

Use this when Jared wants to recreate a reference video as generated clips, extract scene frames, remove social/phone UI from references, create prompt packs, or insert himself as the main walking character.

## Core workflow

1. Extract reference frames from the source video.
2. Build a clean working folder with clear names:
   - `01_reference_original_frames`
   - `02_clean_scene_refs_no_ui`
   - `02_best_scene_refs_selected`
   - `03_your_photo_drop_here`
   - `04_prompts`
   - `05_generated_clips`
   - `06_final_stitch`
3. Create a contact sheet and inspect it before giving Jared the folder.
4. Crop out phone/social UI before attempting AI inpainting.
5. Create moment-specific folders when Jared asks for a scene, e.g. temple tap, guy-looking-at-girl, kid in car, restaurant/salt-sprinkle.
6. When Jared asks to open a folder or file on his Mac, actually open the exact Finder folder/file. Do not only describe the path.

## Reference frame cleaning

Use a three-pass approach:

1. Soft crop: remove top phone UI and bottom app controls while keeping as much scene as possible.
2. Hard crop: remove remaining social overlays, labels, dots, arrows, and playback controls.
3. Selected set: remove app screens, profile screens, black screens, and non-story frames.

Only use AI inpainting on final selected frames. It can smear faces, buildings, and scene detail.

## Identity-lock workflow

When a generator creates the wrong person, simplify the setup.

Bad setup:
- Upload Jared face photo, Jared body photo, and a scene frame containing another prominent man all at once.
- This can cause Higgsfield or Seedance to copy the scene actor as the main character.

Better setup:
1. Test with only Jared's outdoor street/body photo.
2. Generate one simple five-second walking clip.
3. Do not upload the brick-wall headshot for the first identity-lock test.
4. Do not upload a scene frame with another prominent man until identity retention is proven.
5. Once identity is stable, add scene references as background-only inputs.

## Prompt pattern

Separate character and scene roles clearly:

```text
Use the uploaded Jared photo as the only identity and character reference.
Use the scene reference only for background, lighting, camera angle, street layout, and mood.
Do not copy the original person in the scene reference.
Replace the original walking character with Jared.
```

If the generator copies a headshot background, add:

```text
Use the face photo only to match identity. Do not copy the brick wall background. Do not make this a portrait. The scene must be a busy city street.
```

## Clip length judgement

Five seconds per clip is workable. But 43 clips at five seconds becomes 215 seconds, or 3:35. For a punchy social rebuild, advise six to 18 clips unless Jared explicitly wants a full-length reconstruction.

## Response style with Jared

When Jared says the result is bad:

1. Do not defend the prompt.
2. Inspect the actual output if available.
3. Name the failure plainly.
4. Simplify the next test.
5. Give one exact prompt or one exact file/folder to use next.

## Supporting references

- `references/ai-video-scene-rebuild-session-pattern.md` captures a concrete working pattern from a Seedance/Higgsfield street-walk rebuild session.
