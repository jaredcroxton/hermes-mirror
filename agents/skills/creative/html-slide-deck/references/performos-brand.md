# PerformOS Parent Brand System

Source: PerformOS VISUAL.md, IDENTITY.md, COPY.md (2026 identity, current).
Retired identity (2025): navy/teal/green colours, Montserrat, "P" wing-arc mark.

## Colour palette

### Primary

| Token | Hex | Use |
|---|---|---|
| Ivory | `#f2efe8` | Primary background |
| Ivory Soft | `#e8e4da` | Cards, panels, surfaces |
| Ink | `#0a0a0a` | Primary text, dark buttons, dark UI |
| Electric Lime | `#d4ff3b` | CTAs, status dots, highlights, selection |

### Ink opacity scale (light mode)

| Token | Value | Use |
|---|---|---|
| Ink 100% | `rgba(10,10,10,1)` | Primary text |
| Ink 60% | `rgba(10,10,10,0.6)` | Secondary text, body copy |
| Ink 40% | `rgba(10,10,10,0.4)` | Labels, meta, tertiary |
| Ink 12% | `rgba(10,10,10,0.12)` | Borders, dividers |
| Ink 6% | `rgba(10,10,10,0.06)` | Subtle fills |

### Ivory opacity scale (dark variant)

| Token | Value | Use |
|---|---|---|
| Ivory 100% | `rgba(242,239,232,1)` | Primary text |
| Ivory 60% | `rgba(242,239,232,0.6)` | Secondary text, body copy |
| Ivory 40% | `rgba(242,239,232,0.4)` | Labels, meta, tertiary |
| Ivory 12% | `rgba(242,239,232,0.12)` | Borders, dividers |
| Ivory 6% | `rgba(242,239,232,0.06)` | Subtle fills |

### Data colours (in-product UI)

| Token | Value | Use |
|---|---|---|
| Positive / Up | `#d4ff3b` | Up indicator |
| Negative / Down | `rgb(255,154,154)` | Down indicator |
| Neutral | Ink-12 or Ivory-12 | Default bar / point |

## Typography

| Role | Font | Notes |
|---|---|---|
| Display / Headings | **Instrument Serif** | Weight 400. Italic variant for emphasis and the "OS" suffix. Google Fonts. |
| Body / UI | **Inter** | Weights 400 (body), 500 (UI), 600 (emphasis). Google Fonts. |
| Labels / Meta | **JetBrains Mono** | Weights 400-500. Always uppercase. Letter-spacing 1.5px to 2px. Google Fonts. |

### Type scale

| Role | Font | Size | Weight |
|---|---|---|---|
| Hero display | Instrument Serif | `clamp(56px, 9vw, 132px)` | 400 |
| Section H1 | Instrument Serif | 40-48px | 400 |
| H2 / Card title | Instrument Serif | 24-32px | 400 |
| Brand name | Instrument Serif | 20-22px | 400 |
| Body copy | Inter | 16px | 400 |
| UI / Buttons | Inter | 14-15px | 500 |
| Label / Overline | JetBrains Mono | 11px, uppercase, ls 1.5px | 400-500 |

## Logo

### Lockup
Minimal icon mark plus serif wordmark.

### Icon mark
Concentric circle: outer ring filled Ink `#0a0a0a`, inner circle filled Electric Lime `#d4ff3b`. The inner lime dot echoes accent status dots used in product UI.

### Wordmark
`Perform` in roman, `OS` in italic with lighter tonal value. Always Instrument Serif. Tight tracking around `-0.5px`.

### Dark variant
On Ink backgrounds: outer ring shifts to Ivory at 15% opacity. Inner lime dot stays Electric Lime. Wordmark in Ivory with italic `OS` at 40% Ivory opacity.

## Components

### Buttons
All buttons are pills (border-radius `100px`). Never rounded rectangles.

