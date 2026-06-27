# System Prompt Playbook — 10 Techniques from 28+ World-Class AI Tools

**Source:** x1xhlol/system-prompts-and-models-of-ai-tools (141k stars)
**Analysis:** 35 prompts from Anthropic, Google, Vercel, Cursor, Devin, Windsurf
**Published:** 27 June 2026

## The 10 Techniques

1. **Identity framing comes first.** Every prompt opens with who the agent is. Three formats: product identity, skill identity, hybrid. One sentence. Named creator. No hedging.

2. **Conciseness needs examples, not rules.** Claude Code embeds `2+2 → 4` exchanges. Only 2 of 28 tools do this. It's the single most effective technique in the repo. Show, don't describe.

3. **Formatting: pick a camp.** Prose-first (Claude Sonnet) vs markdown-first (Cursor, Antigravity). Pick one and be explicit. Emojis banned unless user uses one first (15/35).

4. **Refusal protocol: never explain why.** "Keep refusals to 1-2 sentences. Do not say what it could lead to — this comes across as preachy." (Claude Code). Devin: respond with a fixed identity string.

5. **Task management: one in_progress at a time.** Mark complete immediately. Never batch. Never mark complete with unresolved errors. Universal across 22/35 prompts.

6. **Tool-use discipline: name what NOT to use.** Devin: "NEVER use grep, use built-in search." Cursor: for every tool, name both when to use it AND when to skip it.

7. **Anti-sycophancy: rare but differentiating.** Only 5/35 prevent yes-man behavior. Claude Code: "Prioritize technical accuracy over validating the user's beliefs."

8. **Knowledge management: Antigravity KI pattern.** Most sophisticated memory architecture. KIs are curated, updateable capsules. Explicit when-to-use/when-NOT-to-use rules for context.

9. **Planning modes: separate thinking from doing.** Devin: planning vs standard mode. Antigravity: workflow files. v0: AskUserQuestions before action.

10. **File creation bias: prefer editing.** Only 3/35 encode this. Claude Code: "NEVER create files unless absolutely necessary. ALWAYS prefer editing existing files."

## Banned Phrases (from top-tier prompts)

- "Here is what I will do next"
- "Based on the information provided"
- "Let me walk you through"
- "Genuinely," "honestly," "straightforward"
- Bullet points when refusing
- Emojis unless user uses one first
- Thanking the user for tool output

## Three Immediate Steals

1. Embedded conciseness examples (3-5 exchanges, user/assistant format)
2. "No preamble" rule with named banned phrases
3. Tool negative guidance (when NOT to use each tool)

## Opportunities Nobody Exploits

- Only 2/35 embed worked examples
- Only 5/35 encode anti-sycophancy
- No prompt has a "when to escalate" rule
- Memory rules are mostly absent (Antigravity is the exception)

Full playbook: /Users/jc/Desktop/system-prompt-playbook.md
