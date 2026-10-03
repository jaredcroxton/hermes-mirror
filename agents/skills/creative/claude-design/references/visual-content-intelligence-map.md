# Visual content intelligence map pattern

Use this when Jared is building a content research, lead intelligence, or JEV-style scoring interface where the value is visual pattern recognition, not data-table review.

## Core lesson

The visual map is the product. Tables, raw scores, workflow steps, and evidence rows are supporting material. If they appear first, the interface reads as a generic analyst dashboard and misses the brief.

## Best default structure

Use a calm workspace shell:

- left sidebar
- top search/header bar
- light grey app background
- large white canvas
- one clear page title
- one primary action
- detail only after selection

Default screen order:

1. Page title and short subtitle
2. Large visual map canvas
3. Minimal selected-item preview or hidden inspector
4. Secondary controls below or in subtabs
5. Evidence table hidden behind a tab or disclosure

## Content map model

For Instagram/content pattern systems, use a 2D map:

- X-axis: Replicability
- Y-axis: Outbound value or commercial value
- top right: Goldmine posts
- top left: Strong but harder to reuse
- bottom right: Reusable but commercially weak
- bottom left: Ignore or manual review

Each post should render as a visual content object, not a table row or plain dot.

Useful node encoding:

- colour = message angle
- size = content strength or engagement
- border strength = confidence
- accent ring = retained or saved to library
- low opacity = review needed
- lines = shared angle or format

A selected node should have an obvious active ring, subtle lift, and a visually linked inspector.

## Interaction rules

Use subtabs instead of one crowded screen:

- Map: only the visual map and minimal controls
- Patterns: message library and angle cards
- Post Detail: full selected post and JEV details
- Evidence: raw table
- Leads: later-stage lead scoring

Rule: if it is not needed to understand the map in three seconds, move it to a subtab or disclosure.

Inspector default:

- empty state: Select a post to inspect the pattern
- selected state: hook, creator, message angle, retained or review status, three key scores, short recommendation
- full model details behind View JEV details

## Scale rules

Always stress test visual maps with more than demo data:

- 10 items
- 25 items
- 50 items if realistic

If the map becomes crowded, add clustering or fan-out. Do not solve density by shrinking everything or reverting to a table-first view.

Cluster behaviour:

- group by message angle or content format
- show count on cluster bubble
- click to expand
- keep table as evidence, not the main interface

## Common failure modes

- table-first layout
- workflow strip, legend, inspector, output summary, and evidence table all visible at once
- too many tiny labels
- dense JEV/model metadata in the first viewport
- map looks like a technical chart instead of a workspace
- detail panel always open and competing with the map
- lead scoring polished before the content map is strong

## Design target language

Use these phrases in handoffs to builders:

- premium visual workspace
- content intelligence map
- visual pattern board
- calm LottieFiles-style shell
- details on click
- the map is the product, the table is evidence

Avoid briefing it as a dashboard unless the output truly should be table or KPI-first.