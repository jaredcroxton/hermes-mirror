# Exact format preservation

Use this note when maintaining `branded-lead-dashboard` or routing future lead-dashboard work.

## Why this exists

Jared confirmed that the exact Claude Code version of this skill is the standard because it reliably brings through real LinkedIn decision makers. Do not simplify the workflow back into a generic company-lead dashboard.

## Non-negotiables

- Preserve the intake sequence.
- Preserve company-first, person-second discovery.
- Preserve the rule that decision-maker URLs must contain `linkedin.com/in/`.
- Preserve HarvestAPI as the source of truth for names.
- Never infer a person's name from a LinkedIn slug or search snippet.
- Preserve verified_date and freshness indicators.
- Preserve self-addressed Gmail drafts.
- Preserve calendar focus blocks.
- Preserve the motion verification gate.
- Preserve the monolithic `dashboard.html` output.

## Drift warning

If a future dashboard has good visual polish but missing decision-makers, the failure is usually not UI. It is that the workflow drifted back to company-level enrichment. Return to Step D2 and D3 before rendering.

## Correct failure response

Do not patch around missing names with generic decision-maker search links. Re-run company-anchored individual LinkedIn search and HarvestAPI profile scraping, then regenerate `data/leads.json`.