# Cinematic Dashboard Entry Pattern

Use when Jared asks to upgrade an existing deployed dashboard with a cinematic first screen, scroll-text intro, Enter gate, or HyperFrames-style motion without requesting a rendered MP4.

## Trigger language

- "first page"
- "cinematic scroll text"
- "Dashboard then the date"
- "Enter button"
- "high visual"
- "use taste / awesome design"
- "use HyperFrames skills" when the artifact remains an interactive dashboard, not a video

## Pattern

1. Preserve the existing dashboard and data flow. Do not rebuild the whole app unless the current file is broken.
2. Add a full-screen fixed intro overlay before the dashboard markup.
3. Start `body` with an `intro-active` class that hides or blurs the dashboard beneath the overlay.
4. Include:
   - Product or intelligence kicker.
   - Large cinematic title, usually `Dashboard`.
   - Updated date pulled from the existing date pill where possible.
   - Primary `Enter` button.
   - Small contextual hint, for example story count.
5. Use restrained cinematic motion:
   - large type scale
   - dark vignette
   - subtle orbit or grid layer
   - scan pass or parallax glow
   - title scroll or rise animation
   - hover sheen on the Enter button
6. Add `prefers-reduced-motion` handling.
7. On Enter:
   - add an exiting class to the overlay
   - remove `intro-active` from body
   - set `aria-hidden="true"` after the transition
8. Keep keyboard support. Enter or Escape should open the dashboard if the intro is active.
9. Keep existing filters, cards, ratings, story count, and data untouched.

## Visual direction

Good reference blend:

- Runway-style cinematic dark scene and title posture.
- Linear-style precise dark UI, subtle borders, and minimal accent use.
- Avoid generic glassmorphism. The entry should feel like a title sequence, not a SaaS modal.

## Verification checklist

- Local file loads.
- Browser vision shows the intro cleanly: title, updated date, Enter button.
- Enter button reveals the dashboard.
- Console has no JavaScript errors.
- Dashboard still shows expected count, for example `30 of 30`.
- Live Vercel URL is verified with a cache-busting query.
- Source is committed and pushed after live verification.

## Common pitfalls

- Do not rely only on accessibility snapshot for visual judgement. Use `browser_vision` for cinematic layout checks.
- Do not let the intro trap the user. Add click and keyboard exit paths.
- Do not hide the dashboard permanently if JavaScript fails. Keep the overlay logic simple.
- Do not alter the data model just to add the intro.
- Do not treat every HyperFrames mention as an MP4 request. If Jared is asking to improve an interactive dashboard, apply HyperFrames-style motion language inside the HTML. Render video only if he explicitly asks for MP4/video.