# High-Impact Animation Patterns for HTML Slide Decks

Tested in the PerformOS AI Team deck (June 2026). All patterns are CSS-only or vanilla JS. No external dependencies.

## 1. Particle Canvas Background

60 floating particles with connection lines. Renders on a `<canvas>` element behind all content.

CSS:
.particle-canvas { position: fixed; inset: 0; z-index: 0; pointer-events: none; }

JS: Create canvas element, get 2d context, spawn 60 particles with random positions/velocities/alphas. In draw loop: update positions, wrap around edges, draw filled circles, then draw connection lines between particles within 150px distance with opacity based on proximity.

## 2. 3D Perspective Slide Transitions

.slide { transform: perspective(1200px) translateY(60px) rotateX(8deg) scale(0.96); }
.slide.active { transform: perspective(1200px) translateY(0) rotateX(0deg) scale(1); }
.slide.exit-up { transform: perspective(1200px) translateY(-40px) rotateX(-4deg) scale(0.98); opacity: 0; }

## 3. Spring Easing

--ease-spring: cubic-bezier(0.34, 1.56, 0.64, 1);

Use for card, pill, and content reveal transitions. Gives a bouncy, alive feel compared to standard ease.

## 4. Animated Gradient Card Borders on Hover

.card::before pseudo-element with conic-gradient background using brand accent. opacity: 0 normally, opacity: 0.6 on hover. animation: cardBorderSpin 4s linear infinite. On hover the card border goes transparent and the rotating gradient shows through.

Register the `--angle` CSS property for smooth animation:

```css
@property --angle {
  syntax: '<angle>';
  inherits: false;
  initial-value: 0deg;
}
```

```css
.card::before {
  content: '';
  position: absolute;
  inset: -2px;
  border-radius: inherit;
  background: conic-gradient(from var(--angle),
    transparent 0deg, var(--color-accent) 90deg, transparent 180deg,
    transparent 180deg, var(--color-accent) 270deg, transparent 360deg);
  opacity: 0;
  transition: opacity 0.4s var(--ease);
  z-index: -1;
}
.card:hover::before {
  opacity: 0.6;
  animation: cardBorderSpin 4s linear infinite;
}
@keyframes cardBorderSpin {
  to { --angle: 360deg; }
}
```

Use semantic ring colours for typed cards (e.g. failure-type cards: red for preventable, amber for complex, lime for intelligent).

## 5. Count-Up Number Animation

Query .stat-val elements in active slide. Extract numeric value. Animate from 0 to target over 1200ms with ease-out cubic (1 - (1-t)^3). Use requestAnimationFrame. Mark elements with data-counted to prevent re-triggering.

## 6. Mouse Parallax on Background Orbs

Add data-depth attributes to orb elements (1, 2, 0.5). On mousemove, calculate normalized x/y position (-1 to 1). Apply transform: translate(x * 15 * depth, y * 12 * depth) to each orb.

## 7. Typing Effect on Title Tag

Target element by ID. Iterate through text string one character at a time. Set textContent to substring(0, i) on each tick. 50ms delay between characters. Start after 600ms initial delay.

## 8. Alternating Feature List Slide-In

.feature-list li { transform: translateX(-20px); }
.feature-list li:nth-child(even) { transform: translateX(20px); }
.slide.active .feature-list li { transform: translateX(0); transition with spring easing }

## 9. Pulse Animation on Active Nav Dot

.dot.active { animation: dotPulse 1.8s ease-in-out infinite; }
@keyframes dotPulse { 0%,100% { box-shadow: 0 0 8px rgba(59,130,246,0.4); } 50% { box-shadow: 0 0 16px rgba(59,130,246,0.7), 0 0 4px rgba(59,130,246,0.3); } }

## 10. Title Scale + Spring Reveal

.slide-title { opacity: 0; transform: translateY(24px) scale(0.97); transition: opacity 0.65s var(--ease-spring) 0.35s, transform 0.65s var(--ease-spring) 0.35s; }
.slide.active .slide-title { opacity: 1; transform: translateY(0) scale(1); }

## 11. Hover Lift + Glow on Cards

Every card surface gets a subtle lift and brand-coloured glow on hover:

```css
.card {
  transition: transform 0.35s var(--ease-spring), box-shadow 0.35s var(--ease);
}
.card:hover {
  transform: translateY(-2px);
  box-shadow: 0 8px 32px rgba(var(--color-accent-rgb), 0.15);
}
```

Apply to stat cards, failure-type cards, session cards, outcome boxes, and any clickable card surface.

## 12. Big-Stat-Number Hover

Large stat numbers (4.2x, 21x, 70%) get a hover treatment: slight scale + text glow in brand accent:

```css
.stat-number {
  transition: transform 0.3s var(--ease-spring), text-shadow 0.3s var(--ease);
}
.stat-number:hover {
  transform: scale(1.08);
  text-shadow: 0 0 24px var(--color-accent-dim);
}
```

## 13. Nav Arrow Hover Enhancement

Arrows start at 0.6 opacity. On hover: full opacity, spring scale, and accent glow ring:

```css
.nav-arrow {
  opacity: 0.6;
  transition: opacity 0.25s var(--ease), transform 0.35s var(--ease-spring), box-shadow 0.25s var(--ease);
}
.nav-arrow:hover {
  opacity: 1;
  transform: scale(1.12);
  box-shadow: 0 0 20px var(--color-accent-dim);
}
.nav-arrow:focus-visible {
  opacity: 1;
  outline: 2px solid var(--color-accent);
  outline-offset: 4px;
}
```

## 14. Ambient Gradient Float

Each slide background slowly drifts via CSS keyframe on background-position. Gives the deck a subtle breathing feel without distracting:

```css
@keyframes bg-float {
  0%, 100% { background-position: 0% 0%; }
  25% { background-position: 100% 0%; }
  50% { background-position: 100% 100%; }
  75% { background-position: 0% 100%; }
}
.slide {
  background-size: 220% 220%;
  animation: bg-float 30s ease-in-out infinite;
}
```

## 15. Pulse Glow on Active Nav Dot

The active dot pulses with a soft brand-accent glow:

```css
.dot.active {
  animation: dotPulse 1.8s ease-in-out infinite;
}
@keyframes dotPulse {
  0%, 100% { box-shadow: 0 0 8px var(--color-accent-dim); }
  50% { box-shadow: 0 0 18px var(--color-accent), 0 0 4px var(--color-accent-dim); }
}
```

## 16. prefers-reduced-motion Block

Always include. Drops ambient loops while keeping essential transitions:

```css
@media (prefers-reduced-motion: reduce) {
  [class*="bg-float"] { animation: none !important; }
  .particle-canvas { display: none; }
}
```

## Performance Notes

- Particle canvas uses requestAnimationFrame — pauses when tab is hidden
- All transforms use GPU-accelerated properties only
- Connection lines use early exit distance check (dist < 150px)
- Tested at 60fps on M4 Mac mini with 14 slides