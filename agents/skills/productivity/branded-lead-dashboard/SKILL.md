---
name: branded-lead-dashboard
description: Use when building a branded lead-generation dashboard, lead list, outreach kit, ABM list, decision-maker list, cold-email batch, or Accor Plus style lead dashboard for a specific brand. Uses brand scrape, company-anchored LinkedIn individual-profile search, HarvestAPI profile verification, source dates, outreach copy, Gmail drafts, calendar focus blocks, and a motion-polished single-file HTML dashboard.
---

# Branded Lead Dashboard

## Locked Jared-approved format

This is Jared's approved branded lead-dashboard workflow. Do not rewrite, simplify, or substitute this format with a generic lead-dashboard process. If Hermes frontmatter validation requires a shorter description, shorten only the YAML `description` field and keep the body, workflow, behavioural rules, HarvestAPI sequence, LinkedIn rules, motion gate, and deliverable checklist intact.

Preserve this exact operating logic:
- Brand scrape first.
- Company-first, person-second.
- Only individual LinkedIn profile URLs containing `linkedin.com/in/`.
- HarvestAPI is the source of truth for decision-maker names.
- Source date and freshness are mandatory.
- Gmail drafts are self-addressed.
- Calendar focus blocks are included.
- Motion verification gate must pass before declaring done.

Approved backups live at `/Users/jc/Desktop/Obsidian/Agent Skill Backups/branded-lead-dashboard/` with SHA256 hashes in `LOCKED_MANIFEST.md`.

You are running an end-to-end lead-generation workflow that produces three artifacts: a branded HTML dashboard, a batch of Gmail drafts, and a week of calendar focus blocks. Everything ties back to one brand, one ICP, and one user.

## Intake (ALWAYS ask)

Even if the user has dropped a brand URL in the message, ask these out loud and confirm before you proceed. Brand intake matters more than any other step. If they only answered some, ask for the rest in a single short turn.

Jared has explicitly called out that lead dashboards drift when intake is inconsistent, especially around LinkedIn inclusion. Treat this intake as a data contract, not a courtesy question. Before any build starts, lock the lead-data fields and inclusion rules so dashboards do not vary from run to run. See `references/lead-data-contract-consistency.md` for the field-consistency rule and verification checklist.

1. Which brand is this for? Get the live website URL.
2. Product or service business? "Product" unlocks pricing language in the email body. "Service" unlocks the website-qualification step that surfaces a signal per target.
3. ICP: industry, region(s), decision-maker role, company size band.
4. Target company list (optional but strongly recommended). Ask: "Do you have a list of specific companies you want to target? If yes, paste them. If not, I will discover matching companies from your ICP." If the user provides companies, skip company discovery in Phase D and go straight to person search. Company-anchored searches produce far higher quality leads.
5. How many leads? Default 20.
6. Required lead fields for this run. Confirm explicitly: company, contact name, role, region, LinkedIn profile URL, source URL, source date, fit score, email status, outreach note, and qualification signal. If the user wants a field omitted, record that decision in memory/decisions.md.
7. LinkedIn rule for this run. Default is include individual LinkedIn URLs. Ask only if there is a reason to vary it: "Should every lead include an individual LinkedIn profile URL where available? Default yes." Do not allow some cards to show LinkedIn and others to silently omit it without a visible `not_found` or `not_applicable` status.
8. Data quality floor. Default: every named lead must have either a verified LinkedIn profile URL or a documented reason it is missing. Dashboard cards must show the status, not hide the field.
9. Your name + email sign-off: pulled from list_calendars primary if not provided, but ask to confirm spelling.
10. Output path: default ~/Desktop/leads/<brand-slug>/. Slug from brand name, lowercase, hyphenated.

Run the rest autonomously once intake is locked. Do not pause for confirmation gates between phases.

## Output structure

~/Desktop/leads/<brand-slug>/
├── CLAUDE.md                  (per-run constitution)
├── dashboard.html             (the deliverable, single file, open in browser)
├── data/
│   ├── brand.json             (colours, fonts, logo, tagline, socials)
│   ├── leads.json             (array of N lead rows)
│   └── focus.json             (5 calendar blocks for next week)
├── memory/
│   ├── progress.md            (done log + errors)
│   ├── findings.md            (per-lead source citations)
│   └── decisions.md           (architectural calls)
└── .tmp/                      (intermediate files, safe to delete)

