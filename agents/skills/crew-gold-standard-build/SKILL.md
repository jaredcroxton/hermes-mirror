---
name: crew-gold-standard-build
description: Use when Jared and Brock are migrating or upgrading Crew skills to gold-standard depth. Covers the migration workflow from old performos-crew-skills into the canonical crew-skill-packs tree, the prompt template for Claude Code, Brock's review checklist, and the two-agent build pattern.
category: performos
---

# Crew Gold-Standard Build

## When to use

Jared wants to bring a Crew skill (or an entire pack) to gold-standard depth. This covers two scenarios:

1. **Migration:** An old full-depth skill exists in `/Users/jc/Desktop/performos-crew-skills/` and needs porting into the canonical tree at `/Users/jc/Desktop/cluade/crew-skill-packs/packs/`
2. **Upgrade:** A canonical skill exists but is shallow (5 sections, ~8-10KB) and needs the full 15-section treatment

## Two-agent build pattern

Brock does not build skills directly. The pattern is:

1. **Brock writes the prompt** — a self-contained Claude Code brief with source path, target path, reference benchmarks, numbered steps, and a report format
2. **Jared pastes the prompt into Claude Code** — Claude Code executes the build
3. **Brock reviews the output** — structural verification (size, sections, banned terms, fixture), then reports pass/fail to Jared

Brock never writes the SKILL.md content. Claude Code is the builder. Brock is the QA gate.

## Gold standard definition

A gold-standard Crew skill has:

- 15 `##` sections minimum (matching the benchmark: Inputs, Modes and when to use them, cognitive framework, domain-specific taxonomies, Workflow with Step 0 context recovery and Final Step handoff save, Output format, Decision briefs, Guardrails, Handoffs, Plan mode, Verification, Completion)
- Context Loop: Step 0 reads from `.claude/crew-state/<pack>/<skill>-handoff.md`, Final Step writes back
- White-label: no Accor examples, no flow-state, no internal agent names (Brock, Bob, Lara, Hermes, Claude Code), no Sarah
- No em dashes
- Fixture file in the pack's `tests/` directory with at least 2 cases
- QA smoke passes: `bash /Users/jc/Desktop/cluade/crew-skill-packs/shared/qa-check.sh --smoke --pack <pack>`

## No arbitrary size ceiling

Jared's rule: skills can go as deep as the content demands. Do not cap at 14KB, 15KB, or any other number. "If it has to go a bit over, it goes a bit over. It can go way over if it needs to." The 14KB figure is a floor for structural completeness, never a ceiling.

## Migration prompt template

Copy this structure for each migration prompt:

```
**Task:** Migrate `flow-support-<name>` from the old build folder into the canonical Crew pack tree as an upgraded `crew-support-<name>`.

**Source file:** `/Users/jc/Desktop/performos-crew-skills/customer-support/flow-support-<name>/SKILL.md`

**Target file:** `/Users/jc/Desktop/cluade/crew-skill-packs/packs/<NN-pack>/crew-<domain>-<name>/SKILL.md`

**Reference gold standards:** [list 1-2 already-migrated benchmarks]

**What to do:**
1. Read the source file completely
2. Read the target file completely
3. Read the reference gold standard(s) as structural benchmarks
4. Merge the depth and structure from the source into the target
5. Preserve all sections from the source, adapt to canonical naming
6. Strip all Accor-specific examples, flow-state bash, internal agent names, flow-* cross-references (remap to canonical crew-* names)
7. White-label business language throughout. No em dashes.
8. Update or create the fixture at `<pack>/tests/crew-<domain>-<name>.fixture.md` — at least 2 cases
9. Run QA: `bash /Users/jc/Desktop/cluade/crew-skill-packs/shared/qa-check.sh --smoke --pack <pack>`
10. Report: old size, new size, sections added, QA result
```

## Upgrade prompt template (no source migration)

When upgrading a shallow canonical skill with no old source:

```
**Task:** Upgrade `crew-<domain>-<name>` to gold-standard depth.

**Target file:** [path]

**Reference gold standards:** [list benchmarks]

**What to do:**
1. Read the target file completely
2. Read reference gold standards for structure
3. Preserve all existing implementation depth
4. Add missing gold-standard sections: Modes, cognitive framework, decision briefs, plan mode, verification, completion
5. Add Context Loop
6. No em dashes. White-label. No internal agent names.
7. Upgrade fixture — at least 2 cases
8. Run QA
9. Report: old size, new size, sections added, QA result
```

## Brock review checklist

After Claude Code reports completion, Brock verifies:

