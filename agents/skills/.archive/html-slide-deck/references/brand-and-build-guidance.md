# HTML Slide Deck — Brand and Build Guidance
# Reference supplement for html-slide-deck SKILL.md

## Brand-First Rule

**Before writing any code, consult the Brand configs section of the html-slide-deck SKILL.md.** If the user names a product (Performlytics, LearnOS, Pocket Customer, PulseCheck 360, PerformOS site default), use the exact colors and fonts from that brand config. Do not guess, do not hunt external files, do not use the default dark/archivo config if the user specified a sub-brand. The brand configs in the skill ARE the source of truth.

Common mistake: spending time digging through Obsidian brand files or website source when the skill already has the correct colors defined. Check the skill first.

## Pitch Documents vs Slide Decks — Deployment Pattern

When Jared asks for a **pitch document** (the written spec, strategy, or proposal), use Local artifact mode: write files to `~/Desktop/Obsidian/PerformOS/` or `~/Desktop/hermes_builds/`, hand the path to Jared, do NOT deploy. This follows the performos-website-builds rule: Brock hands files, never deploys.

When Jared asks for a **slide deck** (HTML presentation, visual deck) and wants to share it or view it on his phone, deploy: `git init` → `gh repo create` → `vercel --prod --yes`. Send the live URL via Telegram. This is a different workflow from pitch documents — decks are deployable artifacts.

## Animation Quality Bar (Confirmed 30 May 2026)

The minimum animation standard for a premium deck:
- Background motion: animated grid drift, floating orbs, or gradient shifts — never static solid
- Staggered element reveals: content elements (tags, titles, subtitles, cards, lists) fade/slide in with cascading delays, never all at once
- Gradient accent text: highlights use gradient fills (e.g., blue-to-violet, cyan-to-blue), never flat single color on dark backgrounds
- Glow effects on interactive elements: active nav dots, hover states on cards have subtle glow or box-shadow
- Smooth slide transitions: opacity + transform with easing, never instant cuts
- No flat, lifeless backgrounds — even "simple" premium decks need a subtle animated element

For the **Performlytics** brand specifically: floating orbs (blur 80px, opacity 0.08-0.15, 12-18s float animation) and grid drift background are the expected ambient motion. Blue (#3B82F6) primary accent, violet (#8B5CF6) secondary, cyan (#22D3EE) data viz.

## Brand Config Quick Reference

### PerformOS (parent brand, light-first with dark variant)

Full system in `references/performos-brand.md`.
- Light: BG `#f2efe8` (Ivory) | Text `#0a0a0a` (Ink) | Accent `#d4ff3b` (Lime)
- Dark: BG `#0a0a0a` (Ink) | Text `#f2efe8` (Ivory) | Accent `#d4ff3b` (Lime)
- Display: Instrument Serif | Body: Inter | Mono: JetBrains Mono
- Buttons: pill only (100px radius). No em dashes. Australian spelling.

### Performlytics (dark, data-aesthetic)
- BG: #0A0A0A | Surface: #111111 | Text: #F0F0F5
- Accent: #3B82F6 | Secondary: #8B5CF6 | Cyan: #22D3EE
- Display: Archivo | Body: Calibri/Inter | Mono: JetBrains Mono

### LearnOS (light, corporate-cool)
- BG: #F8FAFC | Surface: #FFFFFF | Text: #0F172A
- Accent: #0891B2 | Secondary: #22D3EE | Deep: #0E7490
- Display: Archivo | Body: Calibri/Inter | Mono: JetBrains Mono

### Pocket Customer (dark, urgent)
- BG: #0A0A0A | Surface: #141414 | Text: #F5EADB
- Accent: #D4FF3B (lime) | Alerts: #FF5F57
- Display: Archivo | Body: Calibri/Inter | Mono: JetBrains Mono

### PulseCheck 360 (dark, terminal)
- BG: #000000 | Surface: #0A0A0A | Text: #FFFFFF
- Accent: #14B8A6 | Secondary: #3B82F6 | Green: #00FF66
- Display: Archivo | Body: Calibri/Inter | Mono: JetBrains Mono