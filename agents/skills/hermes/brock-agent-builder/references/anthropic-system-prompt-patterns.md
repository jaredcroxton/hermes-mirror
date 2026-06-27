# Anthropic System Prompt Patterns — Agent Soul Design Reference

**Source:** Claude Code 2.0 and Claude Sonnet 4.6 system prompts, extracted June 2026.
**Repo:** x1xhlol/system-prompts-and-models-of-ai-tools (141k stars, 28+ tools)

## 1. Embedded conciseness examples (Claude Code 2.0)

Instead of saying "be concise," Anthropic embeds exact example exchanges:

```
user: 2 + 2
assistant: 4

user: is 11 a prime number?
assistant: Yes

user: what command should I run to list files in the current directory?
assistant: ls
```

**Application:** When designing an agent soul, include 2-3 embedded example exchanges that demonstrate the exact tone and verbosity you want. This trains the model more effectively than abstract rules.

## 2. No-preamble/postamble rule (Claude Code 2.0)

Explicitly ban these patterns by naming them:
- "Here is what I will do next…"
- "Based on the information provided…"
- "Let me walk you through…"
- "I'll help you with that…"

**Application:** Add a "Banned openers" section to agent souls. Name the phrases. One line each. Agents should start responses with the answer, not the meta-commentary.

## 3. Refusal protocol (Claude Code 2.0)

> "If you cannot or will not help the user with something, please do not say why or what it could lead to, since this comes across as preachy and annoying."

- Keep refusals to 1-2 sentences
- Offer helpful alternatives if possible
- Never explain the reasoning behind the refusal

**Application:** Every agent soul's Guardrails section should include a refusal protocol. No long explanations. No "I can't do that because…" paragraphs. One sentence, then redirect.

## 4. Anti-sycophancy stance (Claude Code 2.0)

> "Prioritize technical accuracy and truthfulness over validating the user's beliefs. Provide direct, objective technical information. Apply rigorous standards and disagree when necessary."

**Application:** For technical or advisory agents, explicitly state they must disagree when the user is wrong. This is especially relevant for Brock (CEO agent) and any review/gate agents.

## 5. Single in-progress task (Claude Code 2.0)

> "It is critical that you mark todos as completed as soon as you are done with a task. Do not batch up multiple tasks before marking them as completed. Exactly ONE in_progress at a time."

**Application:** Already Jared's operating pattern. Structural confirmation from Anthropic. Can be cited when designing task-management sections of agent souls.

## 6. File-creation bias (Claude Code 2.0)

> "NEVER create files unless they're absolutely necessary for achieving your goal. ALWAYS prefer editing an existing file to creating a new one. NEVER proactively create documentation files (*.md) or README files."

**Application:** For build agents (Bob_Builder class), this is a useful guardrail. Prefer editing over creating. No docs unless asked.

## 7. Temporal persona framing (Claude Sonnet 4.6)

> "It answers questions the way a highly informed individual in August 2025 would if they were talking to someone from Wednesday, March 04, 2026."

Grounds the model in a specific temporal persona without saying "your knowledge cutoff is X." More human and natural.

**Application:** When designing agent souls with knowledge boundaries, frame them as a persona talking to someone at a specific date rather than stating a cutoff. Example: "I know the Accor Plus sales process as it stood in June 2026."

## 8. Search discipline (Claude Sonnet 4.6)

- 1-6 word queries for best results
- Start broad (1-2 words), then narrow
- Never use `-` operator, `site` operator, or quotes unless explicitly asked
- 1 call for single facts → 5-10 for deeper research → 20+ means suggest a different approach

**Application:** For agents with web search capability, encode these query rules. Short and broad first. No operators unless asked.

## What NOT to copy

- **The formatting minimalism.** Claude Sonnet 4.6 defaults to prose paragraphs and avoids bullets. Jared's agents have brand voices with specific formatting preferences. Don't override those.
- **The conversational warmth rules.** Anthropic's "warm tone, avoid saying genuinely/honestly" is model-level politeness, not agent-design strategy. Ignore for specialist agents.
- **The safety scaffolding.** Child safety, weapons, biometrics — these are platform-level constraints Anthropic embeds. Not relevant to domain-specific agent souls.
