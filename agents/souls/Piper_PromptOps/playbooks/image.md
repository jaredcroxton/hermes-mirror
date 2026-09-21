# Image Prompt Playbook

## Job

Build prompts for image models.

## Live model table

Date checked: 04 June 2026. Verify before high-stakes work.

| Model | Best fit |
|---|---|
| Nano Banana 2, Gemini 3.1 Flash Image | Fast all-round image work with web grounding. |
| Nano Banana Pro, Gemini 3 Pro Image | Professional asset work, tighter reasoning, brand and composition control. |
| Imagen 4 | Clean realistic image generation and general commercial visuals. |
| Flux 2 | High quality stylised and photoreal work. |
| Midjourney V7 | Strong art direction and visual mood. |
| Seedream 5 | Fast creative outputs and visual variation. |
| Ideogram | Text-heavy image work and graphic layouts. |

## Core rule

Describe the scene like a director. Do not list keywords.

Build one connected brief covering:

- Subject.
- Action.
- Location.
- Composition.
- Style.
- Lighting.
- Camera or lens when relevant.
- Colour palette using plain English colour names only.
- On-screen text in quotation marks.
- Exact element counts.

## Product and cinematic prompts

Lock the crew when realism matters:

- Subject and exact count.
- Wardrobe or product material.
- Lighting setup.
- Camera body and lens.
- Angle and framing.
- Background.
- Colour palette.
- Text, if any, in quotes.

Explorer Series style constant:

Sony A7R V, 16mm f2.8, ISO 200.

## Edit prompts

For edits, change one surface or one element at a time. Do not override the whole scene unless Jared wants a new image.

Use this shape:

```prompt
Keep the original composition, camera angle, lighting, subject identity, and reflections. Change only [one element] to [new state]. Do not alter [protected elements].
```

## Reference image rule

Reference images anchor identity. The prompt steers style, mood, and composition. Use both when consistency matters.

## Jared locked rules

- Use plain English colour names. Never hex codes.
- Wrap on-screen text in quotes.
- Specify exact element counts.
- Avoid generic terms.
- JR Factory product shots use a studio white background, right side profile framing, and the logo on the number plate.
- No em dashes.
- Do not use Jared's forbidden persona name.

## Copy-ready prompt shape

```prompt
Create [image type] of [subject] [doing action] in [location]. Frame it as [composition and camera angle]. Use [lighting] with [plain English colours]. Style it as [style]. Include exactly [element count] [elements]. If text appears, it must read "[exact text]". Do not include [negative constraints].
```

## Out of scope

Do not generate the image.
Do not build video prompts here.
