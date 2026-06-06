---
name: html-leads-dashboard
description: Build self-contained HTML dashboards for outbound lead lists, prospecting targets, and local business development workflows.
version: 1.0.0
author: Brock / Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [html, dashboard, leads, prospecting, outbound, crm, sales, local-business]
    related_skills: [claude-design, apollo-io, google-workspace]
---

# HTML Leads Dashboard

**NOTE: For any new lead dashboard build, the master entry point is `world-class-leads-dashboard`. If Jared wants a brand-specific lead dashboard with individual LinkedIn decision-makers, source freshness, Gmail drafts, calendar focus blocks, or Accor Plus style replication, use `branded-lead-dashboard`. This skill remains as a reference for dashboard-specific design rules and build patterns.**

Use this skill when Jared asks for an HTML lead dashboard, prospecting dashboard, target-account list, local business contact dashboard, outbound tracker, mini CRM, or contact-priority tool.

The output should be a usable working dashboard, not a static list.

## Default outcome

Create a single self-contained `.html` file on Jared's Desktop that can be opened directly in a browser.

Default file pattern:

```text
/Users/jc/Desktop/<Client or Offer> <Market or Segment> Leads Dashboard.html
```

## Delivery clarification

For Jared's local HTML dashboard builds, default delivery is the Desktop HTML file opened in Google Chrome for review. Do **not** upload to Google Drive unless Jared explicitly says Google Drive. If Jared says "Google Chrome" or corrects "Drive" to "Chrome", update the build/review instruction immediately: local file, open in Chrome, browser/console verification, no Drive action.

## How to ask Jared for this

One sentence is enough:

> "Build me a leads dashboard for [client/offer]. [Number] leads. [Target]. No emails, no calendar. Bob builds it."

Three sentences gives better context:

> "Build me a leads dashboard for HumanX HR's L&D consulting. 5 leads. Australian decision-makers at mid-market companies. Bob builds it."

The key ingredients to include:
- **Client or offer** — who this is for
- **Lead count** — 5 is a good number
- **Target** — decision-maker role, company type, market
- **Mandatory fields** — ask what fields must be consistent across every lead before build, especially LinkedIn, phone, email, website, decision-maker role, source note, and `why_contact_now`
- **Who builds** — "Bob builds it" routes to Bob Builder

Before building, turn ambiguous field expectations into a short intake checklist. If Jared flags inconsistent data across prior dashboards, ask or infer the required fields and make them explicit in the build brief. Missing LinkedIn should never drift silently: either include the verified LinkedIn URL, include an inferred LinkedIn search link, or label it `LinkedIn not found` consistently across every lead.

You do not need a long brief. Brock fills in the research strategy, brand extraction, and feature requirements from this skill. The shorter the ask, the faster the dashboard lands on Desktop.

## Build orchestration rule

When Jared asks for a high-standard dashboard and names Bob's dashboard/design skills, do not over-gate the build behind every upstream specialist lane. Bob owns dashboard execution. Strategy, scoring, research, and product-positioning agents can sharpen the artifact, but they should not become a permission gate unless the dashboard genuinely cannot be built without their output.

Fast-start pattern:

1. Start Bob once the core dashboard shape is clear.
2. Pass any completed scoring or schema handoff into Bob immediately.
3. Let later research or positioning handoffs become version two improvements.
4. Avoid committee-style dependencies that delay a working artifact.

See `references/ad-spend-waste-dashboard-orchestration.md` for the Ad Spend Waste Dashboard pattern and scoring model.

## Mandatory data contract before build

Before Bob builds any lead dashboard, the brief must declare the required fields. These fields are not optional unless Jared explicitly says to leave them out:

- company name
- segment or category
- location / market
- public website
- phone, or `No phone found`
- email, or `No email found`
- LinkedIn company URL, or `No LinkedIn found`
- likely decision-maker role
- LinkedIn people-search URL for that role
- source note for every lead
- data confidence: high, medium, or low
- last checked date
- next best action

If LinkedIn is missing, the dashboard must show it as a visible data gap. Do not silently omit the LinkedIn field, button, or column. The build is incomplete if LinkedIn appears for some leads but the field itself is absent from others.

