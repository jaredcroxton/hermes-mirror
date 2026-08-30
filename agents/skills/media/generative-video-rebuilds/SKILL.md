---
name: generative-video-rebuilds
description: Use when rebuilding an existing short video with generative video tools such as Seedance, Higgsfield, Runway, Kling, or similar, especially when extracting reference frames, cleaning UI overlays, replacing the original subject with the user, writing image-to-video prompts, and preparing stitchable clips.
---

# Generative video rebuilds

Use this for social-video rebuilds where an existing clip becomes a sequence of reference frames and prompts for an external generative video tool.

## Operating stance

- Produce paste-ready prompts, not just strategy.
- Save prompt packs and run sheets when building a reusable workflow.
- Also post the exact prompt in chat when the user asks what to paste into the tool.
- Prefer a tight story sequence over rebuilding every extracted frame.

## Workflow

1. Extract evenly spaced reference frames from the source video.
2. Create a working folder with clear handoff subfolders:
   - `01_reference_original_frames/`
   - `02_clean_scene_refs_no_ui/`
   - `02_clean_scene_refs_hard_crop_no_ui/`
   - `02_best_scene_refs_selected/`
   - `03_your_photo_drop_here/`
   - `04_video_prompts/`
   - `05_generated_clips_from_video_tool/`
   - `06_final_stitch/`
3. Crop out phone UI and social overlays before using frames as scene references. For vertical screen recordings, a hard 9:16 crop is often more useful than trying to inpaint every UI element.
4. Build a selected-scene folder. Remove app/profile screens, black frames, control-centre screens, and other non-scene frames.
5. Copy identity reference photos into the photo folder using descriptive names.
6. Write a master character lock and scene-specific prompts.
7. Create a run sheet mapping scene reference, prompt group, duration, and output filename.
8. Challenge overly long rebuilds. Example: 43 clips x 5 seconds is 3 minutes 35 seconds. A tighter six clip x 5 second storyboard is usually stronger for social.

## Prompt structure

Each clip prompt should include:

1. Identity lock.
2. Scene-reference role.
3. Action beat.
4. Style and camera language.
5. UI/text removal.
6. Stitchable ending.
7. Negative prompt if the tool supports it.

Use `references/prompt-patterns.md` for reusable blocks.

## Story beats beat generic frame prompts

When the user describes a narrative sequence, turn extracted frames into story beats rather than prompting every frame.

Example:

1. User starts walking along the street.
2. User looks left and notices a side character doing a recognisable action.
3. User keeps walking and notices another pedestrian moment.
4. User passes a car and sees a child looking out.
5. User approaches a restaurant or cafe.
6. User sees a recognisable restaurant performer as the final beat.

## Quality gates

Before handoff, verify:

- Frames exist in the expected folders.
- Clean/contact sheets show usable scene references.
- Obvious UI/control/profile frames are removed from the selected folder.
- Prompt pack exists.
- Run sheet exists.
- The user has the exact first prompt in chat if they are actively using the video tool.
