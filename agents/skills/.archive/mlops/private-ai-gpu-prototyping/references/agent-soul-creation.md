# Agent Soul Creation for Client Deployments

This is a condensed reference for building specialist agent SOUL files from real business websites.

## Extraction pattern

Use Firecrawl scrape with markdown format and `onlyMainContent: true` to extract the core business information. Do not scrape CSS or navigation — focus on the business facts: what they sell, who they sell to, their markets, their numbers.

```json
{
  "url": "https://client-website.com",
  "formats": ["markdown"],
  "onlyMainContent": true
}
```

## SOUL.md template

```
# <Agent Name> — <Role> Agent for <Company>

## Who <Agent Name> Is

<One-paragraph identity statement.>

## <Company> Business Context

<All extracted business facts: products, markets, numbers, brands, revenue model.>

### Key Business Numbers

<Bullet list of stats from the website.>

### Products/Services

<What they sell and how they sell it.>

### Operating Markets

<Countries, regions, locations.>

## How <Agent Name> Operates

<Decision-making principles. How the agent thinks. What it optimizes for.>

## Decision-Making Principles

<Numbered list of core principles. 5-8 items.>

## Key Leadership Context (<User>)

<Who the user is in this business context, what they do, what they need from the agent.>

## Voice and Tone

<Professional. Direct. Industry-aware. Data-informed. Speaks like a senior executive.>
```

## Profile creation on EC2

```bash
# 1. Upload soul
scp -i key.pem soul.md ubuntu@<public-ip>:/home/ubuntu/

# 2. Create profile
hermes profile create <name> --clone
cp /home/ubuntu/soul.md ~/.hermes/profiles/<name>/SOUL.md

# 3. Configure model (Python one-liner)
python3 -c "
import yaml
with open('config.yaml') as f:
    c = yaml.safe_load(f)
c['model']['default'] = 'llama3.1:8b'
c['model']['provider'] = 'custom'
c['model']['base_url'] = 'http://localhost:11434/v1'
yaml.dump(c, open('config.yaml','w'), default_flow_style=False, sort_keys=False, width=120)
"

# 4. Test
hermes --profile <name> chat -q 'State your name, role, and one key fact about the business.' --quiet
```

## Browser interface

See the parent skill's "Browser agent interface pattern" section for building a branded chat page.
