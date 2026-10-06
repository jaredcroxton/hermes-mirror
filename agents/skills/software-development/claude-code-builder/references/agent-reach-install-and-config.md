# Agent Reach — Install and Configure X/Twitter (No Keychain)

## What Agent Reach is

Agent Reach (`agent-reach`) is a pip-installable research router that gives Claude Code and Hermes agents access to 13 platforms: GitHub, YouTube, X/Twitter, Reddit, RSS, B站, Exa semantic search, Jina Reader, and more. It ships a SKILL.md so any agent that can run shell commands can route research through it.

## Install

```bash
pip install agent-reach
agent-reach install --env=auto
agent-reach doctor
```

## Keychain avoidance rule — NEVER use browser cookie auto-extraction

Agent Reach's `agent-reach configure --from-browser` and `agent-reach install --env=auto` both trigger `browser_cookie3`, which reads Chrome's encrypted cookie database via the macOS Keychain (Chrome Safe Storage Key). **Jared rejects this every time. Never use it.** Always use platform-specific manual login or cookie export instead.

The Keychain prompt can also appear when running CLI tools that import `browser_cookie3` internally. `rdt-cli` is one such tool (see Reddit section below).

## Configure X/Twitter — `twitter-cli login` (safe, no Keychain)

`twitter-cli login` does NOT import `browser_cookie3` for its own login flow. It is safe to use directly.

### Option A: twitter-cli login (recommended)

```bash
pip install twitter-cli
twitter-cli login
```

Enter a burner X username and password. Cookies stored at `~/.twitter-cli/.cookies` with 600 permissions. Agent Reach picks them up automatically. No Keychain prompt.

### Option B: Manual cookie export (fallback)

If `twitter-cli login` is unavailable, export cookies manually from a browser where you are logged into X:

1. Open Developer Tools (`Command + Option + I`), Application tab → Cookies → `x.com`
2. Copy `auth_token` and `ct0` values
3. Export: `export TWITTER_AUTH_TOKEN="..."` and `export TWITTER_CT0="..."`
4. Persist in `~/.zshrc`

Verify with `twitter status` — should return `ok: true`. Then `agent-reach doctor` shows X green.

## Configure Reddit — manual credential.json (no Keychain)

`rdt-cli login` imports `browser_cookie3` internally at `rdt_cli/auth.py:141` and triggers the macOS Keychain prompt. `rdt status --json` also scans Chrome. **Never use `rdt login` or `rdt status` interactively on Jared's machine.** Both open the Keychain.

### Install rdt-cli from pinned source

PyPI lags behind. Use the pinned git commit:

```bash
pipx install --force 'git+https://github.com/public-clis/rdt-cli.git@5e4fb3720d5c174e976cd425ccc3b879d52cac66'
```

### Manual cookie export with correct credential format

The credential file format is NOT `{"reddit_session": "..."}`. rdt-cli expects:

```json
{"cookies": {"reddit_session": "<token>"}, "source": "manual", "username": "<reddit_username>", "modhash": null, "saved_at": 0, "last_verified_at": null}
```

Steps:

1. Open Reddit in Chrome. Log in.
2. Open Developer Tools (`Command + Option + I`), Application tab → Cookies → `reddit.com`
3. Find `reddit_session` in the cookie list. Double-click the value. Copy the full JWT.
4. Extract the username from the JWT payload (`sub` claim, e.g. `t2_a0clhhlb`).
5. Write the credential file:

```bash
mkdir -p ~/.config/rdt-cli
cat > ~/.config/rdt-cli/credential.json << 'EOF'
{"cookies": {"reddit_session": "PASTE-FULL-JWT-HERE"}, "source": "manual", "username": "PASTE-USERNAME-HERE", "modhash": null, "saved_at": 0, "last_verified_at": null}
EOF
chmod 600 ~/.config/rdt-cli/credential.json
```

### Reality check — Reddit may stay red

Even with the correct credential format, Reddit's anti-bot detection is aggressive. Direct Python `urllib` requests with the cookie return 403. `rdt status --json` triggers Chrome Safe Storage. Jina Reader also returns 403 (Reddit requires login for all access). Reddit is the hardest platform in Agent Reach. It may not go green without Chrome Safe Storage access or a dedicated Reddit API key. The credential file is saved and correct; future rdt-cli versions may resolve this.

## Configure YouTube — JS runtime fix

YouTube needs a one-line JS runtime config for yt-dlp:

```bash
mkdir -p ~/Library/Application\ Support/yt-dlp && echo '--js-runtimes node' >> ~/Library/Application\ Support/yt-dlp/config
```

Then `agent-reach doctor` shows YouTube green.

## Search syntax

```bash
agent-reach search "Claude Code" --platform x --max-results 10
# or direct:
twitter search "Claude Code" --type top -n 10 --lang en
```

Key flags: `-n` / `--max` for result count, `--type top|latest`, `--lang en`, `--since YYYY-MM-DD`.

## Platform status reference

After `agent-reach install --env=auto`, run `agent-reach doctor` to see status.

**Jared's machine (2026-06-20):** 7 of 13 platforms green. X configured via `twitter-cli login`. YouTube fixed via JS runtime config. Reddit pending manual credential.json. LinkedIn usable via Jina Reader (tier 1, public profiles only).

| Platform | Default state | What it needs to go green |
|---|---|---|
| GitHub | Green | Nothing |
| YouTube | Yellow → Green | One config line: `mkdir -p ~/Library/Application\ Support/yt-dlp && echo '--js-runtimes node' >> ~/Library/Application\ Support/yt-dlp/config` |
| RSS | Green | Nothing |
| Exa | Green | Nothing |
| Jina Reader | Green | Nothing |
| B站 | Green (search API) | Nothing for search |
| X/Twitter | Red → Green | `twitter-cli login` with burner account (safe, no Keychain) |
| Reddit | Red → may stay red | Manual credential.json with correct format. `rdt-cli login` and `rdt status` both trigger Keychain. Anti-bot detection may block even with valid cookie. Hardest platform. |
| 小红书 | Red | OpenCLI desktop or MCP |
| 小宇宙 | Red | Cookie export |
| 雪球 | Red | Install |
| LinkedIn | Red (tier 1 works) | Jina Reader reads public profiles now. Full search needs MCP server |
| V2EX | Green | Nothing |

## Where the skill file lands

After install:
- `~/.agents/skills/agent-reach` (Hermes agents)
- `~/.claude/skills/agent-reach` (Claude Code)
