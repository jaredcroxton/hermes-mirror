---
name: scrubbed-crossfade-fly-through
description: GSAP-scrubbed crossfade pattern for still-image stage-switcher fly-throughs. Replaces binary class toggle with scroll-driven opacity timelines.
---

# Scrubbed Crossfade Fly-Through

## When to use

When building a scroll-driven page with multiple full-bleed backdrop images that should crossfade smoothly as the user scrolls. Four stages. Four backdrops. No hard cuts.

## The problem

Binary class toggle (`.active`) with CSS `transition: opacity 1.2s` fires at a single scroll point. Two backdrops are simultaneously semi-opaque during the fade, or the transition feels like a hard cut.

## The fix

Replace CSS transitions with GSAP-scrubbed opacity timelines. Each backdrop gets a timeline that animates its opacity from 0 to 1 to 0 continuously across the runway. The scrub ties opacity to scroll position, so the crossfade is proportional to how far the user has scrolled.

## Architecture

```
.runway (position: relative, 500vh)
  ├── .scene (position: sticky, top: 0, 100vh)
  │     ├── .bg-layer[0] (opacity scrubbed 0→1→0 via GSAP)
  │     ├── .bg-layer[1]
  │     ├── .bg-layer[2]
  │     ├── .bg-layer[3]
  │     ├── .scrim (shared atmosphere)
  │     └── .stage-deck (panels, switched at markers)
  └── .stage-marker[0..3] (absolute, top: 0%, 25%, 50%, 75%)
```

## Critical CSS rules

- `html, body { overflow-x: clip }` — NOT hidden. Hidden creates a scroll container that breaks position: sticky.
- `.bg-layer { position: absolute; inset: 0; opacity: 0; visibility: hidden }` — NO CSS transition. GSAP owns opacity.
- No transform on any ancestor of `.scene` — creates a containing block that kills sticky.

## The GSAP pattern

```javascript
bgLayers.forEach(function (layer, i) {
  var fadeInStart  = i * segment;
  var fadeInEnd    = fadeInStart + segment * 0.6;
  var fadeOutStart = (i + 1) * segment - segment * 0.4;
  var fadeOutEnd   = (i + 1) * segment;

  var tl = gsap.timeline({
    scrollTrigger: {
      trigger: "#runway",
      start: "top top",
      end: "bottom bottom",
      scrub: 0.8
    }
  });

  // 0 → fadeInStart: opacity 0
  // fadeInStart → fadeInEnd: opacity 0 → 1 (power2.inOut)
  // fadeInEnd → fadeOutStart: hold at 1
  // fadeOutStart → fadeOutEnd: opacity 1 → 0 (power2.inOut)
  // fadeOutEnd → 1: hold at 0
});
```

## Pitfalls

- **Markers inside the sticky scene.** Their `top:%` resolves against 100vh, not the 500vh runway. All markers collapse into the first viewport. Stage switching freezes. Fix: markers must be direct children of `.runway`.
- **CSS transition on bg-layer.** GSAP scrub writes opacity every frame. A CSS transition fights it, producing jitter or delayed fade. Strip the transition.
- **overflow-x: hidden kills sticky.** Use `overflow-x: clip` instead.
- **panel switching is still binary.** Panels sit above the crossfaded backdrop. A clean swap at the marker is correct. Do not scrub panel opacity.
