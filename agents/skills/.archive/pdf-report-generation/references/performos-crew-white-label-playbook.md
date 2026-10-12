# PerformOS Crew White-Label Playbook Notes

Use when generating or updating a PerformOS Crew playbook PDF intended for external business review or white-label client installation.

## Required white-label framing

- Keep the title/name: PerformOS Crew.
- Present PerformOS Crew as the role and workflow layer for Claude Code.
- Present Superpowers as the standards layer only.
- Present Layer 3 as the Business Context Layer, not PerformOS as the business layer.
- The client business supplies the context: brand, customers, workflows, systems, risks, approval rules, privacy/access rules, and commercial outcomes.
- PerformOS Crew supplies the AI work team structure.

## Do not include in client-facing PDFs

- "Caveman mode" or any internal behaviour shortcut.
- Jared-specific wording or ownership.
- Internal agent names such as Brock, Bob, Lara, Neo, Harry, Polly.
- PerformOS business-specific examples like the PerformOS website, AgentOS positioning, internal product strategy, or Jared's agent ecosystem.
- Internal runtime details unless explicitly needed by the client: Hermes, NVIDIA NemoClaw, OpenShell, Obsidian agent souls, Telegram bots.
- External repository names or provenance details in the client-facing body.

## Professional operating-mode names

Use these instead of internal shorthand:

- Fast mode: small, low-risk edits.
- Controlled mode: normal builds where planning and verification matter.
- Governed mode: public, client-facing, financial, data-sensitive, security, agent, or deployment work.

## Client-safe role examples

Use generic specialist roles:

- strategy lead
- build lead
- learning lead
- compliance lead
- operations lead
- QA lead
- release lead

Explain the difference plainly:

- Specialist roles are who is responsible.
- Flow skills are the review lenses or checkpoints.
- Claude Code is the workshop.
- Business Context Layer is the client-specific context and constraints.

## Writing for a business owner who has never used AI

This is the most important rule. When Jared says "so simple someone who has never picked up Claude or AI before can understand it," every section must pass this test:

- Would a business owner with zero AI knowledge understand this paragraph?
- Does this skill's description answer "what does this actually do for my business?"
- Is every technical term either removed or explained in plain business language?
- Are the examples in everyday business situations (sales follow-up, campaign planning, customer questions) rather than technical scenarios?

If a section would confuse a non-technical business owner, rewrite it.

## Skill Pack Catalogue pattern

When Jared asks to break the Crew system down into individual skills:

- Give every skill its own plain-English section with: what it does, a simple workflow, an example use, and an example output.
- Use business language throughout. A "lead research skill" helps "turn a list of prospects into researched briefs." Do not say "a lead-research SKILL.md file that runs inside Claude Code."
- Include a skill selection guide at the end so a business can identify which packs apply to their needs.
- The catalogue should feel like a menu a business owner can read and choose from, not a technical reference.

## Skill authoring contamination rule (HARD GATE)

When authoring white-label Crew skills, the skill body MUST be portable across any business. Never leak client-specific details into a skill file. This is the most important rule and the most common failure.

Before saving any skill SKILL.md, verify zero occurrences of:

- client business names
- client email addresses or domains
- client phone numbers
- client brand names or product names
- client-specific job titles or team names
- any string that would not make sense if the file were given to a different business

Use generic placeholders instead: `[business name]`, `[contact email]`, `[product name]`, `[team name]`.

This rule was learned hard: flow-support-triage, flow-support-reply, and flow-support-feedback were authored with "Accor Plus" references embedded in decision brief examples and example text. All had to be stripped and replaced with generic placeholders. A white-label skill that mentions a specific business is not a skill. It is a configuration that leaked.

## Skill depth standard (HARD GATE)

Every Crew skill must match G-Stack depth. A 15-line markdown stub with four bullet workflow steps and an output format is not a skill. It is a product description posing as an executable skill.

Every skill must include the full operational stack:

