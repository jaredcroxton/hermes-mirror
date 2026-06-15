# Project-local Superpowers and G-Stack Adaptation

Captured after Jared prepared to give Claude Code the Superpowers and G-Stack repos for the `/Users/jc/Desktop/cluade` project. Use this when prompting Claude Code, Codex, OpenCode, or another coding agent to install/adapt workflow frameworks without contaminating the whole machine.

## Core distinction

- **Superpowers = standards layer.** Planning, TDD, systematic debugging, git worktrees, subagent-driven development, code review, verification before completion, and finishing branches.
- **G-Stack = role workflow layer.** CEO review, engineering review, design review, QA, ship/release, investigate, retro, context save/restore, guard/freeze/unfreeze.
- **PerformOS = product/business layer.** Existing agents, public website, Obsidian souls, Hermes profiles, and NemoClaw config remain authoritative.

## Safe install principle

Never ask a coding agent to "install globally" first. Start with a project-local vendor/adaptation:

- Keep changes inside the project, e.g. `.claude/skills/`, `.claude/commands/`, `.claude/gstack/`, or `docs/`.
- Do not add SessionStart hooks unless the user explicitly approves after seeing the diff.
- Do not overwrite `CLAUDE.md`, `AGENTS.md`, settings, hooks, PerformOS website files, Hermes profiles, Obsidian agent soul files, Telegram bots, or NemoClaw config without explicit approval.
- Treat global plugin installs as opt-in only.

## Superpowers prompt pattern

Use this shape when asking Claude Code to adapt Superpowers:

```text
Review https://github.com/obra/superpowers and install/adapt it as a development workflow layer for this project.

Goal:
Use Superpowers to improve planning, TDD, verification, code review, git worktree usage, and completion discipline.

Important:
Do not replace existing PerformOS agents, roles, souls, skills, or site structure.
Do not overwrite existing CLAUDE.md, AGENTS.md, or project instructions without showing me the diff first.
Do not globally install anything that changes my whole machine without asking.
Apply Superpowers only to this project/workspace first.

What I want:
1. Inspect the repo and explain what parts are useful.
2. Identify the safest install path.
3. Add only the parts that improve brainstorming, planning, TDD, systematic debugging, worktrees, subagent-driven development, code review, verification, and finishing branches.
4. Preserve the current PerformOS website and agent ecosystem.
5. After installing/adapting, show changed files, what was added, risks, and day-to-day use.
```

## G-Stack prompt pattern

Use this shape after Superpowers is installed or vendored:

```text
Caveman mode on. Careful multi-step safety-gated task.

Task:
Review https://github.com/garrytan/gstack and adapt only the useful parts into this project as a project-local role workflow layer.

Context:
Superpowers has already been safely vendored into this project as the standards layer.

Goal:
Use G-Stack as the role workflow layer, not as a replacement for Superpowers.

Superpowers = standards.
G-Stack = roles and workflow rhythm.
PerformOS = the product and business layer.

Important guardrails:
1. Do not globally install G-Stack.
2. Do not overwrite existing project files without showing me the diff first.
3. Do not overwrite or create CLAUDE.md, AGENTS.md, settings.json, hooks, or commands without approval.
4. Do not replace existing PerformOS agents, roles, souls, skills, site structure, or naming system.
5. Do not expose internal agent names on public website pages.
6. Do not touch Hermes profiles, Obsidian agent soul files, Telegram bots, or NemoClaw config.
7. Do not modify the PerformOS website unless explicitly approved.
8. Keep everything project-scoped first.
9. If anything wants to be installed globally, stop and ask.

What I want you to do first:
1. Inspect the G-Stack repo.
2. Inspect this local project.
3. Compare G-Stack against the Superpowers skills already installed.
4. Identify what G-Stack adds that Superpowers does not.
5. Identify what would conflict with Superpowers.
6. Identify the safest project-local adaptation path.
7. Do not write files until you present the plan.

Focus on:
office-hours, plan-ceo-review, plan-eng-review, plan-design-review, design-review, design-shotgun, review, qa, qa-only, investigate, ship, land-and-deploy, retro, context-save, context-restore, guard, freeze, unfreeze, document-generate, document-release.

Stop with:
Approve this project-local G-Stack adaptation plan?
```

## G-Stack to PerformOS-safe mapping

- `office-hours` / `plan-ceo-review` → strategy review
- `plan-eng-review` → architecture review
- `plan-design-review` / `design-review` / `design-shotgun` → design quality review
- `review` → code and quality review
- `qa` / `qa-only` → QA and verification
- `investigate` → debugging and root-cause investigation
- `ship` / `land-and-deploy` → release readiness
- `retro` → retrospective and learning capture
- `context-save` / `context-restore` → project memory and handoff
- `guard` / `freeze` / `unfreeze` → safety controls before risky changes
- `document-generate` / `document-release` → documentation and release notes

## Pitfalls

- Do not let G-Stack duplicate or override Superpowers. If a workflow is already a standards skill, keep Superpowers as the source of truth.
- Do not import G-Stack identity wholesale. Borrow role patterns, not public naming.
- Do not expose internal agent names on public website copy.
- Do not confuse project-local Claude Code workflow files with Hermes profiles or Obsidian agent souls.
- Do not let a coding agent write immediately when the task is an adaptation plan. The correct first output is an inspection report and approval gate.
