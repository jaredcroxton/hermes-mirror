# gstack → AgentOS Architecture Mapping

Captured 14 June 2026 from full gstack repo analysis and session with Brock.

## The gstack pattern (what Garry Tan built)

23 AI specialists orchestrated through a CEO agent inside Claude Code. Each specialist is a single SKILL.md file with: name, version, triggers, allowed tools, preamble, voice philosophy, step-by-step workflow, stop points, and completion status.

Pipeline: Think → Plan → Build → Review → Test → Ship → Reflect

```
/office-hours → /plan-ceo-review → /plan-eng-review → Build → /review → /qa → /ship → /retro
```

## The AgentOS equivalent (what you build on Hermes)

Same architecture, different domain:

| gstack (code) | AgentOS (business operations) |
|---|---|
| /office-hours | Brock strategy session |
| /plan-ceo-review | Brock decision review |
| /plan-eng-review | Bob feasibility check |
| /plan-design-review | Mira design review |
| Build | Bob/Mira execution |
| /review | Sam/Nelly quality check |
| /qa | Bob testing |
| /ship | Bob deploy |
| /retro | Brock session search + memory |

## Key architectural parallels

### 1. Specialist routing triggers
gstack auto-invokes skills on keyword match ("think bigger" → /plan-ceo-review). AgentOS needs the same: "build" routes to Bob, "training" routes to Lara, "HR legislation" routes to Harry.

### 2. Cross-session context restoration
gstack has /context-save + /context-restore + decision log. Hermes has session search + memory. The gap: automated recovery at session start.

### 3. Voice embedding per specialist
gstack embeds Garry's philosophy in every skill (Boil the Ocean, anti-sycophancy rules). AgentOS embeds Jared's voice in every agent soul (short punchy sentences, no em dashes, outcomes over activity).

### 4. Multi-agent orchestration
gstack runs parallel sessions via Conductor. AgentOS can run parallel agents via Hermes profiles + NemoClaw sandboxes.

## What gstack validates for AgentOS

1. **The virtual-team model works at scale.** Garry ships at 810× productivity with 23 AI specialists.
2. **The CEO-as-orchestrator pattern is proven.** /plan-ceo-review is the most invoked skill.
3. **Clients understand the metaphor.** "Your private AI team" is the right positioning.
4. **SKILL.md is the universal agent format.** Both gstack and Hermes use it identically.
5. **Open source builds trust.** gstack is MIT. AgentOS can learn from it openly.

## Positioning AgentOS against gstack

| | gstack | AgentOS |
|---|---|---|
| Built by | Garry Tan (YC President) | Jared Croxton (PerformOS) |
| Focus | Software engineering | Business operations |
| Market | Developers, startups | Enterprise teams, L&D, HR |
| Runtime | Claude Code | Hermes + NemoClaw sandbox |
| Specialists | 23 dev roles | Brock, Lara, Bob, Harry, etc. |
| Security | Claude Code permissions | OpenShell policy + token masking |
| Audit | Session logs | Three-layer audit (gateway + sessions + policy) |
| Open source | MIT | Your IP |
| Sandbox | None | OpenShell container |

## What to clone

1. **The SKILL.md structure.** Every AgentOS specialist should follow the same format: name, triggers, allowed tools, preamble, voice, workflow, stop points, completion status.
2. **The pipeline.** Office-hours → CEO review → eng review → build → review → ship. Adapt to business operations.
3. **The routing system.** Keyword-triggered specialist invocation. Auto-route to the right agent.
4. **The context recovery.** Decision log + session search on startup.

## What NOT to clone

1. **Bun-based browser daemon.** Hermes has its own browser tools. Don't duplicate.
2. **Claude-specific commands.** Keep AgentOS Hermes-native.
3. **Code review pipeline.** Different domain. AgentOS reviews business output, not code diffs.
