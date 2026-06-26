# CREW Skill Upgrade Prompt Format

Battle-tested across 93 gold-standard skill upgrades. Every prompt follows this structure.

## Template

```
**Task:** Upgrade `[skill-name]` from 5 sections to full gold-standard depth. Run in ultracode.

**Source file:** `/Users/jc/Desktop/cluade/crew-skill-packs/packs/[pack]/[skill-name]/SKILL.md`

**Reference benchmark:**
- [closest completed skill in same pack, with actual byte count and section count]

**Current state:** ~[bytes], [sections]. [One sentence describing what the skill does.]

**Promote buried Workflow into ## reference sections.** Candidates: [Section 1] (brief description), [Section 2] (brief description), [Section 3] (brief description), [Section 4] (brief description).

**Standard gold-standard sections, Discovery, Step 0 reads brand-context + own handoff.** Output header: `[OUTPUT HEADER]`. Context Loop: `.claude/crew-state/[pack]/[skill-name-handoff].md`. Fixture A/B/C. Adversarial review (3 lenses). QA on `--pack [pack]`. Report.
```

## Rules

- Task header in bold. Always starts with `**Task:**`
- Reference benchmark must include actual byte count and section count from a completed sibling skill
- Promote candidates list 4-5 domain-specific reference sections with one-line descriptions
- Output header in backticks with all caps
- Context loop path always follows `.claude/crew-state/[pack]/[skill-name-handoff].md`
- Adversarial review always specifies "3 lenses"
- QA always `--pack [pack]` not per-skill
- Report always requested: old size, new size, sections, QA result
- Use ultracode on ALL skills. Jared's policy (26 June 2026): "It's no extra cost. It just takes a little bit longer." The adversarial review catches real domain errors that standard mode misses. Never downgrade to save tokens.

## What never goes in

- Long descriptions of what the skill currently does (one sentence max)
- Instructions to "preserve existing depth" or "read source completely" (Claude already does this)
- Reminders about white-label, em dashes, banned names (the harness catches these)
- Recaps of what Jared said or what the conversation was about

## When to batch

Related pairs that form one workflow: batch them (context-save + context-restore, guard-boundary + using-crew). The adversarial review can then verify the handoff contract between them.

Unrelated skills: one prompt each. Batching splits the reviewer's attention and errors slip through.

## Adaptations per skill type

| Skill type | Q1 adaptation | Unique sections |
|------------|--------------|-----------------|
| cinematic-build | Standard 7 questions (template) | Asset manifest, cinematic pipeline |
| scroll-journey | "How many stages?" | Stage transitions, narrative pacing |
| spotlight-hero | "What's the single focal moment?" | Light-source geometry, focal composition |
| stitch | "What sections are we stitching?" | Contract dimensions, DESIGN.md |
| webcam-website | "Upload the image to transform" | Green keyer, frame extraction pipeline |
| real-estate-immersive | "Drop a realestate.com.au link" | Listing scrape, YouTube walkthrough |
| slide-deck-builder | "How many slides? Narrative arc?" | Theme selection, slide types |
| lead-dashboard-builder | "Where's your lead data live?" | Fit scoring, decision-maker lookup |
| fly-through-builder | "What's the descent journey?" | Frame pipeline, stitch stages |
| domain (sales/marketing/etc.) | Standard Discovery | Domain-specific reference sections |
