# Kie GPT Image 2 API notes

Session learning from Mira_Creative setup.

## Use case

Use Kie GPT Image 2 as the primary high-quality text-to-image route for brand-consistent marketing assets when Mira has a prompt or Visual DNA profile but is not directly editing an uploaded reference image.

Do not treat this as the full reference-image workflow. For uploaded image → similar branded image, the image-to-image endpoint and task-detail polling endpoint are still required.

## Credential handling

Store the API key in the profile-local `.env`:

```bash
KIE_API_KEY=REDACTED
```

For Mira:

```text
/Users/jc/.hermes/profiles/miracreative/.env
```

Verify only presence, length, and shape. Never write the key into Obsidian, exported workflow JSON, prompts, packages, or chat summaries.

Common mistake: the user may paste the key as a comment, for example:

```bash
# KIE_API_KEY=...
```

That is ignored. The active line must start with `KIE_API_KEY=`.

## Text-to-image endpoint

Base URL:

```text
https://api.kie.ai
```

Create task endpoint:

```http
POST https://api.kie.ai/api/v1/jobs/createTask
```

Headers:

```http
Authorization: Bearer $KIE_API_KEY
Content-Type: application/json
```

Body:

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

For early testing, polling is simpler. For production, callbacks are cleaner.

## Required fields

- `model`: exactly `gpt-image-2-text-to-image`
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

Constraints:

- `1:1` cannot be converted to `4K`.
- If aspect ratio is `auto` or omitted, use `1K` only.
- `auto` plus `2K` or `4K` may fail validation.

Mira safe default:

```json
{
  "aspect_ratio": "16:9",
  "resolution": "1K"
}
```

Channel defaults:

- LinkedIn feed: `1:1` or `4:5`, `1K`
- LinkedIn banner or website hero: `16:9`, `1K` or `2K`
- Instagram post: `1:1` or `4:5`, `1K`
- Story, Reel cover, TikTok: `9:16`, `1K`
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

The create endpoint only returns a task ID. A complete implementation needs Kie's unified Get Task Details endpoint to poll status and retrieve the final image URL.

## Error codes to handle

- `401`: missing or invalid key
- `402`: insufficient credits
- `404`: endpoint not found
- `422`: validation error
- `429`: rate limit
- `433`: sub-key usage exceeds limit
- `455`: service unavailable or maintenance
- `500`: server error
- `501`: generation failed
- `505`: feature disabled

## Routing rule

Use Kie GPT Image 2 Text to Image when:

- no uploaded reference image is being directly edited
- Visual DNA has already been extracted and converted into a prompt
- the user wants polished campaign, social, ad, or website imagery
- the output includes text in the image
- the task needs high prompt adherence

Do not claim this endpoint covers image-to-image. Ask for or retrieve:

1. GPT Image 2 Image to Image spec.
2. Unified Get Task Details spec.
3. Result response structure and image URL path.
4. Upload/public URL requirements for image-to-image.
5. Optional account credits endpoint.

## Privacy and training language

Do not say the model trains on the client's brand or learns by training an online model.

Safer language:

- “Mira builds a private brand context from approved inputs, prompts, and feedback.”
- “It does not train a public model. It uses approved context to guide each generation.”
- “External APIs receive the prompt and, for image-to-image, the uploaded image or image URL, subject to that provider's retention terms.”
