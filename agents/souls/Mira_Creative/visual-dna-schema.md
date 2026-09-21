# Visual DNA schema and profile format

## Intake schema

```json
{
  "request_id": "string",
  "brand_name": "string or null",
  "brand_url": "string or null",
  "reference_images": [
    { "path": "string", "url": "string or null", "role": "primary_reference | secondary_reference | logo | existing_asset" }
  ],
  "logo_image": "path or url or null",
  "campaign_goal": "string or null",
  "target_channel": "social | linkedin | instagram | tiktok | website | email | paid_ad | video | other | unknown",
  "audience": "string or null",
  "output_mode": "prompts_only | images | video | images_and_video | style_profile",
  "preserve_style_strength": "low | medium | high",
  "preserve_composition": true,
  "allowed_changes": ["string"],
  "avoid_rules": ["string"],
  "num_image_variants": 3,
  "aspect_ratio": "16:9 | 1:1 | 9:16 | 4:5",
  "video_required": false,
  "video_duration_seconds": 5,
  "generation_route": "auto | gpt_image_2 | seedream_v4_edit | seedream_v4_text_to_image | nano_banana | configured_provider"
}
```

## Visual DNA schema

```json
{
  "summary": "string",
  "subject": "string",
  "composition": "string",
  "lighting": "string",
  "palette": ["string"],
  "camera_and_framing": "string",
  "background": "string",
  "texture": "string",
  "typography": "string or null",
  "mood": "string",
  "brand_personality": ["string"],
  "preserve_rules": ["string"],
  "avoid_rules": ["string"],
  "prompt_ingredients": ["string"],
  "confidence": "low | medium | high"
}
```

## Visual DNA profile output (markdown)

```markdown
# Visual DNA profile

## Summary
## What the image shows
## Visual language
- Composition:
- Lighting:
- Colour palette:
- Camera and framing:
- Background:
- Texture:
- Typography:
- Mood:
## Brand personality cues
## Preserve rules
## Avoid rules
## Prompt ingredients
## Confidence notes
```

## Brand review schema

```json
{
  "best_option": "string",
  "rankings": [
    {
      "asset_id": "string",
      "overall_score": 4,
      "palette_score": 4,
      "lighting_score": 5,
      "composition_score": 4,
      "mood_score": 5,
      "brand_fit_score": 4,
      "drift_risk": "low | medium | high",
      "strengths": ["string"],
      "issues": ["string"],
      "recommended_use": "string",
      "prompt_fix": "string"
    }
  ],
  "overall_recommendation": "string",
  "next_prompt_adjustment": "string"
}
```

## Final content pack schema

```json
{
  "request_id": "string",
  "summary": "string",
  "visual_dna": {},
  "prompt_pack": {},
  "generated_assets": [],
  "brand_review": {},
  "captions": ["string"],
  "style_profile_path": "string or null",
  "next_actions": ["string"]
}
```
