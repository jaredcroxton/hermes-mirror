# PerformOS Crew Catalogue — white-label rules and build pattern

## The two-skill distinction (critical pitfall)

Claude Code has two completely separate things with similar names, and this confuses everyone:

### 1. Installed flow skills
These are the 13 `flow-*` skills inside `.claude/skills/`. They are executable workflow methodology. Claude Code loads them during a session and they affect behaviour. Examples: `flow-qa`, `flow-plan-review-product`, `flow-context-save`.

### 2. Catalogue skills
These are the 57 client-facing skill descriptions in the Crew Catalogue PDF. They exist only as data in `build.py` and on the PDF pages. They are NOT installed in Claude Code. They are descriptions for business owners to read, not executable skills.

When a user says "use Ticket Triage from the Customer Support Pack," Claude Code does not have that skill installed. It must either use an existing flow skill (`flow-qa`, `flow-plan-review-product`) or the user must build a new custom skill from scratch.

Never conflate catalogue descriptions with installed skills. Always check what is actually installed before telling a user a skill is available.

## White-label language rules

When building any Crew catalogue content (PDF, website, or marketing):

- **Never** use "caveman mode" — replace with Fast mode, Controlled mode, Governed mode
- **Never** use internal agent names (Brock, Bob, Lara, Neo, etc.) — replace with public role labels (Strategy agent, Build agent, Learning design agent)
- **Never** use runtime or tool names (Hermes, NemoClaw, Claude Code, OpenShell, Obsidian) in client-facing copy
- **Never** use Jared-specific examples or PerformOS business context — the catalogue must read as white-label
- **Never** use em dashes in any output
- Product names (Crew, AgentOS) are allowed only as parentheticals, never as primary labels

## Catalogue build pattern

The Crew catalogue is built as:

1. Single-source `build.py` with all skill data as Python tuples
2. `build.py` generates a static `index.html` with all slides
3. Headless Chrome renders `index.html` to PDF
4. Skills are grouped into packs (Core, Sales, Marketing, Operations, HR, Finance, Support, Documentation, Training & L&D)
5. Every skill has five fields: name, what it does, workflow steps, example use, example output
6. Cards are 3-up tall timeline format (2-up for trailing groups)
7. 16:9 slides, matte-black-on-ivory with single lime accent

## Building custom Claude Code skills from catalogue descriptions

When a user wants a catalogue skill that does not exist in the installed flow skills:

1. Confirm the catalogue skill is not an installed flow skill
2. Check if an existing flow skill can approximate it (e.g. `flow-qa` for Quality Checker)
3. If a new skill is needed, build it as a project-local SKILL.md inside `.claude/skills/`
4. Use the same frontmatter format as existing flow skills (name + description only)
5. Extract methodology from the catalogue description (what it does, workflow, example output)
6. Keep it dependency-free, no hooks, no global install
7. Document the new skill in the project README
