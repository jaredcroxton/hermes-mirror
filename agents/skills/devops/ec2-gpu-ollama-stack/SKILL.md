---
name: ec2-gpu-ollama-stack
description: Cost-controlled AWS EC2 GPU trials for Ollama local-model inference with Hermes agents.
version: 1.0.0
author: Brock / PerformOS
created_by: agent
tags: [aws, ec2, gpu, ollama, hermes, private-cloud, cost-control]
---

# EC2 GPU Ollama Stack

Use this when Jared wants to test or explain running Ollama and Hermes on an AWS GPU server, especially for a large local model such as a 19 GB Ollama model.

## Operating judgement

Do not overbuild the stack before proving the model.

Best first trial:

1. Use **one EC2 GPU instance only**.
2. Run **Ollama and Hermes on the same server**.
3. Keep Ollama private on `127.0.0.1:11434`.
4. Test one model, one Hermes profile, and one Telegram bot.
5. Stop the instance when finished.
6. Add Lightsail later only if a separate always-on control layer is needed.

## Product-language distinction

Use the right label:

- **Local appliance:** model runs on a Mac or server physically at the client site.
- **Private cloud:** model runs on a dedicated cloud GPU server.
- **Hybrid:** Lightsail or another control layer manages a client-site appliance or EC2 GPU model server.

Do not call EC2 GPU “local to the client office.” It is local only to the AWS server.

## Recommended trial shape

For Jared's 19 GB Ollama model, the preferred test instance is:

- **Instance:** `g6.2xlarge`
- **AMI:** Deep Learning AMI with CUDA, ideally Ubuntu or Amazon Linux Deep Learning Base AMI with Single CUDA
- **Storage:** 200 GB minimum if editable; accept larger AMI-required volumes if needed
- **Inbound security:** SSH only, source set to **My IP**
- **Do not open:** Ollama port `11434`
- **File systems:** None

If AWS exposes `g6f.2xlarge` with 8 vCPU, 32 GiB memory, and GPU at materially lower pricing, it can be used for a cost test, but confirm GPU details before launch.

## Region choice

For first proof:

- Prefer **US East, N. Virginia** if AWS restricts a new account to starter regions or if cost matters most.
- Prefer **Sydney** when testing Australian client latency or data-residency positioning.

New AWS accounts may not allow Sydney or GPU launch immediately. If AWS says the region is being validated, do not keep relaunching. Use an allowed starter region or wait for validation.

## Cost-control pattern

Do not start with 24/7 monthly operation.

Run test windows:

1. Four-hour install test
2. Eight-hour quality test
3. 72-hour stability test only if quality passes
4. Monthly always-on only after the model feels sellable

For a scheduled trial window, calculate:

```text
hourly_price × hours_per_day × days
```

Jared's discussed window was **7:00 am to 10:30 pm Sydney time**, which is 15.5 hours per day.

## Launch checklist

Before launch, verify:

- AMI: Deep Learning AMI with CUDA
- Architecture: x86 64-bit for G6
- Instance family: starts with `g6`, not `m`, `t`, `c`, or `r`
- Instance type: preferably `g6.2xlarge`
- SSH: **My IP**, not Anywhere
- HTTP/HTTPS: unchecked unless a dashboard is intentionally being exposed
- Ollama port `11434`: not exposed publicly
- Storage: not a tiny 1 GiB root unless the AMI clearly provisions a separate usable boot/root volume
- File systems: None

## Setup commands once connected

Use the actual AMI's package manager and shell, but the basic path is:

```bash
# Check GPU
nvidia-smi

# Install Ollama
curl -fsSL https://ollama.com/install.sh | sh

# Pull and test model
ollama pull <model-name>
ollama run <model-name>

# Install Hermes
curl -fsSL https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh | bash

# Point Hermes at local Ollama
hermes config set model.base_url http://127.0.0.1:11434/v1
hermes config set model.default <model-name>
hermes config set model.api_key ollama

# Verify
hermes chat -q "Reply exactly OK" --quiet
```

## Verification commands

After launch, check real server state:

```bash
nvidia-smi
lsblk
df -h
free -h || vmstat 1 5
curl http://127.0.0.1:11434/api/tags
```

Then run a real quality prompt, not just “hello.” Test:

- strategic recommendation
- document summary
- sales email draft
- training outline
- two or three near-concurrent requests

## Pitfalls

- **Free-tier EC2 is not enough.** Free-tier or low-cost `m`, `t`, `c`, or `r` instances are CPU servers and do not prove the Ollama GPU stack.
- **Windows is the wrong default.** Use Ubuntu or a Deep Learning AMI. Windows adds driver friction, licensing cost, and setup complexity.
- **Lightsail is optional for the first test.** It is useful later as a control layer, but it is not required to run Ollama or Hermes.
- **Do not expose Ollama publicly.** Keep `11434` bound/private. Hermes can call it over `127.0.0.1` when both run on the same EC2 instance.
- **Do not optimise storage into failure.** A 1 GiB root volume is unsafe unless the AMI clearly provides another usable root/working volume. For a serious test, use 100 to 200 GiB root or accept the AMI's required large volume.
- **Stop is not terminate.** Stop the instance between tests to stop compute charges while keeping the disk. Terminate only when finished with the build.

## Supporting references

- `references/aws-ec2-gpu-ollama-trial-notes.md` captures session-specific pricing, screenshots, and launch decisions from Jared's first EC2 GPU/Ollama trial path.
