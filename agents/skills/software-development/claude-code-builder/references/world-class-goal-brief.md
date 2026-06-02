# World-Class Goal Brief Pattern

When Jared says "make it world class," "use the right people," or gives a quality directive, the correct Brock response is NOT to build it himself — it is to delegate to Bob with a structured goal brief.

## Pattern Structure

```
1. Read the existing artifact (read_file)
2. Write 10 numbered world-class goals targeting specific quality dimensions
3. Reference specific design systems as benchmarks (Stripe, Linear, Vercel, Airbnb)
4. Instruct Bob to use the Taste bundle (claude-design + popular-web-designs)
5. Preserve all existing functionality — list what must stay
6. Set explicit rules (no em dashes, single file, dark theme, no questions)
7. Delegate as a single `delegate_task` goal with the full brief
```

## Goal Categories (cover at least 8 of these)

1. Premium product feel — background texture, gradients, glass effects
2. Micro-interactions — hover states, transitions, spring easing
3. Score/metric badges — SVG rings, color coding, glow effects
4. Header/footer — editorial layout, live timestamps, stats pills
5. Card design — visual hierarchy, typography scale, tag chips
6. Filter bar — pill-style active states, glass frosted, scrollable on mobile
7. Animations — staggered card entrance, scroll-triggered
8. Mobile responsiveness — stacked layout, scrollable filter row, touch targets
9. Typography — font stack, weight scale, letter-spacing, line-height
10. Spacing — breathing room, card padding, section margins

## Example Brief Format

```text
Elevate the [artifact] at [path] to world-class quality.

WORLD-CLASS GOALS:
1. Premium product feel — [specific visual technique]
2. Micro-interactions — [specific animation targets]
3. [dimension] — [specific target]
...

Use the Taste bundle (claude-design + popular-web-designs) for every design decision.
Reference Stripe, Linear, Vercel, and Airbnb design systems.

RULES:
- No em dashes anywhere
- Single monolithic HTML file — all CSS and JS inline
- Keep all existing functionality [list specific items preserved]
- Dark theme throughout
- Output to the same file: [path]
- Do not ask questions. Build and write the file now.
```

## Key: Delegation, not execution

Brock never executes these builds. The hierarchy is:
- Brock → strategy, brief, orchestration
- Bob → build, design, deploy

When Jared says "use the right people," he is endorsing this split. Brock writes the goal brief. Bob executes at world-class quality.
