---
name: world-class-leads-dashboard
description: Master skill for building world-class lead dashboards. Use this as the single entry point for any lead dashboard request. Intake questions, data validation, enrichment, outreach templates, and Bob build orchestration all flow through this skill.
version: 1.0.0
author: Brock / Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [leads, dashboard, apollo, apify, google-maps, linkedin, firecrawl, claude-design, outbound, world-class]
    related_skills: [html-leads-dashboard, apify-google-maps-dashboard, apollo-io, claude-design]
---

# World Class Leads Dashboard

This is the master skill. Every lead dashboard request starts here. This skill handles:
1. Intake questions (get the brief right before anything else)
2. Source orchestration (Apify, Google Maps, Apollo, LinkedIn, Firecrawl)
3. Data validation gate (no incomplete leads ship)
4. Outreach templates (LinkedIn + email, pre-drafted per lead)
5. Bob build execution (design, responsiveness, verification)

Load this skill first. If the request is for one named brand, brand-specific outreach, Gmail drafts, calendar focus blocks, or individual LinkedIn decision-makers, switch to `branded-lead-dashboard` as the execution skill. Otherwise load `apify-google-maps-dashboard` for the scrape/enrich pipeline, then route to `html-leads-dashboard` for the final HTML build if needed.

Core question every dashboard must answer:

> Who should Jared contact first, why now, what evidence supports it, what should he say, and where can he reach them?

## PHASE ONE — Intake Questions

Ask these questions before anything else. Do not start a scrape, enrichment, or build until these are answered.

### The 15 Questions

**1. Who is the dashboard for?**
- Jared's own outbound prospecting?
- An agency client?
- A specific business or project?

**2. What brand or client website should be scraped for design tokens?**
- This is the FIRST research step. Extract colours, fonts, logo, spacing, personality from Firecrawl branding before anything else.
- If no brand website exists, describe the target aesthetic.

**3. What is the offer?**
- What exactly are you selling or pitching?
- Private AI agents, lead gen, ad audit, SEO, training, consulting, done-for-you service?
- Be specific. "AI stuff" is not an offer.

**4. What is the ideal buyer profile?**
- What type of business? (RTO, builder, agency, clinic, gym, accountant)
- What size? (solo operator, small team, mid-market, enterprise)
- What budget authority does the buyer have?

**5. Who is the decision maker?**
- What role title? (Owner, Operations Manager, HR Director, Principal)
- If you are not sure, describe the business type and infer the role.
- Named contacts only if verified. Otherwise label as inferred.

**6. What location or market?**
- City, region, country?
- Multiple markets? Start with one for the first build.

**7. Which niche or industry?**
- Be specific. "Healthcare" is too broad. "Dental clinics on the Sunshine Coast" is right.

**8. How many leads for the first build?**
- Default: 25 to 50.
- Cap for cost control on Apify credits or Apollo enrichment.

**9. What makes a lead valuable for this offer?**
- Admin complexity, ad spend, poor reviews, compliance burden, hiring growth?
- These become your scoring factors.

**10. What evidence signals should the scrape look for?**
- Google Maps rating and reviews
- Website paths: contact forms, missing CTAs, pricing pages, booking links
- Meta Ads Library activity
- Google Ads Transparency
- Hiring or careers pages
- Course or service pages
- LinkedIn company page
- Apollo enrichment data

**11. What outreach channels do you want?**
- LinkedIn (decision maker search + message template)
- Email (pre-drafted per lead)
- Phone (tel: link)
- All of the above (default)

**12. What should the dashboard output be?**
- Local HTML only (default)
- HTML plus CSV and JSON
- Google Sheets source of truth
- n8n refresh workflow
- Hosted later

**13. What is the first outreach angle?**
- Audit offer, direct pitch, partnership, white-label?

