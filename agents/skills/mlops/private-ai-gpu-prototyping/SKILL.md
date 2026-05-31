---
name: private-ai-gpu-prototyping
description: Use when Jared wants to test or explain a private cloud/local AI stack using Ollama, Hermes, EC2 GPU, Lightsail, or client-site hardware. Covers low-cost trial design, AWS EC2 GPU launch checks, cost control, and plain-English product positioning.
version: 1.0.0
author: Brock / PerformOS
created_by: agent
tags: [ollama, ec2, gpu, lightsail, private-cloud, local-ai, performos, aws]
---

# Private AI GPU Prototyping

## Trigger

Use this when Jared asks about:

- running Ollama locally or in AWS
- testing a large local model on EC2 GPU
- comparing Lightsail, EC2 GPU, and client-site Mac options
- setting up a private cloud AI stack for PerformOS
- sizing infrastructure for a 19 GB Ollama model
- keeping cloud testing cheap before committing to monthly spend
- interpreting AWS EC2 launch screenshots for GPU AI testing
- handling new AWS account GPU quota blockers and region restrictions
- storing AWS, EC2, Telegram, and Hermes trial secrets safely during prototyping

## Core judgement

Keep the product story clean:

- **Lightsail** = control layer, dashboards, monitoring, gateways, support, lightweight workloads.
- **EC2 GPU** = private cloud model brain for Ollama and heavier inference.
- **Client-site Mac** = local appliance story for clients who want processing in their office.

Do not blur these. Jared needs the commercial positioning as much as the technical answer.

## Recommended first trial stack

For Jared's first private-cloud Ollama proof:

1. Use **one EC2 GPU server only**.
2. Put **Ollama, the model, Hermes, and one Telegram test bot on the same instance**.
3. Do not add Lightsail until the model performance is proven.
4. Stop the instance when finished testing.

Preferred test instance:

- `g6.2xlarge` if available and affordable
- Deep Learning Base AMI with Single CUDA
- x86 64-bit
- 200 GB storage minimum, but AWS Deep Learning AMIs may add more storage by default
- SSH allowed from **My IP**, not Anywhere
- no inbound rule for Ollama port `11434`

If a cheaper GPU family such as `g6f.2xlarge` appears, check that it genuinely includes a GPU before recommending launch.

## Low-cost testing sequence

Use a staged test. Do not start with a full month.

1. **Four-hour install test**
   - prove GPU is available
   - install Ollama
   - pull the model
   - run one prompt
   - connect Hermes to local Ollama

2. **Eight-hour quality test**
   - test real PerformOS tasks
   - test one agent profile
   - test Telegram if needed
   - judge speed and answer quality

3. **72-hour stability test**
   - only if the quality test passes
   - keep model warm
   - test restarts, logs, and basic health checks

## AWS launch checklist

Before launch, confirm:

- Region matches the test goal. Sydney for Australian-client realism. US East for cheaper proof testing.
- New accounts may only allow launch in US East N. Virginia, US East Ohio, or US West Oregon at first. Do not fight this for the first proof. Use US East N. Virginia if Sydney is blocked.
- AMI is a GPU-ready Deep Learning AMI or equivalent. In US East, **Deep Learning OSS Nvidia Driver AMI GPU PyTorch Ubuntu** is a good option.
- Instance type starts with `g`, such as `g6.2xlarge`. Avoid `m`, `t`, `c`, and `r` for the Ollama GPU test.
- It shows GPU capability, ideally NVIDIA L4 or equivalent with enough GPU memory.
- SSH source is **My IP**.
- HTTP and HTTPS are unchecked unless there is a specific dashboard or web app to expose.
- No inbound Ollama port is opened.
- Storage is large enough for the AMI, Ollama, model files, Hermes, packages, and logs. Do not launch with a 1 GiB root volume just because the form allows it.
- File systems such as EFS, FSx, and S3 Files are not added for the first test.
- A key pair exists before launch. For Jared on Mac, use RSA and `.pem`.

## New AWS account GPU quota blocker

If launch fails with a vCPU quota error for G instances, the account likely has GPU quota set to zero. Route Jared to:

```text
Service Quotas → AWS services → Amazon Elastic Compute Cloud → Running On-Demand G and VT instances
```

For one `g6.2xlarge`, request at least **8 vCPUs**. Prefer **16 vCPUs** because it is still modest and gives room for testing. If AWS asks for justification, say it is a short private AI inference proof-of-concept using Ollama and the instance will be stopped when not actively testing.

## Cost-control rules

Always frame EC2 as hourly until Jared deliberately chooses always-on.

- Stop the instance when not testing.
- Do not terminate until the trial is fully finished, because termination deletes the server.
- Watch storage and snapshots. They can still cost money after compute is stopped.
- Set AWS billing alerts early.
- Test performance first, architecture second.

## Hermes plus Ollama pattern

When Ollama and Hermes live on the same EC2 server:

```text
Telegram or dashboard
↓
Hermes on EC2
↓
Ollama local API
↓
GPU model
↓
Hermes response back to user
```

Ollama should stay private:

```text
http://127.0.0.1:11434/v1
```

Do not expose Ollama publicly unless there is proper VPN, firewalling, authentication, and a deliberate security design.

## Secrets pattern for trials

Use Bitwarden as the master vault, not as an open vault connected to the agent. Agents get only the specific key needed for a specific task.

Recommended pattern:

```text
Bitwarden master vault
↓
manual copy or controlled deploy script
↓
Hermes .env or profile .env
↓
Hermes uses only that secret
```

For early trials, prefer manual copy over Bitwarden CLI automation. Store AWS account details, EC2 key-pair notes, Telegram bot tokens, Hermes provider keys, GitHub tokens, and recovery codes in Bitwarden. Do not ask Jared for or store Bitwarden master passwords, AWS root passwords, recovery codes, or full-vault access in an agent session.

## Positioning language

For AWS-hosted GPU:

**PerformOS Private Cloud AI Team**

For client-site hardware:

**PerformOS Managed Local Appliance**

Avoid calling AWS EC2 GPU a local appliance. It is private cloud, not physically local to the client.

## Plain-English explanation pattern

When Jared asks what EC2 GPU is, explain it like this:

- Lightsail is a regular rented office computer in the cloud.
- EC2 GPU is a rented workstation or gaming PC in the cloud.
- The GPU is the muscle that makes local AI models respond faster.
- EC2 gives you a server to build on, but AWS charges while it is running.

## Pitfalls

- Do not recommend the free-tier EC2 instance for a 19 GB Ollama model. It is usually CPU-only and too small.
- Do not let Jared launch SSH as `Anywhere 0.0.0.0/0` if **My IP** is available.
- Do not open port `11434` to the internet.
- Do not add Lightsail before the EC2 GPU model performance is proven.
- Do not overbuild dashboards, support systems, or multi-agent profiles before confirming the model runs well.
- Do not treat monthly price as the first decision. First test hourly for a few hours.

## Reference

See `references/aws-ec2-gpu-ollama-trial.md` for the detailed session-derived trial pattern, screenshot interpretation notes, quota workflow, Bitwarden secret-handling pattern, and cost framing.