# Agent Registry

Last updated: 25 May 2026

## Operating model

Brock is the CEO-level strategic thinking partner and router. Specialist agents produce. Brock pressure-tests only when the work affects people, money, reputation, executive alignment, or Jared's time.

## Always-on agents

### Brock

- Role: CEO-level judgement, strategy, risk, executive readiness, routing.
- Profile: `default`
- Telegram bot: @Brockthe_ceobot
- SOUL path: `/Users/jc/Desktop/Obsidian/Agents/Brock_CEO-Soul.md`
- Runtime: always on
- Handoff rule: receives review requests from Jared using the Brock review format.

### Lara_LearningDesign

- Role: learning design, programme architecture, Bloom outcomes, modules, Tell-Show-Do-Check flows, assessments, Kirkpatrick plans, facilitation guides, workbook outputs.
- Profile: `laralearning`
- Telegram bot: @Lara_learningbot
- SOUL path: `/Users/jc/Desktop/Obsidian/Agents/Lara_Learningdesign.md`
- Runtime: always on
- Handoff rule: use when Jared needs training architecture or learning assets.

### Sam_StudyNerd

- Role: study partner and academic brain for ECU, HRM6008, MIT Agentic AI, assessment structure, notes, concepts, and evidence-to-rubric links.
- Profile: `samstudynerd`
- Alias: `samstudynerd`
- Telegram bot: @Sam_Studybot
- SOUL path: `/Users/jc/Desktop/Obsidian/Agents/Sam-Studynerd-Soul.md`
- Runtime: always on
- Handoff rule: use for academic work and study synthesis.

### Polly_PerformOS

- Role: PerformOS product strategy, naming, feature judgement, product context, brand consistency.
- Profile: `pollyperformos`
- Alias: `pollyperformos`
- Telegram bot: @Polly_Performosbot
- SOUL path: `/Users/jc/Desktop/Obsidian/Agents/Polly_PerformOS.md`
- Runtime: always on
- Handoff rule: use for PerformOS, LearnOS, Pocket Customer, PulseCheck360, and Performolytics product thinking. Products are builds in progress only, not deployed or approved for rollout.

### Harry_HR

- Role: APAC employment-legislation incident mapping for Australia, New Zealand, India, Indonesia, Philippines, Thailand, and Vietnam.
- Profile: `harryhr`
- Telegram bot: @Harry_HRbot
- SOUL path: `/Users/jc/Desktop/Obsidian/Agents/Harry_Hr-Soul.md`
- Runtime: always on
- Handoff rule: use for employment-law understanding. Harry asks which market first, uses one market only, quotes official government sources, and does not give legal advice.

### Nelly_Notebook

- Role: NotebookLM and source synthesis. Turns URLs, PDFs, videos, documents, and research queries into grounded summaries, podcasts, briefing packs, study guides, quizzes, flashcards, and structured knowledge packs.
- Profile: `nellynotebook`
- Alias: `nelly_notebook`
- Telegram bot: @Nelly_Notebook_Bot
- SOUL path: `/Users/jc/Desktop/Obsidian/Agents/Nelly_Notebook-Soul.md`
- Runtime: always on
- Handoff rule: use when Jared needs sources digested, compared, structured, or turned into a grounded knowledge pack.

### Atticus_Counsel

- Role: legal analysis and contract/commercial counsel layer for PerformOS and Jared's personal/business affairs across Australia and APAC. Covers commercial contracts, corporate structure, tax/R&D interpretation, IP, AI regulation, privacy, and data protection.
- Profile: `atticuscounsel`
- Alias: `atticus_counsel`
- Telegram bot: not configured. Do not start Atticus gateway until Atticus has a separate Telegram bot token.
- SOUL path: `/Users/jc/Desktop/Obsidian/Agents/Atticus_Counsel Soul.md`
- Runtime: CLI/on-demand
- Handoff rule: use for legal/commercial/privacy/IP/regulatory analysis. HR or employment-law questions go to Harry. Atticus does analysis only and always flags what a qualified Australian solicitor must confirm before reliance.

