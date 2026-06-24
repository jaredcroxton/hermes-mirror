# Design Review Gate Spec

The gate-rewiring pass (25 June 2026) established the standard `## Design review gate` section for every pack-10 build skill. This is the integration point where packs 12-14 principles are enforced.

## Binding gate structure

Every build skill's design review gate must reference these packs with specific pass/fail conditions. A fail on any gate blocks the ship.

### Pack 12 — Design Standards

- **crew-design-quality:** Dimensional sweep. Typography, colour, spacing, hierarchy, motion, and execution must score above Slop on 6+ dimensions. Any dimension scoring Slop requires a ranked fix.
- **crew-design-composition:** Eye-path check. Must have one clear focal point per section. No equal-weight everything. No centered-everything unless the register demands it.
- **crew-design-patterns:** Currency check. No patterns from the dated-pattern watchlist. If a dated pattern is found and not explicitly called for by the brand playbook, swap to the current alternative.
- **crew-design-language:** Token coherence. Colours, spacing, typography must be consistent across all sections. No colour drift. No font-size lottery.
- **crew-design-reference:** At minimum, one reference site cited that informed the aesthetic.

### Pack 13 — Design Styles (register-conditional)

If a style was chosen in discovery, confirm coherence against the corresponding style skill:
- Soft → crew-design-soft (check: not Cold, not Saccharine)
- Minimalist → crew-design-minimalist (check: not Cluttered, not Barren)
- Brutalist → crew-design-brutalist (check: not Broken, not WrongLens)
- Authority → crew-design-authority (check: not generic-SaaS)

If no style was committed in discovery, this gate is advisory only.

### Pack 14 — Animation

- Motion must serve narrative or interaction, not decoration. Every animation must have a stated purpose.
- Reduced-motion path must be real (checked in code, not claimed). Under prefers-reduced-motion, non-essential motion stops. Content remains functional and legible.
- Animation skills (gsap, motion, locomotive, etc.) are authoring references — not verdict reviewers. Do not wire them as pass/fail gates. crew-design-quality's Motion dimension is the binding gate.

## Common mistakes (corrected 25 June 2026)

1. **crew-design-authority as pack 13:** It's a pack-12 bedrock skill, not a pack-13 style lens. Style-register gates use crew-design-minimalist for serious/minimalist, crew-design-brutalist for raw, crew-design-soft for warm.

2. **crew-web-design-reviewer phantom:** This skill never existed. All gate references must route to real pack-12 skills. grep and replace.

3. **Animation skills as pass/fail reviewers:** Pack-14 skills are spec-writers (emit STATUS: DONE/BLOCKED), not verdict reviewers. The binding motion gate is crew-design-quality's Motion + Interactive-states dimensions.

4. **Mandatory universal crew-design-soft:** Soft is a conditional style lens that routes fintech/authority away. Make the pack-13 leg register-conditional.

## Asset manifest series-consistency lock

Every build skill's asset manifest must include a SERIES CONSISTENCY LOCK before individual image prompts:

```
SERIES CONSISTENCY LOCK
Product: [locked — same across all frames]
Lighting: [one setup, one temperature — locked across all frames]
Varies only: composition, distance, angle, context
```

Each individual prompt inherits the lock. This prevents the #1 build-skill quality gap: inconsistent images across sections (different glow intensities, different product angles).

## Discovery gate pattern

Step 0 in every build skill reads brand-context.md first, then the per-skill handoff. The discovery section (after H1, before ## Inputs) asks the 3-way branch: fresh start / continuing / existing brand. Fresh starts run the 7 discovery questions.
