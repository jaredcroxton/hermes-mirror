---
name: apify-google-maps-dashboard
description: Use when Jared asks for an Apify or Appify Google Maps dashboard, local lead dashboard, niche market scrape, business opportunity dashboard, or signal engine built from Google Maps plus website and enrichment data.
version: 1.0.0
author: Brock / Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [apify, google-maps, leads, dashboard, prospecting, local-business, enrichment, html]
    related_skills: [html-leads-dashboard, apollo-io, google-workspace, claude-design]
---

# Apify Google Maps Dashboard

**NOTE: For any new lead dashboard build, the master entry point is `world-class-leads-dashboard`. That skill handles intake, validation, enrichment, outreach templates, and Bob orchestration. This skill remains as the detailed reference for the Apify scrape-to-dashboard pipeline.**

Use this skill when Jared says any of these:

- "Apify Google Maps dashboard"
- "Appify Google Maps dashboard"
- "build a Google Maps lead dashboard"
- "scrape local businesses and turn it into a dashboard"
- "build a dashboard for businesses to get more leads"
- "make the Sunshine Coast education dashboard again for another niche"
- "find businesses with visible pain and a reason to contact them"

The purpose is not to scrape a list. The purpose is to build a practical lead signal engine.

Core question:

> Who should Jared contact first, why now, what evidence supports it, and what should he say?

## Before Building, Ask These Questions

Ask these before running Apify or building the dashboard unless Jared has already answered them in the thread.

1. **Who is the dashboard for?**
   - Jared's own PerformOS/AgentOS lead generation?
   - An agency client?
   - A specific business niche?

2. **What offer are we selling?**
   - Private AI agents
   - Lead generation
   - Website conversion improvement
   - Ads waste audit
   - SEO/local visibility
   - Training or consulting
   - Something else

3. **Which niche or industry should we target first?**
   - Example: RTOs, dentists, builders, gyms, accountants, clinics, real estate agencies, trades, hospitality venues.

4. **Which location or market should we scan?**
   - Example: Sunshine Coast, Brisbane, Gold Coast, Melbourne, Auckland, Singapore.

5. **How many leads should the first dashboard contain?**
   - Best first run: 25 to 50 businesses.
   - Use a smaller cap if Apify credits or enrichment cost matter.

6. **What makes a lead valuable for this offer?**
   - Admin complexity
   - Ad spend signal
   - Weak landing page
   - Poor reviews
   - Hiring growth
   - Compliance burden
   - High enquiry volume
   - Poor contact path
   - Visible conversion leakage

7. **What should count as evidence?**
   - Google Maps category, rating, review count
   - Website contact form or missing CTA
   - Course, booking, service, pricing, or policy pages
   - Meta Ads Library activity
   - Google Ads Transparency signal
   - Apollo company enrichment
   - LinkedIn company page
   - Hiring or careers page

8. **What should the dashboard output be?**
   - Local HTML only
   - HTML plus CSV and JSON
   - Google Sheets source of truth
   - n8n refresh workflow
   - Hosted dashboard later

9. **What should the first outreach angle be?**
   - Audit offer
   - Direct product pitch
   - Partnership pitch
   - Done-for-you service pitch
   - White-label dashboard for agencies

10. **Do you want me to run the real scrape now?**
   - Use this confirmation phrase with Jared: "If you want me to build it, say: lock it in."

## Default Build Decision

If Jared answers with a niche, location, and offer, default to:

```text
Apify Google Maps scrape -> public website crawl -> Apollo organisation enrichment where available -> local CSV/JSON -> self-contained HTML dashboard on Desktop
```

Do not block the first useful build on Google Sheets or n8n. Use those after the first local run proves commercial value.

## Cost-Controlled MVP Scope

Default first run:

- One niche
- One city or region
- 25 to 50 businesses
- Public company-level data only
- Business contact details only
- No invented named contacts
- Apollo enrichment capped to 30 domains unless Jared asks for more

If Apify returns too many results, cap per search term.

If Apollo is unavailable or the plan is limited, continue with company-level data and label Apollo as not enriched.

## Source Stack

Recommended sources:

1. **Apify Google Maps actor**
   - Actor used successfully: `compass/crawler-google-places`
   - API actor slug: `compass~crawler-google-places`
   - Use multiple search terms for the niche.
   - Include location in each search term.

