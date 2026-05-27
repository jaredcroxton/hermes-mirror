# PerformOS 12-Week AI Course — Full Build

## What this is

The complete `course.html` for the PerformOS 12-week personalised AI course. Self-contained — no external CSS or JS dependencies beyond Google Fonts and Google Analytics. All styles inline. All JS embedded (nav toggle, FAQ accordion, scroll detection, GA4).

## 15-Beat Structure

1. Nav (sticky, glass blur)
2. Hero — "Your personal AI tutor. 12 weeks. Career-ready."
3. Trust Ribbon — 12 / 1-on-1 / $499 / Certificate
4. Problem — "Most AI courses treat you like everyone else"
5. How You Learn — 4 learning style cards
6. How It Works — Assess → Design → Deliver → Capable
7. Instructor — Jared Croxton + AI-900 + AI-102 + inline disclaimer
8. Curriculum — 4 phases with specialisation tracks
9. Certificate — clean PerformOS-only mockup
10. Spectrum — Start anywhere / Ready to build
11. Pricing — $499 with full inclusions
12. Mandatory Disclosure — Option B negative disclosure
13. Comparison Table — vs Academy Xi, AIM, online courses
14. FAQ — 7 questions including Option B objection handlers
15. Footer — trademark attribution

## Option B Compliance

- Instructor credentials in body text (Beat 7), never in hero H1
- No Microsoft/OpenAI/ChatGPT logos or icons anywhere
- No third-party certification names on Certificate of Completion
- Mandatory negative disclosure on page (Beat 12)
- Trademark attribution in footer
- PerformOS brand always more prominent than any third-party mark

## Deploy

Save as `course.html` and run:
```
vercel --prod --yes
```

Or git push to main (auto-deploys via Vercel).

## Post-Deploy Verification

- [ ] Hero: "Your personal AI tutor. 12 weeks. Career-ready."
- [ ] Trust ribbon visible with 4 stats
- [ ] Problem contrast section present
- [ ] Instructor: Jared Croxton + AI-900 + AI-102 + inline disclaimer
- [ ] Curriculum: 4 phases including specialisation tracks
- [ ] Certificate mockup: no Microsoft/OpenAI marks
- [ ] Pricing: $499 with full inclusions
- [ ] Disclosure block: "This course is not a Microsoft, OpenAI, or ChatGPT certification program..."
- [ ] FAQ: "Is this a Microsoft-certified course?" + "Why doesn't the certificate say Microsoft or Azure?"
- [ ] Footer: full trademark attribution

---

## course.html (981 lines — self-contained, no external CSS/JS)

