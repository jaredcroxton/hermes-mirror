# Education Agent Opportunity Dashboard Pattern

Use this reference when Jared wants a lead dashboard for selling private AI agents, AgentOS, or PerformOS agent services to education, training, RTO, college, tutoring, or VET providers.

## Commercial promise

Find education providers with visible admin complexity, compliance burden, student enquiry volume, and course operations pressure.

Core question the dashboard must answer:

> Which providers should Jared call first, why now, and what private-agent use case should he lead with?

## Best first MVP

Start with one region and one sector cluster.

Good first proof:

- Sunshine Coast education, training, RTOs, colleges, tutoring, VET providers
- 30 to 50 providers
- Real public signals first, not fake demo rows
- Desktop HTML dashboard plus CSV/JSON source files
- Google Sheets only after Google OAuth is confirmed

## Recommended source stack

Use the simplest working source-of-truth first:

1. Apify Google Maps Scraper
   - Actor used successfully: `compass/crawler-google-places`
   - API actor slug: `compass~crawler-google-places`
   - Search terms: `RTO`, `training provider`, `vocational training`, `college`, `first aid training`, `tutoring`, `education centre`, `business training`
   - Location: `Sunshine Coast, Australia`
   - Cap places per search for cost control
2. Public website crawl
   - Course links
   - Enrolment/contact paths
   - Forms
   - Policy/compliance pages
   - Careers/hiring pages
   - RTO/CRICOS signals
3. Apollo.io organisation enrichment where domain is available
   - Employee estimate
   - LinkedIn company URL
   - Industry
   - Technology names
4. Local CSV/JSON as first source of truth
5. Google Sheets after OAuth is configured
6. n8n workflow after the first run proves useful

Do not block the first real build on Google Sheets or n8n if Apify and Apollo are available. Produce CSV/JSON locally first, then automate.

## Implementation lessons from first real build

Jared approved a live run with: `lock it in`. When approved, act as the expert operator: connect the apps that are already available, run a cost-controlled pull, write artifacts, open in Chrome, and verify. Do not stop at architecture advice.

Working first-build flow:

1. Create a project folder on Desktop.
2. Write a reusable `build_dashboard.py` script into that folder.
3. Load `APIFY_TOKEN` or `REDACTED_APIFY_PREFIX_TOKEN` and `APOLLO_API_KEY` from `/Users/jc/.hermes/.env` without printing secret values.
4. Start the Apify run for `compass~crawler-google-places`.
5. Poll the actor run until terminal status. The API may return initial status `READY` even when `waitForFinish` is supplied. Treat that as not done, not as failure.
6. Fetch the default dataset items only after status is `SUCCEEDED` or `TIMED-OUT` and a `defaultDatasetId` exists.
7. Deduplicate by provider name plus domain/address.
8. Crawl public websites with a normal browser user-agent and conservative timeout.
9. Enrich domains with Apollo organisation enrichment where a domain exists. Cap attempts for cost control.
10. Score and write `HTML`, `CSV`, `JSON`, `pipeline-notes.md`, and the build script itself.
11. Open the HTML file in Google Chrome.
12. Verify: file sizes, row counts, search/filter behaviour, CSV export click, and browser console has zero JavaScript errors.

Recommended Apify polling pattern:

```python
run = request_json(run_url, data=input_data, headers={'Content-Type': 'application/json'}, timeout=270)['data']
run_id = run.get('id')
terminal_statuses = {'SUCCEEDED', 'FAILED', 'ABORTED', 'TIMED-OUT'}
for _ in range(80):
    if run.get('status') in terminal_statuses:
        break
    if not run_id:
        break
    time.sleep(6)
    run = request_json(
        f'https://api.apify.com/v2/actor-runs/{run_id}?token={urllib.parse.quote(apify_token)}',
        timeout=60,
    )['data']
```

First real Sunshine Coast education build produced a healthy target shape:

- 64 raw Apify results
- 45 scored providers
- 35 Hot or Warm targets
- 18 RTO or CRICOS signals
- 30 Apollo enrichment attempts
- 27 Apollo matches

Do not hard-code those numbers as expected results. Use them as a benchmark that the search terms and scoring model can produce a useful first dashboard.

## Dashboard columns

Required fields:

- rank
- provider name
- type/category
- location
- website
- domain
- phone
- Google rating
- review count
- Google Maps URL
- RTO number if found
- CRICOS signal if found
- course links detected
- policy links detected
- contact paths detected
- hiring links detected
- website forms detected
- Apollo status
- Apollo employees
- Apollo industry
- LinkedIn company URL
- admin complexity score
- compliance score
- student enquiry score
- clear agent use case score
- growth/hiring score
- contactability score
- fit score out of 100
- priority
- best private agent use case
- use case detail
- likely buyer
- why contact now
- first call angle
- first email opener
- source
- status
- notes

## Scoring model

Use a transparent 100-point model:

- Course/admin complexity: 20
- Compliance burden: 20
- Student enquiry volume: 20
- Clear private-agent use case: 20
- Growth or hiring signal: 10
- Contactability: 10

Priority bands:

- Hot: 85 to 100
- Warm: 70 to 84
- Nurture: 55 to 69
- Low: under 55

Hard rule:

> If there is no clear private-agent use case, cap the score at 69.

## Best private-agent use cases

Map each provider to one primary use case:

1. Student Enquiry and Course Advice Agent
   - Course dates, pricing, eligibility, enrolment steps, next intake, FAQs
2. Compliance and Student Admin Agent
   - Policies, student handbooks, complaints, appeals, assessment process, audit prep
3. Learning Designer Agent
   - Course outlines, trainer notes, quizzes, learner guides, microlearning
4. Trainer Support Agent
   - Session plans, feedback drafts, learner follow-up, resource adaptation
5. Operations Support Agent
   - Email triage, process documentation, weekly reports, staff onboarding
6. Student Support and Parent Enquiry Agent
   - Tutoring, parent/student questions, scheduling, lesson follow-up

## Offer framing

Lead with a low-friction audit before the full AgentOS sale.

Entry offer:

**Private AI Readiness Audit for Education Providers**

Typical price:

- $750 to $1,500

Deliverable:

- repetitive admin workflow map
- top three private-agent opportunities
- student enquiry leakage review
- compliance/documentation pressure scan
- recommended pilot
- implementation quote

Upsell:

**AgentOS by PerformOS**

Private AI team for education providers.

## Outreach angle

First call opener:

> Hi, I work with education and training providers using private AI agents for student enquiries, admin, and compliance workflows. I noticed [Provider] has [visible signal]. I wanted to ask whether enquiry handling, trainer admin, or compliance documentation is taking more staff time than it should.

First email opener:

> I noticed [Provider] appears to run education or training services on the Sunshine Coast. I build private AI agents for providers that want help with student enquiries, course admin, trainer support, and compliance documentation without pushing sensitive business information into public AI tools.

## Data quality rules

- Do not invent named contacts.
- Do not invent RTO or CRICOS numbers.
- Label inferred signals as inferred.
- Public contact details should be verified before high-volume outreach.
- Apollo organisation enrichment is useful but not required for every row.
- A larger company is not automatically a better target unless the dashboard shows a clear agent use case.

## Automation path

Phase 1:

Apify → local website crawl → Apollo enrichment → CSV/JSON → local HTML dashboard.

Phase 2:

Apify → n8n → Google Sheets → HTML dashboard refresh.

Phase 3:

Hosted dashboard with scheduled refresh, evidence links, and segment templates for other regions or industries.