2. **Public website crawl**
   - Crawl official website homepage and obvious contact/service pages.
   - Capture contact paths, forms, pricing, service pages, policy pages, careers pages, booking links, course links, and clear CTAs.

3. **Apollo organisation enrichment**
   - Use when a domain exists.
   - Capture employee estimate, industry, LinkedIn company URL, and technology names where available.
   - Do not invent named contacts unless Jared specifically asks for people enrichment.

4. **Optional ad and conversion signals**
   - Meta Ads Library scraper
   - Google Ads Transparency scraper
   - PageSpeed Insights
   - Google reviews scraper
   - Tech stack scraper
   - SERP scraper

## Apollo API Format (updated June 2026)

The old `GET /v1/organizations?domain=` endpoint returns 404. Use the POST enrich endpoint:

```python
req = urllib.request.Request(
    'https://api.apollo.io/api/v1/organizations/enrich',
    data=json.dumps({'domain': domain}).encode(),
    headers={
        'Content-Type': 'application/json',
        'x-api-key': key,
        'User-Agent': 'HermesApolloConnector/0.1',
    },
    method='POST',
)
```

## HTML Build Pattern — Large Inline JSON

When embedding lead data directly in HTML `<script>` tags, the file can exceed 40KB. Browsers may have issues loading large inline JS via `file://` protocol.

**Fix:** Serve via local HTTP server for verification:
```bash
cd /path/to/dashboard/folder && python3 -m http.server 9876
```
Then open `http://localhost:9876/filename.html` in browser.

The HTML file itself works fine — the issue is only with `file://` protocol on large files.

Load tokens from `/Users/jc/.hermes/.env` when available:

- `APIFY_TOKEN` or `REDACTED_APIFY_PREFIX_TOKEN`
- `APOLLO_API_KEY`

Never print token values.

For `compass~crawler-google-places`, the run may initially show `READY` even when `waitForFinish` is supplied. Do not treat `READY` as failure. Poll the actor run until a terminal status.

Terminal statuses:

- `SUCCEEDED`
- `FAILED`
- `ABORTED`
- `TIMED-OUT`

Fetch dataset items only after the run has a `defaultDatasetId`.

## Data Schema

Every dashboard row should include:

- rank
- business name
- category or type
- location
- website
- domain
- phone
- email or contact path
- Google rating
- Google review count
- Google Maps URL
- key evidence links
- enrichment status
- Apollo employee estimate
- Apollo industry
- LinkedIn company URL
- LinkedIn decision maker role
- LinkedIn decision maker search URL
- LinkedIn decision maker source
- signal scores
- total fit score out of 100
- priority band
- best use case or sales angle
- why contact now
- first call angle
- first email opener
- LinkedIn message template
- status
- notes

## LinkedIn Decision Maker Requirements

Every lead MUST have a clickable LinkedIn decision maker link. This is non-negotiable. If any of these fields are missing, the lead cannot be built into the dashboard until they are resolved.

### Required LinkedIn fields

1. **LinkedIn company URL** — the company page, e.g. `https://www.linkedin.com/company/company-name`
2. **LinkedIn decision maker role** — the inferred role, NOT a named person unless verified. Examples: "Operations Manager," "Training Coordinator," "Owner," "Principal," "HR Manager"
3. **LinkedIn decision maker search URL** — a clickable people search link. Format:
   ```
   https://www.linkedin.com/search/results/people/?keywords={role}%20{company}%20{location}
   ```
4. **LinkedIn decision maker source** — one of: `Apollo verified`, `Apollo inferred`, `Constructed from company data`, `Not found`

### Enrichment fallback for missing LinkedIn

If Apollo does not return a LinkedIn company URL, do NOT leave it blank. Build it:

1. Construct the LinkedIn company search URL:
   ```
   https://www.linkedin.com/search/results/companies/?keywords={company}%20{location}
   ```
2. Set LinkedIn company URL to the search URL above
3. Set LinkedIn decision maker source to `Constructed from company data`

If Apollo returns the company URL but no decision maker role:

1. Infer the most likely buyer role from the business type and offer
2. Construct a people search URL using company name + inferred role + location
3. Set LinkedIn decision maker source to `Apollo inferred`

### LinkedIn message template

Every lead must include a pre-drafted LinkedIn connection request or InMail message. This goes into the `linkedin_message_template` field.

**Connection request format (under 300 characters):**

