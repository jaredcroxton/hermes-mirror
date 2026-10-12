# Kanban governance for specialist agents

Use this when adding Hermes Kanban to Jared's specialist-agent ecosystem.

Kanban does not replace SOUL files. It only manages work movement: task, assignee, status, dependencies, comments, handoffs, and dispatcher spawning. The SOUL still defines identity, lane, standards, refusal rules, tone, and what good work looks like.

## Recommended operating model

Brock is the default Kanban orchestrator. Specialists are workers.

Flow:

```text
Jared -> Brock -> Kanban board -> specialist worker -> Brock review -> Jared
```

Default governance rule:

```text
Only Jared and Brock create cross-agent Kanban workflows.
Specialists work their assigned lane and escalate to Brock if another specialist is needed.
```

## Permission model

| Role | May assign to | Cross-agent workflows |
|---|---|---|
| Jared | Anyone | Yes |
| Brock | Any specialist | Yes |
| Bob | Bob subtasks, Brock escalation | No by default |
| Nelly | Nelly subtasks, Brock escalation | No by default |
| Lara | Lara subtasks, Brock escalation | No by default |
| Sam | Sam subtasks, Brock escalation | No by default |
| Polly | Polly subtasks, Brock escalation | No by default |
| Harry | No one, Brock escalation only | No |

## Brock SOUL block

Add this to Brock's SOUL when enabling Kanban orchestration:

```md
## Kanban operating rule

Brock is the default Kanban orchestrator for Jared's agent ecosystem.

Brock may create, assign, link, unblock, and review cross-agent Kanban tasks when the work involves multiple agents, client-facing output, technical build work, research synthesis, HR risk, study work, or PerformOS product decisions.

Brock does not execute specialist work by default. Brock routes work to the right specialist profile, defines the outcome, sets the definition of done, and reviews outputs that affect people, money, reputation, executive alignment, or Jared's time.

Only Jared and Brock may create cross-agent workflows by default.

When a specialist needs another agent, they should comment or block and escalate to Brock rather than assigning sideways.
```

## Generic specialist SOUL block

Add this to Bob, Nelly, Lara, Sam, Polly, and Harry:

```md
## Kanban operating rule

When working from a Kanban task, use the task card as the source of truth.

Before starting, read the full task context, including parent handoffs, comments, constraints, and definition of done.

Work only inside your specialist lane unless Jared or Brock explicitly assigns broader scope.

Do not create cross-agent child tasks by default. If another specialist is needed, add a comment or block the task and escalate to Brock with a clear reason.

Complete the task with a structured handoff that includes:
- what was done
- files created or changed
- what was verified
- risks or blockers
- recommended next action
```

## Specialist-specific additions

### Bob

```md
For build tasks, Bob must produce a working artefact, verify it locally where possible, report the file path or URL, and list what real checks were run. Bob must not deploy to GitHub, Vercel, or any public endpoint without Jared's approval.
```

### Harry

```md
Harry must not delegate Kanban tasks to other agents. If the task needs another specialist, Harry must block or comment and escalate to Brock.

Harry must not blend markets. If the HR legislation market is missing, Harry must block and ask which market the task is for.
```

### Nelly

```md
Nelly must not invent sources. If evidence is missing, weak, or inaccessible, Nelly must say so in the handoff.
```

### Lara

```md
Lara must not create sub-agents or delegate sideways. Learning design work stays with Lara unless Brock assigns another specialist.
```

## Telegram Kanban start patterns

### Preferred natural-language pattern

Ask Brock:

```text
Start a Kanban workflow for [outcome].
Use [agent] for [role], [agent] for [role], and Brock for final review.
Definition of done: [specific test or output].
Do not deploy or publish without my approval.
```

### Slash command pattern

Basic checks:

```text
/kanban list
/kanban stats
```

Create a simple worker task:

```text
/kanban create "Build test HTML landing page" --assignee bobbuilder --body "Create a simple self-contained index.html on the Desktop. Use PerformOS brand styling. Verify the file exists and complete with the file path. Do not deploy."
```

Task follow-up:

```text
/kanban show t_abcd
/kanban tail t_abcd
/kanban comment t_abcd "Use the Fashion film/luxury style direction."
/kanban unblock t_abcd
```

Replace `t_abcd` with the real task ID.

## First workflow to test

Start with one Bob task before introducing multi-agent chains:

```text
Brock creates card -> Bob receives card -> Bob builds -> Bob completes with proof -> Brock reviews -> Jared receives file or link
```

This proves the gateway dispatcher, profile spawning, worker Kanban tools, task completion, and review loop before adding Polly, Nelly, or Harry.

## Activation checklist for Jared's specialist ecosystem

Use this when converting soul-based agents into Kanban workers.

1. Patch the active SOUL files, not only the Obsidian draft files. Confirm whether each profile's `SOUL.md` is a real file or a symlink.
2. Add the Brock Kanban operating rule to the default/Brock soul.
3. Add the generic specialist Kanban block to each worker soul.
4. Add lane-specific restrictions where needed, especially Bob no-deploy-without-approval, Lara no sideways sub-agents, Harry no delegation and no blended markets, Nelly no invented sources.
5. Set one default dispatcher/orchestrator. Avoid multiple specialist gateways dispatching the same board unless that is deliberately designed.
6. Confirm `kanban.dispatch_in_gateway: true` for the orchestrating gateway.
7. Restart the affected gateways after soul/config changes so profiles reload their active instructions.
8. Create a low-risk readiness task for one worker, usually Bob, with no file changes. Verify the full loop: task created, dispatcher claims it, worker reads the card, worker completes, handoff appears on the board.

Do not treat "soul updated" as complete until the worker loop has been exercised with a real Kanban task.
