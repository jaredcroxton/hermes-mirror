# DGX Spark as AgentOS Reference Appliance

Use when Jared compares DGX Spark, ASUS Ascent GX10, Mac mini, Mac Studio, or Windows RTX workstations for AgentOS, Hermes, NemoClaw, and local model deployment.

## Strategic framing

For AgentOS, the DGX Spark should be framed as the first **AgentOS reference appliance**, not just a faster computer.

Recommended language:

> MacBook Air = cockpit. DGX Spark = engine room.

Client-facing language:

> AgentOS can run on a dedicated NVIDIA AI appliance inside the approved client environment. Users access it through chat or browser interfaces, while the models, agents, sandboxes, and governance controls run locally on the appliance.

## Recommended architecture

MacBook Air remains the control surface:

- Claude Code and Codex build work
- browser review
- Obsidian desktop editing
- Telegram conversations
- dashboard review
- strategy and writing

DGX Spark becomes the operational node:

- Hermes runtime
- specialist agent profiles
- local LLM inference
- NemoClaw and OpenShell sandboxes
- Ollama or NVIDIA model runtime
- vector stores and indexes
- cron jobs
- Kanban dispatcher
- dashboard servers
- private APIs
- Obsidian vault storage or agent-accessible mirror

## Obsidian nuance

Do not describe Obsidian as “running” on the DGX Spark. Obsidian is mainly markdown files plus a desktop app.

Best model:

```text
Obsidian vault source of truth or agent-write mirror → DGX Spark
Obsidian app/editor → MacBook Air
Sync/access method → Git, Syncthing, SMB, or Tailscale file share
```

Agents should write into defined vault zones such as `Agent Outputs/` or `PerformOS/AgentOS/` to reduce sync conflicts.

## Migration sequence

Do not big-bang migrate.

1. **DGX as model server**
   - Install local model runtime.
   - Run one test model.
   - Verify a local API endpoint from MacBook.

2. **DGX as Hermes backend**
   - Move default Hermes profile.
   - Verify config, skills, memory, sessions.
   - Keep MacBook as access device.

3. **Move specialist agents one by one**
   - Move Bob, Lara, Harry, Polly, Nelly, Sam, and others sequentially.
   - Probe each profile with `hermes --profile <profile> chat -q "Reply exactly OK" --quiet`.
   - Do not move all profiles before testing.

4. **Move durable systems**
   - Kanban DB.
   - Cron jobs.
   - Gateway service.
   - Dashboard servers.
   - Vector stores.
   - Obsidian vault or mirror.

5. **Add sandbox layer**
   - NemoClaw.
   - OpenShell.
   - Per-agent sandbox profiles.
   - Network rules.
   - Approval gates.
   - Model routing.

## DGX Spark vs ASUS Ascent GX10

Both are strong if they share the NVIDIA GB10, 128GB unified memory, DGX OS, and NemoClaw/Hermes readiness.

Decision rule:

- ASUS Ascent GX10 is a strong value proof machine if the goal is cost discipline.
- DGX Spark 4TB is the stronger long-term reference appliance because of storage headroom and cleaner NVIDIA appliance positioning.

Storage matters because AgentOS accumulates local models, quantized variants, Docker images, NemoClaw sandboxes, vector databases, logs, session history, dashboard builds, and backups.

## Risks to manage

- ARM compatibility for Python packages, browser drivers, Node packages, and compiled dependencies.
- Obsidian sync conflicts if agents and Jared edit the same files.
- Secrets migration from `.env`, `auth.json`, profile credentials, Telegram tokens, Google OAuth, GitHub, and Vercel.
- Gateway ownership. Only one machine should run a Telegram bot token at a time.
- Backup discipline. If DGX becomes the brain, daily `.hermes` and vault backups are mandatory.

## CEO judgement

DGX Spark is not the best buy for casual Hermes use. It is the better buy if Jared commits to making it the reference AgentOS node for local models, sandboxed agents, NemoClaw, and client-grade private AI team demonstrations.
