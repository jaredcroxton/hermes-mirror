# CREW to Hermes Agent — Complete Migration

Proven on a fresh Mac Mini (28 June 2026) with zero prior state.
93 gold-standard skills across 14 packs, fully installed and tested.

---

## The discovery

The CREW GitHub repo (`github.com/jaredcroxton/crew-skill-packs`) already uses Hermes-compatible directory structure. Each skill is `crew-<name>/SKILL.md`. No restructuring needed.

---

## Architecture — the end state

```
Brock (CEO Agent, orchestrator, Kanban owner)
  └── Routes work via Kanban cards to 14 pack agents

14 Pack Agents (profile-backed, each pre-loaded with their pack's skills):
  01-core          → crew-core-*          (8 skills)
  02-sales         → crew-sales-*         (7 skills)
  03-marketing     → crew-marketing-*     (7 skills)
  04-ops           → crew-ops-*           (5 skills)
  05-hr            → crew-hr-*            (5 skills)
  06-finance       → crew-finance-*       (6 skills)
  07-support       → crew-support-*       (6 skills)
  08-docs          → crew-docs-*          (7 skills)
  09-training      → crew-training-*      (8 skills)
  10-web-design    → crew-web-*           (9 skills)
  11-infrastructure→ crew-infra-*         (1 skill)
  12-design-standards→ crew-design-*      (7 skills)
  13-design-styles → crew-design-*        (5 skills)
  14-animation     → crew-animation-*     (12 skills)
```

Each pack agent has exactly its own pack's skills loaded in its profile skills directory. Delegation is locked. Pack agents receive work via Kanban cards from Brock.

---

## Phase 1: Quick install (all 93 as flat skills)

For rapid testing — install every CREW skill into the default Hermes profile:

```bash
# Clone and scaffold
git clone https://github.com/jaredcroxton/crew-skill-packs.git ~/crew-skill-packs
mkdir -p ~/.hermes/crew-state

# Install all 93 skills with path fix
for pack in ~/crew-skill-packs/packs/*/; do
    for skill_dir in "$pack"crew-*/; do
        [ -d "$skill_dir" ] || continue
        skill_name=$(basename "$skill_dir")
        cp -r "$skill_dir" ~/.hermes/skills/"$skill_name"
        sed -i '' 's|.claude/crew-state/|~/.hermes/crew-state/|g' \
          ~/.hermes/skills/"$skill_name"/SKILL.md
    done
done

# Verify
hermes skills list | grep -c 'crew-'
```

**Critical:** the glob is `crew-*/` (directories), NOT `crew-*.md` (files).

---

## Phase 2: Profile-backed pack agents (the real architecture)

The flat install gives one agent 93 reference documents. The profile-backed install gives 14 agents, each with domain-specific skills loaded as part of their identity. This is the target state.

### Step 1: Create all 14 profiles

```bash
hermes profile create pack-core --clone-from default
hermes profile create pack-sales --clone-from default
hermes profile create pack-marketing --clone-from default
hermes profile create pack-ops --clone-from default
hermes profile create pack-hr --clone-from default
hermes profile create pack-finance --clone-from default
hermes profile create pack-support --clone-from default
hermes profile create pack-docs --clone-from default
hermes profile create pack-training --clone-from default
hermes profile create pack-web-design --clone-from default
hermes profile create pack-infrastructure --clone-from default
hermes profile create pack-design-standards --clone-from default
hermes profile create pack-design-styles --clone-from default
hermes profile create pack-animation --clone-from default
```

### Step 2: Strip inherited credentials

Cloned profiles inherit Telegram, email, and cron from default. Strip it:

```bash
for profile in pack-core pack-sales pack-marketing pack-ops pack-hr \
  pack-finance pack-support pack-docs pack-training pack-web-design \
  pack-infrastructure pack-design-standards pack-design-styles pack-animation; do
    sed -i '' '/^TELEGRAM_/d' ~/.hermes/profiles/$profile/.env
    sed -i '' '/^EMAIL_/d' ~/.hermes/profiles/$profile/.env
    sed -i '' '/^GMAIL_/d' ~/.hermes/profiles/$profile/.env
    sed -i '' '/^SMTP_/d' ~/.hermes/profiles/$profile/.env
    rm -f ~/.hermes/profiles/$profile/cron/state.json
    echo "Cleaned $profile"
done
```

