# Animation Skill Testing Protocol

Proven smoke test templates for every animation skill in pack 14. One fresh chat per test. Format: "Read [skill path] completely. Then review this animation request against the [skill] framework: [description]."

## GSAP
A marketing page needs a stats section. Three numbers counting up from 0 to their target (12,487, 94, and 3.2M) when the section scrolls into view. Each counter appears one after the other with a 200ms stagger. The section also has a horizontal scroll gallery of 8 product images that scrubs through as the user scrolls. After the gallery, a pinned quote section with text that fades in word by word as the user continues scrolling.

Expected: timeline with stagger, ScrollTrigger for gallery scrub, pin + scrub for quote. Should not route elsewhere.

## Motion
A React dashboard. A sidebar that expands on hover with a smooth width transition. Cards in a grid that reorder when a filter is applied — the cards should animate to their new positions. A tab bar where the active indicator slides between tabs with a spring. A modal that fades in and scales up when opened. A notification badge that bounces when the count changes.

Expected: layout animations for card reorder, layoutId for tab indicator, AnimatePresence for modal, spring for badge, whileHover for sidebar. Must flag width-as-animate violation. Must require reduced-motion path.

## Locomotive
A portfolio site for an architecture firm. Full-page smooth scroll with inertia. A sticky project title that pins while images scroll past. Parallax on background elements at 0.5x speed. Section progress indicators that fill as the user scrolls through each project. On mobile, all smooth scroll disabled — native scroll only.

Expected: init with mobile disable, data-scroll-sticky, data-scroll-speed, scroll events for progress. Must enforce mobile fallback.

## Anime
A lightweight landing page with no frameworks. An SVG logo that draws its path on load. Three feature cards that animate in on scroll with a stagger. A CTA button with a subtle pulse loop. All under 15KB of animation code total. Must work vanilla — no React, no GSAP.

Expected: SVG line-drawing, timeline with stagger, pulse loop. Must route pulse to CSS (infinite JS loop anti-pattern). Must catch version pin (v3 vs v4). Must mandate reduced-motion.

## Barba
A creative agency site with three pages: Home, Work, About. When navigating between pages, the current page content should fade out, then the new page content should slide up and fade in. The transition should take 600ms total. No full page reload. URLs must update. The browser back button must work.

Expected: init with views, fadeOut/fadeIn transitions, namespace routing, pushState. GSAP can drive actual animations but Barba orchestrates.

## Lottie
A fintech app needs an animated savings goal celebration. A designer has created the animation in After Effects: a piggy bank bounces, coins fall, confetti bursts, and a number counter rolls up. The animation is 3 seconds, loops once. It must play when the user reaches their savings goal. File size must stay under 80KB. Mobile must not autoplay — respect prefers-reduced-motion.

Expected: counter split (code overlay, not baked), confetti budget warning, Bodymovin export gotchas (particles don't survive, drop shadows fail), reduced-motion path.

## Rive
An interactive settings toggle. Three states: off, on, and locked. Each state has a distinct animation designed in Rive. Tapping toggles between off and on. Long-pressing locks the current state. The button must respond to hover on desktop. Must degrade gracefully when Rive runtime fails to load.

Expected: state machine with three states, input wiring for tap/long-press/hover, runtime fallback.

## Spring
A gallery page. Images enter with a staggered spring animation as they scroll into view. Clicking an image opens a detail view with a spring transition. Dragging the detail view down closes it with a physics-based dismiss. The drag must feel natural — no fixed thresholds, the spring takes over on release.

Expected: useSpring for staggered reveal, useSpring + useDrag for dismiss, stiffness/damping config.

## View Transitions
A blog with list and detail views. Clicking a post thumbnail morphs it into the detail header image using the View Transitions API. The title and excerpt also morph between list and detail positions. Browser back button must reverse the transition smoothly.

Expected: startViewTransition, view-transition-name on thumbnail and header, fallback for browsers without API support.

## Scroll Reveal
A long-form case study page with 8 sections. Each section reveals with a fade-up animation as it enters the viewport. Sections 3 and 6 have parallax background images. The reveal stagger is 80ms per element within a section. On mobile, transforms only — no fixed backgrounds.

Expected: IntersectionObserver with unobserve() for once-only, stagger timing, parallax via translate, reduced-motion override.

## Animated Components
A SaaS onboarding flow. A progress stepper with animated step transitions. A card that flips on click to reveal details. A toast notification that slides in from the top. A skeleton loader that matches the final layout shape. All components must be keyboard-accessible and respect reduced-motion.

Expected: component specs for each element, accessibility requirements, reduced-motion fallbacks.

## CSS Animations
A loading state for a dashboard. Three pulsing dots with a staggered animation. A skeleton screen with a shimmer sweep. A progress bar that fills smoothly. All animations must run on the compositor (transform + opacity only). Must respect prefers-reduced-motion by switching to static states.

Expected: @keyframes with transform/opacity only, animation-delay for stagger, reduced-motion override, CSS-is-enough boundary (no JS library needed).
