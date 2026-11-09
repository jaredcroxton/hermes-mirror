# AWS Private Cloud Ollama Deployment Notes

Use this when Jared is weighing AWS Lightsail versus EC2 GPU for a PerformOS private-cloud AI team or for testing an always-on Ollama model.

## Decision rule

- **Lightsail** is best for Hermes gateways, Telegram bots, dashboards, cron jobs, monitoring, and lightweight support services.
- **Normal Lightsail is CPU-only**, so it can run Ollama but is not the best engine for serious local-model performance.
- **EC2 GPU** is the right AWS path when the goal is a strong private-cloud model experience.
- **Client-site Mac or Mac Studio** remains the stronger path when the sales story is local appliance, client-site data boundary, and enterprise trust.

## 19 GB Ollama model sizing

A 19 GB Ollama model should not be sized as 19 GB only. Allow runtime overhead, context, OS, Hermes, gateway, logs, and active requests.

Practical sizing:

- **32 GB RAM**: minimum and tight.
- **64 GB RAM**: comfortable for one always-on model plus Hermes and light services.
- For CPU-only Lightsail, the **$384 USD/month 64 GB / 16 vCPU plan** is the first normal Lightsail tier worth testing for a 19 GB model kept warm all the time.

## Lightsail options

Use Lightsail for the control layer unless deliberately testing CPU inference.

Recommended roles:

- $24 to $84 USD/month: Hermes gateway, bots, dashboards, health checks, monitoring.
- $384 USD/month: one-client private-cloud prototype with one 19 GB Ollama model, but CPU-only and not ideal for speed.
- Avoid positioning high-tier Lightsail as “best local model performance.” It may work, but it lacks GPU acceleration.

## EC2 GPU options

For AWS-hosted model performance, use EC2 GPU rather than normal Lightsail.

Good starting point for a 19 GB Ollama model:

- **g6.2xlarge**
  - 1 NVIDIA L4 GPU
  - 24 GB GPU memory
  - 8 vCPUs
  - 32 GB system RAM
  - Good first serious test instance for a 19 GB model.

Cheaper quick proof:

- **g6.xlarge**
  - 1 NVIDIA L4 GPU
  - 24 GB GPU memory
  - 4 vCPUs
  - 16 GB system RAM
  - Tighter. Use for short proof tests only.

More comfortable:

- **g6.4xlarge**
  - 1 NVIDIA L4 GPU
  - 24 GB GPU memory
  - 16 vCPUs
  - 64 GB system RAM
  - Better when running Ollama, Hermes, dashboards, logs, and multiple agents on the same box.

Older but still viable:

- **G5 instances** use NVIDIA A10G 24 GB GPUs.
- G6 is usually the better first comparison for AI inference if available in the target region.

## Sydney pricing reference from session check

Pricing checked against AWS public pricing data for Linux on-demand in `ap-southeast-2` during this session. Re-check before quoting a client.

- g6.xlarge: about **$1.0464 USD/hour**, **$763.87 USD/month** at 730 hours.
- g6.2xlarge: about **$1.27107 USD/hour**, **$927.88 USD/month** at 730 hours.
- g6.4xlarge: about **$1.72042 USD/hour**, **$1,255.91 USD/month** at 730 hours.
- g5.xlarge: about **$1.308 USD/hour**, **$954.84 USD/month** at 730 hours.
- g5.2xlarge: about **$1.57584 USD/hour**, **$1,150.36 USD/month** at 730 hours.
- g5.4xlarge: about **$2.11152 USD/hour**, **$1,541.41 USD/month** at 730 hours.

Use AWS Pricing Calculator before implementation: https://calculator.aws/

## Testing protocol

Run a short proof before committing to monthly architecture.

Test:

1. Ollama install and model pull.
2. 19 GB model loads and stays warm.
3. Hermes connects to Ollama endpoint.
4. One Telegram agent responds through Hermes.
5. Real tasks, not just “hello”: document summary, sales email, coaching plan review, transcript actions, Brock-style recommendation.
6. Two to three concurrent requests.
7. RAM, GPU memory, disk, response speed, and crash/reload behaviour.

Pass condition:

- Response speed feels commercially acceptable.
- Model does not constantly unload or crash.
- Hermes can use the model through a profile.
- Logs and health checks show stable operation.

## Product positioning

Do not blur the offer.

- **PerformOS Local Appliance**: model runs on Mac at the client-approved site.
- **PerformOS Private Cloud AI Team**: model runs on AWS EC2 GPU in a dedicated private cloud environment.
- **PerformOS Managed Hybrid**: client-site model for sensitive workflows, Lightsail or AWS control layer for monitoring, updates, support, and dashboards.

Customer-safe wording:

> We do not run client systems from a home device. PerformOS is deployed either inside your approved environment or inside a dedicated private cloud environment.

## Pitfalls

- Do not sell CPU Lightsail as the “best local model” path.
- Do not expose Ollama publicly on `0.0.0.0:11434` without a private network, firewall, authentication, and approved access controls.
- Do not leave EC2 GPU running after tests. It charges while running.
- Do not size always-on Ollama based only on the model file size.
- Do not call AWS-hosted inference “local appliance.” Call it private cloud.
