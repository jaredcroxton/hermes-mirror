# Cross-Agent Orchestration via Terminal CLI

Brock can run full multi-agent pipelines by invoking specialist profiles directly via `hermes --profile <name> chat -q "..." --quiet`. This eliminates the Telegram copy-paste bottleneck (Serge → Jared → Polly → Jared → Serge) and replaces it with: Serge → Brock → Polly → Brock → apply fixes → Jared.

## When to use

- The pipeline involves two or more specialist agents
- Jared is currently the manual router between agents
- The job is repeatable and follows a known sequence (research → review → fix → confirm)

## Pattern

```
hermes --profile <agent1> chat -q "<instruction with file paths>" --quiet 2>&1
hermes --profile <agent2> chat -q "<review instruction referencing agent1 output>" --quiet 2>&1
patch <fixes agent2 requested>
hermes --profile <agent2> chat -q "Confirm the fixes." --quiet 2>&1
```

## Key rules

- Always pass exact file paths so the agent can read previous output
- Timeout generously — SEO/content agents may need 300s
- If the CLI output shows `┊ review diff`, the agent is actively writing files — do not interrupt
- Check file existence after timeout: the agent may have saved even if the CLI session timed out
- Polly reviews best when given specific checks: em dashes, tools/solutions/suite, Australian spelling, product names, commercial framing
- When Polly returns fixes, apply them via `patch` tool directly, then ask Polly to confirm

## Pipeline that works

1. Serge produces keyword briefs → saves to `/SEO/`
2. Brock routes to Polly for brand review
3. Polly returns approved or with fixes
4. Brock applies fixes via patch
5. Serge produces article briefs from approved keyword brief
6. Brock routes to Polly again
7. Polly reviews, Brock applies fixes, Polly confirms
8. Jared gets the final output

## Pitfalls

- 300s timeout is common for SEO agents doing research + file writes. The output may be in the diff but truncated. Always check `ls -lh` on the target file.
- Polly's brand checks must include COPY.md alignment ($500-$5,000/month, "instruments" not "tools", "catalogue" not "suite", "Try it free. Buy it once. Own it forever.")
- DeepSeek may return empty on overloaded context. Retry with shorter prompt if first attempt times out.
