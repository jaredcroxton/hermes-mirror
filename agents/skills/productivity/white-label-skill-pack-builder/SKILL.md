---
name: white-label-skill-pack-builder
description: Build installable white-label Claude Code skill packs from a product catalogue. Use when the user asks to create, expand, or update executable skills for the PerformOS Crew or any white-label client skill library.
---

# White-Label Skill Pack Builder

Build executable, installable Claude Code skills from product catalogue descriptions. Each skill must be a self-contained SKILL.md that Claude Code discovers and executes without external dependencies.

## Trigger

- User asks to build, create, or expand skill packs for the PerformOS Crew
- User asks to turn catalogue descriptions into installable skills
- User says "build out the skills," "make these executable," or "create the actual skills"
- User wants to give a client a folder of skills they can install

## Architecture

### Skill file format

Every skill is a single SKILL.md inside a named directory:

```
.claude/skills/<skill-name>/SKILL.md
```

### Frontmatter

YAML frontmatter with `name` and `description` only. Nothing else.

```yaml
---
name: crew-packname-skill-name
description: One-line description of what this skill does and when to invoke it.
---
```

Never include: `hooks`, `triggers`, `allowed-tools`, `gbrain`, `telemetry`, `preamble-tier`, or any G-Stack frontmatter fields.

### Depth standard (mandatory)

Every PerformOS Crew skill must match G-Stack depth. A skill that is 15-30 lines with four bullet workflow steps is REJECTED. The minimum bar is a skill that can survive a real business session.

All 14 sections are mandatory unless explicitly marked optional:

1. **Preamble** — bash script that records session start, detects project root and branch, checks for prior context saves, initialises state directories, and reports the operating environment.
2. **When to invoke** — trigger rules, anti-trigger rules, and mode selection (Fast, Careful, Governed).
3. **Cognitive framework** — named principles (3-5), a structured rubric or taxonomy, and forcing questions the skill must answer before producing output.
4. **Step-by-step workflow** — numbered phases. Each phase has a clear input, action, and output gate. Minimum 4 phases, typical 5-7.
5. **Guardrails** — safety constraints (minimum 6), escalation triggers, and boundary enforcement rules.
6. **Decision briefs** — a structured format for handling ambiguity. Must include ELI10, stakes, recommendation, completeness scoring, pros/cons, and net line.
7. **Output format** — fenced code block showing the exact output template the skill produces.
8. **Context bridge** — on-exit bash script that saves a context snapshot to `.claude/flow-state/contexts/`, and on-entry recovery that surfaces the most recent context.
9. **Learnings capture** — bash logging to `.claude/flow-state/learnings/learnings.jsonl` for pattern, pitfall, preference, architecture, and operational discoveries.
10. **Completion protocol** — DONE, DONE_WITH_CONCERNS, BLOCKED, NEEDS_CONTEXT with reason, attempted, and recommendation fields.
11. **Cross-skill integration** — which skills call this one, which skills this one calls, and the handoff protocol describing what runs next.
12. **Plan mode behaviour** — what the skill can and cannot do in plan mode without executing code or writing files.
13. **Verification checklist** — minimum 10 checkboxes the agent must confirm before marking the skill DONE.
14. **Brand/domain context** (optional) — if the skill operates on behalf of a specific brand voice, embed the full voice specification, banned phrases, and complaint-specific handling rules directly in the skill body so no external playbook is required.

### Naming convention

Use the prefix `crew-` followed by the pack name and skill function:

```
crew-sales-lead-researcher
crew-marketing-campaign-planner
crew-ops-process-mapper
crew-hr-role-profile-builder
crew-finance-invoice-workflow
crew-support-help-doc-generator
crew-docs-sop-builder
crew-training-needs-analyser
```

Never use internal agent names (Brock, Bob, Lara, Neo) in skill names or bodies.

### Guardrails (mandatory for every skill)

Every skill must include guardrails covering:

- Never fabricate information or make claims the business cannot support
- Never use internal agent names or system references
- Never assume context the skill has not been given
- Keep output concise and professional
- Minimum 6 safety constraints
- Escalation triggers: when to stop and flag, not continue
- Boundary enforcement: what the skill can and cannot access or modify

