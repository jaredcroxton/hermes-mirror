# PerformOS Crew flow layer

Use this reference when Jared asks how Claude Code, named agents, Superpowers, and the project-local flow skills link together.

## Core model

- Named agents are **who**: Brock, Bob, Lara, Neo and other specialist identities with souls, roles, voices, and context.
- Skills are **how**: reusable behaviours and checkpoints that Claude Code can load during a build.
- Superpowers is the **standards layer**: planning, TDD, systematic debugging, worktrees, verification, branch finish.
- PerformOS Crew is the **role and workflow layer** inside Claude Code: product review, engineering review, design review, QA, ship, context, retro, docs, guard.
- PerformOS is the **business layer**: website, training, AgentOS, AI Work Team, client-facing outcomes.

## Plain-English skill translations

- `flow-idea-diagnostic`: should we even build this?
- `flow-plan-review-product`: is this the right thing to build for the buyer and business?
- `flow-plan-review-eng`: is this the right way to build it technically?
- `flow-plan-review-design`: will this look and feel good enough?
- `flow-review`: does the finished work have obvious issues before done?
- `flow-qa`: does the running output work like a real user would use it?
- `flow-ship`: is it safe to deploy, hand over, or move on?
- `flow-context-save`: save the current state so it can be resumed later.
- `flow-context-restore`: read the last saved handoff and resume properly.
- `flow-retro`: review the recent work and capture patterns, wins, risks, and next improvements.
- `flow-guard`: set a soft edit boundary so Claude Code does not wander.
- `flow-docs-generate`: create proper documentation.
- `flow-docs-release`: check whether documentation needs updating after changes.

## How the plan-review flows differ

### Product plan review

Skill: `flow-plan-review-product`

Plain English: is this the right thing to build?

Checks:

- who is this for?
- does the buyer care?
- is the value obvious?
- is the scope too wide?
- should we reduce, expand, hold, or selectively adjust?
- is there a sharper wedge?

Use for public pages, offers, product direction, training paths, pricing, buyer clarity, and commercial outcomes.

### Engineering plan review

Skill: `flow-plan-review-eng`

Plain English: is this the right way to build it?

Checks:

- is the architecture sound?
- is the diff too large?
- are there unnecessary abstractions?
- are tests or verification clear?
- are dependencies risky?
- is there a simpler path?

Use for code-heavy changes, integrations, dashboards, automations, agents, deployment, and multi-file edits.

### Design plan review

Skill: `flow-plan-review-design`

Plain English: will this look and feel good enough?

Checks:

- visual hierarchy
- spacing
- typography
- clarity
- premium feel
- user confidence
- whether it looks like AI slop
- what a 10 out of 10 would require

Use for websites, dashboards, landing pages, UI sections, training pages, decks, and client-facing screens.

## How it links to named agents

A named agent can use flow skills, but the flow skill is not the agent.

Example:

```text
Act as Bob.
Use flow-plan-review-eng before building.
Use flow-qa after building.
```

Meaning:

- Bob is the builder.
- The flow skills are Bob's checkpoints.

Example:

```text
Act as Brock.
Use flow-plan-review-product only.
Do not edit files.
```

Meaning:

- Brock is the strategy identity.
- The product review flow is the structure Brock uses.

## Normal high-stakes Claude Code sequence

```text
Jared gives Claude Code the task.
Claude Code uses flow-idea-diagnostic if the idea is unclear.
Claude Code writes a plan using Superpowers.
Claude Code uses flow-plan-review-product to check business fit.
Claude Code uses flow-plan-review-eng to check technical risk.
Claude Code uses flow-plan-review-design to check visual quality.
Claude Code builds the approved plan.
Claude Code uses flow-qa to test the output.
Claude Code uses flow-review to self-check the finished work.
Claude Code uses flow-ship to confirm readiness.
Claude Code uses flow-context-save if the work should be picked up later.
```

Do not run every step for tiny edits.

## Operating modes

### Fast mode

Use for small edits.

```text
Use executing-plans and verification-before-completion only.
```

### Careful mode

Use for normal builds.

```text
Use writing-plans, relevant flow-plan review, executing-plans, flow-qa, and flow-review.
```

### High-stakes mode

Use for public, client-facing, money, reputation, agents, data, or deployment work.

```text
Use flow-idea-diagnostic, writing-plans, flow-plan-review-product, flow-plan-review-eng, flow-plan-review-design, executing-plans, flow-qa, flow-review, flow-ship, and flow-context-save.
```

## Naming rule

Use **PerformOS Crew** for this adapted project-local workflow layer. Do not describe it to Jared as an external repo or external system unless provenance is specifically relevant. The external source was only the inspiration. The operating language is now PerformOS Crew.
