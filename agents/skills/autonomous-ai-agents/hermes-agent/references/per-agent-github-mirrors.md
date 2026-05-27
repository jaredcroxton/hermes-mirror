# Per-agent GitHub mirrors

Use this when Jared wants each specialist agent to back up its durable identity and custom workflow knowledge to separate GitHub repositories, while keeping Hermes runtime local.

## Recommended mode

Start with **mirror only**, not GitHub as source of truth.

Why:
- safer rollout
- lower risk of breaking live agents
- clean version history without forcing pull-based runtime changes
- easier to tighten what gets mirrored before automating more

## Repo pattern

One private repo per agent, for example:
- `agent-brock-ceo`
- `agent-bob-builder`
- `agent-harry-hr`
- `agent-lara-learningdesign`
- `agent-nelly-notebook`
- `agent-polly-performos`
- `agent-sam-studynerd`
- `agent-atticus-counsel`

Prefer private first. Some SOUL files and custom skills may contain commercially sensitive operating context.

## Mirror boundary

Mirror only the durable identity layer:
- `SOUL.md`
- agent-specific custom or locally modified skills
- short docs such as `docs/how-this-agent-works.md`
- a machine-readable manifest if useful

Do **not** mirror:
- `.env`
- sessions
- logs
- memories
- caches
- runtime DB/state files
- channel directories
- auth tokens or credential files

## Practical structure

Inside each repo:
- `README.md`
- `SOUL.md`
- `skills/`
- `docs/how-this-agent-works.md`
- `docs/mirror-manifest.json`
- `.gitignore`

## Sync model

Recommended flow:
1. Keep local Hermes profiles and Obsidian SOUL files as the working environment.
2. Create one repo per agent.
3. Compare profile-local skills against global skills and mirror only the agent-specific deltas.
4. Commit and push only when a change is detected.
5. Run the sync on a timer, ideally hourly or daily, as a silent script-only cron job.

## Good implementation pattern

Use a manifest that maps:
- agent id
- profile name
- repo name
- canonical SOUL file path
- profile-local skills root

Then run a sync script that:
- copies `SOUL.md`
- copies only custom skill files that differ from the global skill library
- rewrites helper docs inside the repo
- `git add .`
- commits only if `git status --short` is non-empty
- pushes to `main`

## Decision rule

If Jared asks whether to mirror the whole profile folder, the answer is no. Whole-profile mirroring pulls in runtime noise and raises secret-spill risk. Mirror the durable identity layer only.
