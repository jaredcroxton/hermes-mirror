# PerformOS Crew Skill Pack Catalogue — Architecture

Captured 15 June 2026 from the white-label Crew product design session.

## Trigger

When Jared asks how to break the PerformOS Crew system down into a client-facing skill pack catalogue that a business owner with zero AI experience can understand.

## The four-layer architecture

```
PerformOS Crew
│
├── Layer 1: Core Crew — the safe operating rhythm
│   ├── idea review / demand diagnosis
│   ├── task planning
│   ├── quality checking
│   ├── review gates
│   ├── context save and restore
│   ├── documentation
│   ├── approval points
│   └── guardrails
│
├── Layer 2: Skill Packs — optional workflow packs by business function
│   ├── Sales Pack
│   ├── Marketing Pack
│   ├── Operations Pack
│   ├── HR and People Pack
│   ├── Finance and Admin Pack
│   └── Customer Support Pack
│
├── Layer 3: Specialist Agents — role-based AI workers
│   ├── Strategy Agent
│   ├── Sales Agent
│   ├── Marketing Agent
│   ├── Operations Agent
│   ├── HR Agent
│   ├── Finance/Admin Agent
│   ├── Customer Support Agent
│   ├── Research Agent
│   ├── QA Agent
│   └── Documentation Agent
│
└── Layer 4: Business Context Layer — client-specific
    ├── Brand voice
    ├── Products and services
    ├── Customers
    ├── Workflows
    ├── Systems and tools
    ├── Data boundaries
    ├── Approval rules
    ├── Risk level
    └── Success metrics
```

## Skill Pack catalogue structure

Each skill pack in the catalogue follows this format:

1. **Pack name and purpose** — one sentence
2. **What it helps with** — bullet list of business activities
3. **Each individual skill broken down into:**
   - What it does (plain English, one to two sentences)
   - Plain English workflow (the steps)
   - Example use (a real business scenario)
   - Example output (what the business gets)

## White-label rules for the catalogue

- Zero em dashes
- Zero "Caveman mode"
- Zero Jared references
- Zero internal agent names (Brock, Bob, Lara, Neo, etc.)
- Zero Hermes, NemoClaw, Obsidian, or runtime-specific references
- "PerformOS Crew" may appear as the product name but no other PerformOS business context
- Write for a business owner who has never used AI before
- Every skill answers: "What does this actually do for my business?"

## Identified gaps (not yet in any pack)

1. **Documentation Pack** — `docs-generate` and `docs-release` exist in the flow layer but are not surfaced as a client-facing Skill Pack. Every business needs SOPs, policy documents, training guides, and playbooks.

2. **Training and L&D Pack** — not in G-Stack at all. A PerformOS addition built from Jared's professional expertise. Would cover training needs analysis, module outlines, facilitator guides, learner workbooks, assessment design, onboarding programmes, and coaching conversation guides.

## Install options for client proposals

1. **Core Crew** — businesses starting with AI
2. **Department Crew** — one team or function (Sales Crew, Marketing Crew, etc.)
3. **Business Crew** — multiple functions with several skill packs and agents
4. **Governed Crew** — larger or higher-risk environments with stricter approval gates
