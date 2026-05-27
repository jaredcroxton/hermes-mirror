# PerformOS Website Design System

**Class:** Website page builds matching the PerformOS brand
**Proven:** 2026-05-26 — 3 pages built (workshop pillar + 2 blog articles), 6 more in progress + course.html with comparison table, price block, learning styles grid

## Reference file

Always match `/Users/jc/Desktop/Website - PerformOS/faq.html` as the design system source of truth.

## Visual tokens

```
--ivory: #f2efe8       (page background)
--ivory-soft: #e8e4da  (subtle surface)
--ink: #0a0a0a         (primary text)
--ink-60: rgba(10,10,10,.60)  (secondary text)
--ink-40: rgba(10,10,10,.40)  (tertiary text)
--ink-12: rgba(10,10,10,.12)  (borders, dividers)
--ink-06: rgba(10,10,10,.06)  (subtle fills)
--accent: #d4ff3b      (lime highlight)
--accent-glow: rgba(212,255,59,.85)
```

## Typography

```
--serif: 'Instrument Serif', ui-serif, Georgia, serif   (headings, brand wordmark)
--sans: 'Inter', ui-sans-serif, system-ui, -apple-system, sans-serif  (body)
--mono: 'JetBrains Mono', ui-monospace, SFMono-Regular, Menlo, monospace  (labels, breadcrumbs, metadata)
```

Google Fonts import:
```html
<link href="https://fonts.googleapis.com/css2?family=Instrument+Serif:ital@0;1&family=Inter:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
```

## Shared components (copy from faq.html)

- **Nav:** Sticky, glass blur backdrop, brand lockup (Perform*OS* with SVG mark), nav links, CTA buttons
- **Footer:** 4-column grid, brand tagline, Catalogue/Services/Studio link columns, copyright + volume line
- **FAQ accordion:** `.faq-item` > `.faq-q` (button) + `.faq-a` (collapsible answer). JS toggle pattern.
- **Breadcrumb:** Mono font, uppercase, dot separators
- **CTA buttons:** `.btn-ghost` (outline), `.btn-with-dot` (filled + lime dot), `.btn-accent` (lime fill), `.btn-on-dark` (ivory on ink)

## Page types

### Service page (workshop, implementation, agents)
- `.wrap-narrow` (800px max)
- Hero with H1 + intro paragraph + breadcrumb
- Content sections with H2s
- FAQ section at bottom
- CTA bar (ink background, ivory text, lime accent on key words)

### Blog article
- `.wrap-narrow` (800px)
- Article header: H1, date, author
- Body: H2s, paragraphs, lists
- Cross-links to related articles
- CTA at end linking to pillar page

### Catalogue page
- Instrument cards: border, padding, instrument name + description + status badge
- Status badges: green dot + "Live" label

## Build rules
- Single monolithic HTML file. CSS and JS inline. No external dependencies except Google Fonts.
- No em dashes anywhere.
- Australian spelling throughout.
- Mobile responsive at 720px breakpoint (comparison table collapses to 2 columns, styles grid to 1).
- JSON-LD schema inline (Organization, Service, FAQPage, BreadcrumbList, BlogPosting, Offer as appropriate).
- All internal links use relative paths to sibling HTML files.

## New components (from course.html, 2026-05-26)

### Comparison table
5-column grid. Header row: mono uppercase labels. Data rows: label col (bold) + 4 competitor cols with semantic classes (comp-win for green, comp-meh for neutral, comp-nope for dim). PerformOS column gets accent left border. Collapses to 2 cols at 720px.

### Price block
2-column grid (price numeral + detail). Accent border. Large serif price ($499). Feature list with lime dot bullets via ::before pseudo-element. Stacks to single column on mobile.

### Learning styles grid
4-column card grid with emoji icon + h3 + p. Centered text. Cards have border + radius. Collapses 4->2->1.

### Steps component
4-column step cards with mono step number label + h3 heading + p description. Collapses 2->1.

### Spectrum (start/goal pairs)
2-column grid with spec-card. One card gets spec-high class (accent border + tinted background). Collapses to 1 col.
