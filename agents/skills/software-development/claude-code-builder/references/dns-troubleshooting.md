# DNS Troubleshooting for PerformOS

Quick reference for diagnosing and fixing DNS issues on the PerformOS domain stack.

## Check commands

```bash
dig +short performos.com.au A          # Should be 76.76.21.21
dig +short www.performos.com.au A      # Should resolve via Vercel CNAME
dig +short NS performos.com.au         # Registrar ID (GoDaddy = ns35/ns36.domaincontrol.com)
vercel domains inspect performos.com.au  # Vercel config: intended vs current NS, connected projects
curl -s -o /dev/null -w "%{http_code}" "https://www.performos.com.au/"  # 200 = working
```

## GoDaddy apex DNS fix

1. Log into GoDaddy -> My Products -> performos.com.au -> DNS
2. Find A record with Name @ (apex/root)
3. Edit Data from current IP -> 76.76.21.21
4. Save. Propagation: 5-30 min. Vercel auto-provisions SSL.

## Known issues

- **Hermes server hosts file:** The Hermes VM maps performos.com.au to 127.0.0.1 in /etc/hosts. Never trust local curl for apex domain checks. Use dig or browser tool instead.
- **Duplicate Vercel projects:** performos.com.au is connected to both performos-com-au and performos. If apex SSL fails, remove from unused project in Vercel dashboard.
- **Browser vs system DNS:** Chrome uses DNS-over-HTTPS. May resolve differently than system dig. Trust dig for ground truth, browser for user experience.
