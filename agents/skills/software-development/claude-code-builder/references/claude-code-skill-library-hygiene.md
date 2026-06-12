# Claude Code Skill Library Hygiene

Use when Jared complains that Claude Code skills are messy, overlapping, or hard to choose from.

## Core principle

Skills should be **class-level**, not one-session artifacts.

A healthy skill library has fewer, stronger umbrellas with rich `SKILL.md` files and supporting `references/`, `templates/`, and `scripts/` folders.

A messy library has many narrow skills that overlap, such as separate skills for SEO, AEO, schema, competitor alternatives, and AI SEO when one SEO/AEO umbrella would guide the work better.

## Quick diagnosis

When reviewing a Claude Code skill list, flag these patterns:

1. **Duplicate strategy skills**
   - Example: `ai-product-strategy`, `behavioral-product-design`, `ai-launch-planner`, `launch-strategy`, `marketing-ideas`.
   - Likely fix: consolidate into one product or launch umbrella with references.

2. **SEO fragmentation**
   - Example: `seo-aeo-optimization`, `ai-seo`, `schema-markup`, `competitor-alternatives`.
   - Likely fix: one SEO/AEO/GEO umbrella with schema and competitor references.

3. **Build-pattern fragments**
   - Example: separate small skills for scroll pages, landing pages, cinematic sites, and one-off HTML builds.
   - Likely fix: one build/design umbrella, with templates for specific page types.

4. **Content-channel fragments**
   - Example: cold email, ad creative, brand storytelling, copy editing, referral program.
   - Likely fix: one go-to-market content umbrella with references for each channel.

## Cleanup shape

Aim for eight to 12 class-level skills, for example:

- `frontend-builds`
- `product-strategy`
- `seo-aeo-growth`
- `go-to-market-content`
- `learning-design`
- `agent-building`
- `analytics-and-evals`
- `presentation-and-decks`
- `workflow-automation`
- `research-synthesis`

Do not delete skills immediately. First map overlaps, then consolidate content into umbrellas, then archive old fragments.

## How to handle Jared in the moment

If Jared is frustrated, do not explain the entire skill architecture first.

Say the direct thing:

> You are right. This is too fragmented. We should consolidate these into fewer class-level skills so Claude Code stops loading overlapping instructions.

Then give one immediate next action.

## Safe next action

Create a consolidation map before editing:

- Current skill name
- Keep, merge, or archive
- Target umbrella
- Reason
- Any unique content worth preserving

Only after mapping should skills be patched or archived.

## Pitfall

Do not create another narrow cleanup skill for one messy list. That makes the problem worse. Update the umbrella skill or add a reference like this one.
