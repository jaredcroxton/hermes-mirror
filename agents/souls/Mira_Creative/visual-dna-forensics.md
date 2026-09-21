# Visual DNA forensics: reverse-engineer the camera recipe

The reason a regen misses is a lazy read. Vague words ("clean", "premium", "moody") do
not reproduce an image. The exact camera recipe does. Before any master prompt, Mira runs
this forensic pass on every reference image and resolves EVERY field below to a concrete
value with the visual evidence that justifies it. The master prompt then inherits those
exact values. No field left as "unknown" without saying why.

Read it like a photographer reverse-engineering a shot from the print.

## 1. Lens and focal length
- Evidence to read: facial/subject compression, background size relative to subject,
  edge distortion, how much scene is in frame at the subject distance.
- Wide (14-35mm): expansive, slight edge stretch, lots of context, near objects loom.
- Normal (40-60mm): natural perspective, no compression, "as the eye sees".
- Short tele (85-135mm): flattened features, compressed/enlarged background, tight subject.
- Resolve: focal length in mm (a range is fine), and WHY from the evidence.

## 2. Aperture and depth of field
- Evidence: how fast focus falls off, bokeh ball size and shape, how much is sharp.
- Shallow (f/1.2-f/2.8): subject sharp, background creamy, strong separation.
- Mid (f/4-f/5.6): subject + near context sharp, background soft.
- Deep (f/8-f/16): front-to-back sharp, flat-lay / landscape / architecture.
- Resolve: f-stop, plane of focus, and bokeh character (smooth, swirly, hard-edged).

## 3. Exposure and dynamic range
- Evidence: where detail lives in highlights vs shadows, clipping, overall brightness (EV),
  contrast curve.
- Read: high-key (bright, airy, lifted shadows) vs low-key (dark, protected shadows, pools
  of light) vs balanced. Note blown highlights or crushed blacks if present.
- Resolve: exposure feel (high-key / balanced / low-key), contrast (flat / normal / punchy),
  and dynamic range (compressed / wide).

## 4. ISO, grain and sensor character
- Evidence: noise/grain in shadows, smoothness, micro-detail crispness.
- Clean (ISO 100-400): crisp, studio, commercial. Grain present (ISO 800+ or film): raw,
  editorial, authentic.
- Resolve: clean vs grainy, and grain type (digital noise vs film grain) if any.

## 5. Shutter and motion
- Evidence: motion blur, frozen action, light trails, handheld micro-shake.
- Resolve: frozen / subtle motion / long exposure, and whether tripod-still or handheld feel.

## 6. White balance and colour temperature
- Evidence: overall warm/cool cast, skin tone, whites.
- Resolve: colour temperature (warm ~3000-4000K / neutral ~5000-5600K / cool ~6500K+),
  plus any colour grade or LUT feel (teal-orange, muted film, warm golden, desaturated).

## 7. Lighting rig (the biggest realism signal)
- Evidence: shadow direction, shadow hardness/softness, number of shadows, catchlights,
  highlight rolloff, where the brightest point is.
- Resolve EACH:
  - Key light: direction (front / 45 / side / back), height, hardness (hard = small/distant
    source, sharp shadows; soft = large/close source, gradient shadows).
  - Fill: strong (low contrast) or minimal (deep shadows). Estimate key-to-fill ratio.
  - Rim / hair / separation light: present or not.
  - Source type: natural window, golden hour sun, overcast sky, studio softbox, hard flash,
    practical in-scene lamps, mixed.
  - Named setup if it fits: Rembrandt, butterfly, split, loop, rim, high-key studio, etc.

## 8. Camera angle, height and distance
- Evidence: horizon line, perspective convergence, eyeline.
- Resolve: height (low / eye-level / high / top-down), angle (straight / 3-quarter / Dutch),
  distance (macro / close-up / medium / wide), and any tilt.

## 9. Lens character and optical artefacts
- Evidence: vignetting, flare, chromatic aberration, barrel/pincushion distortion, glow/bloom.
- Resolve: which artefacts are present. These are strong "real camera" tells, name them so
  the regen reproduces them instead of rendering a clinical CGI-clean frame.

## 10. Composition and framing
- Resolve: rule of thirds / centred / golden ratio, negative space and where, subject
  placement, foreground/background layering, leading lines, crop ratio.

## 11. Post-processing and finish
- Resolve: retouch level (raw/natural vs polished), texture (kept vs smoothed), grade
  (film emulation, HDR, matte, glossy), sharpening, any halation or bloom.

## Output: the forensic spec block
Mira returns this filled, then folds it verbatim into the master prompt:

```text
CAMERA RECIPE
Lens: <e.g. 85mm short tele, flattened features, compressed bg>
Aperture/DoF: <f/2, shallow, creamy bokeh, focus on eyes>
Exposure: <low-key, punchy contrast, protected shadows>
ISO/grain: <clean, subtle film grain in shadows>
Shutter/motion: <frozen, tripod-still>
White balance/grade: <warm 3500K, teal-orange grade>
Lighting: <soft key 45 left from window, minimal fill, key:fill ~4:1, subtle rim>
Angle/height/distance: <eye-level, 3-quarter, medium close-up>
Lens character: <slight vignette, gentle flare, no distortion>
Composition: <rule of thirds, subject left, negative space right>
Finish: <natural retouch, texture kept, matte film grade>
```

## Match-and-correct loop (this is what closes the gap)
1. Ingest -> fill the forensic spec from the reference.
2. Build the master prompt carrying every resolved value.
3. Generate.
4. COMPARE the output against the reference on each of the 11 fields. Score match 1-5 per field.
5. For any field scoring under 4, name the drift and adjust that one field in the prompt.
6. Regenerate. Repeat until each field is 4+ or the user is happy.
Change one field at a time so each correction is learnable. Never declare a match without
running the field-by-field comparison.

## When uncertain
Vision estimates specs from pixels, it is not EXIF. If a field is genuinely ambiguous, give
the best estimate AND the alternative, then let the first generation disambiguate. Do not
paper over it with a vague word.
