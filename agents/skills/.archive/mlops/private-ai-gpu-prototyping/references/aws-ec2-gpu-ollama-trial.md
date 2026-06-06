# AWS EC2 GPU Ollama Trial Pattern

## Session context

Jared wanted to test a 19 GB Ollama model without committing to a full monthly private-cloud spend. The conversation narrowed the stack from Lightsail plus EC2 to a simpler first proof: one EC2 GPU server running Ollama, Hermes, and a Telegram test bot.

## Key decision

For the first trial, use **EC2 GPU only**.

Do not add Lightsail until the model performance is proven.

Reason:

- one server is easier to debug
- lower trial cost
- fewer moving parts
- proves the model before proving the wider control-layer architecture

## Product architecture distinctions

- **Lightsail:** control layer, support dashboard, monitoring, gateway, logs, admin views.
- **EC2 GPU:** model brain, Ollama, GPU inference, private cloud AI.
- **Client-site Mac:** local appliance, client-trust story, processing inside the client's environment.

Use these terms:

- AWS-hosted GPU = **PerformOS Private Cloud AI Team**
- client-site Mac = **PerformOS Managed Local Appliance**

Do not call EC2 GPU a local appliance.

## Cost framing pattern

Always calculate EC2 by runtime hours first.

For the Sydney `g6.2xlarge` estimate used in the session:

- hourly: about `$1.271 USD/hour`
- 24 hours: about `$30.51 USD`
- seven days at 7:00 am to 10:30 pm Sydney time = 15.5 hours/day x seven days = 108.5 hours
- 108.5 hours: about `$137.91 USD`

The lesson is not the exact price. Prices change. The durable pattern is:

1. multiply hourly price by intended runtime hours
2. convert to AUD if Jared needs local commercial framing
3. compare short trial cost against full 730-hour month
4. stop the instance when not testing

## AWS signup and launch flow

1. Create AWS account at `https://aws.amazon.com/free/`.
2. Open EC2 console at `https://console.aws.amazon.com/ec2/`.
3. Pick region based on goal:
   - Sydney for Australian-client realism and data-residency story
   - US East N. Virginia for cheaper technical proof and better new-account availability
4. If AWS blocks Sydney on a fresh account, do not fight it during proof-of-concept. Switch to US East N. Virginia and prove the stack first.
5. Launch instance.
6. Choose a GPU-ready AMI:
   - **Deep Learning Base AMI with Single CUDA** when available
   - in US East, **Deep Learning OSS Nvidia Driver AMI GPU PyTorch Ubuntu** is a good option
   - x86 64-bit, not ARM
   - avoid Neuron AMIs for G6 because those are for AWS Inferentia/Trainium, not NVIDIA GPU
7. Choose instance:
   - preferred: `g6.2xlarge`
   - cheaper/tighter: `g6.xlarge`
   - if `g6f.2xlarge` appears, verify GPU details before recommending
8. Storage:
   - target at least 200 GiB
   - Deep Learning AMI may show two volumes and a higher total such as 480 GiB or 650 GiB
   - do not launch with a 1 GiB root volume just because AWS accepts the field
9. Network:
   - auto-assign public IP enabled for SSH access
   - create a new security group
   - allow SSH from **My IP** only
   - do not allow SSH from Anywhere if avoidable
   - leave HTTP and HTTPS unchecked for the first test
   - do not open Ollama port `11434`
10. Key pair:
   - create a new key pair if none exists
   - use RSA and `.pem` for Mac terminal access
   - store the key-pair note safely in Bitwarden
11. Launch.
12. Stop instance after testing.

## New AWS account blockers

### Region validation or new-account region restriction

Fresh AWS accounts may not be able to launch EC2 in every region immediately. AWS may say the region is being validated, or it may list only initial regions such as:

- US East N. Virginia
- US West Oregon
- US East Ohio

For a proof-of-concept, switch to **US East N. Virginia** rather than losing time. It is usually cheaper and has broad instance availability. Move to Sydney later when the client story or latency matters.

### GPU quota set to zero

Fresh AWS accounts commonly have **0 vCPUs** for GPU families. The launch failure may mention that the request exceeds current vCPU limits for G instances.

Quota path:

```text
Service Quotas → AWS services → Amazon Elastic Compute Cloud (Amazon EC2) → Running On-Demand G and VT instances
```

