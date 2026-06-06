---
name: ascii-media
description: "Use when creating ASCII art, terminal-style diagrams, image-to-ASCII conversions, or full ASCII video/GIF/MP4 treatments."
version: 1.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [ascii, art, video, terminal, pyfiglet, image-to-ascii]
    related_skills: []
---

# ASCII Media

## Overview

This umbrella covers ASCII as a visual medium, from quick text banners and cowsay-style terminal art to image/video conversions and rendered ASCII MP4/GIF outputs.

## When to Use

- Generate text banners, boxes, cowsay, or decorative terminal output.
- Convert an image into monochrome or colored ASCII.
- Build an ASCII video/GIF pipeline from source video/audio.
- Design terminal-native visual assets.

## Workflow

1. Choose still vs motion output.
2. For stills, use pyfiglet/boxes/cowsay or image-to-ASCII tooling.
3. For video, plan scenes, resolution, palette, frame rate, and audio handling before rendering.
4. Preview small outputs before long encodes.
5. Deliver the final text/image/video artifact and cite the command used.

## Pitfalls

- High-resolution video conversion is expensive; test with a short clip first.
- ASCII legibility depends on font, contrast, and target display width.
- Colored terminal output may not survive copy/paste; export an image/video when fidelity matters.
