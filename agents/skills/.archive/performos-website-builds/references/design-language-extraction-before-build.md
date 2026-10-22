# Design language extraction before PerformOS website builds

Use this when Jared wants a PerformOS, AgentOS, LearnOS, or PulseCheck360 page to feel like a premium reference site before Bob or AntiGravity builds it.

## Why this matters

Jared does not want generic AI SaaS pages. Before serious website builds, extract the reference site's design language so the build starts from a clear visual system, not guesswork.

The output should translate the reference site's design decisions into an original PerformOS build. It must not copy source copy, logos, photography, videos, brand marks, or protected assets.

## Correct workflow

1. Identify one to three reference URLs.
2. Decide the output mode before briefing Bob:
   - **Neutral extraction mode:** if Jared asks to extract a reference site only, keep the deliverable strictly about the reference site. Do not inject AgentOS, PerformOS, Jared, or destination-brand recommendations.
   - **Applied build mode:** if Jared asks to use the reference for a PerformOS, AgentOS, LearnOS, or PulseCheck360 page, include translation notes for the destination brand.
3. Route the extraction to Bob_Builder if build execution is needed.
4. In Bob's brief, explicitly tell him to use the Claude Code skill:
   `/Users/jc/.hermes/profiles/bobbuilder/home/.claude/skills/design-language`
5. Ask Bob to produce a Markdown kit before any build starts.
6. Use that kit to guide the page architecture, typography, spacing, motion, and component feel.
7. Build original PerformOS/AgentOS content using Jared's copy and positioning only when the task is in applied build mode.

## Bob brief patterns

### Neutral extraction mode

Use when Jared asks to extract a reference site's design language as a standalone asset.

```text
Use the `design-language` Claude Code skill to strip apart the reference website from a design perspective. Extract the design language, layout architecture, typography, spacing rhythm, visual hierarchy, component patterns, interaction feel, page structure, and the three load-bearing decisions that make the site feel premium.

Keep this deliverable strictly about the reference website. Do not mention AgentOS, PerformOS, Jared, or any destination brand unless I explicitly ask for translation notes. Do not copy source copy, photography, videos, brand marks, or protected assets.

Reference URL: <url>
Deliverable: /Users/jc/Desktop/<reference>-design-language-extraction.md
```

### Applied build mode

Use when Jared asks to use a reference site to shape a PerformOS, AgentOS, LearnOS, or PulseCheck360 build.

```text
Before building, use the `design-language` Claude Code skill to strip apart the reference website from a design perspective. Extract the design language, layout architecture, typography, spacing rhythm, visual hierarchy, component patterns, interaction feel, page structure, and the three load-bearing decisions that make the site feel premium. Do not copy source copy, photography, videos, brand marks, or protected assets. Use the extracted design language only as inspiration for an original AgentOS by PerformOS build.

Reference URL: <url>
Deliverable: /Users/jc/Desktop/<reference>-design-language-extraction.md
```

## What the extraction should include

- executive read: why the site feels premium
- typography feel and weights
- colour system and accent usage
- spacing rhythm
- layout architecture
- section hierarchy
- component patterns
- interaction and motion patterns
- conversion architecture
- three load-bearing design decisions
- starter CSS or token guidance if useful
- limitations and methods used
- translation notes only when the task is in applied build mode

## Known implementation note

As of 01 June 2026, Bob has the `design-language` Claude Code skill installed at:

`/Users/jc/.hermes/profiles/bobbuilder/home/.claude/skills/design-language/`

The original zip was found at:

`/Users/jc/Downloads/design-language-skill.zip`

Bob may not always have Firecrawl, Apify, or Claude-in-Chrome MCP exposed. If those are unavailable, the fallback is browser rendering plus curl against live CSS bundles, with limitations stated clearly in the output. Do not encode a permanent claim that those MCP tools are unavailable because that is environment state and may change.

## Example proven output

For `https://antigravity.google/`, Bob produced:

`/Users/jc/Desktop/antigravity-design-language-extraction.md`

The useful pattern from that output:

- Start with method and limitations.
- Explain the three design choices that create the feel.
- Keep it clear that the result is a translation, not a clone.
- In neutral extraction mode, keep the file reference-only and remove destination-brand mentions.
- In applied build mode, add destination-brand translation guidance after the reference analysis.

## Pitfalls

- Do not call this an architecture diagram skill. It is design language extraction.
- Do not start building before the design language kit exists when Jared has asked for inspiration from a reference site.
- Do not copy the reference site's text, images, brand marks, or product screenshots.
- Do not lead with raw token dumps. Lead with why the design works, then provide the tokens.
- Do not overstate scraper limitations as permanent. State the method used in that run.
- Do not automatically make every reference extraction about AgentOS or PerformOS. Jared may want a neutral design-language asset first, then decide later how to apply it.
