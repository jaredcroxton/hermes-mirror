# Lead Dashboard V2 Depth Standard

When building or reviewing a Crew lead dashboard skill, the bar is the Accor Plus Outreach Dashboard (live at https://accor-plus-leads-dashboard.vercel.app/). A passing lead dashboard skill must produce cards with full intelligence, not thin company rows.

## V1 failure mode (what to reject)

A V1 lead dashboard skill that produces cards where every row says "LinkedIn research not enabled" is REJECTED. This means the skill treated LinkedIn as a gated permission rather than the default research path. The result is a company list, not an intelligence dashboard.

## V2 depth signals (all 8 required)

1. **Fit scoring (0-100 per lead).** Five weighted dimensions: size (25), seniority (20), signal (25), industry (20), timing (10). Buckets: Hot 80-100, Warm 50-79, Cool 0-49. Score shown as a badge on every card with sub-score breakdown.

2. **LinkedIn research runs by default.** The skill finds real decision-maker names, profiles, and personalisation signals automatically. No permission gate. Confirmation moves downstream to email drafting and calendar, not to research.

3. **Decision-maker lookup with two backup rules.** Primary: named DM by role from LinkedIn. Backup 1: role-target placeholder if no name found ("Head of Ops, name to verify"). Backup 2: company-level only if LinkedIn is genuinely unavailable. Contact tagged Confirmed or Derived.

4. **Personalised insight per lead.** One sentence connecting the decision-maker's world to the offer. References something specific about the person or company. If the signal is thin, the insight is ESCALATED rather than fabricated.

5. **Dual-channel outreach.** Cold email AND LinkedIn DM drafted per lead. Different rules per channel. DM is shorter (~50 words), conversational, no link. Both follow the cold email methodology: Observation/Problem/Proof/Ask, 2-4 word lowercase subjects, no AI-slop openings.

6. **Four-colour evidence tags on every field.** Confirmed (sourced and cited), Inferred (reasoned from context), Derived (computed or looked-up), Escalated (thin signal, verify before use).

7. **Dashboard filters.** Region, quality score, and outreach status filters that show/hide cards client-side. Sticky top bar. Status badges per card. Expandable outreach panels.

8. **Calendar offer, never auto-create.** After the dashboard builds, the skill asks if the user wants focus blocks for outreach. If yes, blocks are proposed and confirmed individually. Never auto-created.

## The V2 rebuild pattern

When a V1 lead dashboard skill fails the depth standard, rebuild it from scratch (not patched). Same folder, same name. Full depth. Fresh 3-case fixture.

The rebuild adds: fit scoring step, LinkedIn-by-default research, personalised insight generation, dual-channel outreach, evidence tagging on every field, escalation for thin data, dashboard filters, and calendar offer.

## Test verification

A V2 test run must show:
- Fit scores 0-100 with sub-scores per lead
- Decision-makers found (not "LinkedIn research not enabled" on every row)
- Per-lead personalised insight
- Cold email + LinkedIn DM per card
- Working filter controls
- Evidence tags visible
- Thin-signal leads correctly escalated (coral badge)
- No fabricated people, no auto-sent emails, no auto-created calendar events
