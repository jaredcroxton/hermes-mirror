---
name: marketing-content-agent
category: productivity
description: Design and build marketing content agents that turn uploaded brand/reference images into Visual DNA profiles, reusable prompt packs, image variants, optional image-to-video assets, and brand consistency reviews.
tags: [marketing, image-generation, brand, prompts, video, agents]
---

# Marketing Content Agent

Use this skill when Jared wants to design, package, build, or improve a marketing/content agent that accepts uploaded reference images and creates more assets in the same brand look and feel.

The class of work is not “image generation.” The class of work is **brand-consistent content production from reference material**.

## Core positioning

Frame the product as:

**Turn one approved visual into a reusable brand content system.**

Avoid positioning it as:

> Upload an image and make similar images.

That sounds like a toy. The stronger business value is consistency, repeatability, and speed for marketing teams.

## Core workflow

The durable operating loop is:

**Upload → Clarify → Visual DNA → Prompt Pack → Generate → Review → Optional Video → Package**

Do not jump straight from image upload to generation unless Jared explicitly asks for a quick generation test.

## PerformOS content-launch approval workflow

When Jared asks for a full PerformOS content strategy, launch plan, video campaign, or social content system but says not to act until approval, produce an Excel approval workbook rather than a prose-only plan. Use approval statuses such as `Approve`, `Decline`, `Hold`, and `Needs edit`, and make clear that only approved rows become action briefs after Jared re-uploads the workbook.

For PerformOS launch/content work, Brock orchestrates and pressure-tests. Specialist agents produce their lanes: Polly for PerformOS positioning and product-state claims, Mira for visual/video direction, Serge for SEO, Bob for builds, Nelly for source synthesis, Lara for learning-design crossover, and Harry for HR/legal understanding when a specific market/scenario risk exists. If Jared explicitly says to use sub-agents, add a governance tab or routing section to the workbook.

When Jared selects a calendar row such as `CAL-002`, route to Mira first for the production prompt, storyboard, captions, shot list, editing style, CTA, and preview-asset list. Then build only a lightweight preview/animatic unless final production is explicitly approved. See `references/performos-content-launch-approval-and-preview.md`.

## PerformOS real-world content launches

When Jared asks for a world-class content strategy for PerformOS, AgentOS, street interviews, real-life videos, founder videos, or a launch content engine, use `references/performos-ai-real-world-content-launch.md`.

Key strategic rule: do not lead with generic AI hype. Lead with the real-world confusion, risk, workflow pain, and leadership uncertainty around AI. The creative wedge is **AI in the Real World** supported by street interviews, founder field notes, workflow breakdowns, safe-AI trust content, and selective AgentOS scenario demos.

## Recommended MVP

Start with one strong orchestrator agent, not five live agents.

For the Mira-style operating pattern, use `references/mira-creative-agent-operating-model.md`. It captures the three-way intake menu, Go gate, internal roles, output standard, and image-to-video sequence.

Start with one strong orchestrator agent, not five live agents.

Working identity:

**Creative Consistency Agent**

Internal roles:

1. **Visual DNA Analyst** extracts composition, lighting, palette, texture, typography, mood, brand personality, preserve rules, and avoid rules.
2. **Prompt Strategist** turns Visual DNA into master prompts, edit prompts, text-to-image prompts, channel prompts, video prompts, and negative prompts.
3. **Image Generator** executes the selected generation route and records exact prompts, provider, settings, file paths, and errors.
4. **Brand Consistency Reviewer** compares generated outputs to the source Visual DNA, ranks options, identifies drift, and recommends prompt repairs.

The user-facing orchestrator owns intake, clarification, routing, packaging, and final recommendation.

## Clarifying questions

Before paid or time-consuming generation, ask the minimum useful questions. Do not interrogate the user.

Default compact set:

1. What is this for: social, ad, website, email, campaign, or video?
2. Should I preserve the exact style or only use it as inspiration?
3. What should change in the new asset?
4. Do you want prompts only, images, video, or images and video?

If Jared says “go for it,” proceed with sensible defaults:

- output mode: images
- variants: three
- style strength: high
- channel: social and website adaptable
- aspect ratio: source-aware, default 16:9 if unclear

## Model routing

Do not hardcode the agent around one image model. The image model is a supplier. The workflow is the product.

Use routing rules:

