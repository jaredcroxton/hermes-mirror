# Seedance 2.5 reference-video recreation

Use this when Jared wants to remake a reference video in Seedance 2.5 using uploaded character reference images, then stitch short clips together.

## Key model-relevant distinction

Seedance 2.5 supports richer multimodal referencing than earlier workflows. In practice, for character-led recreations, use references to lock identity and style, but do not expect one long generation to hold every face and action perfectly. Short scene generation still gives better keeper rates.

## Operating workflow

1. Inspect the reference video first:
   - duration
   - aspect ratio
   - resolution
   - visual beats
   - camera style
   - transition style
2. Create a contact sheet with timestamps to find natural scene ranges.
3. Break the video into 4 to 7 second beats.
4. Build a continuity bible before prompts:
   - upload order for reference images
   - character labels, e.g. Character A and Character B
   - which images define each character
   - face, hair, wardrobe, accessories
   - setting and time of day
   - camera language
   - global negative block
5. Write one complete prompt per scene.
6. Keep the same global style, continuity, and negative blocks in every prompt.
7. Change only the scene, action, and camera blocks per clip.
8. Stitch with straight cuts unless the source clearly relies on a transition.
9. Apply one final shared grade after stitching.

## Prompt structure

```text
REFERENCES:
Use @Image 1 and @Image 2 for Character A. Preserve facial identity, hairstyle, skin tone, body shape, wardrobe, accessories, and overall presence.

GLOBAL STYLE:
Vertical 9:16 cinematic realism, [specific city/location], [time of day], [lighting], [street details], [camera texture], no app overlays, no usernames, no captions, no logos.

SCENE:
A [duration]-second [shot type] of [character] in [specific place]. [One visual story beat].

CAMERA:
[Shot size], [angle], [one camera move], [lens/depth of field], [handheld/gimbal/static feel].

ACTION:
[One clear action only]. [Important gesture or reaction happens slowly and visibly].

CONTINUITY:
Maintain exact identity from the reference images. Same face, hair, age, build, outfit, and accessories. Keep wardrobe consistent across scenes.

NEGATIVE:
No face morphing, no identity drift, no distorted hands, no extra fingers, no random outfit change, no social media UI, no black bars, no watermarks, no unwanted style shift.
```

## Reference image mapping pattern

Use explicit labels. Do not rely on the model guessing.

```text
@Image 1: Character A close-up identity reference.
@Image 2: Character A front-view wardrobe reference.
@Image 3: Character A side-view expression reference.
@Image 4: Character B front-view identity and wardrobe reference.
@Image 5: Character B wider body and outfit reference.
```

Then refer to the labels consistently:

```text
Character A must match @Image 1, @Image 2, and @Image 3.
Character B must match @Image 4 and @Image 5.
```

## Scene breakdown pattern

For a 36 to 42 second vertical reference video, seven clips is a clean structure:

1. Hook or character close-up, 5 seconds
2. Location walk or movement setup, 6 seconds
3. Conversation or explanation beat, 5 seconds
4. Comic or surprise beat, 5 seconds
5. Reaction cutaway, 5 seconds
6. Secondary performance beat, 6 seconds
7. Final reaction beat, 5 seconds

## Take selection order

Pick outputs in this order:

1. Face consistency
2. Wardrobe consistency
3. Clean hands and body shape
4. Camera movement
5. Location quality
6. Lighting quality
7. Comic or emotional timing

Reject clips with identity drift even when the action is good.

## Retry modifiers

If faces drift:

```text
Use the reference images more strongly. Preserve exact facial identity and wardrobe. The character must be recognisable as the same person in every frame.
```

If it looks too AI-polished:

```text
Make it more natural and documentary-realistic. Reduce glossy CGI appearance. Add realistic handheld camera imperfections, real street texture, natural shadows, and practical sunlight.
```

If the location is weak:

```text
Make the location unmistakable through specific local signals, street furniture, vehicles, buildings, lighting, signage style without readable text, and pedestrian behaviour.
```

If the action is unclear:

```text
Simplify the movement. One clear action only. The character performs the gesture slowly and visibly in the centre of frame.
```

## Screen recording pitfall

When the reference is a TikTok, X, Instagram, or phone screen recording, do not recreate the app interface unless Jared explicitly asks for it. Treat the recording as source choreography only. Prompt against the actual scene, not the social media shell.

Use negatives like:

```text
no social media interface, no app overlays, no usernames, no captions, no logos, no phone screen UI, no black bars
```

## New York golden-hour pattern

For a Manhattan remake, use grounded local signals:

```text
New York City at golden hour, warm amber sunlight between tall brick buildings, yellow taxis, glass storefronts, sidewalk cafes, crosswalks, traffic lights, dense but natural pedestrian movement, realistic Manhattan street texture, soft lens flare, shallow depth of field.
```
