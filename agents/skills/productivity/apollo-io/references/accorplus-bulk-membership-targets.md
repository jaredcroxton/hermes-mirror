# Accor Plus Bulk-Membership Targeting — First Apollo.io Run

## Context

The user wanted Apollo.io automation to find 20 professionals inside companies that could buy bulk Accor Plus memberships or consider partnership deals.

The user configured `APOLLO_API_KEY` in `/Users/jc/.hermes/.env` and restarted Hermes gateway successfully.

## API Access Observed

Using the current API key/plan:

- `POST https://api.apollo.io/api/v1/organizations/enrich` worked.
- `POST https://api.apollo.io/api/v1/mixed_people/search` returned `403 API_INACCESSIBLE`.
- `POST https://api.apollo.io/api/v1/mixed_companies/search` returned `403 API_INACCESSIBLE`.
- `POST https://api.apollo.io/api/v1/people/match` returned `403 API_INACCESSIBLE`.
- `POST https://api.apollo.io/api/v1/people/enrich` returned `403 API_INACCESSIBLE`.

Interpretation: company enrichment was available, but named people search/enrichment was not available on the current plan. Future agents should re-probe before assuming this is still true.

## Fallback Used

Because named people search was unavailable, the useful deliverable became:

- 20 company targets.
- The target professional titles/personas inside each company.
- Apollo organization enrichment fields where available.
- A partnership/bulk-membership angle for Accor Plus.
- CSV export.

## CSV Path Produced

```text
/Users/jc/Desktop/accorplus_apollo_bulk_membership_targets.csv
```

## CSV Columns Used

```text
rank
company
domain
website
linkedin_company_url
apollo_company_id
industry
estimated_employees
location
target_professional_titles
best_angle_for_accor_plus
suggested_offer
fit_score_100
apollo_status
notes
```

## Targeting Pattern

Best-fit company categories for Accor Plus bulk memberships or partnerships:

1. Travel sellers and corporate travel companies.
2. Large employers with employee-benefits teams.
3. Banks, telcos, and loyalty/rewards ecosystems.
4. Professional services firms with frequent travel.
5. Tech employers with people-experience/benefits budgets.

Best personas/titles:

- Head of Partnerships
- Strategic Partnerships Manager
- Corporate Travel Director
- Employee Benefits Manager
- Rewards Manager
- People Experience Lead
- Travel Manager
- Procurement Manager
- Loyalty Program Manager
- Supplier Relations Manager

## Domain-Matching Note

Apollo organization enrichment can sometimes resolve a domain to an unexpected regional subsidiary. In the first run:

- `flightcentretravelgroup.com` did not enrich well; `fctgcareers.com` resolved to Flight Centre Travel Group.
- `helloworld.com.au` resolved to a Mackay/Townsville agency; `helloworldlimited.com.au` resolved to Helloworld Travel Limited.

For high-value rows, try alternate domains and verify company names before final delivery.

## Final Communication Pattern

When delivering this class of result:

1. Attach the CSV as `MEDIA:/absolute/path.csv`.
2. State row count and enrichment count.
3. Disclose endpoint limitation clearly.
4. Avoid saying named contacts were found if only target personas were produced.
