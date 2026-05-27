# Session reference: Accor Plus US market HTML deck

## Context

Jared asked for a premium HTML slide deck built from public information on `accorplus.com`, aimed at a US hotel leadership audience. The goal was to position Accor Plus as a membership-led demand engine that could help lift US hotel occupancy.

## Source synthesis pattern

When scraping a source site for a commercial deck:

- Extract factual product claims separately from proposed-market strategy.
- Preserve limitations. In this case, Accor Plus was presented publicly as Asia Pacific-led with worldwide Accor hotel benefits, so the deck must not claim Accor Plus already operates in the USA.
- Frame speculative expansion as a proposed market application or pilot.

Useful source facts from the session:

- ALL Accor+ Explorer is a 12-month travel loyalty subscription membership.
- Public positioning: unlock new horizons, designed for explorers at heart.
- Scale shown: 20 countries, 1,300+ hotels, 1,600+ restaurants, 400+ exclusive events.
- Benefits include two Stay Plus free nights, Red Hot Rooms, dining and drinks discounts, 15% off stays at Accor hotels worldwide, 30 status nights, member-only events, partner offers, and More Escapes packages.
- Price shown: USD 249 per year or 14,000 Reward Points per year.

## Strategic spine that worked

The strongest commercial line was:

> Accor Plus is not just a discount programme. It is a membership-led demand engine.

For US hotel leaders, emphasise:

- controllable demand
- need-period occupancy
- shoulder-night stimulation
- repeat stays
- direct demand
- dining and bar utilisation
- loyalty economics
- reduced dependency on broad discounting and OTA pressure

## Visual direction that worked

- Premium hotel-commercial, not patriotic gimmick.
- Deep navy base, Accor-like royal blue, refined gold, restrained red and blue micro-accents.
- US theme through abstract map lines, premium city labels, revenue grid motifs, and corridor/pilot language.
- Avoid flag stripes as the dominant design device.

## QA lesson

The first rendered version had lower navigation crowded against topic chips and source text. Fixes:

- Reserve more vertical space at the bottom of `.frame`.
- Add bottom padding to hero copy.
- Move source note from bottom-left to top-left or otherwise away from navigation.
- Re-run visual check after fixing.

This is a reusable pattern: deck navigation must not compete with slide content. Inspect the first slide and at least one content-heavy slide before delivery.
