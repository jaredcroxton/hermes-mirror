---
name: plain-language-content
description: "Use when turning technical, academic, corporate, or AI-sounding material into clear human language for non-technical readers, clients, frontline staff, or training audiences."
version: 1.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [plain-language, humanizer, training, explanation, simplification]
    related_skills: []
---

# Plain-Language Content

## Overview

This umbrella covers three related editing jobs: explain technical concepts to non-technical people, simplify expert training material for frontline use, and humanize stiff/AI-sounding prose.

## When to Use

- Jared asks for a simple explanation for family, clients, executives, or non-technical teams.
- Training material is too academic, theoretical, or jargon-heavy for learners.
- Draft text sounds AI-generated, generic, over-polished, or unlike a real person.

## Output modes

### Explain tech to non-technical readers
- Start with the real-world outcome, not the architecture.
- Use analogies only where they reduce cognitive load.
- Define unavoidable terms once, then use plain wording.

### Simplify training content
- Rewrite for a day-three frontline worker or sales rep.
- Convert theory into actions, examples, practice prompts, and checklists.
- Preserve required facts while removing academic scaffolding.

### Productized internal playbooks
- Use when turning technical setup, agent workflows, repo adaptations, or operating models into a source-of-truth playbook.
- Replace external-tool framing with the user's own product taxonomy when asked. Example pattern: "external repo method" becomes "PerformOS Crew" or another approved internal label.
- Explain the operating model in layers: what sets standards, what provides roles/rhythm, and what remains the business/product layer.
- Include practical usage modes, example prompts, when-not-to-use guidance, red flags, and verification checks.
- If the user wants old labels removed, verify the final file has zero old-label mentions and zero em dashes.
- Prefer saving durable playbooks into the user's Obsidian vault and returning the file as `MEDIA:/absolute/path`.

### Humanize prose
- Remove AI tells: empty intensifiers, symmetrical lists, generic transitions, and over-formal conclusions.
- Add a natural point of view, specific examples, and uneven but readable cadence.

## Verification Checklist

- [ ] Audience and reading level are explicit.
- [ ] No key facts were lost in simplification.
- [ ] The final text sounds like a competent human, not a template.