## Required dashboard features

Every leads dashboard should include:

1. **Clear commercial framing**
   - who the dashboard is for
   - who the leads are
   - what action the user should take next

2. **Prioritised lead list**
   - company / prospect name
   - segment or category
   - location / market
   - public website
   - phone and email where available
   - lead priority
   - fit score
   - tailored sales angle
   - source note

3. **Useful controls**
   - search
   - filters for segment and priority
   - status filter
   - CSV export

4. **Outbound workflow support**
   - call script
   - email opener
   - best target roles or routing ask
   - practical first action

5. **Light CRM behaviour**
   - editable status per lead
   - note field per lead
   - `localStorage` persistence for statuses and notes

6. **Direct actions**
   - `tel:` links for phone numbers
   - `mailto:` links with drafted subject/body when email exists
   - website open buttons
   - LinkedIn company profile links — every lead with a known LinkedIn URL must include a clickable LinkedIn company button in both table and mobile card views.
   - LinkedIn decision-maker action — every lead must show the likely decision-maker role and a clickable LinkedIn people-search link. If a named contact is not verified, label it as an inferred target role, not a named person.

7. **Responsive view**
   - desktop table
   - mobile card view

## Research workflow

When source data is needed, gather enough public data to make the dashboard useful, but do not overbuild a full enrichment pipeline unless asked.

Recommended sequence:

1. **Extract the client's brand FIRST.** Use Firecrawl branding extraction (`firecrawl_scrape` with `formats: ["branding"]`) on the client's homepage. Get exact colours, fonts, logo URL, border radius, component styles, and personality. This prevents generic dark-mode SaaS dashboards being built for brands that are light-mode, warm, and human-centric. Save this as your design token file before writing any HTML.
2. Search public web sources for target companies in the requested market.
3. Pull official company website URLs first.
4. Visit public company pages to extract visible phone/email where practical.
5. Remove directories, marketplaces, and generic listicles from the final dashboard unless they are being used only as discovery sources.
6. Score leads based on commercial fit, not just search rank.
7. Add a source note that contact details were gathered from public websites and should be spot-checked before bulk outreach.

If Apollo.io is available and the user wants named contacts or enrichment, load `apollo-io`. If the task only needs public company-level leads, Apollo is optional.

## Design rules

Use `claude-design` principles when building the interface:

- premium, clean dashboard
- no fake metrics
- no generic SaaS filler
- dark or light system based on the client context
- strong hierarchy
- compact but readable table
- no clipping or overflow
- mobile-friendly cards

Avoid decorative complexity. The dashboard exists to help the user call, email, filter, and export.

### High-standard lead dashboard pattern

When Jared says the dashboard "isn't what it was", "still isn't what it was", or flags that the build quality has dropped, do not defend the current artifact. Rebuild the interaction model.

Default upgrade pattern:

1. Replace the plain full-width table with a lead command centre.
2. Put KPI cards and data-quality flags at the top.
3. Use ranked lead cards as the primary list.
4. Add a right-side lead detail panel or modal with the full outreach pack.
5. Keep CSV export and filters, but make the first screen answer: who should I contact first, why, and what do I say?
6. Add visible risk flags for weak target fit, not just missing data.

A technically correct table is not enough for Jared's “world-class dashboard” standard.

**Critical: match the client's brand, not a default theme.** If the client uses light mode, coral accents, and navy headers, do not ship a dark-mode purple-accent SaaS dashboard. Brand accuracy is more important than looking "dashboard-like."

### Post-build brand review

After the HTML is built, compare it against the extracted brand tokens:

- [ ] Colours match the client's actual brand, not a generic dark/light theme
- [ ] Client's logo is in the header (use the CDN URL from Firecrawl branding extraction)
- [ ] Font matches or has a reasonable CDN substitute (see `popular-web-designs` font substitution table)
- [ ] Border radius, spacing, and component style feel like the client's site
- [ ] Tone matches the brand personality

If any of these fail, rebuild with the brand tokens applied. A dashboard built in the wrong brand is wrong, even if every feature works.

## Lead scoring guidance