- YAML frontmatter (name, description, triggers, language)
- Preamble (session tracking, state init, context recovery, methodology link)
- When to invoke (trigger rules, anti-trigger rules, mode selection)
- Operating modes (fast, careful, governed)
- Cognitive framework (forcing questions, rubrics, pattern language)
- Step-by-step workflow (numbered phases with gates)
- Guardrails (safety constraints, escalation triggers, boundary enforcement)
- Decision briefs (completeness scoring, recommendation format, one-way gates)
- Output format (structured template)
- Context bridge (save on exit, restore on entry, cross-session compounding)
- Learning capture (pattern, pitfall, preference, architecture logging)
- Completion protocol (DONE, DONE_WITH_CONCERNS, BLOCKED, NEEDS_CONTEXT)
- Cross-skill integration (which skills call this one, which skills this one calls)
- Plan mode behaviour (what it can do without executing, what it cannot)
- Verification (checklist before claiming done)

The canonical skill template is saved at `references/performos-crew-skill-template.md` under this skill. Read it before authoring any new Crew skill. Every skill the user receives must pass the template. If a skill is shorter than 8KB, it almost certainly does not meet the standard.

## Verification checklist

Before rebuilding the PDF, verify the markdown source has:

- zero em dashes
- zero "caveman"
- zero Jared-specific references
- zero internal agent names
- zero PerformOS business-specific examples
- zero internal runtime references (Hermes, NemoClaw, etc.)
- zero business-specific names, emails, domains, or brands in skill bodies (contamination rule)
- Layer 3 named Business Context Layer
- client-facing or white-label language throughout
- every skill description passes the "non-technical business owner" test
- every skill body passes the "could this be given to a different business unchanged" test

Then render the PDF and deliver both the PDF and source path.

## Catalogue update via Claude Code prompt file

When the PerformOS Crew catalogue needs new packs or skills, do not rebuild the entire catalogue manually. Instead, create a self-contained markdown prompt file and hand it to Claude Code inside the catalogue project.

Pattern:

1. Write a markdown file (e.g. `performos-crew-catalogue-update.md`) containing the exact new skills and packs needed.
2. Each skill must include: what it does, plain English workflow, example use, example output.
3. Include build rules at the end: update build.py, match existing format, no em dashes, no internal names, white-label only, regenerate PDF.
4. Deliver the file to Jared via `MEDIA:<path>` so he can download it and hand it to Claude Code.
5. Claude Code reads the file, updates `build.py`, and regenerates the PDF.

This is the preferred pattern for catalogue updates. It keeps the source of truth (build.py) consistent and avoids two agents writing conflicting catalogue content.

## Methodology framework slide

When Jared asks to include a methodology slide without linking to Superpowers or any external project, use this pattern:

- Title the slide "How the Crew Works."
- List the 8 development standards as numbered steps with a one-line explanation each: brainstorm before building, plan in bite-sized tasks, build with testing built in, debug from root cause, verify before claiming done, review before shipping, finish cleanly, save and restore context.
- Close with a line like "These eight standards run underneath every Crew skill. They are the reason the output is consistent, safe, and professional, session after session."
- No external attributions, links, project names, or repo references.
- Place the slide after the architecture overview and before Core Crew.

## Canonical PerformOS Crew architecture

The four-layer model is the standard framing for all client-facing materials:

1. Core Crew — the safe operating rhythm (Idea Pressure Tester, Plan Reviewer, Quality Checker, Context Saver, Context Restorer, Guard Boundary).
2. Skill Packs — function-specific workflow packs (Sales, Marketing, Operations, HR and People, Finance and Admin, Customer Support, Documentation, Training and L&D).
3. Specialist Agents — role-based AI workers (Strategy Agent, Sales Agent, Marketing Agent, Operations Agent, HR Agent, Finance Admin Agent, Customer Support Agent, Research Agent, QA Agent, Documentation Agent).
4. Business Context Layer — the client-specific operating layer (brand, customers, products, workflows, systems, data boundaries, approval rules, risk level, success metrics).