- **Kie GPT Image 2 via native Hermes provider:** preferred route for Mira_Creative text-to-image when `KIE_API_KEY` is present and `image_gen.provider: kie` is configured. See `references/kie-gpt-image-2-hermes-provider.md` for the createTask → recordInfo → download pattern and verification sequence.
- **GPT Image 2 via `openai-codex`:** fallback Hermes `image_generate` path when Jared wants to use his ChatGPT/Codex auth without a separate OpenAI API key, or when Kie credits/daily limits block generation. If Mira says `OPENAI_API_KEY not set`, check whether the target profile should use `image_gen.provider: openai-codex` instead of `openai`.
- **GPT Image 2:** default quality class for brand-consistent marketing outputs and reliable prompt following.
- **Seedream V4 Edit:** best fit when the user uploads a reference image and asks “make more like this.”
- **Seedream V4 Text to Image:** best fit for fresh campaign directions from a brief.
- **Nano Banana / n8n-compatible route:** use when the user's configured automation stack already provides it.
- **Lite or draft models:** use for bulk ideation only. Do not use as default final output until quality is proven.
- **Seedream V4 Text-to-Image:** useful when no source image exists and the user wants fresh campaign concepts from a brief.
- **Nano Banana or KIE-style APIs:** useful execution pattern for async create, poll, download, save workflows. Treat as a provider route, not the whole product.
- **Cheaper/lite models:** use for bulk drafts or ideation, not first-choice final brand assets until tested.

## Image provider credentials

Keep image-provider keys out of chat exports, Claude packages, workflow JSON, and Obsidian briefs. For Mira-style profile-backed agents, store keys in the profile-local `.env`, for example `/Users/jc/.hermes/profiles/miracreative/.env` with `KIE_API_KEY=REDACTED#`, it is a comment and the agent cannot read it. See `references/image-provider-credential-handling.md` and `references/kie-gpt-image-2-api.md`.

Common names:

- `KIE_API_KEY` for Kie.ai GPT Image 2
- `FAL_KEY` or `FAL_API_KEY` for fal/Seedream-style routes

If Jared struggles to reach the hidden file in Finder, open it directly with TextEdit and have him paste the key there:

```bash
open -a TextEdit /Users/jc/.hermes/profiles/miracreative/.env
open /Users/jc/.hermes/profiles/miracreative
```

Pitfall: if he enters the key as `# 3. KIE_API_KEY=REDACTED#`, numbering, or spaces around the key name. Verify only presence, length, prefix, and expected shape. See `references/image-provider-credential-handling.md` and `references/kie-gpt-image-2-api.md`.

## Privacy and training language

Do not describe Mira as training online models or training a public model on the client's brand. The safer and more accurate positioning is:

**Mira builds a private brand context from approved inputs, prompts, outputs, and feedback, then uses that context to guide each generation.**

When explaining external APIs, be clear that the provider may receive the prompt and, for image-to-image, the uploaded image or image URL. That is not the same as model training, but provider retention terms still matter.

## Image-to-video rule

Video is a second-stage workflow.

Correct sequence:

**Reference image → Visual DNA → still image outputs → user selects or approves image → image to video**

Only go straight to video if the user explicitly asks.

Before image-to-video, clarify:

1. Which image should be animated?
2. Which channel is it for: LinkedIn, Instagram, TikTok, website hero, ad, or email?
3. What motion style: subtle, cinematic, product-focused, social, or energetic?

## Output package

A complete run should deliver:

- Visual DNA profile
- prompt pack
- generated images, if requested
- generated videos, if requested
- prompts used
- provider/settings metadata
- brand consistency review
- best-option recommendation
- caption or usage notes, if requested
- reusable style profile, if approved

Never deliver generated assets without the prompt used and a short consistency review.

## Nano Banana workflow lesson

Jared provided an n8n Nano Banana blueprint that shows a useful execution pattern:

- form upload or Airtable prompt input
- image hosting if required
- async generation task creation
- wait and poll
- switch on `success`, `generating`, or `fail`
- extract result URL
- download result
- save to Google Drive or Airtable

Use this as the execution pattern, not as the whole product. The agent intelligence layer must sit before and after it.

See `references/nano-banana-workflow-pattern.md`.

## Security and sharing rule

Before putting workflow exports into a package for Claude, GitHub, or external review:

- sanitise hardcoded bearer tokens
- replace keys with `API_KEY`
- move real credentials into environment variables or platform credentials
- do not preserve live API tokens in exported JSON

## Quality gates

The agent is not done until it has either:

- delivered prompt-only outputs if requested, or
- generated images and reviewed them, or
- generated video and reviewed motion quality, or
- saved a reusable style profile if that was the task.

The best outputs explain:

- what makes the source image work
- what should be preserved
- what should change
- what must be avoided
- why the generated output is or is not on brand

## References

- `references/performos-content-launch-approval-and-preview.md` — PerformOS content strategy approval workbook pattern, sub-agent routing, CAL-row first-preview workflow, and animatic fallback pattern.
- `references/nano-banana-workflow-pattern.md` — Review and reusable pattern from Jared's Nano Banana n8n blueprint.
- `references/mira-creative-agent-operating-model.md` — Mira-style brand visual agent operating model: intake menu, Go gate, output standard, and image-to-video sequence.
- `references/image-provider-credential-handling.md` — Safe handling for fal/Seedream/Nano Banana/API keys in profile-local `.env` files and exported workflow packages.
- `references/kie-gpt-image-2-api.md` — Kie.ai GPT Image 2 text-to-image endpoint, auth variable, aspect/resolution constraints, async task pattern, and missing specs needed for full image-to-image.
- `templates/creative-consistency-agent-package.md` — Starter package outline for Claude or Hermes agent-building work.
