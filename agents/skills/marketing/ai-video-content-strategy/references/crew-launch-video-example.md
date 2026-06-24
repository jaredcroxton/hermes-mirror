# Worked Example: PerformOS Crew Launch Video
## 24 June 2026

A complete launch video prompt library for a product catalogue (13 packs, 92 skills), built for Seedance 2.0 on Higgsfield. Demonstrates the full video content strategy workflow in practice.

---

## What This Example Teaches

1. **Elements-first workflow.** Five reference images uploaded once and referenced across all generations: @CubeGrid, @AgentWindows, @LimeGlow, @CreamBG, @LogoLockup. No per-generation re-uploading.
2. **Multi-generation sequencing.** Six generations tell a complete story: establish brand → reveal scale → show architecture → demonstrate concept → close with lockup. Each generation is 8-10 seconds, self-contained, but sequenced.
3. **The face-restriction workaround.** Seedance 2.0 blocks realistic human faces. This entire video is product-only spectacle: cubes, windows, grids, typography, particles. Zero human characters. Real Jared footage layers in during post-production.
4. **Multi-shot timeline format.** Generations 2-6 use [0s]...[3s]...[6s] markers for shot-by-shot control within a single generation. The Seedance "under 80 words" rule relaxes for structured timeline prompts.
5. **8-second short-form variants.** Six standalone 8-second scripts, each carrying one message. Same Elements, shorter form, social-optimized.

---

## The Visual Metaphor

Two core visual systems, both already in the catalogue:

- **Cube grid:** Dark charcoal cubes on warm cream. Represents packs and skills as building blocks. One cube glows lime green (#d4ff3b) — the active element.
- **Agent windows:** Four stacked browser windows (macOS traffic lights, claymorphism). The front window has a lime border. Represents "One call. One output" — the user invokes one window, the crew works behind it.

---

## The 6-Generation Sequence (60 seconds)

| Gen | Time | What it does | Visual |
|-----|------|-------------|--------|
| 1 | 0-10s | The Grid Awakens | Cube grid, center cube glows lime, camera dollies in |
| 2 | 10-20s | Business Crew Fans Out | 9 cubes (packs 01-09) spread radially, pulse amber |
| 3 | 20-30s | Design Crew Rises | 4 larger cubes rise above, Pack 10 glows lime |
| 4 | 30-40s | Architecture: Bedrock → Fuel → Engine | Three stacked blocks, lime pulse travels down, Engine dominates |
| 5 | 40-50s | Agent Windows: One Call. One Output. | Four stacked windows, lime pulse travels backward, front window expands |
| 6 | 50-60s | Constellation and Lockup | 92 lime dots → PERFORMOS CREW wordmark → tagline |

---

## Key Prompt Pattern: Multi-Shot Timeline

```
@Reference as the first frame.
[0s] Establishing composition. Static camera. Clean.
[2s] First change — motion begins. Camera movement specified.
[5s] Second beat — energy peaks. Subject transforms or new element enters.
[8s] Resolution. Hold on final composition. Fade.
```

One primary action per time block. Camera movement named once. Sound cues at transition points.

---

## Key Prompt Pattern: 8-Second Standalone

```
@Reference as the first frame.
[0s] Single subject, single composition. Static.
[2s] One transformation or reveal.
[5s] Peak moment — the message lands visually.
[7s] Hold. Logo or lockup implied.
[8s] Fade.
```

Each 8-second clip carries exactly one message. Use individually on social or string together as a reel.

---

## Production Workflow Used

1. Research Seedance 2.0 capabilities and prompt structure (Newly.app guide, RunDiffusion guide, Higgsfield blog)
2. Study the catalogue PDF for visual language (cream bg, charcoal, lime accent, serif type, cube grid)
3. Design Elements (reference images) from catalogue screenshots
4. Write generations in sequence, each building on the last
5. Write short-form variants as standalone scripts
6. Production notes: Fast mode first, 3 takes per shot, 40% keeper rate, VO layered in post

---

## Files Produced

- `crew-launch-video-all-prompts.txt` — 6-generation full launch video
- `crew-launch-8sec-scripts.txt` — 6 standalone 8-second social clips
- Each file contains complete copy-paste Seedance prompts with VO scripts

---

## Lessons for Future Launch Videos

1. **Study the product's visual language first.** The catalogue's cream/charcoal/lime palette became the entire video's colour grade. No inventing.
2. **Screenshot the product as your Elements.** Don't generate reference images separately — the product IS the reference kit.
3. **Design around model limitations from the start.** Knew faces were blocked before writing a single prompt. Saved redesign time.
4. **Two lengths, same assets.** The 6-gen sequence and 8-second scripts use identical Elements. One upload, two output formats.
5. **VO is separate.** Seedance audio is ambient texture. The message travels on human voice, layered in post.
