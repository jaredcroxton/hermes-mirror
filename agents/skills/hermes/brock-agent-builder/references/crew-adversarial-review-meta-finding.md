# CREW Adversarial Review — The Recurring Meta-Finding

Across 93 gold-standard skill upgrades, the adversarial review process has revealed a consistent pattern. This is not a one-off. It is structural.

## The meta-finding

**Every skill's worked example violates its own rules.** The example that the skill presents as canonical output (the one a builder copies, the one the fixture enshrines as correct) consistently breaks one or more of the skill's own guardrails. When the fixture records that example as the expected correct answer, the wrong lesson gets baked in permanently.

## Examples across packs

- **Lottie:** The worked example showed a baked-in number counter in the Lottie asset, violating the "Lottie renders an asset, cannot author one" rule. The fixture was about to enshrine a counter rendering the wrong number.
- **Coaching-conversation-guide:** The worked example asked "Walk me through the last task you could have handed off but kept" — presupposing the manager's verdict as the coachee's admitted fact, the exact shame-move the skill bans.
- **Process-map:** The worked example's top fix "pre-provision the license" relocated the single-approver constraint instead of relieving it, while claiming to relieve it. The fixture enshrined the wrong fix as correct.
- **Policy-summary:** The worked employee guide stated no carryover beyond 5 days as a settled rule while the Flagged section flagged carryover as ambiguous — the example both resolved and flagged the same question.

## Why it happens

1. The worked example is written by the author (pre-review), not the reviewer
2. The author is focused on demonstrating the output format, not validating the content against guardrails
3. The fixture copies the example verbatim, creating a closed loop
4. The most-copied artifact is the most error-prone

## The fix applied across all upgrades

1. The adversarial review always checks the worked example against the skill's own guardrails
2. When the example violates a rule, both the example AND the fixture are fixed
3. The fixture's EXPECT block must test for the rule violation, not just the output format

## Rule for future skill builders

Before considering a skill complete, read the worked example and ask: "Does this example violate any of the skill's own rules?" If yes, the example is wrong, not the rule. Fix the example, then fix the fixture to assert the corrected behavior.
