# gstack as a build tool for PerformOS

Captured 14 June 2026. MIT-licensed. 110k stars.

## What it is

Garry Tan's virtual engineering team: 23 AI specialists inside Claude Code. Pipeline: Think → Plan → Build → Review → Test → Ship → Reflect.

## Quick install

```bash
git clone --single-branch --depth 1 https://github.com/garrytan/gstack.git ~/.claude/skills/gstack && cd ~/.claude/skills/gstack && ./setup
```

## Key specialists relevant to PerformOS builds

| Skill | Use |
|---|---|
| /office-hours | Reframe a product idea before building |
| /plan-ceo-review | CEO-level review of any build plan |
| /plan-eng-review | Architecture and edge-case review |
| /plan-design-review | Design-dimension audit |
| /design-shotgun | Generate multiple design variants |
| /design-html | Production HTML with Pretext |
| /review | Pre-landing code review |
| /ship | Run tests, push, open PR |
| /qa | Browser-based QA with real Chromium |

## When to use gstack vs AgentOS agents

- **gstack**: software development, code review, HTML production, deployment, QA
- **AgentOS agents (Bob/Mira/Lara/etc.)**: business operations, dashboards, training, HR compliance, strategy

They are complementary. Use gstack for code-heavy builds. Use your agents for business output.

## Important: gstack and Hermes are compatible

gstack supports Hermes as a host. The SKILL.md format is identical. AgentOS specialists and gstack specialists can coexist in the same Hermes runtime.