1. **Size:** run `wc -c` on the target SKILL.md. Compare to old size. Confirm growth.
2. **Sections:** run `grep "^##"` and count `##` headings. Confirm 15 minimum.
3. **Banned terms:** run `grep -in "flow-state\|Accor\|Sarah\|PerformOS\|Brock\|Bob\|Lara\|Hermes\|gstack\|free night\|ACA\|ACCC"` on the target. Must be clean except for em-dash prohibition rules.
4. **Fixture:** confirm the fixture file exists and has content.
5. **Report back to Jared:** one line per skill. Size, sections, clean/dirty, pass/fail.

## Canonical paths

- **Source of truth:** `/Users/jc/Desktop/cluade/crew-skill-packs/packs/`
- **Old full-depth skills (migration sources):** `/Users/jc/Desktop/performos-crew-skills/`
- **Shared QA:** `/Users/jc/Desktop/cluade/crew-skill-packs/shared/qa-check.sh`
- **Dist zips:** `/Users/jc/Desktop/cluade/crew-skill-packs/dist/` (only packs 01-09 built; 10-11 pending)
- **Plugin tree:** `/Users/jc/Desktop/cluade/crew-skill-packs/plugins/` (regenerate with `build-plugins.sh`)

## Crew pack structure (24 June 2026)

| Pack | Skills | Gold | Upgraded | Shallow |
|------|--------|------|----------|---------|
| 01-core | 7 | 0 | 0 | 7 |
| 02-sales | 7 | 0 | 0 | 7 |
| 03-marketing | 7 | 0 | 0 | 7 |
| 04-ops | 5 | 0 | 0 | 5 |
| 05-hr | 5 | 0 | 0 | 5 |
| 06-finance | 6 | 0 | 0 | 6 |
| 07-support | 6 | 3 (ticket-triage, reply-builder, feedback-summary) | 0 | 3 |
| 08-docs | 7 | 0 | 0 | 7 |
| 09-training | 8 | 0 | 0 | 8 |
| 10-web-design | 3 | 1 (slide-deck-builder) | 1 (fly-through-builder) | 1 (lead-dashboard-builder) |
| 11-infrastructure | 1 | 0 | 1 (project-builder, 7 sections) | 0 |

**Key:** Gold = 15+ sections, clean. Upgraded = above baseline but under 15 sections. Shallow = 5-7 sections, ~8-11KB baseline.

## Upgrade prompt template: the "promote ### to ##" technique

When upgrading a skill with deep implementation content already present under `###` headings, identify every `###` heading that contains substantive build instructions (not one-liners) and promote it to `##`. This is how slide-deck-builder reached 17 sections — spec blocks like Slide types, Brand variables, Navigation, and Code highlighting earned `##` status because they contained real implementation depth. The Claude Code prompt must explicitly instruct: "Identify every `###` heading with substantive implementation depth. These are candidates for `##` promotion. Only promote if the content warrants it — no filler sections."

## Brock review checklist

After Claude Code reports completion, Brock verifies:

1. **Size:** run `wc -c` on the target SKILL.md. Compare to old size. Confirm growth.
2. **Sections:** run `grep "^##"` and count `##` headings. Confirm 15 minimum.
3. **Banned terms:** run `grep -in "flow-state\|Accor\|Sarah\|PerformOS\|Brock\|Bob\|Lara\|Hermes\|gstack\|free night\|ACA\|ACCC"` on the target. Must be clean except for em-dash prohibition rules.
4. **Fixture:** confirm the fixture file exists and has content.
5. **Report back to Jared:** one line per skill. Size, sections, clean/dirty, pass/fail.

## Never trust memory over disk

Memory entries about CREW pack state can be stale. The entry "lead-dashboard gold" in memory was wrong — disk showed 5 sections. Before reporting any skill as gold, always verify with `wc -c` and `grep -c '^## '` directly on the SKILL.md file. Memory is a hint. Disk is truth.

## Pitfalls

- The old `performos-crew-skills/` folder uses `flow-` prefix naming. Always remap to `crew-` prefix in the canonical tree.
- The `build-plugins.sh` script hardcodes "58 skills" — stale. Actual count is 62.
- The `README.md` in crew-skill-packs lists only 9 packs. Packs 10 and 11 are missing from the table.
- Dist zips and plugin tree only cover packs 01-09. Do not rebuild them until Jared says the pack is done.
- Some canonical skills in `crew-skill-packs/packs/` are structurally shallow (5 sections) despite the same pack having gold-standard neighbours. Always check before assuming a pack is complete.
- The `flow-` grep in banned-term checks matches CSS properties like `overflow-x`. These are false positives, not skill-name leaks. When Claude Code reports a `flow-` match, verify it's not a CSS property before flagging it.
- Internal references (APOGEE, jaredcroxton, aether-genesis, premium-dashboard-design-reviewer, "Update memory") can live in three places: the SKILL.md, bundled reference files (HTML, JSON), and fixtures. A scrub must check all three. The Claude Code prompt should explicitly list each file type that needs cleaning.
