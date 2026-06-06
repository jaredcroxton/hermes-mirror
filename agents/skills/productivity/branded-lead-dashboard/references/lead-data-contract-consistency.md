# Lead Data Contract Consistency

## Session signal

Jared noticed lead dashboards changing from run to run. The build quality was good, but the data fields were inconsistent. Example: LinkedIn was sometimes included and sometimes left off.

## Durable lesson

For branded lead dashboards, the lead data shape must be locked before research or rendering starts. Treat the lead fields as a data contract, not an optional design choice.

## Required practice

Before building:
- Confirm required fields explicitly.
- Default LinkedIn to included for every lead where available.
- If LinkedIn is missing, show a visible status such as `not_found`, `private_profile`, `not_applicable`, or `not_checked`.
- Do not silently hide the LinkedIn field on some cards.
- Record any deliberate field omissions in `memory/decisions.md`.

Use this short intake block when Jared asks for a lead dashboard:

```text
Before I build, I need to lock the lead data contract so the dashboard stays consistent.
1. Should every lead include LinkedIn where available? Default yes.
2. If LinkedIn is missing, should I show not_found/private_profile rather than hiding it? Default yes.
3. Required fields: company, contact name, role, region, LinkedIn, source URL, source date, fit score, email status, outreach note, qualification signal. Any fields to remove or add?
```

If Jared is moving fast, ask the block once, then proceed on defaults. Do not keep pausing between phases.

During build:
- Use the same lead schema across `data/leads.json`, dashboard cards, detail drawer, export buttons, and outreach copy.
- Add a completeness check before declaring done.
- Flag missing mandatory fields rather than smoothing them over visually.

Suggested minimum lead row fields:
- `id`
- `company`
- `contact_name`
- `role`
- `region`
- `linkedin_url`
- `linkedin_status`
- `source_url`
- `source_date`
- `fit_score`
- `email_status`
- `outreach_note`
- `qualification_signal`

## Verification checklist

Before final delivery:
- Every lead row has the same keys.
- Every lead card renders the LinkedIn field or a visible LinkedIn status.
- The dashboard summary counts missing LinkedIn values.
- The findings file explains every missing LinkedIn profile.
- No card silently omits a field that appears on another card.
