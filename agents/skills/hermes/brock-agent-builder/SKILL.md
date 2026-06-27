---
name: brock-agent-builder
description: Use when Jared asks to "build an agent", "create a new agent", "make me a [role] agent", "design a soul for...", "I need an agent that...", or describes new agent functionality. Covers both Claude Code task agents (frontmatter + system prompt) AND PerformOS specialist souls (identity, brand, voice, domain knowledge). Brock executes the full design — qualified question, format decision, comprehensive soul or agent file, and handoff to deployment.
tags: [agents, souls, profiles, design, deployment]
---

# Brock Agent Builder — World-Class Agent Design

## Trigger

Use when Jared asks to create any kind of agent. This includes:
- "Build me an agent for..."
- "Create a new specialist agent..."
- "Make me a soul for..."
- "I need an agent that does X"
- "Design a [role] agent"
- "Add a sub-agent to [ecosystem]"

## The one qualifying question

Before building, ask exactly one question:

**"Is this a one-shot task agent (does a job and exits) or a persistent specialist (has ongoing conversations, domain knowledge, and brand context)?"**

This single question determines the format, depth, and destination.

## Format decision

### Format A: Task Agent (Claude Code style)
For one-shot workers that spin up, do one job, and exit.

**Destination:** Claude Code plugin `agents/` directory or Hermes skills directory
**Format:** YAML frontmatter + system prompt
**Lifespan:** Stateless, no memory, no persistence

**When to use:**
- Code reviewers, test generators, API validators
- One-shot builders that produce a file and return
- Pipeline steps that feed into another agent

### Format B: Specialist Soul (PerformOS / Hermes style)
For persistent agents with domain expertise, brand voice, and ongoing conversations.

**Destination:** `/Users/jc/Desktop/Obsidian/Agents/[agent]-soul.md`
**Format:** Identity-driven soul document with brand context
**Lifespan:** Persistent, memory-aware, cross-session

**When to use:**
- Product specialists (OnboardOS, AgentOS, Pocket Customer, etc.)
- CEO advisors and strategic thinking partners
- Domain experts (HR legislation, learning design, SEO)
- Any agent that represents a product, role, or sustained capability

## Format A: Task Agent Design Process

### Step 1: Extract intent
Identify the core purpose from Jared's description. What single job does this agent do?

### Step 2: Name the agent
Lowercase, hyphens, 3-50 characters. Descriptive. Never generic.

**Good:** `code-reviewer`, `test-generator`, `dashboard-builder`
**Bad:** `helper`, `agent`, `tool`

### Step 3: Write the frontmatter
```yaml
---
name: agent-name
description: Use this agent when [triggering conditions]. Typical triggers include [scenario 1], [scenario 2], and [scenario 3]. See "When to invoke" in the agent body for worked scenarios.
model: inherit
color: [blue|cyan|green|yellow|magenta|red]
tools: ["Tool1", "Tool2"]  # Least privilege — only what it needs
---
```

**Color rules:**
- Blue/cyan: Analysis, review, research
- Green: Creation, generation, building
- Yellow: Validation, caution, checking
- Red: Security, critical, dangerous operations
- Magenta: Creative, transformation, design

**Tool rules:**
- Read-only analysis: `["Read", "Grep", "Glob"]`
- Code generation: `["Read", "Write", "Grep"]`
- Testing: `["Read", "Bash", "Grep"]`
- Full access: Omit the field entirely (never use `["*"]`)

### Step 4: Write the system prompt
Standard structure — every task agent follows this:

```
You are [role] specializing in [domain].

## When to invoke

- **[Scenario A].** [What the situation looks like and what the agent should do.]
- **[Scenario B].** [Same.]
- **[Scenario C].** [Same.]

**Your Core Responsibilities:**
1. [Primary]
2. [Secondary]
3. [Additional...]

**Process:**
1. [Step one — what to do first]
2. [Step two]
3. [Step three]

**Quality Standards:**
- [Standard 1]
- [Standard 2]

**Output Format:**
[Exact format specification]

**Edge Cases:**
- [Edge case 1]: [How to handle]
- [Edge case 2]: [How to handle]
```

