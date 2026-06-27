# Dark-Theme Deck Navigation Arrows

## Problem

Navigation arrows on dark-theme HTML slide decks render invisible. The default theme uses `--color-surface-2` (near-black, e.g. `#111111`) for arrow backgrounds and `--color-border` (dark gray, e.g. `#1F1F1F`) for borders. Both blend into the black background. Combined with `opacity: 0` on load (visible only on hover), the arrows are functionally invisible to the user.

## Fix pattern (apply to every dark-theme deck)

```css
.nav-arrow {
  background: rgba(0,0,0,0.7);      /* always faintly visible */
  border: 1px solid var(--color-primary); /* accent stands out */
  color: var(--color-primary);
  opacity: 0.45;                     /* floor, not 0 */
  transition: opacity .3s ease, background .3s ease;
}
#deck:hover .nav-arrow { opacity: 1; }
.nav-arrow:hover {
  background: var(--color-primary);
  color: var(--color-bg);
}
```

## Verification

After every dark-theme deck build, open the file and confirm:
- Arrows visible at rest (faint teal/lime against black)
- Arrows brighten on hover
- Arrow click advances to next/previous slide
- Mobile swipe works without arrows

## Sessions where this bug shipped

- crew-pitch-deck.html (Black + Teal + Terminal theme)
- LearnOS deck dist (earlier session)
- Multiple CREW slide-deck-builder test outputs
