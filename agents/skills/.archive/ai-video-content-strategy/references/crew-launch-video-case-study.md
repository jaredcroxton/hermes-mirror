# Crew Launch Video — Case Study

## Context
24 June 2026. Jared built a launch video for the PerformOS Crew Skill Pack Catalogue (13 packs, 92 skills) using Seedance 2.0 on Higgsfield. The constraint: Seedance 2.0 blocks realistic human faces, so the entire video is product-only spectacle.

## What worked

### Elements-first workflow
Five reference images uploaded to Higgsfield as @Elements before any generation:
- @CubeGrid — catalogue cover screenshot (cream bg, dark charcoal cubes, one lime)
- @AgentWindows — 4 stacked browser windows, front one glowing lime border
- @LimeGlow — pure lime radial gradient on ink black
- @CreamBG — warm cream/linen background
- @LogoLockup — PERFORMOS CREW wordmark

Using brand-accurate screenshots from the actual PDF was faster and more authentic than generating reference images from scratch.

### Two deliverable formats
1. **60-second multi-shot video** — 6 generations, 10 seconds each, with timeline markers inside prompts. Best for the main launch asset.
2. **8-second standalone clips** — 6 self-contained clips, each carrying one message. Best for social and short-form.

### VO + Visual pairing
Every visual prompt shipped with a separate VO script line. The editor needs both. Seedance audio mixed low as texture; VO carries the message.

### The "send me the prompt" mode
When Jared is actively inside Higgsfield generating, he wants single prompts inline — not file references. Deliver the one prompt he needs. Clean. No commentary.

### Image-as-signal
Jared dropped a window-stack image mid-conversation without commentary. Expected pattern: read the visual, name what you see, weave it into the strategy as a new Element.

### CapCut pivot
When Seedance prompts didn't produce usable results for the paper planes concept, Jared pivoted to CapCut. The CapCut prompt was a completely different format: scene descriptions with stock-footage-matchable keywords, kinetic typography as the hero, no timeline markers. CapCut's AI video maker assembles stock footage + text overlays + music — it does not generate novel visuals. Lesson: when Jared says "they're not quite turning out," do not iterate the Seedance prompt. Offer a CapCut alternative immediately.

## The 6-clip structure (8-second Seedance format)

| # | Message | Visual anchor |
|---|---------|---------------|
| 1 | "13 Packs. 92 Skills." | @CubeGrid — grid awakens, ripple effect |
| 2 | "One call. One output." | @AgentWindows — front window glows, signal pulses back |
| 3 | "Built on a loop, not a prompt." | @CreamBG — orbiting rings: plan, act, review, repeat |
| 4 | "Bedrock. Fuel. Engine." | @CreamBG — three blocks, pulse travels down, engine fires |
| 5 | "Your business. Your crew." | @CubeGrid — cubes assemble from core outward |
| 6 | "The Future of High Performance." | @LogoLockup — 92 dots form constellation, resolve to logo |

## Full prompt libraries saved at
- `~/Desktop/cluade/performos-crew-catalogue/crew-launch-video-all-prompts.txt` — 60-second multi-shot version
- `~/Desktop/cluade/performos-crew-catalogue/crew-launch-8sec-scripts.txt` — 8-second standalone version