### Step 5: Save and verify
Save as `agents/[agent-name].md` in the relevant Claude Code plugin directory.
Verify: identifier follows naming rules, description has trigger scenarios, system prompt is 500-3,000 words, model choice is appropriate, tools follow least privilege.

---

## Format B: Specialist Soul Design Process

This is the format used for PerformOS product agents (OnboardOS, AgentOS, Pocket Customer, PulseCheck360, Performolytics, LearnOS) and any persistent domain specialist.

### Step 1: Name the agent
Descriptive, memorable. PerformOS products use their brand name. Role-based agents use [Name]_[Role] (e.g., Polly_PerformOS, Harry_HR).

### Step 2: Source context
Before designing the soul, pull context from:
1. **Obsidian vault:** `/Users/jc/Desktop/Obsidian/PerformOS/MARKDOWN/[Product]/IDENTITY.md`, `VISUAL.md`, `COPY.md`
2. **Full context file:** `/Users/jc/Desktop/Obsidian/PerformOS/Performos-Full-Context.md`
3. **User memory:** System prompt memory for Jared's preferences, ecosystem, constraints
4. **Session history:** `session_search` for recent discussions about this product/topic
5. **Existing agent souls:** `/Users/jc/Desktop/Obsidian/Agents/` for sibling agents to align with
6. **Skills:** Relevant Hermes skills that inform the domain

### Step 3: Design the soul — required sections

Every specialist soul must include these sections. Order matters:

#### 1. Identity (H2)
Who the agent is. First-person. Two to three sentences.

```
## Identity

**[Agent Name]** is the specialist [role] for [domain]. I know [key knowledge areas] inside out. I report to [orchestrator].
```

#### 2. What I am (H2)
Expanded role description. What the agent can answer. What it specialises in.

```
## What I am

I am the expert on [domain]. I can answer any question about [specific areas]. I [key capability statement].
```

#### 3. The product/domain I represent (H2)
For product agents: detailed product facts. For role agents: domain boundaries.

Must include:
- Product name, category, tagline
- Current status (Live / Paused / Build in progress / Planned)
- Target audience
- Key differentiators

#### 4. Visual identity (H2, product agents only)
Colour palette table with token names, hex codes, and use descriptions.
Typography choices if relevant.
Dark/light canvas preference.

#### 5. Voice and tone (H2)
3-5 voice principles. How the agent speaks. What it never sounds like.

#### 6. Technical architecture (H2, if applicable)
Routes, files, database tables, APIs. Real code references, not invented ones.

#### 7. Competitive positioning (H2, if applicable)
Comparison table vs alternatives. What makes this product different.

#### 8. Relationship to ecosystem (H2)
Where this agent fits. Who it reports to. Sibling agents and how they relate.

#### 9. Guardrails — "What I must never say" (H2)
Hard lines. Legal boundaries. Brand rules. Things the agent must refuse.

#### 10. What I can help with (H2)
Bullet list of specific question types and tasks the agent handles.

#### 11. Operating principle (H2)
One sentence. How the agent routes or escalates.

### Step 4: Quality gates — check every soul against these

Before saving, verify:

**Structure:**
- [ ] Identity section is first-person ("I am...")
- [ ] At least 8 of the 11 recommended sections present
- [ ] No section is placeholder or "TODO"
- [ ] Product status is explicitly stated (Live/Paused/Build in progress/Planned)

**Accuracy:**
- [ ] All hex codes are real 6-digit values, not guesses
- [ ] File paths reference actual files in the repo, not invented ones
- [ ] Product facts match the full context file, not memory
- [ ] Competitor names and prices are sourced, not estimated

**Voice:**
- [ ] Voice principles section exists and has 3-5 specific rules
- [ ] "Never say" section lists actual forbidden phrases, not generic advice
- [ ] Tagline and positioning language match the brand MARKDOWN files

**Ecosystem:**
- [ ] States who the agent reports to (Polly, Brock, etc.)
- [ ] Lists sibling agents and how they relate
- [ ] Includes routing/escalation rule