## Workflow

### Phase L, Link

Scrape brand identity from the brand URL using Firecrawl:

firecrawl_scrape(
  url = <brand_url>,
  formats = ["branding", "markdown", "links"],
  onlyMainContent = false
)

Write data/brand.json per the shape in references/01_brand_extraction.md. Capture social URLs from the links array by filtering for known social domains.

Also call list_calendars once to capture the primary calendar id + timezone. Confirm these match the user's expectation.

### Phase D, Discover

#### Step D1: Build target company list (skip if user provided one)
If the user did not supply companies, run WebSearch to find companies matching the ICP:

"<industry>" companies "<region>" "<company size>" 2025 OR 2026
site:linkedin.com/company "<industry>" "<region>"

Collect 1.5x the lead count as candidate companies (e.g. 30 companies for 20 leads) to allow for misses. Log each company name + LinkedIn company URL in memory/findings.md.

#### Step D2: Find individual profiles at each company

For each target company, search for individual decision-makers. Critical rule: only keep URLs that contain linkedin.com/in/. Discard any URL containing linkedin.com/company/, linkedin.com/pub/, or any other LinkedIn path. If a search returns only company pages, run a refined pass before moving on.

Search passes per company (run in parallel across companies, 5-10 at a time):

- Pass 1: site:linkedin.com/in/ "<role>" "<company name>"
- Pass 2: site:linkedin.com/in/ "<company name>" "<role>" 2025 OR 2026
- Pass 3 (only if passes 1-2 yield no linkedin.com/in/ URLs): "<company name>" "<role>" linkedin profile

Collect all valid linkedin.com/in/ URLs. Deduplicate by URL before proceeding. One URL per unique person. If the same URL appears from multiple passes, keep it once.

#### Step D3: Scrape profiles with HarvestAPI

Batch all deduplicated linkedin.com/in/ URLs into the Apify actor:

call-actor(
  actorId = "harvestapi/linkedin-profile-scraper",
  input = {
    "profileUrls": ["https://www.linkedin.com/in/..."],
    "scrapeMode": "profile-details-no-email"
  }
)

From each scraped profile, capture:
- contact_name: full name from profile (never infer from URL)
- current_role: headline or most recent position title
- company: current employer from profile
- location: city + country
- linkedin_url: the canonical URL
- verified_date: ISO date of the actor run (e.g. 2026-05-15)
- tenure_years: approximate years in current role (use start date if available)

If HarvestAPI returns no data for a URL, mark contact_name: null and flag as stale. Do not fabricate any field.

#### Step D4: Compute fit score

For each scraped lead, assign fit_score (0-100) based on:

| Signal | Weight |
|---|---|
| Role matches ICP decision-maker title exactly | 40 |
| Company industry matches ICP | 25 |
| Region matches ICP target region | 20 |
| Tenure 1-4 years (established but not entrenched) | 10 |
| Profile is complete (has photo, headline, experience) | 5 |

Sort all leads by fit_score descending. Take the top N.

#### Step D5: Qualification signal (service brands only)

For service brands, Firecrawl-scrape each target company website to surface a qualification_signal. This signal becomes the email opener. Look for: outdated copyright year, missing service page matching what the brand sells, recent press or job posts signalling growth, tech stack signals.

#### Step D6: Email discovery via web lookup

For each lead with a verified contact_name and company, run a web lookup to find their email:

"<first name> <last name>" "<company>" email OR contact
"<first name> <last name>" "@<company domain>"

If web lookup finds a pattern but cannot confirm an address, set email_status: pattern_unverified and note the likely pattern (e.g. REDACTED_EMAIL). If lookup fails entirely, set email_status: not_found. Never guess an email address.

Log every source citation in memory/findings.md.

### Phase E, Enrich + Draft

For each lead, generate linkedin_message (<300 chars) and email_subject + email_body (120-180 words) per references/03_outreach_drafting.md.

Personalise using signals from the HarvestAPI profile data:
- Use the verified first name from the scraped profile. Use the literal {firstname} placeholder only if contact_name is null.
- Reference their current role and company by name.
- If tenure is short (<12 months), signal awareness of a fresh perspective or new priorities.
- If tenure is long (5+ years), signal stability and an established relationship to protect.

