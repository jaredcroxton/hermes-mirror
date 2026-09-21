# Kie GPT Image 2 API notes

## Source

User-provided OpenAPI spec for Kie.ai GPT Image-2 Text to Image.

Official doc URL:

```text
https://docs.kie.ai/market/gpt/gpt-image-2-text-to-image
```

Provider base URL:

```text
https://api.kie.ai
```

Authentication:

```http
Authorization: Bearer KIE_API_KEY
```

Store the key in Mira's profile-local environment file:

```text
/Users/jc/.hermes/profiles/miracreative/.env
```

Use:

```bash
KIE_API_KEY=<secret>
```

Never hardcode the key in workflow JSON, Obsidian notes, prompts, or exported packages.

## Text-to-image endpoint

```http
POST https://api.kie.ai/api/v1/jobs/createTask
```

Required body:

```json
{
  "model": "gpt-image-2-text-to-image",
  "input": {
    "prompt": "A cinematic night city poster with neon reflections on a rainy street.",
    "aspect_ratio": "16:9",
    "resolution": "1K"
  }
}
```

Optional:

```json
{
  "callBackUrl": "https://your-domain.com/api/callback"
}
```

For early Mira testing, the installed Hermes Kie provider uses polling rather than callback. For production, prefer callback if a stable public callback endpoint is available.

Installed provider files:

```text
/Users/jc/.hermes/hermes-agent/plugins/image_gen/kie/plugin.yaml
/Users/jc/.hermes/hermes-agent/plugins/image_gen/kie/__init__.py
```

Mira profile config:

```yaml
image_gen:
  provider: kie
  model: gpt-image-2-text-to-image
  kie:
    resolution: 1K
    timeout_seconds: 180
    poll_interval_seconds: 5
```

Polling endpoint used by the provider:

```http
GET https://api.kie.ai/api/v1/jobs/recordInfo?taskId=<taskId>
```

## Required fields

- `model`: must be `gpt-image-2-text-to-image`
- `input.prompt`: required, 1 to 20,000 characters

## Aspect ratios

Allowed:

- `auto`
- `1:1`
- `3:2`
- `2:3`
- `4:3`
- `3:4`
- `5:4`
- `4:5`
- `16:9`
- `9:16`
- `2:1`
- `1:2`
- `3:1`
- `1:3`
- `21:9`
- `9:21`

## Resolution

Allowed:

- `1K`
- `2K`
- `4K`

Important constraints:

- Images with `1:1` aspect ratio cannot be converted to `4K`.
- If `aspect_ratio` is `auto` or omitted, only `1K` is valid.
- If `aspect_ratio` is `auto` and resolution is `2K` or `4K`, task creation may fail.

Mira default should be:

```json
{
  "aspect_ratio": "16:9",
  "resolution": "1K"
}
```

Unless the user specifies a channel:

- LinkedIn feed: `1:1` or `4:5`, `1K`
- LinkedIn banner or website hero: `16:9`, `1K` or `2K`
- Instagram post: `1:1` or `4:5`, `1K`
- Instagram story/Reel cover/TikTok: `9:16`, `1K`
- Wide website hero: `21:9`, `1K` or `2K`

## Success response

```json
{
  "code": 200,
  "msg": "success",
  "data": {
    "taskId": "task_gptimage_1765180586443"
  }
}
```

The returned `taskId` must be queried using Kie's unified Get Task Details endpoint.

## Error codes to handle

- `401`: missing or invalid API key
- `402`: insufficient credits
- `404`: endpoint not found
- `422`: validation error
- `429`: rate limited
- `433`: sub-key usage exceeds limit
- `455`: service unavailable or maintenance
- `500`: server error
- `501`: generation failed
- `505`: feature disabled

## Mira routing decision

Use Kie GPT Image 2 Text to Image when:

- the user has no uploaded reference image
- the user wants net-new campaign visuals from a brief
- the prompt pack has already captured brand Visual DNA
- the output requires strong text rendering inside an image
- the user wants polished marketing visuals

Do not use this endpoint for true image-to-image from an uploaded image. For that, Mira needs the Kie GPT Image 2 Image to Image endpoint spec.

## Mira text-to-image operating flow

1. Clarify channel, objective, style strictness, and output count.
2. Build or load Visual DNA.
3. Create one master prompt and channel prompts.
4. Send approved prompt to `createTask`.
5. Poll the task details endpoint until success or failure.
6. Download result image.
7. Save result and metadata.
8. Review output against Visual DNA.
9. Return image, prompt used, settings, and brand consistency note.

## Example request skeleton

```bash
curl -X POST 'https://api.kie.ai/api/v1/jobs/createTask' \
  -H 'Authorization: Bearer $KIE_API_KEY' \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gpt-image-2-text-to-image",
    "input": {
      "prompt": "Create a premium business marketing image in a calm editorial style...",
      "aspect_ratio": "16:9",
      "resolution": "1K"
    }
  }'
```

## Still needed

Ask for or retrieve these Kie specs before building the full live tool:

1. GPT Image 2 Image to Image endpoint.
2. Unified Get Task Details endpoint.
3. Result response structure, especially where the image URL appears.
4. Any file upload or public image URL requirements for image-to-image.
5. Credit/account endpoint if we want Mira to check balance before generation.
