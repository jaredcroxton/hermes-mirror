---
name: seo-content-pipeline
description: Multi-file SEO content operations for PerformOS — keyword briefs, pillar pages, article briefs, FAQ pages, internal link tables, and agent routing through Serge → Polly → Bob with brand compliance gates.
category: productivity
triggers:
  - "Continue the SEO journey"
  - "Run the SEO pipeline"
  - "Produce keyword brief"
  - "Build the pillar page"
  - "Article brief for [keyword]"
  - "Update the FAQ page for [topic]"
  - "Internal link table"
  - "Serge SEO"
  - "Polly review SEO"
  - "get me on Google"
  - "appear in AI searches"
  - "two businesses"
  - "turn up and train"
  - "full automation"
  - "organisational transformation with AI"
  - "build the transformation page"
  - "rebuild the homepage"
  - "ship the SEO cluster"
  - "take control of this project"
  - "AgentOS SEO"
  - "private AI team SEO"
  - "free AdWords"
  - "Google Ads credits"
  - "SEO research for AgentOS"
---

# SEO Content Pipeline

Multi-file SEO asset production for PerformOS. Covers the full content cluster lifecycle: keyword research → pillar draft → article briefs → FAQ enrichment → internal link mapping → build handoff → deploy → verify. All work routes through Serge_SEO for production, Polly_PerformOS for brand compliance, and Bob_Builder for build.

## Pipeline sequence

1. **Keyword brief** (Serge) — primary + secondary keywords, intent map, content mapping, production plan
2. **Polly review** of keyword brief — brand alignment, vocabulary compliance, commercial relevance
3. **Pillar page draft** (Serge) — target page for the primary keyword, full SEO markup
4. **Polly review** of pillar draft — delivery-gap risk, catalogue accuracy, brand voice
5. **Placeholder fills** (Brock) — duration, cities, group size, pricing model. Document all decisions in status line.
6. **Polly second-pass** of populated pillar draft — link resolution, duplication check, final vocabulary sweep
7. **Article briefs** (Serge) — supporting blog posts, one per high-priority secondary keyword
8. **Polly review** of article briefs — instrument status labels, pricing framing, catalogue names
9. **Article drafts** (Serge) — full article drafts from approved briefs
10. **Polly review of article drafts** — **MANDATORY product-state verification gate** (see below)
11. **Blog index page** (Serge) — landing page listing all published articles with descriptions, dates, read-more links. Links to pillar.
12. **Polly review of blog index** — article descriptions match actual draft content, no incorrect instrument names, no jargon (LLM → AI)
13. **AI Transformation page** (Brock or Serge) — full-service consulting page with five-step process, safe AI framework, custom agents. See AI Transformation page pattern below.
14. **Polly review of transformation page** — support boundary on "We stay", OUT vocabulary check, product evidence in framework. See transformation-specific Polly checks.
15. **Service pages** (Serge) — AI Implementation, AI Agents, About, Contact. One call for all remaining pages.
16. **Polly review of service pages** — brand voice, vocabulary, commercial coherence per page.
17. **Homepage rebuild** (Brock edits, Serge or Bob build) — four-lane structure: Transform, Learn, Implement, Use. See Homepage two-business framing below.
18. **FAQ enrichment** — extract FAQ from pillar draft, append to faq.html with JSON-LD schema update.
19. **Internal link table** (Serge) — four directional tables (pillar outbound, pillar inbound, cross-article, catalogue)
20. **Polly review** of link table — link density, reciprocal completeness, anchor text voice, density summary accuracy
21. **Bob build** — build all pages in parallel. Route via `hermes --profile bobbuilder` with source→output mapping.
22. **Technical SEO layer** (Brock) — inject GA4 + Twitter cards, create sitemap, create robots.txt.
23. **Push to production** — `git add . && git commit -m "message" && git push origin main` from Website folder. Vercel auto-deploys.
24. **Deploy verify** — `vercel inspect` for Ready, curl all routes for 200. New pages may 404 for 10-20 seconds after inspect shows Ready. If 404: `sleep 15` then retry.
25. **Schema verify** — curl each page, grep for `application/ld+json`, confirm schema types per page context.
26. **Search Console handoff** — user creates property at search.google.com/search-console, verifies, submits sitemap.
22. **Search Console handoff** — user creates property at search.google.com/search-console, verifies, submits sitemap. Cannot be agent-done (needs Google login).

