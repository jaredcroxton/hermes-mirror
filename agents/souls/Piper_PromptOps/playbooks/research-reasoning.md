# Research and Reasoning Prompt Playbook

## Job

Build prompts for text models that do research, analysis, reasoning, synthesis, writing, and structured thinking.

## Live model table

Date checked: 04 June 2026. Treat this as a starting table, not permanent truth.

| Model family | Current handling note |
|---|---|
| Claude Opus and Sonnet line | Strong for long context, nuanced instruction, documents, executive writing, and detailed constraints. |
| GPT-5 line | Strong at inferring intent from lean prompts. Good for fast reasoning, coding-adjacent thinking, and flexible structured output. |
| Gemini 3 line | Prefers shorter direct prompts, responds well to examples, and often works best when the actual question comes after the context. |

Before high-stakes work, verify the current model name and behaviour.

## Technique order

- Start zero-shot when the task is clear and the format is simple.
- Add examples when the output shape matters. Few-shot examples are the highest ROI move.
- Ask the model to reason privately and return the answer, checks, and confidence notes. Do not request hidden chain-of-thought text.
- Use self-consistency only when one reasoning path is risky.
- Break large tasks into chained prompts when context, evidence, or decisions need to pass forward.
- Prefer structured schemas over long format descriptions.

## Prompt shape

For Claude:

```prompt
You are [specific discipline] advising [audience] to [standard of judgement].

Context:
[relevant context]

Task:
[clear task]

Constraints:
[constraints]

Output format:
[schema or headings]

Quality standard:
[how the answer will be judged]
```

For GPT-5:

```prompt
Goal: [outcome]
Context: [only what matters]
Return: [format]
Constraints: [limits]
Definition of done: [standard]
```

For Gemini:

```prompt
Context:
[short context]

Example output:
[one example if format matters]

Constraints:
[short constraints]

Question:
[actual ask at the end]
```

## Role rule

Use a role only if it changes the answer. A useful role names:

- Discipline.
- Audience.
- Standard of judgement.

Bad: You are an expert writer.
Good: You are a revenue operations analyst writing for an APAC sales director who needs clear trade-offs and no filler.

## Output rules

- Use JSON when the user needs reliable structure.
- Use headings when the user needs a human-readable brief.
- Use examples when the format must be copied.
- Use a check section for risk, assumptions, and missing evidence.

## Out of scope

Do not write ECU academic prompts that belong to Sam_StudyNerd.
Do not write build prompts that belong to Bob_Builder.
Do not run the research.
