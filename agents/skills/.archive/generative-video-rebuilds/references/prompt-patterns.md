# Prompt patterns for generative video rebuilds

## Master character lock

```text
Use the uploaded identity photos as the only identity reference for the main character. Match face, hair, build, skin tone, outfit, and smile. Keep the identity consistent across every clip. Use the scene reference only for location, camera angle, lighting, background movement, and mood. Do not copy the original main person from the scene reference. Replace that person completely with the user.
```

## Scene reference role

```text
Use the uploaded scene image as the reference for the street layout, buildings, lighting, pedestrians, cars, camera angle, depth, and mood. Do not use it as the identity reference for the main character.
```

## UI removal block

```text
No Instagram UI. No X UI. No TikTok UI. No captions. No usernames. No likes. No comments. No phone status bar. No playback controls. No watermarks. No logos. No readable text.
```

## Stitchability block

```text
Duration: exactly 5 seconds. End with forward walking motion so the next clip can continue the journey.
```

## Walking opener prompt

Use when the first clip must show the user’s face, then move into a walk.

```text
Create a 5 second vertical 9:16 realistic cinematic video.

The main character is the user from the uploaded reference photos. Match their face, smile, hair, build, skin tone, and outfit exactly. Do not use or copy the person from the scene reference. Do not create a different person.

Opening shot: the user stands on a busy city sidewalk outside a glass storefront with urban buildings, street reflections, pedestrians, and natural daylight around them. The camera starts in front of the user at chest height. Their face is clearly visible for the first two seconds. They smile naturally and look directly into the camera, like the start of a confident walking vlog.

Then the user turns their shoulders, pivots away from the camera, and begins walking forward through the city scene. The camera smoothly moves with them, shifting from a front-facing view into a natural follow shot from behind and slightly to the side. Keep movement realistic and casual, not slow motion.

Style: realistic phone-shot cinematic footage, natural handheld camera, shallow depth of field, subtle motion blur, believable pedestrians and cars, warm city light, premium social-video look.

No social media interface. No captions. No usernames. No phone controls. No watermarks. No logos. No readable text.

End with the user walking forward into the street scene so the next clip can continue the journey.
```

## Side-character observation prompt

Use when the user walks past recognisable moments.

```text
Create a 5 second vertical 9:16 realistic cinematic video.

The main character is the user from the uploaded reference photos. Keep their face, outfit, and identity consistent. The user walks along a busy city sidewalk. They glance toward a side character doing the action shown in the scene reference, react subtly, then keep walking forward.

The side character is only a background moment. Do not turn the user into the side character. Keep the camera mostly with the user but reveal the side-character action clearly enough for the viewer to understand it.

Use realistic handheld street footage, natural daylight, believable pedestrians, cars, storefronts, and slight motion blur. End with the user still walking forward for stitching.

No social media UI, captions, usernames, phone controls, watermarks, logos, or readable text.
```

## Negative prompt base

```text
wrong face, different person, copied original character, inconsistent identity, face morphing, distorted face, bad hands, extra fingers, extra arms, plastic skin, CGI, cartoon, glossy fake look, over-stylized, Instagram UI, X UI, TikTok UI, username, caption, likes, comments, share icon, phone status bar, playback controls, watermark, logo, readable text
```
