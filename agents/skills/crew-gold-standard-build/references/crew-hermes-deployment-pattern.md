# CREW on Hermes — Deployment Pattern

Proven on Mac Mini fresh install, 28 June 2026. 93 skills across 14 packs, deployed to Hermes Agent with profile-backed pack agents and Kanban orchestration.

## Prerequisites

- Hermes Agent installed (`curl -fsSL https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh | bash`)
- CREW repo cloned: `git clone https://github.com/jaredcroxton/crew-skill-packs.git ~/crew-skill-packs`
- Brand context file at `~/.hermes/crew-state/brand-context.md` (11-question onboarding output)
- Obsidian installed (for SOUL source of truth)

## Phase 1: Install skills with path fix

CREW skills on GitHub use the Hermes directory format (`crew-<name>/SKILL.md`). Each SKILL.md references `.claude/crew-state/` paths. Fix with sed during copy:

```bash
for pack in ~/crew-skill-packs/packs/*/; do
    for skill_dir in "$pack"crew-*/; do
        [ -d "$skill_dir" ] || continue
        skill_name=$(basename "$skill_dir")
        cp -r "$skill_dir" ~/.hermes/skills/"$skill_name"
        sed -i '' 's|.claude/crew-state/|~/.hermes/crew-state/|g' ~/.hermes/skills/"$skill_name"/SKILL.md
    done
done
```

Verify: `hermes skills list | grep crew- | wc -l` — expect 93.

## Phase 2: Brand context file

The brand-context.md is the single shared file every CREW skill reads in Step 0. It lives at `~/.hermes/crew-state/brand-context.md`. If it doesn't exist, skills route to crew-core-brand-context for the 11-question onboarding.

Build it from Obsidian source files:
- `~/Desktop/Obsidian/PerformOS/MARKDOWN/PerformOS/IDENTITY.md`
- `~/Desktop/Obsidian/PerformOS/MARKDOWN/PerformOS/VISUAL.md`
- `~/Desktop/Obsidian/PerformOS/MARKDOWN/PerformOS/COPY.md`
- Product-specific MARKDOWN files for instruments

Include colour system as reference-only (not presented during onboarding).

## Phase 3: Profile-backed pack agents

Each of the 14 packs becomes a Hermes profile. Create fresh (not cloned from default, to avoid credential inheritance):

```bash
for profile in pack-core pack-sales pack-marketing pack-ops pack-hr pack-finance pack-support pack-docs pack-training pack-web-design pack-infrastructure pack-design-standards pack-design-styles pack-animation; do
    hermes profile create "$profile" --no-skills --description "CREW $(echo $profile | sed 's/pack-//') specialist"
done
```

Pitfall: `--no-skills` conflicts with `--clone-from`. Create fresh profiles, then copy skills in.

Strip inherited credentials:
```bash
for profile in pack-*; do
    sed -i '' '/^TELEGRAM_BOT_TOKEN=/d' ~/.hermes/profiles/$profile/.env
    sed -i '' '/^EMAIL_/d' ~/.hermes/profiles/$profile/.env
    sed -i '' '/^SMTP_/d' ~/.hermes/profiles/$profile/.env
    rm -f ~/.hermes/profiles/$profile/cron/state.json
done
```