## AgentOS SEO research pattern

When Jared asks for SEO research, free AdWords, Google Ads credits, or low-cost acquisition for **AgentOS by PerformOS**, do not produce a quick keyword list yourself. Treat it as a multi-agent SEO workflow.

Recommended routing:
1. **Serge_SEO** — keyword and intent map for private AI team / custom AI agents / AI agents for business.
2. **Serge_SEO** — free and low-cost Google acquisition research: Google Ads credits, Keyword Planner, Search Console, Google Business Profile, free SEO tools, conversion tracking, and 30-day no/low-cost launch plan.
3. **Serge_SEO** — competitor and SERP landscape for private AI agents, AI automation agency, AI workforce, Google Chat AI assistant, AI business assistant.
4. **Polly_PerformOS** — brand-safe SEO review: reject terms that commoditise the offer, define metadata-vs-body language, check product architecture against PerformOS / LearnOS / PulseCheck 360 / AgentOS.
5. **Brock** — final synthesis for Jared: executive call, page architecture, keyword priorities, free Google setup steps, paid-search test plan, 30-day action plan, risks, and single next action.

Early strategic hypothesis to test, not assume:
- Do not lead only with "AI agents" because it may attract hobbyists, SaaS shoppers, and low-ticket chatbot buyers.
- Commercially stronger lanes may be "private AI team for business," "custom AI agents for business," "AI business automation consultant," "AI assistant for business leaders," and "AI transformation for small business."
- Positioning gap to explore: **private AI team for business leaders**, not another chatbot or subscription.

## Keyword strategy rule

Target keyword strings use search terms buyers actually type. Editorial copy (title tags, H1s, H2s, body) uses brand terms. This is the search-vs-brand split:

- Keyword column: "AI tools for small business Australia" (matches search intent)
- Title tag/H1: "AI Instruments for Small Business Australia" (brand-distinctive)
- Body copy: "instruments" throughout (brand voice)

The split must be clearly noted in every keyword brief and article brief so writers do not accidentally target the wrong term.

## Product-state verification (MANDATORY)

**Before any article that lists PerformOS instruments is published, Polly must verify every instrument's status.** Do not trust the brief or an earlier draft. Product state can change between pipeline stages, and agent context exports can be stale.

**Founder authority rule:** When Polly's context-export data conflicts with Jared's direct statement about product state, Jared is authoritative. If Polly flags a product as paused or non-live and Jared has previously indicated otherwise, route to Jared for confirmation before removing it from content. Never silently remove a product Jared considers live.

Current catalogue (26 May 2026, confirmed by Jared):
- **Pocket Customer** — Live. Shipping.
- **LearnOS** — Live. Shipping.
- **PulseCheck 360** — Live. Shipping.
- **Performlytics** — Live. Shipping.

All four instruments are Live. Status labels in articles should read "Live. Available now."

When an article draft lists products, Polly's review prompt must include: "Verify every instrument status label. If any product appears paused or non-live in context data, flag it for Jared confirmation before recommending removal."

## Brand compliance checkpoints

Every piece of SEO content passes through Polly before Jared sees it. Polly checks:
- Forbidden vocabulary: platform, suite, all-in-one, seamless, unlock, leverage, revolutionary, game-changer, enterprise-grade
- Required vocabulary: instruments (not tools in body), catalogue (not suite), ship/shipping, operators
- Australian spelling: practise (verb), organisation, customise, optimise, behaviour, centre
- No em dashes
- Sentence case H1
- No superlatives
- Instrument catalogue accuracy — current: Pocket Customer (Live), LearnOS (Live), PulseCheck 360 (Live), Performlytics (Live). All four confirmed Live by Jared 26 May 2026.
- Pricing framing: "Try it free. Buy it once. Own it forever."
- Beta status honesty: never present undeployed or paused products as available. When in doubt about product state, ask Jared directly — do not rely solely on agent context exports.

