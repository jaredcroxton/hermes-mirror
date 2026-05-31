# HTML Animation Patterns for Slide Decks

Reusable animation code for PerformOS HTML slide decks. Copy these patterns into any deck that needs high-impact visual animation. All code is vanilla CSS/JS — zero dependencies.

---

## 1. Particle Canvas Background

**CSS** (add once):

```css
.particle-canvas {
  position: fixed;
  inset: 0;
  z-index: 0;
  pointer-events: none;
}
```

**HTML** (add inside `.deck`, before other bg elements):

```html
<canvas class="particle-canvas" id="particles"></canvas>
```

**JS** (add before `</script>`):

```js
(function() {
  const canvas = document.getElementById('particles');
  const ctx = canvas.getContext('2d');
  let w, h, particles = [];
  const COUNT = 60;

  function resize() {
    w = canvas.width = window.innerWidth;
    h = canvas.height = window.innerHeight;
  }
  window.addEventListener('resize', resize);
  resize();

  for (let i = 0; i < COUNT; i++) {
    particles.push({
      x: Math.random() * w,
      y: Math.random() * h,
      vx: (Math.random() - 0.5) * 0.3,
      vy: (Math.random() - 0.5) * 0.3,
      r: Math.random() * 1.5 + 0.5,
      alpha: Math.random() * 0.5 + 0.1
    });
  }

  function draw() {
    ctx.clearRect(0, 0, w, h);
    particles.forEach(p => {
      p.x += p.vx; p.y += p.vy;
      if (p.x < 0) p.x = w; if (p.x > w) p.x = 0;
      if (p.y < 0) p.y = h; if (p.y > h) p.y = 0;
      ctx.beginPath();
      ctx.arc(p.x, p.y, p.r, 0, Math.PI * 2);
      ctx.fillStyle = `rgba(59,130,246,${p.alpha})`;
      ctx.fill();
    });
    for (let i = 0; i < COUNT; i++) {
      for (let j = i + 1; j < COUNT; j++) {
        const dx = particles[i].x - particles[j].x;
        const dy = particles[i].y - particles[j].y;
        const dist = Math.sqrt(dx * dx + dy * dy);
        if (dist < 150) {
          ctx.beginPath();
          ctx.moveTo(particles[i].x, particles[i].y);
          ctx.lineTo(particles[j].x, particles[j].y);
          ctx.strokeStyle = `rgba(59,130,246,${0.08 * (1 - dist / 150)})`;
          ctx.lineWidth = 0.5;
          ctx.stroke();
        }
      }
    }
    requestAnimationFrame(draw);
  }
  draw();
})();
```

**Tuning**: Change `COUNT` for more/fewer particles. Change `150` connection distance threshold. Use brand color in fillStyle/strokeStyle.

---

## 2. 3D Perspective Slide Transitions

**CSS** (replace existing `.slide` / `.slide.active` / `.slide.exit-up`):

```css
.slide {
  position: absolute;
  inset: 0;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: flex-start;
  padding: 72px 96px;
  opacity: 0;
  visibility: hidden;
  transform: perspective(1200px) translateY(60px) rotateX(8deg) scale(0.96);
  transition: opacity 0.7s cubic-bezier(0.4, 0, 0.2, 1), transform 0.7s cubic-bezier(0.4, 0, 0.2, 1), visibility 0.7s;
  overflow-y: auto;
  background: var(--ink);
  transform-origin: center top;
}
.slide.active {
  opacity: 1;
  visibility: visible;
  transform: perspective(1200px) translateY(0) rotateX(0deg) scale(1);
}
.slide.exit-up {
  transform: perspective(1200px) translateY(-40px) rotateX(-4deg) scale(0.98);
  opacity: 0;
}
```

---

## 3. Spring Easing

**CSS variable** (add to `:root`):

```css
--ease-spring: cubic-bezier(0.34, 1.56, 0.64, 1);
```

