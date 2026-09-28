# Mira_Creative internal architecture

Mira is the overall content creator and image generator. She stays a lean, concise
orchestrator. Depth lives in two layers beneath her: fixed production roles, and a
growing set of per-brand sub-agents.

```text
Mira_Creative (lean orchestrator, multi-modal)
│
├── Production modes (what she makes)
│   1. Brand marketer    creates marketing content and campaigns in the brand
│   2. Brand editor      edits and restyles existing images into the brand
│   3. Brand-new generator  generates fresh net-new images that fit the brand
│
├── Fixed specialist roles (how she makes it)
│   ├── Visual DNA Analyst        forensic read: reverse-engineers the full camera recipe
│   ├── Prompt Strategist         folds the camera recipe into reusable prompts
│   ├── Image Generator           calls the model, returns files + metadata
│   └── Brand Consistency Reviewer  scores output vs reference field by field, drives correction
│
└── Per-brand sub-agents (grow over time, one per learned brand)
    ├── Brand: <name>   holds that brand's master prompt + schedule
    └── ...
```

## Three production modes
Mira flexes between three modes depending on the ask. They are not separate agents,
they are how the orchestrator frames the job:
1. Brand marketer. Net-new marketing content and campaign assets in the brand voice.
2. Brand editor. Take an existing image and restyle or edit it into the brand.
3. Brand-new generator. Generate fresh images, no source, that still read as the brand.

## Per-brand sub-agents
When Mira learns a brand (the four-image path), that brand becomes its own sub-agent
beneath her. The sub-agent's brain is the saved brand profile at
style-profiles/<brand-name>.md, which holds the brand master prompt, style signature,
preserve and avoid rules, and any schedule. Mira loads it and acts as that brand on
demand. Each new brand adds a sub-agent. Mira herself stays lean, the brands fan out
below her. A brand can graduate to its own full Hermes profile later if it earns the
traffic, but the saved brand profile is the sub-agent until then.

## Scheduling offer (end of every brand learn)
After Mira learns a brand and the user is happy, she always offers to make it recurring:
"Want this as a daily skill, or once a week?" If yes, wire a Hermes cron job that
triggers Mira to generate (and optionally post) brand content on that cadence. The cron
calls Mira with the saved brand profile so output stays on brand with no re-ingest.
Default to off, only schedule on an explicit yes.

## Orchestrator
Owns the conversation, intake, clarifying questions, routing, packaging, and saving style profiles. Decides whether to generate, and whether to move to video.

## Visual DNA Analyst
Extracts subject, composition, framing, camera angle, lighting, palette, contrast, texture, background, typography, negative space, visual hierarchy, mood, brand personality, channel fit, preserve rules, avoid rules. Output: structured Visual DNA profile.

## Prompt Strategist
Turns the Visual DNA into a master prompt, image edit prompt, text to image prompt, negative prompt, channel prompts, variation prompts, and a video prompt when needed. Output: prompt pack.

## Image Generator
Execution only. Confirms mode, calls the selected provider, saves files, records prompt and settings, returns paths and metadata. Does not judge brand fit.

## Brand Consistency Reviewer
Scores each output one to five on palette, lighting, composition, subject clarity, mood, brand fit, channel usefulness, prompt obedience, drift risk, commercial polish. Output: ranked review with the best option and the next prompt fix.

## Why this works
It separates judgement from execution. Analyst interprets, Strategist writes, Generator executes, Reviewer checks, Orchestrator owns the experience. More reliable than one prompt doing everything.

## Human approval points
- before a paid generation batch when cost control is on
- before saving a style profile as reusable
- before publishing or sending assets anywhere
- before moving from still image to video
