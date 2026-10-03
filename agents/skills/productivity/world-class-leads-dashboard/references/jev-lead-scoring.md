# JEV Lead Scoring Reference

Use this when a lead dashboard or outbound system should rank leads using TypeSafe AI JEV rather than a generative LLM.

## Core pattern

JEV is for structured decisions, not prose.

Use JEV to decide:

- lead fit
- priority
- best outreach angle
- buying readiness signal
- whether manual review is needed

Use a generative model after JEV to write LinkedIn and email copy from the JEV decisions.

## Official docs

- Introduction: https://docs.typesafe.ai/introduction
- Quickstart: https://docs.typesafe.ai/introduction/quickstart
- Score: https://docs.typesafe.ai/primitives/score
- Choice: https://docs.typesafe.ai/primitives/choice
- Noul: https://docs.typesafe.ai/primitives/noul
- Python SDK: https://docs.typesafe.ai/sdk/python

## API basics

Endpoint:

```text
POST https://api.typesafe.ai/v1/systemone
Authorization: Bearer <API_KEY>
Content-Type: application/json
```

Model:

```json
"model": "jev-latest"
```

Environment variable:

```bash
TYPESAFE_API_KEY=<provided separately>
```

Never write the API key into markdown, source files, CSV, JSON, logs, or dashboards.

## JEV question types

| JEV type | Use in lead scoring | Returns |
|---|---|---|
| `Score` | Fit, pain strength, urgency, message fit | `score`, `probabilities`, `confidence`, `legend` |
| `Choice` | Best outreach angle, lead segment | `choice`, `probabilities`, `confidence` |
| `Noul` | Yes/no probability checks | `noul` from 0 to 1 |

## Recommended architecture

Start local and prove the scoring before adding automation.

Input:

- Apollo CSV export
- offer definition
- ideal customer profile
- outreach angles

Output:

- scored CSV
- scored JSON
- data quality report
- optional local HTML dashboard

Avoid n8n, CRM syncing, and automated sending in the first pass unless Jared explicitly asks. The first proof is whether the ranked list produces better targets.

## State design

Send one lead at a time. Prefer JSON object state over a plain string.

```json
{
  "offer": "I help small to mid-sized businesses find repeat manual work and replace it with practical AI agents, dashboards, and workflow automation without adding headcount.",
  "ideal_customer_profile": "Owner, founder, director, operations leader, sales leader, or HR leader in a small to mid-sized business with admin load, sales follow-up problems, recruiting or onboarding friction, customer support volume, manual reporting, or repeated internal processes that could be automated.",
  "lead": {
    "title": "Operations Manager",
    "company": "Example Co",
    "industry": "Professional Services",
    "location": "Brisbane, Australia",
    "employee_count": 42,
    "website": "https://example.com",
    "company_description": "Provides managed services to small businesses",
    "email": "available",
    "phone": "missing",
    "linkedin_url": "available"
  },
  "outreach_angles": {
    "admin_bottleneck": "Find repeat manual work and automate it",
    "sales_follow_up": "Improve speed and consistency of sales follow-up",
    "training_speed": "Reduce time to competency for new starters",
    "customer_support": "Reduce repeated customer support load",
    "dashboard_visibility": "Create a clear dashboard for operational decisions"
  }
}
```

## Standard questions

Ask these in one JEV request per lead:

