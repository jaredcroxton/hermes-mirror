# Prompt pack templates

Fill the brackets from the Visual DNA profile. Keep every prompt editable by a non designer.

## Style master prompt (the reusable engine, build this first)

This is the most important output. Extract the STYLE from the ingested image and
leave the subject as a blank slot. Subject specific words from the source image must
NOT appear here. Only the reusable style signature.

```text
[SUBJECT / MESSAGE], rendered as a [RENDER STYLE] marketing image:
[ENVIRONMENT], lit by [LIGHTING], [FOCAL TREATMENT] against [PALETTE],
[TEXTURE AND ATMOSPHERE], [DEPTH AND CONTRAST], clean negative space for a headline.
[ASPECT_RATIO], polished commercial finish.
```

After producing it, ask the fork question (see workflow.md): "More like this" (same
subject and style) or "Use this style" (apply the look to new content). Branch 2 is
the default content-creator mode: drop the user's topic into [SUBJECT] and generate.

## Image analysis prompt

```text
Analyse this uploaded marketing reference image.
Extract the reusable Visual DNA behind it.
Focus on: subject, composition, lighting, colour palette, camera angle, texture,
background treatment, typography if present, mood, brand personality,
what must be preserved, what should be avoided.
Do not describe only what is visible. Explain what makes the image feel the way it feels.
Output a structured Visual DNA profile.
```

## Master image prompt

```text
Create a marketing image with the same visual direction as the reference style.
Visual DNA to preserve: [VISUAL_DNA_SUMMARY]
Subject: [NEW_SUBJECT]
Scene: [SCENE]
Composition: [COMPOSITION]
Lighting: [LIGHTING]
Colour palette: [PALETTE]
Mood: [MOOD]
Brand feel: [BRAND_PERSONALITY]
Preserve: [PRESERVE_RULES]
Avoid: [AVOID_RULES]
Output format: [ASPECT_RATIO], high-quality marketing asset, polished commercial finish.
```

## Image edit prompt

```text
Use the uploaded image as the visual reference.
Create a new marketing asset that preserves the look and feel while changing the content to: [CHANGE_REQUEST]
Keep consistent: [PRESERVE_RULES]
Style cues: [LIGHTING], [PALETTE], [COMPOSITION], [MOOD], [TEXTURE]
Do not copy protected logos, exact text, or proprietary assets unless explicitly supplied and approved by the user.
Avoid: [AVOID_RULES]
Aspect ratio: [ASPECT_RATIO]
```

## Negative prompt

```text
Avoid off-brand colours, harsh lighting, cluttered composition, distorted logos,
unreadable text, generic stock photo feel, plastic skin, over-saturated gradients,
random typography, extra fingers, malformed objects, low-resolution detail,
inconsistent shadows, and any visual elements that conflict with the reference style.
```

## Channel prompt slots
Adapt the master prompt per channel and aspect ratio:
- LinkedIn (1:1 or 16:9, professional, B2B)
- Instagram square (1:1)
- Instagram story (9:16)
- Website hero (16:9, generous negative space for headline)
- Email header (wide, light, text safe area)
- Paid ad (clear focal point, room for CTA)

## Video prompt

```text
Animate the selected image into a [DURATION]-second video for [CHANNEL].
Preserve the original visual DNA: [VISUAL_DNA_SUMMARY]
Camera motion: [CAMERA_MOTION]
Subject motion: [SUBJECT_MOTION]
Environmental motion: [ENVIRONMENTAL_MOTION]
Keep consistent: [PRESERVE_RULES]
Avoid: [AVOID_RULES]
The video should feel [MOOD] and suitable for [CAMPAIGN_GOAL].
```

## Prompt pack output (markdown)

```markdown
# Prompt pack
## Master prompt
## Image edit prompt
## Text-to-image prompt
## Channel prompts
### LinkedIn
### Instagram square
### Instagram story
### Website hero
### Email header
### Paid ad
## Video prompt
## Negative prompt
## Variation prompts
## Prompt repair rules
```
