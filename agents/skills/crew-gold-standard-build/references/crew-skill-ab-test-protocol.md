# Crew Skill A/B Test Protocol

## When to use

Jared wants to answer: "Are my Crew skills actually producing the quality, or is Claude's base model already this good?" This protocol isolates the variable.

## The core question

When Claude Code builds something beautiful using Crew skills, there are two possible explanations:
1. The Crew skill is providing real design direction, locked templates, quality gates, and anti-pattern knowledge
2. Claude's base model is already capable of producing that quality — the skill is along for the ride

This test answers which one is true.

## Protocol

### Setup

- **Hardware:** Mac Mini with zero cloud-synced Claude skills. No Anthropic skills plugin signed in. Clean environment.
- **Claude Code version:** Same binary for both runs.
- **Two runs, same prompts, one variable:** whether Crew skills are loaded.

### Phase 1 — Control (with Crew skills)

1. Install the full Crew skill pack repo on the Mac Mini
2. Load all relevant pack skills (e.g. Pack 10 for website builds)
3. Start a fresh Claude Code chat from the crew-skill-packs directory
4. Paste the original prompt (references crew skill by name)
5. Save the output

### Phase 2 — Experimental (no Crew skills)

1. On the same Mac Mini, run Claude Code with a completely clean slate:
   - No `.claude/skills/` loaded
   - No `brand-context.md`
   - No `crew-state/`
   - No CLAUDE.md referencing any Crew conventions
2. Start a fresh Claude Code chat from any directory (not the crew-skill-packs repo)
3. Paste the stripped-down prompt (describes the same output without naming Crew conventions)
4. Save the output

### Phase 3 — Compare

Put outputs side by side. Compare across these dimensions:

| Dimension | What to compare |
|-----------|----------------|
| Visual impact | Which version feels more premium at first glance? |
| Layout | Spacing, grid, visual hierarchy |
| Typography | Font pairing, scale, readability |
| Motion | Smoothness, timing, does motion serve the design? |
| Polish | Subtle details — shadows, borders, gradients, grain |
| Responsive | Does it work on mobile or is it desktop-only? |
| Code quality | Clean, well-structured, or spaghetti? |
| Consistency | Does each version feel coherent or Frankensteined? |

If Crew output is dramatically better, the skills are doing real work. If they are similar, the base model is the engine.

## Stripping prompts for fairness

The stripped-down prompt must describe the same desired output without naming Crew skill names, conventions, or phrases. Remove:
- `Use crew-web-*` directives
- References to "pack 10", "design review gate", "Context Loop", "handoff file"
- Crew-specific language like "Careful mode", "Step 0", "gold standard"
- Any mention of locked templates or Crew architecture

Keep:
- The same visual brief, same brand, same theme, same desired effect
- The same technical requirements (single file, dark theme, specific effects)
- The same output expectation (deploy to Vercel, self-contained HTML)

## Fairness checks

1. **Same hardware.** Both runs on the same machine.
2. **Same Claude Code version.** Both runs use the same binary.
3. **No cloud skill bleed.** Do not sign into Anthropic skills plugin for the experimental run.
4. **Stripped prompts are fair.** They describe the same output without naming Crew conventions.
5. **Judge with fresh eyes.** Wait an hour between runs, or compare them blind.

## Prompt pairs (example from Pack 10)

### Original (Crew skills loaded)
```
Use crew-web-spotlight-hero.
Build me a spotlight hero for "Verdant"...
```

### Stripped (no Crew skills)
```
Build a single-page HTML website for "Verdant"...
[Same visual brief, same effects, zero Crew language]
```

Full prompt pairs for spotlight-hero, fly-through-builder, and webcam-website are in the session that produced this protocol (28 June 2026).

## What the results tell you

| Crew wins | Base model wins | Tie |
|-----------|----------------|-----|
| Skills carry real weight. Keep investing. Pack depth matters. | Skills are window dressing. Audit what they actually contribute. Strip to essentials. | Skills add polish but not substance. Worth keeping for consistency, not for differentiation. |

## Using fixture prompts as test data

The Crew Pack 10 skill fixtures (`tests/crew-web-*-fixture.md`) contain Case A inputs that are excellent test prompts. They are:
- Already designed to exercise the skill's full capability
- Clean, well-formed briefs
- Not dependent on any specific Crew infrastructure

Use Case A inputs directly as the "original" prompt in the control run. Strip them for the experimental run.
