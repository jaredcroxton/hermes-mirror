---
name: agent-ecosystem-audit
category: hermes
description: Audit an agent ecosystem against the 12-Factor Agent framework, design a Thread/Event state model, and build remediation infrastructure (handoff protocol, capability registry, tool access control, metrics dashboard, eval suite).
tags: [12-factor, audit, agents, architecture, state-model, thread-model, ecosystem]
---

# Agent Ecosystem Audit (12-Factor)

When Jared asks for a full audit of the agent ecosystem against a formal framework, or wants to upgrade the ecosystem's architecture, execute the full audit pipeline. Do not give a summary. Build the artefacts.

This skill covers the full class: framework-based ecosystem audits, state model design, Thread/Event architecture, handoff protocol design, capability registry, tool access control, cost tiering, metrics, and eval test suites.

## Trigger

Use when Jared asks any of:
- "audit the agents against 12-factor"
- "how does Brock stack up against 12-factor agents"
- "upgrade the ecosystem to 12-factor"
- "design a state model for the agents"
- "build a Thread model"
- "assess every agent against this framework"
- References a specific agent-framework repo (e.g. humanlayer/12-factor-agents)

## Core principle

Do not just assess. Build. The audit produces code, not just analysis. Every weak factor gets a concrete fix. Every fix is a deliverable.

## The audit pipeline

