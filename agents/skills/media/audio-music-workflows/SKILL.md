---
name: audio-music-workflows
description: "Use when writing songs, generating music or sound with AI, preparing Suno/HeartMuLa prompts, or analyzing audio features and spectrograms."
version: 1.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [audio, music, songwriting, suno, heartmula, audiocraft, spectrograms]
    related_skills: []
---

# Audio and Music Workflows

## Overview

This umbrella covers creative and technical audio work: songwriting craft, Suno/HeartMuLa-style prompt packaging, AudioCraft/MusicGen/AudioGen generation, and Songsee-style spectrogram/feature analysis.

## When to Use

- Write or refine lyrics, structure, genre tags, and AI music prompts.
- Generate music or sound effects with local/cloud audio models.
- Use HeartMuLa or Suno-like workflows from lyrics and tags.
- Analyze audio features such as mel spectrograms, chroma, MFCC, or waveform summaries.

## Workflow lanes

### Songwriting and prompt craft
- Define genre, tempo, vocal style, structure, lyrical point of view, and production notes.
- Keep prompts concise enough for the target music generator.

### AI generation
- Pick the backend (HeartMuLa, AudioCraft/MusicGen, AudioGen, or another provider) based on installed tools and desired output.
- Run a short generation first, then iterate tags/lyrics.

### Audio analysis
- Use spectrogram/features when the task asks what is inside an audio file or how to visualize it.
- Save plots/audio artifacts and report exact paths.

## Verification Checklist

- [ ] Required audio tool/model is installed or blocker is stated.
- [ ] Prompt/lyrics/tags were preserved for reproducibility.
- [ ] Generated or analyzed media artifacts were opened, probed, or otherwise verified.
