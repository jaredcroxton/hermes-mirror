# Brock pipeline orchestration: zero-copy multi-agent workflows

Use this when Brock needs to run a multi-agent content pipeline (Serge → Polly → Serge → Jared) or any chain of specialist agents without Jared copy-pasting between bots.

## Why this pattern exists

Telegram bots cannot DM each other. Serge cannot send output directly to Polly. Polly cannot return review to Serge. Without orchestration, Jared becomes the human router: copy from Serge, paste to Polly, copy from Polly, paste back. That is broken.

Brock can invoke any agent profile via CLI and receive output synchronously. This turns Brock into the central router for multi-agent pipelines.

## Pattern

```
Jared → Brock (one instruction)
           → hermes --profile <agent1> chat -q "..."
           ← agent1 output
           → hermes --profile <agent2> chat -q "..."
           ← agent2 output
           → patch file (apply fixes)
           → hermes --profile <agent1> chat -q "..." (if needed)
Jared ← Brock (final deliverable)
```

## When to use this instead of send_message

`send_message` only reaches Telegram bots that have a home channel set. Jared's specialist bots (Polly, Serge) have home channels set to Jared's DM. Brock cannot `send_message` directly to those bots.

Use CLI invocation instead. It is synchronous, returns output directly, and works for any profile regardless of gateway state.

## Example: SEO content pipeline

```bash
# Step 1: Serge produces draft
hermes --profile sergeseo chat -q "Serge, apply Polly's fixes and produce the full pillar page draft for..." --quiet

# Step 2: Polly reviews draft
hermes --profile pollyperformos chat -q "Polly, final brand review of the draft at /path/to/draft.md. Read it. Check:..." --quiet

# Step 3: Brock applies Polly's fixes via patch
patch mode=replace path="/path/to/draft.md" old_string="..." new_string="..."

# Step 4: Return final to Jared
```

## Pitfalls

- **CLI timeouts.** Serge producing a full draft can take 300s+. The command may time out while Serge is still writing to disk. Check whether the output file exists and has content before assuming failure. `ls -lh` the target file after a timeout.

- **Large output truncation.** Diff output from `hermes chat -q` can be enormous when the agent edits files. The return payload may be truncated. Read the saved file directly with `read_file` rather than relying on the CLI output.

- **Don't chain more than three agents in one turn.** Each CLI invocation adds latency. Three agents (Serge → Polly → Serge) plus file patches is a realistic upper bound for one Brock response cycle.

- **Always verify file writes.** After an agent claims to have saved a file, `ls -lh` and `wc -l` the path before routing it to the next agent. Agents sometimes hallucinate file writes.

## Orchestration vs delegation

Do not confuse this with `delegate_task`. Brock is not spawning Serge as a sub-agent. Serge has his own profile, SOUL, memory, and Telegram bot. Brock invokes him as a peer specialist via CLI, receives output, and routes it forward.
