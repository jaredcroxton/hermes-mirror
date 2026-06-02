# Taste Bundle Placement — Why Blueprint, Not Stylize

## The question

Should the Taste bundle (`claude-design` + `popular-web-designs`) load in Phase 1 Blueprint or Phase 4 Stylize?

## The answer: Phase 1 Blueprint

**Rationale:**

Taste is a design-direction tool. It shapes *what* gets built and *how it looks*. If it loads in Stylize (the polish phase), the builder has already made all design decisions during Architect (Phase 3) without any design framework. The result is functional-first, design-second: a working file that then needs design correction.

By moving Taste into Blueprint:
- The 5 discovery questions are answered through a design-taste lens
- The design direction locks alongside the functional spec
- Phase 3 Architect executes against a locked design brief — no design debates during build
- Phase 4 Stylize is pure polish + GitHub push — no design work, just approval

**Before/after:**

| Phase 4 Stylize (OLD) | Phase 1 Blueprint (NEW) |
|---|---|
| Build without design framework | Taste bundle loads before any decisions |
| Taste checks code after it exists | Design direction locked with functional spec |
| Rework likely | No rework — design was upstream |
| Stylize = design + polish | Stylize = polish only |

## How to implement

In Phase 1, before asking the 5 discovery questions:
1. Load `claude-design` — gives the design-taste lens for every decision
2. Load `popular-web-designs` — gives 50 real brand references (Stripe, Airbnb, Figma, etc.)
3. Use both to shape the 5 answers into a design brief that is already taste-approved

## Related: heading accent anti-pattern

Using `<em>` tags with `font-style:normal` + accent color to highlight words in headings (e.g. `<h1><em>PerformOS</em> Intelligence</h1>`) creates visual clash on dark themes. It is markup pretending to be design.

**Fix:** Uniform heading text. Clean. No accent tricks. If emphasis is needed, use a `<span>` with a class — not `<em>` with overridden semantics.

Example from June 2026: the PerformOS Trending Dashboard heading was changed from `<h1><em>PerformOS</em> Intelligence</h1>` to `<h1>PerformOS Intelligence</h1>` with uniform `color:var(--primary)` and `font-weight:600`. Result: cleaner, more professional, no color clash.
