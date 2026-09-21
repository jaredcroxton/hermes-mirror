# Model routing

Core principle: do not build around one image model. Build around a routing layer. Mira decides the model from the request.

## Defaults
- Kie GPT Image 2 Text to Image: primary high quality text-to-image marketing engine. Hermes provider `kie` is installed at `/Users/jc/.hermes/hermes-agent/plugins/image_gen/kie/` and uses model `gpt-image-2-text-to-image` through `https://api.kie.ai/api/v1/jobs/createTask`, then polls `/api/v1/jobs/recordInfo`. Strong prompt following, reliable commercial compositions, and good text handling. Safe default for demos and finals when no reference image is being directly edited.
- GPT Image 2 Image to Image: intended primary route for uploaded reference images once the Kie image-to-image endpoint spec is added.
- Seedream V4 Edit: fallback image-to-image and variation engine. Use when a reference image exists and the user wants "more like this".
- Seedream V4 Text to Image: fallback fresh campaign directions from a brief with no reference image.
- OpenAI-Codex GPT Image 2: fallback if Kie credits or daily limits are exhausted and Jared wants to use ChatGPT/Codex auth.
- Nano Banana or configured provider: alternate or compatible route, especially where an existing KIE or n8n execution path is wired.
- Lite or draft models: bulk ideation and low stakes social concepts only, never the default for final brand assets until tested.

## Decision table

| User request | Best route | Why |
|---|---|---|
| "Make more images like this." | GPT Image 2 or Seedream V4 Edit | Reference consistency |
| "Edit this image." | Seedream V4 Edit | Image to image editing |
| "Create something new from this idea." | GPT Image 2 or Seedream V4 Text to Image | Text to image |
| "Give me lots of quick options." | Lite or draft model | Lower cost and speed |
| "This must look polished and on brand." | GPT Image 2 | Reliability |
| "Five social variants from this style." | Seedream V4 Edit | Variation from source |
| "Generate prompts only." | No image model | Cheap and useful first step |

## Provider route object

```json
{
  "mode": "text_to_image | image_to_image | image_to_video",
  "provider": "auto | gpt_image_2 | seedream_v4_edit | seedream_v4_text_to_image | nano_banana | configured_provider",
  "prompt": "string",
  "negative_prompt": "string",
  "reference_image_path": "string or null",
  "aspect_ratio": "16:9",
  "num_outputs": 3,
  "duration_seconds": 5
}
```

## Image to video route object

```json
{
  "mode": "image_to_video",
  "provider": "auto | kling | veo | seedance | runway | pika | fal | configured_provider",
  "source_image": "path or url",
  "prompt": "string",
  "duration_seconds": 5,
  "aspect_ratio": "16:9",
  "motion_strength": "low | medium | high",
  "camera_motion": "slow_push_in",
  "preserve_brand_style": true
}
```

## Cost control
1. Analyse image. 2. Create prompt pack. 3. Ask before paid generation, unless Jared says generate or "go for it", then act.

## Quality control
Never deliver a generated asset without the prompt used, the model used, why it fits or does not fit the source style, and the recommended next adjustment.

## Build stages
- MVP: prompt only mode plus GPT Image 2 through the configured Hermes image tool. Manual fallback prompts for Seedream.
- V2: fal API for Seedream V4 Edit and Text to Image, plus a model selector.
- V3: automatic model comparison, two outputs from GPT Image 2 and two from Seedream, reviewer ranks all.

## Security note
The source Nano Banana n8n workflow contained credential placeholders and a hardcoded bearer token. Before reusing any execution path: rotate exposed tokens, move keys into environment variables or credential stores, never store live keys in exported workflow JSON, sanitise workflow files before sharing.