```json
{
  "industry_fit": {
    "type": "score",
    "instructions": "How well does this company fit the offer and ideal customer profile based on industry and business model?",
    "criteria": [
      "Poor fit or irrelevant business type",
      "Possible fit but weak signal",
      "Good fit with a plausible operational use case",
      "Strong fit with clear operational complexity",
      "Excellent fit with obvious repeat manual work or AI automation need"
    ]
  },
  "buyer_seniority_fit": {
    "type": "score",
    "instructions": "How likely is the listed person to influence or decide on workflow automation, AI agents, dashboards, or operational improvement?",
    "criteria": [
      "Not a relevant buyer or influencer",
      "Low influence",
      "Possible influencer",
      "Strong influencer or manager",
      "Clear decision maker or budget owner"
    ]
  },
  "pain_signal_strength": {
    "type": "score",
    "instructions": "How strong is the evidence that this lead may have a real workflow, admin, sales, training, support, or reporting problem worth solving?",
    "criteria": [
      "No visible pain signal",
      "Weak inferred pain",
      "Moderate likely pain",
      "Strong likely pain",
      "Very strong and specific pain signal"
    ]
  },
  "timing_or_urgency": {
    "type": "score",
    "instructions": "How likely is this lead to have a reason to act soon based on role, company context, hiring, growth, visible activity, or operational complexity?",
    "criteria": [
      "No timing signal",
      "Weak timing signal",
      "Moderate timing signal",
      "Strong timing signal",
      "Very strong reason to act now"
    ]
  },
  "best_outreach_angle": {
    "type": "choice",
    "instructions": "Which outreach angle best fits this lead? Choose the strongest commercial angle, not the most generic one.",
    "criteria": {
      "admin_bottleneck": "The lead likely has repeat manual admin work that can be automated",
      "sales_follow_up": "The lead likely needs better lead handling, sales follow-up, or pipeline speed",
      "training_speed": "The lead likely hires, trains, or manages staff capability frequently",
      "customer_support": "The lead likely handles repeated support questions, tickets, or customer service load",
      "dashboard_visibility": "The lead likely needs better reporting or decision visibility",
      "manual_review": "There is not enough information to choose a confident angle"
    }
  },
  "ready_to_buy_signal": {
    "type": "noul",
    "instructions": "This lead shows signs that they may be ready to discuss workflow automation, AI agents, dashboards, or operational improvement in the near term."
  },
  "should_contact": {
    "type": "noul",
    "instructions": "This lead is worth contacting for the offer based on the available information."
  },
  "manual_review_needed": {
    "type": "noul",
    "instructions": "This lead has insufficient, conflicting, or weak data and should be reviewed manually before outreach."
  }
}
```

## Score conversion

JEV Score returns an index across the rubric levels. For five levels, raw score runs from 0 to 4.

```python
def normalise_score(raw_score: float, level_count: int) -> float:
    if level_count <= 1:
        return 0.0
    return raw_score / (level_count - 1)
```

Suggested fit score:

```python
fit_score = round(100 * (
    0.25 * industry_fit_norm +
    0.20 * buyer_seniority_fit_norm +
    0.25 * pain_signal_strength_norm +
    0.15 * timing_or_urgency_norm +
    0.10 * ready_to_buy_signal +
    0.05 * should_contact
))
```

Calculate contactability outside JEV as a visible field, not a hidden override.

```python
contactability = 0
if email: contactability += 40
if phone: contactability += 25
if linkedin_url or company_linkedin_url: contactability += 25
if website: contactability += 10
```

## Priority and gates

| Fit score | Priority |
|---:|---|
| 85 to 100 | Hot |
| 70 to 84 | Warm |
| 55 to 69 | Nurture |
| Under 55 | Low |

Override rules:

- If `manual_review_needed.noul >= 0.70`, set priority to `Manual Review`.
- If `best_outreach_angle.choice == manual_review`, set priority to `Manual Review`.
- If any major Score confidence is below `0.55`, set `confidence_flag = low_confidence`.
- If `should_contact.noul < 0.45`, cap priority at `Nurture`.
- If contactability is under `35`, cap priority at `Nurture`.

## Pitfalls

- Do not use JEV to write outbound copy. Use it to choose the angle and score the lead, then call a generative model for copy.
- Do not add n8n or CRM automation before the scored CSV has proved value.
- Do not let a pretty dashboard hide weak-fit leads. Manual Review must be visible.
- Do not treat contactability as part of semantic fit. Show it separately.
- Do not ignore low confidence distributions. Confidence gates are part of the system.
