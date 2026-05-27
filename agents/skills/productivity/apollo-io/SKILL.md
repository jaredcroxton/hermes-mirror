---
name: apollo-io
description: "Use when automating Apollo.io sales intelligence workflows: configuring API access, enriching companies, sourcing lead/persona targets, exporting CSVs, and designing B2B partnership or bulk-membership prospecting workflows."
version: 1.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [apollo, sales-intelligence, lead-generation, enrichment, b2b, csv-export]
    related_skills: [google-workspace, airtable, linear]
---

# Apollo.io Workflows

## Overview

Apollo.io is used here as a B2B sales-intelligence connector for company enrichment, prospect/persona targeting, lead-list creation, partnership research, and CSV exports. Use this skill whenever the user asks for Apollo automations, prospecting lists, company/person enrichment, or sales workflows involving bulk memberships, partnerships, employee benefits, travel, hotels, or similar B2B opportunities.

The user's current setup stores the API key in Hermes' environment file as `APOLLO_API_KEY`. Never print or expose the key. Verify presence with a boolean check only.

## When to Use

Use this skill for:

- Setting up Apollo.io API access in Hermes.
- Testing whether `APOLLO_API_KEY` is visible after a gateway restart.
- Building company/persona target lists from Apollo data.
- Enriching organizations by domain.
- Exporting Apollo-derived results to CSV.
- Creating lead-selection strategies for B2B partnerships, employee benefits, travel memberships, hotel partnerships, or corporate bulk-buying programs.
- Explaining Apollo API plan limitations and safe fallbacks.

Do **not** use this skill for Apollo GraphQL. If the user says “Apollo” ambiguously, confirm whether they mean **Apollo.io** or GraphQL before taking action.

## Secret Safety

- Never ask the user to paste the Apollo API key into chat.
- Never print `APOLLO_API_KEY` or the full `.env` file.
- Never include screenshots or logs that expose tokens.
- If checking setup, only report booleans/lengths, e.g. “key line found: yes; non-empty: yes”.
- Warn the user if a screenshot of `.env` exposes other secrets, but do not repeat the secret.

## Setup

Hermes reads secrets from the env file reported by:

```bash
hermes config env-path
```

Typical path on this machine:

```bash
/Users/jc/.hermes/.env
```

The user should add:

```bash
APOLLO_API_KEY=their_real_apollo_key_here
```

Rules:

- No `#` at the start.
- No spaces around `=`.
- One line only.
- Do not use `export` unless the specific runtime requires it.

After editing, restart the gateway:

```bash
hermes gateway restart
```

## Setup Verification

Check without revealing the key:

```bash
python3 - <<'PY'
from pathlib import Path
p = Path('/Users/jc/.hermes/.env')
found = False
nonempty = False
for line in p.read_text(errors='ignore').splitlines():
    s = line.strip()
    if s.startswith('APOLLO_API_KEY='):
        found = True
        val = s.split('=', 1)[1].strip().strip('"').strip("'")
        nonempty = bool(val)
        break
print({'apollo_key_line_found': found, 'apollo_key_nonempty': nonempty})
PY
```

Never run the `.env` file directly. If the user tries `/Users/jc/.hermes/.env` and gets “permission denied,” explain that `.env` is a text file to edit, not a command.

## API Calling Pattern

Use `APOLLO_API_KEY` from the env file, not from chat. Use `x-api-key` in request headers.

Minimal organization enrichment probe:

```python
import json, urllib.request
from pathlib import Path

key = None
for line in Path('/Users/jc/.hermes/.env').read_text(errors='ignore').splitlines():
    s = line.strip()
    if s.startswith('APOLLO_API_KEY='):
        key = s.split('=', 1)[1].strip().strip('"').strip("'")
        break

req = urllib.request.Request(
    'https://api.apollo.io/api/v1/organizations/enrich',
    data=json.dumps({'domain': 'qantas.com'}).encode(),
    headers={
        'Content-Type': 'application/json',
        'x-api-key': key,
        'User-Agent': 'HermesApolloConnector/0.1',
    },
    method='POST',
)
obj = json.loads(urllib.request.urlopen(req, timeout=30).read())
print(obj.get('organization', {}).get('name'))
```

Useful organization enrichment fields:

- `name`
- `primary_domain`
- `website_url`
- `linkedin_url`
- `id`
- `industry` / `industries`
- `estimated_num_employees`
- `city`, `state`, `country`
- `departmental_head_count`
- `keywords`
- `technology_names`

## Apollo Plan Limitations and Fallbacks

Current observed setup:

- `api/v1/organizations/enrich` worked with the user's API key.
- `api/v1/mixed_people/search`, `api/v1/mixed_companies/search`, `api/v1/people/match`, and `api/v1/people/enrich` returned `API_INACCESSIBLE` on the current/free plan.

Do not hard-code this as a permanent global limitation. Treat it as a plan-specific runtime condition. Probe the endpoint, then adapt.

