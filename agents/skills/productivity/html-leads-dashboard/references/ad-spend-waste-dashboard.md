# Ad Spend Waste Dashboard Pattern

Use this reference when Jared asks for an agency-facing dashboard that finds businesses already advertising but leaking conversions through weak websites, weak offers, poor landing pages, review pain, or weak follow-up.

## Product promise

Find businesses with visible public signals that suggest they are paying for traffic but not converting enough of it.

Core question the dashboard must answer:

> Who should the agency contact today, why now, and what should they say?

## Best first MVP

Start with one niche and one location. Good first niches:

- Dentists
- Cosmetic clinics
- Solar installers
- Builders and renovation companies
- Gyms and fitness studios

Recommended first proof:

- Dentists or cosmetic clinics in Brisbane
- 25 to 50 businesses
- Static self-contained HTML dashboard first
- Clearly labelled demo data if live scraping credentials are not available
- No fake ad spend amounts

## Required dashboard sections

A strong Ad Spend Waste Dashboard should include:

1. **Executive hero framing**
   - who the tool is for
   - what it finds
   - what the agency should do next

2. **Opportunity Board**
   - prioritised business list
   - fit score
   - urgency score
   - why contact now
   - recommended next action

3. **Ad Signals**
   - Meta Ads Library signal
   - Google Ads Transparency signal
   - ad hook or visible offer
   - landing page URL where available
   - visible-signal wording only, not spend estimates

4. **Conversion Leaks**
   - weak headline
   - unclear CTA
   - weak booking path
   - poor mobile path
   - ad-to-page mismatch
   - missing proof or testimonials
   - contact friction

5. **Review Pain**
   - rating and review count where available
   - repeated complaint themes
   - repeated praise themes that can become copy
   - objection themes

6. **Outreach Studio**
   - suggested pitch angle
   - first email opener
   - first call opener
   - recommended buyer or persona
   - direct call, email, website, and LinkedIn buttons where available

7. **Data Pipeline / Connectors**
   - Apify
   - Google Maps scraper
   - Meta Ads Library scraper
   - Google Ads Transparency scraper
   - website crawler
   - review scraper
   - PageSpeed Insights
   - Apollo
   - Google Sheets
   - n8n

8. **Data schema preview**
   - sample JSON row or schema block so Jared can see how automation will feed the dashboard

## Lead scoring model

Use a transparent score out of 100. Suggested breakdown:

- Ad spend signal: 25
- Conversion leak: 30
- Contactability: 15
- Review pain: 15
- Commercial fit: 15

Optional urgency modifier can be shown separately or incorporated into fit.

Priority labels:

- Hot: 80 to 100
- Warm: 60 to 79
- Watch: 40 to 59
- Skip: below 40

Each lead should include sub-scores, not just a total score.

## Data quality rules

- Do not invent ad spend amounts.
- Do not imply live scraped data when using a demo dataset.
- Do not invent named contacts, phone numbers, or emails.
- Prefer public business contact details only.
- Every lead must include `why contact now`.
- Use wording such as `visible ad signal`, `active ads found`, or `public campaign signal` rather than claiming exact spend.
- Include this quality note in the dashboard: `Verify public contact details before outreach. Dashboard uses visible public signals, not guaranteed spend estimates.`

## Recommended automation workflow

1. Input niche and location.
2. Run Google Maps scraper.
3. Run Meta Ads Library scraper.
4. Run Google Ads Transparency scraper where available.
5. Merge by business name, domain, phone, and location.
6. De-duplicate.
7. Crawl each website or landing page.
8. Pull reviews.
9. Analyse conversion leaks and review pain.
10. Score each lead.
11. Generate pitch angle, email opener, and call opener.
12. Write rows to Google Sheets or JSON.
13. Refresh the HTML dashboard.
14. Notify Jared when complete.

## Recommended multi-agent workflow

For a high-standard build, avoid sending Bob a vague build task first. Use a fan-out then fan-in pattern:

1. Piper PromptOps creates scoring and prompt pack.
2. Nelly Notebook creates source and data pipeline blueprint.
3. Polly PerformOS creates agency-facing packaging and dashboard copy.
4. Bob Builder builds the final HTML artifact after those handoffs are complete.

This prevents Bob building a beautiful empty shell. The dashboard needs strategy, scoring, data logic, and product packaging before visual execution.

## Bob build acceptance criteria

The HTML artifact should include:

- Self-contained HTML/CSS/JS
- Premium original design, not generic SaaS filler
- Search, filters, priority filter, status filter, score sorting
- CSV export
- Mobile card view
- localStorage persistence for lead status and notes
- Lead detail panel or modal
- Direct actions for call, email, website, and LinkedIn where available
- Scoring breakdown out of 100
- Connector readiness section
- Sample data schema
- Keyboard and focus states
- Subtle motion with `prefers-reduced-motion`
- No em dashes in visible copy

Verification before final handoff:

- File exists at the promised path.
- Opens cleanly in browser.
- Console has no JavaScript errors.
- Search and filters change visible row count.
- Status and notes persist after refresh.
- CSV export button exists and triggers download where possible.
- Desktop layout has no obvious clipping.
- Mobile card CSS exists and works.