**Safety:**
- [ ] No invented legal claims
- [ ] No guarantee of outcomes or results
- [ ] No disparaging named competitors
- [ ] No "Sarah" anywhere in the document

### Step 5: Save and handoff

Save to: `/Users/jc/Desktop/Obsidian/Agents/[agent-name]-soul.md`

If the agent reports to an orchestrator (Polly, Brock), offer to update the orchestrator's soul to add the sub-agent to their ecosystem section.

Then handoff with a summary:
- Agent name and purpose
- Format (task agent or specialist soul)
- File path
- Key design decisions
- Suggested next step (deploy, test, or integrate)

---

## Decision-gated build briefs

When Jared provides a build brief that contains explicit open decisions, do not treat the default recommendation as permission to build. Ask the open decisions one at a time before writing any SOUL files, playbooks, setup prompts, profile configs, or startup files.

Use this sequence:
1. Pressure-test the architecture briefly and name the recommendation.
2. Ask the first open decision only.
3. Continue one decision at a time until every decision that changes the file content is resolved.
4. Only then write the files.
5. If tool approval blocks the write, report that nothing was written. Do not imply the build landed.

This applies especially to orchestrator-plus-playbook agents, sub-agent vs playbook decisions, optional specialist domains, naming, and overlap with existing agents.

### Design QA task agent under Bob

When Jared asks whether Bob needs a design or themes sub-agent, recommend a **Claude Code style task agent**, not a persistent chat specialist, unless Jared explicitly wants an independently addressable creative specialist.

Default pattern:
- Bob_Builder owns implementation.
- The design QA task agent owns the visual standard.
- Brock reviews only when the artifact affects people, money, reputation, executive alignment, or Jared's time.

The design QA task agent should be a reviewer with teeth, not a second builder. It should return: pass, pass with minor fixes, or fail with required fixes. Bob then implements the fixes.

Suggested role name: `premium-dashboard-design-reviewer`.

Trigger: after Bob builds any HTML dashboard, lead dashboard, landing page, deck, or client-facing interface.

Quality gate:
1. Bob builds.
2. Bob opens in Chrome.
3. Design QA reviews screenshot, DOM, console, brand fit, motion, and task-specific checklist.
4. Bob fixes any failures.
5. Design QA passes.
6. Only then is the artifact returned to Jared.

## Premium design QA gate

When creating or updating build agents for Bob, keep design QA as a reviewer gate, not a competing builder. See `references/premium-design-qa-gate.md` for the pattern. Use this especially when the output is an HTML dashboard, landing page, lead dashboard, deck, or client-facing interface.

## Cross-agent orchestration (for specialist souls)

When building a specialist that reports to an orchestrator:

1. **Design the soul first** — let the specialist's identity stand alone
2. **Then update the orchestrator** — add the specialist to the sub-agent table in the orchestrator's soul
3. **Define routing rules** — when does the orchestrator handle a question vs route to the specialist?
4. **Set the escalation path** — what does the specialist do when it needs something outside its domain?

### Leadership-agent design pattern

When Jared asks for a leadership, executive judgement, difficult-conversation, manager-coaching, or team-dynamics agent, do not produce a generic advice bot or a single script generator. Jared expects the agent to take rich team context, apply source-backed leadership lenses, and return multiple strategic stances before recommending one.

Use `references/leadership-agent-research-pattern.md` as the research and output pattern. The leadership specialist should diagnose the situation, present three to five strategic angles, recommend a stance, give exact language, name what not to say, and identify follow-up risk.

Key pitfall: do not over-index on authority. Authority is one lens, not the answer. Pair clarity with curiosity, psychological safety, influence, and accountability. Treat resistance as data before treating it as defiance.

### Playbook-backed orchestrator option

Before creating multiple new specialist agents or Telegram bots, test whether Jared actually needs separately addressable specialists. If the answer is no, build one persistent orchestrator plus markdown playbooks under its agent folder. This keeps one front door, reduces gateway/profile overhead, and still gives specialist-quality output.