### Step 3: Install pack-specific skills per profile

Each profile gets only its own pack's skills:

```bash
declare -A PACK_MAP
PACK_MAP["01-core"]="pack-core"
PACK_MAP["02-sales"]="pack-sales"
PACK_MAP["03-marketing"]="pack-marketing"
PACK_MAP["04-ops"]="pack-ops"
PACK_MAP["05-hr"]="pack-hr"
PACK_MAP["06-finance"]="pack-finance"
PACK_MAP["07-support"]="pack-support"
PACK_MAP["08-docs"]="pack-docs"
PACK_MAP["09-training"]="pack-training"
PACK_MAP["10-web-design"]="pack-web-design"
PACK_MAP["11-infrastructure"]="pack-infrastructure"
PACK_MAP["12-design-standards"]="pack-design-standards"
PACK_MAP["13-design-styles"]="pack-design-styles"
PACK_MAP["14-animation"]="pack-animation"

for pack_dir in ~/crew-skill-packs/packs/*/; do
    pack_name=$(basename "$pack_dir")
    profile="${PACK_MAP[$pack_name]}"
    rm -rf ~/.hermes/profiles/$profile/skills/crew-*
    for skill_dir in "$pack_dir"crew-*/; do
        [ -d "$skill_dir" ] || continue
        skill_name=$(basename "$skill_dir")
        cp -r "$skill_dir" ~/.hermes/profiles/$profile/skills/"$skill_name"
        sed -i '' 's|.claude/crew-state/|~/.hermes/crew-state/|g' \
          ~/.hermes/profiles/$profile/skills/"$skill_name"/SKILL.md
    done
    echo "$pack_name -> $profile"
done
```

### Step 4: Lock delegation on all pack agents

Pack agents never spawn sub-agents directly. They go through Brock via Kanban:

```bash
for profile in pack-core pack-sales pack-marketing pack-ops pack-hr \
  pack-finance pack-support pack-docs pack-training pack-web-design \
  pack-infrastructure pack-design-standards pack-design-styles pack-animation; do
    sed -i '' 's/max_spawn_depth: [0-9]*/max_spawn_depth: 0/' \
      ~/.hermes/profiles/$profile/config.yaml
    sed -i '' 's/max_concurrent_children: [0-9]*/max_concurrent_children: 0/' \
      ~/.hermes/profiles/$profile/config.yaml
    echo "Locked $profile"
done
```

### Step 5: Write SOUL files

Each profile needs a SOUL.md defining its domain, skills, and operating rules.
Template and per-pack domain descriptions are in `references/crew-pack-agent-soul-templates.md`.

### Step 6: Create Brock orchestrator profile

```bash
hermes profile create brock --clone-from default
```

Brock's SOUL.md has the full 14-agent ecosystem map and Kanban orchestration rules.

---

## Brand context — shared across all profiles

`~/.hermes/crew-state/brand-context.md` is the single source of brand truth. Every pack agent reads it before producing any output. The path resolves correctly for all profiles on the same machine.

### Building brand context from multiple sources

When a business doesn't have a single brand document, pull from scattered sources.
Pattern proven for PerformOS (28 June 2026):

1. Scrape the website (performos.com.au)
2. Read Obsidian MARKDOWN (IDENTITY.md, VISUAL.md, COPY.md)
3. Read Desktop brand style files (01-brand-identity.md)
4. Read agent souls for product positioning (Polly_PerformOS.md)
5. Pull from memory for accumulated brand knowledge
6. Mark pre-launch gaps honestly — never fabricate customer data, churn rates, or pricing
7. Write the consolidated brand-context.md

Full recipe: `references/building-brand-context-from-multiple-sources.md`

### The 11 onboarding questions

When brand-context.md does not exist, ask the business these questions.
Never ask about colours, fonts, or visual design — that belongs to design skills (packs 12-14).

1. What do you do and why does it matter?
2. Who buys from you?
3. Why would a customer leave?
4. If your business was a person at a dinner party, how would they show up?
5. What do you always get right?
6. What are you trying to achieve?
7. Website and online presence?
8. What's unwritten?
9. Where do you let customers down?
10. Anything I must know?
11. What haven't I asked?