### Quality rules (hard)

- Zero em dashes anywhere in any SKILL.md
- Zero internal agent names (Brock, Bob, Lara, Neo, etc.)
- Zero runtime references (Hermes, NemoClaw, Claude Code, OpenShell)
- Zero G-Stack or external project names
- White-label business language only
- Frontmatter: name + description only, no other fields

## Workflow for building a skill pack

### Step 1: Create the pack directory

```
.claude/skills/ or any target directory/
  packname/
    skill-name/SKILL.md
    skill-name/SKILL.md
    ...
```

### Step 2: Write each skill

For each skill in the catalogue:

1. Define the role in second person
2. List the workflow steps in order
3. Add guardrails (minimum: no fabrication, no internal names, no system references, keep concise)
4. Define the output format with a fenced code block
5. Verify: zero em dashes, zero internal names, zero runtime references
6. Verify: frontmatter has name + description only

### Step 3: Verify the pack

Run verification on every SKILL.md:

```bash
# Check em dashes
python3 -c "
import os
em_dash = '\u2014'
for root, dirs, files in os.walk('target-dir'):
    for f in files:
        if f.endswith('.md'):
            path = os.path.join(root, f)
            with open(path) as fh:
                if em_dash in fh.read():
                    print(f'EM DASH: {path}')
"

# Check banned terms
grep -rli 'brock\|bob\|\blara\|\bneo\b\|hermes\|nemoclaw\|openshell\|claude code' target-dir/
```

### Step 4: Confirm frontmatter

Every SKILL.md must start with `---` on line 1 and close `---` after name + description. No other frontmatter fields.

### Step 5: Report counts

Report: pack name, number of skills, total across all packs, total size on disk.

## PerformOS Crew current-state reference

Before building or reporting on Crew skill packs, check `references/performos-crew-current-state.md`. It records the current catalogue source, executable folders, known count mismatch, approved full-depth Customer Support benchmark, and the missing `sales-pack-gstack-build.md` warning.

When Jared asks to continue building Crew skills, do not rely on memory counts alone. State which source of truth is being used: catalogue source, executable folder, installed folder, or architecture model.

## Pitfalls

- **Superpowers is methodology, not a skill pack.** Do not count Superpowers as a pack or a set of skills. Treat it as the standards layer underneath all Crew skills: brainstorm, plan, build with tests, debug root cause, verify, review, finish, and save or restore context.
- **Crew counts must be reconciled before quoting.** Current sources can disagree: catalogue deck source, executable build folder, installed `.claude/skills` folder, and architecture model. Always say which source is being counted before reporting totals.
- **Missing build spec files may need recreation.** A previous response referenced `/Users/jc/Desktop/sales-pack-gstack-build.md`, but it was not found during review. If Jared asks for it, recreate it from the catalogue source, the depth standard, and the full-depth Customer Support reference skills.
- **Lightweight stubs are REJECTED.** A skill that is 15-30 lines with a role statement, four bullet workflow steps, and an output format is product marketing, not an executable skill. It will not survive one real business session. Every skill must include all 14 sections from the Depth Standard. The user will reject skills that do not match G-Stack depth.
- **Product catalogue is not executable.** The 57 skills described in the PerformOS Crew catalogue are marketing material. Only skills built to the Depth Standard are executable. Do not confuse the catalogue with installed skills.
- **Do not include hooks, triggers, or allowed-tools in frontmatter.** These skills must be dependency-free and project-local. They are discovered by Claude Code automatically.
- **Do not reference G-Stack, Superpowers, or any external project in the skill bodies.** These are white-label skills for client installs.
- **Do not use em dashes anywhere.** Check with Unicode codepoint U+2014, not just grep for `---`.
- **Do not collapse multiple skills into one file.** Each skill gets its own directory with a single SKILL.md.
- **Workflow steps must be discrete numbered phases with input, action, and output gates, not a flat list of bullet points.**
- **Output format must be a fenced code block.** It is the contract between the skill and the user.

## Example skill

See `references/example-skill.md` for a complete annotated example.

## Reference install path

Skills install into `.claude/skills/` in any Claude Code project. Copy the pack directory in. Claude Code discovers them on next session start. No global install. No hooks. No repo dependency.