## Pricing model default

When no workshop pricing model has been specified: **standalone one-time fee, fully credited toward first instrument purchase within 30 days.** This preserves the "one price, no subscription" model, generates revenue from workshop-only buyers, and creates a conversion path to instrument ownership. Document the decision in the pillar draft status line.

## GA4 + Twitter injection pattern

Inject into all HTML pages in one pass using sed:

```bash
# GA4 snippet before </head> (runs once per file, skips if already present)
for f in *.html; do
  if ! grep -q "googletagmanager" "$f"; then
    sed -i '' '/<\/head>/i\
  <!-- Google tag (gtag.js) -->\
  <script async src="https://www.googletagmanager.com/gtag/js?id=G-XXXXXXXXXX"><\/script>\
  <script>\
    window.dataLayer = window.dataLayer || [];\
    function gtag(){dataLayer.push(arguments);}\
    gtag("js", new Date());\
    gtag("config", "G-XXXXXXXXXX");\
  <\/script>\
' "$f"
  fi
done

# Twitter cards after og:site_name (skips if already present)
for f in *.html; do
  if ! grep -q "twitter:card" "$f"; then
    sed -i '' '/<meta property="og:site_name" content="PerformOS">/a\
  <meta name="twitter:card" content="summary_large_image">\
  <meta name="twitter:site" content="@PerformOS">\
' "$f"
  fi
done
```

The GA4 ID is a placeholder (`G-XXXXXXXXXX`) until Jared supplies the real measurement ID from analytics.google.com.

## Sitemap update pattern

When new pages are added to production, regenerate sitemap.xml with all routes. Use a heredoc:

```bash
cat > sitemap.xml << 'SITEMAP'
<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url><loc>https://www.performos.com.au/</loc><changefreq>weekly</changefreq><priority>1.0</priority></url>
  ...all pages with priorities...
</urlset>
SITEMAP
```

Homepage: priority 1.0, weekly. Pillar: 0.9, monthly. Service pages: 0.8, monthly. Articles: 0.7, monthly. Blog index: 0.8, weekly. FAQ: 0.7, monthly. About: 0.6, monthly. Contact: 0.5, monthly.

## PulseCheck 360 naming standardisation

Before any production push, standardise all occurrences to "PulseCheck 360" (no space). The brand library is split but the cross-cutting rules and link table use the no-space form. Fix command:

```bash
cd "/Users/jc/Desktop/Website - PerformOS"
sed -i '' 's/Pulse Check 360/PulseCheck 360/g' *.html
# Verify zero spaced occurrences
grep -c "Pulse Check 360" *.html
```

Do NOT touch `#pulsecheck-360` URL fragments (lowercase, no-space is correct for anchors).

## FAQ page update pattern

When adding a new FAQ category to faq.html:
1. Add category link to `.faq-categories` nav with `href="#new-id"`
2. Insert new `.faq-group` section with unique `id`, numbered sequentially
3. Re-number all subsequent group numbers
4. Add matching Q&A entries to the JSON-LD `FAQPage` schema
5. Keep answers consistent between HTML body and JSON-LD
6. When patching FAQ HTML, include enough surrounding context in `old_string` to avoid matching adjacent Q&A blocks. Over-broad matches can swallow neighbouring content.

## Agent routing

- **Serge_SEO** (`sergeseo`): keyword briefs, article briefs, pillar drafts, blog index, internal link tables
- **Polly_PerformOS** (`pollyperformos`): brand review of all SEO content before Jared sees it
- **Bob_Builder** (`bobbuilder`): build/deploy pages from content drafts. Route multiple pages in one call with source→output mappings.
- **Brock**: orchestration, cross-document consistency checks, keyword strategy decisions, technical SEO layer, deploy verification

