---
name: local-dashboard-access
description: Use when the user needs to make a locally-hosted dashboard (Hermes, Vite, or static) accessible from outside their local network. Covers ngrok, Tailscale Funnel, and Cloudflare tunnel options with trade-offs for each.
version: 1.0.0
author: PerformOS / Jared Croxton
license: MIT
metadata:
  hermes:
    tags: [networking, tunnel, ngrok, tailscale, dashboard, local, devops]
    related_skills: [claude-code-builder]
---

# Local Dashboard Access

## Vite AllowedHosts Fix

When using ngrok or any tunnel with a Vite dev server, add the tunnel hostname to `vite.config.ts`:

```typescript
server: {
  host: "localhost",
  port: 9119,
  strictPort: true,
  allowedHosts: ["your-tunnel-hostname.ngrok-free.dev"], // ADD THIS
}
```

Without this, Vite returns "Blocked request. This host is not allowed." On every page load.

Note: ngrok free plan generates a new random hostname each restart. Paid plan ($25/mo) gives reserved domains so the config stays stable.

## ngrok Auth Token Setup

Ngrok requires an authtoken even on the free plan. One-time setup:

```bash
ngrok config add-authtoken YOUR_TOKEN_HERE
```

Get the token from https://dashboard.ngrok.com/get-started/your-authtoken

Until this is done, `ngrok http <port>` will fail with ERR_NGROK_4018.

## The Problem

A client's Mac mini runs Hermes agents and a local dashboard (e.g., Vite dev server at `localhost:9119`). The client cannot access it from their phone, from another office, or from home. You need to create a public tunnel.

## Three Options (pick one)

### Option 1: ngrok (Fastest for Demos)

**Best for:** Prospect demos, proof-of-concept, temporary access.
**Cost:** Free (random URL changes each restart) or $25/mo (reserved domain).
**Security:** Traffic goes through ngrok's servers. HTTPS encrypted.

```bash
# Install (macOS)
curl -sO https://bin.equinox.io/c/bNyj1mQVY4c/ngrok-v3-stable-darwin-amd64.tgz
tar xzf ngrok-v3-stable-darwin-amd64.tgz

# Authenticate (one-time, get token from https://dashboard.ngrok.com/get-started/your-authtoken)
./ngrok config add-authtoken <YOUR_TOKEN>

# Start tunnel
./ngrok http 9119
# or with Vite host rewrite
./ngrok http 9119 --host-header=rewrite
```

**Vite gotcha:** Vite blocks ngrok hostnames by default. The exact error is: "Blocked request. This host is not allowed. To allow this host, add it to server.allowedHosts in vite.config.ts." Fix in `vite.config.ts`:
```ts
server: {
  allowedHosts: ["your-subdomain.ngrok-free.dev"],
}
```
Then **restart the dev server** — changes to vite.config.ts are NOT hot-reloaded. If the dev server is not restarted, the old config remains in effect.

**Ngrok binary location (this machine, already downloaded):** `~/ngrok` — no need to reinstall. Just ensure `~/.config/ngrok/ngrok.yml` has the authtoken (already configured as at May 2026).

**Get the public URL:**
```bash
curl -s http://localhost:4040/api/tunnels | grep public_url
```

### Option 2: Tailscale Funnel (Best for Production)

**Best for:** Ongoing client access, encrypted, no third-party traffic.
**Cost:** Free for personal use. $15/user/mo for Teams.
**Security:** End-to-end encrypted via WireGuard. Data never leaves Tailscale's encrypted tunnel.

1. Install Tailscale on the Mac mini: `brew install tailscale`
2. Authenticate: `tailscale up`
3. Enable Funnel: `tailscale funnel --bg 9119`
4. Get the URL from `tailscale funnel status`

The URL looks like: `https://<machine-name>.<tailnet-name>.ts.net`

**Advantages over ngrok:** Fixed URL on same machine. End-to-end encrypted. No third-party can see traffic. Works even if the Mac mini is behind NAT/firewall (Tailscale uses DERP relays).

**Downside:** The client needs Tailscale installed too if they want to verify it works from their end. For demos where the client just needs a link to click in their browser, this works without them installing anything — the Funnel URL is publicly accessible.

