# Local Service Exposure Patterns

How to make a locally-hosted service (e.g., Hermes dashboard on a Mac mini) accessible to remote clients.

## Options

### 1. ngrok (Best for demos and POCs)

Setup: `cd ~ && ./ngrok http <port>`
First time: `~/ngrok config add-authtoken <TOKEN>`
Binary at `~/ngrok` (v3.39.5 as of May 2026)
Tunnel check: `curl -s http://localhost:4040/api/tunnels`
Free tier URLs: `*.ngrok-free.app` or `*.ngrok-free.dev`

Pros: Fastest setup. HTTPS URL in seconds. No client install.
Cons: Free tier URL changes every restart. Third-party data transit.
Cost: Free (random URL) or $25/mo (reserved domain).

**Vite gotcha (30 May 2026):** Vite blocks ngrok hostnames by default with "Blocked request. This host is not allowed." Fix in `vite.config.ts`:

    server: {
      allowedHosts: ["your-subdomain.ngrok-free.dev"],
    }

Restart dev server after. Changes to vite.config.ts are NOT hot-reloaded.

Session notes:
- Auth token from https://dashboard.ngrok.com/get-started/your-authtoken
- Dashboard on port 9119 tunneled to `https://garage-chain-hardwired.ngrok-free.dev`
- ngrok API at `http://localhost:4040/api/tunnels` -- use curl, not browser (CORS)

### 2. Tailscale Funnel (Best for production)

E2E encrypted via WireGuard. No third-party data access. Stable URL.
Free for personal use. ~$15/user/mo for Teams.

    brew install tailscale
    tailscale up
    tailscale funnel --bg 9119
    tailscale funnel status

URL: `https://<machine-name>.<tailnet-name>.ts.net`

Advantages: Fixed URL. E2E encrypted. No third-party plaintext access. Works behind NAT.

### 3. Cloudflare Tunnel (Enterprise)

    brew install cloudflare/cloudflare/cloudflared
    cloudflared tunnel login
    cloudflared tunnel create my-tunnel
    cloudflared tunnel route dns my-tunnel dashboard.clientdomain.com

Cost: Free tier available.

### 4. Cloudflare Pages (Static ONLY -- NOT for chat)

Cloudflare Pages serves static files only. Cannot proxy to Hermes/Ollama.

Use for: KPI dashboards, reports, static landing pages with cron sync.
Do NOT use for: Real-time chat, agent conversations, live backend connections.

## Client Matrix

| Client type | Solution | Cost |
|---|---|---|
| Demo/POC | ngrok free | $0 |
| Small business | Tailscale Funnel | $0-$15/mo |
| Compliance-heavy | Tailscale Funnel or Cloudflare Tunnel | $0-$50/mo |
| Enterprise | Cloudflare Tunnel + custom domain | $5-$50/mo |
| Static dashboards | Cloudflare Pages + cron | $0 |

## WhatsApp vs Telegram

Telegram: Free. Proactive push. Rich formatting. Use for all AI agents.
WhatsApp API: $0.01-$0.12/convo. 24h reply window. Cannot push proactively.

| | Telegram | WhatsApp API |
|---|---|---|
| Cost | Free | $0.01-$0.12/convo |
| Proactive | Yes | 24h window only |
| 5K convos/mo | Free | ~$100-$200/mo |
| Setup | Low | High (BSP, verification) |

Verdict: Telegram for all AI agent products.

## PerformOS Architecture

Two-tier approach:
1. Agent chat interface: Local web server on Mac mini + Tailscale Funnel (prod) or ngrok (demo)
2. Data dashboards: Cloudflare Pages/Vercel with cron sync

Pricing: Dashboard included in $4,999/mo. Enterprise relay add-on: $200-$500/mo.
