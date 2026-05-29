---
name: explain-tech-to-non-technical
description: When Jared asks to explain a technical concept, system, or agent workflow in plain English for someone who is not technical (family, clients, executives). Strip jargon, use real-world analogies, and structure explanations so a novice can follow and relay the information to others.
tags: [communication, explanation, plain-english, non-technical, analogies]
---

# Explain Tech to Non-Technical

## Trigger
Use when Jared says any of the following:
- "explain easy" / "explain simply" / "break this down"
- "explain it to [person] who is not technical"
- "rewrite this so [person] can understand"
- "dumb it down" / "novice version"
- "how do I explain this to [person]"

Also use whenever Jared passes a technical explanation and says "this is for [person]."

## Core rules

1. **Strip all jargon.** No tokens, no context windows, no FTS5, no dependencies, no caching, no plugins — unless you immediately translate each one into a real-world analogy.

2. **Use analogies drawn from Jared's world:**
   - Gym / fitness equipment / training routines
   - Business outcomes (revenue, sales, staff)
   - Cars, tools, machines anything physical and tactile
   - Phone apps (everyone understands apps on a phone)

3. **Structure:**
   - One short paragraph per concept
   - Bold the key relationship or takeaway
   - Use comparison tables only if they are simple two-column (concept vs analogy)
   - Short sentences. Active voice. No em dashes.

4. **Answer the "why does this matter?" question** for every concept. The non-technical person needs to know why they should care before they absorb what it is.

5. **Anticipate follow-up.** Plain English explanations invite "but why?" and "how does that work?" — be ready to go one level deeper without reintroducing jargon.

6. **If explaining architecture or a workflow:** Use the specialist/agent analogy consistently. Brock = head office. Agents = specialist employees. Skills = instruction manuals. Soul files = personality and rules. Models = the engine. Tokens = phone minutes.

## Pitfalls

- Do not assume the reader understands what a "database" means. Say "a filing cabinet on his computer."
- Do not say "the AI reads context." Say "the AI looks through everything saved from past conversations before answering."
- Do not list features without saying what each one lets a real person actually do.
- Do not hedge with "essentially" or "basically." Just say it directly.

## Output format

1. Brief one-line summary of what we are explaining
2. Each concept as its own short section with a clear heading in plain English
3. The analogy right after the definition
4. A "why this matters" line at the end of each section

## References

See `references/hermes-glossary.md` for a running list of technical terms and their plain-English translations. Update it as new terms come up in sessions.
