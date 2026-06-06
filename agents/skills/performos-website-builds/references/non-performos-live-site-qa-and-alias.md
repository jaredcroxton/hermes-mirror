# Non-PerformOS live site update, Bob QA, and Vercel alias pattern

Use this when Jared asks to fix or polish an existing non-PerformOS static site, demo site, gym page, lead dashboard, or client-facing visual artifact.

## Workflow correction from Jared

Jared corrected the process after a live gym site shipped with visible mobile/layout issues:

- Do not hand back a client-facing visual artifact without Bob-level visual QA.
- If text escapes cards or a design still looks like a mockup, fix and redeploy. Do not explain the blocker if a local deployment path exists.
- If Vercel token auth fails, check the local Vercel session before declaring deployment blocked.

## Required sequence

1. **Capture the actual correction.** If Jared marks up a screenshot or says an element was only an example, update the build brief and artifact immediately.
2. **Use Bob for visual QA.** Bob_Builder should inspect phone and desktop layout before final handoff. If Brock must move fast, Brock can deploy, but Bob's QA expectations still govern the checks.
3. **Remove mockup cues.** Browser chrome, red/yellow/green dots, fake URL pills, “panel preview” labels, and example placeholder images must be removed unless Jared explicitly wants a mockup aesthetic.
4. **Use real supplied imagery.** If Jared sends images, use them as the visual direction. Prefer images with left-side negative space for hero copy and subject weight on the right.
5. **Verify live, not just local.** Use the public URL with a cache-busting query after deployment.
6. **Run viewport checks.** Minimum widths: 320, 360, 375, 390, 430, 768, and 1280. Confirm document/body `scrollWidth` equals viewport width and no obvious element clipping.
7. **Check console messages.** A favicon 404 still counts as a quality issue on final handoff. Add an inline SVG favicon if needed.
8. **Update the original URL.** If Vercel creates a new project/deployment, assign the existing production alias back to the new deployment.

## Vercel auth lesson

A rejected `VERCEL_TOKEN` does not mean deployment is blocked. Check local login:

```bash
npx -y vercel whoami
```

If it returns Jared's account, deploy from the artifact directory:

```bash
npx -y vercel deploy --prod --yes
```

If that creates a new Vercel project or different deployment URL, move the original alias:

```bash
npx -y vercel alias set <new-production-url> <original-clean-domain>.vercel.app
```

Then verify:

```bash
curl -I https://<original-clean-domain>.vercel.app/ | head
```

## Final handoff standard

Only tell Jared it is done after:

- Public URL returns HTTP 200.
- Original clean URL points to the new deployment.
- Phone and desktop checks pass.
- No sideways overflow.
- No console/page errors.
- Screenshot or visual inspection confirms mockup/example elements are gone.
