# CSS Notes

## Dependencies

The course page links to:
- `styles.css` — the main PerformOS site stylesheet (must exist in the same directory)
- `main.js` — site JavaScript for nav toggle, FAQ accordion (must exist in the same directory)

Both files must be present for the page to render correctly.

## Existing CSS classes used

The page uses the PerformOS design system from styles.css:
- `.site-nav`, `.nav-inner`, `.brand-lockup`, `.brand-mark`, `.brand-wordmark`, `.nav-links`, `.nav-cta`
- `.btn`, `.btn-ghost`, `.btn-sm`, `.btn-accent`, `.btn-with-dot`, `.live`
- `.hero`, `.hero-eyebrow`, `.hero-subhead`, `.intro`
- `.section`, `.section-alt`, `.section-label`, `.section-intro`
- `.wrap`, `.wrap-narrow`
- `.styles-grid`, `.style-card`, `.style-icon`
- `.steps-grid`, `.step-card`, `.step-num`
- `.spectrum`, `.spec-card`, `.spec-high`
- `.price-block`, `.price-num`, `.price-detail`
- `.comparison`, `.comp-row`, `.comp-header`, `.comp-label`, `.comp-win`, `.comp-meh`, `.comp-nope`
- `.faq-preview`, `.faq-item`, `.faq-q`, `.faq-toggle`, `.faq-a`, `.faq-a-inner`
- `.cta-band`, `.cta-row`
- `.site-footer`, `.foot-grid`, `.foot-col`, `.foot-tagline`, `.foot-loc`, `.foot-base`

## Design tokens (from styles.css)

```css
--ivory: #f2efe8;           /* Page background */
--ink: #0a0a0a;             /* Primary text */
--ink-60: rgba(10,10,10,.6); /* Secondary text */
--ink-40: rgba(10,10,10,.4); /* Muted text */
--ink-12: rgba(10,10,10,.12); /* Borders */
--ink-06: rgba(10,10,10,.06); /* Subtle backgrounds */
--accent: #d4ff3b;          /* Lime accent */
--accent-dim: #b8e81c;      /* Darker lime */
--serif: 'Instrument Serif'; /* Display font */
--sans: 'Inter';            /* Body font */
--mono: 'JetBrains Mono';   /* Code font */
```

## Inline styles used (where no CSS class existed)

The following sections use inline styles because they introduced new patterns not covered by the existing stylesheet:

1. **Trust Ribbon (Beat 3):** Flexbox layout for stat cards — `display:flex; align-items:center; justify-content:center; gap:40px;`
2. **Problem contrast cards (Beat 4):** `border-left` colour differentiation for left vs right cards
3. **Instructor disclaimer:** Centred text at bottom of instructor section
4. **Certificate mockup (Beat 9):** Custom card styling with `background`, `border`, `border-radius`, `padding`, `max-width`, `margin`
5. **Disclosure block (Beat 12):** Highlighted card with `background`, `border`, `border-radius`, `padding`
6. **Trademark attribution (Beat 15):** Additional `div` with `border-top`, `font-size`, `color`, `line-height`

## If you want to add these to styles.css

These inline styles could be extracted into proper CSS classes for cleaner maintenance. Suggested class names:
- `.trust-ribbon` — for Beat 3
- `.problem-grid` — for Beat 4
- `.instructor-cert` — for Beat 7
- `.cert-mockup` — for Beat 9
- `.legal-disclosure` — for Beat 12
- `.foot-legal` — for Beat 15
