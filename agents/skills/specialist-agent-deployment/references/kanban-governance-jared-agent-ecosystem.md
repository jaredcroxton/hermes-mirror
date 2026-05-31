# Kanban governance for Jared's specialist agent ecosystem

Use this when setting up or maintaining Jared's profile-backed specialist agents with Hermes Kanban.

## Operating model

Jared uses Brock as the default Kanban orchestrator. Specialist agents keep their souls and lanes. Kanban is the durable work board, not the identity layer.

Default flow:

```text
Jared
↓
Brock
↓
Kanban board
↓
Specialist agent
↓
Brock review when people, money, reputation, executive alignment, or Jared's time is affected
↓
Jared
```

## Governance rule to add to Brock

```md
## Kanban operating rule

Brock is the default Kanban orchestrator for Jared's agent ecosystem.

Brock may create, assign, link, unblock, and review cross-agent Kanban tasks when the work involves multiple agents, client-facing output, technical build work, research synthesis, HR risk, study work, or PerformOS product decisions.

Brock does not execute specialist work by default. Brock routes work to the right specialist profile, defines the outcome, sets the definition of done, and reviews outputs that affect people, money, reputation, executive alignment, or Jared's time.

Only Jared and Brock may create cross-agent workflows by default.

When a specialist needs another agent, they should comment or block and escalate to Brock rather than assigning sideways.
```

## Generic specialist rule

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

## Specialist additions

### Bob_Builder

```md
For build tasks, Bob must produce a working artefact, verify it locally where possible, report the file path or URL, and list what real checks were run. Bob must not deploy to GitHub, Vercel, or any public endpoint without Jared's approval.
```

### Nelly_Notebook

```md
Nelly must not invent sources. If evidence is missing, weak, or inaccessible, Nelly must say so in the handoff.
```

### Lara_LearningDesign

```md
Lara must not create sub-agents or delegate sideways from Kanban. Learning design work stays with Lara unless Brock assigns another specialist.
```

### Sam_StudyNerd

```md
Sam stays in the study and academic synthesis lane. If a Kanban task requires product strategy, build execution, HR legislation, or commercial judgement, Sam escalates to Brock.
```

### Polly_PerformOS

```md
Polly stays in the PerformOS product, positioning, brand, offer, and feature strategy lane. If build execution, source research, HR legislation, or academic work is required, Polly escalates to Brock.
```

### Harry_HR

```md
Harry must not delegate Kanban tasks to other agents. If the task needs another specialist, Harry must block or comment and escalate to Brock.

Harry must not blend markets. If the HR legislation market is missing, Harry must block and ask which market the task is for.
```

## Config pattern

For Jared's current setup, use one dispatcher through the default/Brock gateway.

```yaml
kanban:
  dispatch_in_gateway: true
  orchestrator_profile: default
```

Specialist profiles should not each run their own dispatcher by default. Keep specialist gateway dispatcher settings off to avoid duplicate dispatchers competing.

## Verification pattern

After setup, create a low-risk readiness card for Bob:

```bash
hermes kanban create "Kanban readiness check for Bob" \
  --assignee bobbuilder \
  --body "Read this Kanban task, confirm you are Bob_Builder, make no file changes, and complete with a structured handoff showing the Kanban worker loop is functioning. Definition of done: task completed with summary only." \
  --tenant setup \
  --priority 100 \
  --max-runtime 3m \
  --json
```

Expected verified loop:

```text
task created
↓
dispatcher claimed it
↓
Bob spawned
↓
Bob read the card
↓
Bob completed the task
↓
Kanban recorded the handoff
```

## Telegram usage pattern

Jared can start a workflow naturally through Brock:

```text
Start a Kanban workflow for the PerformOS website.
Use Polly for positioning, Bob for build, and Brock for final review.
Do not deploy without approval.
```

Or directly with slash commands:

```text
/kanban create "Build PerformOS Private AI Team website" --assignee bobbuilder --body "Build one self-contained cinematic HTML file using the PerformOS brief and brand styles. Verify locally. Do not deploy."
```

## Pitfalls

- Kanban does not replace agent souls. Souls define lane and behaviour. Kanban assigns and tracks work.
- Do not let specialists freely delegate sideways. They should comment or block and escalate to Brock.
- Always use real profile names. Unknown assignees sit ready and never spawn.
- For client-facing or commercial work, include a Brock review task as a gate before Jared uses the output.
- For build work, include explicit no-deploy-without-approval language.