Use this for prompt operations, research domains, content systems, and other expert stacks where the sub-specialists are knowledge modules rather than independent actors. See `references/playbook-backed-orchestrators.md` for the file set, gates, and Piper_PromptOps example.

Example from Polly's ecosystem:
```
Polly (PerformOS — product orchestrator)
├── OnboardOS — $499 AI course (Planned)
├── AgentOS — Private AI team (Product dev)
├── Pocket Customer — AI roleplay coach (Live)
├── PulseCheck360 — Flight-risk detection (Paused)
├── Performolytics — AI business intelligence (Build in progress)
└── LearnOS — Custom LMS (Live)
```

## Integration with deployment

After designing a specialist soul, Brock usually does NOT deploy it. The default deployment path is:
1. Brock designs the soul → saves to Obsidian
2. Jared reviews and approves
3. Bob_Builder deploys using the `specialist-agent-deployment` skill

Exception: if Jared explicitly asks Brock to complete, run, wire, or verify the agent, Brock may execute the deployment steps directly rather than hand off. In that case, treat deployment as unfinished until the profile is wired, gateway status is verified, and a real identity probe path is ready for Jared.

### Crew and AgentOS dual-runtime pattern

When Jared is discussing gstack, Crew, AgentOS, or whether Claude Code and Hermes/NemoClaw need separate agents, use the **same souls, two runtimes** model. Do not create duplicate agents with different names just because the runtime changes. Crew runs the canonical souls in Claude Code for speed. AgentOS runs the same canonical souls in Hermes + NemoClaw/OpenShell for security, audit, token masking, and sandbox policy.

Use `references/crew-agentos-dual-runtime-pattern.md` for the full product distinction, reporting line, gstack-inspired phase roles, and the four missing souls: Finn, Quinn, Trace, and Pace.

When Claude Code returns a build plan for a new Crew skill pack, use the 7-Gate Review Framework in `references/crew-skill-review-framework.md` before approving any construction. Every gate must pass before skills are written.

### Delegation locking for specialists

When a specialist agent must never spawn sub-agents or route work to Bob/Lara/Harry/etc., lock delegation permanently in `config.yaml`:

```yaml
delegation:
  max_spawn_depth: 0
  max_concurrent_children: 0
  orchestrator_enabled: false
```

This prevents `delegate_task` entirely. Apply this during deployment for any specialist that is knowledge-only, a thinking partner, or a domain expert with no build/execution responsibilities. Neo_NemoClaw uses this pattern — he owns the NemoClaw knowledge domain but must never route work to Bob or other builders.

### Model injection on clone

When cloning from `default` profile, the new specialist inherits the default model. Change it to the specialist's intended model before gateway start:

```bash
hermes --profile <profile> config set model.default "nvidia/nemotron-3-super-120b-a12b"
hermes --profile <profile> config set model.provider "nvidia"
hermes --profile <profile> config set model.base_url "https://integrate.api.nvidia.com/v1"
```

Then copy the provider's API key into the profile-local `.env`. Verify with a direct probe:

```bash
hermes --profile <profile> chat -q "What model are you running on? One sentence." --quiet
```

### Inherited credential stripping on clone

When cloning from `default`, the new profile inherits email config, cron jobs, and platform credentials the specialist should not have. Strip immediately after clone:

```bash
sed -i '' '/^SMTP_/d' ~/.hermes/profiles/<profile>/.env
sed -i '' '/^GMAIL_/d' ~/.hermes/profiles/<profile>/.env
sed -i '' '/^EMAIL_/d' ~/.hermes/profiles/<profile>/.env
```

Only the platforms the specialist actually needs (e.g., Telegram for a messaging agent) should remain.

### Cron-driven knowledge refresh for specialists

For specialists that need to stay current on external knowledge sources (NVIDIA docs, GitHub releases, YouTube channels), set a daily cron job that refreshes their domain knowledge and saves updates to memory:

```bash
hermes --profile <profile> cron add "daily-kb-refresh" \
  --schedule "0 8 * * *" \
  --prompt "Check [source URLs] for any updates related to [domain]. If there is new information, summarize it and save to memory. If nothing new, reply 'no changes' and exit."
```

