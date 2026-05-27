# PerformOS Domain Configuration

As of 26 May 2026.

## Live URLs

- `https://performos-com-au.vercel.app` — Vercel subdomain. Always works. Auto-deploys on git push.
- `https://www.performos.com.au` — Custom domain. SSL active. Auto-deploys on git push.

## Broken / not owned

- `performos.com.au` (apex) — DNS A record fixed to `76.76.21.21` on 26 May 2026 (was `216.150.1.1`). DNS confirmed propagated. SSL blocked by dual-project assignment: domain is connected to both `performos-com-au` (active) and `performos` (stale). Fix: remove from `performos` in Vercel Dashboard. CLI cannot remove per-project — dashboard only.
- `performos.com` — Registered 2012, Namecheap, DNSimple nameservers. NOT owned by PerformOS. Do not use, do not link to, do not report as live.

## Why apex may not resolve after DNS fix

DNS propagated (confirmed via `dig +short performos.com.au A` → `76.76.21.21`). If site still does not load at apex:

- **Dual-project conflict:** Domain is connected to both `performos-com-au` and `performos`. Remove from the stale project in Vercel Dashboard.
- **SSL provisioning lag:** After removing the conflict, Vercel auto-provisions SSL. May take 5-10 minutes.
- **Local hosts file:** The Hermes server and some development machines may have `/etc/hosts` entries mapping `performos.com.au` to `127.0.0.1`. This causes `ERR_CONNECTION_REFUSED` from those machines even when the site is live for everyone else. Use an external checker or incognito browser to verify.
