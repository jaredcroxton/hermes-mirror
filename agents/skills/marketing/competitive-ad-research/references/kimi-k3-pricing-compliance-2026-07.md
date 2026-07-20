# Kimi K3 — Competitive Intelligence (July 2026)

## Overview

Kimi K3 is Moonshot AI's flagship reasoning model. 2.8T parameters (MoE — 16 of 896 experts per token). 1M token context window. Always-on reasoning (every request runs a full thinking pass). Competes at the Claude Sonnet / GPT-5.6 Sol tier, not a budget alternative.

**Company**: MOONSHOT AI PTE. LTD., Singapore-based. Consumer site: kimi.com. API platform: platform.kimi.ai.

## API Pricing (per 1M tokens)

| | Price |
|---|---|
| Input (cache miss) | $3.00 |
| Input (cache hit) | $0.30 |
| Output (incl. reasoning tokens) | $15.00 |
| Context window | 1,048,576 tokens (1M flat) |

Key: 90% cache discount. All reasoning tokens billed as output at $15/M — verbose reasoning traces inflate costs beyond visible answers. Flat pricing across full 1M context window (no premium for long prompts).

## Consumer Subscription Tiers

**Consumer subscriptions and API access are completely separate.** Paying for a subscription does not give API access or discount tokens.

| Tier | Monthly | Annual (eff./mo) | Key Access |
|---|---|---|---|
| Free (Adagio) | $0 | — | Basic chat, daily quotas |
| **Moderato** | **$19** | $15 | K2.6 chat, Deep Research, light Kimi Code, Slides/Websites |
| Allegretto | $39 | $31 | 2x credits/quotas |
| Allegro | $99 | $79 | Agent Swarm, 5x Kimi Code credits |
| Vivace | $199 | $159 | 300 parallel agents, Kimi Claw, max quotas |

**Critical**: The $19/mo Moderato tier runs K2.6, NOT K3. K3 is API-only or available on higher consumer tiers. Kimi and Kimi Code benefits expected to split into separate products soon.

## Competitive Positioning vs Jared's Stack

Jared's current subs: Claude Max 5x ($167/mo), Highfield ($99/mo).

| | Kimi K3 (API) | Claude Sonnet (API) | DeepSeek V4 Pro (API) |
|---|---|---|---|
| Input | $3.00 | ~$3.00 | $0.435 |
| Output | $15.00 | ~$15.00 | $0.87 |
| Context | 1M | 200K-1M | 1M |
| Cache discount | 90% | Limited | 99%+ |

K3 is mid-pack on price — on par with Claude Sonnet, 21x output cost vs DeepSeek V4 Pro. The 90% cache discount is the differentiator for agent/RAG workloads with repeated context.

## Data Compliance Details

**Entity**: MOONSHOT AI PTE. LTD. (Singapore)
**Data storage**: Servers in Singapore
**Last policy update**: 30 April 2025
**DPO contact**: api-service@moonshot.ai

### What they collect
- Account info (email, phone, username, profile picture)
- **User content** (prompts, audio, images, videos, files, generated outputs)
- Communication info (support emails, messages)
- Device/usage data, log data, cookies
- Third-party login tokens (Google sign-in)

### How they use data
- Service provision and account management
- **Model training and improvement** — this is the headline risk
- Communication and support
- Safety, security, fraud prevention
- Legal compliance
- Marketing (with consent where required)

### Data sharing
- Service providers (hosting, customer service, cloud, CDN, analytics, payment)
- Affiliates
- Corporate transactions (merger, acquisition)
- Legal/regulatory compliance

### Security measures
- Industry-standard encryption
- Regular security audits and vulnerability patches
- Dedicated data protection team
- Staff access controls and monitoring
- Data backups in separate physical locations
- Real-time breach monitoring and emergency response plan

### GDPR/EEA coverage
Full rights: access, rectify, delete, portability, withdraw consent, object to processing, restrict processing, lodge complaints with local DPA. Legal bases mapped per processing purpose.

### Accor Plus risk assessment
- **Training-use clause**: User content explicitly used to train and refine models. This is the primary concern for corporate use.
- Singapore-based servers are better than mainland China for data sovereignty.
- No mention of SOC 2, ISO 27001, or enterprise compliance certifications on the API platform page (enterprise tier mentions "security and compliance assurance" but no specifics).
- Bottom line: do not put Accor Plus employee data, internal sales scripts, or commercially sensitive material through the consumer app without clearance. API usage may have different terms — verify before production use.

## Sources

- Kimi API Platform pricing: https://platform.kimi.ai/docs/pricing/chat
- Privacy Policy: https://platform.kimi.ai/docs/agreement/userprivacy
- eesel.ai pricing analysis: https://www.eesel.ai/blog/kimi-k3-pricing
- Lorphic pricing breakdown: https://lorphic.com/kimi-ai-pricing/
