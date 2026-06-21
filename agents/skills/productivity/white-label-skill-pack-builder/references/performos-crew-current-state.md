# PerformOS Crew current state reference

Captured from the completed Crew Skill Packs product build, 17 June 2026. Updated after final verification.

## Purpose

Use this reference when Jared asks to continue building, auditing, or reconciling PerformOS Crew skills. It captures the current completed state so future sessions do not rely on stale counts.

## Product state: 11 packs (62 skills, pack 10 building)

**60 skills across the original 10 packs (complete). Pack 10 (Web Design) is under active construction with 3 of 8 planned skills built.**

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
| 10 Web Design | 3 built (fly-through, slide-deck, lead-dashboard V2), 5 planned | Building |
| 11 Infrastructure | 1 built (project-builder from Express/A.N.T. protocol) | Done |
| **Total** | **62** | |

Pack 10 (Web Design) built skills:
- `crew-web-fly-through-builder` — cinematic scroll-descent website builder with locked reference build, pipeline scripts, and 13-row failure-modes table.
- `crew-web-slide-deck-builder` — branded HTML slide deck builder with 4 preset themes extracted from PerformOS brand configs. No CDN, single file, offline-capable.
- `crew-web-lead-dashboard-builder` (V2) — end-to-end lead intelligence pipeline: scrape → fit scoring (0-100) → LinkedIn decision-maker lookup (default on) → personalised insight → dual-channel outreach (email + LinkedIn DM) → dashboard with filters → calendar offer. Four-colour evidence tags (Confirmed/Inferred/Derived/Escalated). Escalation for thin signals. V2 rebuild was necessary because V1 treated LinkedIn as a gated permission rather than default on, producing thin cards with "LinkedIn research not enabled" on every row.

Pack 11 (Infrastructure) built skills:
- `crew-project-builder` — deterministic build protocol adapted from the Express/A.N.T. 5-phase system. Scaffolds CLAUDE.md, memory files, architecture/, execution/, .tmp/. Five discovery questions. Three-layer architecture (SOPs, Navigation, Tools). Self-annealing repair loop. Mandatory Taste Skill bundle auto-load. Renamed from "Express" to "Project Builder" for new-user clarity.

Web Design pack skills carry bundled reference builds, pipeline scripts, and `.env.example` files alongside their SKILL.md. Unlike the text-only packs (01-09), Web Design skills are code-producing and their verification steps include opening a browser, inspecting rendered output, and taking screenshots at multiple viewports.

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

Currently shows 9 packs, 58 skills, Core (7), 42 pages. Packs 10 (Web Design) and 11 (Infrastructure) are not yet represented. Regenerate after completing the Web Design pack to show all 11 packs, 62+ skills.

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

- PDF catalogue: 9 packs, 58 skills (Core = 7). Needs regeneration after packs 10 and 11 complete.
- Built packs: 11 packs, 62 skills (packs 01-09 + 11 done; pack 10 at 3 of 8 building)
- Structural QA: 62/62 PASS (all packs)
- Functional smoke: 62/62 PASS (all packs)
- Known mismatch: PDF shows 9 packs, product has 11. Regenerate PDF after pack 10 (Web Design) is complete.

## Recommended rebuild sequence (if expanding)

If Jared wants to add more skills or packs in the future:

1. Define the skill in the catalogue source first (`performos-crew-catalogue/build.py`).
2. Regenerate the PDF to match.
3. Build the skill to the locked template in `crew-skill-packs/packs/`.
4. Add a 3-case test fixture.
5. Run structural QA + functional smoke.
6. Rebuild zip + update plugin.

**Web Design pack (10) special handling:** This pack is the first where skills carry bundled reference builds, pipeline scripts, and `.env.example` files alongside SKILL.md. Unlike text-only packs (01-09), Web Design skills produce code artifacts. Their verification steps include browser inspection, console checks, and multi-viewport screenshots. When building new Web Design skills, follow the `crew-web-fly-through-builder` pattern: restructure first to the Crew template (Step 0 + Final Step), preserve all locked engineering and reference builds, then add guardrails, handoffs, and fixtures. The `crew-web-slide-deck-builder` brief is ready at `~/Desktop/crew-web-slide-deck-builder-brief.md`.
