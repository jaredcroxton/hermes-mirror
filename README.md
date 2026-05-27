# Hermes Agent Ecosystem — Full Mirror

**Last backup:** 27 May 2026
**Purpose:** Reproducible backup of all agent configurations, souls, skills, and memory. If anything happens to the local Hermes installation, this repo can regenerate the full agent ecosystem.

## What's included

| Directory | Contents |
|-----------|----------|
| `agents/souls/` | All 18 agent soul files (Brock, Bob, Lara, Sam, Polly, Harry, Atticus, Nelly, Dexter, Jules, Leo, Otto, Rex, Serge, + Agent Registry) |
| `agents/profiles/` | Per-agent Hermes profiles (config.yaml, skills) — 7 agents |
| `agents/skills/` | All Hermes skills from `~/.hermes/skills/` |
| `config/` | Main Hermes config.yaml, CLAUDE.md, AGENTS.md, agent-startup.md |
| `memory/` | Memory export (sanitized — no tokens or PII) |
| `performos-website/` | Latest PerformOS website build package (11 files) |

## Regeneration guide

If you need to restore from this mirror:

1. **Agent souls** — Copy `agents/souls/*.md` back to `/Users/jc/Desktop/Obsidian/Agents/`
2. **Hermes config** — Copy `config/config.yaml` to `~/.hermes/config.yaml`
3. **Skills** — Copy `agents/skills/*` to `~/.hermes/skills/`
4. **Agent profiles** — Copy each profile from `agents/profiles/` to `~/.hermes/profiles/`
5. **API keys** — Restore from your own secure backup (NOT in this repo)
6. **State DB** — Recreate from your own secure backup (NOT in this repo)

## What's NOT included (for security)

- API keys, tokens, or `.env` files
- Raw state databases (`state.db`) — may contain tokens in conversation history
- Private emails, phone numbers, or PII
- Session transcripts

## Agent registry

See `agents/souls/Agent Registry.md` for the full agent roster with profiles, bots, and soul file paths.

## Automated backup

This mirror is updated manually. To refresh, clone the repo and run the backup script from the Hermes environment.
