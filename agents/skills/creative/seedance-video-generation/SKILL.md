---
name: seedance-video-generation
description: Use when Jared asks to create AI video prompts, video content strategies, or marketing video assets using Seedance 2.0 (ByteDance) or similar AI video generation models. Covers prompt engineering rules, model capabilities and limitations, reference image workflows, and the hybrid AI+real-footage editing pattern.
tags: [seedance, video, ai-video, prompting, content-strategy, marketing, higgsfield]
---

# Seedance AI Video Generation

## Trigger

Use when Jared asks to:
- Create video prompts for Seedance 2.0 or similar AI video models
- Build a video content strategy using AI-generated footage
- Generate marketing videos, brand films, product demos, UGC-style ads, or launch assets
- Understand what Seedance 2.0 can and cannot do before building prompts

## Model Overview

Seedance 2.0 is ByteDance's multimodal AI video generation model (1269 Elo, beats Veo 3, Sora 2, Runway Gen-4.5). It is a **reference-driven conditioning engine**, not a simple text-to-video tool. It accepts up to 9 images, 3 video clips, 3 audio files, and text in a single generation. Outputs 720p-1080p video at 4-15 seconds.

Primary platforms: Higgsfield.ai (30-day unlimited Fast promotion), fal.ai API, Topview AI, Imagine.Art, Picsart, Artlist.

Two model tiers:
- **Fast:** 2x speed, half credits, identical capabilities. Use for all drafts and iteration.
- **Standard:** Full quality. Use only for final keepers after the look is locked in Fast.

## The Non-Negotiable Prompt Rules

These rules come from extensive research across actual user testing, not marketing material. Break them and the output will be unusable.

| Rule | Why |
|---|---|
| **Under 80 words** | Beyond ~80 words the model cherry-picks random details and invents the rest |
| **Subject → Action → Scene → Camera → Style** | Fixed order. The model weights early tokens heavier |
| **One camera move per shot** | Pan + zoom + tracking in one prompt = jittery garbage |
| **Max 2 characters** | Three or more = faces drift, bodies warp |
| **No on-screen text** | 90% garbled. One large centered word max |
| **No fast hand gestures** | "Rapidly gestures while counting" = extra fingers, fused hands. Slow movements only |
| **Start at 5 seconds** | Lock the look first on a 5s clip. Scale up once it holds |
| **Fast for drafts, Standard for keepers** | Never generate first attempts in Standard. Waste of credits |
| **Tag every reference image explicitly** | `@image1 as the main character, preserve face and outfit` — without this the model may use your face as wallpaper texture |

### What "Director Thinking" Means

Write what the camera sees, not what a character feels. Abstract adjectives are noise. Physical detail is signal.

| Bad (Narrator) | Good (Director) |
|---|---|
| She is sad | Disheveled hair clings to pale cheeks, trembling fingertips |
| A dramatic scene | Cold blue neon halos reflect on wet asphalt |
| Cinematic lighting | Soft key light from the left, warm rim light, shallow depth of field, film grain |

### The Universal Prompt Template

```
[Specific subject with age, clothing, expression] + [One concrete physical action] +
[Environment with objects, textures, time of day] + [One camera movement with framing] +
[Lighting source, direction, quality] + [Style anchor and finish]
```

Example (62 words, good):
> A woman in her 30s, dark hair pulled back, navy linen blazer, turns slowly toward the camera and smiles. Standing on a rooftop terrace at sunset, city skyline behind her. Medium close-up, slow dolly-in. Soft key light from the left, warm rim light, shallow depth of field, film grain.

Example (bad — what NOT to write):
> A beautiful cinematic scene of a stylish woman at sunset looking confident and powerful, epic camera work, professional lighting, premium film look.

### Camera Language That Works

- **Framing:** Wide shot, medium shot, medium close-up, close-up, extreme close-up, over-the-shoulder, top-down
- **Movement (pick ONE):** Slow dolly in/out, locked tripod with micro push-in (1-3%), tracking shot left to right, slow pan with stop point, static, slight lateral slide
- **Moves that break:** 180° wraps, crash zooms with subject motion, spiral dollies, stacking multiple moves

### Lighting Language That Works

Name source, direction, quality. Never say "cinematic lighting."

- "Soft key light from the left, warm rim light, shallow depth of field"
- "Motivated window light, warm amber tones, deep shadows on the opposite side"
- "Screen glow as the only light source, cool blue spill on the face, dark room"
- "Harsh midday sun, slightly overexposed, handheld energy"

### Style Anchors That Work

Pick one primary style + one reinforcement. Never stack adjectives.

- `cinematic, soft contrast, warm grade, 50mm`
- `editorial, high micro-contrast, cool grade, handheld micro-sway`
- `product-focused, controlled reflections, white sweep background, 85mm macro`
- `iPhone handheld, slightly overexposed, harsh midday sun`

## What Seedance 2.0 Excels At

