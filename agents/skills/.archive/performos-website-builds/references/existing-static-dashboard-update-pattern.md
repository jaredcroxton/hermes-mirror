# Existing static dashboard update pattern

Use when Jared asks to update an already-live static dashboard or web utility, especially an existing Vercel project such as Trending AI Pulse.

## Trigger
- Jared gives a live Vercel URL and asks to keep the same flow/cards/layout but refresh data, date, copy, or a visible label.
- The request is an update to an already-deployed tool, not a new PerformOS marketing-site strategy build.

## Pattern
1. Locate the local repo from known build paths first, commonly `/Users/jc/Desktop/hermes_builds/<slug>`.
2. Inspect the source files before editing. For single-file dashboards, check both the visible HTML and any mirrored source data file such as `data/sample.json`.
3. Preserve structure unless Jared explicitly asks for redesign:
   - same card order
   - same filters
   - same IDs where possible
   - same metadata fields
   - same UI flow
4. If the page embeds data in HTML, update both:
   - the source data file
   - the embedded `RAW_DATA` or equivalent HTML payload
5. Add or update a visible date marker when the user asks for “today's date” so the change is obvious on the page, not only hidden in timestamps.
6. Validate with scripts before deployment:
   - JSON parses
   - expected item count is unchanged
   - visible date string exists
   - key first/last records still exist
7. Open the local page or dev server and verify in-browser with DOM/console checks, not just file inspection.
8. Deploy with Vercel production from the repo:
   - `npx vercel --prod --yes`
9. Verify the production alias with a cache-busting URL in the browser:
   - `https://<site>.vercel.app/?v=<yyyymmdd>-verify`
10. Commit and push the changed source files after successful deployment when git is configured.

## Verification standard
Report only after real checks show:
- production alias loads
- expected count/card total renders
- visible date is correct
- core flow still works
- git commit/push result if attempted

## Firecrawl/cache pitfall
Firecrawl may return cached or stale extraction for a Vercel page even after deployment. If metadata indicates a cache hit or the extracted data is clearly stale, do not treat that as authoritative. Use direct browser verification with a cache-busting URL and DOM/console checks.

## Scope control
Do not commit unrelated untracked files such as local `memory/`, `.gitignore`, or `vercel.json` unless Jared explicitly asks. Commit only the files required for the update.
