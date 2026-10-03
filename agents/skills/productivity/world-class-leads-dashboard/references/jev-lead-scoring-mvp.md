# Jev-style lead scoring MVP

Use this when Jared sends a reel or example showing "Apollo + Claude + Jev" lead scoring, ranked prospects, or AI-selected outreach messages.

## What the system is

The useful workflow is not the reel hype. It is a scoring pipeline:

```text
Apollo leads -> CSV/table -> AI scoring rubric -> ranked lead list -> best outreach angle -> personalised LinkedIn/email copy -> dashboard/status tracking
```

Tools commonly claimed in these examples:

- Apollo: source leads and company/contact fields.
- Claude or GPT: reshape, enrich, draft messages, or add leads into a table/CRM.
- Jev: fast typed classification/scoring, useful for many cheap decisions at scale.
- CRM/table/dashboard: stores the ranked output and outreach state.

## CEO-level recommendation

Do not start with Jev, CRM integration, or n8n automation unless the ranked list has already proven value.

Recommended proof sequence:

1. Start with 50 to 100 Apollo leads, exported as CSV.
2. Define one offer and one ICP.
3. Define three to five outreach angles.
4. Score every lead against the rubric and every angle.
5. Generate the first LinkedIn message and email draft per lead.
6. Build a local HTML dashboard or CSV review output.
7. Only then consider Apollo API, Jev, n8n, Supabase, or CRM integration.

## Minimum scoring rubric

| Factor | Points |
|---|---:|
| Industry fit | 20 |
| Buyer seniority | 15 |
| Pain signal | 20 |
| Company size fit | 10 |
| Contactability | 15 |
| Urgency or timing signal | 10 |
| Message fit | 10 |
| **Total** | **100** |

Priority bands:

| Score | Priority |
|---:|---|
| 85 to 100 | Hot |
| 70 to 84 | Warm |
| 55 to 69 | Nurture |
| Under 55 | Low |

## Batch scoring prompt

```text
You are scoring B2B leads for this offer:

[PASTE OFFER]

Target customer:
[PASTE ICP]

Available outreach angles:
1. [ANGLE ONE]
2. [ANGLE TWO]
3. [ANGLE THREE]

Lead data:
[PASTE LEAD ROW]

Score this lead from 0 to 100 using this rubric:
- Industry fit: 0 to 20
- Buyer seniority: 0 to 15
- Pain signal: 0 to 20
- Company size fit: 0 to 10
- Contactability: 0 to 15
- Urgency or timing signal: 0 to 10
- Message fit: 0 to 10

Return JSON only:
{
  "fit_score": number,
  "priority": "Hot | Warm | Nurture | Low",
  "best_angle": "string",
  "why_now": "string",
  "personalised_opener": "string",
  "linkedin_message": "string",
  "email_subject": "string",
  "email_body": "string",
  "next_action": "string",
  "confidence": number
}
```

## When to use Jev

Jev is useful after the MVP works because it can answer typed scoring/classification questions quickly and cheaply. Treat it as a scale optimisation, not the starting point.

Use Jev-style classification for:

- yes/no fit checks
- lead priority scoring
- message-angle selection
- routing leads to sequences
- confidence/probability decisions

## Pitfalls

- Do not copy the reel's claim that scoring cost is the main value. The value is ICP clarity, offer clarity, and message quality.
- Do not overbuild n8n or CRM automation before validating whether the ranked leads are useful.
- Do not let a pretty dashboard hide weak lead fit. Target fit still matters more than completeness.
- Do not imply Jev is required. Claude/GPT can prove the workflow first.
