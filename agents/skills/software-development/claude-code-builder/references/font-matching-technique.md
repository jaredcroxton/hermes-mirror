# Technique: Matching a Reference Site's Font Stack

**Date:** 2 June 2026
**Context:** Extracting the exact font stack from agentos.ai to match the PerformOS Trending Dashboard typography.

## The Problem

You need to match a reference website's typography on a build. You cannot inspect the CSS manually. You need the exact font-family stack, including custom fonts and fallbacks.

## The Technique

Navigate to the reference site with `browser_navigate`, then use `browser_console` with a JavaScript expression:

```javascript
JSON.stringify({
  headingFont: window.getComputedStyle(document.querySelector('h1')).fontFamily,
  bodyFont: window.getComputedStyle(document.querySelector('p')).fontFamily,
  allFonts: [...new Set([...document.querySelectorAll('*')]
    .map(el => window.getComputedStyle(el).fontFamily)
    .filter(f => f && !f.includes('emoji')))].slice(0, 10)
})
```

This returns the computed font-family for each heading level plus a deduplicated list of all fonts on the page.

## What to Look For

- **Custom fonts** appear as quoted names like `'__aspekta_db5589'`. These are `@font-face` loaded fonts. They will NOT be available on other machines unless you host them or use the same CDN.
- **Fallback stack** follows the custom font. Example: `'__aspekta_db5589', '__aspekta_Fallback_db5589', system-ui, -apple-system, sans-serif`
- If the custom font is not a Google Font, the fallback stack is what users will actually see. Design for the fallback.

## AgentOS Font Stack (2 June 2026)

- Primary/heading/body: `Aspekta` → fallback: `system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif`
- Monospace: `JetBrains Mono` → fallback: `ui-monospace, Menlo, monospace`
- Serif (decorative): `Instrument Serif` → fallback: `ui-serif, Georgia, serif`

## CSS Variable Pattern

When applying a matched font stack, use CSS custom properties:

```css
:root {
  --font-primary: 'Aspekta', 'Inter', system-ui, -apple-system, sans-serif;
  --font-mono: 'JetBrains Mono', ui-monospace, Menlo, monospace;
}
```

## SSL Certificate Errors

If `browser_navigate` returns an SSL error (526, ERR_CERT_COMMON_NAME_INVALID), use `firecrawl_scrape` with `formats: ["branding"]` instead. It extracts fonts, colors, and typography directly.