For service brands, lead the email with the qualification signal surfaced in D5 and skip pricing.
Write all leads to data/leads.json matching assets/leads.schema.json. Sort by fit_score descending. Assign sequential IDs L-01, L-02, etc. Include linkedin_url, verified_date, tenure_years, fit_score, and email_status on every row.

### Phase R, Render

Before rendering, read `references/07_dashboard_patterns.md`. That file is the locked-in visual + motion staples library (hero number, coach tip, scorecard cards, live widget, week timeline, filter pills) plus an expert library for gradients, animations, layouts, and data-viz to pull from on request. Every dashboard generated by this skill MUST ship with the six staples unless the user explicitly waives one.

Compute next-week focus blocks first:

python scripts/compute_next_week.py --timezone <user_timezone>

Build data/focus.json as an array of 5 entries:
{ "day": "Mon 18 May", "time": "09:00 to 10:30 AEST",
  "title": "<Brand> outreach: Block 1, leads L-01 to L-05 (Company A, B, C, D, E)" }

Render the dashboard:

python scripts/render_dashboard.py \
  --template /Users/jc/.claude/skills/branded-lead-dashboard/assets/dashboard.template.html \
  --brand    <project>/data/brand.json \
  --leads    <project>/data/leads.json \
  --focus    <project>/data/focus.json \
  --user-name "<user_name>" \
  --brand-url "<brand_url>" \
  --calendar-account "<calendar_id>" \
  --timezone "<timezone>" \
  --out      <project>/dashboard.html

The script enforces a 500KB cap. If it raises, prefer SVG URLs over base64 images, or remove decorative assets.

Open the result:

open <project>/dashboard.html

### Phase T, Trigger (Gmail + Calendar)

Gmail drafts per references/05_gmail_drafts.md. One draft per lead, self-addressed for safety:

mcp__gmail__create_draft(
  to = [user_email],
  subject = "[DRAFT L-01] {company}, {contact_role}",
  htmlBody = "<p><strong>Verify before send:</strong> {email_pattern} &middot; <a href='{linkedin_url}'>find on LinkedIn</a></p><hr>{rendered email body as HTML paragraphs}"
)

Run drafts in batches of 5 in parallel.

Calendar blocks per references/06_calendar_blocks.md. Five events:

- Mon-Thu next week: 09:00 to 10:30 local, 5 leads per block, colorId: "9"
- Friday next week: 09:00 to 10:00, review + follow-ups, colorId: "2"

Use list_calendars primary id + timezone.

## Preservation rule

This skill is Jared's locked-in branded lead-dashboard format. Before changing the workflow, read `references/exact-format-preservation.md`. Do not simplify it into a company-only enrichment dashboard. The decision-maker pipeline, `linkedin.com/in/` rule, HarvestAPI source-of-truth rule, source freshness, Gmail drafts, calendar blocks, and motion gate are all part of the standard.

## Behavioural rules

- No em dashes anywhere. Use commas, periods, or parentheses.
- When Jared flags inconsistency in lead-dashboard data, patch this lead-dashboard skill or its references only. Do not make broad permanent changes to unrelated design/build/reviewer skills unless Jared explicitly asks.
- Always ask which brand it is for. Do not assume from context.
- Company-first, person-second. Always anchor person search to a specific company. Broad person searches without a company anchor produce low-quality leads.
- LinkedIn individual profiles only. Only keep URLs containing linkedin.com/in/. Discard all linkedin.com/company/ and linkedin.com/pub/ URLs before passing to HarvestAPI.
- Deduplicate before scraping. Never send the same LinkedIn URL to HarvestAPI twice.
- HarvestAPI is the source of truth for names. Never infer a person's name from a URL slug or search snippet. If HarvestAPI returns no name, the field is null.
- Email lookup uses verified name only. Do not attempt email lookup for leads where contact_name is null.
- Source date matters. Every named lead has a verified_date from the HarvestAPI run. Without one, mark contact_name: null.
- Drafts are self-addressed. Never put an unverified email in the live to: field.
- Mark `email_status: pattern_unverified` until externally validated. The dashboard surfaces this with an amber badge.
- Single monolithic HTML file. Never componentise the dashboard.
- Soft delete only. Never hard delete production data.

## Memory writing

