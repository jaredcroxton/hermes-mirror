# Pasted HTML dashboard rescue pattern

Use when Jared pastes raw HTML from another agent, server, Brev sandbox, or terminal output and wants it opened, built, or turned into a reviewable dashboard.

## Trigger

- "He's given me the HTML to give to you to build."
- Raw `<!DOCTYPE html>` content pasted into chat.
- HTML came from a remote server where `localhost:<port>` is not directly accessible.
- Jared needs a clickable link quickly.

## Workflow

1. Treat the pasted HTML as the source, but do not assume it is production-ready.
2. Save it as a single-file artifact under `~/Desktop/hermes_builds/<descriptive-project>/index.html`.
3. Repair obvious paste damage:
   - wrapped URLs split across lines
   - broken indentation or missing closing tags
   - inaccessible link colors
   - tiny mobile hit targets
   - hard-to-read default browser styling
4. Keep the original content and links intact unless they are visibly broken.
5. Upgrade the visual shell enough for executive review:
   - clean hero/header
   - card grid
   - responsive layout
   - search/filter if there are multiple cards
   - clear source labels and action buttons
6. Add `vercel.json` only when a public click link is useful.
7. Verify locally first:
   - start a simple HTTP server from the artifact directory
   - open in browser
   - check card count and external link count
   - check console errors
   - strip em dashes
8. If Jared needs phone/gym review or a link, deploy with `vercel --prod --yes` and verify the production alias returns HTTP 200.
9. Stop the local server after deployment.

## Verification checklist

- File exists and opens locally.
- Visible title matches the requested dashboard.
- Expected cards/links render.
- No console errors.
- Production URL returns HTTP 200 if deployed.
- Final reply gives the live link first, then local path and verification.

## Pitfall

Do not over-explain remote port forwarding once Jared has supplied the HTML. The task has shifted from remote access troubleshooting to build-and-publish. Build the artifact and give him the review link.