| Variant | Spec | Use |
|---|---|---|
| Primary | `bg: #0a0a0a`, `color: #f2efe8`, `radius: 100px`, `padding: 14px 24px` | Main CTAs, nav |
| Ghost | `border: 1px solid ink-12`, `color: ink`, `radius: 100px` | Secondary actions |
| Accent | `bg: #d4ff3b`, `color: #0a0a0a`, glow on hover | Featured CTAs |

### Labels and chips
- Chip: pill with mono label and small accent dot (Live, Shipping).
- Pill (category): small uppercase mono label inside ink-06 background, ink-12 border.
- Tag: lime-tinted rounded rectangle (6px radius) for status markers.

### Cards
- Background Ivory Soft `#e8e4da`
- Border `1px solid ink-12`
- Radius `16px`
- Padding `28px`
- Tag (mono, uppercase, ink-40) on top, serif heading, ink-60 body.
- Dark variant: background Ink `#0a0a0a` or lifted `#141414`, body at Ivory 60%.

### Navigation
- Sticky, frosted glass (`rgba(242,239,232,0.9)` + `backdrop-filter: blur(12px)`)
- Height 64-72px
- Brand wordmark in Instrument Serif left, links in Inter 14px, Contact CTA dark pill with glowing lime dot.

## Dark variant summary (dashboards, Pocket Customer, lead dashboards)

```css
:root {
  --ink: #0a0a0a;
  --ink-lift: #141414;
  --ink-surface: #1a1a1a;
  --ivory: #f2efe8;
  --ivory-60: rgba(242, 239, 232, 0.6);
  --ivory-40: rgba(242, 239, 232, 0.4);
  --ivory-12: rgba(242, 239, 232, 0.12);
  --ivory-06: rgba(242, 239, 232, 0.06);
  --lime: #d4ff3b;
  --lime-glow: rgba(212, 255, 59, 0.18);
  --font-serif: 'Instrument Serif', Georgia, serif;
  --font-body: 'Inter', -apple-system, sans-serif;
  --font-mono: 'JetBrains Mono', 'Courier New', monospace;
}
```

Google Fonts URL: `https://fonts.googleapis.com/css2?family=Instrument+Serif:ital@0;1&family=Inter:wght@400;500;600&family=JetBrains+Mono:wght@400;500&display=swap`

## Voice and copy rules

- Headings: serif. Labels: uppercase mono. Body: Inter.
- Australian spelling (catalogue, colour, practise).
- No em dashes. Use commas, periods, or parentheses.
- Vocabulary IN: instruments, catalogue, studio, operators, precision, focused, shipping, volume, surgically, compounding, tempo, craft.
- Vocabulary OUT: platform, suite, all-in-one, revolutionary, game-changer, enterprise-grade, seamless, unlock, leverage.
- "PerformOS" always capital P, capital O, capital S. Never PERFORMOs, Performos, or performOS.
- Never use "Sarah" in any product, demo, or test data.

## Do and don't

### Do
- Use Ivory `#f2efe8` as default page background.
- Use Instrument Serif for all headings and brand name.
- Set `OS` in italic when writing brand name.
- Use Electric Lime `#d4ff3b` sparingly as single accent.
- Use JetBrains Mono for all labels, overlines, and metadata.
- Use pill-shaped buttons (border-radius 100px) for all CTAs.
- Use Ink opacity scale for hierarchy, never hard-coded greys.

### Don't
- Don't use old navy/teal/green from 2025 identity.
- Don't use Montserrat (retired).
- Don't use old "P" mark with blue and green wing arcs.
- Don't write PERFORMOs in all caps.
- Don't use accent `#d4ff3b` as background for large areas.
- Don't use rounded-rectangle buttons (pill only: 100px radius).
- Don't mix serif and sans within same heading level.
- Don't use dark navy backgrounds outside specific dark card variants (the dark variant uses Ink `#0a0a0a`, not navy).