```
Hi [Role First Name], I help [industry] businesses like [Company] with [specific pain point]. Not looking to pitch, just sharing a quick idea that might be relevant. Worth connecting?
```

**InMail format:**

```
Hi [Role First Name],

I noticed [Company] [specific evidence signal, e.g. "offers multiple training courses" or "has active job listings"]. I work with [industry] providers to [specific outcome, e.g. "reduce student enquiry response time" or "cut admin overhead on compliance docs"].

Would it be worth a quick 10-minute chat to see if there is a fit?

[Your name]
```

**Rules:**
- Never use a named contact unless verified from Apollo or the company website
- If the role is inferred, use the role title only, not a name
- Reference a specific evidence signal from the scrape
- Keep it short. No generic "I'd love to connect" filler

### Email template

Every lead must include a pre-drafted email in the `first_email_opener` field.

**Format:**

```
Subject: [Company] — [specific pain point] question

Hi [Role],

I noticed [Company] [specific evidence signal]. I help [industry] businesses [specific outcome] without adding headcount.

Worth a quick 10-minute chat this week?

[Your name]
```

**Rules:**
- Subject line must reference the company name and a specific pain point
- Body must reference at least one evidence signal from the scrape
- No generic templates. Every email must feel like it was written for that specific business
- If no email address exists, draft the email anyway and store it for manual send

## Scoring Model Template

Use a transparent 100-point model. Adapt the factors to the offer.

For private AI agent dashboards:

- Admin or operational complexity: 20
- Compliance or documentation burden: 20
- Enquiry or customer volume: 20
- Clear private-agent use case: 20
- Growth, hiring, or expansion signal: 10
- Contactability: 10

For ad or conversion dashboards:

- Verified or inferred ad activity: 20
- Website or conversion leak: 25
- Contactability: 15
- Review or reputation pain: 15
- Commercial fit: 15
- Urgency: 10

Priority bands:

- Hot: 85 to 100
- Warm: 70 to 84
- Nurture: 55 to 69
- Low: under 55

Caps:

- No clear contact path caps total score at 69.
- Missing `why_contact_now` caps priority at Warm.
- No clear use case caps private-agent fit at 69.
- Inferred ad evidence must be labelled as inferred, not verified.

## Dashboard Requirements

Create a self-contained HTML file on Desktop unless Jared asks for another format.

Must include:

- KPI cards with real counts only
- Lead table
- Search
- Priority filter
- Segment or category filter
- Status filter
- CSV export
- Clickable website, phone, email, maps, LinkedIn company, and LinkedIn decision-maker search actions where available
- Visible LinkedIn decision-maker role for each lead
- Clear label when the decision maker is an inferred target role rather than a verified named person
- Editable lead status
- Editable notes
- localStorage persistence
- Mobile card layout
- Clear data quality note
- "Why contact now" field visible in the lead detail view

Also write:

- CSV source file
- JSON source file
- pipeline notes markdown
- reusable build script

## File Pattern

Use a project folder on Desktop:

```text
/Users/jc/Desktop/<Market> <Niche> <Offer> Dashboard/
```

Recommended files:

```text
<Market> <Niche> <Offer> Dashboard.html
<slug>_leads.csv
<slug>_leads.json
pipeline-notes.md
build_dashboard.py
```

## Pre-Build Data Validation Gate

After enrichment and before the dashboard build, run a completeness check on every lead. Do NOT pass data to Bob until this gate is passed.

### Minimum fields every lead must have

Every row must contain ALL of the following or be flagged:

1. Business name
2. Website URL
3. Google Maps URL
4. LinkedIn company URL (or constructed search URL)
5. LinkedIn decision maker role (inferred is acceptable)
6. LinkedIn decision maker search URL
7. LinkedIn message template
8. First email opener
9. Phone OR email (at least one)
10. Location
11. Fit score
12. Why contact now
13. Priority band

### Data quality report

Generate a `data-quality-report.md` in the project folder alongside the CSV/JSON. Include:

```
## Data Quality Report

- Total leads scraped: X
- Leads after deduplication: X
- Leads with LinkedIn company URL (from Apollo): X
- Leads with LinkedIn company URL (constructed fallback): X
- Leads missing LinkedIn company URL: X
- Leads with LinkedIn decision maker role: X
- Leads with phone: X
- Leads with email: X
- Leads with both phone and email: X
- Leads missing both phone and email: X
- Leads with why_contact_now: X
- Leads with LinkedIn message template: X
- Leads with pre-drafted email: X
- Overall completeness: X%
- Apollo enrichment match rate: X%
- Apollo enrichment miss rate: X%

### Leads requiring manual review
[List any leads where critical fields could not be resolved]
```

