# Ad Spend Waste Dashboard orchestration pattern

Session learning: when Jared asks for a high-standard dashboard build and explicitly names Bob's design/dashboard skills, do not over-gate the build behind every upstream strategy/research lane.

## Product frame

Ad Spend Waste Dashboard promise:

> Find businesses already spending on ads, but leaking conversions through weak websites, weak offers, poor landing pages, review pain, or weak follow-up.

The dashboard must answer:

> Who should an agency contact today, why now, and what should they say?

## Recommended build sequence

1. Start Bob quickly once the core dashboard shape is known.
2. Use specialist inputs as enhancements, not blockers, unless the dashboard cannot be built without them.
3. If one upstream input finishes early, pass its summary into Bob immediately.
4. Let later research/positioning handoffs become version two improvements.
5. Avoid committee-style dependencies that delay the working artifact.

## When to parallelise

Good parallel lanes:

- Piper or prompt specialist: scoring rubric, row schema, AI analysis prompts.
- Nelly or synthesis specialist: source/data pipeline blueprint.
- Polly or product specialist: agency-facing offer, naming, positioning, pricing.
- Bob: dashboard artifact and visual interaction design.

## Key orchestration pitfall

Do not make Bob wait for every strategic input when Jared has asked to lock in the build. Bob already owns dashboard execution. The upstream agents should sharpen the build, not become a permission gate.

## MVP dashboard requirements

- Opportunity board
- Ad signals
- Conversion leaks
- Review pain
- Outreach studio
- Connector readiness
- Search and filters
- Priority/status filters
- Score sorting
- CSV export
- localStorage status and notes
- Lead detail panel
- Mobile card view

## Scoring model captured from Piper handoff

Total score: 100

Weights:

- Ad spend signal: 20
- Conversion leak: 25
- Contactability: 15
- Review pain: 15
- Commercial fit: 15
- Urgency: 10

Priority bands:

- Hot: 85 to 100 with why_contact_now and contactability >= 9
- Warm: 70 to 84
- Nurture: 55 to 69
- Low: 0 to 54

Caps:

- No contact path caps total at 69
- Missing why_contact_now caps priority at Warm
- Inferred ad evidence caps total at 84 until verified
- Missing website_url caps total at 54

Quality rules:

- No fake ad spend numbers
- No invented contacts
- Every lead needs why_contact_now
- Every non-null claim needs source URL or source note
- Active ad claims need observed_date and platform
- Direct evidence beats inference
- Unknown values stay null
- Review pain must be ethical and non-shaming
- Verify phone and email before high-volume outreach

## Connector set

Minimum viable:

- Apify
- Google Maps scraper
- Meta Ads Library scraper
- Website crawler
- Google Sheets or CSV
- n8n automation shell

Later:

- Google Ads Transparency scraper
- PageSpeed Insights
- Apollo enrichment
- Review scraper
- Email verifier
