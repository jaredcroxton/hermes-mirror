# Seedance 2.0 — Capability Map
## Captured 18 June 2026

## Model Overview
- **Name:** Seedance 2.0 (ByteDance)
- **Released:** March 2026
- **Elo Rating:** 1269 (beats Google Veo 3, OpenAI Sora 2, Runway Gen-4.5)
- **Architecture:** Multimodal audio-video joint generation

## Seedance 2.5 (Released July 2026) — Key Upgrades
- **Duration:** Up to 30 seconds single generation (was 15s)
- **Multi-modal references:** Up to 50 (images, video, audio) — was 12 total
- **Region-level editing:** Regenerate only a specific section of a clip
- **Native audio sync:** Dialogue, SFX, music baked in with lip-sync
- **Tempo shifts mid-clip:** Can change pacing inside one generation
- **Persistent characters across sessions:** Via reference system
- **Prompt adherence:** +20% over 2.0
- **Scene changes:** Handle scene changes inside a single generation while character, lighting, camera stay consistent
- **Platforms:** Higgsfield.ai, fal.ai API, OpenArt.ai, SeaDance.io, Imagine.Art, Neural4D

## Inputs
| Type | Limit | Notes |
|---|---|---|
| Images | Up to 9 | Max 6000×3000 px each |
| Video clips | Up to 3 | Max 15 seconds each, 720p, 24fps |
| Audio clips | Up to 3 | Max 15 seconds each |
| Text prompt | Up to 2,500-3,000 chars | Character limit varies by platform |
| Total assets | 12 files max | Across all types |

## Outputs
| Spec | Value |
|---|---|
| Resolution | 720p native (upscale to 4K post-generation) |
| Duration | 4 to 30 seconds per clip (2.5: up to 30s single gen) |
| Aspect ratios | 21:9, 16:9, 4:3, 1:1, 3:4, 9:16 |
| Audio | Native co-generation — lip-sync, music, SFX, dialogue, ambient |
| Format | MP4 |

## Platforms
| Platform | Model Tier | Pricing |
|---|---|---|
| Higgsfield.ai | Fast + Standard | 17 credits/5s (Fast 720p), 22 credits/5s (Standard 720p). Plans from $19/mo. 30-day unlimited Fast promo. |
| fal.ai API | Fast only | $0.2419/sec of 720p video (~$2.42 for 10s) |
| Topview AI | Standard | Business Annual plan includes 365 days unlimited |
| Imagine.Art | Standard | App-based |
| Picsart | Standard | Integrated into creative suite |
| Artlist | Standard | Integrated into AI Toolkit |

## Key Capabilities
- **Multi-shot within one generation:** Timeline prompting with [0s] [3s] [6s] markers
- **Camera control:** Dolly, pan, tilt, tracking, crane, handheld, rack focus, arc shot
- **Elements system:** Save custom characters/props/locations with @ references for cross-video consistency
- **Text in video:** Slogans, subtitles, speech bubbles — auto-matched font/colour
- **First-frame control:** Upload image as starting visual anchor
- **Audio-video co-generation:** Audio generated alongside video in a single pass
- **Lip-sync:** Multiple languages, synced with character speech
- **Physics-aware:** Realistic collisions, fabric, character motion
- **Upscaling:** 720p → 4K inside Higgsfield

## Critical Limitations (updated 24 June 2026)

| Limitation | Detail | Workaround |
|---|---|---|
| **No realistic human faces** | Identifiable faces blocked entirely. Use Seedance 1.5 Pro, Kling, or Veo 3.1 for people. | Product-only spectacle. Layer real human footage in post. |
| **Best for scenes/architecture/environments** | Excels at products, spaces, abstract visuals. Struggles with realistic people. | Lean into the strength. Build worlds, not characters. |
| **720p native** | Upscale to 4K post-generation inside Higgsfield. | Factor upscale step into production timeline. |

## Seedance 2.5 Specific Capabilities (Added August 2026)

| Capability | Description | Use Case |
|---|---|---|
| **30-second single generation** | One continuous clip, no stitching needed | Full narrative beats, multi-shot sequences |
| **Up to 50 multi-modal references** | Images, video clips, audio files | Complex character consistency, brand asset libraries |
| **Region-level editing** | Regenerate only a specific section | Fix hands, faces, background elements without full re-roll |
| **Native audio sync** | Lip-sync, music, SFX, dialogue co-generated | Character speaking, synced action + sound |
| **Tempo shifts mid-clip** | Change pacing inside one generation | Slow build → fast action → slow resolution |
| **Scene changes in single gen** | Character/lighting/camera consistent across scene cuts | Multi-location stories, before/after transformations |
| **Persistent characters across sessions** | Reference system maintains identity | Series content, recurring characters |

