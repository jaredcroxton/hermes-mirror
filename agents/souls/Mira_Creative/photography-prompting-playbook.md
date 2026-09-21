# Photography prompting playbook

Mira's expert layer. Read before any generation. Turns plain briefs into camera-grade
prompts. Sourced from OpenAI's gpt-image guide, photorealism frameworks, and commercial
photographer prompt guides (2026). Mira uses this so outputs look shot, not rendered.

## The two prompt formulas

### Commercial formula (default for marketing assets)
```
[Subject + action/context] + [camera angle & framing] + [lighting & environment]
+ [technical: camera body, lens, aperture, ISO] + [style/aesthetic] + [aspect ratio]
```
Example:
```
Close-up of a steaming ceramic mug of black coffee on a rustic wooden table, eye-level
angle. Natural morning sunlight through a window, soft shadows. Shot on Canon R5, 50mm
lens, f/2.8, ISO 100. Photorealistic, commercial food photography, 8k, hyper-detailed. 4:5
```

### Photorealism formula (when realism is the goal, esp. people)
```
[Realism trigger] + [subject] + [camera/lens] + [lighting] + [texture/detail]
+ [colour/tone] + [composition] + [grain/quality] + [negative instructions]
```

## The 8 photorealism levers (use 2-3 minimum, all 8 for max realism)
1. **Realism triggers** photorealistic, ultra-realistic, cinematic realism, true-to-life textures, natural imperfections. Without these, models default to subtly stylised.
2. **Camera + lens** DSLR / mirrorless / cinematic film still + focal length (see cheat sheet). Pushes model into photo mode, not illustration.
3. **Lighting** natural light, soft window light, golden hour, overcast, studio softbox, rim light, realistic shadows. Strongest realism signal. Never "good lighting", say the source.
4. **Texture + detail** visible pores, fabric grain, skin micro-detail, dust, slight imperfections. Kills the plastic look. Highest-impact, most-skipped lever.
5. **Colour + tone** natural colour grading, muted tones, cinematic balance, soft highlights, deep shadows. Over-saturation = instant AI tell.
6. **Composition** rule of thirds, eye-level, candid moment, unstaged, foreground/background separation, over-the-shoulder.
7. **Film grain + quality** subtle film grain, sensor noise in shadows, sharp focus, clean but not overly polished.
8. **Negative prompts** no cartoon, no CGI, no 3D render, no plastic skin, no airbrushing, no watermark, no distorted text. Guardrails against stylisation.

## Camera + lens cheat sheet
| Lens | Use | Effect |
|---|---|---|
| 24mm / 35mm wide | environmental / lifestyle, subject + surroundings | most natural realism, sees context |
| 50mm | general, "human eye" perspective | neutral, documentary |
| 85mm | portraits, headshots, faces | flatters features, compresses + blurs background |
| 100mm macro | product detail, jewellery, texture | extreme close detail |

**Aperture (depth of field):** f/1.4-f/1.8 = subject sharp, creamy blurred background (bokeh), separates product from noise. f/8-f/11 = everything in focus, for landscapes and flat-lay product.
**ISO:** ISO 100 = cleanest, crisp studio quality. Higher ISO = grain (use for raw, authentic, street feel).
**Lighting setups:** Studio (even, e-commerce white bg) · Softbox (soft shadows, flattering skin) · Rembrandt (triangle of light, drama, prestige) · Rim light (edge highlight, separates dark subject from dark bg) · Golden hour (warm, soft) · Practical (in-scene lamps).

## GPT Image 2 specifics (Mira's default engine)
- Strongest model for photorealism, text-in-image, identity-preserving edits, brand-consistent style transfer. Default for new work.
- **Quality tiers:** low (fast, high-volume, ideation, often as good as mini) · medium (balanced default) · high (max fidelity, fewer retries).
- **Structure GPT Image likes:** consistent order background/scene -> subject -> key details -> constraints. State the intended use ("Instagram ad", "website hero") to set polish mode. For complex prompts use short labelled segments or line breaks, not one long run-on.
- **Sizes (multiple of 16, ratio <= 3:1):** 1024x1024 square · 1024x1536 portrait · 1536x1024 landscape · 2560x1440 2K (reliability ceiling). Above 2K is experimental.
- Format is flexible: paragraphs, JSON-like, tags all work. Prioritise a skimmable template over clever syntax.

## Model-specific notes
- **GPT Image 2 / Kie GPT Image 2:** default. Best all-round reliability, text, brand consistency. See model-routing.md for the live route.
- **Seedream V4 / 4.5:** best-in-class at holding consistency with a source image while following an edit prompt. Use for "more like this" variations and identity retention. Responds to structured prompts + reference images.
- **Nano Banana Pro:** strongest for photorealistic humans and character consistency across many images. Lean into micro-detail (hair strands, pores, oiliness). Good for an influencer/face-locked brand.

## Caveats (do not over-trust)
- Diffusion models read camera terms (f/1.8, 85mm) mostly as STYLE TRIGGERS, not literal optics. They bias the look, they do not simulate exact physics. Use them to summon the aesthetic, verify the result, do not assume exact f-stop control.
- Prompt length: 50-200 words is the sweet spot. Under 30 can work if it hits the key levers. Longer gives the model more to anchor on.
- Change one lever at a time when refining, so you learn what each change did.

## Common mistakes that kill quality
- Too vague ("beautiful woman in a park") -> generic AI look. Specificity is the engine.
- Forgetting imperfections -> plastic, too-perfect, fake.
- Fantasy/illustration words ("magical", "ethereal", "stunning") -> pushes away from photo realism.
- Over-specifying colours ("vivid blue", "bright red") -> over-saturated, unnatural.
- Ignoring the background -> unreal background breaks the whole illusion. Describe it with the same care as the subject.

## How Mira uses this
On any generation, Mira silently runs the brief through the right formula, fills the
8 levers from the Visual DNA or brand profile, picks lens/lighting that match the look,
appends the default negative prompt, then shows the user the finished prompt before the
Go gate. In Path C she shows the prompt so the user learns it.
