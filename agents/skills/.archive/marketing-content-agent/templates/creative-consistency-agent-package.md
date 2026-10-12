# Creative Consistency Agent package outline

Use this template when preparing a Claude-ready or Hermes-ready package for a marketing content agent.

## README.md

Explain the product idea:

**Turn one approved visual into a reusable brand content system.**

Include:

- package purpose
- core workflow
- model routing summary
- file list
- recommended implementation path

## 01-product-brief.md

Include:

- working name
- one-line description
- buyer problem
- product solution
- MVP scope
- later scope
- non-negotiables

## 02-agent-architecture.md

Recommended structure:

```text
Creative Consistency Agent, Orchestrator
├── Visual DNA Analyst
├── Prompt Strategist
├── Image Generator
└── Brand Consistency Reviewer
```

Start with one live orchestrator agent and internal roles. Split into separate live profiles only after the MVP works.

## 03-workflow.md

Document:

```text
Upload → Clarify → Analyse → Prompt → Generate → Review → Optional Video → Package
```

Include clarification questions and failure modes.

## 04-model-routing.md

Document routing rules:

- GPT Image 2 for high-quality brand-consistent output
- Seedream V4 Edit for reference-image variation
- Seedream V4 Text-to-Image for fresh campaign concepts
- Nano Banana or similar as async execution route
- video provider only after image approval

## 05-implementation-plan.md

Recommended path:

1. Claude design pass using agent-development skill.
2. Save approved design to Obsidian.
3. Create one Hermes specialist profile.
4. Wire upload handling, vision, generation, and file delivery.
5. Verify with a real uploaded image.

## 06-provider-workflow-review.md

If a provider or n8n blueprint is supplied, review it as an execution pattern.

Always separate:

- what the workflow already proves
- what the agent intelligence layer must add
- credential risks
- provider-specific assumptions

## 07-image-to-video-extension.md

Document the second-stage workflow:

```text
Approved still image → video prompt → image-to-video model → motion review → final pack
```

## agent-specs/

Include Claude-style or Hermes-style specs for:

- creative-consistency-orchestrator.md
- visual-dna-analyst.md
- prompt-strategist.md
- image-generator.md
- brand-consistency-reviewer.md

## schemas/input-output-schema.md

Include schemas for:

- intake
- Visual DNA
- prompt pack
- generation route
- generation result
- brand review
- final content pack

## prompts/master-prompt-template.md

Include templates for:

- image analysis
- master image prompt
- image edit prompt
- text-to-image prompt
- negative prompt
- video prompt

## workflows/image-to-content-pack.md

Write the full operating workflow and quality gate.

## Zip delivery

Package the folder as a zip and send it as a Telegram `MEDIA:` file when Jared asks for Claude-ready material.
