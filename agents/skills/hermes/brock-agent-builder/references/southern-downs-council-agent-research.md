# Southern Downs Regional Council — Research Addendum

## Source session

30 June 2026. Jared provided 11 Dight Road, Rosenthal Heights, referring to "Darling Downs Council." Research confirmed the correct council is **Southern Downs Regional Council** (Darling Downs is the region name, not a council name).

## Critical Discovery: Brisbane Methodology Does Not Transfer

The Brisbane council agent methodology is built on a **character overlay risk engine** (TBC, Pre-1911, DCP). Southern Downs has **no character overlays of any kind**. The risk engine must be completely different.

### Brisbane vs Southern Downs — Key Differences

| Dimension | Brisbane | Southern Downs |
|---|---|---|
| Character overlays | TBC, Pre-1911, DCP | NONE. Heritage only. |
| Primary risk factor | Demolition prohibition (character) | Bushfire hazard (BAL rating) |
| Data infrastructure | ArcGIS FeatureServer REST API | TechnologyOne IntraMaps + PDF maps |
| DA tracking | Development.i | eTrack + Planning Alerts |
| Planning scheme | City Plan 2014 (interactive ePlan) | Southern Downs PS v5 (9.3MB PDF) |
| Lot sizes | 400-800m² | 1,000m² to 50+ hectares |
| Key overlays | TBC, Pre-1911, Heritage, Flood, Neighbourhood Plans | Bushfire, Biodiversity, Flood, Water Catchments, Mining Tenements, Agricultural Resources, Airport Environs, Extractive Resources |
| Development questions | Can I demolish? Can I extend? | How many dwellings? Can I subdivide? What BAL rating? |

### Southern Downs Planning Framework

**Council:** Southern Downs Regional Council
**Planning Scheme:** Southern Downs Planning Scheme (Version 5), 9.3MB PDF
**Governing Act:** Planning Act 2016 (Qld) — same legislation as Brisbane but different local planning scheme
**Assessment Pathways:** Code assessable vs Impact assessable (same structure under the Act)
**Online Mapping:** TechnologyOne IntraMaps at sdrc.spatial.t1cloud.com/spatial/intramaps/
**DA Tracking:** eTrack at sdrc-web.t1cloud.com/T1PRDefault/WebApps/eProperty/
**Planning Alerts:** planningalerts.org.au/authorities/southern_downs/ (accessible feed of recent DAs)

### Regional Overlay Categories

1. **Bushfire Hazard Overlay** — BAL ratings. The single most important overlay for rural properties. BAL-40 or BAL-FZ can add $50K-$150K+ to construction costs.
2. **Biodiversity Areas Overlay** — Essential habitat, vegetation corridors, koala habitat. Can block development on portions of the lot.
3. **Flood Hazard Overlay** — Defined flood levels, habitable floor requirements.
4. **Heritage Overlay** — Local heritage places and precincts. Limited in rural areas.
5. **Water Resources Catchments** — Watercourse buffers, riparian corridors.
6. **Mining Tenements** — Active mining or exploration permits. Can restrict surface development.
7. **Agricultural Resources** — Good Quality Agricultural Land (GQAL) classification. May restrict subdivision.
8. **Airport Environs** — Height restrictions, noise contours near Warwick Airport.
9. **Extractive Resources** — Buffers around quarries and mines.

### Agent Adaptation Requirements

The agent must:
1. **Replace character risk engine with bushfire risk engine.** BAL rating replaces TBC overlay as the primary deal-breaker check.
2. **Parse PDF maps instead of querying ArcGIS APIs.** Southern Downs publishes all overlay maps as downloadable PDFs.
3. **Scrape TechnologyOne IntraMaps** instead of querying ArcGIS FeatureServer.
4. **Use Planning Alerts as primary DA feed** instead of Development.i (eTrack is also available but less accessible programmatically).
5. **Add dwelling entitlement logic.** Rural zone codes restrict dwelling numbers. Minimum lot sizes for subdivision must be checked against the specific precinct.
6. **Add agricultural land classification checks.** GQAL can block subdivision proposals.

### 11 Dight Road, Rosenthal Heights — Verified Facts (30 June 2026)

- Property is **Lot 11 Dight Road** (not street number 11 — rural lots use lot numbers)
- **Land size: 506,224 m² (50.6 hectares)** — confirmed via realestate.com.au
- **Existing house on the property** — confirmed
- Median house price in Rosenthal Heights area: ~$790,000
- Agent: Leanne Cameron, LJ Hooker Warwick
- Neighbouring lots: Lot 2 (505,976 m²), Lot 4 (505,976 m²), 164 Dight Rd (24,056 m²)
- School catchments: Warwick West State School, Warwick State High School

### Dight Road Precedent

- **8-stage, 49-lot rural residential subdivision approved on Dight Road**
- This is the single most significant planning precedent for the area
- Demonstrates Council willingness to approve rural residential subdivision
- Conditions from this approval are the benchmark for any future development on Lot 11
- Recent DAs nearby are predominantly private certification building works (sheds, carports, dwelling repairs)

### 10 Critical Unknowns (Priority Order)

1. Zone and precinct (Rural A, B, C, or Rural Residential)
2. Bushfire BAL rating (BAL-40+ may render development uneconomical)
3. Biodiversity overlay (essential habitat could block development)
4. Dwelling entitlement under Rural Zone Code
5. Flood hazard (watercourse crossing?)
6. Heritage listing of existing dwelling
7. Mining tenements (active leases or exploration permits)
8. Agricultural land classification (GQAL)
9. Subdivision conditions from the 49-lot Dight Road approval
10. Draft planning scheme impact (new scheme endorsed, awaiting finalisation)

### Data Access Limitations

- **TechnologyOne IntraMaps** is a JS web application. Scraping or browser automation required (similar to Development.i).
- **PDF overlay maps** are static. Spatial cross-referencing requires manual coordinate matching or OCR.
- **No ArcGIS REST API.** The open data infrastructure that makes Brisbane viable does not exist in Southern Downs.
- **eTrack** is a TechnologyOne web form. Search by application number or property. Not designed for programmatic access.
- **Planning Alerts** is the most accessible real-time DA feed but is a third-party aggregator.

### Build Implications

- The Southern Downs agent requires **more manual verification steps** than the Brisbane agent
- PDF parsing adds complexity that Brisbane's API-based approach avoids
- The agent should default to **flagging unknowns** rather than assuming overlay status — especially bushfire BAL
- Council direct enquiry (phone/email) should be a recommended step in the agent's output for properties with unverified overlays
- Expansion to other regional QLD councils (Western Downs, Toowoomba, Goondiwindi) follows the same adaptation pattern

### Deliverables Produced for Southern Downs

Three documents adapted from the Brisbane template:
1. Excel Overview — Southern Downs edition with regional overlays, bushfire risk tiers, comparison table
2. Executive Risk Brief PDF — Bushfire-focused risk framework, Dight Road context, decision tree
3. Property Planning Report PDF — 11 Dight Road mock report with provisional overlay assessment, dwelling entitlement analysis, BAL table, DA readiness checklist
