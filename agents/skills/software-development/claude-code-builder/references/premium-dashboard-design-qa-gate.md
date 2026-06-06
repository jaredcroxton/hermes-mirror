# Premium dashboard design QA gate

Use when Bob or Claude Code builds any HTML dashboard, lead dashboard, landing page, deck, or client-facing interface for Jared.

## Operating model

Design QA is a reviewer with teeth, not a second builder.

- Bob owns implementation.
- `premium-dashboard-design-reviewer` owns the visual standard.
- Brock reviews only if the output affects people, money, reputation, executive alignment, or Jared's time.

Bob should not call a client-facing interface finished until the design reviewer returns PASS or PASS WITH MINOR FIXES and the minor fixes are either addressed or explicitly accepted.

## Mandatory review stack

The reviewer should draw from:

- `taste-skill`
- `awesome-design-md`
- `web-design-guidelines`
- `modern-web-design`
- `power-design`
- `emil-design-eng`
- `stitch-skill`
- `cinematic-website-build`
- HyperFrames family for motion principles:
  - `hyperframes`
  - `hyperframes-cli`
  - `hyperframes-media`
  - `hyperframes-registry`
  - `website-to-hyperframes`
  - `remotion-to-hyperframes`
  - adapters such as gsap, animejs, lottie, three, waapi, tailwind, css-animations, typegpu

## Checks

The design reviewer checks:

- brand match
- typography discipline
- visual hierarchy
- text scale
- body copy density
- premium spacing
- motion polish
- responsive behaviour
- console errors
- button and anchor behaviour
- four-tile or required structure compliance
- whether it feels like a client-ready premium artefact

## Typography lesson from AgentOS reference

When Jared references the AgentOS site as the benchmark, the key is restraint:

- dark executive surface
- ivory text
- one strong lime or blue accent
- huge but controlled hero type
- clean executive sans, not chunky generic SaaS type
- mono only for small labels and system tags
- short body copy with generous line height
- right-side visual that balances the hero
- fewer words per section

If Jared says the font is wrong, do not just resize text. Change the font feel, hierarchy, density, and rhythm.

## Pitfall

A visually strong build can still fail if it uses the wrong type treatment. Typography is part of the brand system, not a cosmetic afterthought.