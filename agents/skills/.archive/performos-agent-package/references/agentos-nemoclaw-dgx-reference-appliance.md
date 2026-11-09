# AgentOS NemoClaw and DGX Reference Appliance

Use this reference when Jared is shaping AgentOS as a private AI team product with sandboxed agents, local models, NemoClaw/OpenShell, and a dedicated NVIDIA appliance.

## Strategic framing

AgentOS is not the sandbox. AgentOS is the business agent layer: roles, workflows, approval gates, outputs, governance, and measurable outcomes.

NemoClaw/OpenShell can sit underneath AgentOS as the controlled runtime layer.

Client-facing line:

> AgentOS gives your business a private AI team that works inside approved systems, with scoped access, network rules, model routing, audit logs, and human approval gates.

Avoid saying clients are buying NemoClaw. They are buying controlled business outcomes.

## Recommended product architecture

```text
Client data sources
→ approved connectors
→ sandboxed agent workspace
→ model routing
→ draft, recommendation, or action
→ human approval gate
→ business system
```

Layer model:

1. Infrastructure: DGX Spark, NemoClaw/OpenShell, private cloud, client-site appliance, network policy, model routing, logs.
2. Agent operations: Brock, Bob, Lara, Harry, Polly, Nelly, Sam, and client-specific agents.
3. Business outcomes: lead dashboards, executive briefings, training assets, HR decision preparation, sales coaching, operations reporting.

## DGX Spark judgement

For AgentOS, treat NVIDIA DGX Spark 4TB as the stronger reference-appliance candidate when Jared wants future-proofing.

Why:

- 128GB unified memory for serious local models.
- NVIDIA GB10 Grace Blackwell platform.
- NVIDIA DGX OS and NVIDIA AI software stack.
- NemoClaw/OpenShell alignment.
- 4TB storage gives room for models, containers, sandboxes, vector stores, logs, dashboards, and Obsidian vault data.
- Stronger client-facing credibility than a generic mini PC.

The ASUS Ascent GX10 is a strong value alternative if cost discipline matters, but its common 1TB configuration is the compromise. If ASUS storage is upgradeable, it becomes more attractive. If Jared wants the long-term reference appliance, DGX Spark is the cleaner choice.

## MacBook plus DGX operating model

Recommended split:

```text
MacBook Air = cockpit
DGX Spark = engine room
```

MacBook Air handles:

- Claude/Codex build flow.
- Obsidian editing interface.
- browser review.
- Telegram conversations.
- dashboard review.
- strategic control.

DGX Spark handles:

- Hermes runtime.
- specialist profiles.
- local models.
- NemoClaw/OpenShell sandboxes.
- Ollama or NVIDIA runtime.
- vector stores.
- cron jobs.
- Kanban dispatcher.
- dashboard servers.
- private APIs.
- Obsidian vault storage and agent-readable knowledge base.

Do not frame the DGX as replacing the MacBook. Frame it as the first AgentOS reference node.

## Migration sequence

Do not big-bang migrate everything.

1. DGX as model server: install model runtime, run one small test model, expose one endpoint.
2. DGX as Hermes backend: move default Hermes profile and verify one prompt.
3. Move specialist profiles one at a time and verify each with `hermes --profile <profile> chat -q "Reply exactly OK" --quiet`.
4. Move durable systems: gateway, cron, Kanban DB, dashboard servers, vector stores, Obsidian source vault.
5. Add NemoClaw/OpenShell sandboxing and per-agent policies.

Gateway rule: only one machine should run a given Telegram bot token. MacBook for development. DGX for live gateways.

## Local model stack guidance

On a 128GB DGX Spark, do not default to the biggest model it can technically load.

Recommended stack:

- Daily AgentOS model: 70B to 72B instruct model, quantised.
- Premium local reasoning: 120B class model, ideally NVIDIA-aligned Nemotron if it runs cleanly.
- Fast utility/coding: 30B class coder or Nemotron model.
- Small routing/extraction: 8B to 14B.

200B class models may be possible in heavy quantisation, but treat them as showcase or specialist mode because they leave little headroom for Hermes, tools, sandboxes, context cache, and concurrent jobs.

## Sandbox business controls

Every AgentOS sandbox policy should define:

- allowed systems
- blocked systems
- file access
- API access
- allowed websites
- tools allowed
- model route
- approval rules
- logging rules
- output format
- escalation triggers

Autonomy levels:

1. Draft only.
2. Recommend and queue.
3. Execute within boundaries.

For early clients, default to level one or two. Earn level three through evidence.

## First pilot recommendations

Best first pilots:

- Sales Lead Agent: commercially visible, dashboard-friendly, lower risk.
- Executive Briefing Agent: leadership-facing, low risk, useful demo.
- Learning Design Agent: strong fit with Jared's domain and visible quality.

Avoid starting with payroll, terminations, disciplinary action, high-value financial approvals, or live outbound emails.