**14. What data quality standard do you want?**
- Standard: every lead has LinkedIn company URL (or constructed search URL), decision maker role, LinkedIn message template, email opener, phone or email
- High: every lead has verified named contact, direct email, direct phone, LinkedIn profile company URL
- Premium: all above plus Apollo employee estimate, ad signals, page speed score

**15. Ready to run the real scrape?**
- Use this confirmation phrase: "If you want me to build it, say: lock it in."

### Quick intake shortcut

If Jared gives a short brief, extract what you can and ask only what is missing. One or two clarifying questions maximum. Never ask all 15 if the answer is obvious from context.

---

## PHASE TWO — Research and Source Orchestration

Use this sequence regardless of dashboard type. Every step feeds the next.

### Step 1: Brand extraction (Firecrawl)

Before anything else:
```
firecrawl_scrape → formats: ["branding"]
```
Target: the client or Jared's brand website.
Save: colours, fonts, logo URL, border radius, spacing, component styles, personality.
Use: as design tokens for the HTML build. No generic dark-mode SaaS dashboards.

### Step 2: Google Maps scrape (Apify)

```
compass~crawler-google-places
```
- Use multiple search terms for the niche
- Include location in each search term
- Cap results per search term for cost control
- Poll until terminal status (SUCCEEDED, FAILED, ABORTED, TIMED-OUT)
- Fetch dataset items only after defaultDatasetId exists

### Step 3: Public website crawl (Firecrawl)

For each lead with a website URL:
- Crawl homepage, contact, service, pricing, policy, careers, booking pages
- Capture: contact paths, forms, CTAs, course links, hiring signals, compliance pages
- Use conservative timeout and normal user-agent

### Step 4: Apollo organisation enrichment

For each lead with a domain:
- **Use POST endpoint:** `https://api.apollo.io/api/v1/organizations/enrich` with `x-api-key` header
- **Do NOT use** `GET /v1/organizations?domain=` — returns 404 on current API versions
- Capture: employee estimate, industry, LinkedIn company URL, technology names
- Cap attempts for cost control (default: 30 domains)
- Do not invent named contacts unless specifically asked
- If Apollo is unavailable, continue with company-level data and label as not enriched

### Step 5: LinkedIn enrichment (mandatory)

Every lead MUST have LinkedIn data. This is non-negotiable.

**Priority order:**
1. Apollo enrichment returns LinkedIn company URL → use it
2. Apollo missing → construct LinkedIn company search URL:
   `https://www.linkedin.com/search/results/companies/?keywords={company}%20{location}`
3. Infer decision maker role from business type and offer
4. Construct LinkedIn people search URL:
   `https://www.linkedin.com/search/results/people/?keywords={role}%20{company}%20{location}`
5. Set source field: `Apollo verified`, `Apollo inferred`, or `Constructed from company data`

### Step 6: Optional signal enrichment

Add if relevant to the offer:
- Meta Ads Library scraper (ad spend signal)
- Google Ads Transparency scraper
- PageSpeed Insights (conversion leak signal)
- Google reviews scraper (reputation pain)
- Tech stack scraper
- SERP scraper (SEO opportunity)

---

## PHASE THREE — Pre-Build Data Validation Gate

Do NOT pass data to Bob until every lead passes this gate.

### Minimum fields every lead must have

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
11. Fit score (0 to 100)
12. Why contact now
13. Priority band (Hot, Warm, Nurture, Low)

### Data quality report

Generate `data-quality-report.md` in the project folder:

```
## Data Quality Report

- Total leads scraped: X
- Leads after deduplication: X
- Leads with LinkedIn company URL (Apollo): X
- Leads with LinkedIn company URL (constructed): X
- Leads missing LinkedIn company URL: X
- Leads with decision maker role: X
- Leads with phone: X
- Leads with email: X
- Leads with both phone and email: X
- Leads missing both phone and email: X
- Leads with why_contact_now: X
- Leads with LinkedIn message template: X
- Leads with pre-drafted email: X
- Overall completeness: X%
- Apollo match rate: X%
- Apollo miss rate: X%

### Leads requiring manual review
[Leads where critical fields could not be resolved]
```