Route via `hermes --profile <profile> chat -q "..." --quiet` for agent-to-agent handoffs. For long-running jobs (600s+): use `background=true notify_on_complete=true`.

## Execution principle

When Jared says "continue the journey" or "run this until complete" or "take control and ensure it gets done", do not ask clarifying questions for tactical decisions within authority. Make the call, document it, and keep moving. Only stop for: pricing decisions, legal risks, or catalogue changes that affect public claims.

When running multiple pipeline stages, use `background=true notify_on_complete=true` for long agent jobs so they run in parallel while you advance other work. Fire Serge, Polly, and Bob simultaneously when their inputs are independent.

## Tool quirks and fixes

Load `references/tool-quirks-and-fixes.md` for execute_code file corruption fixes and patch matching gotchas encountered in SEO content production.

## Deploy timing and verification

Load `references/deploy-timing-and-verification.md` for Vercel propagation lag patterns, full-route verification after push, and custom domain check procedures.

Load `references/performos-domain-config.md` for the full domain configuration — which URLs are live, which are broken, and why the apex `performos.com.au` does not resolve.

## Cross-document consistency

When pillar drafts get updated, check all downstream documents for staleness:
- Article briefs may reference old instrument names
- Internal link tables may point to removed pages
- FAQ pages may miss new categories
- Build briefs may specify wrong instrument counts or status labels

The pillar draft is the source of truth for the current catalogue. If an instrument name changes there, every other file in the cluster must follow.

## Homepage and footer governance — avoid over-explaining

When Jared is rebuilding the PerformOS homepage after feedback that a prior site felt too full, treat the homepage as a clean front door, not a full sales page. The homepage should create the next question, not answer every question.

**Homepage rules:**
- One buyer-level message, one primary CTA, and three solution routes max.
- Keep the hero concise: one headline, one short subhead, one button where possible.
- Do not add a second CTA just for visual balance if the next section already routes to solutions.
- If detail only matters after the buyer shows intent, move it to the relevant deep page.
- AgentOS is the approved deep-dive page for private AI agents. Do not re-review or reopen AgentOS unless Jared explicitly asks.

**Footer rules:**
- Use the footer as a quiet navigation layer, not a junk drawer.
- Recommended columns: PerformOS, Solutions, Resources, Company, Legal.
- Keep footer body copy to one short positioning sentence.
- Put SEO depth into subpages such as `/faq.html`, `/privacy.html`, `/terms.html`, `/contact.html`, later `/security.html` and `/pricing.html`.
- Do not put the full FAQ on the homepage. Add only a small link such as “Have questions? Read the FAQ.”

**Sergio/Serge SEO lane:** route Sergio/Serge to produce FAQ keyword map, footer internal-link structure, page titles, meta descriptions, FAQ schema, and buyer-intent search terms. Do not let SEO rewrite the homepage into a dense explainer.

**Current recommended main-site hero direction:**
- H1: “Build the AI layer your business actually uses.”
- Subhead: “PerformOS creates private agents, practical tools, and AI adoption programmes that help teams work smarter.”
- CTA: “Book a conversation.”

## Homepage pivot — course-as-front-door (direct edit, no pipeline)

When PerformOS pivots the homepage to a new primary offer while keeping instruments/programmes as ecosystem credibility behind it, use targeted patches on the existing HTML rather than a full Serge→Polly→Bob pipeline rerun. This pattern applies when:

- The offer changes but the instrument catalogue, film, about section, and design system stay intact
- Jared is giving real-time copy direction (not briefing Serge to draft blind)
- Speed matters — LinkedIn ad traffic lands here

### What changes vs what stays

