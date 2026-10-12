# 12-Factor Agents Framework Summary

Source: https://github.com/humanlayer/12-factor-agents
Author: Dex Horthy (HumanLayer)
License: Content CC BY-SA 4.0, Code Apache 2.0

## The 12 Factors

1. **Natural Language to Tool Calls** — Convert NL to structured tool calls. Deterministic code executes them. No magic.

2. **Own Your Prompts** — Don't outsource prompt engineering to a framework. Treat prompts as first-class code. Test them. Version them.

3. **Own Your Context Window** — Don't use only standard message-based formats. Build custom context structures (XML, YAML). Compress. Filter. "Everything is context engineering."

4. **Tools Are Just Structured Outputs** — Tools are JSON from the LLM that triggers deterministic code. LLM decides what. Code controls how.

5. **Unify Execution State and Business State** — Don't separate "where am I in the workflow" from "what has happened." The context window IS the state. Serialize it.

6. **Launch/Pause/Resume with Simple APIs** — Agents should be launchable, pausable, resumable. External triggers should work without deep integration.

7. **Contact Humans with Tool Calls** — Human contact is just another tool. Always output JSON. RequestHumanInput is a first-class intent alongside deploy_backend.

8. **Own Your Control Flow** — You decide when to loop, break, escalate, compact, retry. Not the framework.

9. **Compact Errors into Context Window** — Format errors for LLM recovery. After 3 consecutive errors, escalate. Remove resolved errors from context.

10. **Small, Focused Agents** — Don't build monoliths. 3-10 steps max. Keep context small. "As context grows, LLMs are more likely to get lost."

11. **Trigger from Anywhere, Meet Users Where They Are** — Cron, webhooks, Slack, email, SMS. Agents respond via same channels.

12. **Make Your Agent a Stateless Reducer** — (state, event) → (new_state, action). Threads are foldable. The agent is a pure function.

## Appendix

**Factor 13: Pre-fetch all the context you might need** — If you know the model will call tool X, fetch it deterministically and include the result in context. Don't waste a token round trip.

## Core agent loop

```python
initial_event = {"message": "..."}
context = [initial_event]
while True:
  next_step = await llm.determine_next_step(context)
  context.append(next_step)
  if (next_step.intent == "done"):
    return next_step.final_answer
  result = await execute_step(next_step)
  context.append(result)
```

## Key insight

"Even as models support longer and longer context windows, you'll ALWAYS get better results with a small, focused prompt and context."

The pattern that works: micro-agents sprinkled into a broader deterministic DAG.
