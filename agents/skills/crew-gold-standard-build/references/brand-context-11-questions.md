# Brand Context 11 Questions

Finalised 27 June 2026. Replaces the earlier 12 design-heavy questions.

## Design principles

- No visual design questions. A florist or marketing person should never have to think about fonts, colours, or visual style registers. Those are gathered by the design skills at build time or scraped from the website.
- Every question must produce actionable data. Jared's test: "What outcome do you want from this question?" If you can't name the skill action it feeds, drop it. The "past agencies/tools" question was cut because it overlapped with Q3 and Q10.
- The dinner party metaphor (Q4) replaces direct voice questions. Anyone can describe how they'd show up at a dinner party. The skill translates that into tone tokens.

## The 11 questions

1. What does your business do, and why does it matter? Two sentences.

2. Who buys from you? Start with the person who pays. Then anyone else who matters. Different age, different need, different problem.

3. Why would a customer leave you? The real reason. What do customers consistently misunderstand?

4. If your business was a person at a dinner party, how would they show up? What would they wear? How would they speak? Would they arrive early to help set up, slide in late and apologetic, or exactly on time with a bottle of wine? Warm host? Quiet expert? Loud storyteller? This is your voice.

5. What's the one thing you always get right? What do customers compliment? What do they tell their friends?

6. What are you trying to achieve right now? What does success look like in six months?

7. What's your website? And where else do people find you online? URL. Social accounts. Review pages.

8. What's something unwritten that a new person would need to know? The unwritten rules. What would surprise an outsider.

9. Where do you feel you let your customers down? The gap between what you wish you could deliver and what you can reliably deliver today.

10. Is there anything I must know to get this right? Regulations. Sensitive topics. History that shapes decisions.

11. What question haven't I asked that I should have? The safety net.

## Architecture

The brand-context.md file lives at `.claude/crew-state/brand-context.md`. Every CREW skill reads it in Step 0 before its own per-skill handoff. If it exists: "Working with [brand]." If not: route to crew-core-brand-context for onboarding.

## Count-agnostic language

Never hardcode "twelve questions" or "61 skills" in skill boilerplate. Use "a few quick questions" and "every skill." Prevents breakage on every count change.
