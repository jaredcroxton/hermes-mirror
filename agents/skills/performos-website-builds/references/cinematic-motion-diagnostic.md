# Cinematic Motion Diagnostic — Why a Site Does Not "Flow"

Use this when Jared shares a live URL and says it does not feel as good as a reference site, or asks why his build lacks the "epic flow" of a showcase example.

## Trigger

- Jared shares his site and a reference site and asks why his does not feel the same
- Jared says his site "does not flow" or "feels flat" or "lacks the epic feel"
- Any session where motion quality, scroll experience, or cinematic feel is the review target

## The Three Gaps (in order of impact)

When a site looks beautiful but does not feel cinematic, the cause is almost always one of these three things.

### 1. No Scroll-Driven Motion — "Posters vs. Film"

**The tell:** Sections are visually distinct compositions stacked vertically. Scrolling moves you from one poster to the next. Each section is its own visual world with no connective tissue.

**The fix:** Scroll position must drive the animation timeline. As the user scrolls, visuals must move, reveal, transform, or transition in real time. The scroll bar IS the playhead. The site should feel like one continuous film, not a sequence of static compositions.

**Technical stack that achieves this:**
- GSAP ScrollTrigger (pins sections, binds element position to scroll progress, scrub tied to a runway div not body)
- Lenis smooth-scroll (removes native scroll jerk, enables buttery interpolation — but NOTE: Lenis can fight display:none lock/unlock patterns; the APOGEE reference build removed it twice)
- Frame extraction from video (Higgsfield, Seedance, Kling) for scroll-synced motion clips

**Diagnostic question to ask:** "When I scroll, does the image move with me or does a new section just appear?"

**Specific implementation patterns (verified in APOGEE build and Higgsfield showcase sites):**

Pin the hero and create scroll-driven zoom/reveal:
```javascript
gsap.to('.hero-background', {
  scale: 1.15, opacity: 0, ease: 'none',
  scrollTrigger: {
    trigger: '.hero-section', start: 'top top', end: 'bottom top',
    scrub: true, pin: true,
  },
});
```

Crossfade between sections (opacity, not hard cuts):
```javascript
gsap.fromTo('.section-2',
  { opacity: 0 },
  { opacity: 1, ease: 'none',
    scrollTrigger: {
      trigger: '.section-2', start: 'top 80%', end: 'top 20%', scrub: true,
    },
  }
);
```

Parallax depth (background moves slower than foreground):
```javascript
gsap.to('.section-background', {
  yPercent: -15, ease: 'none',
  scrollTrigger: {
    trigger: '.section', start: 'top bottom', end: 'bottom top', scrub: true,
  },
});
```

Persistent scroll-line element:
```javascript
gsap.to('.scroll-line', {
  scaleY: 1, ease: 'none',
  scrollTrigger: {
    trigger: 'body', start: 'top top', end: 'bottom bottom', scrub: 0.5,
  },
});
```

Micro-motion on text (gentle fade-in, slide-up):
```javascript
gsap.from('.section-heading', {
  y: 30, opacity: 0, duration: 1, ease: 'power2.out',
  scrollTrigger: {
    trigger: '.section-heading', start: 'top 85%',
    toggleActions: 'play none none reverse',
  },
});
```

### 2. No Transition Choreography — "Hard Cuts vs. Seamless Scenes"

**The tell:** Each section is its own visual world. There is no connective tissue between sections. The experience feels like flipping pages.

**The fix:** Elements must persist across section boundaries. A visual motif, glow, particle system, or character stays on screen while the background shifts around it. Sections feel like scenes in one continuous film.

**Techniques:**
- Opacity crossfades between sections (not hard cuts)
- Persistent visual element that travels through the entire scroll
- Parallax layering (foreground text moves faster than background imagery)
- Overlapping section boundaries (next section begins before the current one ends)

**Diagnostic question to ask:** "If I screenshot the boundary between two sections, is there a visual element that appears in both?"

### 3. No Micro-Motion — "Still Image vs. Living Page"

**The tell:** The page is visually still when the user is not scrolling. Nothing moves. No life.

**The fix:** Subtle constant motion that makes the page feel alive even at rest.

**Techniques:**
- Particle systems drifting in the background
- Slow ambient light shifts or gradient animations
- Film grain texture overlay
- Character breathing or idle animation (if using video assets)
- Subtle parallax on background elements
- Floating objects with gentle CSS keyframe motion

**Diagnostic question to ask:** "If I stop scrolling and stare at the page for five seconds, does anything move?"

## The Higgsfield Pattern (Reference Standard)

The Higgsfield + Claude Code showcase sites achieve epic flow through a specific pipeline:

1. **Generate video clips** using Seedance, Kling, or Veo through Higgsfield MCP
2. **Extract frames** from those clips at key moments
3. **Build scroll-driven layout** using GSAP ScrollTrigger + Lenis
4. **Bind frame display to scroll position** so the video plays as you scroll
5. **Add cinematic effects** (film grain, particles, vignette, glass cards, color tints)
6. **Layer parallax** so multiple visual layers move at different speeds

The "epic" feeling comes from the video-quality motion, not the web framework. The web framework just makes it scroll-synced.

## How to Communicate This to Jared

Do not say "you need GSAP ScrollTrigger." Jared is not a developer by background.

Say: "Your site is four beautiful posters stacked vertically. To get the epic flow, those four posters need to become one continuous scene where scrolling moves you through the journey. Right now scroll is just navigation. It needs to be the thing that drives the motion."

Then specify which of the three gaps is the biggest issue and what the single highest-impact fix is.

## What to Recommend

For Jared's builds specifically:
- If he wants Higgsfield-level motion: he needs to generate video clips, extract frames, and build a scroll-driven site around those frames
- If he wants to improve what he has: add Lenis smooth-scroll + GSAP ScrollTrigger to bind existing visuals to scroll position
- Quick win: add one persistent visual element and a crossfade between sections. This alone transforms the feel.

## Pitfall

Do not recommend "add more animations" as the fix. Random animations on a static site make it worse, not better. The fix is always about making scroll position drive the experience, not about adding decorative motion.

## APOGEE-Specific Notes

The APOGEE site (apogee-ivory.vercel.app) uses a frame-sequence scrub approach (canvas-based, not video element). This is the highest-quality approach but requires:
- Video generation via KIE API (nano-banana keyframes + Seedance clips)
- Frame extraction and WebP conversion
- Canvas rendering with GSAP ScrollTrigger scrub
- Load gate (first N frames paint before scroll unlocks)
- Mobile portrait frame set (separate 720x1080 center-crop)

The APOGEE build removed Lenis because its cached scroll-limit fights display:none lock/unlock. Native scroll plus ScrollTrigger scrub is the smoothing. When evaluating whether to use Lenis, check if the site uses display:none to lock/unlock sections. If yes, skip Lenis. If no, Lenis is safe to add.