Use `var(--ease-spring)` for cards, pills, agent rows, feature list items. Avoid on large elements like slides (causes jank).

---

## 4. Animated Gradient Card Borders on Hover

**CSS** (add `::before` pseudo-element to `.card`):

```css
.card {
  position: relative;
  overflow: hidden;
  transition: transform 0.35s var(--ease-spring), border-color 0.3s, background 0.3s, box-shadow 0.35s var(--ease-spring);
}
.card::before {
  content: '';
  position: absolute;
  inset: -1px;
  border-radius: 11px;
  background: conic-gradient(from 0deg, var(--blue), var(--violet), var(--cyan), var(--blue));
  opacity: 0;
  transition: opacity 0.4s;
  z-index: -1;
  animation: cardBorderSpin 4s linear infinite;
}
@keyframes cardBorderSpin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}
.card:hover {
  border-color: transparent;
  background: var(--ink-3);
  box-shadow: 0 8px 32px rgba(59,130,246,0.12), 0 0 0 1px rgba(59,130,246,0.1);
  transform: translateY(-2px) scale(1.01);
}
.card:hover::before {
  opacity: 0.6;
}
```

Card stagger delays with spring (0.12s between cards):

```css
.slide.active .card:nth-child(1) { transition: opacity 0.55s var(--ease-spring) 0.5s, transform 0.55s var(--ease-spring) 0.5s, border-color 0.3s, background 0.3s, box-shadow 0.35s var(--ease-spring); }
.slide.active .card:nth-child(2) { transition: opacity 0.55s var(--ease-spring) 0.62s, transform 0.55s var(--ease-spring) 0.62s, border-color 0.3s, background 0.3s, box-shadow 0.35s var(--ease-spring); }
.slide.active .card:nth-child(3) { transition: opacity 0.55s var(--ease-spring) 0.74s, transform 0.55s var(--ease-spring) 0.74s, border-color 0.3s, background 0.3s, box-shadow 0.35s var(--ease-spring); }
.slide.active .card:nth-child(4) { transition: opacity 0.55s var(--ease-spring) 0.86s, transform 0.55s var(--ease-spring) 0.86s, border-color 0.3s, background 0.3s, box-shadow 0.35s var(--ease-spring); }
```

---

## 5. Mouse Parallax on Orbs

**HTML** (add `id="orbs"` and `data-depth`):

```html
<div class="bg-orbs" id="orbs">
  <div class="orb orb-1" data-depth="1"></div>
  <div class="orb orb-2" data-depth="2"></div>
  <div class="orb orb-3" data-depth="0.5"></div>
</div>
```

**JS**:

```js
document.addEventListener('mousemove', e => {
  const x = (e.clientX / window.innerWidth - 0.5) * 2;
  const y = (e.clientY / window.innerHeight - 0.5) * 2;
  document.querySelectorAll('.orb').forEach(orb => {
    const depth = parseFloat(orb.dataset.depth) || 1;
    orb.style.transform = `translate(${x * 15 * depth}px, ${y * 12 * depth}px)`;
  });
});
```

---

## 6. Count-Up Number Animation on Stats

**JS** (call `triggerCountUp()` from inside the `update()` function):

```js
function triggerCountUp() {
  const activeSlide = document.querySelector('.slide.active');
  if (!activeSlide) return;
  activeSlide.querySelectorAll('.stat-val').forEach(el => {
    if (el.dataset.counted) return;
    const text = el.textContent.trim();
    const numMatch = text.match(/^[\$]?([\d,]+)/);
    if (!numMatch) return;
    const target = parseInt(numMatch[1].replace(/,/g, ''));
    const prefix = text.startsWith('$') ? '$' : '';
    const suffix = text.replace(/^[\$]?[\d,]+/, '');
    const duration = 1200;
    const start = performance.now();
    el.dataset.counted = 'true';
    function animate(now) {
      const elapsed = now - start;
      const progress = Math.min(elapsed / duration, 1);
      const eased = 1 - Math.pow(1 - progress, 3);
      const current = Math.round(target * eased);
      el.textContent = prefix + current.toLocaleString() + suffix;
      if (progress < 1) requestAnimationFrame(animate);
    }
    requestAnimationFrame(animate);
  });
}
```

