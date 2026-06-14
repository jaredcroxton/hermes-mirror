# Crew and AgentOS dual-runtime agent pattern

Use this when Jared discusses cloning gstack, building Crew, building AgentOS, or asking whether Claude Code and Hermes/NemoClaw need separate agents.

## Core answer

One agent soul can run in two runtimes.

```text
Canonical Obsidian soul
/Users/jc/Desktop/Obsidian/Agents/<Agent>-Soul.md
        │
        ├── Crew loads it as a Claude Code skill/task-agent instruction
        └── AgentOS loads it as a Hermes profile inside NemoClaw/OpenShell
```

Do not create duplicate agents with different names just because the runtime is different. The agent identity remains the same; the wrapper changes.

## Product distinction

- **Crew** = fast orchestration platform. Runs the agent pipeline in Claude Code. Best for speed, builds, dashboards, content, and high-trust teams.
- **AgentOS** = secure governed platform. Runs the same agent souls in Hermes + NemoClaw/OpenShell. Best for enterprise, policy gates, audit trails, token masking, and per-user sandbox isolation.

The difference is not the agent. It is the runtime, security layer, and buyer promise.

## Reporting line pattern

Brock remains the only direct report to Jared. Other agents report to Brock or a phase lead.

```text
Jared
  └── Brock (CEO/orchestrator)
        ├── Planning specialists: Finn, Lara, Harry, Polly, Sam, Leo
        ├── Build specialists: Bob, Mira, Nelly, Neo
        ├── Review gate: Quinn
        ├── QA/debug gate: Trace
        └── Sprint/context state: Pace
```

## gstack-inspired pipeline

Mirror the gstack separation of narrow roles. Do not overload Brock and Bob with every hat.

```text
THINK      Brock
PLAN       Finn / Lara / Harry / Polly / Sam / Leo
BUILD      Bob / Mira / Nelly / Neo
REVIEW     Quinn
QA/DEBUG   Trace
SHIP       Bob
RETRO      Pace
SIGN-OFF   Brock
```

## New souls likely needed for Crew

When adapting gstack to Jared's ecosystem, avoid renaming existing agents. Add only the missing narrow roles:

- **Finn** — architecture and feasibility review. “Will this build work?”
- **Quinn** — quality inspection. “Is the output complete, sourced, formatted, link-safe, and ready?”
- **Trace** — testing and debugging. “Why did it fail and what proves it works now?”
- **Pace** — sprint state, context restore, after-action summary. “Where are we and what happened last session?”

Existing souls remain: Brock, Bob, Lara, Harry, Polly, Nelly, Sam, Mira, Neo, Leo.

## Pitfall from the gstack discussion

Do not explain Crew and AgentOS as if they are two separate sets of agents. Jared found that confusing. Say:

> Same souls. Two runtimes.

If asked why the agent names are the same, answer:

> Brock is still Brock. Lara is still Lara. Crew runs them fast in Claude Code. AgentOS runs them securely in NemoClaw.

## Build order recommendation

1. Clone/study gstack in Claude Code to learn the SKILL.md role pattern.
2. Build the four missing souls: Finn, Quinn, Trace, Pace.
3. Patch Brock routing so he calls the right phase roles.
4. Test Crew on PerformOS work first.
5. Only then port the same souls into AgentOS/NemoClaw.

## Naming rule

Do not call both products AgentOS.

- Claude Code version: **Crew**
- NemoClaw/OpenShell version: **AgentOS**

Crew is the pipeline. AgentOS is the secured operating environment.