```html
<!DOCTYPE html>
<html lang="en-AU">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>12-Week Personalised AI Course | $499 | PerformOS</title>
  <meta name="description" content="A 12-week personalised AI course built around how you learn. Instructor holds Microsoft Azure AI certifications. $499 one-time. Certificate of Completion included.">
  <meta name="author" content="Jared Croxton">

  <meta property="og:title" content="12-Week Personalised AI Course | $499 | PerformOS">
  <meta property="og:description" content="A 12-week personalised AI course. Instructor holds Microsoft Azure AI certifications. $499 one-time. Certificate of Completion included.">
  <meta property="og:type" content="website">
  <meta property="og:url" content="https://performos.com.au/course.html">
  <meta property="og:locale" content="en_AU">
  <meta property="og:site_name" content="PerformOS">
  <meta property="og:image" content="https://performos.com.au/og-image.svg">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="630">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:site" content="@PerformOS">

  <meta name="theme-color" content="#f2efe8" media="(prefers-color-scheme: light)">
  <meta name="theme-color" content="#0a0a0a" media="(prefers-color-scheme: dark)">
  <meta name="apple-mobile-web-app-capable" content="yes">
  <meta name="format-detection" content="telephone=no">

  <link rel="canonical" href="https://performos.com.au/course.html">
  <link rel="icon" type="image/svg+xml" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'%3E%3Ccircle cx='32' cy='32' r='30' fill='%230a0a0a'/%3E%3Ccircle cx='32' cy='32' r='16' fill='%23d4ff3b'/%3E%3C/svg%3E">

  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Instrument+Serif:ital@0;1&family=Inter:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">

  <style>
    :root {
      --ivory: #f2efe8;
      --ivory-soft: #e8e4da;
      --ink: #0a0a0a;
      --ink-80: rgba(10,10,10,.80);
      --ink-60: rgba(10,10,10,.60);
      --ink-40: rgba(10,10,10,.40);
      --ink-12: rgba(10,10,10,.12);
      --ink-06: rgba(10,10,10,.06);
      --accent: #d4ff3b;
      --accent-dim: rgba(212,255,59,.45);
      --accent-glow: rgba(212,255,59,.85);
      --serif: 'Instrument Serif', ui-serif, Georgia, serif;
      --sans: 'Inter', ui-sans-serif, system-ui, -apple-system, sans-serif;
      --mono: 'JetBrains Mono', ui-monospace, SFMono-Regular, Menlo, monospace;
      --border-radius-sm: 10px;
      --border-radius-md: 14px;
      --border-radius-lg: 18px;
    }
    *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
    html { scroll-behavior: smooth; }
    body {
      background: var(--ivory);
      color: var(--ink);
      font-family: var(--sans);
      font-size: 16px; line-height: 1.55;
      -webkit-font-smoothing: antialiased;
    }
    ::selection { background: var(--accent); color: var(--ink); }
    a { color: inherit; text-decoration: none; }
    ul { list-style: none; padding: 0; margin: 0; }
    button { font: inherit; cursor: pointer; border: 0; background: none; color: inherit; }
    :focus-visible { outline: 2px solid var(--accent); outline-offset: 3px; border-radius: 4px; }

    h1 { font-family: var(--serif); font-weight: 400; font-size: clamp(40px, 6vw, 72px); letter-spacing: -1.2px; line-height: 0.98; color: var(--ink); }
    h1 em { font-style: italic; color: var(--ink-40); }
    h2 { font-family: var(--serif); font-weight: 400; font-size: clamp(28px, 4vw, 40px); letter-spacing: -0.5px; line-height: 1.08; }
    h2 em { font-style: italic; color: var(--ink-40); }
    h3 { font-family: var(--serif); font-weight: 400; font-size: 22px; letter-spacing: -0.3px; line-height: 1.2; }

    .wrap { width: 100%; max-width: 1200px; margin: 0 auto; padding: 0 40px; }
    .wrap-narrow { width: 100%; max-width: 820px; margin: 0 auto; padding: 0 40px; }

    /* NAV */
    nav.site-nav {
      position: sticky; top: 0; z-index: 50;
      background: rgba(242,239,232,.82);
      backdrop-filter: saturate(150%) blur(12px);
      -webkit-backdrop-filter: saturate(150%) blur(12px);
      border-bottom: 1px solid transparent;
      transition: border-color .25s ease;
    }
    nav.site-nav.scrolled { border-bottom-color: var(--ink-12); }
    .nav-inner { display: flex; align-items: center; justify-content: space-between; height: 64px; gap: 24px; }
    .brand-lockup { display: inline-flex; align-items: center; gap: 10px; font-family: var(--serif); font-size: 20px; letter-spacing: -0.3px; color: var(--ink); }
    .brand-mark { width: 24px; height: 24px; flex-shrink: 0; }
    .brand-wordmark em { font-style: italic; color: var(--ink-40); }
    .nav-links { display: flex; gap: 24px; align-items: center; }
    .nav-links a { font-size: 14px; color: var(--ink-60); font-weight: 500; transition: color .15s ease; }
    .nav-links a:hover, .nav-links a.current { color: var(--ink); }
    .nav-cta { display: flex; align-items: center; gap: 10px; }
    .nav-toggle { display: none; width: 40px; height: 40px; flex-direction: column; gap: 5px; align-items: center; justify-content: center; border-radius: 100px; }
    .nav-toggle span { display: block; width: 18px; height: 1.5px; background: var(--ink); }
    .btn { display: inline-flex; align-items: center; gap: 8px; padding: 12px 20px; border-radius: 100px; font-family: var(--sans); font-size: 14px; font-weight: 500; transition: background .18s ease, box-shadow .18s ease, transform .12s ease; white-space: nowrap; }
    .btn:hover { transform: translateY(-1px); }
    .btn-ghost { background: transparent; color: var(--ink); box-shadow: inset 0 0 0 1px var(--ink-12); }
    .btn-ghost:hover { box-shadow: inset 0 0 0 1px var(--ink-40); }
    .btn-sm { padding: 10px 16px; font-size: 13px; }
    .btn-with-dot { display: inline-flex; align-items: center; gap: 8px; padding: 10px 18px; border-radius: 100px; background: var(--ink); color: var(--ivory); font-size: 13px; font-weight: 500; transition: transform .12s ease, box-shadow .18s ease; }
    .btn-with-dot:hover { transform: translateY(-1px); box-shadow: 0 8px 24px rgba(10,10,10,.15); }
    .btn-with-dot .live { width: 6px; height: 6px; border-radius: 50%; background: var(--accent); box-shadow: 0 0 8px var(--accent-glow); }
    .btn-accent { background: var(--accent); color: var(--ink); }
    .btn-accent:hover { box-shadow: 0 8px 24px rgba(212,255,59,.45); }
    .btn-on-dark { background: var(--ivory); color: var(--ink); }

    /* HERO */
    .hero { padding: 64px 0 32px; }
    .hero-eyebrow {
      font-family: var(--mono); font-size: 11px;
      letter-spacing: 1.5px; text-transform: uppercase;
      color: var(--ink-40); margin-bottom: 20px;
    }
    .hero h1 { max-width: 900px; }
    .hero-subhead {
      font-family: var(--serif); font-size: clamp(20px, 2.4vw, 26px);
      font-style: italic; color: var(--ink-60);
      margin-top: 22px; max-width: 720px; line-height: 1.3;
    }
    .hero .intro { font-size: 17px; color: var(--ink-60); line-height: 1.65; margin-top: 22px; max-width: 720px; }
    .cta-row { display: flex; flex-wrap: wrap; gap: 12px; margin-top: 32px; }

    /* SECTIONS */
    .section { padding: 64px 0; }
    .section-alt { background: var(--ivory-soft); }
    .section-label { font-family: var(--mono); font-size: 11px; letter-spacing: 1.5px; text-transform: uppercase; color: var(--ink-40); display: block; margin-bottom: 14px; }
    .section-intro { font-size: 17px; color: var(--ink-60); line-height: 1.65; margin-top: 16px; max-width: 720px; }

    /* TRUST RIBBON */
    .trust-ribbon { display: flex; align-items: center; justify-content: center; gap: 56px; flex-wrap: wrap; text-align: center; }
    .trust-stat .trust-num { font-family: var(--serif); font-size: 36px; font-weight: 400; line-height: 1; letter-spacing: -0.5px; }
    .trust-stat .trust-num em { font-style: normal; color: var(--ink); }
    .trust-stat .trust-num .lime { background: linear-gradient(180deg, transparent 55%, var(--accent) 55%); padding: 0 4px; }
    .trust-stat .trust-label { font-size: 13px; color: var(--ink-60); margin-top: 8px; }

    /* CARD GRID */
    .steps-grid { display: grid; grid-template-columns: repeat(4, 1fr); gap: 18px; margin-top: 36px; }
    .steps-grid.two-col { grid-template-columns: repeat(2, 1fr); }
    .steps-grid.three-col { grid-template-columns: repeat(3, 1fr); }
    .step-card {
      padding: 26px;
      border-radius: var(--border-radius-md);
      border: 1px solid var(--ink-12);
      background: var(--ivory);
      display: flex; flex-direction: column;
      transition: border-color .18s ease, transform .18s ease;
    }
    .section-alt .step-card { background: var(--ivory); }
    .step-card:hover { border-color: var(--ink-40); transform: translateY(-2px); }
    .step-card .step-num { font-family: var(--mono); font-size: 11px; letter-spacing: 1.5px; text-transform: uppercase; color: var(--ink-40); margin-bottom: 14px; display: block; }
    .step-card h3 { margin-bottom: 10px; }
    .step-card p { font-size: 14px; color: var(--ink-60); line-height: 1.65; }
    .step-card ul { font-size: 14px; color: var(--ink-60); line-height: 1.7; }
    .step-card.compare-bad { border-left: 3px solid var(--ink-12); }
    .step-card.compare-good { border-left: 3px solid var(--accent); }
    .step-card.compare-bad h3 { color: var(--ink-60); }

    /* LEARNING STYLES */
    .styles-grid { display: grid; grid-template-columns: repeat(4, 1fr); gap: 18px; margin-top: 36px; }
    .style-card {
      padding: 28px 24px;
      border-radius: var(--border-radius-md);
      border: 1px solid var(--ink-12);
      background: var(--ivory);
      transition: border-color .18s ease, transform .18s ease;
    }
    .style-card:hover { border-color: var(--ink-40); transform: translateY(-2px); }
    .style-icon { font-size: 22px; margin-bottom: 14px; display: inline-block; width: 40px; height: 40px; border-radius: 50%; background: var(--ivory-soft); display: inline-flex; align-items: center; justify-content: center; }
    .section-alt .style-icon { background: var(--ivory); }
    .style-card h3 { font-size: 20px; margin-bottom: 8px; }
    .style-card p { font-size: 14px; color: var(--ink-60); line-height: 1.65; }

    /* CERTIFICATE PREVIEW */
    .cert-card {
      background: var(--ivory);
      border: 1px solid var(--ink-12);
      border-radius: var(--border-radius-md);
      padding: 44px 32px;
      max-width: 540px;
      margin: 36px auto 0;
      text-align: center;
      box-shadow: 0 24px 48px -24px rgba(10,10,10,.15);
    }
    .section-alt .cert-card { background: var(--ivory); }
    .cert-brand { font-family: var(--serif); font-size: 22px; font-weight: 400; margin-bottom: 6px; letter-spacing: -0.3px; }
    .cert-brand em { font-style: italic; color: var(--ink-40); }
    .cert-rule { width: 40px; height: 1px; background: var(--ink-12); margin: 18px auto; }
    .cert-line { font-size: 13px; color: var(--ink-60); margin-bottom: 6px; }
    .cert-name { font-family: var(--serif); font-style: italic; font-size: 26px; color: var(--ink); margin: 12px 0 20px; }
    .cert-course { font-family: var(--serif); font-size: 20px; color: var(--ink); margin: 10px 0 22px; }
    .cert-footer { font-size: 11px; color: var(--ink-40); margin-top: 14px; line-height: 1.6; }

    /* SPECTRUM */
    .spectrum { display: grid; grid-template-columns: repeat(2, 1fr); gap: 18px; margin-top: 36px; }
    .spec-card {
      padding: 32px;
      border-radius: var(--border-radius-md);
      border: 1px solid var(--ink-12);
      background: var(--ivory);
      transition: border-color .18s ease, transform .18s ease;
    }
    .spec-card:hover { border-color: var(--ink-40); transform: translateY(-2px); }
    .spec-card h3 { font-size: 24px; margin-bottom: 12px; }
    .spec-card p { font-size: 15px; color: var(--ink-60); line-height: 1.65; }
    .spec-high { background: var(--ink); color: var(--ivory); border-color: var(--ink); }
    .spec-high h3 { color: var(--ivory); }
    .spec-high p { color: rgba(242,239,232,.7); }
    .spec-high:hover { border-color: var(--ink); }

    /* PRICING */
    .price-block {
      margin-top: 32px;
      display: grid;
      grid-template-columns: 0.7fr 1.3fr;
      gap: 0;
      background: var(--ivory);
      border: 1px solid var(--ink-12);
      border-radius: var(--border-radius-lg);
      overflow: hidden;
    }
    .price-num {
      background: var(--ink);
      color: var(--ivory);
      padding: 40px 32px;
      font-family: var(--serif);
      font-size: clamp(56px, 8vw, 88px);
      letter-spacing: -2px;
      line-height: 1;
      display: flex; align-items: center; justify-content: center;
      position: relative;
    }
    .price-num::after {
      content: 'AUD . one-time';
      position: absolute; bottom: 24px; left: 0; right: 0;
      font-family: var(--mono); font-size: 10px; letter-spacing: 1.5px;
      text-transform: uppercase; color: rgba(242,239,232,.5);
      text-align: center;
    }
    .price-detail { padding: 36px 32px; }
    .price-detail h3 { font-size: 22px; margin-bottom: 10px; }
    .price-detail > p { font-size: 14px; color: var(--ink-60); line-height: 1.65; margin-bottom: 18px; }
    .price-detail ul { display: flex; flex-direction: column; gap: 8px; }
    .price-detail ul li {
      font-size: 14px; color: var(--ink-80);
      padding-left: 22px; position: relative; line-height: 1.55;
    }
    .price-detail ul li::before {
      content: ''; position: absolute; left: 0; top: 8px;
      width: 12px; height: 8px;
      border-left: 2px solid var(--ink); border-bottom: 2px solid var(--ink);
      transform: rotate(-45deg);
    }

    /* DISCLOSURE */
    .disclosure-box {
      background: var(--ink-06);
      border: 1px solid var(--ink-12);
      border-radius: var(--border-radius-md);
      padding: 22px 26px;
      font-size: 13px; color: var(--ink-60); line-height: 1.7;
    }
    .disclosure-box strong { color: var(--ink); font-weight: 600; }

    /* COMPARISON */
    .comparison {
      margin-top: 32px;
      border: 1px solid var(--ink-12);
      border-radius: var(--border-radius-md);
      background: var(--ivory);
      overflow: hidden;
    }
    .section-alt .comparison { background: var(--ivory); }
    .comp-row {
      display: grid;
      grid-template-columns: 1.3fr 1fr 1fr 1fr 1fr;
      align-items: center;
      gap: 0;
      padding: 16px 22px;
      border-bottom: 1px solid var(--ink-12);
      font-size: 14px;
    }
    .comp-row:last-child { border-bottom: 0; }
    .comp-row > span { padding: 0 8px; }
    .comp-header {
      background: var(--ink);
      color: var(--ivory);
      font-family: var(--mono);
      font-size: 11px;
      letter-spacing: 1.5px;
      text-transform: uppercase;
      padding: 16px 22px;
    }
    .comp-header > span { color: var(--ivory); }
    .comp-header > span:nth-child(2) { color: var(--accent); }
    .comp-label { font-family: var(--mono); font-size: 11px; letter-spacing: 1.5px; text-transform: uppercase; color: var(--ink-40); }
    .comp-win { color: var(--ink); font-weight: 500; }
    .comp-meh { color: var(--ink-60); }
    .comp-nope { color: var(--ink-40); }

    /* FAQ */
    .faq-preview { margin-top: 32px; border-top: 1px solid var(--ink-12); }
    .faq-item { border-bottom: 1px solid var(--ink-12); }
    .faq-q {
      width: 100%;
      display: flex; align-items: center; justify-content: space-between;
      padding: 22px 0;
      text-align: left;
      font-family: var(--serif); font-size: 22px; line-height: 1.25; letter-spacing: -0.2px;
      color: var(--ink);
    }
    .faq-q:hover { color: var(--ink-80); }
    .faq-toggle {
      width: 28px; height: 28px; border-radius: 50%;
      border: 1px solid var(--ink-12);
      position: relative; flex-shrink: 0; margin-left: 16px;
      transition: background .18s ease, border-color .18s ease, transform .25s ease;
    }
    .faq-toggle::before, .faq-toggle::after {
      content: ''; position: absolute;
      background: var(--ink);
      top: 50%; left: 50%;
      transition: transform .25s ease;
    }
    .faq-toggle::before { width: 10px; height: 1.5px; transform: translate(-50%, -50%); }
    .faq-toggle::after { width: 1.5px; height: 10px; transform: translate(-50%, -50%); }
    .faq-q[aria-expanded="true"] .faq-toggle { background: var(--accent); border-color: var(--accent); }
    .faq-q[aria-expanded="true"] .faq-toggle::after { transform: translate(-50%, -50%) scaleY(0); }
    .faq-a {
      max-height: 0; overflow: hidden;
      transition: max-height .35s ease;
    }
    .faq-a-inner {
      padding: 0 0 24px 0;
      font-size: 15px; color: var(--ink-60); line-height: 1.7; max-width: 680px;
    }
    .faq-q[aria-expanded="true"] + .faq-a { max-height: 600px; }

    /* CTA BAND */
    .cta-band {
      background: var(--ink); color: var(--ivory);
      border-radius: var(--border-radius-lg); padding: 48px;
      display: grid; grid-template-columns: 1.3fr 0.7fr; gap: 32px; align-items: center;
    }
    .cta-band h2 { font-family: var(--serif); font-weight: 400; color: var(--ivory); font-size: clamp(28px, 3.5vw, 38px); line-height: 1.05; letter-spacing: -0.5px; }
    .cta-band h2 em { font-style: italic; color: var(--accent); }
    .cta-band p { color: rgba(242,239,232,.7); margin-top: 14px; font-size: 15px; line-height: 1.55; }
    .cta-band .cta-row { margin-top: 0; justify-content: flex-end; }

    /* FOOTER */
    footer.site-footer { border-top: 1px solid var(--ink-12); padding: 48px 0 24px; background: var(--ivory); }
    .foot-grid { display: grid; grid-template-columns: 1.5fr 1fr 1fr 1fr; gap: 40px; margin-bottom: 32px; }
    .foot-tagline { color: var(--ink-60); font-size: 14px; line-height: 1.55; margin-top: 14px; max-width: 320px; }
    .foot-loc { display: inline-flex; align-items: center; gap: 8px; margin-top: 16px; font-family: var(--mono); font-size: 10px; letter-spacing: 1.5px; text-transform: uppercase; color: var(--ink-40); }
    .foot-col h5 { font-family: var(--mono); font-size: 11px; letter-spacing: 1.5px; text-transform: uppercase; color: var(--ink-40); font-weight: 400; margin-bottom: 14px; }
    .foot-col ul { display: flex; flex-direction: column; gap: 9px; }
    .foot-col a { font-size: 14px; color: var(--ink-60); transition: color .15s ease; }
    .foot-col a:hover { color: var(--ink); }
    .foot-base { display: flex; justify-content: space-between; align-items: center; padding-top: 22px; border-top: 1px solid var(--ink-12); font-family: var(--mono); font-size: 11px; letter-spacing: 1.5px; text-transform: uppercase; color: var(--ink-40); }
    .foot-trademark { margin-top: 22px; padding-top: 18px; border-top: 1px solid var(--ink-12); font-size: 11px; color: var(--ink-40); line-height: 1.7; }
    .foot-trademark strong { color: var(--ink-60); }

    @media (max-width: 980px) {
      .steps-grid, .steps-grid.three-col { grid-template-columns: repeat(2, 1fr); }
      .styles-grid { grid-template-columns: repeat(2, 1fr); }
      .comp-row { grid-template-columns: 1.3fr repeat(4, 1fr); font-size: 13px; padding: 14px 16px; }
      .comp-header { padding: 14px 16px; }
    }
    @media (max-width: 720px) {
      .wrap, .wrap-narrow { padding: 0 22px; }
      .nav-links { display: none; }
      .nav-toggle { display: inline-flex; min-width: 44px; min-height: 44px; }
      .nav-cta .btn-ghost { display: none; }
      .nav-inner { gap: 12px; }
      .hero { padding: 36px 0 24px; }
      .hero h1 { font-size: 38px; }
      .section { padding: 48px 0; }
      .trust-ribbon { gap: 28px; }
      .steps-grid, .steps-grid.two-col, .steps-grid.three-col { grid-template-columns: 1fr; }
      .styles-grid { grid-template-columns: 1fr; }
      .spectrum { grid-template-columns: 1fr; }
      .price-block { grid-template-columns: 1fr; }
      .price-num { padding: 36px 24px; }
      .price-num::after { bottom: 16px; }
      .price-detail { padding: 28px 24px; }
      .comparison { font-size: 12px; }
      .comp-row { grid-template-columns: 1fr; gap: 6px; padding: 16px; }
      .comp-row > span { padding: 2px 0; }
      .comp-header { display: none; }
      .comp-label { color: var(--ink-40); }
      .cta-band { grid-template-columns: 1fr; padding: 28px 24px; }
      .cta-band .cta-row { justify-content: flex-start; }
      .foot-grid { grid-template-columns: 1fr; gap: 24px; margin-bottom: 24px; }
      .foot-base { flex-direction: column; gap: 10px; text-align: center; font-size: 10px; }
    }
    .nav-links.open {
      display: flex; flex-direction: column; gap: 0;
      position: absolute; top: 64px; left: 0; right: 0;
      background: var(--ivory);
      padding: 14px 24px 22px;
      border-bottom: 1px solid var(--ink-12);
    }
    .nav-links.open li { padding: 12px 0; border-bottom: 1px solid var(--ink-12); }
    .nav-links.open li:last-child { border-bottom: 0; }

    @media (prefers-reduced-motion: reduce) {
      *, *::before, *::after { transition-duration: .01ms !important; animation-duration: .01ms !important; }
    }
  </style>

  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@graph": [
      {
        "@type": "Service",
        "@id": "https://performos.com.au/course.html#service",
        "name": "12-Week Personalised AI Adoption Course",
        "provider": { "@id": "https://performos.com.au/#organization" },
        "description": "A 12-week personalised AI course built around how you learn. Instructor holds Microsoft Azure AI certifications. Custom curriculum from basic AI fluency to custom agents. $499 one-time. Certificate of Completion included.",
        "offers": {
          "@type": "Offer",
          "price": "499",
          "priceCurrency": "AUD",
          "availability": "https://schema.org/InStock"
        },
        "url": "https://performos.com.au/course.html"
      },
      {
        "@type": "FAQPage",
        "mainEntity": [
          {
            "@type": "Question",
            "name": "How is the course personalised to how I learn?",
            "acceptedAnswer": { "@type": "Answer", "text": "We start with a conversation. You tell us how you absorb information best: 20-minute daily practical modules, three-minute video lessons, explicit written instructions, or any combination. We design all 12 weeks around that. Nothing is off the shelf." }
          },
          {
            "@type": "Question",
            "name": "What can I expect to be able to do after 12 weeks?",
            "acceptedAnswer": { "@type": "Answer", "text": "That depends on where you start and where you want to land. From zero AI experience to confidently using AI in your daily work. Or from intermediate to building custom agents and automating workflows. We design the curriculum around your goals." }
          },
          {
            "@type": "Question",
            "name": "Is this a Microsoft-certified course?",
            "acceptedAnswer": { "@type": "Answer", "text": "No. PerformOS is an independent training provider. Our instructor holds current Microsoft Azure AI certifications, and those credentials inform the curriculum. But the course itself is not a Microsoft certification program, and completing it does not earn you a Microsoft credential. You receive a PerformOS Certificate of Completion." }
          },
          {
            "@type": "Question",
            "name": "How does this compare to Academy Xi or AIM courses?",
            "acceptedAnswer": { "@type": "Answer", "text": "Academy Xi charges $899 to $3,150 for AI courses with some mentoring. AIM charges $600 to $800 for one to two day short courses. PerformOS is $499 for a full 12-week personalised curriculum built around how you actually learn." }
          }
        ]
      }
    ]
  }
  </script>
  <script async src="https://www.googletagmanager.com/gtag/js?id=G-HMWH2EPLZ3"></script>
  <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){dataLayer.push(arguments);}
    gtag("js", new Date());
    gtag("config", "G-HMWH2EPLZ3");
  </script>

</head>
<body>

  <nav class="site-nav" id="nav" aria-label="Primary">
    <div class="wrap nav-inner">
      <a href="index.html" class="brand-lockup" aria-label="PerformOS home">
        <svg class="brand-mark" viewBox="0 0 64 64" aria-hidden="true">
          <circle cx="32" cy="32" r="30" fill="#0a0a0a"/>
          <circle cx="32" cy="32" r="16" fill="#d4ff3b"/>
        </svg>
        <span class="brand-wordmark">Perform<em>OS</em></span>
      </a>
      <ul class="nav-links" id="navMenu">
        <li><a href="course.html" class="current">12-Week Course</a></li>
        <li><a href="catalogue.html">Catalogue</a></li>
        <li><a href="ai-transformation.html">Transformation</a></li>
        <li><a href="ai-implementation.html">Implementation</a></li>
        <li><a href="ai-fluency-workshop.html">Workshop</a></li>
        <li><a href="about.html">Studio</a></li>
      </ul>
      <div class="nav-cta">
        <a href="contact.html?topic=12-Week%20Course" class="btn btn-ghost btn-sm" style="box-shadow:inset 0 0 0 1px var(--ink-40);">Start your plan</a>
        <a href="contact.html?topic=12-Week%20Course" class="btn-with-dot"><span class="live" aria-hidden="true"></span>Contact</a>
        <button class="nav-toggle" id="navToggle" type="button" aria-label="Toggle menu" aria-expanded="false" aria-controls="navMenu">
          <span aria-hidden="true"></span><span aria-hidden="true"></span><span aria-hidden="true"></span>
        </button>
      </div>
    </div>
  </nav>

  <!-- HERO -->
  <section class="hero">
    <div class="wrap">
      <p class="hero-eyebrow">12 Weeks . Personalised . $499 One-Time</p>
      <h1>Your personal AI tutor.<br><em>12 weeks. Career-ready.</em></h1>
      <p class="hero-subhead">A course that adapts to your skill level, your pace, and your goals. Not a crowded classroom. Not a one-size-fits-all curriculum. Just you, an expert instructor, and the AI skills employers actually want.</p>
      <p class="intro">Most AI courses are built for the average learner. You are not the average learner. You absorb information differently. You have different goals. You are starting from a different place. This course is designed around exactly where you are and exactly how you learn best.</p>
      <div class="cta-row">
        <a href="contact.html?topic=12-Week%20Course" class="btn-with-dot"><span class="live" aria-hidden="true"></span>Book your plan, $499</a>
        <a href="#compare" class="btn btn-ghost">Compare options</a>
      </div>
    </div>
  </section>

  <!-- TRUST RIBBON -->
  <section class="section section-alt" style="padding: 36px 0;">
    <div class="wrap">
      <div class="trust-ribbon">
        <div class="trust-stat">
          <div class="trust-num">12</div>
          <div class="trust-label">Weeks, fully personalised</div>
        </div>
        <div class="trust-stat">
          <div class="trust-num">1-on-1</div>
          <div class="trust-label">Instructor-led, not self-serve</div>
        </div>
        <div class="trust-stat">
          <div class="trust-num"><span class="lime">$499</span></div>
          <div class="trust-label">One-time. No subscription.</div>
        </div>
        <div class="trust-stat">
          <div class="trust-num">&#10003;</div>
          <div class="trust-label">Certificate of Completion</div>
        </div>
      </div>
    </div>
  </section>

  <!-- PROBLEM -->
  <section class="section" id="problem">
    <div class="wrap">
      <span class="section-label">The problem</span>
      <h2>Most AI courses treat you like<br><em>everyone else.</em></h2>
      <p class="section-intro">Same curriculum. Same pace. Same format. Whether you are a marketer who needs AI for campaigns or a developer who wants to build agents, you get the same course. That is the problem we built PerformOS to solve.</p>
      <div class="steps-grid two-col">
        <div class="step-card compare-bad">
          <h3>What most courses do</h3>
          <ul>
            <li>, Recorded videos from 2023</li>
            <li>, Hundreds of students per cohort</li>
            <li>, Zero instructor feedback</li>
            <li>, Learn PyTorch when you need prompt engineering</li>
            <li>, No certificate employers recognise</li>
          </ul>
        </div>
        <div class="step-card compare-good">
          <h3>What PerformOS does</h3>
          <ul>
            <li>, Curriculum built around your goals</li>
            <li>, 1-on-1 with a certified instructor</li>
            <li>, Weekly check-ins and real feedback</li>
            <li>, Learn exactly what your role needs</li>
            <li>, Certificate of Completion you can share</li>
          </ul>
        </div>
      </div>
    </div>
  </section>

  <!-- HOW YOU LEARN -->
  <section class="section section-alt" id="styles">
    <div class="wrap">
      <span class="section-label">Your learning style</span>
      <h2>Choose how you learn.<br><em>We build around it.</em></h2>
      <p class="section-intro">No two people learn the same way. During your first conversation we identify what works for you. Everything we build for the next 12 weeks follows that format.</p>
      <div class="styles-grid">
        <div class="style-card">
          <div class="style-icon">&#9201;</div>
          <h3>20-minute daily</h3>
          <p>Practical modules delivered in focused sprints. One concept. One exercise. Built into your workday.</p>
        </div>
        <div class="style-card">
          <div class="style-icon">&#9654;</div>
          <h3>3-minute video</h3>
          <p>Short, focused video lessons you watch between meetings. One idea per lesson. Immediately applicable.</p>
        </div>
        <div class="style-card">
          <div class="style-icon">&#9783;</div>
          <h3>Explicit instructions</h3>
          <p>Step-by-step written guides. Every click documented. Every concept explained in plain English. Work through at your desk.</p>
        </div>
        <div class="style-card">
          <div class="style-icon">&#8644;</div>
          <h3>Mixed format</h3>
          <p>Your combination. Video for concepts. Written for technical steps. Sprints for practice. Whatever works.</p>
        </div>
      </div>
    </div>
  </section>

  <!-- HOW IT WORKS -->
  <section class="section" id="process">
    <div class="wrap">
      <span class="section-label">How it works</span>
      <h2>Four steps. Twelve weeks.<br><em>One outcome.</em></h2>
      <div class="steps-grid">
        <div class="step-card">
          <span class="step-num">01 Assess</span>
          <h3>We talk</h3>
          <p>A conversation, not a form. Where are you with AI? Where do you want to be? How do you learn best? This shapes everything. We map your starting point and your destination before we build anything.</p>
        </div>
        <div class="step-card">
          <span class="step-num">02 Design</span>
          <h3>We build</h3>
          <p>Your custom 12-week curriculum. Modules in your preferred format. Paced to your availability. Skip what you know. Deep-dive what you need. Every week is built for you, not a cohort.</p>
        </div>
        <div class="step-card">
          <span class="step-num">03 Delivery</span>
          <h3>You learn</h3>
          <p>Weekly modules delivered in your format. Check-ins when you want them. Adjustments if something is not working. Real instructor feedback, not automated quizzes. The course bends to you, not the other way around.</p>
        </div>
        <div class="step-card">
          <span class="step-num">04 Capable</span>
          <h3>You ship</h3>
          <p>By week 12 you are building what you set out to build. Custom agents. Automated workflows. Confident daily AI use. A portfolio project relevant to your actual job. Your Certificate of Completion. Your outcome, delivered.</p>
        </div>
      </div>
    </div>
  </section>

  <!-- INSTRUCTOR -->
  <section class="section section-alt" id="instructor">
    <div class="wrap">
      <span class="section-label">Your instructor</span>
      <h2>Learn from a certified<br><em>AI practitioner.</em></h2>
      <p class="section-intro">Your instructor, Jared Croxton, holds current Microsoft Azure AI certifications (AI-900: Azure AI Fundamentals and AI-102: Azure AI Engineer Associate). These credentials inform the course curriculum and practical exercises. Real certifications. Real teaching. Not a chatbot.</p>
      <div class="steps-grid three-col">
        <div class="step-card">
          <span class="step-num">AI-900</span>
          <h3>Azure AI Fundamentals</h3>
          <p>Microsoft-certified knowledge of AI workloads, machine learning principles, computer vision, NLP, and generative AI on Azure. The foundation of the course curriculum.</p>
        </div>
        <div class="step-card">
          <span class="step-num">AI-102</span>
          <h3>Azure AI Engineer</h3>
          <p>Microsoft-certified expertise in building, managing, and deploying AI solutions. This is the depth behind the custom agents and automation modules in the course.</p>
        </div>
        <div class="step-card">
          <span class="step-num">Practitioner</span>
          <h3>Real-world experience</h3>
          <p>Not just certifications. Real experience building AI instruments, training teams, and deploying AI in actual business environments across APAC.</p>
        </div>
      </div>
      <p style="font-size:12px;color:var(--ink-40);margin-top:28px;text-align:center;">
        Microsoft and Azure are trademarks of the Microsoft group of companies. PerformOS is an independent training provider.
      </p>
    </div>
  </section>

  <!-- CURRICULUM -->
  <section class="section" id="curriculum">
    <div class="wrap">
      <span class="section-label">Curriculum</span>
      <h2>What you will learn<br><em>in 12 weeks.</em></h2>
      <p class="section-intro">Every curriculum is personalised to your starting point and goals. Below is the framework. Your actual modules adapt to you: your industry, your tools, your level.</p>
      <div class="steps-grid">
        <div class="step-card">
          <span class="step-num">Weeks 1, 3</span>
          <h3>AI Foundations &amp; Prompt Engineering</h3>
          <p>Understand how AI actually works. Master prompting that gets results. Learn which tools do what. Build the mental model that makes everything else stick.</p>
        </div>
        <div class="step-card">
          <span class="step-num">Weeks 4, 6</span>
          <h3>Building with AI</h3>
          <p>Custom GPTs, AI agents, retrieval-augmented generation, webhook connections, memory and context. Move from user to builder.</p>
        </div>
        <div class="step-card">
          <span class="step-num">Weeks 7, 9</span>
          <h3>Your Specialisation Track</h3>
          <p>Choose your lane: Marketing AI, Engineering AI, or Leadership AI. Deep-dive into the tools and workflows your role actually needs. Skip what is not relevant.</p>
        </div>
        <div class="step-card">
          <span class="step-num">Weeks 10, 12</span>
          <h3>Capstone Project &amp; Career</h3>
          <p>Week 12 is one real project. Build something relevant to your job. Document your workflow. Graduate with your PerformOS Certificate of Completion and a body of work you can show employers.</p>
        </div>
      </div>
    </div>
  </section>

  <!-- CERTIFICATE -->
  <section class="section section-alt" id="certificate">
    <div class="wrap-narrow" style="text-align:center;">
      <span class="section-label">Certificate of Completion</span>
      <h2>Graduate with proof<br><em>you can share.</em></h2>
      <p class="section-intro" style="margin-left:auto;margin-right:auto;">At the end of your 12 weeks you receive a PerformOS Certificate of Completion, a record of your personalised AI training. Share it on LinkedIn. Add it to your CV. Show employers what you built.</p>
      <div class="cert-card">
        <div class="cert-brand">Perform<em>OS</em></div>
        <div class="cert-line" style="font-family:var(--mono);font-size:10px;letter-spacing:1.5px;text-transform:uppercase;color:var(--ink-40);">Certificate of Completion</div>
        <div class="cert-rule"></div>
        <div class="cert-line">This certifies that</div>
        <div class="cert-name">[Your Name]</div>
        <div class="cert-line">has successfully completed the</div>
        <div class="cert-course">12-Week Personalised AI Course</div>
        <div class="cert-footer">A professional development program covering practical AI skills, AI tooling, and applied AI concepts. Issued by PerformOS.</div>
      </div>
      <p style="font-size:12px;color:var(--ink-40);margin-top:18px;">
        This certificate is issued by PerformOS and is not a Microsoft, OpenAI, or third-party certification.
      </p>
    </div>
  </section>

  <!-- SPECTRUM -->
  <section class="section" id="spectrum">
    <div class="wrap">
      <span class="section-label">Where you land</span>
      <h2>Start anywhere.<br><em>Go as far as you want.</em></h2>
      <p class="section-intro">Your starting point determines your curriculum. Your ambition determines your finish line.</p>
      <div class="spectrum">
        <div class="spec-card">
          <h3>Starting from zero</h3>
          <p>You have not used AI beyond maybe asking ChatGPT a question. By week 12 you are confident using AI across your daily work, writing effective prompts, and knowing which tools to reach for. You move from feeling behind to feeling capable.</p>
        </div>
        <div class="spec-card spec-high">
          <h3>Ready to build</h3>
          <p>You already use AI but want to build. Custom agents that automate your workflows. Webhook connections between your tools. Memory and context that persists across sessions. By week 12 you are shipping working automation, not watching tutorials about it.</p>
        </div>
      </div>
    </div>
  </section>

  <!-- PRICING -->
  <section class="section section-alt" id="pricing">
    <div class="wrap-narrow">
      <span class="section-label">Pricing</span>
      <h2>One price.<br><em>Everything included.</em></h2>
      <div class="price-block">
        <div class="price-num">$499</div>
        <div class="price-detail">
          <h3>12-week personalised AI adoption course</h3>
          <p>Custom curriculum. Your format. Your pace. Your outcome. No upsells. No subscriptions. No per-module fees.</p>
          <ul>
            <li>Skills assessment and goal-setting conversation</li>
            <li>Custom 12-week curriculum in your format</li>
            <li>1-on-1 instructor check-ins</li>
            <li>Specialisation track (Marketing, Engineering, or Leadership AI)</li>
            <li>Capstone portfolio project</li>
            <li>PerformOS Certificate of Completion</li>
            <li>Lifetime access to your course materials</li>
            <li>One-time payment. Owned forever.</li>
          </ul>
        </div>
      </div>
    </div>
  </section>

  <!-- DISCLOSURE -->
  <section class="section" id="disclosure" style="padding-top: 0;">
    <div class="wrap-narrow">
      <div class="disclosure-box">
        <strong>This course is not a Microsoft, OpenAI, or ChatGPT certification program.</strong> Completion does not confer any Microsoft, OpenAI, or third-party credential. PerformOS is an independent training provider and is not endorsed by, affiliated with, or partnered with Microsoft Corporation, OpenAI, or any certification-issuing body. Your instructor holds current Microsoft Azure AI certifications (AI-900 and AI-102) as independent professional credentials. Those credentials inform the curriculum but do not make this an accredited Microsoft course. You receive a PerformOS Certificate of Completion.
      </div>
    </div>
  </section>

  <!-- COMPARISON -->
  <section class="section section-alt" id="compare">
    <div class="wrap">
      <span class="section-label">How we compare</span>
      <h2>You have options.<br><em>Here is how they stack up.</em></h2>
      <p class="section-intro">Most AI courses are either expensive cohort programmes, short one-day workshops, or cheap video libraries with no support. PerformOS is none of those.</p>
      <div class="comparison">
        <div class="comp-row comp-header">
          <span></span>
          <span>PerformOS</span>
          <span>Academy Xi</span>
          <span>AIM</span>
          <span>Online courses</span>
        </div>
        <div class="comp-row">
          <span class="comp-label">Price</span>
          <span class="comp-win">$499 one-time</span>
          <span class="comp-meh">$899, $3,150</span>
          <span class="comp-meh">$600, $800</span>
          <span class="comp-nope">$15, $59/mo</span>
        </div>
        <div class="comp-row">
          <span class="comp-label">Duration</span>
          <span class="comp-win">12 weeks</span>
          <span class="comp-meh">6, 12 months</span>
          <span class="comp-nope">1, 2 days</span>
          <span class="comp-nope">Self-paced</span>
        </div>
        <div class="comp-row">
          <span class="comp-label">Personalised</span>
          <span class="comp-win">100% custom</span>
          <span class="comp-meh">Some mentoring</span>
          <span class="comp-nope">Off the shelf</span>
          <span class="comp-nope">None</span>
        </div>
        <div class="comp-row">
          <span class="comp-label">Learning format</span>
          <span class="comp-win">Your choice</span>
          <span class="comp-meh">Self-paced + mentor</span>
          <span class="comp-nope">Classroom only</span>
          <span class="comp-nope">Video only</span>
        </div>
        <div class="comp-row">
          <span class="comp-label">Instructor</span>
          <span class="comp-win">Microsoft-certified</span>
          <span class="comp-meh">Varies</span>
          <span class="comp-meh">Industry</span>
          <span class="comp-nope">None</span>
        </div>
        <div class="comp-row">
          <span class="comp-label">Subscription</span>
          <span class="comp-win">None</span>
          <span class="comp-win">None</span>
          <span class="comp-win">None</span>
          <span class="comp-nope">Yes</span>
        </div>
        <div class="comp-row">
          <span class="comp-label">Built for</span>
          <span class="comp-win">Individuals who feel behind</span>
          <span class="comp-meh">Career changers</span>
          <span class="comp-meh">Managers</span>
          <span class="comp-nope">Anyone</span>
        </div>
      </div>
    </div>
  </section>

  <!-- FAQ -->
  <section class="section" id="faq">
    <div class="wrap-narrow">
      <span class="section-label">Frequently asked questions</span>
      <h2>Straight answers<br><em>about the course.</em></h2>
      <div class="faq-preview">
        <div class="faq-item">
          <button class="faq-q" type="button" aria-expanded="false">
            <span>How is the course personalised to how I learn?</span>
            <span class="faq-toggle" aria-hidden="true"></span>
          </button>
          <div class="faq-a"><div class="faq-a-inner"><p>We start with a conversation. You tell us how you absorb information best: 20-minute daily practical modules, three-minute video lessons, explicit written instructions, or any combination. We design all 12 weeks around that. Nothing is off the shelf. Everything is built for the way your brain actually works.</p></div></div>
        </div>
        <div class="faq-item">
          <button class="faq-q" type="button" aria-expanded="false">
            <span>What can I expect to be able to do after 12 weeks?</span>
            <span class="faq-toggle" aria-hidden="true"></span>
          </button>
          <div class="faq-a"><div class="faq-a-inner"><p>That depends on where you start and where you want to land. If you are coming in with zero AI experience, you will leave confident using AI in your daily work. If you want to build custom agents and automate workflows, we will get you there. We design the curriculum around your goals, so week 12 looks exactly like the outcome you want.</p></div></div>
        </div>
        <div class="faq-item">
          <button class="faq-q" type="button" aria-expanded="false">
            <span>Is this a Microsoft-certified course?</span>
            <span class="faq-toggle" aria-hidden="true"></span>
          </button>
          <div class="faq-a"><div class="faq-a-inner"><p>No. PerformOS is an independent training provider. Your instructor, Jared Croxton, holds current Microsoft Azure AI certifications (AI-900 and AI-102), and those credentials inform the curriculum. But the course itself is not a Microsoft certification program and completing it does not earn you a Microsoft credential. You receive a PerformOS Certificate of Completion as evidence of your learning.</p></div></div>
        </div>
        <div class="faq-item">
          <button class="faq-q" type="button" aria-expanded="false">
            <span>Why doesn't the certificate say Microsoft or Azure?</span>
            <span class="faq-toggle" aria-hidden="true"></span>
          </button>
          <div class="faq-a"><div class="faq-a-inner"><p>The PerformOS Certificate of Completion reflects that you have completed a PerformOS program. It is our credential, not Microsoft's. Your instructor's Microsoft certifications are separate, they are the credentials the instructor holds, not credentials the course awards.</p></div></div>
        </div>
        <div class="faq-item">
          <button class="faq-q" type="button" aria-expanded="false">
            <span>Is there a team version?</span>
            <span class="faq-toggle" aria-hidden="true"></span>
          </button>
          <div class="faq-a"><div class="faq-a-inner"><p>The 12-week course is built for individuals. If you want to train your whole team, our half-day AI Fluency Workshop is the better fit. On-site or remote. Your team leaves with a working AI instrument configured for your actual business.</p></div></div>
        </div>
        <div class="faq-item">
          <button class="faq-q" type="button" aria-expanded="false">
            <span>How does this compare to Academy Xi or AIM?</span>
            <span class="faq-toggle" aria-hidden="true"></span>
          </button>
          <div class="faq-a"><div class="faq-a-inner"><p>Academy Xi charges $899 to $3,150 for AI courses with some mentoring. AIM charges $600 to $800 for one to two day short courses. We are $499 for a full 12-week personalised curriculum built around how you actually learn. No one else at this price point builds a custom curriculum designed for your specific learning style.</p></div></div>
        </div>
        <div class="faq-item">
          <button class="faq-q" type="button" aria-expanded="false">
            <span>Can I switch format partway through?</span>
            <span class="faq-toggle" aria-hidden="true"></span>
          </button>
          <div class="faq-a"><div class="faq-a-inner"><p>Yes. If the format is not working, tell us. We adjust. The point of a personalised course is that it adapts to you, not the other way around.</p></div></div>
        </div>
      </div>
    </div>
  </section>

  <!-- FINAL CTA -->
  <section class="section">
    <div class="wrap">
      <div class="cta-band">
        <div>
          <h2>You are not behind.<br><em>You just need your plan.</em></h2>
          <p>One conversation. Twelve weeks. Your outcome. $499.</p>
        </div>
        <div class="cta-row">
          <a href="contact.html?topic=12-Week%20Course" class="btn btn-accent">Book your plan, $499</a>
        </div>
      </div>
    </div>
  </section>

  <!-- FOOTER -->
  <footer class="site-footer">
    <div class="wrap">
      <div class="foot-grid">
        <div>
          <div class="brand-lockup" style="font-size:18px;">
            <svg class="brand-mark" viewBox="0 0 64 64" aria-hidden="true" style="width:22px;height:22px;">
              <circle cx="32" cy="32" r="30" fill="#0a0a0a"/>
              <circle cx="32" cy="32" r="16" fill="#d4ff3b"/>
            </svg>
            <span class="brand-wordmark">Perform<em>OS</em></span>
          </div>
          <p class="foot-tagline">Personalised AI adoption for professionals. 12-week custom plans built around how you learn. From the basics through to custom agents and workflows.</p>
          <div class="foot-loc">
            <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg>
            Based in Australia
          </div>
        </div>
        <div class="foot-col">
          <h5>Catalogue</h5>
          <ul>
            <li><a href="catalogue.html#performlytics">Performlytics</a></li>
            <li><a href="catalogue.html#pocket-customer">Pocket Customer</a></li>
            <li><a href="catalogue.html#pulsecheck-360">PulseCheck 360</a></li>
            <li><a href="catalogue.html#learnos">LearnOS</a></li>
          </ul>
        </div>
        <div class="foot-col">
          <h5>Services</h5>
          <ul>
            <li><a href="course.html">12-Week Course</a></li>
            <li><a href="ai-fluency-workshop.html">Fluency Workshops</a></li>
            <li><a href="ai-implementation.html">Implementation</a></li>
            <li><a href="catalogue.html">Catalogue</a></li>
          </ul>
        </div>
        <div class="foot-col">
          <h5>Studio</h5>
          <ul>
            <li><a href="about.html">About</a></li>
            <li><a href="faq.html">FAQ</a></li>
            <li><a href="contact.html">Contact</a></li>
            <li><a href="contact.html?topic=12-Week%20Course">Book your plan</a></li>
          </ul>
        </div>
      </div>
      <div class="foot-base">
        <span>&copy; PerformOS . Made in Australia</span>
        <span>Volume 01 . 2026 . Powering high performance</span>
      </div>
      <div class="foot-trademark">
        <p><strong>Trademark attributions:</strong> Microsoft, Azure, and Microsoft Azure are trademarks of the Microsoft group of companies. OpenAI and ChatGPT are trademarks of OpenAI. All other trademarks are the property of their respective owners. Use of these marks does not imply endorsement, sponsorship, or affiliation. PerformOS is an independent training provider.</p>
      </div>
    </div>
  </footer>

  <script>
    const nav = document.getElementById('nav');
    const onScroll = () => { if (window.scrollY > 8) nav.classList.add('scrolled'); else nav.classList.remove('scrolled'); };
    window.addEventListener('scroll', onScroll, { passive: true });
    onScroll();

    const toggle = document.getElementById('navToggle');
    const menu = document.getElementById('navMenu');
    toggle.addEventListener('click', () => {
      const open = menu.classList.toggle('open');
      toggle.setAttribute('aria-expanded', String(open));
    });

    // FAQ accordion
    document.querySelectorAll('.faq-q').forEach(btn => {
      btn.addEventListener('click', () => {
        const expanded = btn.getAttribute('aria-expanded') === 'true';
        btn.setAttribute('aria-expanded', String(!expanded));
      });
    });
  </script>
</body>
</html>
```