---

## 7. Typing Effect on Title Tag

**HTML** (empty element with id):

```html
<div class="slide-tag" style="text-align:center" id="titleTag"></div>
```

**JS**:

```js
(function() {
  const el = document.getElementById('titleTag');
  if (!el) return;
  const text = 'Your tagline here';
  let i = 0;
  el.style.opacity = '1';
  el.style.transform = 'translateY(0)';
  function type() {
    if (i <= text.length) {
      el.textContent = text.substring(0, i);
      i++;
      setTimeout(type, 50);
    }
  }
  setTimeout(type, 600);
})();
```

---

## 8. Alternating Feature List Slide-In

**CSS** odd items from left, even from right:

```css
.feature-list li {
  opacity: 0;
  transform: translateX(-20px);
}
.feature-list li:nth-child(even) {
  transform: translateX(20px);
}
.slide.active .feature-list li {
  opacity: 1;
  transform: translateX(0);
}
/* Spring easing on stagger: */
.slide.active .feature-list li:nth-child(1) { transition: opacity 0.45s var(--ease-spring) 0.5s, transform 0.45s var(--ease-spring) 0.5s; }
.slide.active .feature-list li:nth-child(2) { transition: opacity 0.45s var(--ease-spring) 0.6s, transform 0.45s var(--ease-spring) 0.6s; }
.slide.active .feature-list li:nth-child(3) { transition: opacity 0.45s var(--ease-spring) 0.7s, transform 0.45s var(--ease-spring) 0.7s; }
.slide.active .feature-list li:nth-child(4) { transition: opacity 0.45s var(--ease-spring) 0.8s, transform 0.45s var(--ease-spring) 0.8s; }
.slide.active .feature-list li:nth-child(5) { transition: opacity 0.45s var(--ease-spring) 0.9s, transform 0.45s var(--ease-spring) 0.9s; }
.slide.active .feature-list li:nth-child(6) { transition: opacity 0.45s var(--ease-spring) 1.0s, transform 0.45s var(--ease-spring) 1.0s; }
```

---

## 9. Pulsing Active Nav Dot

```css
.dot.active {
  background: var(--blue);
  width: 22px;
  border-radius: 4px;
  box-shadow: 0 0 8px rgba(59,130,246,0.4);
  animation: dotPulse 1.8s ease-in-out infinite;
}
@keyframes dotPulse {
  0%, 100% { box-shadow: 0 0 8px rgba(59,130,246,0.4); }
  50% { box-shadow: 0 0 16px rgba(59,130,246,0.7), 0 0 4px rgba(59,130,246,0.3); }
}
```

---

## 10. Title with Scale + Spring

```css
.slide-title {
  opacity: 0;
  transform: translateY(24px) scale(0.97);
  transition: opacity 0.65s var(--ease-spring) 0.35s, transform 0.65s var(--ease-spring) 0.35s;
}
.slide.active .slide-title {
  opacity: 1;
  transform: translateY(0) scale(1);
}
```

---

## General Notes

- All patterns use the PerformOS dark brand: `#0A0A0A` background, cream text, blue/violet/cyan accents.
- Spring easing: `cubic-bezier(0.34, 1.56, 0.64, 1)` — define as `--ease-spring` in `:root`.
- Particle canvas adds ~2-5% CPU on modern machines. Reduce `COUNT` if needed.
- Count-up animates once per element (tracked via `data-counted`). To re-animate, remove the flag in `update()`.
- All patterns are vanilla CSS/JS. Zero external dependencies. Single monolithic file.

## Known Pitfalls (from June 2026 code review)