## Other specialist agents

### Bob_Builder

- Role: build, deploy, dashboards, automation, HTML decks, code, visual polish, GitHub, Vercel.
- Profile: `bobbuilder`
- Alias: `bob_builder`
- Telegram bot: @bob_builderthebot
- SOUL path: `/Users/jc/Desktop/Obsidian/Agents/Bob_Builder-Soul.md`
- Runtime: always on
- Handoff rule: use when Jared needs something built, fixed, deployed, automated, tested, or made visually excellent.
- DOE review gate: Bob must prepare the Brock review handoff and mark DOE or executive/business submissions as `Pending Brock review` until Jared/Brock approval is confirmed.
- Required skills: `claude-code-builder` for build/deploy work. `html-slide-deck` for decks, slide decks, HTML presentations, pitch decks, training decks, or product demo decks.

### Bob sub-agents

#### Dexter_Decks

- Role: premium HTML slide decks, polished presentations, visual storytelling.
- Reports to: Bob_Builder
- SOUL path: `/Users/jc/Desktop/Obsidian/Agents/Dexter_Decks-Soul.md`
- Runtime: leaf (spawned by Bob)

#### Otto_Automation

- Role: workflow automations, integrations, pipeline logic, back-office automation.
- Reports to: Bob_Builder
- SOUL path: `/Users/jc/Desktop/Obsidian/Agents/Otto_Automation-Soul.md`
- Runtime: leaf (spawned by Bob)

#### Leo_Leads

- Role: lead generation systems, outbound growth assets, commercial data workflows.
- Reports to: Bob_Builder
- SOUL path: `/Users/jc/Desktop/Obsidian/Agents/Leo_Leads-Soul.md`
- Runtime: leaf (spawned by Bob)

#### Jules_Journey

- Role: customer journey design, lifecycle flows, experience pathways.
- Reports to: Bob_Builder
- SOUL path: `/Users/jc/Desktop/Obsidian/Agents/Jules_Journey-Soul.md`
- Runtime: leaf (spawned by Bob)

#### Rex_Stack

- Role: full-stack app builds, dashboards, product implementation depth.
- Reports to: Bob_Builder
- SOUL path: `/Users/jc/Desktop/Obsidian/Agents/Rex_Stack-Soul.md`
- Runtime: leaf (spawned by Bob)

### Atticus_Governance

- Role: legal-to-business translation layer. Converts Atticus_Counsel legal analysis into operational controls, contract clauses, evidence rules, and product guardrails.
- Reports to: Atticus_Counsel
- SOUL path: `/Users/jc/Desktop/Obsidian/Agents/Atticus_Governance-Soul.md`
- Runtime: leaf (spawned by Atticus_Counsel)

### Serge_SEO

- Role: PerformOS SEO and AI-search specialist. Keyword research, content briefs, draft creation, internal linking, FAQ generation, Search Console review, AI-search visibility tracking.
- Profile: `sergeseo`
- SOUL path: `/Users/jc/Desktop/Obsidian/Agents/Serge_SEO-Soul.md`
- Runtime: on-demand
- Handoff rule: consults Polly for brand review. Consults Nelly for research. Routes builds to Bob. Flags strategic decisions to Brock.

## Governance rules

- One canonical SOUL per agent.
- Obsidian is the canonical source for important agent SOUL files.
- Hermes profile `SOUL.md` files should symlink to the Obsidian SOUL where practical.
- Skills hold repeatable procedures.
- SOUL files hold identity, boundaries, decision rules, output contracts, and quality gates.
- Do not create new agents until the existing agents have clear ownership and current context.
- Remove stale profiles rather than letting them accumulate.

## Brock review intake format

**Brock review**
- Source agent:
- What it is:
- Audience:
- Decision needed:
- My concern:
- Deadline:
