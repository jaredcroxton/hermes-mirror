# Deploy verification patterns

## Vercel deploy lag

After `git push origin main`, Vercel auto-deploys. `vercel inspect` may show "Ready" before all routes are accessible. New pages frequently return 404 for 10-20 seconds after Ready status.

Full verify sequence:
```bash
# 1. Check deployment status
vercel inspect https://performos-com-au.vercel.app --scope jaredcroxtons-projects

# 2. Curl all routes (expect some 404s on first pass for new pages)
for page in index about ai-fluency-workshop catalogue contact faq blog blog-how-to-use-ai-small-business blog-ai-instruments-small-business-australia; do
  code=$(curl -s -o /dev/null -w "%{http_code}" "https://performos-com-au.vercel.app/${page}.html")
  echo "$page.html → $code"
done

# 3. If any 404s on new pages: sleep 15 and retry
sleep 15
# Re-run curl loop
```

## Custom domain verification

`performos.com.au` is aliased in Vercel but requires DNS configuration. The alias exists in the Vercel dashboard (visible in `vercel inspect` output under Aliases) but DNS may not resolve. Check with `curl -s -o /dev/null -w "%{http_code}" "https://performos.com.au/"`. If 000 or timeout, DNS is not configured. This is a user dashboard task — point A record at Vercel.

## Schema verification command

Quick JSON-LD presence check on all live pages:
```bash
for page in index about ai-fluency-workshop ai-implementation ai-agents catalogue contact faq blog-how-to-use-ai-small-business blog-ai-instruments-small-business-australia; do
  url="https://performos-com-au.vercel.app/${page}.html"
  has_schema=$(curl -s "$url" | grep -c 'application/ld+json')
  schema_types=$(curl -s "$url" | grep -o '"@type"\s*:\s*"[^"]*"' | tr '\n' ' ')
  echo "$page: schema blocks=$has_schema | types=$schema_types"
done
```

Expected results per page:
- index: Organization, WebSite
- about: Organization, Person, BreadcrumbList
- ai-fluency-workshop: BreadcrumbList, Service, FAQPage (with 6 questions)
- ai-implementation: Organization, BreadcrumbList, Service
- ai-agents: Organization, BreadcrumbList
- catalogue: Organization, BreadcrumbList
- contact: Organization, BreadcrumbList
- faq: Organization, BreadcrumbList, FAQPage (with 20 questions)
- blog articles: Organization, BreadcrumbList, BlogPosting
- blog index: Organization, BreadcrumbList

## File corruption recovery

When `execute_code` read_file returns content with "LINE_NUM|" prefixes and write_file bakes them in:
```bash
python3 -c "
import re
path = '/path/to/corrupted/file.md'
with open(path) as f: content = f.read()
cleaned = re.sub(r'^ +\d+\|', '', content, flags=re.MULTILINE)
with open(path, 'w') as f: f.write(cleaned)
"
```

If line numbers are doubled (from a previous failed cleanup): use two regex passes or `re.sub(r'^ +\d+\| +\d+\|', '', content, flags=re.MULTILINE)` first, then the single-prefix pass.

## HTML bulk modifications with sed

GA4 injection before </head>:
```bash
for f in *.html; do
  if ! grep -q "googletagmanager" "$f"; then
    sed -i '' '/<\/head>/i\
  <!-- Google tag (gtag.js) -->\
  <script async src="https://www.googletagmanager.com/gtag/js?id=G-XXXXXXXXXX"><\/script>\
  <script>\
    window.dataLayer = window.dataLayer || [];\
    function gtag(){dataLayer.push(arguments);}\
    gtag("js", new Date());\
    gtag("config", "G-XXXXXXXXXX");\
  <\/script>\
' "$f"
  fi
done
```

Twitter cards after og:site_name:
```bash
for f in *.html; do
  if ! grep -q "twitter:card" "$f"; then
    sed -i '' '/<meta property="og:site_name" content="PerformOS">/a\
  <meta name="twitter:card" content="summary_large_image">\
  <meta name="twitter:site" content="@PerformOS">\
' "$f"
  fi
done
```

PulseCheck 360 standardisation:
```bash
sed -i '' 's/Pulse Check 360/PulseCheck 360/g' *.html
grep -c "Pulse Check 360" *.html  # expect all :0
```
