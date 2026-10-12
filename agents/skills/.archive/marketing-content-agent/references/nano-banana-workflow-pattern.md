# Nano Banana workflow pattern for marketing content agents

## Source

Jared provided an n8n workflow export named:

`🍌Nano Banana (BLUEPRINT)`

It is a useful execution reference for marketing content agents, especially when using async image generation APIs through KIE or similar providers.

## What the workflow proved

It contains two practical generation lanes.

### Lane 1: Image to image

1. Form trigger collects brand URL and uploaded image.
2. Uploaded image is sent to an image hosting endpoint.
3. Hosted image URL is sent to Nano Banana edit API.
4. Workflow waits.
5. Workflow polls job status.
6. Switch routes `success`, `generating`, or `fail`.
7. If still generating, it loops back to wait.
8. On success, result URL is extracted.
9. Result image is downloaded.
10. File is saved to Google Drive.

### Lane 2: Text to image

1. Manual trigger starts the flow.
2. Airtable records are searched.
3. Prompt field is extracted.
4. Prompt is sent to Nano Banana create API.
5. Workflow waits and polls.
6. On success, result URL is extracted.
7. Image is downloaded.
8. Airtable is updated with the generated image.

## Durable pattern to reuse

The reusable part is the async lifecycle:

```text
createTask → wait → recordInfo/status poll → switch state → loop if generating → extract result URL → download → save asset
```

This pattern applies to Nano Banana, Seedream via fal if async, video models, and many hosted generation APIs.

## What not to copy directly

Do not treat the n8n workflow as the complete product.

It lacks:

- clarifying questions
- Visual DNA extraction
- model routing
- prompt strategy
- brand consistency review
- image-to-video approval gate
- reusable style profile saving
- safe credential handling

## Required agent intelligence layer

Put this before generation:

```text
Uploaded image → clarify goal → Visual DNA profile → prompt pack → model route
```

Put this after generation:

```text
Generated output → compare to Visual DNA → score → recommend best option → prompt repair → package assets
```

## Clarifying question layer

Before paid generation, the agent should ask the smallest useful set:

1. What is this for: social, ad, website, email, campaign, or video?
2. Should the output preserve the exact style or use it as inspiration?
3. What should change in the new asset?
4. Do you want prompts only, images, video, or images and video?

If Jared says “go for it,” use sensible defaults and proceed.

## Video extension

Do not go straight from uploaded reference image to video unless explicitly requested.

Preferred sequence:

```text
Reference image → Visual DNA → still image variants → user selects/approves → image-to-video
```

Video prompt should specify:

- duration
- aspect ratio
- camera motion
- subject motion
- environmental motion
- preserve rules
- avoid rules
- channel use

## Credential pitfall

The workflow export contained a hardcoded bearer token in at least one node.

Before packaging workflows for Claude, GitHub, or external review:

- replace bearer tokens with `Bearer API_KEY`
- move live keys into n8n credentials or `.env`
- rotate any token that has been exposed in exported JSON

## Recommended route object

```json
{
  "mode": "text_to_image | image_to_image | image_to_video",
  "provider": "auto | gpt_image_2 | seedream_v4_edit | seedream_v4_text_to_image | nano_banana | configured_provider",
  "prompt": "string",
  "negative_prompt": "string",
  "reference_image_path": "string or null",
  "aspect_ratio": "16:9 | 1:1 | 9:16 | 4:5",
  "num_outputs": 3,
  "duration_seconds": 5
}
```

## Strategic lesson

The model is not the product.

The product is the workflow that turns brand reference material into repeatable marketing content:

**Clarify → Visual DNA → Prompt Pack → Generate → Review → Optional Video → Package**
