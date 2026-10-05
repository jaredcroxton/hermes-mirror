# Deploy Timing and Verification Patterns

## Vercel propagation lag

**Symptom:** After `git push origin main`, `vercel inspect` shows deployment status Ready within seconds, but new page routes return 404.

**Root cause:** Vercel's CDN edge propagation lags behind the build-complete signal. The deployment is marked Ready when the build finishes, but edge nodes may take 10-20 seconds to pick up new static files.

**Fix:** After `vercel inspect` returns Ready, wait 15 seconds before curling new routes. If routes still 404, wait another 10 seconds and retry. Do not report deployment failure on first 404.

```bash
sleep 15
for page in blog-new-page-1 blog-new-page-2; do
  code=$(curl -s -o /dev/null -w "%{http_code}" "https://performos-com-au.vercel.app/${page}.html")
  echo "$page.html → $code"
done
```

## Full-route verification after push

After deploying new pages, verify ALL new routes, not just a spot check. A passing homepage does not mean new routes resolved.

**Pattern:**
```bash
for page in page1 page2 page3 page4 page5; do
  code=$(curl -s -o /dev/null -w "%{http_code}" "https://performos-com-au.vercel.app/${page}.html")
  echo "$page.html → $code"
done
```

All must return 200. If any return 404, wait and retry the full set. If persistent 404s after 60 seconds, check git for uncommitted files or missing pushes.

## Custom domain check

**Current state (26 May 2026):**
- `https://www.performos.com.au` — LIVE. SSL active. Works.
- `https://performos.com.au` (apex, no www) — BROKEN. DNS A record is `216.150.1.1` instead of Vercel's `76.76.21.21`. Will not resolve until DNS is fixed.
- `performos.com` — NOT OWNED by PerformOS. Do not use.

Always verify both live URLs after deploy:
```bash
curl -s -o /dev/null -w "vercel: %{http_code}" "https://performos-com-au.vercel.app/" && echo "" && curl -s -o /dev/null -w "www: %{http_code}" "https://www.performos.com.au/"
```

See `references/performos-domain-config.md` for full details including the apex DNS fix instructions.

After deploy, test the custom domain as well. It may resolve separately from the Vercel subdomain:

```bash
curl -s -o /dev/null -w "%{http_code}" "https://performos.com.au/"
```

If the custom domain returns 000 (connection error) while the Vercel subdomain returns 200, DNS is not configured. The user needs to set A/CNAME records in their domain registrar dashboard pointing to Vercel.