After each phase update:
- memory/progress.md with what happened, drafts saved (ids), calendar events created (ids).
- memory/findings.md with per-lead source citations + the search queries that surfaced them.
- memory/decisions.md with any judgement calls (which candidate name to pick when sources conflicted, currency inference, etc.).

## Motion verification gate (run before checklist)

Before the deliverable checklist, run this verification against the rendered dashboard.html and fix any failures inline:
# All five LearnOS staple keyframes must be present
grep -c '@keyframes kpiCountUp' dashboard.html    # must be 1
grep -c '@keyframes barFill' dashboard.html       # must be 1
grep -c '@keyframes livePulse' dashboard.html     # must be 1
grep -c '@keyframes sparkDraw' dashboard.html     # must be 1
grep -c '@keyframes staggerRise' dashboard.html   # must be 1

# Counter pulse must be APPLIED to each kpi number (not just declared)
grep -c 'animation: kpiCountUp' dashboard.html    # must be >= 1

# Card stagger must use per-card index variable
grep -c 'style="--i:' dashboard.html              # must equal lead count

# Reduced-motion media query must be present
grep -c 'prefers-reduced-motion: reduce' dashboard.html  # must be 1

If any check fails, edit dashboard.html directly to add the missing animation and re-verify. Do not declare the render phase done until all six checks pass.

When generating lead cards, the render script (or inline HTML) MUST emit each card with an index variable:

<article class="card" style="--i: 0">...</article>
<article class="card" style="--i: 1">...</article>
<article class="card" style="--i: 2">...</article>

This is what drives the per-card stagger animation. Without --i, all cards fade in at once and the entrance feels flat.

For richer motion (live status widget, week timeline with playhead, pillar bars on cards, sparkline on hero), read references/07_dashboard_patterns.md for the HTML snippets and apply them as additional widgets above the lead grid.

## Deliverable checklist before declaring done

- [ ] Lead data contract passes: every lead row has the same keys, every card renders LinkedIn URL or visible LinkedIn status, missing LinkedIn values are counted or explained, and no card silently omits a field shown on another card.
- [ ] dashboard.html renders, opens in browser, all features intact (hero, KPIs, search, region chips, count pill, card grid with stagger fade-in, drawer with copy buttons, focus blocks, footer, toast).
- [ ] Each card shows a freshness pill next to the name (fresh/aging/stale colouring).
- [ ] Hero and footer show the user's brand socials (only icons for socials present).
- [ ] Region chips reflect the actual regions in the leads, not a baked list.
- [ ] KPI numbers are computed (not hardcoded).
- [ ] Gmail drafts saved: count matches lead count, all subject-prefixed [DRAFT L-NN].
- [ ] Calendar: 5 events on next-week dates, primary calendar, correct timezone.
- [ ] memory/findings.md cites a source URL + date for every named lead.

## Failure modes

| Symptom | Cause | Fix |
|---|---|---|
| Firecrawl returns minimal HTML | JS-rendered site | Retry with waitFor: 5000. |
| Brand colours render illegibly | Both primary + bg are light | Swap primary with accent before render. |
| Logo URL 404s | Site changed CDN paths | Fall back to a 64x64 SVG wordmark with brand name + accent. |
| Render script raises >500KB | Inline base64 images in scraped logo | Use the original URL instead of base64, or strip decorative images. |
| Drafts not visible in Gmail | Gmail MCP not authed | Run list_labels to confirm auth; reauthorise if it errors. |
| LinkedIn searches return only company pages | Query too broad or role too generic | Add the person's full role title in quotes. Switch Pass 1 to: site:linkedin.com/in/ "<exact role title>" "<company>". |
| HarvestAPI returns empty profile | Profile is private or URL is a redirect | Discard that URL. Run another search pass for the same company to find an alternative person. |
| Fewer than N leads after deduplication | ICP is too narrow or company list is small | Expand company list by 50% or broaden role title to include variants (e.g. "Director of Marketing" OR "Marketing Director"). |
| Email lookup fails for most leads | Company uses obfuscated email format | Use HarvestAPI email mode as fallback: rerun the actor with "scrapeMode": "profile-details-and-email" for the leads where email_status: not_found. Note this costs more per run. |

## Notes on tool access

This skill assumes the following MCPs are available in the user's session: Firecrawl, Gmail, Google Calendar, WebSearch (built-in). Apify is mentioned only as a paid LinkedIn cookie fallback; do not invoke without explicit user consent.