This keeps the specialist's knowledge current without manual intervention. Neo_NemoClaw uses this pattern to monitor NVIDIA's developer page, docs.nvidia.com, and YouTube for NemoClaw/Hermes updates.

### Brock-routed leadership specialists

When Jared creates a leadership strategy specialist to sit behind Brock, use the pattern in `references/brock-routed-leadership-agent.md`.

Key rules:
- Verify the actual canonical Brock soul path before editing. Jared may name a shorthand path that does not exist.
- Verify whether supplied or referenced specialist files actually exist. If the user says "still to create: nothing" but the files are absent, create them at the requested paths and report that correction plainly.
- Check for naming collisions before activation. For example, `Leo_Leads` and `Leo_Leadership` are different lanes.
- Update both the orchestrator soul and the relevant startup maps, then verify the inserted text and file paths before saying the agent is active.
- Start Brock-routed when the agent handles high-stakes leadership judgement. Direct Telegram bot can come later after the pattern proves useful.

For Telegram specialist bots, follow `references/specialist-telegram-deployment-hygiene.md`: store the token in the target profile only, set allowlists, verify `getMe`, remove inherited platform credentials like email unless explicitly wanted, restart the gateway, and verify the expected platform count before saying the bot is live.

For NemoClaw/Hermes specialists or NVIDIA sandbox setup agents, follow `references/nemoclaw-specialist-and-onboarding.md`: keep the specialist Jared-only by default, lock delegation if it should never route to Bob or other agents, use Nemotron option 1 for NVIDIA Endpoint sandboxes, press `1` to enable Telegram during onboarding, and use Balanced policy for functional demos unless intentionally stress-testing Restricted.

For task agents (Format A), Brock saves the agent file and the user deploys it in their Claude Code plugin.

## Design principles (Brock's signature)

1. **Context before design.** Pull from Obsidian, memory, and session history before writing a single line.
2. **Real facts only.** Never invent hex codes, file paths, table names, or competitor prices.
3. **Identity first.** The agent's voice and persona are as important as its functional capabilities.
4. **Guardrails are features.** "Never say" sections protect the product more than capability lists.
5. **Status is sacred.** Every product agent must declare Live / Paused / Build in progress / Planned explicitly.
6. **Orchestration is design.** How agents route to each other is part of the design, not an afterthought.

## Pitfalls

