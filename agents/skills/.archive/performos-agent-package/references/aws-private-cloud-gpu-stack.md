# AWS Private Cloud GPU Stack for PerformOS

Use this reference when Jared is evaluating an AWS-hosted private-cloud version of the PerformOS AI Team with Ollama and Hermes.

## Core distinction

Do not call this a local appliance. If Ollama runs on AWS, the product is **PerformOS Private Cloud AI Team**.

Use:
- **Local Appliance** when the model runs on a PerformOS-owned Mac or appliance inside the client-approved environment.
- **Private Cloud** when the model runs on dedicated AWS compute managed by PerformOS.
- **Hybrid** when a cloud control layer monitors or manages a client-site appliance.

## Recommended proof stack

For a 19 GB Ollama model:

- AWS EC2 **g6.2xlarge** as the first serious GPU test tier.
- Ubuntu Deep Learning AMI where possible, to reduce NVIDIA driver setup friction.
- 200 GB storage minimum for the first test.
- Ollama and Hermes can run on the same EC2 instance for the first proof because it removes network complexity.
- Add Lightsail only after model quality and speed are proven.

## Pricing anchors from the session

Sydney g6.2xlarge estimate:
- About **$1.271 USD/hour**.
- About **$927.88 USD/month** at 730 hours.
- About **$1,293 AUD/month** using the checked exchange rate from the session.

US East g6.2xlarge estimate:
- About **$0.9776 USD/hour**.
- About **$713.65 USD/month** at 730 hours.

Sydney g6.xlarge estimate:
- About **$1.0464 USD/hour**.
- About **$763.87 USD/month** at 730 hours.
- Lower cost, but tighter for a 19 GB model because system RAM is limited.

Sydney g6.4xlarge estimate:
- About **$1.720 USD/hour**.
- About **$1,255.91 USD/month** at 730 hours.
- Safer if Hermes, dashboards, logs, and multiple agents run on the same server.

Lightsail $384/month plan:
- Useful as a control layer or CPU-only experiment.
- Not the best model engine for a 19 GB Ollama model because it has no GPU.

## Low-cost trial pattern

Do not start 24/7.

Use scheduled runtime:
- 7:00 am to 10:30 pm Sydney time = 15.5 hours/day.
- Seven days = 108.5 GPU hours.

Approx EC2 cost for g6.2xlarge:
- Sydney: **$137.91 USD / $192.21 AUD** for 108.5 hours.
- US East: **$106.07 USD / $147.83 AUD** for 108.5 hours.

If combining with full-month Lightsail $384:
- Sydney EC2 trial plus full Lightsail month: about **$521.91 USD / $727.41 AUD**.
- US East EC2 trial plus full Lightsail month: about **$490.07 USD / $683.03 AUD**.

## Best sequence

1. Test EC2 only first.
2. Put Ollama, the 19 GB model, Hermes, and one test Telegram agent on the same g6.2xlarge.
3. Run short sessions first: 4 hours, 8 hours, 24 hours.
4. Stop the instance when not testing.
5. If model speed and quality pass, run the seven-day scheduled trial.
6. Add Lightsail as the control layer only after the model proves useful.

## Pass criteria

A trial only passes if:
- Ollama loads the 19 GB model successfully.
- GPU is being used.
- Hermes can call Ollama through `http://127.0.0.1:11434/v1`.
- One Telegram agent can complete real tasks.
- Response speed feels commercially usable.
- The model survives repeated prompts and short concurrent use.
- Stopping and restarting the instance does not break the setup.

## Cost-control rules

- Stop EC2 when not testing.
- Set AWS billing alerts at low thresholds such as $25, $50, and $100.
- Do not create multiple GPU instances during proof.
- Keep storage modest at first.
- Delete unused snapshots and volumes after testing.
- Do not leave GPU instances running overnight unless stability is the thing being tested.

## AWS console launch guidance

When Jared is walking through the AWS console from screenshots, steer him to the GPU choices and away from free-tier CPU defaults.

### Account and entry links

- AWS signup/free account: `https://aws.amazon.com/free/`
- AWS console: `https://console.aws.amazon.com/`
- EC2 console: `https://console.aws.amazon.com/ec2/`
- EC2 G6 instance page: `https://aws.amazon.com/ec2/instance-types/g6/`
- EC2 on-demand pricing: `https://aws.amazon.com/ec2/pricing/on-demand/`
- AWS pricing calculator: `https://calculator.aws/`

