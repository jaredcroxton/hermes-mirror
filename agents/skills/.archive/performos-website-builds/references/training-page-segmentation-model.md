# Training Page Segmentation Model

Captured 15 June 2026. Documents the evolution from single-track to two-track to three-tier, and the design principles that drove each shift.

## Evolution

### Phase 1: One track (original)
Single training page. Everyone takes the same path. Problem: enterprise buyers saw no team angle. Individual learners saw too much business framing. Nobody felt fully served.

### Phase 2: Two tracks (14 June 2026)
Split into Learn AI (individual) and AI for Teams (business operators). Shared modules 1 to 7, forked modules 8 to 10. Problem: the sole operator who runs a small business fell between both tracks. Learn AI felt too basic ("I need business outcomes"). AI for Teams felt too heavy ("I am not an enterprise").

Jared's correction (15 June 2026):
> "I want to target everyday individuals who are running their own business that want all these things as well. I feel like it just keeps pulling it back into the business workflow."

### Phase 3: Three tiers (15 June 2026, current)
Three clearly separated buyer profiles on page load:

| Tier | Buyer | Build outcomes | Modules 8-10 |
|---|---|---|---|
| Build Yourself | Individual learner | Portfolio, personal projects, skill | Design, maintenance, personal capstone |
| Build for Small Business | Sole operator | Stripe, dashboards, client tools, revenue | Business tools, client systems, revenue capstone |
| Build for Enterprise | Team leader | Governed AI, specialist agents, audit | Team agents, governed deployment, enterprise capstone |

## Design principles

### Do not split the buyer in half
A two-track model forces a single buyer to pick between "not business enough" and "too enterprise." They bounce. Three tracks gives the most common buyer (sole operator) a clear home.

### The agents page and the training page serve different buyers
- Agents page: "We build your private AI team." Enterprise sale. Done-for-you.
- Training page: "Learn to build with AI." Skill sale. Anyone.

The enterprise training tier teaches leaders to lead AI. It does not compete with the agents page — it feeds it. A leader who takes enterprise training may still buy the done-for-you service.

### Shared foundation, forked finish
All three tiers share modules 1 to 7: Foundations, Real Websites, Deploy, Power Features, AI Agents, Memory Systems, Build Anything. Only modules 8 to 10 diverge. This keeps the build manageable and the value proposition clear: start together, specialise at the end.

### Specific build outcomes sell harder than topic names
"Build a Stripe-connected order page" outperforms "Business Tools" as a module description. "Build a revenue dashboard that tracks your business" outperforms "Build Anything." Name what the learner ships, not what the module covers.

## Page layout rule

When someone opens the training page, they see three tiles and nothing else. Clean choice. No copy. No scrolling required. Click a tile to see the modules relevant to that path.

## Module fork map

| Module | Build Yourself | Small Business | Enterprise |
|---|---|---|---|
| 08 | Design Systems (personal brand) | Business Tools (Stripe, dashboards, client portals) | Team AI Agents (specialist agents across business functions) |
| 09 | Maintenance and Growth | Client Systems (CRM, lead gen, automation) | Governed Deployment (NemoClaw, policies, audit) |
| 10 | Personal Capstone | Revenue Capstone (ship a money-making tool) | Enterprise Capstone (deploy governed team workflow) |

## Shared foundation module architecture (locked 15 June 2026)

Rebuilt after Jared asked Brock to restructure the modules to match Jack's comprehensive Claude Code curriculum flow. The order and naming are intentional:

| Module | Title | Lessons | Key differentiator |
|---|---|---|---|
| 01 | Foundations | 9 | CLAUDE.md + Plan Mode, not just setup |
| 02 | Real Websites | 7 | Three-step system: competitor intel → design → host |
| 03 | Power Features and Skills | 11 | **Highlighted module.** Skills, hooks, MCP, subagents, critic loop. The "wow" module. |
| 04 | Memory Systems | 6 | Three levels: context, project, long-term. Obsidian + NotebookLM + vector. |
| 05 | AI Agents | 8 | Specialist agents with roles, voices, boundaries. Hermes runtime. |
| 06 | Apps and Dashboards | 7 | Dedicated app module. Stripe, Supabase, real applications. |
| 07 | Build Anything | 6 | Browser automation, Telegram bots, lead pipelines, n8n. Full-stack capstone prep. |

**Module naming rules:**
- "Apps and Dashboards" is a dedicated module, not bundled into "Build Anything." It signals real application building.
- "Power Features and Skills" is the hero module. It gets visual highlighting (neon border, radial gradient background). This is the module that makes people think "AI can do THAT?"
- "Build Anything" is the bridge module before the fork. It teaches general composing skills so the learner is ready for any track.

**Lesson detail rule:**
Every lesson must carry a one-line description of what the learner actually does. "Install Claude Code — desktop app and terminal path" not just "Install Claude Code." The description answers "what will I actually do in this lesson?"

**Tool tags per module:**
Every module card lists the specific tools used (e.g., Module 06: Claude Code, Stripe, Supabase, Vercel, APIs). Tool tags in the module card preview the stack before the learner commits.

## Shared → fork pattern

Modules 01-07 are shared by all three tiers. The fork happens at module 08. On the page, modules 08-10 are presented in three columns under the heading "Modules 8 to 10: choose your path."

## Anti-patterns

- Do not use "AI for Teams" language. It confuses the sole operator buyer.
- Do not put enterprise governance language (NemoClaw, audit trails, token masking) on the Build Yourself or Small Business tracks.
- Do not let the training page compete with the agents page. Enterprise training teaches leadership; agents page sells the build service.
- Do not bundle Apps into Build Anything. Apps and Dashboards deserves its own module — it signals the transition from "building websites" to "building real applications."
- Do not bury Skills inside Power Features without naming it. "Power Features and Skills" makes the Skills promise explicit in the module title.