---

## Kanban — the cross-agent workflow engine

### The context loop, ported

Claude Code: `Read handoff → Do work → Write handoff`
Hermes Kanban: `Read card body (contains prior handoffs) → Do work → kanban_complete(summary, metadata)`

### Handoff format

```python
kanban_complete(
    summary="Built FAQ for PerformOS: 12 questions across 4 categories",
    metadata={
        "changed_files": ["~/Desktop/performos-faq.md"],
        "qa_passed": True,
        "gaps_flagged": ["pricing", "refund policy"],
        "next_action": "Route to pack-docs for help document"
    }
)
```

### Cross-pack chains

Support pack → Docs pack is the canonical test chain.
Pack-support builds FAQ → kanban_complete → dependent card for pack-docs auto-promotes → pack-docs reads parent metadata → builds help doc.

---

## The Step 0 gap

CREW skills on Claude Code auto-execute Step 0 when the skill is invoked.
On Hermes, skills are loaded as reference documents — the agent reads them as context but does not auto-execute their workflow.

**Fix:** Profile-backed pack agents. Each profile's SOUL tells the agent to always read brand-context and load relevant skills before working. The Kanban card body includes explicit instructions.

**Direct invocation workaround (testing only):**
```bash
hermes --profile pack-support chat -q \
  "Load crew-support-faq-builder. Read ~/.hermes/crew-state/brand-context.md. Build an FAQ." \
  --quiet
```

---

## Path resolution

| Element | Claude Code | Hermes |
|---|---|---|
| Brand context | `.claude/crew-state/brand-context.md` | `~/.hermes/crew-state/brand-context.md` |
| Skill handoffs | `.claude/crew-state/<pack>/<skill>-handoff.md` | `~/.hermes/crew-state/<pack>/<skill>-handoff.md` |
| Skills directory | `.claude/skills/` or plugin registry | `~/.hermes/skills/<name>/SKILL.md` |

---

## Verified — what has been proven

- [x] 93 skills installed on Hermes (flat install)
- [x] Path fix: `.claude/crew-state/` → `~/.hermes/crew-state/` (sed replacement)
- [x] Brand context loaded from `~/.hermes/crew-state/brand-context.md`
- [x] Handoff written to `~/.hermes/crew-state/core/crew-core-brand-context-handoff.md`
- [x] Full read → work → write loop confirmed
- [x] Brand context built from multiple sources (website + Obsidian + Desktop + memory)
- [x] Handover document written: `~/Desktop/crew-hermes-handover.md` (34KB)

## Not yet verified — next to test

- [ ] Profile-backed pack agents created (14 profiles)
- [ ] Pack-specific skills installed per profile
- [ ] Delegation locked on all pack agents
- [ ] Brock orchestrator profile created
- [ ] Kanban board initialised and dispatcher running
- [ ] First Kanban card completes (pack-core brand verification)
- [ ] Cross-pack Kanban chain completes (pack-support → pack-docs)

---

## Pitfalls discovered during Hermes migration

### Zsh inline comments in pasted scripts

`# comment` on its own line inside a pasted multi-line script produces `zsh: command not found: #` noise. Harmless but distracting. Strip inline comments before pasting or use `: 'comment'` instead.

### Glob pattern: directories, not files

CREW skills are `crew-*/` directories with `SKILL.md` inside. Using `crew-*.md` in a for loop matches nothing. Always use `crew-*/`.

### execute_code sandbox is on the local machine

When Brock runs `execute_code` to transform files, it executes on the MacBook Pro, not the Mac Mini. For remote machine operations, give the user the exact commands to paste.

### Brand context must exist before first skill run

If `~/.hermes/crew-state/brand-context.md` doesn't exist when a skill's Step 0 fires, the skill falls into onboarding mode. Pre-load brand context before installing skills.

### Step 0 does not auto-fire on Hermes

Skills loaded via `hermes -s` or `/skill` are reference documents. The agent reads them but does not execute their workflow unless explicitly asked. The profile-backed pack agent model is the fix — the SOUL encodes the workflow trigger.

### DeepSeek v4 Pro context saturation

If a pack agent with many skills loaded stops mid-workflow with no error, the model's context window is saturated. Reduce the number of skills loaded or simplify the prompt.
