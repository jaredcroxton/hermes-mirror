# Lead Dashboard Depth Standard

The Accor Plus Outreach Dashboard (https://accor-plus-leads-dashboard.vercel.app/) sets the bar for what a Crew-level lead dashboard must produce. Any `crew-web-lead-dashboard-builder` skill must match or exceed this depth.

## What the standard requires

### 1. Fit scoring (mandatory)
Every lead gets a 0-100 fit score based on:
- Staff size match (50-500 is the mid-market sweet spot)
- Decision-maker seniority (CPO, Head of People, VP — not generic HR)
- Pain signal strength (hiring, funding, news, job listings)
- Industry relevance to the offer

Hot leads flagged at 90+. Filter control: "Hot only (90+)"

### 2. LinkedIn research as default path (mandatory)

LinkedIn research runs by default. No permission gate. No discovery question asking whether LinkedIn is permitted. It just runs.

The confirmation gates move downstream:
- Emails and LinkedIn DMs are still drafted but never sent without human review. The "verify before send" tag still applies to every derived email and contact.
- The calendar question still asks before creating anything. Never auto-create calendar events.
- The skill is a research and drafting tool, not an auto-send tool.

When LinkedIn is on (default), every lead card must include:
- Decision-maker name (verified, not guessed)
- Actual title
- LinkedIn profile URL
- Verification date (month and year)

### 3. Derived email (mandatory)
Pattern-match email from company domain and contact name. Always tagged "verify before send." Never presented as confirmed. Format: firstname.lastname@company.com or the most common pattern for that company.

### 4. Personalised insight per lead (mandatory)
One specific sentence that connects the decision-maker's world to the offer. This is the hardest part and the most valuable. Not "Company X is in Y industry." Write: "CPO signs off benefits directly — one fast conversation. Travel-and-dining perk helps compete against larger tech employers." The insight must name the mechanism, not the category.

### 5. LinkedIn DM drafted alongside email (mandatory)
Different medium, different rules. Shorter than email. Even more peer-level. Often just the personalised observation and a question. The Accor Plus dashboard produces both per lead.

### 6. Cold email with personalisation signal (mandatory)
The email must use the personalised insight. If the insight is thin, the email is thin. No generic templates with {{FirstName}} swapped in. Follow the cold email methodology: Observation/Problem/Proof/Ask, 2-4 word lowercase subject, one low-friction CTA, no banned openings.

### 7. Calendar integration (mandatory question)
After the dashboard builds, ask: "Do you want me to block focus sessions for outreach next week?" If yes, suggest time blocks and let the user confirm. The Accor Plus dashboard shows "Focus Blocks: 5 (next week)."

### 8. Filter controls in the dashboard HTML (mandatory)
- Region filter (All, plus individual regions)
- Quality toggle (Hot only, 90+)
- Outreach status filter

### 9. Staff sizing with estimates (mandatory)
Mid-market 50-500 staff. Estimated per company, tagged as estimate. Never presented as confirmed unless the scrape source states it explicitly.

### 10. Dashboard metrics row (mandatory)
At the top of the page: Total Leads, Hot Leads, Regions Covered, Focus Blocks. Four cards. Visually immediate.

## What the Crew skill must never do

- Produce thin cards with no decision-maker name and "LinkedIn research not enabled" on every row
- Skip fit scoring
- Treat LinkedIn as off by default
- Omit derived emails
- Omit LinkedIn DMs
- Omit personalised insights
- Omit filter controls
- Omit the calendar question
- Produce cards that look like a table, not intelligence

## Reference build

The Accor Plus dashboard is a single self-contained HTML file with:
- Dark theme, brand colours
- 20 lead cards with expandable outreach panels
- Filter controls at the top
- Metrics row at the top
- Each card: fit score badge, company, region, staff, contact name/title, verified LinkedIn, personalisation insight, derived email with warning, LinkedIn DM draft, cold email draft
- No external dependencies

This is the standard. Every `crew-web-lead-dashboard-builder` invocation must aim for this depth.
