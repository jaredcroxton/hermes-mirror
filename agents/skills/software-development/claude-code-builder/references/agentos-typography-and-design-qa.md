# AgentOS Typography and Design QA Pattern

Use this when Jared asks Bob to build a premium AI agents, PerformOS, AgentOS, dashboard, landing page, or client-facing HTML artifact and then points to the AgentOS reference page as the quality bar.

## Durable lesson

The issue is often not visual decoration. It is typography discipline.

When Jared says a page is "not bad" but calls out text size, font, or legibility, treat it as a design-system correction, not a minor CSS tweak.

## Reference posture

Benchmark: AgentOS style, without cloning.

Mirror these principles:
- Near-black executive surface.
- Ivory or warm white text.
- One clear accent, usually lime for AgentOS or a single electric accent if the brand calls for it.
- Huge but controlled hero headline.
- Accent word treatment inside the H1.
- Sparse supporting copy.
- Small mono labels only for eyebrow text, system tags, status rows, or technical labels.
- Clean modern sans for body and headline.
- Strong right-side visual card or command-centre panel to balance the hero.
- Generous spacing and restraint.

Avoid:
- Oversized H1 that creates a tall, clumsy hero.
- Dense body copy under the hero.
- Generic SaaS fonts or decorative type choices.
- Too many cards, chips, labels, or visual noise.
- Using mono font for paragraph text.

## Bob handoff language

Add this to the build brief when relevant:

```text
Use AgentOS typography discipline as the benchmark, without cloning the AgentOS page. The correction is restraint: controlled H1 scale, clean sans typography, sparse supporting copy, mono labels only in small places, premium spacing, and a balanced right-side visual. Do not treat this as a simple font-size tweak. Re-run premium-dashboard-design-reviewer after the revision.
```

## Design QA gate

For any HTML dashboard, landing page, lead dashboard, deck, or client-facing interface:

1. Bob builds.
2. Bob opens the artifact in Chrome.
3. `premium-dashboard-design-reviewer` reviews visual quality, typography, brand fit, motion, responsiveness, console errors, and client-readiness.
4. If the verdict is fail or pass with minor fixes, Bob fixes the artifact and reruns the review.
5. Only then should the artifact be called production-ready.

A pass with minor fixes is acceptable for draft sharing. It is not final production signoff unless Jared explicitly accepts the trade-off.
