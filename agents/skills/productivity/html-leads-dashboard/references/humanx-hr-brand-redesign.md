# HumanX HR — Dashboard Brand Redesign

Captured 03 June 2026. Bob built a functional 5-lead dashboard for HumanX HR L&D consulting, but in a generic dark-mode SaaS theme with purple accents. The dashboard needed a full brand redesign to match HumanX HR's actual identity.

## The Pitfall

The dashboard was built without brand context. It shipped as:
- Dark mode (#0f1117 background)
- Purple accent (#6c5ce7, #a78bfa)
- No logo, text-based "HX" placeholder
- System font stack
- Generic SaaS dark dashboard look

## HumanX HR's Actual Brand (Firecrawl branding extraction)

- Primary: #021639 (deep navy)
- Secondary: #76DBFF (light sky blue)
- Accent: #FE6448 (warm coral/red)
- Background: #FFFFFF (light mode)
- Font: Bio Sans (proprietary — substituted with Source Sans 3 from Google Fonts)
- Logo: SVG on Webflow CDN
- Border radius: 20px on inputs, 4px on buttons
- Tone: professional, warm, human-centric

## What Changed

| Before | After |
|---|---|
| Dark mode (#0f1117) | Light mode, HumanX HR brand |
| Purple accent (#6c5ce7) | Coral accent (#FE6448) |
| "HX" text logo | Real HumanX HR logo from CDN |
| System font stack | Source Sans 3 (Bio Sans substitute) |
| Sharp 6-8px radius | 20px on cards, 10px on stat cards |
| Low-contrast dark inputs | White cards with navy headers |
| Stats: all purple | Stats: coral (hot), amber (warm), green (meetings) |
| Table header: dark grey | Navy (#021639) with white uppercase labels |

## The Lesson

**Always extract the client's brand BEFORE building the dashboard.** Use Firecrawl branding extraction on the client's homepage. If the dashboard is for a client (not PerformOS), the brand must match the client, not a default theme. A functionally perfect dashboard in the wrong brand is wrong.

## Brand Extraction Command (Firecrawl)

```
firecrawl_scrape(url="https://www.clientdomain.com.au", formats=["branding"])
```

Returns: colour scheme, fonts, logo URL, border radius, component styles, button colours, personality, target audience.