Install pack-specific skills (each profile gets only its pack's skills):
```bash
declare -A PACK_MAP
PACK_MAP["01-core"]="pack-core"
# ... (full mapping)

for pack_dir in ~/crew-skill-packs/packs/*/; do
    pack_name=$(basename "$pack_dir")
    profile="${PACK_MAP[$pack_name]}"
    rm -rf ~/.hermes/profiles/$profile/skills/crew-*
    for skill_dir in "$pack_dir"crew-*/; do
        [ -d "$skill_dir" ] || continue
        skill_name=$(basename "$skill_dir")
        cp -r "$skill_dir" ~/.hermes/profiles/$profile/skills/"$skill_name"
        sed -i '' 's|.claude/crew-state/|~/.hermes/crew-state/|g' ~/.hermes/profiles/$profile/skills/"$skill_name"/SKILL.md
    done
done
```

Lock delegation on all pack agents:
```bash
for profile in pack-*; do
    sed -i '' 's/max_spawn_depth: [0-9]*/max_spawn_depth: 0/' ~/.hermes/profiles/$profile/config.yaml
    sed -i '' 's/max_concurrent_children: [0-9]*/max_concurrent_children: 0/' ~/.hermes/profiles/$profile/config.yaml
done
```

## Phase 4: SOUL files in Obsidian

Obsidian is the canonical source of truth. Write every SOUL to `~/Desktop/Obsidian/Agents/` first, then symlink profiles.

Each SOUL must include a Kanban routing block:
```markdown
## Kanban operating rules

- I receive work via Kanban cards assigned to my profile.
- I read the full card body before loading any skills.
- I always read `~/.hermes/crew-state/brand-context.md` before producing output.
- When I finish: `kanban_complete(summary=..., metadata={changed_files, checks_run, risks, next_action})`.
- If I need another pack agent: I `kanban_comment` and escalate to Brock. I NEVER create cross-agent child tasks.
- If I hit a genuine blocker: `kanban_block(reason=...)`.
- Only Brock and Jared create cross-agent workflows.
```

Create an Agent Registry at `~/Desktop/Obsidian/Agents/Agent Registry.md` — a markdown table of all 15 agents (14 pack agents + Brock) with their profiles, pack numbers, skill counts, and Kanban assignee names.

Symlink profiles to Obsidian:
```bash
rm -f ~/.hermes/profiles/$profile/SOUL.md
ln -s ~/Desktop/Obsidian/Agents/$obsidian_name ~/.hermes/profiles/$profile/SOUL.md
```

## Phase 5: Brock orchestrator profile

Create Brock as a separate profile:
```bash
hermes profile create brock --no-skills
```

Brock's SOUL includes:
- Full ecosystem map (all 14 pack agents with domains and skill counts)
- Kanban routing rules (Brock is the only profile that creates cross-agent cards)
- Review protocol (only review outputs affecting people, money, reputation, executive alignment, or Jared's time)

Brock gets all 93 skills for reference (not isolation-locked like pack agents).

## Phase 6: Kanban board

```bash
hermes kanban init
```

Kanban dispatcher runs inside the gateway. Brock's gateway must be running:
```bash
hermes --profile brock gateway install
hermes --profile brock gateway start
```

### Cross-pack chain pattern

```
pack-core (brand verify) → pack-support (FAQ builder) → pack-docs (help doc)
```

Parent-child dependency links auto-promote cards `todo → ready` when parents complete. Pack agents hand off via `kanban_complete(summary, metadata)` — the Kanban card IS the handoff, replacing the file-based context loop from Claude Code.

## Proven pitfalls

1. **Step 0 does not auto-fire on Hermes.** Claude Code skills auto-execute Step 0 when invoked. Hermes loads skills as reference documents. Fix: profile SOULs instruct the agent to always read brand-context and load skills before working.

2. **`--no-skills` conflicts with `--clone-from`.** Create fresh profiles, then copy skills in separately.

3. **execute_code 300s timeout on large loops.** Use bash `for` loops directly in terminal for bulk operations.

4. **Gateway cannot be started from within a gateway TUI session.** Use a separate terminal.

5. **Pack agents must never route sideways.** Delegation locking (`max_spawn_depth: 0`) is essential. Only Brock creates cross-agent Kanban cards.

6. **Brand context path must be absolute.** `~/.hermes/crew-state/brand-context.md` — all profiles resolve `~` to the same home directory.

7. **DeepSeek v4 Pro context saturation.** If a pack agent with many skills loaded stops mid-workflow with no error, reduce skills loaded or simplify the prompt.

## Verification checklist

- [ ] All 14 pack profiles exist: `hermes profile list | grep pack-`
- [ ] Each profile has only its pack's skills
- [ ] Delegation locked on all pack agents
- [ ] Brock profile exists with full ecosystem SOUL
- [ ] Brand context at `~/.hermes/crew-state/brand-context.md`
- [ ] All SOUL files in Obsidian, symlinked to profiles
- [ ] Agent Registry exists in Obsidian
- [ ] Kanban board initialised
- [ ] Brock gateway running
- [ ] Cross-pack Kanban chain completes end to end

## What a successful end-to-end test looks like

User message to Brock on Telegram:
> Build me a PerformOS sales deck. 5 slides. Use brand colours. Make it move.

Brock creates three dependent Kanban cards:
1. `pack-core` — verify brand context loaded
2. `pack-web-design` — build slide deck HTML (parent: card 1)
3. `pack-design-standards` — design review gate (parent: card 2)
4. `pack-animation` — motion injection (parent: card 3)

Output: a single branded, animated HTML file with correct colours, typography, logo, navigation, transitions, and responsive breakpoints.