### Completeness threshold

Below 80% overall completeness: flag the build, list the gaps, do not ship.
Above 80%: proceed to build.

### Target-fit threshold

Do not treat field completeness as data quality. A dashboard can have 100% LinkedIn coverage and still be commercially wrong if the leads do not match the buyer profile.

For lead dashboards with a defined size, geography, niche, or buyer profile:

- Calculate a `target_fit` field for every lead: `Strict fit`, `Close fit`, `Manual review`, `Below target`, or `Unknown`.
- Show the target-fit count in the dashboard KPI cards.
- Make target-fit filterable.
- If fewer than 70% of leads are strict or close fit, say the data set needs replacement before calling the dashboard final.
- Do not hide weak-fit leads inside a pretty interface. Flag them visibly.
- For employee-count targets, distinguish local site headcount from parent-company/global employee estimates where possible.

Pitfall: Jared will judge a leads dashboard by whether the leads are actually useful, not by whether every field is populated. If the dashboard “looks good” but half the leads are outside the target range, the build is not finished.

---

## PHASE FOUR — Outreach Templates

Every lead gets pre-drafted outreach. No exceptions.

### LinkedIn connection request (under 300 characters)

```
Hi [Role], I help [industry] businesses like [Company] with [specific pain point]. Not looking to pitch, just sharing a quick idea. Worth connecting?
```

### LinkedIn InMail

```
Hi [Role],

I noticed [Company] [evidence signal]. I work with [industry] providers to [specific outcome].

Worth a quick 10-minute chat to see if there is a fit?

[Name]
```

### Email

```
Subject: [Company] — [pain point] question

Hi [Role],

I noticed [Company] [evidence signal]. I help [industry] businesses [specific outcome] without adding headcount.

Worth a quick 10-minute chat this week?

[Name]
```

### Rules

- No named contacts unless verified from Apollo or the company website
- If role is inferred, use role title only
- Every message must reference at least one evidence signal from the scrape
- No generic templates. Every message must feel written for that specific business
- If no email address exists, draft the email anyway for manual send
- Subject lines must reference company name + specific pain point

---

## PHASE FIVE — Scoring Model

Transparent 100-point model. Adapt factors to the offer.

### Default factors (customise per build)

| Factor | Points |
|---|---|
| Direct fit with offer | 20 |
| Contactability (phone + email + LinkedIn) | 15 |
| Evidence signal strength | 15 |
| Geographic fit | 10 |
| Growth or hiring signal | 10 |
| Admin or operational complexity | 10 |
| Compliance or documentation burden | 10 |
| Clear use case alignment | 10 |

### Priority bands

| Band | Score |
|---|---|
| Hot | 85 to 100 |
| Warm | 70 to 84 |
| Nurture | 55 to 69 |
| Low | under 55 |

### Hard caps

- No clear contact path → cap at 69
- Missing `why_contact_now` → cap at Warm
- No clear use case → cap at 69
- Inferred evidence → label as inferred, not verified

---

## PHASE SIX — Bob Build Execution

Route to Bob Builder with the complete validated dataset. Bob owns the visual execution.

### What Bob must deliver

**Design (claude-design principles):**
- Premium, clean dashboard. No generic SaaS filler
- Brand-matched colours, fonts, logo, spacing from Firecrawl extraction
- Strong visual hierarchy
- Compact but readable table
- No clipping or overflow
- Dark or light system based on brand context

**Layout:**
- Desktop table view with all lead fields
- Mobile card view (fully responsive, touch-friendly)
- KPI cards at top with real counts only
- Lead detail view with all outreach actions