- Single-subject scenes with slow camera moves
- Realistic physics: fabric movement, water, reflections, collisions
- Neon and rain on wet surfaces (noir aesthetic)
- Subtle facial expressions and micro-movements
- Talking-head direct address (medium close-up, locked camera)
- Product floating/rotating on clean backgrounds
- Atmospheric single-location shots with strong lighting

## What Seedance 2.0 Cannot Do

These are hard constraints. Do not write prompts that require them.

| Limitation | Workaround |
|---|---|
| **Cannot render realistic software UI** | Use real screen recordings (QuickTime). Generate Seedance human reaction shots. Edit together in CapCut/DaVinci |
| **Cannot produce readable on-screen text** | One large centered word max. All text overlays done in post |
| **Cannot hold 3+ consistent characters** | Max 2. Crowds must stay blurry background elements |
| **Cannot handle multi-character multi-shot in one generation** | Generate each character/shot individually. Edit together in post |
| **Cannot do fast complex hand gestures** | Slow deliberate movements only. "Gently raises one hand" not "rapidly gestures" |
| **Cannot execute multiple camera moves in one prompt** | One move per shot. Pan OR zoom OR track. Never combine |
| **Cannot handle prompts over ~100 words** | The model cherry-picks. Stay under 80 |

## The Hybrid Workflow (Critical)

For any video that involves a product interface, dashboard, or software:

1. **Generate the human element in Seedance:** Person at desk, reacting to screen, looking satisfied/relieved/focused. The screen glow is visible but the content is NOT. Prompt specifies "screen content not visible" or "screen glow visible but content blurred."
2. **Record the real product:** QuickTime screen recording of the actual PerformOS product interface.
3. **Edit together in CapCut or DaVinci Resolve:** Intercut Seedance human reaction shots with real screen recordings. Add text overlays, end cards, and voiceover.
4. **Export at 1080p minimum.**

For multi-shot sequences (launch hero, training promo):
1. Generate each shot/scene as a separate Seedance generation
2. Edit the clips together in post
3. Never attempt a multi-shot narrative in a single generation

## The Reference Image System

Before generating any talking-head or character-consistency video:

1. Upload a clean, front-facing, well-lit photo of the person (or AI-generated consistent character portrait)
2. In the prompt, reference it: `@image1 as the main character, preserve face and outfit exactly`
3. Use the same @image1 reference across all videos in the same series
4. Upload separate references for: product shots, logo, brand colour swatches, background locations

Without explicit role assignment, the model guesses what each uploaded file does — often using a character reference as background texture.

## UGC / Street Interview Pattern

Street interview or multi-person reaction videos must use the individual-shot pattern:

1. Write one prompt per character: one person, one line, one location
2. Generate each as a separate 8-second clip
3. Edit together with fast jump cuts in CapCut
4. Add the "iPhone handheld, harsh midday sun, slightly overexposed" style anchor to every prompt
5. Vary the character description and background across shots

Never attempt 5 characters with 5 lines in a single 12-second generation. Faces will morph. Dialogue will desync. The output will be unusable.

## Common Pitfalls

- **Overwriting prompts.** The first instinct is to write 150-word narrative descriptions. This produces garbage. Every prompt must be under 80 words with one clear physical action.
- **Abstract brand metaphors fail.** "Ink drops resolving into a logo" and "light emerging from darkness" produce weird, unusable outputs. Use physical scenes with real objects and clear action.
- **Expecting the model to do the editing.** Seedance generates individual shots. Multi-shot sequences, text overlays, voiceovers, and end cards are assembled in post.
- **Generating directly in Standard mode.** Always draft in Fast. Standard costs double credits and takes twice as long. Only use it for the final keeper of hero videos.
- **Skipping reference images for character consistency.** The model cannot remember what your founder looks like across generations. Upload a reference image and tag it in every prompt.
- **Putting "cinematic" as the only style direction.** The word "cinematic" alone produces flat gray output. You must spell out the lighting recipe like you are briefing a director of photography.

## End Card Pattern

Generate a clean brand end card as a standalone 4-second clip:
- Static camera, clean background (PerformOS: warm Ivory with subtle grain)
- Logo mark centred
- One subtle animation (lime dot pulse at 2-second mark)
- No text beyond the brand wordmark
- Generate in all three formats: 16:9, 9:16, 1:1

Attach this end card to every video in post-production.

## PerformOS-Specific Notes

- Brand colours for reference images: Ivory #f2efe8, Ink #0a0a0a, Electric Lime #d4ff3b
- Logo: concentric circle mark (Ink outer ring, Lime inner dot) + Instrument Serif wordmark
- For founder/talking-head videos: upload a consistent reference image as @image1
- For product shots: the four instruments are Pocket Customer, LearnOS, PulseCheck 360, Performlytics
- All product demos use the hybrid workflow: Seedance human reaction + real screen recording

## References

- `references/seedance-research-sources.md` — Full research bibliography and source excerpts from the 18 June 2026 deep dive
