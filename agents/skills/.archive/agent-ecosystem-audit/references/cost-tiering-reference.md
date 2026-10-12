# Cost Tiering Reference

Three model tiers for the agent ecosystem. Orchestrators run on expensive models. Specialists run on cheap models.

## Tiers

| Tier | Model | Max Tokens | Cost/1K tokens (USD) | Use for |
|---|---|---|---|---|
| Tier 1 — Lightweight | gpt-4.1-mini | 4,000 | $0.00015 | Simple source fetch, status check, single-step |
| Tier 2 — Standard | gpt-4.1 | 16,000 | $0.002 | Multi-step workflows, content gen, incident interpretation |
| Tier 3 — Deep Reasoning | gpt-4.5 | 32,000 | $0.01 | Orchestration, cross-agent, complex legal, strategic |

## Agent assignments

| Agent | Tier | Est. cost/run (AUD) |
|---|---|---|
| brock | Tier 3 — Deep Reasoning | $0.105 |
| bobbuilder | Tier 3 — Deep Reasoning | $0.105 |
| atticuscounsel | Tier 3 — Deep Reasoning | $0.105 |
| harry_hr | Tier 2 — Standard | $0.021 |
| nelly_notebook | Tier 2 — Standard | $0.021 |
| laralearning | Tier 2 — Standard | $0.021 |
| samstudynerd | Tier 2 — Standard | $0.021 |
| pollyperformos | Tier 2 — Standard | $0.021 |
| miracreative | Tier 2 — Standard | $0.021 |
| sergeseo | Tier 2 — Standard | $0.021 |

## Cost formula

```python
cost_per_1k = tier["estimated_cost_per_1k_tokens_usd"]
cost_in = (tokens_in / 1000) * cost_per_1k
cost_out = (tokens_out / 1000) * cost_per_1k
total_usd = cost_in + cost_out
total_aud = total_usd * 1.50  # Approximate AUD conversion
```
