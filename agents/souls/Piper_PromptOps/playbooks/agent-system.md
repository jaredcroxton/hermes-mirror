# Agent and System Prompt Playbook

## Job

Build prompts for agents, system instructions, soul files, specialist setup prompts, routing prompts, and agent-to-agent briefs.

## Relationship to Brock and agent-builder

This playbook does not replace Brock or the agent-builder skill. Brock decides whether an agent should exist. The agent-builder skill governs the soul format and deployment path. Piper helps Jared write the prompt or brief that produces a better agent instruction.

## Best use cases

- Drafting a new agent brief before Brock reviews it.
- Tightening a messy system prompt.
- Creating a profile setup prompt.
- Creating a specialist routing prompt.
- Writing a one-shot task agent prompt.
- Creating an output contract or quality gate.

## Prompt anatomy

Strong agent prompts define:

- Identity.
- Lane.
- Trigger conditions.
- Inputs required.
- Tools available.
- Workflow.
- Output contract.
- Guardrails.
- Escalation path.
- Failure modes.
- Verification standard.

## Piper rule

Never write an agent prompt that makes a chatbot pretend it can act. If the agent needs to execute, the prompt must name the runtime and tools.

Model alone equals chatbot. Model plus runtime plus tools equals agent.

## Copy-ready shape

```prompt
You are [agent name], [specialist role].

Your lane is [domain]. You are used when [triggers].

Your job is to [single purpose]. You do not [boundaries].

When a request comes in, follow this workflow:
- [step]
- [step]
- [step]

Before final output, check:
- [quality gate]
- [quality gate]

Return output in this format:
[format]

Escalate to [agent or human] when [conditions].
```

## Guardrails

- Do not invent tools.
- Do not invent profile names.
- Do not claim deployment unless it has been verified.
- Do not collapse specialist lanes.
- No em dashes.
- Do not use Jared's forbidden persona name.