### Completeness threshold

If overall completeness is below 80%, flag the build and list the gaps before proceeding. Do not ship a dashboard where more than 1 in 5 leads is missing core fields.

### Enrichment fallback sequence

When a lead is missing LinkedIn data, run this sequence in order:

1. Check Apollo enrichment output for LinkedIn company URL
2. If missing, search for "[Company name] LinkedIn" and construct a company search URL
3. Infer the decision maker role from business type and offer
4. Construct a LinkedIn people search URL using company name + inferred role + location
5. Set LinkedIn decision maker source to `Constructed from company data`
6. Draft a LinkedIn message template and email using available signals

If after all fallback steps a lead still has no LinkedIn data, include it in the data quality report under "Leads requiring manual review" and do not include it in the dashboard until resolved.

Before telling Jared it is done:

- [ ] HTML file exists.
- [ ] CSV and JSON exist.
- [ ] Pipeline notes exist.
- [ ] Dashboard opens in Google Chrome.
- [ ] Browser console has zero JavaScript errors.
- [ ] Row count in UI matches the data file.
- [ ] Search works.
- [ ] Filters work.
- [ ] CSV export button works.
- [ ] Status and notes persist with localStorage.
- [ ] Mobile card CSS exists.
- [ ] No fake metrics or invented contact details are present.
- [ ] Data source limitations are labelled.
- [ ] Every lead has a LinkedIn decision maker search URL.
- [ ] Every lead has a LinkedIn message template.
- [ ] Every lead has a pre-drafted email.
- [ ] Data quality report generated and reviewed.

## Best Dashboard Variants

Use this same logic for:

1. **Education AI Agent Opportunity Dashboard**
   - Finds RTOs, colleges, tutoring, training providers, and schools with admin, compliance, and student enquiry pressure.

2. **Ad Spend Waste Dashboard**
   - Finds businesses visibly advertising but leaking conversions through weak landing pages, poor CTAs, low trust, or bad reviews.

3. **Missed Booking Dashboard**
   - Finds service businesses losing bookings through hidden phone numbers, broken forms, slow pages, or no online booking.

4. **Local SEO Opportunity Dashboard**
   - Finds weak Google Business Profiles, poor categories, low review volume, and local ranking gaps.

5. **Review Pain Dashboard**
   - Finds businesses with low ratings, high complaint volume, or competitor reputation gaps.

6. **Competitor Conquest Dashboard**
   - Shows a business where local competitors are advertising, ranking, collecting reviews, and making stronger offers.

7. **Recruitment Leakage Dashboard**
   - Finds businesses with hiring activity, weak career pages, no follow-up automation, or poor candidate conversion.

8. **Private Agent Readiness Dashboard**
   - Finds businesses with enough admin load, compliance, support volume, and documentation pressure to justify a private AI team.

## Final Response Pattern

Keep Jared's final update short:

```text
Built.

File: /Users/jc/Desktop/<folder>/<dashboard>.html

Includes:
- X scored leads
- CSV and JSON
- real Google Maps data
- website crawl signals
- enrichment where available
- search, filters, notes, status, CSV export

Verified:
- opened in Chrome
- row count checked
- search/filter works
- CSV export works
- 0 JavaScript errors
```

## Common Pitfalls

1. **Building a pretty list instead of a signal engine.**
   - Fix: every row needs `why_contact_now` and a first outreach angle.

2. **Overbuilding before proof.**
   - Fix: local HTML, CSV, and JSON first. Google Sheets, n8n, and hosting come after proof.

3. **Treating Apify `READY` as failure.**
   - Fix: poll until terminal status and then fetch dataset items.

4. **Inventing contacts or evidence.**
   - Fix: label missing data clearly and use only public business data.

5. **Letting Apollo failure stop the build.**
   - Fix: Apollo is enrichment, not the source of truth.

6. **No buyer logic.**
   - Fix: ask what offer is being sold and score against that offer.

7. **No conversion action.**
   - Fix: include first call angle, first email opener, and the next best action.