Fallback strategy when people/company search is inaccessible:

1. Use Apollo organization enrichment by known company domains.
2. Export company-level targets plus **target professional titles/personas** rather than named contacts.
3. Include notes that named-person search requires an Apollo plan/API entitlement or Apollo UI workflow.
4. Provide clear filters the user can paste into Apollo UI, e.g. company + title + geography.
5. If the user upgrades, re-probe search endpoints before rebuilding the connector.

## Lead-List Workflow

1. Clarify the commercial objective:
   - bulk memberships
   - employee benefits
   - customer rewards
   - partnership distribution
   - corporate travel
   - travel agent resale/channel partnership

2. Define target organizations:
   - high employee count
   - relevant travel/dining/lifestyle audience
   - corporate travel needs
   - rewards/loyalty ecosystems
   - retail or professional-services workforce
   - travel sellers or agencies

3. Define target professionals/personas:
   - Head of Partnerships
   - Strategic Partnerships Manager
   - Employee Benefits Manager
   - Rewards Manager
   - People Experience Lead
   - Procurement Manager
   - Travel Manager
   - Corporate Travel Director
   - Supplier Relations Manager
   - Loyalty Program Manager

4. Enrich organization domains through Apollo.

5. Score fit:
   - travel seller/channel fit: high
   - huge workforce/employee benefits fit: high
   - loyalty/rewards customer-base fit: high
   - frequent business-travel workforce: high

6. Export to CSV with enough context to act on.

## Recommended CSV Columns

For company + persona target exports:

- `rank`
- `company`
- `domain`
- `website`
- `linkedin_company_url`
- `apollo_company_id`
- `industry`
- `estimated_employees`
- `location`
- `target_professional_titles`
- `best_angle_for_<offer>`
- `suggested_offer`
- `fit_score_100`
- `apollo_status`
- `notes`

For named-contact exports, if the Apollo plan allows person search/enrichment:

- `first_name`
- `last_name`
- `title`
- `company`
- `email_status`
- `business_email` only if compliant and permitted
- `linkedin_url`
- `city/state/country`
- `apollo_person_id`
- `persona_match_reason`

## Compliance and Quality Guardrails

- Prefer B2B contacts and business use cases.
- Do not generate or send cold outreach automatically unless the user explicitly requests it and compliance requirements are clear.
- Avoid personal emails unless the user explicitly asks and the use is lawful/appropriate.
- For Australia-focused prospecting, keep geography and messaging Australian unless the user broadens scope.
- When exporting leads, include why each lead fits; raw names/domains are less useful than actionable context.

## Accor Plus / Travel Membership Targeting Pattern

For Accor Plus partnership or bulk membership deals, prioritize:

- Travel sellers: Flight Centre Travel Group, Helloworld, CTM, travel agencies.
- Airlines and travel-adjacent companies: Qantas, airport/hospitality groups.
- Large employers: Woolworths, Coles, Wesfarmers, banks, telcos, consulting firms, tech companies.
- People teams: employee benefits, rewards, wellbeing, people experience.
- Partnership teams: strategic partnerships, loyalty, customer rewards, affinity partnerships.
- Procurement/travel managers: corporate travel and employee perks.

Offer angles:

- Bulk employee Accor Plus memberships.
- Corporate benefits package.
- Customer rewards/loyalty partnership.
- Co-marketing travel and dining offers.
- Travel agency/channel distribution partnership.

## Common Pitfalls

1. **User types confirmation text into Terminal.** If they type “Apollo key is added” in shell and get `zsh: command not found`, explain that the phrase was meant for chat, not Terminal.

2. **User runs `.env` directly.** `/Users/jc/.hermes/.env` is not executable. Tell them to edit it with `nano /Users/jc/.hermes/.env`.

3. **Printing secrets while debugging.** Do boolean checks only.

4. **Assuming all Apollo endpoints work.** Probe endpoint access. If search endpoints return `API_INACCESSIBLE`, switch to organization-enrichment + persona export.

5. **Overpromising named contacts.** If plan limitations prevent person search, say so clearly and produce the best useful artifact: companies + target titles + Apollo UI filters.

6. **One-off company domain mismatch.** Apollo enrichment can map generic domains to unexpected regional subsidiaries. Verify high-value rows and try alternate domains where needed.

## Verification Checklist

- [ ] `APOLLO_API_KEY` exists and is non-empty without exposing it.
- [ ] Gateway restarted after `.env` edit.
- [ ] At least one low-cost API probe completed.
- [ ] Endpoint permissions confirmed for the current plan.
- [ ] CSV exists at the promised path and has the expected row count.
- [ ] CSV content is inspected for obvious wrong company matches.
- [ ] Final response states any API limitations and the fallback used.

## References

- See `references/accorplus-bulk-membership-targets.md` for the first Apollo.io workflow run: Accor Plus bulk-membership/partnership targets in Australia, API permissions observed, and CSV shape used.
