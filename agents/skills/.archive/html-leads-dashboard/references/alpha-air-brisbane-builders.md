# Alpha Air Brisbane Builder Leads Dashboard

Session reference for the `html-leads-dashboard` skill.

## User request

Build an HTML leads dashboard for Alpha Air in Brisbane to contact builders in the area that build homes.

## Assumption used

Alpha Air likely sells HVAC / air-conditioning services into residential builders. The dashboard should position Alpha Air as a trade partner that protects build schedules, supports ducted and split-system installs, reduces callbacks, and improves handover quality.

## Data shape used

The dashboard used company-level public leads, not named contacts.

Lead fields:

- builder name
- segment
- priority
- fit score
- website
- phone
- email
- area
- tailored Alpha Air sales angle
- source note

Segments used:

- Volume builder
- Custom builder
- Luxury builder
- Renovation/custom

Priority labels used:

- Hot
- Warm
- Niche

## Useful lead examples

Hot targets included:

- Brighton Homes
- Plantation Homes
- Coral Homes Brisbane
- Metricon
- Clarendon Homes QLD
- Creation Homes QLD
- Orbit Homes QLD
- G.J. Gardner Brisbane
- McCarthy Homes

Warm/niche targets included custom, luxury, and renovation builders such as Nuvo Homes, Ownit Homes, GW Homes, Lindon Homes, Jensen Constructions, Tide Constructions, HB Build Collective, ProRes Construction, and others.

## Dashboard mechanics that worked

- Self-contained HTML file on Desktop.
- Dark premium dashboard visual system.
- Search across all lead fields.
- Filters for segment, priority, and status.
- Status dropdown per lead.
- Note field per lead.
- `localStorage` persistence for status and notes.
- `tel:` action buttons.
- `mailto:` action buttons with drafted email body.
- CSV export of currently visible filtered rows.
- Desktop table and mobile card view.

## Copy pattern that worked

Commercial hook:

> Keep build schedules moving when air-con demand spikes.

First routing ask:

> Who manages HVAC trade partners for your Brisbane builds?

Call script:

> Hi, this is Alpha Air in Brisbane. We support residential builders with ducted and split-system air installs. I’m trying to reach the person who manages air-conditioning trade partners or supplier panels. Who is best for that?

Email opener:

> We help builders protect handover dates with responsive quoting, clean installs, and fewer post-handover HVAC callbacks. Worth a 10-minute supplier fit check?

## Verification performed

- Opened local file in browser.
- Confirmed search filtered visible rows correctly.
- Checked browser console: no JavaScript errors.
- Visual review showed no major clipping or broken table layout.
- Minor layout fix applied so `No email found` and source text sit on separate lines.

## Pitfalls

- Public scraping can pull malformed phone numbers. Clean manually before embedding.
- Do not treat company-level public contacts as verified CRM data.
- If no email or phone exists, show the absence clearly rather than inventing details.
- Keep the final answer short and give the file path first.
