# Sales Pack — Testing Protocol

From the 26 June 2026 real-world test: PerformOS brand, Sunshine Coast wellness SMBs, 5 leads researched and briefed. The chain: lead-research → prospect-brief → outreach-draft.

## Test results

**Anti-fabrication held.** Dropped Coconut (UK, not Sunshine Coast). Refused the Joe Caldow Canada LinkedIn match (same name, different person). Every owner email marked "not found" instead of guessed. Labels enforced: Evidence vs Inference on every claim.

**Pattern surfaced.** "Always-open business, business-hours-only enquiry capture" — repeatable mechanism across the entire wellness segment, not a one-off observation.

**Escalation fired correctly.** KX Pilates flagged as franchise-compliance escalation. No outreach drafted to a lead needing corporate approval.

## Gaps exposed

1. **Owner name gap.** Two businesses had no public owner names. Skill correctly stops at "not found" but the chain needs LinkedIn/ABN enrichment. Future: crew-sales-lead-enrich skill or Apify LinkedIn integration.

2. **Dependency gap.** Skills reference crew-core-brand-context and crew-core-quality-checker but they're not installed as tools in the test session. Chain can't self-close. Distribution problem — plugins aren't built yet.

3. **Brand-context gate soft.** Skill says "run crew-core-brand-context when brand-context.md missing" but offers no fallback if that skill isn't installed. Solo-skill test can't satisfy it.

## Test protocol for sales chain

1. **Use real data.** Pick a real business, a real segment, a real geography. Fabrication defeats the purpose.
2. **Run the full chain.** Lead-research → prospect-brief → outreach-draft. Don't skip steps.
3. **Verify labels.** Every claim must carry Evidence or Inference. No unlabelled assertions.
4. **Verify anti-fabrication.** Did it refuse to invent emails, owner names, metrics? Did it drop irrelevant leads?
5. **Verify eligibility.** Did it screen do-not-contact, existing-customer, regulated-sector?
6. **Verify escalation.** Did it flag franchise/compliance/legal-sensitive leads?
7. **Verify handoffs.** Did each skill write its handoff so the next skill can read it?
