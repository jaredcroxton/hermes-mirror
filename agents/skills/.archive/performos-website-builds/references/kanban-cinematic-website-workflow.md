# Kanban-driven PerformOS cinematic website production

Use this when Jared asks for an immersive PerformOS website and wants the agent ecosystem to produce it through Kanban.

## Recommended task graph

Use three agents only unless the scope clearly needs more.

```text
Polly_PerformOS
  validates offer, positioning, buyer message, claim risk, CTA, pricing frame
      ↓
Bob_Builder
  builds the single-file cinematic HTML artefact and verifies locally
      ↓
Brock
  reviews commercial readiness before Jared sends it to businesses
```

Do not add extra agents by default. More agents add noise unless there is a real source-research, learning-design, HR, or academic lane.

## Polly card pattern

Title:

```text
Polly review: PerformOS Private AI Team offer and brand direction
```

Body essentials:

- Validate product positioning, offer logic, target buyer, brand fit, and sales narrative.
- Confirm the $4,999 AUD/month offer is framed clearly.
- Check trust language and risk language.
- Flag overclaims, especially any suggestion that PerformOS products are deployed, approved, or live with clients if that has not been confirmed.
- Handoff must give Bob the strongest hero message, CTA, pricing framing, and section order.

## Bob card pattern

Title:

```text
Bob build: cinematic PerformOS Private AI Team website
```

Body essentials:

- Build one single self-contained HTML file.
- Use the website brief and PerformOS brand styles.
- Use the actual asset folder path, including spelling and trailing spaces if present.
- Make it cinematic, immersive, premium, scroll-driven, and commercially clear.
- Include the $4,999 AUD/month offer.
- No fake testimonials.
- No fake logos.
- No fake client claims.
- No public deployment without Jared approval.
- Verify locally and report the file path plus checks run.

## Brock review card pattern

Title:

```text
Brock review: commercial readiness of PerformOS website
```

Review criteria:

- Does it sell the $4,999 AUD/month offer clearly?
- Is it credible for business buyers?
- Does it avoid overclaiming deployed, live, or client-approved status?
- Is the CTA obvious?
- Is the pricing framed properly?
- Is the risk and governance language strong enough?
- Does the visual style support premium trust, not gimmick AI hype?
- What is the single next decision for Jared?

## Commercial success standard

The site should help a business buyer understand the offer in under 10 seconds and want to book a private AI team setup call.

## Brock review lessons from the Private AI Team cinematic site

When reviewing or briefing a PerformOS cinematic website, do not stop at “it looks premium.” Pressure-test scroll pacing, offer clarity, and buyer comprehension.

### What good looks like

- Hero names the category plainly: “private AI team,” not only “custom agents.”
- The buyer sees the value proposition before architecture: hours reclaimed, repeat work removed, team supported.
- The offer appears early: built, hosted, and maintained agents, up to ten where relevant, inside the client-approved environment.
- Use cases appear before technical stack: sales, recruitment, operations, executives, or the specific target functions for the buyer.
- Security claims are careful: say “designed to run inside your approved environment,” not absolute claims like “no data ever leaves your control” unless the deployment truly guarantees it.
- CTAs are specific: “Book a private AI team assessment,” not a generic “Book assessment.”
- Add CTA reassurance near the first button: what happens after the assessment, for example a scoped pilot plan, deployment option, expected workflow impact, and setup cost.

### Common fixes to ask Bob for

- Remove dead scroll space. A cinematic site can breathe, but every viewport should contain a visual, copy block, transition element, section marker, or scroll cue. Long flat black gaps feel broken.
- Tighten scroll pacing by 30 to 40 percent before adding more content.
- Add an early price anchor for cold business traffic, for example “Private AI teams from $4,999 AUD/month.” The full pricing block can remain later.
- Replace broad promises with function-specific value, for example removing repeat admin from sales, recruitment, operations, and executive workflows.
- Make guarantees precise: scope, refund target, exclusions, and timing.

## Asset path pitfall

Jared may refer to a folder as `AI website`, but the real local folder can contain typos or trailing spaces, for example:

```text
/Users/jc/Downloads/AI webiste /
```

Always use the real path discovered from the filesystem, not the corrected spelling in prose.

## Execution rule

Brock routes through Kanban. Bob builds. Brock does not build directly.