### Option 3: Cloudflare Tunnel (Enterprise)

**Best for:** Custom domains, enterprise clients, branded URLs.
**Cost:** Free tier available. Cloudflare Tunnel is free.
**Security:** Traffic goes through Cloudflare's edge. HTTPS.

```bash
# Install cloudflared
brew install cloudflare/cloudflare/cloudflared

# Authenticate
cloudflared tunnel login

# Create and run tunnel
cloudflared tunnel create my-tunnel
cloudflared tunnel route dns my-tunnel dashboard.clientdomain.com
cloudflared tunnel --url http://localhost:9119 run my-tunnel
```

**Downside:** More setup. DNS configuration required. Overkill for most PerformOS clients.

## Decision Matrix

| Factor | ngrok | Tailscale Funnel | Cloudflare Tunnel |
|---|---|---|---|
| Setup time | 2 minutes | 10 minutes | 20 minutes |
| Cost | Free / $25mo | Free / $15mo/user | Free |
| Fixed URL | Paid only | Yes | Yes (custom domain) |
| Encryption | HTTPS only | E2E WireGuard | HTTPS only |
| Client installs nothing | Yes | Yes | Yes |
| Data leaves client network | Yes (via ngrok) | No (via Tailscale) | Yes (via Cloudflare) |
| Works behind NAT | Yes | Yes (DERP relays) | Yes |
| Good for demos | Best | Good | Overkill |
| Good for production | No | Best | Good |

## For PerformOS AI Team Clients

- **Phase 1 (Demo):** Use ngrok. Fast, free, prospects can click a link and see the dashboard immediately.
- **Phase 2 (Paid client, no strict compliance):** Use Tailscale Funnel. Encrypted, fixed URL, no ongoing cost.
- **Phase 3 (Paid client, compliance-heavy):** Use Cloudflare Tunnel with the client's own domain and DNS. Gives them full control and branding.

## Server-Side API Proxy Pattern

When serving a web-based chat UI or dashboard from a remote server (EC2, VPS) that needs to call a local API (Ollama, Hermes, any `localhost`-only service), JavaScript runs in the user's browser. `localhost` in `fetch()` always resolves to the client machine, not the server. The page loads but API calls fail silently.

### The fix: backend proxy

Instead of exposing the API port publicly, serve both the HTML and a proxy endpoint from the same Python server:

```
Browser ──► :8090 (public) ──► Python server ──► :11434 (localhost, Ollama)
               │                      │
               GET / → HTML           POST /api/chat → Ollama API
```

The JavaScript calls `/api/chat` (same origin, no CORS), and the Python backend proxies to Ollama on localhost. See `references/ec2-api-proxy-server.md` for a complete deployable template.

### Ollama idle-model timeout

Ollama unloads models from GPU when idle. First query after idle can take 10-30 seconds to reload, which exceeds browser timeouts and causes "Connection lost" loops. Fix: pre-warm the model at server startup by sending a short ping through the Ollama API before `serve_forever()`.

## Common Pitfalls

1. **`localhost` in JavaScript on remote servers.** `fetch('http://localhost:11434')` in a page served from EC2 resolves to the user's laptop, not the EC2. Use same-origin proxy endpoints (`/api/chat`) or the server's public IP instead.
2. **Vite `allowedHosts` block.** Always add the tunnel hostname to `server.allowedHosts` in vite.config.ts. Restart the dev server after.
3. **Open port does not prove target identity.** When several local dashboards or studios are running, do not assume the first responsive port is the requested artifact. Check the page title, visible heading, repo/file path, or specialist handoff first. If the target cannot be identified, say so and ask for the exact path, URL, screenshot, or project name rather than opening a likely wrong dashboard.
4. **Specialist blocked means not finished.** If a build/polish task is blocked because the artifact was not found, report that status before showing a local URL. Distinguish clearly between “this local app is running” and “this is the confirmed dashboard Jared asked for.”
5. **Showing in Chrome.** When Jared asks to see a local dashboard in Google Chrome and the URL is known, use `open -a "Google Chrome" <url>` and then state exactly which URL was opened. Do not imply production/live status from opening a local URL.
6. **ngrok URL changes on restart.** Free ngrok gives a random URL each time. If the client bookmarks it, it will break. Use Tailscale Funnel for stable URLs.
7. **ngrok authtoken required.** You must run `ngrok config add-authtoken <token>` before the first use. Token is at https://dashboard.ngrok.com/get-started/your-authtoken.
8. **Dashboard server must be running.** ngrok/tunnel only forwards traffic. If the Vite/dev server is not running on the target port, the tunnel returns connection refused.
9. **ngrok API for URL.** The local ngrok API is at `http://localhost:4040/api/tunnels`. CORS is not enabled; use from server-side or curl only — not from browser JS.
10. **Cloudflare Pages is NOT for real-time chat.** Cloudflare Pages serves only static files. It cannot proxy to a running Hermes/Ollama backend. Use it only for static dashboards (KPI displays, reports), not chat interfaces.
11. **WhatsApp API is wrong channel for AI agents.** WhatsApp API charges $0.01-$0.12 per conversation and only allows replies within 24-hour windows. Telegram is free and allows proactive push. Use Telegram for all AI agent communication.