**Changed (targeted patches):**
- Meta tags (title, description, OG)
- JSON-LD Organization description
- Nav (add new primary link, update CTA button)
- Hero (H1, subhead, intro, CTAs — complete rewrite)
- Lanes section (reorder, new featured lane for the offer)
- Commercial model section (reframe around the new offer)
- FAQ preview (swap questions to match the new offer)
- CTA band (new headline and CTA)
- Footer tagline and services links
- About/operator section (add origin story for the new offer)

**Stays untouched:**
- Hero film (four instruments cycling — proof of capability)
- Instrument catalogue section
- Design system CSS (ivory/ink, fonts, responsive breakpoints)
- JSON-LD structure (@graph with Organization + WebSite)
- GA4 placeholder, theme-color, favicon, font preconnects
- Nav links for existing inside pages (Catalogue, Transformation, Implementation, Workshop, Studio)
- Footer catalogue and studio columns

### Course copy rules

When writing course copy for the homepage, use concrete specificity over abstract claims:

- **Right:** "If you learn best in 20-minute daily sprints, that is what you get. If three minutes at a time through video works better, that is the plan. If you want explicit step-by-step instructions, they are written for you."
- **Wrong:** "Personalised to your learning style." / "Learn your way."

List the actual modalities (time blocks, formats, instruction types). Make the customisation feel tangible. The reader should see themselves in one of the examples.

### Deploy

```bash
cd "/Users/jc/Desktop/Website - PerformOS"
git add index.html
git commit -m "Pivot homepage: [one-line description of new offer]"
git push origin main
```

Vercel auto-deploys. Verify both URLs return 200:

```bash
curl -s -o /dev/null -w "vercel: %{http_code}" "https://performos-com-au.vercel.app/" && echo "" && curl -s -o /dev/null -w "www: %{http_code}" "https://www.performos.com.au/"
```

Always report both live URLs after deploy: `performos-com-au.vercel.app` and `www.performos.com.au`.

**Note on apex domain:** `performos.com.au` DNS A record fixed to `76.76.21.21` on 26 May 2026. The apex is blocked by dual-project Vercel assignment (remove from stale project in Vercel Dashboard). `www.performos.com.au` and `performos-com-au.vercel.app` are both live. Never report `performos.com` — not owned.

### Key principle

The homepage is the LinkedIn landing page. The new offer leads. Everything else — instruments, programmes, about — sits behind it as proof of credibility and real capability. Do not delete the ecosystem. Reframe the front door.

## Homepage — two-business framing

When PerformOS is positioned as two distinct offerings (software instruments + AI transformation consulting), the homepage must communicate both clearly without collapsing into one.

**Four-lane structure:**
- **Transform** — "We turn up and do it." AI organisational transformation. Assessment, agent architecture, team training, workflow build, custom agents. Links to `/ai-transformation.html`.
- **Learn** — "We train your team." AI Fluency Workshop. Half-day. On-site or remote. Links to `/ai-fluency-workshop.html`.
- **Implement** — "We redesign your workflows." Four-week sprint. Fixed scope, fixed price. Links to `/ai-implementation.html`.
- **Use** — "We ship instruments you own." Self-serve software. Four instruments, buy once own forever. Links to `/catalogue.html`.

**Key principles:**
- Lead with the full-service promise ("We turn up. We train your team. We redesign your workflows. We ship the instruments.") — not the software.
- Each lane starts with a bold done-for-you verb ("We train your team." / "We redesign your workflows." / "We ship instruments you own.").
- The Transform lane is the entry point for most operators — position it first.
- Meta description must mention both businesses: "We turn up and transform your operation, or you deploy our instruments yourself."

## AI Transformation page pattern

A full-service consulting page distinct from the software catalogue. Structure:

1. **Hero:** "Safe adoption. Real workflows. No consulting circus."
2. **Five-step process:** Assess → Design → Train → Build → Stay
3. **What we do not do** section — subscription rejection, over-engineering, report-writing, lock-in, over-automation
4. **Safe AI adoption framework** — Boundaries first, Human review built in, Team fluency before tool adoption, Start small ship fast compound. Anchor one principle in concrete product evidence (e.g. Pocket Customer scorecards).
5. **Custom agents section** — distinct from catalogue instruments, same commercial model
6. **Who this is for** — operator persona list
7. **CTA** — "If we cannot help, we will tell you before you spend a dollar."

