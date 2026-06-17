# PerformOS Crew current state reference

Captured from the completed Crew Skill Packs product build, 17 June 2026. Updated after final verification.

## Purpose

Use this reference when Jared asks to continue building, auditing, or reconciling PerformOS Crew skills. It captures the current completed state so future sessions do not rely on stale counts.

## Product state: 10 packs (58+ currently building)

**58 skills across the original 9 packs (complete). Pack 10 (Web Design) is under active construction.**

| Pack | Skills | Status |
|---|---|---|
| 01 Core | 7 (incl. using-crew dispatcher) | Done |
| 02 Sales | 7 | Done |
| 03 Marketing | 7 | Done |
| 04 Operations | 5 | Done |
| 05 HR & People | 5 | Done |
| 06 Finance & Admin | 6 | Done |
| 07 Customer Support | 6 (crew-support-*) | Done |
| 08 Documentation | 7 | Done |
| 09 Training & L&D | 8 | Done |
| 10 Web Design | 1 built (fly-through-builder), 7 planned | Building |
| **Total** | **59+** | In progress |

Pack 10 is unique: its skills carry bundled reference builds, pipeline scripts, and `.env.example` files alongside their SKILL.md. Unlike the text-only packs (01-09), Web Design skills are code-producing and their verification steps include opening a browser, inspecting rendered output, and taking screenshots at multiple viewports.

## Primary build location

`/Users/jc/Desktop/cluade/crew-skill-packs/`

- `packs/` — all 9 pack folders with SKILL.md files
- `shared/` — crew-method.md, SKILL-TEMPLATE.md, qa-check.sh
- `dist/` — 9 per-pack zips + crew-full-bundle.zip
- `install.sh` / `uninstall.sh` / `package.sh`
- Plugin marketplace wrapper for `/plugin install`

## Locked skill template

Every skill follows this structure (~85-120 lines):

1. Frontmatter — name + description only
2. Title + role-opening paragraph — named expert role, cognitive instinct, what it does and does NOT do
3. Inputs — what it needs, missing-input fork
4. Workflow — Step 0: Context Recovery, 6-7 numbered phases with taxonomies, decision forks, forcing questions, verification penultimate step, Final Step: Handoff Save
5. Output format — fenced block with filled example
6. Guardrails — three families: business risk, evidence/honesty, house style
7. Handoffs — to sibling skills and Core by name

## Methodology layer

`shared/crew-method.md` documents the 8 standards and 5 loops every skill uses:

**8 standards:** brainstorm, plan, build with tests, debug root cause, verify, review, finish, save context.

**5 loops:** missing input, quality failure, escalation, context change, learning capture.

Every skill's workflow references the loops by name.

## White-label state

- Brand is "Crew" only.
- Zero banned-name leaks (Brock, Bob, Lara, Neo, Hermes, NemoClaw, gstack, gbrain, PerformOS).
- Zero em dashes.
- CREDITS.md acknowledges Superpowers and gstack as method influences only. All text is authored fresh.

## PDF catalogue

`/Users/jc/Desktop/cluade/performos-crew-catalogue/PerformOS-Crew-Skill-Pack-Catalogue.pdf`

Currently shows 9 packs, 58 skills, Core (7), 42 pages. The just-built Pack 10 (Web Design) is not yet represented. Regenerate after completing the Web Design pack to show 10 packs.

## Install paths

Three methods a buyer can use:

1. **install.sh** — POSIX shell script. `./install.sh --pack sales` copies 14 skill folders (7 Sales + 7 Core). Supports --all, --pack, --target, --global, --dry-run, --list. Idempotent no-clobber.
2. **Plugin** — `/plugin install` or `/crew:install sales`. `/crew:list` shows installed. `/crew:uninstall sales` removes.
3. **Claude Code file copy** — tell Claude Code: `Copy every folder from ~/Desktop/Crew-Skills-Core-and-Sales/01-core/ into .claude/skills/`

None touch settings, hooks, or CLAUDE.md. All are project-local.

## Old build folder (deprecated)

`/Users/jc/Desktop/performos-crew-skills/` contains the original lightweight stubs. Do not use this folder for builds or counts. Use `crew-skill-packs/` as the source of truth.

## Old reference implementations (deprecated)

The `flow-support-*` skills in the old build folder were replaced by `crew-support-*` in the completed product. The new skills use the locked template with Step 0 + Final Step.

## Count reconciliation

- PDF catalogue: 9 packs, 58 skills (Core = 7). Needs regeneration after pack 10 completes.
- Built packs: 10 packs, 59+ skills (pack 10 building: 1 done, 7 planned)
- Structural QA: 58/58 PASS (original 9 packs). Pack 10 fly-through-builder: verified separately against Crew template.
- Functional smoke: 58/58 PASS (original 9 packs). Pack 10: smoke pending on full pack.
- Known mismatch: PDF shows 9 packs, product has 10. Regenerate PDF after pack 10 is complete.

## Recommended rebuild sequence (if expanding)

If Jared wants to add more skills or packs in the future:

1. Define the skill in the catalogue source first (`performos-crew-catalogue/build.py`).
2. Regenerate the PDF to match.
3. Build the skill to the locked template in `crew-skill-packs/packs/`.
4. Add a 3-case test fixture.
5. Run structural QA + functional smoke.
6. Rebuild zip + update plugin.

**Web Design pack (10) special handling:** This pack is the first where skills carry bundled reference builds, pipeline scripts, and `.env.example` files alongside SKILL.md. Unlike text-only packs (01-09), Web Design skills produce code artifacts. Their verification steps include browser inspection, console checks, and multi-viewport screenshots. When building new Web Design skills, follow the `crew-web-fly-through-builder` pattern: restructure first to the Crew template (Step 0 + Final Step), preserve all locked engineering and reference builds, then add guardrails, handoffs, and fixtures. The `crew-web-slide-deck-builder` brief is ready at `~/Desktop/crew-web-slide-deck-builder-brief.md`.
