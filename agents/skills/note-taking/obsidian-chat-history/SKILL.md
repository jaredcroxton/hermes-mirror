---
name: obsidian-chat-history
description: Save Hermes agent conversations into Jared's Obsidian vault under Chat History. Use whenever Jared asks to save, archive, remember, export, or preserve a chat history, and at the end of meaningful agent conversations when practical.
version: 1.0.0
author: Brock / Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [obsidian, chat-history, transcript, archive, sessions, agents]
---

# Obsidian Chat History

## Purpose

Save every meaningful chat with Jared into his Obsidian vault so agent work is searchable, auditable, and recoverable.

Target vault folder:

`/Users/jc/Desktop/Obsidian/Chat History`

Default folder pattern:

`/Users/jc/Desktop/Obsidian/Chat History/YYYY-MM-DD HHMM - <Agent or Profile> - <Short Topic>/`

Default file inside that folder:

`Transcript.md`

## Trigger

Use this skill when:

- Jared asks to save or archive a chat history.
- Jared asks for conversation history to appear in Obsidian.
- A specialist agent finishes a meaningful work session and has enough context to preserve the exchange.
- The chat contains decisions, strategy, build outputs, legal or HR reasoning, study work, product work, or reusable instructions.

For tiny exchanges with no durable value, do not create noise unless Jared explicitly asked for every exchange to be captured.

## Required Output Shape

Create one folder per chat/session under `Chat History`.

Inside `Transcript.md`, use this structure:

```markdown
---
type: chat-history
agent: <agent name>
profile: <profile name if known>
platform: <Telegram / CLI / other>
date: DD Month YYYY
time: HH:mm
session_id: <session id if known>
topic: <short topic>
---

# <Short Topic>

## Summary
- <three to seven bullets capturing what mattered>

## Decisions
- <only durable decisions, if any>

## Actions / Outputs
- <files created, agents routed, tasks done, if any>

## Full Chat Transcript

### User
<message>

### Assistant
<reply>
```

## Procedure

1. Confirm the Obsidian target folder exists:
   - `/Users/jc/Desktop/Obsidian/Chat History`
2. Create a new child folder for the chat using the folder pattern above.
3. Save `Transcript.md` using the required output shape.
4. Preserve Jared's words exactly where available.
5. Preserve assistant outputs exactly where available, except do not duplicate huge tool logs unless they are decision-critical.
6. If the full transcript is not available in the active context, save the visible/recoverable portion and include this note under Summary:
   - `Transcript scope: partial, based on active session context available to the agent.`
7. Do not save secrets, tokens, private auth logs, or raw `.env` content into Obsidian.
8. If a tool output contains sensitive operational logs, summarise the result instead of pasting raw output.
9. After writing, verify the file exists and report the exact path.

## Naming Rules

- Use dates as `DD Month YYYY` inside the note.
- Use filesystem folder names as `YYYY-MM-DD HHMM - Agent - Topic` so they sort correctly.
- Keep topic under eight words.
- Replace slashes, colons, and unsafe filename characters with hyphens.

## Agent Behaviour

When this skill is active, the agent should treat chat-history capture as a closing discipline:

- Finish the user's actual work first.
- Then save the chat if it was meaningful or Jared asked for capture.
- Keep the final note concise: `Saved to: <path>`.

Do not let archiving become the main task unless Jared specifically asks for it.

## Verification

After saving, verify with a file existence check. If verification fails, fix the path and retry once.

## Multi-profile rollout

When Jared asks for this capture standard to apply across specialist agents, use the rollout notes in `references/multi-profile-rollout.md`.

Core rule: keep this as one class-level skill and distribute the full skill directory to each profile. Do not create separate narrow chat-history skills for each agent.

## Limits

This skill is a procedure for agents. It is not a background recorder by itself. True automatic capture after every message requires a Hermes gateway/session hook or scheduled exporter that reads the session store and writes new sessions to Obsidian.
