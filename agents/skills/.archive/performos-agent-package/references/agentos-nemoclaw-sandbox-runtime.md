# AgentOS NemoClaw Sandbox Runtime Reference

## Trigger
Use when Jared is shaping AgentOS as a business-grade private AI team, comparing NVIDIA NemoClaw/OpenShell, choosing local AI appliance hardware, or explaining sandboxed agents to clients.

## Core framing
NemoClaw is infrastructure, not the product. AgentOS by PerformOS should own the business agent layer: roles, workflows, approvals, outputs, dashboards, and measurable outcomes.

Client-facing line:

> AgentOS gives your business a private AI team that works inside approved systems, with scoped access, network rules, model routing, audit logs, and human approval gates.

## Plain-language sandbox explanation
A normal agent is like a smart worker sitting at your desk. A sandboxed agent is a smart worker inside a secure office.

The office has:
- approved tools
- restricted internet access
- file boundaries
- start and stop controls
- logs
- model routing
- security policies
- a controlled workspace

Architecture shorthand:

```text
Client systems -> approved connectors -> sandbox -> agent -> approval gate -> output
```

Do not describe this as:

```text
Agent -> everything
```

## What NemoClaw contributes
NVIDIA NemoClaw is an open-source reference stack for running always-on agents inside NVIDIA OpenShell sandboxes. It is relevant because it points to the market direction: agents as managed runtime infrastructure, not agents as chat windows.

Important capabilities to mention:
- guided onboarding
- hardened sandbox blueprints
- routed inference
- network policy enforcement
- agent lifecycle management
- Hermes support
- OpenClaw support

## AgentOS product layers
### Layer one: Infrastructure
- NemoClaw or similar sandbox runtime
- NVIDIA OpenShell
- private cloud containers
- client-site managed appliance
- model routing
- network policy
- logs and monitoring

### Layer two: Agent operations
- specialist agents
- approved tools
- business knowledge
- workflow rules
- approval gates
- escalation rules

### Layer three: Business outcomes
- lead generation
- executive briefings
- HR decision preparation
- learning design
- sales coaching
- customer feedback summaries
- dashboards

Clients pay for layer three. Layer one makes it safe.

## Risk classification model
### Low risk
Public information only. Examples: market research, competitor summaries, public article monitoring.

Controls: basic isolation, limited tools, public web access, no sensitive data.

### Medium risk
Internal business data, but no direct people, money, legal, or customer harm. Examples: sales dashboards, training content, meeting summaries, lead enrichment.

Controls: scoped file access, approved APIs only, no auto-send without review, logs retained.

### High risk
People, money, legal, reputation, or sensitive customer data. Examples: HR legislation, payroll, workplace incidents, customer complaints, executive communications.

Controls: strict network policy, private inference where possible, human approval gates, no direct final action, strong audit logging, narrow data access.

## Human approval model
Use three levels:

1. Draft only: agent produces output, human decides.
2. Recommend and queue: agent prepares action, human approves.
3. Execute within boundaries: agent acts automatically only on pre-approved low-risk actions.

For early AgentOS clients, default to level one or two.

## Deployment options
### Client-site managed appliance
Best for data sovereignty, private inference, and strict client policies.

### Private cloud GPU
Best for scalable proof-of-concept, remote maintenance, and clients comfortable with dedicated cloud infrastructure.

### Hybrid
Best for staged rollouts and mixed-sensitivity workflows.

Hard rule: never position a client system as running from Jared's home Mac, home internet, or personal environment.

## DGX Spark appliance note
NVIDIA DGX Spark is a strong candidate for an AgentOS proof appliance, not a required baseline for all Hermes use.

Relevant specs captured from NVIDIA and AU reseller research:
- NVIDIA GB10 Grace Blackwell Superchip
- 20-core Arm CPU
- Blackwell GPU architecture
- 128GB unified LPDDR5x memory
- 4TB encrypted NVMe storage
- up to 1 petaFLOP FP4
- NVIDIA says models up to 200B parameters
- NVIDIA DGX OS, NVIDIA AI software stack, NemoClaw
- AU reseller price observed: around $7,450 AUD

CEO read:
- Hermes alone: overkill.
- Hermes plus local models plus NemoClaw plus AgentOS proof appliance: strong fit.
- Treat it as a deliberate product proof investment, not a casual computer purchase.

Client-facing framing:

> For clients requiring local AI execution, AgentOS can run on a dedicated NVIDIA AI appliance placed inside the client's approved environment. This supports private agent workflows, local inference, scoped system access, and sandboxed execution without relying on shared public chatbot accounts.

## First pilots to recommend
Best first pilots are low-to-medium risk and visible:
- Executive Briefing Agent
- Sales Lead Agent
- Learning Design Agent

Avoid starting with payroll, terminations, disciplinary matters, live outbound emails, or anything that can damage trust quickly.

## Dashboard source-of-truth pattern
When Jared asks to turn this thinking into an HTML dashboard, build sections for:
- executive overview
- architecture map
- sandbox controls
- agent blueprint library
- risk matrix
- rollout roadmap
- commercial package
- deployment options
- next actions

The dashboard should explain the business model, not just the technology.
