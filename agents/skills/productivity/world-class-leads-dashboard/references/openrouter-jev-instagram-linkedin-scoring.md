# OpenRouter JEV pattern for Instagram to LinkedIn lead scoring

Use this when Jared wants to replicate the Instagram Reel style workflow where JEV scores content patterns and leads.

## Core sequence

Do **Instagram first**, then LinkedIn or Apollo.

Reason: Instagram produces the message library. LinkedIn or Apollo produces the people to score against that library. Starting with leads first creates generic outreach because there are no tested angles to match against.

Recommended loop:

```text
Instagram content intelligence -> message library -> LinkedIn/Apollo lead scoring -> outreach copy
```

## API path

Use OpenRouter's Decisions API, not TypeSafe direct, when Jared says he will use the OpenRouter JEV page.

```text
POST https://openrouter.ai/api/alpha/decisions
Authorization: Bearer $OPENROUTER_API_KEY
Content-Type: application/json
```

Model:

```json
"typesafe/jev-1.13"
```

Optional alias:

```json
"~typesafe/jev-latest"
```

Use the fixed model first for repeatability.

## JEV role boundary

JEV makes decisions only. Do not use it for prose generation.

Use JEV for:

- content format classification
- message angle selection
- hook strength scoring
- pain clarity scoring
- lead fit scoring
- best message angle per lead
- manual review flags

Use a generative model after JEV for:

- readable message library markdown
- LinkedIn connection request
- LinkedIn follow-up
- email subject and body
- call opener

## Instagram phase inputs

CSV fields:

| Field | Required | Notes |
|---|---:|---|
| post_url | Yes | Instagram Reel or post URL |
| creator | Yes | Account name |
| caption | Preferred | Full caption if available |
| transcript | Preferred | Reel transcript if available |
| on_screen_text | Preferred | Text shown in video |
| views | Optional | Weighting only |
| likes | Optional | Weighting only |
| comments | Optional | Weighting only |
| saves | Optional | Weighting only |
| post_date | Optional | Recency |

If transcript is missing, proceed with caption and on-screen text. Do not block the MVP.

## Instagram JEV questions

Useful question set:

- `content_format` as Choice: system_demo, case_study, how_to, contrarian_take, trend_commentary, offer_pitch, manual_review
- `primary_message_angle` as Choice: speed, cost_reduction, hidden_system, competitive_edge, simplicity, proof, authority, manual_review
- `hook_strength` as Score
- `pain_clarity` as Score
- `replicability` as Score
- `outbound_angle_value` as Score
- `save_to_message_library` as Noul
- `manual_review_needed` as Noul

Generate `message_library.md` and `message_library.json` after this phase.

## LinkedIn or Apollo phase

For MVP, do not scrape LinkedIn profiles directly. Use Apollo CSV or a manually prepared LinkedIn lead CSV.

Lead state should include:

- offer
- ICP
- `message_library` from Instagram phase
- lead row fields

Useful lead JEV questions:

- `industry_fit` as Score
- `buyer_seniority_fit` as Score
- `pain_signal_strength` as Score
- `best_message_angle` as Choice using the Instagram derived angles
- `ready_to_buy_signal` as Noul
- `should_contact` as Noul
- `manual_review_needed` as Noul

## Priority rule

JEV Score returns an index-like score across rubric levels. For five levels, normalise raw score from 0 to 4 into 0 to 1:

```python
def normalise_score(raw_score: float, level_count: int) -> float:
    if level_count <= 1:
        return 0.0
    return raw_score / (level_count - 1)
```

Example fit score:

```python
fit_score = round(100 * (
    0.25 * industry_fit_norm +
    0.20 * buyer_seniority_fit_norm +
    0.25 * pain_signal_strength_norm +
    0.15 * ready_to_buy_signal +
    0.15 * should_contact
))
```

Override rules:

- `manual_review_needed.noul >= 0.70` -> Manual Review
- `best_message_angle.choice == manual_review` -> Manual Review
- any major Score or Choice confidence below `0.55` -> low confidence flag
- `should_contact.noul < 0.45` -> cap at Nurture
- contactability under `35` -> cap at Nurture

## Build order for coding agents

When handing to Codex or SOL, instruct:

1. OpenRouter Decisions smoke test.
2. Five Instagram posts through JEV.
3. Generate `message_library.md` and `message_library.json`.
4. Five Apollo or LinkedIn leads through JEV using the message library.
5. Generate scored CSV, scored JSON, and data quality report.
6. Only then consider dashboard.

If Codex asks whether to summarize, review, or continue, choose: **Continue the project it describes.**

## Pitfalls

- Do not start with the dashboard.
- Do not start with leads before messages.
- Do not use JEV for generated copy.
- Do not scrape LinkedIn profiles directly for the MVP.
- Do not write `OPENROUTER_API_KEY` into files or logs.
- Do not hide manual review rows.
