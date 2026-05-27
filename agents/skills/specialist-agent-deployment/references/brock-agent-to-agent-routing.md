# Brock agent-to-agent routing pattern

When Jared needs a multi-agent workflow, he should not copy-paste between Telegram bots. Brock receives one instruction and runs the full pipeline.

## How it works

```
Jared → Brock (one instruction)
           → Agent A (via CLI: hermes --profile <a> chat -q "...")
           ← Agent A output
           → Agent B (via CLI: hermes --profile <b> chat -q "...")
           ← Agent B output
           → Agent A (apply fixes, continue)
           ← Agent A final output
Jared ← Brock (final deliverable, no copy-paste required)
```

## When to use

- Multi-step SEO content pipeline (Serge → Polly → Serge)
- Build-and-review workflows (Bob builds, Brock reviews)
- Any workflow requiring two or more specialist agents in sequence

## Why CLI, not Telegram

Telegram bots cannot DM each other. Attempting send_message to a specialist bot's Telegram channel will fail or not route correctly. The `hermes --profile <name> chat -q "..." --quiet` pattern is the reliable agent-to-agent path.

## Pitfalls

- DeepSeek profiles may time out on 300s CLI calls during heavy output. The agent may still save its work to disk before the timeout. Check for the output file after a timeout before retrying.
- Always verify the file saved correctly after a timeout (ls -lh, wc -l) before routing to the next agent.
- The consultation pattern (Serge → Polly review) produces a handoff prompt. Polly does not need the full context. Give her the file path and specific checks.