## Reference

- Ngrok binary location (when downloaded manually): `~/ngrok`
- Hermes dashboard default port: 9119
- ngrok auth config: `~/.config/ngrok/ngrok.yml`
- Local ngrok API: `http://localhost:4040`

## Tabbed Dashboard Pattern

When building dashboards with multiple data sets (e.g., weekly batches of GitHub trending repos), use a **tabbed single-file HTML** pattern:

### Structure

```html
<div class="tab-nav">
  <button class="tab-btn active" onclick="switchTab('batch1')">Batch 1 — 01 June 2026</button>
  <button class="tab-btn" onclick="switchTab('batch2')">Batch 2 — 01 June 2026</button>
</div>
<div class="tab-panel active" id="batch1"></div>
<div class="tab-panel" id="batch2"></div>
```

### Tab switching JS

```javascript
function switchTab(tab) {
  document.querySelectorAll('.tab-btn').forEach(b => b.classList.remove('active'));
  document.querySelectorAll('.tab-panel').forEach(p => p.classList.remove('active'));
  document.querySelector('[onclick="switchTab(\'' + tab + '\')"]').classList.add('active');
  document.getElementById(tab).classList.add('active');
  renderTab(tab);
}
```

### Data: embed inline, never fetch

`file://` protocol blocks `fetch()` to local JSON files due to CORS. Always embed data as inline variables:

```javascript
var BATCHES = {
  'batch1': [{name: '...', stars: 123, ...}, ...],
  'batch2': [{name: '...', stars: 456, ...}, ...]
};
// Data embedded inline. No fetch needed.
```

This makes the dashboard fully self-contained — a single HTML file, zero external dependencies, portable via any file transfer method.

### Performlytics color palette (use for all dashboards)

```css
:root {
  --bg: #0A0A0A;
  --text: #F0F0F5;
  --text-muted: #A0A0B0;
  --accent: #3B82F6;
  --accent-hover: #60A5FA;
  --violet: #8B5CF6;
  --cyan: #22D3EE;
  --surface: #111111;
  --surface-hover: #1A1A1A;
  --border: #222222;
}
/* Fonts: Archivo (headings), Inter (body), JetBrains Mono (mono/metrics) */
/* Never use lime (#D4FF3B) — it is reserved for PerformOS brand, not Performlytics */
```

### Card grid pattern

```css
.card-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(380px, 1fr));
  gap: 18px;
  padding: 20px 0;
}
.card {
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: 12px;
  padding: 22px 24px 20px;
  transition: border-color 0.2s, background 0.2s;
}
.card:hover {
  border-color: var(--accent-hover);
  background: var(--surface-hover);
}
```

### Pitfall: Unicode breaks JavaScript in embedded data

When scraping text for dashboard cards, always sanitize Unicode before embedding in `<script>` tags:

```python
text = text.replace('\u2014', '--').replace('\u2013', '-')
           .replace('\u2018', "'").replace('\u2019', "'")
           .replace('\u201c', '"').replace('\u201d', '"')
```

Em dashes, en dashes, and curly quotes silently corrupt JavaScript parsing when embedded inline. Symptoms: `REPOS` variable undefined, no cards rendering, silent JS exceptions with empty error messages.
