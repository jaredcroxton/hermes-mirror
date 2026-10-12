# AgentOS EC2 Governance Model

How to run a multi-machine agent ecosystem where Obsidian is the source of truth and EC2 is the runtime engine. This is the deployment pattern for PerformOS/AgentOS client setups.

## The split

| Layer | Where | What |
|---|---|---|
| Source of truth | Mac (Obsidian vault) | SOUL files, custom skills, agent registry, governance docs |
| Runtime engine | EC2 (or client appliance) | Hermes profiles, Ollama, model files, gateway services, session logs |
| Visual demo | EC2 → browser | Open WebUI on port 8080 |
| Client access | Telegram/Slack | Hermes gateway → messaging platform |

## Obsidian folder structure (source of truth)

```
~/Desktop/Obsidian/
├── Agents/              # SOUL files for each specialist
│   ├── Agent Registry.md
│   ├── Brock-CEO-Soul.md
│   ├── Bob_Builder-Soul.md
│   └── ...
├── Skills/              # Custom skill files authored in Obsidian
│   └── ...
├── Chat History/        # Session archives
│   └── ...
└── AgentOS/             # Governance and deployment docs
    └── ...
```

## EC2 folder structure (runtime)

```
~/.hermes/
├── skills/              # Skills synced from Obsidian + bundled
├── profiles/            # Agent profiles with SOUL.md symlinks
│   └── <name>/
│       ├── SOUL.md      # Should symlink to Obsidian source
│       ├── .env         # Profile-local secrets
│       └── ...
├── sessions/            # What the agents actually did
├── config.yaml
└── .env
```

## Sync pipeline

**Obsidian → EC2 (source to runtime):**

```bash
# Sync agent SOUL files
rsync -av ~/Desktop/Obsidian/Agents/ ubuntu@<ec2-ip>:~/agents/

# Sync custom skills
rsync -av ~/Desktop/Obsidian/Skills/ ubuntu@<ec2-ip>:~/.hermes/skills/
```

After syncing skills or SOUL files, restart affected profile gateways:

```bash
hermes --profile <name> gateway restart
```

**EC2 → Obsidian (sessions back):**

```bash
# Export sessions weekly
ssh ubuntu@<ec2-ip> "hermes sessions export ~/backups/sessions-$(date +%Y%m%d).jsonl"
rsync ubuntu@<ec2-ip>:~/backups/ ~/Desktop/Obsidian/Chat\ History/
```

## Client governance deliverables

For each client deployment:

1. **Session log exports** (weekly automated)
2. **Git history of SOUL changes** (git-track the Obsidian Agents folder)
3. **Usage insights** (`hermes insights` on EC2)
4. **Agent registry** (list of active profiles, their models, and their Telegram bots)

## Model serving note

Open WebUI gives clients a ChatGPT-style interface at `http://<ec2-ip>:8080`. This is the visual proof that the private AI stack works. It connects to local Ollama on the same EC2 instance. No Hermes gateway needed for basic chat demo.

Hermes agents run separately through Telegram/Slack gateways for the full "private AI team" experience.

## Key pitfall

Do not edit SOUL files directly on the EC2. The Obsidian vault is the master copy. EC2 copies are runtime artifacts. If you edit on EC2 and forget to sync back, the source of truth drifts and the next deploy overwrites your changes.
