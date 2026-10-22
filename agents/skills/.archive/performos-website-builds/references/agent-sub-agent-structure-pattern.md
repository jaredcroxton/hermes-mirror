# Agent Sub-Agent Structure Pattern

Reusable pattern for adding sub-agents to a principal agent. Applied to Lara_LearningDesign (Rory_Research, Ava_Activities, Eva_Evaluation). Mirrors Bob_Builder's sub-agent model (Archie_Architect, Dexter_Decks, Otto_Automation, Leo_Leads, Jules_Journey, Rex_Stack).

## When to add sub-agents

Add sub-agents when:

- The principal agent's workflow has distinct craft phases that benefit from focused attention (e.g. research → activity design → evaluation)
- The principal agent is producing work where depth in a sub-speciality matters (e.g. creative activity design vs reliable Tell-Show-Do-Check)
- Jared wants the same "activate agent + sub-agents" pattern as Bob

Don't add sub-agents for:

- Tasks the principal agent can do quickly themselves
- Work that is truly one-step (no distinct phases)
- When the principal's soul already handles it well

## Naming convention

Follow Bob's pattern: `FirstName_RoleDescriptor`. Alliterative preferred.

| Principal | Sub-agent | Role |
|-----------|-----------|------|
| Bob_Builder | Archie_Architect | Architecture specs |
| Bob_Builder | Dexter_Decks | Decks |
| Bob_Builder | Otto_Automation | Automation |
| Bob_Builder | Leo_Leads | Lead-gen |
| Bob_Builder | Jules_Journey | Journeys |
| Bob_Builder | Rex_Stack | Apps |
| Lara_LearningDesign | Rory_Research | Research |
| Lara_LearningDesign | Ava_Activities | Activities |
| Lara_LearningDesign | Eva_Evaluation | Evaluation |

## What goes in the principal's soul

Add a "Sub-agents" section after the "Who [agent] is" section. Three elements:

### 1. Sub-agent table

| Sub-agent | Owns | Trigger phrases |
|-----------|------|-----------------|

The "Owns" column defines scope boundaries. The "Trigger phrases" are what Jared says that activates them.

### 2. Delegation contract

```
Brief:               the specific task
Lane:                which sub-agent
Thinker lens:        which thinkers apply
Source material:     raw content
Hard stops:          what not to skip
Return condition:    output format
```

### 3. Integration rule

"Lara never passes sub-agent output straight to Jared. She reviews it, applies her own judgement, integrates it, and delivers it as part of the full design."

This prevents the principal from becoming a pass-through. They own the final output.

## What goes in each sub-agent's soul

Four sections, one page max:

1. **Who [name] is** — identity, relationship to principal, scope boundary
2. **What [name] does** — specific tasks, with process
3. **Output format** — the standard handoff the sub-agent uses every time
4. **What [name] never does** — lane boundaries, what stays with principal or other sub-agents

## What goes in the Agent Registry

Three entries per sub-agent under the principal agent:

```
Role: [description]
Reports to: [principal]
SOUL path: /Users/jc/Desktop/Obsidian/Agents/[Name]-Soul.md
Runtime: leaf (spawned by [principal])
```

## What goes in the profile config

The principal's `~/.hermes/profiles/[profile]/config.yaml` needs:

```yaml
delegation:
  orchestrator_enabled: true
  max_concurrent_children: 3
  max_spawn_depth: 1
  child_timeout_seconds: 600
  subagent_auto_approve: false
```

If these already exist (copied from Bob's config), no changes needed. If missing, add them.

## Verification checklist

After setting up sub-agents:

- [ ] Principal soul has sub-agent table + delegation contract + integration rule
- [ ] Each sub-agent has a one-page soul file in `/Users/jc/Desktop/Obsidian/Agents/`
- [ ] Agent Registry updated with three new entries under principal
- [ ] Principal's profile config has `orchestrator_enabled: true`
- [ ] Principal's model/provider is functional (tested)
- [ ] Jared can say "activate Lara's sub-agents" or "Brock, get Lara to design X using Rory and Ava"