### Free-tier trap

If AWS only offers or highlights instances like `m7i-flex.large`, `t*`, `m*`, `c*`, or `r*`, explain that these are CPU instances. They are fine for learning EC2 and SSH, but they do not prove the Ollama GPU stack.

For the 19 GB Ollama model, look for an instance type starting with `g6`, preferably `g6.2xlarge`.

### Quota and new-account traps

New AWS accounts often cannot launch GPU instances immediately. If `g6.2xlarge` is missing or blocked, route Jared to **Service Quotas** and request:

- Quota name: `Running On-Demand G and VT instances`
- Region: `Asia Pacific (Sydney) ap-southeast-2` if testing Australian client conditions
- If AWS only permits starter regions on a new account, use `US East (N. Virginia) us-east-1` first and move to Sydney later.
- Minimum request: `8 vCPUs` for one `g6.2xlarge`.
- Better request: `16 vCPUs` for headroom.

Suggested quota request text:

```text
I am testing a short-term AI inference workload using Ollama on an EC2 G6 instance. I need access to one g6.2xlarge instance for a limited proof-of-concept. The instance will be stopped when not in use. Please increase my Running On-Demand G and VT instances quota to 16 vCPUs.
```

Common screenshot pitfall: if the breadcrumb says `Service Quotas > AWS services > Service Quotas`, Jared is looking at quotas for the Service Quotas product itself, not EC2. The request button will be greyed out because those rows are not EC2 GPU quotas. Route him to:

1. `Service Quotas`.
2. Left menu `AWS services`.
3. `Amazon Elastic Compute Cloud (Amazon EC2)`.
4. Search `G and VT`.
5. Open `Running On-Demand G and VT instances`.
6. Request account-level increase to `16`.

If the launch error says the quota is `0 vCPUs`, do not switch to a CPU instance. The setup is fine; the account needs GPU quota approval.

### AMI choice

For a first EC2 GPU Ollama test, prefer a GPU-ready x86 Deep Learning AMI, for example:

- `Deep Learning Base AMI with Single CUDA`.
- `Deep Learning OSS Nvidia Driver AMI GPU PyTorch ... (Ubuntu 24.04)`.
- `64-bit x86`.
- Supports G5, G6, G6e, and other NVIDIA GPU families.

This reduces NVIDIA/CUDA driver setup friction compared with a plain Amazon Linux or Ubuntu AMI.

Do not choose ARM for `g6.2xlarge`. Do not choose Neuron AMIs for G6; Neuron is for AWS Inferentia/Trainium, not NVIDIA GPU. If AWS warns that changing the AMI will reset security groups or delete old draft volumes, confirm the change, then re-check SSH/security/storage before launching.

### Instance type screenshot checks

- Free-tier-looking defaults such as `m7i-flex.large` are CPU-only and wrong for the 19 GB Ollama GPU proof.
- `g6.2xlarge` is the preferred first serious test.
- If AWS offers `g6.xlarge`, it is the cheapest GPU test but tighter.
- If AWS offers `g6f.2xlarge` or `g6f.4xlarge`, treat them as possible low-cost test options only after confirming the details show an NVIDIA GPU and GPU memory. Do not launch an unfamiliar family just because the hourly price is attractive.

### Launch guardrails

- Use about 200 GB storage for the proof if you control the root volume.
- Some Deep Learning AMIs add required secondary volumes, so the launch summary may show 450 GB to 650 GB total. This is acceptable for a short proof. Do not spend 10 minutes fighting AMI-required storage if the GPU/AMI/security settings are correct.
- Do not set the root volume to 1 GiB just to minimise storage. The form may accept it, but the OS, CUDA stack, Ollama, Hermes, and model files need real space.
- Allow SSH port 22 only from Jared's current IP where possible. If Jared sets `My IP` from his phone, warn that his Mac must be on the same public IP or SSH will fail.
- Do not open HTTP/HTTPS unless the proof actually needs a web dashboard.
- Do not open Ollama port `11434` to the internet.
- Keep Ollama bound locally for the proof: `http://127.0.0.1:11434/v1`.
- Stop the instance when testing ends. Terminate only when intentionally deleting the server.

## Positioning language

Customer-facing phrase:

> PerformOS Private Cloud AI Team runs on dedicated AWS GPU infrastructure managed by PerformOS, with private model hosting, audit logs, controlled access, and managed support.

Do not say:

> It runs locally.

Say:

> It runs in a dedicated private cloud environment.