Request:

- Region: US East N. Virginia, unless testing another allowed region
- Requested value: 16 vCPUs
- Minimum required for one `g6.2xlarge`: 8 vCPUs

Justification if AWS asks:

```text
This is for a short private proof-of-concept to test AI inference using Ollama on one EC2 G6 instance. The workload is not production-facing, will not serve public traffic, and the instance will be stopped when not actively testing.
```

If the Service Quotas page shows quotas for **Service Quotas** itself, it is the wrong page. Navigate to **Amazon Elastic Compute Cloud (Amazon EC2)** first, then search `G and VT`.

## Screenshot interpretation notes

If AWS shows an instance such as `m7i-flex.large`, `t`, `m`, `c`, or `r` family, it is not the GPU test instance. It may be free-tier eligible, but it will not prove a 19 GB Ollama GPU stack.

If the AMI screen shows plain Amazon Linux, it can work but may require manual GPU driver and CUDA setup. Prefer the Deep Learning Base AMI with Single CUDA for a fast proof.

If the security group source shows `Anywhere 0.0.0.0/0` for SSH, steer Jared to **My IP**.

If storage appears larger than planned because the Deep Learning AMI includes extra volume capacity, note the extra cost but do not block the trial unless cost control is the dominant concern.

If AWS shows `1 GiB` as the lowest editable root volume, do not assume it is safe. The form allowing 1 GiB does not mean the OS and AI stack will work. Prefer at least 100 GiB, ideally 200 GiB, unless the AMI clearly provides a separate large usable volume and the launch summary is acceptable.

If AWS asks for a key pair, create one. Do not proceed without a key pair. For Jared's Mac workflow, use RSA and `.pem`, then connect with `ssh -i <key>.pem ubuntu@<public-ip>` or the AMI's documented username.

## First server setup concept

Once launched, the server should run:

```text
EC2 GPU instance
  Ollama
  19 GB model
  Hermes
  one test profile
  optional Telegram bot
```

Hermes should call Ollama locally:

```text
http://127.0.0.1:11434/v1
```

Keep Ollama private. Do not expose it to the public internet.

## Secrets handling for the trial

Use Bitwarden as the master vault. Do not connect an agent to the full vault by default.

Safe pattern:

```text
Bitwarden master vault
↓
manual copy or controlled deploy script
↓
Hermes .env or profile .env
↓
specific agent uses only the key it needs
```

Store these in Bitwarden:

- AWS root account entry
- AWS recovery codes
- EC2 key-pair note, not casually pasted into chat
- Telegram bot tokens
- Hermes provider keys
- GitHub tokens
- Zapier notes or tokens if used

Do not ask for:

- Bitwarden master password
- full vault export
- AWS root password in chat
- recovery codes in chat
- unrestricted vault access for agents

Early-stage recommendation: use manual copy from Bitwarden into `.env` files. Only automate with the Bitwarden CLI after the AWS/Ollama stack is working and the secret flow is deliberate.

## Test sequence

### Four-hour install test

Pass conditions:

- SSH works
- GPU is visible
- Ollama installs
- model pulls
- model runs one response
- Hermes can call local Ollama

### Eight-hour quality test

Pass conditions:

- realistic PerformOS tasks feel useful
- response speed is tolerable
- one agent profile works
- Telegram works if included

### 72-hour stability test

Run only after quality passes.

Pass conditions:

- model stays warm
- service survives normal use
- logs are clean enough
- restart path works
- costs are understood

## Pitfalls

- Do not advise launching free-tier CPU instances for the large Ollama model.
- Do not combine Lightsail plus EC2 for the first proof unless Jared explicitly wants the control-layer test too.
- Do not leave the GPU running overnight by accident.
- Do not terminate the instance while Jared still wants to keep setup work.
- Do not open Ollama publicly.
- Do not let the infrastructure conversation drift away from the commercial decision: does the model feel good enough to sell?
- Do not assume AWS signup means GPU launch is available. New accounts often need G and VT quota approval first.
- Do not let Jared burn time in Sydney if AWS only permits US regions during initial validation. Use US East for proof, then migrate later.
- Do not connect agents to the full Bitwarden vault. Agents get specific keys, not vault-wide access.