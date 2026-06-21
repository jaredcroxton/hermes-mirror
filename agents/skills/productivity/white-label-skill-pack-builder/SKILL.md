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

### Locked skill template (approved gold standard)

Every PerformOS Crew skill must match G-Stack role-depth. A skill that is 15-30 lines with four bullet workflow steps is REJECTED. The approved gold standard was proven across 58 skills (9 packs, all smoke-tested green). Reference implementations: `crew-sales-lead-research` (gold standard), `crew-training-module-outline-builder` (118 lines, full Bloom/Kirkpatrick depth), `crew-docs-sop-builder` (92 lines, five step-type taxonomy with rejection paths).

The locked template has 7 mandatory sections (~85-120 lines):

1. **Frontmatter** — `name` and `description` only. name matches the folder. description has natural-language triggers, 120-400 chars.
2. **Title + role-opening paragraph** — `# Crew: Name`, then name a specific expert role, the cognitive instinct ("you work from evidence, not vibes"), who the output is for, and what the skill does NOT do.
3. **Inputs** — what the skill needs. The missing-input fork: ask once, then proceed with gaps marked. Never invent domain facts, prices, dates, or quantities.
4. **Workflow** — opens with **Step 0: Context Recovery** (read the prior handoff file or state first run), then 6-7 numbered phases expanding the catalogue bullets into a deterministic process: taxonomies/enums, decision forks, forcing questions asked one at a time, an anti-generic instruction ("name the mechanism, not the category"), and a verification penultimate step that re-reads inputs and confirms coverage before emitting. Closes with **Final Step: Handoff Save** (write the handoff file always, even with no output).
5. **Output format** — exactly ONE fenced block: the structured artifact template plus a short filled example so output looks finished.
6. **Guardrails** — "Never..." lines in three families: business risk (skill-specific fabrication bans), evidence/honesty (label inferences, name sources), house style (no em dashes, no AI-slop, specific nouns). Plus "if a project playbook exists, it wins."
7. **Handoffs** — to sibling crew skills by name and to Core standards by name (`crew-core-quality-checker`, `crew-core-context-save`, `crew-core-context-restore`). References `crew-method.md` as the methodological parent.

**Key design decisions that were proven in the 58-skill build:**

- **Context Loop over bash bridge.** The mandatory Step 0 + Final Step pair replaces bash-level context save/restore scripts. The handoff file (`.claude/crew-state/<pack>/<skill>-handoff.md`) is the bridge. It is simpler, dependency-free, and was proven functional across all 58 smoke tests.
- **Guardrails over decision briefs.** The three-family guardrail format (business risk / evidence / house style) replaces the longer decision-brief format. Every skill carries "Never invent a [price/date/threshold/role]" specific to its domain plus "label inferences" and "no em dashes."
- **Forcing questions inline.** Rather than a separate Cognitive Framework section, forcing questions live inside the numbered workflow steps where they actually gate progress.
- **Mode selection is implicit.** Fast/Careful/Governed modes are not in the skill body. They are in the buyer's project playbook or the Crew Method doc. The skill's guardrails and escalation rules enforce the right behaviour regardless of mode.
- **Completion protocol is implicit.** The Final Step Handoff Save serves as the completion marker. If the handoff file exists, the skill ran. If it does not, the skill did not complete.
- **Test fixtures are mandatory.** Every skill ships with a 3-case fixture (clean, messy, missing-input) in a `tests/` directory per pack. The `qa-check.sh` harness runs structural and functional smoke passes against these fixtures.
- **Handoff state dir is `crew-state`, not `flow-state`.** The handoff files live at `.claude/crew-state/<pack>/<skill>-handoff.md`. This separates Crew product state from internal flow development state.

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
- **Crew counts must be reconciled before quoting.** The product is currently at 62 skills across 11 packs (Web Design pack still building). Always check `references/performos-crew-current-state.md` for the latest count before quoting a number to Jared. If building additional packs, update the current-state reference afterwards so counts stay synced.
- **The locked template, not the old 14-section standard, is the build target.** The approved gold standard across all 58 skills uses 7 sections: frontmatter, role, inputs, workflow (with Step 0 + Final Step), output format, guardrails, handoffs. Do not require bash preamble, bash context bridge, or bash learnings capture. The Context Loop achieves the same result without shell dependencies.
- **Handoff state lives at `.claude/crew-state/`, not `.claude/flow-state/`.** Crew product state is separate from internal flow development state.
- **Product catalogue is not executable.** The skills described in the PerformOS Crew catalogue are marketing material. Only skills built to the locked template are executable. Do not confuse the catalogue with installed skills.
- **Install paths must be the simplest thing that works.** Three options exist: shell installer, plugin wrapper, or Claude Code file copy. When giving install instructions to a non-technical buyer, default to Claude Code file copy: "Copy every folder from ~/Desktop/Crew-Skills/01-core/ into .claude/skills/." Do not lead with terminal commands, Finder hidden-folder hunting, or drag-and-drop. The user corrected this in session: overcomplicated install paths frustrate buyers. Give the simplest path first.
- **Claude Code cannot reliably read files from the Desktop.** When handing off a build brief or spec to Claude Code, do NOT save it to `~/Desktop/` and tell Claude Code to read it from there. Desktop file delivery failed three times in one session due to iCloud sync interference and sandbox boundary issues. Instead, either: (a) paste the brief directly into the Claude Code chat (most reliable), or (b) save the file to the project directory where `.claude/skills/` already lives (e.g., `packs/10-web-design/`). The Desktop is an unreliable handoff point between Hermes and Claude Code. The project directory is reliable.
- **Lightweight stubs are REJECTED.** A skill that is 15-30 lines with a role statement, four bullet workflow steps, and an output format is product marketing, not an executable skill. Every skill must include all 7 sections from the Locked Skill Template. The user will reject skills that do not match G-Stack role-depth.
- **Do not reference G-Stack, Superpowers, or any external project in the skill bodies.** These are white-label skills for client installs.
- **Do not use em dashes anywhere.** Check with Unicode codepoint U+2014, not just grep for `---`.
- **Do not collapse multiple skills into one file.** Each skill gets its own directory with a single SKILL.md.
- **Workflow steps must be discrete numbered phases with input, action, and output gates, not a flat list of bullet points.**
- **Output format must be a fenced code block.** It is the contract between the skill and the user.

## Example skill

See `references/example-skill.md` for a complete annotated example.

## Reference install path

Skills install into `.claude/skills/` in any Claude Code project. Copy the pack directory in. Claude Code discovers them on next session start. No global install. No hooks. No repo dependency.