### P1: 3D Perspective Transforms Hide Content
The pattern in Section 2 uses `perspective(1200px) rotateX(8deg)`. This causes cards and content below the subtitle to be clipped invisible in Chrome/Safari. The content exists in the DOM but renders below the visible area and overflow-y does not help because the 3D transform creates a new stacking context. **Do not use 3D perspective on slides with more than 3 content rows.** Use plain `translateY` instead.

### P2: Particle Canvas Hidden by Opaque Slide Background
`.slide { background: var(--ink) }` (opaque) completely covers the particle canvas at z-index 0. Particles only flash during cross-fade. **Fix:** Set `.slide { background: transparent }` and put the solid dark background on `body` or `.deck`. Or accept that particles only show during transitions.

### P3: Card Gradient Border ::before Never Renders
The `::before` pseudo-element with `z-index: -1` and `overflow: hidden` on the card means the gradient border is clipped invisible. The `cardBorderSpin` keyframes also waste CPU on every card continuously. **Fix:** Remove `::before` and `cardBorderSpin` entirely. Use plain `border-color` hover: `.card:hover { border-color: rgba(59,130,246,0.5); }`.

### P4: Canvas Not HiDPI-Scaled
`canvas.width = window.innerWidth` ignores `devicePixelRatio`. Circles look blurry on Retina. **Fix:** Multiply by dpr, set CSS dimensions separately, and `ctx.scale(dpr, dpr)`.

### P5: Particle Loop Runs on Inactive Tab
No Page Visibility API check. Wastes CPU/battery when tab is backgrounded. **Fix:** Pause/resume with `visibilitychange` event.

### P6: Orb Parallax Overrides CSS Animation
Setting `orb.style.transform` directly overrides the `animation: orbFloat`. Orbs stop floating on mouse move. **Fix:** Use CSS custom properties (`--px`, `--py`) for parallax offset and combine with animation in CSS.

### P7: Count-Up Fires on Text Stats Like "4 hrs"
Regex `/^[\$]?[\d,]+/` matches "4 hrs" prefix, animates 0→4, leaves " hrs" suffix. **Fix:** Skip elements where trailing text is long (>3 chars). Skip if target is 0. Mark with `data-counted` to prevent re-trigger on re-visit.

### P8: Nav Dots Are Not Keyboard Accessible
Created as plain `<div>` elements with `onclick`. Not focusable, not announced by screen readers. **Fix:** Use `<button type="button">` with `aria-label="Go to slide N"`.

### P9: No prefers-reduced-motion Gate
Particles, orbs, 3D transitions, spinning borders, pulsing dots — all ignore `prefers-reduced-motion: reduce`. **Fix:** Add `@media (prefers-reduced-motion: reduce)` block that kills all animations and hides the canvas.

### P10: Touch Swipe Triggers on Vertical Scroll
No vertical/horizontal discrimination. Swiping up/down on a tall slide can trigger slide change. **Fix:** Compare `|diffX|` vs `|diffY|` and only trigger if horizontal dominates.

### P11: Multiple h1 Elements
Slides 1 and 14 both use `<h1>`. **Fix:** Only slide 1 gets `<h1>`. All others use `<h2>`.

### P12: Spacebar Fires on Input Fields
Global spacebar handler fires even when user is typing in an input. **Fix:** Guard with `if (target.tagName === 'INPUT' || target.tagName === 'TEXTAREA') return;`.

### P13: Inline Styles Everywhere
Repeated `style=""` on table cells, cards, stats makes edits slow. **Fix:** Use utility classes like `.tc`, `.tc-muted`, `.tc-red`, `.tc-cyan`.

## Usage History
- First used in: PerformOS AI Team Local Edition deck (`performos-ai-team-deck`), June 2026.
- Proven at: https://performos-ai-team-deck.vercel.app
- Code review fixes applied: June 2026 (25 issues, see session notes)