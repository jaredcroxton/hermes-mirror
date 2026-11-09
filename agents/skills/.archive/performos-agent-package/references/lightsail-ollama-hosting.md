# Lightsail and Ollama hosting notes

Use this when Jared asks whether Amazon Lightsail should run Hermes agents, Ollama, or part of the PerformOS Local AI Team infrastructure.

## Strategic rule

Lightsail is a good **agent hosting and control layer**. It is not the default product engine for the PerformOS Local AI Team.

Use Lightsail for:
- always-on Hermes gateway
- Telegram bots
- specialist profile hosting
- cron jobs and scheduled briefs
- monitoring and admin tooling
- audit dashboards and lightweight cloud control layer
- optional lightweight backup/local model testing

Use the PerformOS-owned local appliance for:
- client-private workflows
- local model inference
- data sovereignty positioning
- client-approved network placement
- local AI team delivery

## Pricing ladder from AWS Lightsail pricing page, June 2026

Linux/Unix plans with public IPv4 address:

- $12 USD/month: 2 GB RAM, 2 vCPU, 60 GB SSD. Suitable for basic Hermes gateway and one or two light profiles. Not suitable for Ollama.
- $24 USD/month: 4 GB RAM, 2 vCPU, 80 GB SSD. Sensible starter for always-on Hermes hosting without local models.
- $44 USD/month: 8 GB RAM, 2 vCPU, 160 GB SSD. Minimum practical test box for very small Ollama models.
- $84 USD/month Compute Optimized: 8 GB RAM, 4 vCPU, 320 GB SSD. First sensible Ollama test tier for lightweight models.
- $168 USD/month Compute Optimized: 16 GB RAM, 8 vCPU, 640 GB SSD. More realistic CPU-only Ollama testing tier.
- $384 USD/month General Purpose: 64 GB RAM, 16 vCPU, 1280 GB SSD, 8 TB transfer. Viable as a serious PerformOS cloud control layer and CPU-only Ollama test host, but do not buy this before workflow/load is proven. First normal Lightsail tier worth serious consideration for a 19 GB Ollama model.

## Ollama reality check

Lightsail virtual servers are CPU-only for this use case. Ollama can run, but performance depends heavily on model size.

Good fit:
- llama3.2:3b
- phi3:mini
- qwen2.5:3b

Possible but slower:
- qwen2.5:7b
- mistral:7b
- llama3.1:8b
- some quantised 13B/14B models on larger tiers

Poor fit:
- 30B+ models
- heavy multi-user inference
- fast real-time chat across many agents
- commercial delivery where latency matters

## 19 GB Ollama model sizing

A 19 GB Ollama model needs more than 19 GB system memory when running. Use this rule of thumb:

- model file: 19 GB
- likely running memory: 24 to 38 GB once overhead and working space are included
- 32 GB RAM: tight minimum for one model and light Hermes use
- 64 GB RAM: comfortable for one model plus Hermes gateway, dashboards, logs, and a few profiles

Lightsail implications:

- $164 USD/month General Purpose: 32 GB RAM, 8 vCPU, 640 GB SSD. Minimum viable for a 19 GB model, but tight and likely slow.
- $336 USD/month Compute Optimized: 32 GB RAM, 16 vCPU, 1280 GB SSD. More CPU, but still tight on RAM.
- $384 USD/month General Purpose: 64 GB RAM, 16 vCPU, 1280 GB SSD. Best normal Lightsail balance for a 19 GB model.
- $844 USD/month Compute Optimized: 72 GB RAM, 36 vCPU, 1280 GB SSD. Better CPU-only performance, but at this price compare against EC2 GPU or client-site Apple silicon.

Recommendation: if Jared wants to prove a 19 GB model in a managed cloud setup, use the $384 tier. If he wants best performance, use EC2 GPU or a Mac Studio/local appliance instead.

## Commercial framing

For the $4,999 AUD/month PerformOS Local AI Team offer, a $384 USD/month Lightsail box is not margin-breaking. The question is not cost first. The question is job-to-be-done.

Good job-to-be-done for $384 Lightsail:
- control layer for multiple clients
- agent gateway reliability
- dashboards and logs
- lightweight backup inference
- monitoring client appliances

Weak job-to-be-done:
- main AI brain for the Local AI Team offer
- replacement for the PerformOS-owned appliance
- pretending CPU inference equals local GPU or Apple silicon performance

## Recommendation pattern

Default recommendation:
1. Start with $24 USD/month Lightsail for Hermes hosting.
2. Use external models for serious reasoning.
3. Keep local/private inference on the Mac Mini or managed local appliance.
4. If testing Ollama on Lightsail, trial $84 or $168 for one month.
5. Move to $384 only when there is real multi-client control-layer load or a proven need.

## Client-facing language

Do not say: "We run Ollama on Lightsail."

Say:
"PerformOS can use a lightweight cloud control layer for uptime, monitoring, and secure access, while the private AI team runs in the approved local environment."

## Pitfall

Do not let cloud convenience dilute the Local Edition promise. If client data sovereignty is the value proposition, keep inference and private workflows local unless the client explicitly approves a cloud integration path.
