# Crew vs AgentOS Architecture-Stage Proposal Pattern

Use when Jared asks for a proposal, PDF, or plan comparing Crew and AgentOS while he is still working through the concept.

## Core distinction

Crew and AgentOS are separate platforms, not one product with two tiers.

- Crew = fast execution platform running in Claude Code.
- AgentOS = secure governance platform running Hermes inside NemoClaw/OpenShell.

## One soul, two runtimes

Each agent has one source-of-truth soul file. The same soul loads into either runtime.

- Crew loads the soul as a Claude Code skill or command.
- AgentOS loads the soul as a Hermes profile/skill/context inside a NemoClaw sandbox.

Do not describe this as two copies of Brock, Bob, Lara, etc. The agent identity is the same. The stadium changes.

## Architecture-stage document rule

When Jared says he is “just working it through,” remove pricing and price sections entirely.

Include:

- platform distinction
- one soul, two runtimes
- reporting line
- pipeline flow
- existing agents
- new agents needed
- gstack lessons
- audit model
- build roadmap
- risks and decisions

Exclude unless explicitly requested:

- monthly price
- setup fee
- package names based on price
- internal margin
- price comparison tables

Use neutral commercial language such as “commercial terms can be developed later.”

## Reporting line

Jared is the human owner.

Brock is the CEO-level orchestrator and reports directly to Jared.

Specialists report to Brock or to the appointed phase lead. Specialists should not route sideways by default.

## Pipeline

- Think: Brock
- Plan: Finn, Lara, Harry, Polly, Sam, Leo depending on domain
- Build: Bob, Mira, Nelly, Neo, Lara, Harry depending on artefact
- Review: Quinn
- QA/debug: Trace
- Ship: Bob or execution owner
- Retro/context: Pace
- Sign-off: Brock

## New souls needed

- Finn: architecture review and technical feasibility
- Quinn: quality inspection
- Trace: testing and debugging
- Pace: sprint state and context continuity

## PDF naming pattern

Use a clear no-pricing filename while the concept is being shaped:

`Crew-and-AgentOS-Platform-Plan-No-Pricing.pdf`

Save source markdown beside it:

`Crew-and-AgentOS-Platform-Plan-No-Pricing.md`