**Functionality:**
- Search across all lead fields
- Filters: priority, segment/category, status, and target fit where the brief has a defined ICP
- CSV export of currently visible rows
- Editable status per lead (dropdown)
- Editable notes per lead (text field)
- localStorage persistence for status and notes
- Clickable: website, tel, email (mailto with drafted subject/body), Google Maps, LinkedIn company, LinkedIn decision maker search
- LinkedIn message visible in lead detail (copy-ready)
- Email draft visible in lead detail (copy-ready)

**Executive usability:**
- Avoid a plain table as the primary experience for high-standard dashboards.
- Use a lead command-centre pattern: KPI cards, filter bar, ranked lead cards, and a right-side or modal lead detail panel.
- The detail panel should surface the decision maker path, why contact now, LinkedIn copy, email copy, call opener, and notes/status.
- Tables are acceptable as a secondary export/review mode, not the whole product experience.

**Data quality note on dashboard:**
- "Verify phone and email before high-volume outreach."
- "LinkedIn roles are inferred unless labelled verified."
- "Data sourced from public websites, Google Maps, Apollo enrichment, and LinkedIn search."

### File pattern

```
/Users/jc/Desktop/<Market> <Niche> <Offer> Dashboard/
  <Market> <Niche> <Offer> Dashboard.html
  <slug>_leads.csv
  <slug>_leads.json
  pipeline-notes.md
  data-quality-report.md
  build_dashboard.py
```

---

## PHASE SEVEN — Verification Checklist

Before telling Jared it is done:

- [ ] HTML file exists at stated path
- [ ] CSV and JSON exist
- [ ] Pipeline notes exist
- [ ] Data quality report exists
- [ ] Dashboard opens in Google Chrome
- [ ] Browser console has zero JavaScript errors
- [ ] Row count in UI matches data file
- [ ] Search works across all fields
- [ ] Filters work (priority, segment, status)
- [ ] CSV export button works
- [ ] Status and notes persist with localStorage
- [ ] Mobile card CSS renders correctly on phone-width
- [ ] No fake metrics or invented contact details
- [ ] Data source limitations are labelled
- [ ] Every lead has LinkedIn decision maker search URL
- [ ] Every lead has LinkedIn message template
- [ ] Every lead has pre-drafted email
- [ ] Brand colours and logo match the extracted tokens
- [ ] Overall completeness above 80%

### HTML Verification Tip

If the HTML file is large (40KB+) with inline JSON data, `file://` protocol may fail to execute JS. Serve locally instead:
```bash
cd /path/to/dashboard && python3 -m http.server 9876
```
Open `http://localhost:9876/filename.html` in Chrome and verify from there.

---

## Final Response Format

Keep it short:

```
Built.

File: /Users/jc/Desktop/<folder>/<dashboard>.html

Includes:
- X scored leads (X Hot, X Warm, X Nurture)
- CSV + JSON source files
- Google Maps data + website crawl signals
- Apollo enrichment (X% match rate)
- LinkedIn decision maker links on every lead
- Pre-drafted LinkedIn + email outreach per lead
- Search, filters, status, notes, CSV export
- Mobile responsive

Data quality: X% complete
LinkedIn coverage: X% (X Apollo, X constructed)

Verified: opens in Chrome, search/filter works, 0 console errors.
```

---

## Common Pitfalls

1. **Building a pretty list instead of a signal engine.** Every row needs `why_contact_now` and a first outreach angle.
2. **Letting missing LinkedIn slide.** Every lead gets a LinkedIn decision maker link. No exceptions.
3. **Generic outreach templates.** Every message must reference a specific evidence signal.
4. **Overbuilding before proof.** Local HTML, CSV, JSON first. Sheets, n8n, hosting come after.
5. **Treating Apify READY as failure.** Poll until terminal status.
6. **Letting Apollo failure stop the build.** Apollo is enrichment, not the source of truth.
7. **No brand extraction.** Always run Firecrawl branding before the build.
8. **Skipping the validation gate.** No data goes to Bob until completeness is above 80%.