Every client-facing document should reference this architecture and explain that PerformOS Crew supplies the structure while the client business supplies the context.

## PDF first, website second

When Jared asks for both a PDF and a website version of white-label content, always build the PDF first. The PDF becomes the clean source of truth. The website can then break the same content into clickable sections.

## Customer review monitoring workflow pattern

When Jared asks to build an automated review monitoring and response workflow for a business (e.g. ProductReview, Trustpilot, Google Reviews), use this proven pattern:

1. Build the flow skills first, not after the workflow. Use a self-contained markdown spec file that defines each skill with name, description, what it does, workflow, guardrails, and output format. Match the existing flow-* format exactly (YAML frontmatter with name and description only, no hooks or triggers). Save to .claude/skills/flow-support-*/SKILL.md. The three standard skills are: flow-support-triage (categorise reviews by severity, topic, escalation, and reply priority), flow-support-reply (draft warm professional replies under 150 words with a clear next step), and flow-support-feedback (identify complaint patterns and recommend root-cause actions).
2. Build the workflow after the skills are installed. Use: scraper (Firecrawl MCP or Python + Firecrawl API key) → dedup (content fingerprint, not timestamp) → triage → reply drafter → quality gate → Google Doc output → state commit.
3. The tone-of-voice playbook is mandatory. Before any reply is drafted, the workflow must read a playbook file that defines brand voice, reply structure, banned phrases, complaint-type handling rules, worked examples, escalation criteria, and a quality checklist. The playbook is a standalone markdown file the business can review and approve. See `references/accor-plus-review-playbook.md` for the canonical template.
4. Quality gate rules: every reply passes a checklist before landing in the doc. A rejected reply is withheld from the doc, not softened. The invariant must hold. Use flow-qa methodology even if the skill was designed for browser QA: check tone, accuracy, escalation risk, relevance, and whether the reviewer would feel heard.
5. Google Doc output: Drive MCP cannot append to existing docs. Use a fresh dated doc per run with master-log.md as the cumulative source of truth.
6. Reply boundary: draft only, never auto-post. Workflow ends at the doc. A human reviews and posts.
7. Schedule: manual until the workflow has produced verified output over multiple days, then wire as a daily Claude Code routine.

## Tone-of-voice playbook template

When a business needs AI to draft customer-facing replies, create a playbook following this structure: brand voice definition (what it is and what it is never), reply structure (exact sections in order), word limit, banned phrases list, complaint-type handling rules with worked examples for each type, escalation criteria, and a quality checklist. The canonical template is saved at `references/accor-plus-review-playbook.md` under this skill. Copy and adapt it for each new business.

Website section structure for a PerformOS Crew page:
- Hero: A modular AI work team for your business
- How it works: the four-layer model
- Skill Packs: clickable sections per pack
- Specialist Agents: role descriptions
- Business Context Layer: how the system becomes client-specific
- Install options: Core Crew, Department Crew, Business Crew, Governed Crew
- Examples: real business scenarios
- Call to action: book a Crew audit

## Standard skill packs and skill counts

The catalogue currently includes these packs with verified counts:

- Core Crew: 6 skills
- Sales Pack: 7 skills
- Marketing Pack: 7 skills
- Operations Pack: 5 skills
- HR and People Pack: 5 skills
- Finance and Admin Pack: 6 skills
- Customer Support Pack: 6 skills
- Documentation Pack: 7 skills
- Training and L&D Pack: 8 skills

Total: 57 client-facing skills across 9 sections (1 core + 8 packs). Report the exact count from the build.py data when regenerating.

The catalogue is a single-source build: build.py (data) renders to static index.html, then headless Chrome converts to PDF. Every skill is a 5-field tuple: (name, does, [workflow_steps], example_use, output). The card format is now 3-up timeline with a fourth content block (IN PRACTICE) between workflow and output. All catalogue updates should go through Claude Code reading a markdown prompt file that modifies build.py and regenerates.
