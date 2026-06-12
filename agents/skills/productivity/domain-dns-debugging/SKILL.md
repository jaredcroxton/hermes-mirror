---
name: domain-dns-debugging
description: Use when a domain is not resolving correctly — wrong records, stale DNS, propagation issues, or SaaS-specific DNS UI confusion (Squarespace DNS Presets vs Custom Records, Vercel domain verification, etc.). Covers dig-based debugging, multi-resolver verification, and the common pitfalls of DNS management UIs.
---

# Domain DNS Debugging

## Triggers

- "my domain is showing the wrong page"
- "DNS is not pointing to [Vercel/Netlify/etc.]"
- "still seeing the old site"
- "propagation is taking too long"
- user sends a screenshot of DNS settings and asks what's wrong

## Core technique: multi-resolver dig

Never trust a single resolver. Use:

```bash
dig +short @8.8.8.8 <domain> A
dig +short @1.1.1.1 <domain> A
dig +short @9.9.9.9 <domain> A
```

Different resolvers cache at different times. If one shows the new record and another shows the old one, the change was made but propagation is incomplete.

Also check nameservers:

```bash
dig +short <domain> NS
```

This tells you who is authoritative. If nameservers are `ns-cloud-*.googledomains.com`, the domain was registered through Google Domains/Squarespace and DNS management lives there.

For CNAME subdomains:

```bash
dig +short www.<domain> CNAME
dig +short www.<domain> A
```

## Local override check when public DNS looks right

If public DNS is correct but the domain still fails on the user's machine, check the local resolver and hosts file before suggesting more DNS edits:

```bash
dscacheutil -q host -a name <domain>      # macOS local resolver answer
grep -n "<domain>" /etc/hosts            # local hosts override
```

A result like `127.0.0.1 <domain>` in `/etc/hosts` means the Mac is forcing the root domain to localhost. Remove that hosts entry, then flush DNS:

```bash
sudo dscacheutil -flushcache; sudo killall -HUP mDNSResponder
```

Verification pattern:

```bash
curl -I -L https://<domain>/
curl -I -L https://www.<domain>/
```

For Vercel root-to-www setups, the expected root response is usually a `308` redirect to `https://www.<domain>/`.

## TTL and propagation

Most DNS hosts set TTL to 4 hours by default (Squarespace: 4 hrs, Google: 1 hr). After changing records, public resolvers may serve the old records until TTL expires.

**Do not keep changing records.** Once the records are correct, wait. Changing them again resets the TTL clock.

## Squarespace DNS: Presets vs Custom Records

The most common pitfall: Squarespace shows DNS Presets at the top of the DNS page. These are NOT the same as Custom Records.

**DNS Presets** — pre-built templates (Email Campaigns, Domain Connect, Google verification). These do not affect A/CNAME routing for your website. Do not delete the Google verification TXT record.

**Custom Records** — the section lower down. This is where A records (`@`) and CNAME records (`www`) live. This is the only section that matters for pointing a domain to an external host.

Never click "Update DNS records" or "Add Squarespace Defaults" when you see a warning. That will add back the wrong records.

## Vercel DNS pattern

Correct records for pointing a domain to Vercel must be taken from the current Vercel domain screen. Do not rely on older generic defaults.

Common shapes:

```
CNAME  www  →  <project-specific>.vercel-dns-0xx.com OR cname.vercel-dns.com
A      @    →  <current Vercel-recommended IP from the screen>
```

Vercel has changed recommended apex IPs over time. If Vercel shows a "DNS Change Recommended" warning, use the exact `A @` value shown in Vercel, then verify with `dig`.

Delete any old `@` A records from previous hosts (Squarespace: `198.*`, Netlify, etc.). Keep only the current Vercel A record Vercel asks for.

## Vercel domain verification and Squarespace TXT records

If Vercel says a domain is linked to another Vercel account or project, deleting the old project may not instantly clear the lock. Vercel still requires DNS proof of ownership through TXT records.

Important workflow:

1. Treat the latest Vercel screen as the source of truth. Verification tokens can change between attempts.
2. Check the live TXT value before advising:
   ```bash
   dig +short @8.8.8.8 _vercel.<domain> TXT
   ```
3. If Squarespace already has a `_vercel` TXT record, do not create random duplicates. Replace the stale value, or add the new value to the same `_vercel` TXT record if the UI supports multiple values.
4. Vercel may ask for separate verification values for apex and `www`, both under `_vercel`:
   ```text
   vc-domain-verify=<domain>,<token>
   vc-domain-verify=www.<domain>,<token>
   ```
5. After saving, verify externally before telling the user to refresh Vercel:
   ```bash
   dig +short @8.8.8.8 _vercel.<domain> TXT
   dig +short @8.8.8.8 www.<domain> CNAME
   dig +short @8.8.8.8 <domain> A
   ```

User-facing guidance when Jared is stuck in the Squarespace UI: give one action at a time. Example: "First fix the CNAME `www` value. Then refresh Vercel. TXT comes next." Avoid long DNS theory while he is mid-screen.

## Web-hosted DNS UI verification

When the user sends screenshots of DNS management UIs, verify you are looking at the Custom Records section, not the Presets section. If you cannot see Custom Records in the screenshot, ask them to scroll down. Never confirm "records look correct" from a Presets-only screenshot.

## Reference files

- `references/mongodb-atlas-render-connection.md` — MongoDB Atlas → Render connection string, network access, environment variables, and common failures
- `references/vercel-project-transfer-options.md` — Three paths for moving Vercel projects between accounts, free to paid

## Pitfalls

- **TTL impatience:** After records are confirmed correct, propagation may take up to 4 hours. Don't suggest more changes.
- **Presets blindness:** Squarespace's DNS Presets section looks like the main records but is not. Always scroll to Custom Records.
- **Single-resolver trust:** One resolver may cache faster than another. Always check 2-3.
- **Old host debris:** Domains moved between hosts often leave old A records behind. Delete all non-Vercel A records for `@`.
