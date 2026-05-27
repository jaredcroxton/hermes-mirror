# PerformOS Website Management

**Class:** Operate/patch the live PerformOS website
**Proven:** 2026-05-26 — full site pivot executed (homepage rewrite, course page creation, 6 page nav updates) + DNS fix (apex A record updated to Vercel IP) + competitive teardown methodology established
**Parent:** `claude-code-builder`

## References

- `references/dns-troubleshooting.md` — DNS diagnostics, GoDaddy fix steps, known host issues
- `references/competitive-teardown.md` — Competitor scraping and white space analysis methodology

## Site inventory

```
/Users/jc/Desktop/Website - PerformOS/
├── index.html              — Homepage (primary landing)
├── course.html             — 12-week course sales page
├── catalogue.html          — Four instruments
├── ai-transformation.html  — Organisational transformation
├── ai-implementation.html  — Four-week sprint
├── ai-fluency-workshop.html— Half-day workshop
├── ai-agents.html          — Custom agents
├── about.html              — Studio/about
├── contact.html            — Contact
├── faq.html                — FAQ (design system source of truth)
├── blog.html               — Blog index
├── blog-*.html             — 6 blog articles
├── robots.txt
└── sitemap.xml
```

## Infrastructure

- **Repo:** `/Users/jc/Desktop/Website - PerformOS/` — same folder _is_ the git repo
- **Remote:** `https://github.com/jaredcroxton/performos-com-au.git` (main branch)
- **Deploy:** Vercel project `performos-com-au` — auto-deploys on every push to main
- **Live URLs:**
  - `https://performos-com-au.vercel.app` (Vercel subdomain, always works)
  - `https://www.performos.com.au` (custom domain, SSL active)
  - `https://performos.com.au` (apex) — DNS A record updated from `216.150.1.1` to `76.76.21.21` on 26 May 2026. DNS confirmed propagated (`dig +short performos.com.au A` → `76.76.21.21`). Domain is connected to TWO Vercel projects (`performos-com-au` and `performos`). This dual-project assignment likely blocks SSL provisioning. Fix: remove from the `performos` project in Vercel Dashboard → Settings → Domains. The CLI does not support per-project domain removal — dashboard only. After removal, SSL auto-provisions within minutes.
- **DNS managed at:** GoDaddy (ns35/ns36.domaincontrol.com)
- **Vercel project name:** `performos-com-au` under `jaredcroxtons-projects`

## Deploy workflow

**Preferred path: Vercel CLI direct deploy.** Git push is blocked in Hermes's sandbox (osxkeychain credential helper cannot be reached, HTTPS token auth times out). Vercel CLI works reliably:

```bash
cd "/Users/jc/Desktop/Website - PerformOS"
git add -A
git commit -m "<description>"
vercel --prod --yes
# Deploys directly. Aliased to performos.com.au within ~8s.
```

**Fallback (only if running from Jared's terminal, not the sandbox):**

```bash
cd "/Users/jc/Desktop/Website - PerformOS"
git push origin main
# Vercel auto-deploys on push. Wait ~10s.
```

When using the Vercel CLI path, the git commit is still created but the push is skipped. The remote will lag behind the live deployment until Jared manually pushes from his terminal.

## Verify deploy

```bash
curl -s -o /dev/null -w "%{http_code}" "https://performos-com-au.vercel.app/"
curl -s -o /dev/null -w "%{http_code}" "https://www.performos.com.au/"
```

Always report both URLs after deploy. Always check HTTP 200 on both.

## Updating nav across all pages

When adding a new nav item (e.g., course link), the nav structure is:
```html
<li><a href="course.html">12-Week Course</a></li>
<li><a href="catalogue.html">Catalogue</a></li>
```
Insert new items before `catalogue.html` entry.

Core pages that share this nav: index.html, course.html, catalogue.html, ai-transformation.html, ai-implementation.html, ai-fluency-workshop.html, ai-agents.html, about.html, contact.html.

Blog pages and faq.html use different nav structures — check individually.

Use `execute_code` to batch-patch across files rather than editing individually.

## GA4

**Measurement ID:** `G-HMWH2EPLZ3` (active, replaced placeholder across all 17 pages 26 May 2026).

When creating new pages, copy the GA4 snippet from any existing page. The ID is live — do not use `G-XXXXXXXXXX`.

## Creating a new page

1. Copy the `<head>` (meta tags, OG, fonts, CSS vars), `<nav>`, and `<footer>` from `faq.html`
2. Update `<title>`, `<meta name="description">`, OG tags, canonical URL
3. Write page-specific content between nav and footer
4. Add JSON-LD schema as appropriate (Service, FAQPage, etc.)
5. Push and verify both URLs

## Common pitfalls

- **Em dashes:** Never use them. Banned site-wide.
- **Australian spelling:** colour, organise, personalised (not personalized, organize, color).
- **Apex DNS:** `performos.com.au` without www was broken due to GoDaddy A record pointing to 216.150.1.1. Fixed 26 May 2026 by updating to 76.76.21.21. If apex breaks again: check with dig and update at GoDaddy DNS dashboard.
- **File modified externally:** The site is a live git repo. If someone else pushes, your local copy may be stale. Run `git pull` before editing.
- **File overwritten mid-session:** When a tracked file appears to have reverted or been overwritten (e.g., course.html showing old content after a write), the working tree may have been reset. Restore your last known good commit with `git checkout <commit_hash> -- <filename>`, then verify the file content before redeploying.
- **Patch conflicts:** When patch() fails with "Found 2 matches", use `replace_all=true` or add surrounding context for uniqueness.
- **Git push blocked in sandbox:** `git push origin main` times out in the Hermes sandbox because the osxkeychain credential helper cannot be reached and HTTPS token auth hangs. Use `vercel --prod --yes` from the project directory instead. The git commit is created locally; Jared pushes from his terminal later.
- **Apex domain blocking:** `performos.com.au` may 404 even when the Vercel deploy URL works perfectly. This is the dual-project conflict in Vercel — both `performos-com-au` and `performos` projects claim the apex domain. Fix in Vercel Dashboard → Settings → Domains on the non-production project. CLI cannot resolve this.
