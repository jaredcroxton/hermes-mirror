# AgentOS page copy and interaction patterns

Use this reference when Jared asks Brock for PerformOS/AgentOS website page copy, AntiGravity briefs, hero demo copy, pricing/security/solution page structure, or page-review judgement.

## Core positioning

AgentOS by PerformOS should be framed as:

**Private AI team for business leaders.**

Avoid making the offer sound like another chatbot, bot pack, or AI subscription. The premium story is:

**AgentOS maps how the business operates, then builds private AI capability around its roles, systems, workflows, standards, judgement, and approved boundary.**

Useful repeated lines:

- Private AI team for business leaders.
- Built around your operating model.
- Bring AI inside your boundary.
- AgentOS is built around the business, not the other way around.
- Ask like a leader. Get work back like an operator.

## Jared’s preferred deliverable pattern

For AgentOS website work, Jared often wants Markdown files he can paste into AntiGravity, not execution or deployment.

Default when asked for pricing/security/solution/hero copy:

1. Create a concise but complete `.md` file on Desktop.
2. Include page purpose, page structure, exact copy blocks, CTA copy, comparison sections if useful, and language to avoid.
3. Send immediately as a Telegram `MEDIA:` attachment.
4. Keep the chat summary short.

Do not over-brand the file unless asked. Jared will use AntiGravity to build the page.

## Pricing page pattern

Do not lead with parameter counts. Lead with buyer value.

Use two clear options:

- Standard: everyday business support, usually 8B-class local/private model.
- Advanced: complex leadership reasoning, usually 14B to 70B-class private model range.

Explain parameter counts lower down for technical buyers.

Recommended comparison rows:

- Private/local data retention
- Client-controlled environment
- Approved business sources
- Role-scoped access
- Human approval
- Audit logs
- Up to 10 custom agents
- Everyday briefs and summaries
- Workflow support
- Dashboard/report support
- Complex reasoning
- Multi-step strategic analysis
- Advanced executive decision support
- Larger model options
- Higher setup depth

Tone: business plan comparison, not model benchmark sheet.

## Security page pattern

The security page should make this point land hard:

**The risk is not AI. The risk is uncontrolled AI.**

Then position AgentOS as:

**Bring AI inside your boundary.**

Be technically accurate. Do not claim the data is never interpreted by any language model. The model must interpret data to be useful.

Safer language:

- Your business data does not need to be sent to public AI tools.
- Local/private configurations do not use your business data to train public vendor models.
- AgentOS runs inside the boundary the client approves.
- Every action can be approved, logged, and scoped.

Security proof points:

- Human approval on every action
- Audit logs for what agents do
- Client-controlled environment
- No public AI tools by default
- Data stays in the approved boundary
- Role-scoped access only

## Solution page pattern

The solution page should not feel like a list of easy agents. It should feel like a mapped operating model.

Use two solution paths:

### 1. Orchestrated company AI team

Up to 10 specialist agents that play defined roles across leadership, operations, growth, HR, research, reporting, learning, customer insight, and workflow support.

Best for shared business capability.

### 2. Personalised leader and team agents

Private agents configured around executives, department heads, or teams. These should account for priorities, meetings, communication style, decision patterns, team rhythm, source documents, and approval boundaries.

Best for executive adoption and deep personalisation.

Recommended section line:

**Your operating model, encoded.**

## Hero demo interaction pattern

If the hero/demo section needs to show “how does this work?”, do not show a simple chatbot exchange. Show an executive operating console.

Animation loop:

**Ask → Review → Deliver → Clarify → Build**

Recommended interaction:

1. Compact prompt card opens.
2. It expands into a full-size chat/workspace console.
3. Operator asks in plain business language.
4. AgentOS reviews approved sources/context via checklist.
5. AgentOS returns a structured output card.
6. AgentOS asks the next intelligent question.
7. The next workflow path appears.

The chat is the doorway. The structured output is the value.

Example copy:

**Operator**

> “We need more qualified leads this quarter without wasting budget. Where should I focus first?”

**AgentOS**

> “I’ll review your approved sources, current channels, lead quality, conversion patterns, and owner capacity.”

**AgentOS reviews**

- Approved sources
- Current channels
- Lead quality
- Conversion patterns
- Wasted effort
- Owner capacity

**Growth brief**

- **Focus:** prioritise the highest-fit lead sources
- **Stop:** reduce low-conversion activity
- **Test:** three sharper outreach angles
- **Track:** weekly revenue actions and follow-up status

**AgentOS asks next**

> “Before I build the dashboard, what counts as a qualified lead for this business?”

Scope line:

**The same loop works for meeting prep, decision briefs, risk reviews, people conversations, operations updates, and dashboards.**

## Page review principles

When Jared asks “how can we lift this?” review like Brock, not a copywriter.

Look for:

- Is the page selling outcomes or tasks?
- Does it support a $4,999/month managed offer?
- Does it make AgentOS feel private, governed, and business-specific?
- Is it too narrow by function, e.g. only sales or admin?
- Does it explain how AgentOS adapts to each business?
- Does the demo show judgement and operating leverage, not just text generation?

Common correction:

If the copy says “agent does admin task,” lift it to “leader asks messy business request, AgentOS returns decision-ready work and asks the next business-rule question.”

## Design-language extraction before visual builds

Jared has a Claude Code skill called `design-language` for extracting a reference website’s design language before building. Bob now has it installed at:

`/Users/jc/.hermes/profiles/bobbuilder/home/.claude/skills/design-language/`

Use it when Jared wants a website to feel like a premium reference site. It extracts typography, colour, spacing rhythm, layout architecture, component patterns, interaction feel, page structure, and the load-bearing design decisions.

Do not confuse it with `architecture-diagram`, which is for SVG architecture diagrams, not website architecture extraction.

Two modes matter:

- **Neutral extraction:** keep the file strictly about the reference site. Do not inject AgentOS, PerformOS, Jared, or destination-brand notes.
- **Applied build:** use the reference design language as inspiration for an original AgentOS/PerformOS page after the neutral extraction exists.

See `references/design-language-extraction-before-build.md` for Bob brief patterns.

## Antigravity-inspired motion pattern

When Jared says he wants the Antigravity look and feel, do not simply add lots of animation. The lesson is: **more motion, less noise.** Antigravity feels premium because motion is large, sparse, slow, and purposeful.

Translate the feel with:

- Hero ambient particles: small coloured dots or line fragments drifting slowly around the hero, low opacity, subtle mouse parallax.
- Hero reveal: fade up plus slight blur-to-sharp. Stagger headline lines by about 120ms. Avoid typewriter for the main H1.
- Tactile CTA pills: 2px lift, arrow moves 4px, slight darkening, soft shadow.
- Operating loop console: animate through `Ask → Review → Deliver → Clarify → Build`, with the left rail highlighting each step, context nodes appearing, output cards rendering, and the next-question bubble appearing before the workflow skeleton.
- Scroll reveals: section blocks fade up 24px with slight blur, child cards stagger by about 80ms, trigger once.
- Use-case proof cards: ask appears first, then delivered output lines fade in or type in cleanly.
- Security section: subtle audit ticks, boundary/grid line, or scanning line to make “governed like infrastructure” visible.

Avoid bouncing, spinning icons, constant flashing, typewriter everywhere, cartoon robots, excessive gradients, and animated clutter.

Best builder instruction:

**Make the page feel alive, not busy.**
