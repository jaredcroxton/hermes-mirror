# PerformOS Crew current state reference

Captured from the Crew skills context review on 17 June 2026.

## Purpose

Use this reference when Jared asks to continue building, auditing, or reconciling PerformOS Crew skills. It captures the current source-of-truth issue so future sessions do not rely on stale counts or missing files.

## Current strategic model

PerformOS Crew is the portable AI work team layer.

Clean internal line:

- Agents are who does the work.
- Skills are how the work gets done.
- Context is what keeps the work specific to the business.

Superpowers is not a skill pack. It is the methodology layer underneath the skills.

## Methodology standards

Every Crew skill should inherit these eight standards:

1. Brainstorm before building
2. Plan in bite-sized tasks
3. Build with testing built in
4. Debug from root cause
5. Verify before claiming done
6. Review before shipping
7. Finish cleanly
8. Save and restore context

## Current catalogue source

Primary catalogue source found during review:

`/Users/jc/Desktop/cluade/performos-crew-catalogue/build.py`

Generated PDF:

`/Users/jc/Desktop/cluade/performos-crew-catalogue/PerformOS Crew Skill Pack Catalogue.pdf`

The deck source currently defines 9 packs and 57 catalogue skills:

1. Core Crew Skills, 6
2. Sales Pack, 7
3. Marketing Pack, 7
4. Operations Pack, 5
5. HR and People Pack, 5
6. Finance and Admin Pack, 6
7. Customer Support Pack, 6
8. Documentation Pack, 7
9. Training and L&D Pack, 8

## Existing executable skill folders

Project-local installed flow layer:

`/Users/jc/Desktop/cluade/.claude/skills/`

Observed state:

- 45 SKILL.md files total in that folder
- 16 are `flow-*` skills
- 29 are other local project or dev/design skills

Crew build folder:

`/Users/jc/Desktop/performos-crew-skills/`

Observed state:

- 50 SKILL.md files total
- Three Customer Support skills are full-depth reference implementations
- Most other pack files are lightweight stubs and should not be treated as shippable

## Full-depth reference implementations

Approved benchmark folder:

`/Users/jc/Desktop/performos-crew-skills/customer-support/`

Full-depth reference files:

- `flow-support-triage/SKILL.md`, about 15.7 KB, 435 lines
- `flow-support-reply/SKILL.md`, about 16.0 KB, 483 lines
- `flow-support-feedback/SKILL.md`, about 14.1 KB, 367 lines

Use these as the quality benchmark for future pack builds.

## Important count mismatch

Do not quote one total without reconciling it first.

Observed counts:

- Catalogue deck source: 57 skills across 9 packs
- Earlier clean architecture note: 16 flow engine plus 47 crew pack skills equals 63 total
- Actual Crew build folder: 50 SKILL.md files
- Installed `.claude/skills` folder: 45 SKILL.md files, only 16 are flow

Recommended operating rule:

Before building or reporting totals, state which source is being used: catalogue source, executable folder, installed folder, or architecture model.

## Missing file warning

A previous response referenced:

`/Users/jc/Desktop/sales-pack-gstack-build.md`

That file was not found during the review. Do not rely on it existing. If Jared asks for it, recreate it from the catalogue source, depth standard, and Customer Support reference skills.

## Build recommendation

The next sensible build sequence is:

1. Lock the master catalogue source of truth.
2. Rebuild Sales Pack to full depth, because it is the clearest commercial wedge.
3. Rebuild Marketing Pack.
4. Rebuild Operations Pack.
5. Rebuild Training and L&D Pack once the commercial packs are clean.

## White-label rules

For client-facing Crew materials and skills:

- No internal agent names
- No runtime references
- No external project references
- No em dashes
- Frontmatter must only include `name` and `description`
- White-label business language only
- A skill under 5 KB is rejected as a stub unless Jared explicitly asks for a catalogue-only description