### Phase 1: Research
1. Clone or read the framework repo. Read every factor. Read the appendix. Read the history.
2. Pull in supplementary research (Anthropic's Building Effective Agents, context engineering patterns, etc.).
3. Understand the framework as a whole before assessing anything.

### Phase 2: Assess
1. Score every active agent against every factor. Use a 4-point scale: Strong, Moderate, Weak, N/A.
2. Build a summary matrix. Identify cross-cutting patterns.
3. The assessment must name specific gaps, not generalities. "No custom context formatting" is a gap. "Could improve" is not.

### Phase 3: Design the fix
1. The fix is almost always a state model. For 12-factor agents, it's a Thread/Event model.
2. Design the core types: Thread, Event, Action. Define serialization, context building, error handling, pause/resume.
3. This is a Python module, not a diagram. It must be runnable.

### Phase 4: Build infrastructure
Build these modules in order:
1. **Thread core** (`hermes_thread.py`) — Thread, Event, Action types. Context builder. Error compaction. Pause/resume. Forking. ThreadStore.
2. **Handoff protocol** (`hermes_handoff.py`) — Structured cross-agent handoff envelopes. Validation. Pre-built templates for common handoffs.
3. **Capability registry** (`hermes_registry.py`) — Auto-discovery from SOUL files. Routing table generation. Tool access control with per-agent allow/deny lists.
4. **Metrics dashboard** (`hermes_metrics.py`) — Weekly metrics collection. Self-contained HTML dashboard. Cost tiering with 3 tiers (lightweight/standard/deep-reasoning).
5. **Eval suite** (`hermes_evals.py`) — Behavioral tests per agent. Identity, routing, source, output, error, and handoff categories. Offline structural checks.

### Phase 5: Define agent Thread flows
For every agent, define a named Thread flow: the sequence of Events that defines the agent's control flow. Include error scenarios and handoff destinations.

Format per agent:
```markdown
## AgentName — Flow Name
**Agent ID:** x
**Flow name:** x
**Steps:** N max
**Class:** specialist | orchestrator

### Event sequence
1. user_message ← ...
2. human_approval ← ...
...

### Error scenarios
| Scenario | Behavior |
|---|---|
| ... | ... |

### Handoff destinations
- **Agent:** When/why
```

### Phase 6: Save and document
1. All code modules go to `~/.hermes/hermes-agent/`.
2. All design docs go to `~/Desktop/Obsidian/AgentOS/12-factor-audit/`.
3. Agent Thread flows go to `~/Desktop/Obsidian/AgentOS/thread-integration/`.
4. An index document ties everything together.

## Deliverables checklist

After a full audit, the following must exist:

- [ ] `hermes_thread.py` — core state library (tested, all self-tests pass)
- [ ] `hermes_handoff.py` — handoff protocol (tested)
- [ ] `hermes_registry.py` — capability registry + tool access control (tested)
- [ ] `hermes_metrics.py` — metrics collector + HTML dashboard (tested, dashboard built)
- [ ] `hermes_evals.py` — eval test suite (tested)
- [ ] 12-factor-audit/00-index.md
- [ ] 12-factor-audit/01-thread-event-model.md
- [ ] 12-factor-audit/02-per-agent-assessment.md
- [ ] 12-factor-audit/03-beyond-12-factors.md
- [ ] 12-factor-audit/04-implementation-plan.md
- [ ] 12-factor-audit/05-eval-report.md
- [ ] thread-integration/thread-model-addendum.md
- [ ] thread-integration/week-N-flows.md (one per batch of agents)
- [ ] Metrics dashboard HTML at `~/Desktop/hermes_builds/agent-metrics/dashboard.html`
- [ ] Thread store populated with test threads at `~/.hermes/threads/`

## Architecture decisions baked into this skill

1. **Thread IS the state.** Not a representation. The Thread object is the single source of truth.
2. **Every interaction is an Event.** Tool calls, results, errors, human messages, approvals — all Events.
3. **Context is built from Thread.** `build_context(thread)` produces custom XML. No raw chat format.
4. **Three-strike error escalation.** 3 consecutive errors → escalate to Brock. 2 errors → use compact context.
5. **Pause/resume via serialization.** `pause_for_human()` saves Thread to disk. `resume_with_human_response()` loads and continues.
6. **Handoffs are structured envelopes.** No context lost between agents. Every handoff is auditable.
7. **Tool access is enforced per agent.** Orchestrators can delegate. Specialists cannot. Mira can generate images. Brock cannot.
8. **Cost tiering: orchestrators = expensive, specialists = cheap.** Orchestrators on GPT-4.5 (~$0.10/run). Specialists on GPT-4.1 (~$0.02/run).

## Pitfalls

- **Do not assess without building.** An audit that stops at analysis is half-done. The value is in the code.
- **Do not skip the self-tests.** Every Python module must have a `if __name__ == "__main__"` block that exercises all features.
- **Agent ID mapping is fragile.** Eval tests use short IDs (brock, harry_hr). Registry uses filename-derived IDs (brock_ceo). Always verify alignment.
- **LSP warnings about Optional types are expected.** The dataclass pattern with Optional fields triggers Pyright. Not a bug.
- **JavaScript template literals in Python f-strings need escaping.** When embedding JS inside a Python f-string for the dashboard, use string concatenation instead of template literals to avoid Python interpreting `${}`.
- **The eval suite will score low on first run.** Offline structural checks catch ID mismatches and missing policies. This is expected. Fix the mappings and rerun.

## Framework-driven audit variants

### General agent-system scoring and implementation plans

When the user asks for an audit against a published framework (12-Factor Agents, Anthropic best practices, OpenAI agent guidance, or an internal operating model), use this same audit spine but make the framework explicit at the top of the deliverable:

1. Name the benchmark/framework and source.
2. Score each agent or lane against the framework dimensions.
3. Separate **capability gaps** (missing tools, routing, memory, evals) from **governance gaps** (ownership, safety gates, handoff contracts, monitoring).
4. Produce a phased implementation plan with immediate fixes, medium-term architecture changes, and later maturity improvements.
5. Preserve user-facing clarity: executives need the scorecard and priorities; builders need the exact remediation tasks.

For jurisdictional or domain-specific audit examples such as Australian site-blocking workflows, keep the narrow domain notes in `references/` and cite them only when the task matches that domain.

## References

- `references/12-factor-agents-readme.md` — Summary of the framework from the upstream repo
- `references/anthropic-building-effective-agents.md` — Key patterns from Anthropic's agent guide
- `references/thread-model-api-reference.md` — Quick API reference for the Thread/Event model
- `references/cost-tiering-reference.md` — Model tiers, pricing, and agent assignment
- `references/agent-system-audit-au-site-blocking-patterns.md` — Domain-specific audit example absorbed from the old `agent-system-audit` skill.
