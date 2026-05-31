# Local Edition — Complete Reference

## Hardware Tiers

| Tier | Machine | RAM | Agents | Model Tier | Cost (RRP) |
|---|---|---|---|---|---|
| Standard | Mac Mini M4 | 24 GB | 5 agents | Llama 3.1 8B | ~$999 AUD |
| Professional | Mac Mini M4 Pro | 48 GB | 10 agents | Mixed 8B + 14B | ~$1,399 AUD |
| Enterprise | Mac Studio M5 Ultra | 128 GB | 10+ agents | Phi-4 14B + Qwen 2.5 14B | ~$6,499 AUD |

## Cloud vs Local Quick Comparison

| Factor | AWS Lightsail | Orgo (Cloud) | Local Mac |
|---|---|---|---|
| Monthly cost | $34-$384 USD | $324 USD | $0 after purchase |
| GPU acceleration | No | Managed | Yes (Metal) |
| Data sovereignty | No (AWS servers) | Partial | Full (on-prem) |
| Offline capable | No | No | Yes |
| Latency | High (internet) | Medium | Zero (local) |
| 10 agents possible | No (max ~3-4) | Yes | Yes (48GB+) |
| Zero data retention | No | No | Yes |

**Verdict:** Lightsail is not suitable for the Local Edition product. No GPU, high latency, data on AWS servers. Use Mac Mini for Local Edition, Orgo for Cloud Edition.

## Internal Cost Model (Professional Tier — Mac Mini M4 Pro 48GB)

| Item | Amount |
|---|---|
| Hardware (passed to client via setup fee) | $1,399 AUD |
| Setup fee | $3,000 AUD |
| Your 10hr time | ~$500 |
| First-month revenue | $7,999 AUD |
| First-month margin | ~$6,100 AUD |
| Monthly margin (ongoing) | ~$4,957 AUD |

## Connecting Hermes to Local Ollama

```bash
# Install
brew install ollama

# Start
ollama serve

# Pull models (Professional tier)
ollama pull llama3.1:8b
ollama pull phi4:14b
ollama pull qwen2.5:14b-bnb-4bit
```

Hermes config to add to `~/.hermes/config.yaml`:

```yaml
ollama:
  models:
    llama3.1:8b:
      context_length: 32768
    phi4:14b:
      context_length: 32768
  metal: true
  gpu_layers: -1
```

## Version

Locked 2026-05-30. Created for PerformOS AI Team — Local Edition.