Use a simple transparent score from 0 to 100.

Suggested scoring factors:

- volume or likely number of opportunities
- direct fit with the offer
- geographic fit
- ease of contact
- likely buying authority path
- partnership or repeat-work potential

Priority labels:

- **Hot:** high volume or high strategic fit
- **Warm:** good fit, likely useful after hot leads
- **Niche:** smaller, specialist, premium, or opportunistic target

## Contact data quality rules

- Prefer official company website contact details.
- Keep business contact details only.
- Do not invent named contacts.
- Do not invent phone numbers or emails.
- If no contact is found, show `No phone found` or `No email found`.
- If a scraped phone number looks malformed, clean it manually or omit it.
- Include a dashboard note: `Verify phone and email before high-volume outreach.`

## Verification checklist

Before final response:

- [ ] HTML file exists at the stated path.
- [ ] Browser opens the file cleanly.
- [ ] Console has no JavaScript errors.
- [ ] Search/filter changes visible row count correctly.
- [ ] CSV export button exists.
- [ ] Table has no obvious clipping at desktop width.
- [ ] Mobile card CSS is included.

## Final response format

Keep it short:

```text
Built.

File: /Users/jc/Desktop/<name>.html

Includes:
- X leads
- filters/search
- status and notes
- call/email actions
- CSV export

Verified: opens cleanly, search works, no console errors.
```

## Apify Google Maps Dashboard pattern

When Jared asks for an "Apify Google Maps dashboard", "Appify Google Maps dashboard", local niche scrape, or business opportunity dashboard, load `apify-google-maps-dashboard` before building or routing. That skill contains the intake questions, cost-controlled Apify plus website crawl plus Apollo workflow, scoring model, artifact requirements, and verification checklist.

## Education Agent Opportunity Dashboard pattern

When Jared asks for a lead dashboard to sell private AI agents, AgentOS, or PerformOS agent services to education, training, RTO, college, tutoring, or VET providers, use `references/education-agent-opportunity-dashboard.md` before building or routing.

Key rule: the dashboard must answer `Which providers should Jared call first, why now, and what private-agent use case should he lead with?` It is not enough to show provider names or generic AI-readiness scores.

Default real-data path: Apify Google Maps → public website crawl → Apollo organisation enrichment where available → local CSV/JSON → self-contained HTML dashboard. Do not block the first real build on Google Sheets or n8n if those services are not already authenticated and running.

## Ad Spend Waste Dashboard pattern

When Jared asks for an agency-facing dashboard to find businesses already advertising but leaking conversions, use `references/ad-spend-waste-dashboard.md` before building or routing.

When Jared asks how to make a demo/static dashboard real, use `references/real-leads-dashboard-pipeline.md`. The default first real stack is `Apify/MCP scrapers → n8n cleanup/scoring → Google Sheets source of truth → HTML dashboard`. Do not overbuild the backend first unless Jared explicitly asks for a hosted app.

Key rule: the dashboard must answer `Who should the agency contact today, why now, and what should they say?` It is not enough to show lead names or decorative metrics. The most important real-data field is `why_contact_now`; without it, the dashboard is just a list.

For high-standard builds, use a fan-out then fan-in workflow before Bob builds:

1. Piper PromptOps creates the scoring and prompt pack.
2. Nelly Notebook creates the source and data pipeline blueprint.
3. Polly PerformOS creates product packaging and agency-facing copy.
4. Bob Builder builds the final HTML artifact after those handoffs are complete.

This prevents a beautiful empty shell. The dashboard needs strategy, scoring, data logic, and product packaging before visual execution.

## References

- `references/alpha-air-brisbane-builders.md` — first dashboard pattern: Alpha Air targeting Brisbane/SEQ residential builders.
- `references/humanx-hr-brand-redesign.md` — brand extraction before build: how a generic dark-mode dashboard was rebuilt to match HumanX HR's actual navy/coral/light-mode brand identity.
- `references/ad-spend-waste-dashboard.md` — agency-facing dashboard pattern for finding visible ad spend signals, conversion leaks, review pain, outreach angles, scoring logic, connector readiness, and Bob build acceptance criteria.
