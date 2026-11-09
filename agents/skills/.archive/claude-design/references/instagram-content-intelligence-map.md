# Instagram Content Intelligence Map Pattern

Use when Jared is building a JEV, AI scoring, content research, or lead-scoring product where Instagram posts are analysed before LinkedIn or Apollo leads.

## Core lesson

The visual map is the product. A table-first dashboard makes the system feel like admin software. Jared wants the Instagram reference style: an AI intelligence surface where posts become visible objects in a spatial system.

## Required sequence

1. Instagram first: analyse posts and create a message library.
2. Visual map second: show where every post sits.
3. Message library third: make the retained patterns obvious from the map.
4. LinkedIn or Apollo lead scoring last: score people against the message library.

Do not polish the LinkedIn table before the Instagram map exists.

## Primary screen

Lead with a 2D content map, not import controls, KPI cards, or a source table.

If Jared says the layout is confusing, too busy, or asks why it cannot look like the Instagram video, the fix is usually subtraction and separation, not more explanation or more panels.

Default to a tabbed workspace:

| Subtab | Job |
|---|---|
| Map | Large clean graph of Instagram posts |
| Patterns | Retained message angles and source post chips |
| Post Detail | One selected post and its JEV decision |
| Evidence | Source table and raw fields |
| Leads | LinkedIn or Apollo scoring later only |

The default Map tab should show only the page title, short subtitle, large map canvas, minimal controls, and a collapsed or light selected-post preview. If an element is not needed to understand the map in three seconds, hide it in a subtab.

Recommended axes:

| Axis | Meaning |
|---|---|
| X-axis | Replicability |
| Y-axis | Outbound angle value |

Quadrants:

| Quadrant | Meaning |
|---|---|
| Top right | Goldmine posts, save to library |
| Top left | Strong but harder to reuse |
| Bottom right | Reusable but weak commercially |
| Bottom left | Ignore or manual review |

## Node design

Each Instagram post should appear as a visual node or mini Reel-style tile, not a plain dot or table row.

Encode meaning visually:

| Visual property | Meaning |
|---|---|
| Colour | JEV-selected message angle |
| Size | Engagement or overall content strength |
| Border strength | JEV confidence |
| Glow or pulse | Saved to message library |
| Low opacity | Manual review or weak evidence |
| Connection lines | Same angle, same format, or high similarity |

## Detail panel

Clicking a node should open a right-side intelligence panel with:

- post URL
- hook
- caption or transcript snippet
- content format
- primary message angle
- JEV scores
- confidence
- retained or not retained
- why it should or should not enter the message library
- suggested outbound use

## Supporting table

The table remains useful, but it should be secondary and labelled as evidence, for example:

- Evidence table
- Source post review
- Decision evidence

The table must not be the primary experience.

## Design posture

Aim for a premium intelligence board or calm visual workspace, depending on the reference Jared supplies.

For Instagram-video or AI-system references:

- visual, spatial, and focused
- content objects as the main surface
- one hero map, not a dashboard wall
- restrained accent and subtle motion

For LottieFiles-style references:

- light grey app background
- white map canvas
- simple left navigation
- top search or workspace bar
- generous whitespace
- sparse controls
- details only when selected
- no dense legends or tables above the fold

Avoid:

- CRM table-first layouts
- generic KPI card walls
- purple AI SaaS templates
- dashboards where the graph is absent or decorative
- analyst screens where every control, legend, workflow step, table, and inspector is visible at once
- moving to LinkedIn scoring UI before the Instagram map is compelling

## Review language for Jared

When reviewing iterations for Jared, judge layout density before backend completeness. Useful verdict pattern:

- "This is clean, but still table-first" when the map exists only as a supporting element.
- "The visual map is now the hero" when the first viewport is dominated by the graph.
- "Subtract, do not add" when the screen is busy.
- "Keep this direction, refine rather than redesign" once the shell, map, hidden table, and click inspector are working.

Stress test the map with 10, 25, and 50 posts before calling the design direction stable.
