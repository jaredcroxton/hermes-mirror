# Brand-Context Depth Spectrum

When a business has a brand guide, website, or design reference, the skill should extract at TOKEN depth. When they don't, conversational depth is enough. The skill must detect which and produce accordingly.

## Two levels

| Level | What it captures | Sufficient for | Source |
|-------|-----------------|----------------|--------|
| Conversational | Voice, audience, positioning, what matters | FAQ, proposals, support, sales | 11 questions |
| Token | Hex values, CSS custom properties, font imports, type scale, spacing, button specs, do/don't visual rules | Build skills (websites, dashboards, decks) | Website scrape or brand guide |

## When to go deep

Any build skill (page-builder, slide-deck, fly-through, cinematic-build, spotlight, webcam, lead-dashboard, immersive-narrative) benefits from token-depth brand. Without it, the skill defaults to a style pole (minimal, soft, bold, authority, cinematic) and generates a visually coherent but generic output.

With token-depth brand — exact hex values, the real font import, component specs — the output reads as THAT business, not a generic business that happens to be in the same style pole.

## How to get token-depth brand

1. **The business has a brand guide.** Read it. Extract the CSS `:root` block, font imports, type scale, button specs, colour palette with ratios. Write these into brand-context-assets.md alongside the conversational brand-context.md.

2. **The business has a live website.** Run `crew-web-website-architect` on it. That skill scrapes the site, extracts CSS custom properties, type scale, spacing, and colour palette. Its output IS a token-depth brand reference. Write the tokens into brand-context-assets.md.

3. **The business has neither.** Ask the 11 conversational questions. Note in the handoff: "Token-depth brand not available. Build skills will default to style pole [chosen]. A brand guide or website URL can be added later to upgrade from generic to specific."

## The PerformOS proof case (30 June 2026)

The conversational brand-context.md for PerformOS captured: voice (direct, confident, warm), audience (business owners/ops leaders), what they do (private AI systems), products (CREW, LearnOS, Pocket Customer, PulseCheck360, Performolytics). Colours: "ink, lime, ivory." Typography: "clean and minimal."

The PerformOS Brand Guide (10 sections, extracted from PerformOS_Brand_Guide.html) captured: 10+ hex values with opacity scale (`--ink`, `--ink-60`, `--ink-40`, `--ink-12`, `--ink-06`), CSS `:root` block ready to drop into output, Google Fonts import with exact weights, type scale from hero display to label, button specs (pill, 100px radius, primary/ghost/accent variants), chip/pill/tag specs, voice traits with vocabulary to use and avoid, do/don't lists, build rules for light editorial vs cinematic campaign modes.

The conversational brand-context is enough for the FAQ builder to produce a competent PerformOS FAQ. The token-depth brand is enough for the page-builder to produce a website that looks like PerformOS. The gap is real and measurable.

## Implementation

Add a post-onboarding step to `crew-core-brand-context`:

```
Do you have a brand guide, a website, or design references I can pull from?

If yes: I'll extract token-depth brand — colours, fonts, spacing, component specs — into a companion brand-context-assets.md file. This makes every build skill produce output that looks like YOUR business, not a generic business in your style pole.

If no: no problem. The conversational brand from our 11 questions is enough for most skills. You can add a website or brand guide later to upgrade from generic to specific.
```
