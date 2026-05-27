# Mobile HTML deck QA

Session learning: Jared explicitly expects HTML slide decks to be built and verified for mobile, not only desktop.

## Minimum mobile QA

Verify at `375 x 812` before delivery.

Check:

- Headline is readable and not clipped.
- Body copy wraps cleanly.
- Logo does not overlap core content or visual panels.
- Navigation arrows and dots fit inside the viewport.
- Dot buttons are not accidentally enlarged by broad selectors.
- Visual panel fits above the navigation.
- Content does not sit behind the nav bar.
- Source/footer text is hidden, moved, or reduced if it crowds the phone viewport.
- Touch swipe support exists.

## CSS pitfall

Avoid this selector for mobile sizing:

```css
.nav button { ... }
```

It also targets dot buttons inside `.dots`, which can make slide dots huge on mobile.

Prefer:

```css
.nav > button { ... }
```

Then style dots separately:

```css
.dotbtn { width: 7px; height: 7px; }
.dotbtn.active { width: 20px; }
```

## Useful verification pattern

If Playwright is available via npx and local browser channel is installed:

```bash
npx -y playwright screenshot --channel=chrome --viewport-size=375,812 \
  file:///absolute/path/to/deck.html /tmp/mobile-deck-check.png
```

Then inspect the screenshot visually. If using vision analysis, ask specifically about navigation, logo overlap, clipping, readability, and mobile layout.

## Deployment rule

If mobile fixes are made after the initial deploy:

1. Re-check no em dashes.
2. Commit the HTML change.
3. Push to GitHub.
4. Redeploy to Vercel.
5. Reopen the live URL.
