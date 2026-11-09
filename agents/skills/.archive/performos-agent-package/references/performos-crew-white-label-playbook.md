# PerformOS Crew White-Label Playbook Pattern

Captured: 15 June 2026

## Core distinction

PerformOS Crew is the role and workflow rhythm layer for Claude Code. It should be positioned as a portable operating model, not as the external repo it was adapted from.

Use this language:

- Superpowers = standards layer
- PerformOS Crew = roles and workflow rhythm
- Business Context Layer = client-specific context, constraints, brand, risks, and outcomes

Do not frame Layer 3 as "PerformOS is the business layer" when discussing white-label or client installs. PerformOS supplies the AI work team structure. The client business layer supplies the context.

## Named agents vs flow skills

Explain the system like this:

- Named agents are who does the work. They have souls, voice, role, memory/context, and sometimes a Hermes profile or bot.
- Flow skills are how Claude Code does the work. They are reusable lenses, gates, and workflow steps.
- Claude Code is the workshop.
- Hermes is the command centre.

Plain-English line:

> Agents are who. Skills are how. Flow skills are the steps Claude Code takes so the work does not become random.

## Installed PerformOS Crew skills

The adapted project-local skills are:

1. flow-idea-diagnostic
2. flow-plan-review-product
3. flow-plan-review-eng
4. flow-plan-review-design
5. flow-review
6. flow-qa
7. flow-ship
8. flow-retro
9. flow-context-save
10. flow-context-restore
11. flow-guard
12. flow-docs-generate
13. flow-docs-release

The external full system has about 59 skills. Jared's adaptation keeps 13 dependency-free role/workflow skills and skips global state, browser binaries, telemetry, auto-update, heavy deploy automation, and duplicated debugging flows.

## White-label Layer 3 wording

Use this wording in playbooks and client-facing strategy docs:

### Layer 3: Business Context Layer

The Business Context Layer defines what the AI work team is working on and why it matters.

It answers:

- What business are we supporting?
- Who are the users or customers?
- What outcomes matter?
- What brand voice should be used?
- What workflows should the AI team support?
- What systems can the AI team access?
- What privacy, approval, and risk rules apply?
- What does success look like commercially?

In the PerformOS environment, this includes the PerformOS website, AI Work Team positioning, AgentOS, training products, client dashboards, private AI teams, and secure AI deployment.

In a white-label client environment, this becomes the client's brand, products, services, workflows, approved tools, risk level, and success measures.

Examples:

- Law firm: client intake, matter summaries, compliance boundaries, legal review steps, document workflows.
- Real estate agency: lead capture, listing copy, buyer follow-up, appraisal workflows, campaign reporting.
- Training business: course content, learner journeys, assessments, facilitator guides, sales funnels.

## Playbook PDF pattern

When Jared asks for a playbook PDF:

1. Update the source markdown first so the wording is correct and white-label ready.
2. Render a polished PDF.
3. Deliver with `MEDIA:<absolute path>`.
4. Keep the markdown source in Obsidian as the source of truth.
5. Verify the source has zero em dashes.

Known source file from this session:

- `/Users/jc/Desktop/Obsidian/PerformOS/PerformOS-Crew-Playbook.md`
- `/Users/jc/Desktop/Obsidian/PerformOS/PerformOS-Crew-Playbook.pdf`

## Best-practice operating modes

- Fast mode: small edits. Use executing-plans and verification-before-completion.
- Careful mode: normal builds. Use writing-plans, relevant PerformOS Crew review, executing-plans, flow-qa, and flow-review.
- High-stakes mode: public, client-facing, money, security, agents, or deployment. Use idea diagnostic, product/engineering/design review, QA, review, ship, and context save.

Rule: small task, few gates. Big task, more gates. Public or client-facing, full gates.
