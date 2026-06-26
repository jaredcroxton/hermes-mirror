# GitHub Repo Presentation Standards

Standards for presenting CREW pack repositories to match or exceed top open-source projects (Hermes Agent, Ruflo).

## Must include

1. **Header image.** Dark banner (ink-black #0a0a0a), large brand name in ivory (#F5F5F0), thin lime accent line (#32CF32), tagline below. 1200x630. Standard GitHub social card dimensions.

2. **Badges.** Version, skill count, pack count, QA status, license. Lime label (left) with dark text, dark gray value (right) with white text. Never white text on lime — fails contrast. Use shields.io with `labelColor=lime&color=333333`.

3. **One-liner description.** Bold blockquote under the title. "The only agent skill pack with a built-in brand context system." States the differentiator immediately.

4. **Comparison table.** Product vs alternatives. Five rows minimum. Specific, provable claims (not "better quality" — "3-lens adversarial review on every skill" vs "bugs ship to production").

5. **Quick Start.** Clone, build, install. Three platform paths (Claude Code, Hermes Agent, OpenClaw). First run instructions.

6. **Full architecture section.** Skill flow diagram (ASCII), 8 Crew Standards, 5 Core Loops table, Bedrock/Fuel/Engine diagram, Three Words (Skill/Agent/Context).

7. **Pack catalogue table.** All 14 packs with skill counts and one-line descriptions.

8. **Quality standards table.** Every gold-standard requirement listed. Specific, checkable claims.

9. **Compatibility matrix.** Platforms and support level.

10. **FAQ section.** 4 questions minimum. Real questions a buyer would ask.

11. **Brand story.** Founder name, company thesis ("We don't chase tools. We build leverage."), three pillars. Link to company website.

12. **0 em dashes.** Same white-label discipline as skills.

## Files

- `header.png` in repo root
- `README.md` with all sections above
- `LICENSE` (MIT)
- `.gitignore` (node_modules, .DS_Store, build artifacts)

## Repo settings

- Private by default until launch
- 9+ topics for discovery (claude-code, ai-agents, agent-skills, hermes-agent, openclaw, multi-agent, etc.)
- Homepage URL set to company website
- Description: one-line summary with pack/skill count
