# SEO Content Pipeline: Keyword Brief to Production

**Class:** Multi-agent SEO content production
**Proven:** 2026-05-26 — AI Fluency Workshop cluster (9 pages, 5 agents)
**Parent skill:** `specialist-agent-deployment`

## Pipeline stages

1. **Serge (keyword brief)** — Target keywords, search intent map, competitor landscape, content mapping
2. **Polly (brand review)** — Required edits + recommended additions. Serge applies, Polly confirms.
3. **Serge (pillar draft)** — Full page copy with frontmatter, JSON-LD schema, FAQ, CTAs
4. **Serge (article briefs)** — One brief per supporting article. H2/H3 outline, keywords, internal links, CTA.
5. **Polly (brief review)** — Per-brief approval with fix list.
6. **Serge (article drafts)** — Full article copy from approved briefs.
7. **Polly (article review)** — Product-state accuracy, brand voice, vocabulary, commercial claims.
8. **Bob (HTML builds)** — Match existing site design system. Single-file HTML with inline CSS/JS.
9. **Brock (orchestration)** — Placeholder fills, pricing model decisions, keyword strategy calls.

## Routing pattern

All agent-to-agent routing uses `hermes --profile <profile> chat -q "..." --quiet`:

```
Serge:  hermes --profile sergeseo chat -q "..." --quiet
Polly:  hermes --profile pollyperformos chat -q "..." --quiet
Bob:    hermes --profile bobbuilder chat -q "..." --quiet
Lara:   hermes --profile laralearning chat -q "..." --quiet
```

## Product-state override rule

Polly's context export may be stale on product status. If Jared (founder) states a product is Live/Ship/Active, that overrides Polly's context. Do not argue. Apply the override everywhere — pillar draft, articles, link table, FAQ page, build brief. 

Example: PulseCheck 360 flagged as "PAUSED" by Polly. Jared confirmed all four instruments Live. Reverted removal across 5 files.

## Common pitfalls

- **Status label inconsistency between pages.** Homepage might say "Live" while catalogue says "Shipping." Align all labels before build.
- **Stale instruments in article briefs.** If the catalogue changes (e.g. Manager OS → PulseCheck 360), article briefs referencing old instrument names must be updated before Serge drafts.
- **Keyword brand tension.** "Instruments" is brand-true but buyers search "tools." Split: keyword targets use "tools," editorial body uses "instruments."
- **Placeholder procrastination.** Fill all placeholders before Polly second-pass. Brock makes the calls on duration, delivery, group size, pricing model.
