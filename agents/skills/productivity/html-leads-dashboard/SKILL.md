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

Use this skill when Jared asks for an HTML lead dashboard, prospecting dashboard, target-account list, local business contact dashboard, outbound tracker, mini CRM, or contact-priority tool.

The output should be a usable working dashboard, not a static list.

## Default outcome

Create a single self-contained `.html` file on Jared's Desktop that can be opened directly in a browser.

Default file pattern:

```text
/Users/jc/Desktop/<Client or Offer> <Market or Segment> Leads Dashboard.html
```

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

7. **Responsive view**
   - desktop table
   - mobile card view

## Research workflow

When source data is needed, gather enough public data to make the dashboard useful, but do not overbuild a full enrichment pipeline unless asked.

Recommended sequence:

1. Search public web sources for target companies in the requested market.
2. Pull official company website URLs first.
3. Visit public company pages to extract visible phone/email where practical.
4. Remove directories, marketplaces, and generic listicles from the final dashboard unless they are being used only as discovery sources.
5. Score leads based on commercial fit, not just search rank.
6. Add a source note that contact details were gathered from public websites and should be spot-checked before bulk outreach.

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

## References

- `references/alpha-air-brisbane-builders.md` captures the first dashboard pattern: Alpha Air targeting Brisbane/SEQ residential builders.