**Polly checks specific to transformation page:**
- "We stay" section must have a support boundary (e.g. 90 days post-launch included, then studio rates). Unbounded ongoing support is an over-promise.
- "We do not build platforms" → replace with "We do not over-engineer" ("platform" is OUT vocabulary even in negative frame).
- Safe AI framework must include one concrete product example, not read as generic consulting methodology.

## Common pitfalls

1. **Skipping Polly on article drafts that list products.** This is how paused products ship in public content. Always route article drafts to Polly with explicit instruction to verify product state.

2. **Forgetting to update article briefs after pillar edits land.** When the pillar draft changes (instruments renamed, catalogue updated), article briefs must be checked for stale instrument names. Stale briefs produce drafts listing products that no longer exist or have changed status.

3. **Patch matching too broadly in HTML.** When using patch on HTML with repetitive structures (like FAQ Q&A blocks), include unique surrounding elements in old_string. One over-broad match can swallow adjacent content. If a patch removes more than intended, restore from memory and try again with more context.

4. **execute_code read_file returning line number prefixes.** The `read_file` function in `execute_code` returns content WITH line number prefixes. Writing that back via `write_file` corrupts the file. Use `terminal` with Python regex to strip prefixes, or use the standalone `patch` tool for text replacements.

5. **Placeholder links not resolved before marking draft ready.** CTA links that read "[Book the workshop → link to /contact or Calendly embed]" are draft markup, not copy. Always resolve to live links before marking a draft ready for build.

6. **Duplication after batch replacements.** When using execute_code with a list of (old, new) tuples, check for adjacent sections that may create duplicate paragraphs after replacement. Polly catches these; apply fixes immediately.

7. **Removing an instrument from a table but not from body copy.** When removing a product from the operational-problem table, also remove it from the instruments-not-platforms paragraph, the catalogue intro, and any other inline mentions.

8. **Not updating the link table when removing instruments.** If PulseCheck rows are removed from articles and the pillar, the link table must follow. Orphaned link table rows referencing removed pages create dead-end UX.

9. **Undo cascade from stale product-state data.** Removing an instrument from 5+ files (pillar draft, article draft, link table, FAQ page, build brief) based on agent context data that turns out to be stale creates a costly undo. Before executing a product removal across the cluster, confirm with Jared directly — do not trust Polly's context-export data alone. One founder confirmation saves 12 patches in reverse.

10. **Not verifying deployment after git push.** Pushing to main triggers Vercel auto-deploy, but propagation lag and silent failures are invisible without verification. Always `vercel inspect` and curl each new route. A 200 on the homepage does not mean the new pages resolved. If routes 404 after inspect shows Ready: `sleep 15` then retry.

11. **Forgetting to update the build brief after product-state changes.** If PulseCheck is removed/restored in the pillar and articles, the Bob build brief must be updated before build. Stale build briefs produce HTML that contradicts source drafts.

12. **PulseCheck 360 naming inconsistency.** Standardise to "PulseCheck 360" (no space) across all files before production push. Use `sed -i '' 's/Pulse Check 360/PulseCheck 360/g' *.html`. Do not touch `#pulsecheck-360` URL fragments. Verify with `grep -c`.

13. **Blog index coming-soon descriptions not matching actual drafts.** When Serge drafts the blog index before article drafts exist, Polly must verify that coming-soon descriptions match the actual article content. Mismatched teasers create reader dissonance when the article ships.

15. **Forgetting to report both live URLs after deploy.** Always report `performos-com-au.vercel.app` AND `www.performos.com.au`. Never report `performos.com.au` (apex broken) or `performos.com` (not owned). See `references/performos-domain-config.md` for full domain configuration.
