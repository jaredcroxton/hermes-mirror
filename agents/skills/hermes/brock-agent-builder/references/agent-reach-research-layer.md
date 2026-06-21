# Agent Reach — Internet Research Layer for Hermes and Claude Code

## What it is

A capability layer that gives any AI agent internet eyes. One `pip install agent-reach` and the agent can read Twitter/X, search Reddit, extract YouTube transcripts, browse XiaoHongShu, query GitHub, parse RSS feeds, search the web via Exa, and read LinkedIn pages. 13 platforms. MIT license. Author: Neo Reid.

**GitHub:** https://github.com/Panniantong/Agent-Reach.git
**Version:** 1.5.0
**Python:** 3.10+

## Installation (already done on Jared's MacBook Pro)

```bash
pip install agent-reach
agent-reach install --env=auto
agent-reach doctor
```

## Current status (20 June 2026)

7 of 13 platforms live:

| Platform | Status |
|---|---|
| GitHub | ✅ Green, full access |
| YouTube | ✅ Green, video + transcripts |
| V2EX | ✅ Green, public API |
| RSS feeds | ✅ Green, feedparser |
| Exa semantic search | ✅ Green, free tier |
| Any webpage (Jina Reader) | ✅ Green |
| B站 (Bilibili) | ✅ Green, search API only |
| X / Twitter | ⚠️ Needs `twitter-cli login` with burner account |
| Reddit | ⚠️ Needs OpenCLI browser login |
| 小红书 (XiaoHongShu) | ⚠️ Needs OpenCLI desktop or MCP |
| 小宇宙 (podcasts) | ⚠️ Needs cookie export |
| 雪球 (stocks) | ⚠️ Needs install |
| LinkedIn | ⚠️ Needs MCP server |

## Skill files installed

- Hermes agents: `~/.agents/skills/agent-reach`
- Claude Code: `~/.claude/skills/agent-reach`

Any Crew skill or Hermes agent can route research through Agent Reach automatically.

## Unlocking remaining platforms

### X / Twitter (no Keychain)

```bash
pip install twitter-cli
twitter-cli login    # Use a burner account, not personal
```

### YouTube config fix

```bash
mkdir -p ~/Library/Application\ Support/yt-dlp
echo '--js-runtimes node' >> ~/Library/Application\ Support/yt-dlp/config
```

## Multi-backend architecture

Every platform has a primary backend plus fallbacks. When a platform changes anti-scraping rules, Agent Reach swaps to the fallback. No user action required.

## Security

- Reads content only. Does not post, comment, or like.
- Does not auto-send emails or DMs.
- All config stored locally at `~/.agent-reach/config.yaml` with 600 permissions.
- Platforms requiring login (Twitter, 小红书): use a burner account, not main.

## Integration with Crew skills

- **crew-web-lead-dashboard-builder:** LinkedIn research and company intelligence
- **crew-sales-lead-research:** Multi-platform prospect research
- **crew-marketing-campaign-plan:** Twitter/Reddit trend analysis
- **crew-project-builder:** GitHub research during Phase 1 Blueprint

## Doctor command

```bash
agent-reach doctor
```

Shows what is green, what needs config, and what is not installed.
