# Visual intelligence map workspaces

Use this reference when Jared is guiding a dashboard or AI tool toward a premium visual workspace rather than a dense table-first dashboard.

## Trigger signals

- Jared says the layout is confusing, busy, or not like the Instagram video/reference.
- The product's value is a visual relationship map, content map, lead map, workflow map, or pattern space.
- A builder keeps adding panels, tables, KPI cards, legends, and workflow strips into one screen.
- Jared asks for subtabs or says the UI should look more like a clean reference such as LottieFiles.

## Core principle

The map is the product. The table is supporting evidence.

Do not ask a single screen to show every requirement. Separate functions into tabs or subtabs, then make the default screen carry one clear visual job.

## Preferred layout

Use a calm light workspace unless the brand explicitly requires dark.

Recommended structure:

```text
Left sidebar
Top bar with search/status/action
Page title and one-line subtitle
Primary visual map canvas
Collapsed or minimal inspector
Secondary subtabs for Patterns, Detail, Evidence, Leads
```

Default subtab should be the visual map. Evidence tables, detailed model fields, workflow rows, and long legends should be hidden behind subtabs or disclosure controls.

## Map screen rules

The above-the-fold map screen should show only:

- page title
- short subtitle
- large visual canvas
- minimal map controls if needed
- selected-object preview only after selection
- one primary action

Do not show by default:

- raw table
- workflow step row
- synthetic/sample disclaimer banners unless legally required
- long legends
- quadrant explanation blocks
- output summaries
- all model fields
- secondary workflow areas

If an element is not needed to understand the map in three seconds, move it into a subtab.

## Visual encoding pattern

For content or lead maps, use clear spatial meaning instead of random clusters.

Example for an Instagram content map:

- X-axis: Replicability
- Y-axis: Outbound angle value
- colour: message angle
- size: strength or engagement
- border or ring: confidence or retained status
- muted opacity: manual review
- lines: shared angle or format

Use object-like nodes, not plain dots, when the source items are content objects. For Instagram-style work, each node should feel like a mini Reel tile with post number, hook, handle, state badge, and a subtle play/content marker.

## Interaction pattern

Clicking a node opens a clean inspector. The inspector should show only the decision-critical information first:

- title or hook
- source/creator
- category or angle
- retained/review status
- three to five key scores
- short recommendation

Detailed model fields belong behind `View details`, `JEV details`, or a Detail subtab.

The selected node should visibly connect to the inspector using an active ring, slight lift, matching accent, or soft connector. Keep it subtle.

## Density and scale

Always stress test visual maps with more than the demo count.

Minimum checks:

- 10 items
- 25 items
- 50 items if the use case may reach that scale

If the map gets crowded, add clustering, zoom, filters, or fan-out. Do not solve density by shrinking tiles until unreadable or reverting to a table-first layout.

## Jared-specific judgement rule

When Jared is reacting to a reference video or clean product screenshot, avoid defending functional completeness. His concern is usually composition and clarity.

Respond at the level of layout hierarchy:

- What should be visible first?
- What should be hidden in a subtab?
- What is the one job of this screen?
- Does the map feel like the product or just a decoration?

Short verdict language works best: `This is cleaner, but still too table-first.` Then give the exact builder prompt.
