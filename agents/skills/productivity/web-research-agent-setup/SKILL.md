---
name: web-research-agent-setup
description: Configure Agent Reach or similar web-research agents with per-platform cookie authentication. Use when setting up X/Twitter, Reddit, YouTube, LinkedIn, GitHub, or other platforms for agentic web research; when the user says "install Agent Reach", "set up research agent", "configure platform access"; or when macOS Keychain prompts appear during cookie-based auth setup.
---

# Web Research Agent Setup

Install and configure Agent Reach (or similar web-research agents) with per-platform authentication. The core principle: **manual cookie export beats browser auto-extraction every time.** Browser cookie auto-extraction hits the macOS Keychain (Chrome Safe Storage Key) and triggers a system-level security prompt that cannot be bypassed from the terminal. Deny it. Use the manual path.

## Trigger

- User asks to install, configure, or set up Agent Reach or a web-research agent
- User wants to give their agent access to X/Twitter, Reddit, YouTube, LinkedIn, or other platforms
- macOS Keychain prompt appears during cookie-based auth setup
- User says "set up X platform for research" or "connect agent to [platform]"

## Platform difficulty tiers

| Tier | Platforms | Pattern |
|---|---|---|
| **Easy** (zero auth) | GitHub, V2EX, RSS feeds, Exa, Jina Reader (any webpage), B站 search | Works out of the box. No cookies needed. |
| **Medium** (one config) | YouTube, LinkedIn (public profiles) | One config line or Jina Reader. No login needed for basic access. |
| **Hard** (manual cookie) | X/Twitter, Reddit | Manual cookie export required. `browser-cookie3` triggers Keychain — always deny and use the manual path. |
| **Very Hard** (cookie + anti-bot) | Reddit, 小红书, 雪球 | Aggressive anti-bot detection. Even with valid cookies, Python requests may be 403 blocked. The credential file must use the exact format the CLI tool expects. |

## Setup pattern for each platform

### YouTube (one config line)

```bash
mkdir -p ~/Library/Application\ Support/yt-dlp && echo '--js-runtimes node' >> ~/Library/Application\ Support/yt-dlp/config
```

### X / Twitter (manual cookie, two cookies needed)

**Path A: `twitter-cli login` (cleanest)**
```bash
pip install twitter-cli
twitter-cli login
```
Use a burner account. Cookies stored at `~/.twitter-cli/.cookies` with 600 permissions. No Keychain prompt.

**Path B: Manual cookie export**
1. Open X.com in your browser. Log in.
2. Developer Tools (`Command + Option + I`) → Application → Cookies → `x.com`
3. Copy `auth_token` (long hex string) and `ct0` (shorter hex string)
4. Export as env vars or configure via `agent-reach configure`:
```bash
export TWITTER_AUTH_TOKEN="paste-auth-token"
export TWITTER_CT0="paste-ct0"
```

### Reddit (manual cookie, exact JSON format required)

Reddit is the hardest platform. `rdt-cli` and its `rdt login` command auto-scan Chrome cookies via `browser-cookie3`, triggering the Keychain prompt. Even `rdt status --json` hits the Keychain. The fix: write the credential file directly in the exact format `rdt-cli` expects.

**Step 1: Export the cookie**
1. Open reddit.com in your browser. Log in.
2. Developer Tools → Application → Cookies → `reddit.com`
3. Copy the `reddit_session` value (a long JWT string)

**Step 2: Write the credential file directly**
```bash
mkdir -p ~/.config/rdt-cli
cat > ~/.config/rdt-cli/credential.json << 'EOF'
{
  "cookies": {"reddit_session": "PASTE-YOUR-COOKIE-HERE"},
  "source": "manual",
  "username": "your-reddit-username",
  "modhash": null,
  "saved_at": 0,
  "last_verified_at": null
}
EOF
chmod 600 ~/.config/rdt-cli/credential.json
```

