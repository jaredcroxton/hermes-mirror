# AWS EC2 GPU Ollama Trial Notes

Session-specific detail from Jared's EC2 GPU/Ollama trial planning.

## User goal

Jared wanted to test a **19 GB Ollama model** without committing to a full always-on monthly bill.

The stack under consideration:

- Ollama
- 19 GB model
- Hermes
- Telegram bot or agent profile
- AWS EC2 GPU

## Key decision

For the first trial, run **EC2 only**:

```text
EC2 GPU server
  Ollama
  19 GB model
  Hermes
  Telegram bot
  logs
```

Do **not** add Lightsail at first. Lightsail is useful later for dashboards, monitoring, support tickets, or multi-client control, but it is unnecessary before the model is proven.

## Pricing figures used in-session

Pricing was checked during the session from AWS pricing data and converted using a live USD to AUD rate around **1.393744**.

Approximate examples discussed:

- `g6.2xlarge` in **US East**: about **$0.9776 USD/hour**
- `g6.2xlarge` in **Sydney**: about **$1.27107 USD/hour**
- `g6.xlarge` in **US East**: about **$0.8048 USD/hour**
- `g6.xlarge` in **Sydney**: about **$1.0464 USD/hour**

For Jared's proposed seven-day testing window, **7:00 am to 10:30 pm Sydney time**, total runtime was:

```text
15.5 hours/day × 7 days = 108.5 hours
```

Estimated `g6.2xlarge` trial cost:

- Sydney: about **$137.91 USD**, about **$192.21 AUD**
- US East: about **$106.07 USD**, about **$147.83 AUD**

These are directional only. Always recheck AWS pricing before launch.

## Region issue

A new AWS account may not allow launching in Sydney immediately. AWS may restrict first launches to regions such as:

- US East, N. Virginia
- US West, Oregon
- US East, Ohio

If that happens, use **US East, N. Virginia** for the proof instead of fighting the account validation flow.

## Screenshot-driven choices from the session

### AMI

Preferred:

- Deep Learning Base AMI with Single CUDA
- Deep Learning AMI with CUDA
- x86 64-bit for G6

Avoid for this trial:

- Windows
- plain free-tier Amazon Linux unless manually installing GPU drivers

### Instance type

Avoid:

- `m7i-flex.large`
- anything free-tier CPU-only
- families starting with `m`, `t`, `c`, or `r`

Use:

- `g6.2xlarge` for the safer 19 GB model test
- `g6.xlarge` only for a cheaper but tighter proof
- `g6f.2xlarge` only if AWS exposes it with confirmed GPU details and favourable pricing

### Network settings

Use:

- Auto-assign public IP: enabled
- Create security group: yes
- SSH: enabled
- SSH source: **My IP**
- HTTP/HTTPS: unchecked

Avoid:

- SSH from Anywhere `0.0.0.0/0`
- opening Ollama port `11434`

### Storage

Minimum safe root target:

- 100 GiB acceptable
- 200 GiB preferred

If the Deep Learning AMI adds a required large volume, do not fight it during a short trial. Compute is the main cost driver.

Do not launch with an obviously tiny 1 GiB root volume unless it is proven the AMI's larger volume is the true usable system volume.

## Plain-English explanation used

EC2 GPU is a rented AWS computer with a powerful graphics card built for AI work.

- Lightsail is like a regular office laptop in the cloud.
- EC2 GPU is like a rented workstation or gaming PC in the cloud.
- The GPU is the muscle that makes local AI models respond faster.

## Product-language guidance

If the model runs on EC2, call it:

```text
PerformOS Private Cloud AI Team
```

If the model runs on a client-site Mac or server, call it:

```text
PerformOS Local Appliance
```

Do not blur these two. The trust story changes depending on where the model runs.
