# Premium design QA gate pattern

Use this reference when creating or maintaining Claude Code task agents that review client-facing UI built by Bob or a build-lane subagent.

## Pattern

Create a reviewer task agent, not another builder.

- Builder owns implementation.
- Reviewer owns the quality gate.
- Reviewer returns pass, pass with minor fixes, or fail.
- Builder fixes until the reviewer passes.

## Recommended agent

`premium-dashboard-design-reviewer`

Trigger:

> Use after Bob builds any HTML dashboard, landing page, lead dashboard, deck, or client-facing interface.

## Required review stack

The reviewer should consult these Claude Code skills where available:

- `taste-skill` for premium UI taste and anti-slop rules.
- `awesome-design-md` for top-tier design-system inspiration.
- `web-design-guidelines` for interface compliance.
- `modern-web-design`, `power-design`, `emil-design-eng`, `stitch-skill`, and `cinematic-website-build` where relevant.
- HyperFrames family for motion and animation quality: `hyperframes`, `hyperframes-cli`, `hyperframes-media`, `hyperframes-registry`, `website-to-hyperframes`, `remotion-to-hyperframes`, plus GSAP, AnimeJS, Lottie, Three, WAAPI, Tailwind, CSS animations, and TypeGPU adapters.

## Gate standard

The reviewer should fail any output that:

- Works technically but looks generic.
- Looks polished but has broken functionality.
- Uses company LinkedIn pages as decision-maker links.
- Omits source freshness for lead data.
- Has no responsive mobile layout.
- Has motion declared but not applied.
- Lacks reduced-motion handling when motion is used.
- Does not feel client-ready.

## Why this matters

The failure mode Jared identified was not lack of design skill. It was inconsistent application of the design standard. Turning design review into a mandatory gate protects the build quality without turning Bob into a designer or creating another builder with competing ownership.