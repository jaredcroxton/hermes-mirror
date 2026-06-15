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

## Verification checklist

Before rebuilding the PDF, verify the markdown source has:

- zero em dashes
- zero "caveman"
- zero Jared-specific references
- zero internal agent names
- zero PerformOS business-specific examples
- zero internal runtime references (Hermes, NemoClaw, etc.)
- Layer 3 named Business Context Layer
- client-facing or white-label language throughout
- every skill description passes the "non-technical business owner" test

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

The catalogue currently includes these packs (approximate skill counts):

- Core Crew: 6 skills
- Sales Pack: 7 skills
- Marketing Pack: 7 skills
- Operations Pack: 7 skills
- HR and People Pack: 7 skills
- Finance and Admin Pack: 7 skills
- Customer Support Pack: 7 skills
- Documentation Pack: 7 skills
- Training and L&D Pack: 8 skills

Total: approximately 63 client-facing skills across 9 sections (1 core + 8 packs). Report the exact count from the build.py data when regenerating.
