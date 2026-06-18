# Seedance 2.0 — Capability Map
## Captured 18 June 2026

## Model Overview
- **Name:** Seedance 2.0 (ByteDance)
- **Released:** March 2026
- **Elo Rating:** 1269 (beats Google Veo 3, OpenAI Sora 2, Runway Gen-4.5)
- **Architecture:** Multimodal audio-video joint generation

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
| Duration | 4 to 15 seconds per clip |
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
