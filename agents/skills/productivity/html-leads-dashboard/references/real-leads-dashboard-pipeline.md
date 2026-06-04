# Real Leads Dashboard Pipeline

Use this reference when converting a demo/static HTML leads dashboard into a real lead-intelligence dashboard.

## Core principle

Do not frame the work as `scrape leads`. Frame it as building a signal engine:

> Find businesses with visible money, visible pain, and a clear reason to contact them today.

The dashboard should answer:

1. Who should be contacted today?
2. Why now?
3. What evidence supports that?
4. What should the first message say?

## Recommended first real stack

Start simple:

```text
Apify actors / MCP scrapers → n8n cleanup workflow → Google Sheets source of truth → HTML dashboard
```

Why this stack first:

- Google Sheets is easy for Jared to inspect and manually fix.
- n8n can normalise, dedupe, and score rows without a full app backend.
- The existing HTML artifact can read a CSV/JSON export before becoming a hosted app.
- This avoids overbuilding Supabase/Airtable/backend logic before the offer is proven.

Move to `Apify → n8n → Supabase/Airtable → hosted dashboard` only after the workflow proves commercial value.

## Signal sources

For an Ad Spend Waste or conversion-opportunity dashboard, useful source categories are:

| Signal | Likely source/tool | Use |
|---|---|---|
| Businesses in niche/location | Google Maps scraper | Base prospect universe |
| Meta ad activity | Meta Ads Library scraper | Visible ad-spend signal |
| Google ad activity | Google Ads Transparency scraper | Visible/inferred spend signal |
| Website quality | Website crawler | CTA, form, landing-page, trust, offer leaks |
| Page speed | PageSpeed Insights | Technical conversion drag |
| Reviews | Google reviews scraper | Reputation pain and competitor comparison |
| Contacts | Website scrape, contact page, Apollo | Contactability score |
| LinkedIn/company info | LinkedIn/company scrape or Apollo | Decision-maker and persona angle |
| Tech stack | BuiltWith/Wappalyzer-style scrape | CRM, CMS, tracking, ecommerce clues |
| Search visibility | SERP scraper | Competitor or SEO gap |

## First MVP scope

Do not connect every source at once. Build one narrow proof:

```text
One niche + one city + 25 to 50 businesses
```

Example:

```text
Brisbane dentists running ads with weak conversion pages
```

Minimum v1 pipeline:

1. Google Maps scrape for businesses.
2. Meta Ads Library signal where available.
3. Website crawl for CTA/form/offer/mobile issues.
4. Google review scrape for rating, volume, and complaint themes.
5. Public contact extraction from website/contact page.
6. Optional Apollo organization enrichment if the API plan allows it.
7. n8n normalises and dedupes.
8. Scoring logic assigns priority and caps.
9. Google Sheets stores the latest rows.
10. HTML dashboard reads the latest CSV/JSON export.

## Required real-data columns

A real dashboard should include evidence and action fields, not only lead names:

- business_name
- niche
- location
- website_url
- phone
- email_or_contact_page
- meta_ad_signal
- google_ad_signal
- ad_hook_or_offer
- landing_page_url
- conversion_leak
- website_issue
- review_rating
- review_count
- review_pain
- contactability_score
- commercial_fit_score
- urgency_score
- total_score
- priority_band
- why_contact_now
- evidence_links
- first_outreach_message
- status
- notes

`why_contact_now` is the commercial unlock. Without it, the output is just a list.

## Scoring reminder

Suggested total score: 100.

- Verified ad activity: 20
- Website/conversion leak: 25
- Contactability: 15
- Review/reputation pain: 15
- Commercial fit: 15
- Urgency: 10

Caps:

- No clear contact path caps total score at 69.
- Missing `why_contact_now` caps priority at Warm.
- Inferred ad evidence must be labelled as inferred, not verified.

## Dashboard/product variants

Once the pipeline works, clone the class for different commercial buyers:

1. **Ad Spend Waste Dashboard** — agencies find advertisers leaking conversions.
2. **Competitor Conquest Dashboard** — local businesses see competitor ads, reviews, rankings, and offers.
3. **Local SEO Opportunity Dashboard** — SEO agencies find weak Google Business Profiles and local ranking gaps.
4. **Missed Booking Dashboard** — service businesses find no booking, weak CTA, broken forms, hidden phone, or poor mobile flow.
5. **Review Pain Dashboard** — reputation agencies find weak review profiles and complaint themes.
6. **LinkedIn Buyer Intent Dashboard** — B2B sellers find hiring growth, new execs, expansion posts, and target personas.
7. **Website Conversion Leak Dashboard** — web/CRO agencies find weak CTA, form friction, poor trust, and slow pages.
8. **High Spend, Low Trust Dashboard** — agencies target visible advertisers with poor trust signals.

## Packaging language

For agencies, package as:

> Lead Leakage Intelligence Dashboard

Promise:

> Find businesses already trying to buy growth, then show where their leads are leaking.

Indicative pricing:

- One niche scan: $299 to $799 AUD.
- City/market dashboard: around $1,499 AUD.
- Monthly refreshed agency dashboard: $1,499 to $2,999 AUD/month.
- White-label agency version: setup plus monthly retainer.

## Build sequence for future agents

1. Confirm buyer: Jared's own lead generation or agency-facing product.
2. Choose one niche and location.
3. Build the source pipeline in n8n.
4. Store rows in Google Sheets first.
5. Add scoring and evidence fields.
6. Replace demo data in the HTML dashboard with exported real rows.
7. Verify row counts, filters, CSV export, and evidence labels.
8. Only then consider hosted backend, white-label theming, or recurring refresh.