- **Wrong format for the job.** Do not design a full specialist soul for a one-shot code reviewer. Do not write a bare system prompt for a product agent that needs brand context.
- **Inventing product details.** If the context file and brand MARKDOWN don't specify something, do not guess. Note the gap explicitly.
- **Skipping the orchestrator update.** If the new agent reports to Polly or another orchestrator, the orchestrator's soul must be updated. Do not consider the job done without this step.
- **Generic voice sections.** "Be helpful and professional" is not voice design. Specific voice principles with actual language examples are.
- **Forgetting the status.** Product agents that don't declare their status create confusion. Live? Paused? Planned? Say it.
- **Brain without hands.** A raw model behind a chat UI (Ollama + system prompt + web page) is NOT an agent. It can only talk about doing things — it produces ChatGPT-style non-answers ("Here is how you could...") instead of executing. A real agent has tools (terminal, browser, files, web) and a runtime that dispatches them. The AP agent on EC2 was phi4:14b behind a Python HTTP proxy with no Hermes runtime — it explained what to do but could not do anything. When someone asks why their agent cannot act, the diagnostic is: model alone = chatbot; model + runtime + tools = agent. A Hermes agent is the latter.
- **Testing without reading the skill.** When Jared asks for a test prompt, do not assume what inputs the skill needs. Read the skill file first — check the Inputs section, the Workflow steps, the source material it expects. Giving pre-written answers when the skill is designed to source questions from raw tickets is the wrong test. The FAQ Builder sources questions from ticket dumps, not from a list you provide. Read the skill, then design the test.
- **White-label leaking.** When building business skills that will be sold or given to clients, never embed a specific business's context (brand name, contact details, domain, product names, internal workflows) into the skill body. G-Stack skills are portable across any software project — they never mention a specific company. Crew skills must be equally portable. If you are building a skill while thinking about a specific client (e.g., "Accor Plus review replies"), the client context WILL leak into examples, guardrails, and output blocks. After authoring, grep the skill for any business-specific noun and replace it with a generic placeholder (`[business name]`, `[contact email]`, `[industry]`). White-label is a verification step, not an intention. The QA ban-list in the install package enforces this, but the author is the first line of defence.
- **Racing ahead without confirmation.** CEO-level agents (Brock class) must state their intended action before executing. Analysis → state the plan → wait for confirmation → then act. Jumping from diagnosis to execution in one turn erodes trust. See `references/brock-interaction-protocol.md` for the full operating pattern. This was explicit feedback from Jared on 26 June 2026.
- **Context Loop is mandatory, not optional.** Every Crew skill must include Step 0 (Context Recovery: read the prior handoff file or state "No prior context, first run") and a Final Step (Handoff Save: write output, decisions, unfinished work, and next-skill needs to the handoff file). This is what makes the Crew a system that remembers across sessions rather than a folder of stateless prompts. The handoff path is `.claude/crew-state/<pack>/<skill>-handoff.md`. Always write it, even when the run produced no output. This is not an optional State section — it is a mandatory Step 0 and Final Step in every Workflow.
- **Desktop file delivery to Claude Code is unreliable.** When Hermes/Brock writes a markdown brief to `~/Desktop/` for Claude Code to read, the file often does not land — Claude Code reports the file unreadable despite Hermes confirming it is on disk. The root cause is unclear (possible iCloud sync interference, sandbox boundary, or file handle release), but the pattern is consistent across multiple sessions. The fix: when Brock needs to give Claude Code a build brief, paste it directly into the chat (most reliable) or save it into the project directory where `.claude/skills/` lives (Claude Code reads from its own project directory reliably). Never rely on Desktop as the handoff point between Hermes and Claude Code. Jared's words: "I'm happy for you just to post the markdown file in here so I can just copy and transfer it, because every time this is happening." Follow that instruction.
- **Fresh-install routing failure.** When a business clones the Crew repo and invokes a skill directly without installing plugins, Step 0 routes to `crew-core-brand-context` but Claude Code has no plugin registry. The skill fails during onboarding. Fix: inline fallback in Step 0, or scaffold blank brand-context.md in install script, or require plugins as prerequisite. See `references/crew-fresh-install-routing-gap.md`.
- **README brand identification leaks into Claude context.** Claude Code reads repo README and CLAUDE.md into every session. Any brand name in these files (\"Built by PerformOS,\" founder name) leaks into the user's context before any skill loads. The skill's Step 0 cannot prevent what Claude already knows. Fix: repo README must contain zero brand identification. Brand story lives in ABOUT.md (Claude does not auto-load it). A business downloads the repo; the repo must not assume who they are. See `references/crew-readme-brand-leak.md`.
- **Build skills reference animation but don't inject it.** The design review gate cross-references `crew-animation-gsap` and `crew-animation-motion`, confirming animation quality standards are met. But the HTML output template never generates a `<script>` block with actual animation code. Result: beautiful static pages with no motion. Fix: add animation injection step to build skill Workflows. Not a gate reference — a code generation step.
- **Worked example is the most error-prone artifact.** Across 93 skill upgrades, every adversarial review catches the worked example violating the skill's own rules. The canonical example that a builder copies is consistently the place where guardrails break. Before considering a skill complete, read the worked example and ask: \"Does this example violate any of the skill's own rules?\" If yes, fix the example, then fix the fixture to assert the corrected behavior. See `references/crew-adversarial-review-meta-finding.md` for the full pattern.
- **Lead dashboards must match the Accor Plus depth standard.** When building or reviewing a `crew-web-lead-dashboard-builder` skill, the bar is the Accor Plus Outreach Dashboard (https://accor-plus-leads-dashboard.vercel.app/). A passing dashboard must include: fit scoring (0-100 with sub-scores, hot leads flagged at 90+), LinkedIn research running by default with named decision-makers (never a permission gate), derived emails with "verify before send" warnings, personalised insights per lead that name the specific mechanism not the category, LinkedIn DMs drafted alongside cold emails, filter controls (region, quality, outreach status), a metrics row, staff size estimates, evidence tags on every field (Confirmed/Inferred/Derived/Escalated), and a calendar question after the build (ask, never auto-create). Confirmation gates belong downstream — email drafts and calendar blocks need human approval before action, but research and drafting run automatically. Thin cards with "LinkedIn research not enabled" on every row or generic insights fail the standard. This standard was proven end to end in a live V2 rebuild on 17 June 2026 (8 Sunshine Coast leads, all 8 additions live, design review pass). See `references/lead-dashboard-depth-standard.md` for the full specification.
- **Brand-context discovery must stay business, not design.** When designing onboarding questions for a business brand-context file, ask about who they are (what they do, who buys, why they leave, dinner-party voice, what they get right, goals, online presence, unwritten rules, where they let down, must-know). Do NOT ask about colours, fonts, visual style, or imagery. Design discovery belongs in the design skills' own pre-build flow. A florist should finish onboarding without ever thinking about hex codes. The 11 practical questions replaced a 12-question set that leaked design vocabulary into business onboarding. This split is load-bearing: design packs 12-14 read from the website and their own discovery, not from brand-context.md. See `references/crew-brand-context-11-questions.md` for the canonical set. When building or reviewing a `crew-web-lead-dashboard-builder` skill, the bar is the Accor Plus Outreach Dashboard (https://accor-plus-leads-dashboard.vercel.app/). A passing dashboard must include: fit scoring (0-100 with sub-scores, hot leads flagged at 90+), LinkedIn research running by default with named decision-makers (never a permission gate), derived emails with "verify before send" warnings, personalised insights per lead that name the specific mechanism not the category, LinkedIn DMs drafted alongside cold emails, filter controls (region, quality, outreach status), a metrics row, staff size estimates, evidence tags on every field (Confirmed/Inferred/Derived/Escalated), and a calendar question after the build (ask, never auto-create). Confirmation gates belong downstream — email drafts and calendar blocks need human approval before action, but research and drafting run automatically. Thin cards with "LinkedIn research not enabled" on every row or generic insights fail the standard. This standard was proven end to end in a live V2 rebuild on 17 June 2026 (8 Sunshine Coast leads, all 8 additions live, design review pass). See `references/lead-dashboard-depth-standard.md` for the full specification.

## Voice design reference: Anthropic system prompt patterns

When designing agent voice, conciseness rules, refusal protocols, or task-management discipline, reference `references/anthropic-system-prompt-patterns.md` — distilled from Claude Code 2.0 and Claude Sonnet 4.6 leaked prompts (June 2026). Covers: embedded conciseness examples, banned preambles, refusal protocol (1-2 sentences, no reasons), anti-sycophancy stance, single-task discipline, file-creation bias, temporal persona framing, and search query rules.

## Version

Locked 02 June 2026. Updated 28 June 2026 with Anthropic prompt patterns reference. Synthesised from Claude Code agent-creator, agent-development, Hermes specialist-agent-deployment, and the six PerformOS souls built earlier this session.

## Reference files

- `references/crew-skill-upgrade-prompt-format.md` — CREW skill upgrade prompt template (93 skills battle-tested). Task header, source + benchmark, promote candidates, standard sections.
- `references/token-limit-handoff-pattern.md` — Token-limit handoff to fresh chat. Save to .claude/crew-state/brock-handoff.md, resume with single command.
- `references/photon-imessage-setup.md` — Photon Spectrum iMessage setup (Hermes v0.17.0+). One command: `hermes photon setup`. Replaces BlueBubbles entirely.
- `references/system-prompt-playbook-10-techniques.md` — 10 techniques extracted from studying 35 system prompts across 28+ world-class AI tools (Anthropic, Google, Vercel, Cursor, Devin, Windsurf). Use when designing agent souls or system prompts. Embedded conciseness examples, banned phrases, refusal protocol, tool negative guidance, anti-sycophancy patterns.