**CRITICAL:** The format must be `{"cookies": {"reddit_session": "..."}, "source": "manual", ...}`. The simpler format `{"reddit_session": "..."}` will NOT work. Agent Reach's `_check_rdt()` looks for the `cookies` wrapper.

**Step 3: Verify (optional, may still trigger Keychain)**
```bash
rdt status --json
```
This may still trigger the Keychain prompt because `rdt-cli` is wired to check Chrome cookies on every invocation. Deny it. The credential file is already correct.

**Honest gap:** Even with a valid credential file, Reddit's anti-bot detection may 403-block Python `urllib` requests. `rdt-cli` works around this with browser-like headers. If direct Python requests return 403, that is expected — use `rdt-cli` as the backend (which Agent Reach does automatically), or accept that Reddit is the hardest platform and skip it.

### LinkedIn (two tiers)

**Tier 1: Jina Reader (zero setup, works now)**
```bash
curl -s "https://r.jina.ai/https://linkedin.com/in/username"
```
Reads any public LinkedIn profile. Returns markdown. No login needed. Agent Reach routes through this automatically.

**Tier 2: Full MCP server (needs setup)**
Requires: MCP server clone, LinkedIn cookies (`li_at` + `JSESSIONID`), mcporter registration. An hour of work. Not a one-command install.

## The Keychain problem

`browser-cookie3` is a Python package that reads browser cookies from Chrome, Firefox, Edge, Brave, and Opera. On macOS, Chrome encrypts sensitive cookies using a key stored in the macOS Keychain (the Chrome Safe Storage Key). When `browser-cookie3` tries to decrypt Chrome cookies, macOS prompts: "iTerm2 wants to use your confidential information stored in Chrome Safe Storage in your keychain."

**Always deny this prompt.** It appears because:
- Agent Reach's `cookie_extract.py` calls `browser_cookie3` as a fallback
- `rdt-cli`'s `login` command auto-scans Chrome before asking for credentials
- Any tool built on `browser-cookie3` will trigger it

**The fix every time:** Export cookies manually from the browser (Developer Tools → Application → Cookies) and feed them to the CLI tool via env vars or config files. No Keychain. No Chrome Safe Storage. No macOS popup.

## Installation

```bash
pip install agent-reach
agent-reach install --env=auto
agent-reach doctor
```

`agent-reach doctor` shows what is green and what needs configuration. The SKILL.md is auto-installed to both `~/.agents/skills/agent-reach` (Hermes agents) and `~/.claude/skills/agent-reach` (Claude Code).

## Verification

```bash
agent-reach doctor
```

Green = working. Yellow = installed but needs auth. Red = broken. The `doctor` command does NOT trigger Keychain prompts — it only checks if CLI tools are installed and functional.

## Pitfalls

- **Never use `agent-reach configure --from-browser`.** It calls `cookie_extract.py` which uses `browser-cookie3`, which triggers the Keychain prompt. Always configure platforms manually.
- **Never run `rdt login` or `rdt status` without expecting a Keychain prompt.** `rdt-cli` is wired to check Chrome cookies on every invocation. Write the credential file directly instead.
- **Reddit's credential format is strict.** The wrapper key `cookies` is mandatory. A flat `{"reddit_session": "..."}` will be ignored.
- **Reddit may still 403 even with valid cookies.** Its anti-bot detection is aggressive. Agent Reach's `rdt-cli` backend handles this with browser-like headers. Direct Python `urllib` requests will likely fail.
- **Do not install `browser-cookie3` unless absolutely required.** Agent Reach installs it as a dependency. That is fine. But do not invoke it directly. Every invocation triggers the Keychain prompt.
- **Agent Reach has no `read` or `search` CLI command.** It is a library that routes to platform-specific tools. Use `agent-reach doctor` for status, `yt-dlp` for YouTube, `twitter-cli` for X, `rdt-cli` for Reddit, and Jina Reader (`r.jina.ai`) for webpages.