## 2D Anime Generation with Seedance 2.5 (Added August 2026)

**Why Seedance 2.5 works for 2D anime:**
- No realistic face restriction applies — stylised anime faces are not "identifiable human faces"
- Consistent character references via @Elements system (upload character sheets)
- 30-second generations allow full anime scene beats (establish → action → reaction)
- Native audio sync for dialogue, SFX, OST-style music
- Region editing fixes common anime issues: hand signs, eye expressions, effect layers

**Prompt pattern for 2D anime:**
```
@character_ref as main character, preserve face and outfit exactly + [one concrete action] + [stylised environment] + [one camera move] + [anime lighting: cel-shaded, rim light, limited palette] + [era anchor: 2000s digital / 90s cel / modern hybrid]
```

**Hard rules for anime:**
- Under 80 words (same as all Seedance)
- One camera move per shot
- Max 2 characters (3+ = face drift even in stylised)
- No on-screen text — add in CapCut post
- Reference images first: upload character turnarounds as @Elements before prompting
- Fast mode for drafts, Standard for keepers
- 40% keeper rate target
| **Best for scenes/architecture/environments** | Excels at products, spaces, abstract visuals. Struggles with realistic people. | Lean into the strength. Build worlds, not characters. |
| **720p native** | Upscale to 4K post-generation inside Higgsfield. | Factor upscale step into production timeline. |

## Updated Prompt Structure (Newly.app guide, April 2026)

The most reliable Seedance 2.0 prompt follows a strict 4-part order:

```
Subject and action (verb-first) → Camera movement → Sound direction → Transition or ending beat
```

| Position | What goes there | Example |
|---|---|---|
| 1. Subject + Action | Verb-first. One primary action. | "A hand swipes through a budgeting app." |
| 2. Camera | Real cinematography terms. One move. | "The camera pushes in slowly from a three-quarter angle." |
| 3. Sound | Audio cues: UI taps, crowd swell, synth bed. | "Soft UI taps and a subtle warm synth hit." |
| 4. Transition/End | Cut label or final frame spec. | "End on the completed goal ring with logo appearing." |

The old formula (Subject → Action → Camera → Scene → Style → Audio hints) still works but the 4-part structure is more reliable for product and launch content.

## Prompt Engineering Rules

### The Director Mindset
Write what the camera sees, not what a character feels. Abstract adjectives are noise. Physical detail is signal.

| Bad | Good |
|---|---|
| She is sad | Disheveled hair clings to pale cheeks, trembling fingertips clutch a faded photograph |
| A dramatic scene | Cold blue neon halos reflect on wet asphalt, rain slides down her temple |
| He ran fast | He glances nervously behind, flips up his collar, and sprints along the wall |

### Universal Formula
```
Subject → Action → Camera → Scene → Style → Audio hints
```
First 20-30 words anchor subject and action. Style words come after.

### Timeline Template
```
[0s] Wide establishing shot: [scene]. Static camera.
[3s] [Camera movement]. [What changes].
[6s] Close-up on [detail]. Shallow depth of field.
[8s] Pull back / hold / exit. [Resolution].
```

### Cinematography Vocabulary
**Camera movements:** Slow dolly in/out, pan left/right, tilt up/down, tracking shot, crane/jib up, arc shot (orbit), handheld (organic shake), Steadicam walk, pull back reveal

**Lens & focus:** Shallow depth of field, rack focus, anamorphic lens flare, long lens compression, deep focus

**Lighting:** Motivated from window/lamp, hard rim light, low-key, silhouette, golden hour, practical tungsten, hard side-lighting

**Colour grades:** Teal and orange (classic cinematic), bleach bypass (desaturated gritty), warm Ivory tones + deep Ink shadows, cool blue tones, high contrast

**Shot types:** Wide shot (WS), Medium shot (MS), Close-up (CU), Extreme close-up (ECU), Over-the-shoulder (OTS)

### Hard Rules
1. One clear action per shot. Multi-action prompts confuse the model.
2. Use cinematography terms — the model responds to them.
3. Keep clips under 10 seconds for best consistency.
4. Use @Elements for character/product consistency across videos.
5. Generate fast, curate later. Volume compounds. 40% keeper rate is excellent.

## Higgsfield 30-Day Unlimited Promo
- "Enhanced Seedance 2.0 Fast Unlimited" for 30 days
- Also includes 7-day Nano Banana Pro Unlimited
- Fast model only (half credits of Standard)
- Normal pricing context: Ultra plan ($99/mo, 3,000 credits) ≈ 2,000 Fast clips
- Promo delivers effectively unlimited generations for 30 days
- Risk: Some users report throttling or queue prioritisation on heavy use
