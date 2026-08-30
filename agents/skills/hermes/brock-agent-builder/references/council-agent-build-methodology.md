# Council Agent Build — Methodology and Transfer Lessons

## Source sessions

30 June 2026. Two council agents built in one session: Brisbane (Paddington mock) and Southern Downs (Lot 11 Dight Road real property).

## The Critical Transfer Lesson

**The Brisbane methodology does not transfer to other councils.** Each council has its own planning scheme, its own overlay categories, its own data infrastructure, and its own risk profile. The agent's risk engine must be tuned to the specific council.

### Brisbane Risk Engine (Metropolitan)
1. TBC overlay → demolition prohibited?
2. Pre-1911 → absolute retention?
3. Heritage → individually listed?
4. Flood → basement trigger?
5. Neighbourhood plan → height limits?

### Southern Downs Risk Engine (Regional)
1. Bushfire BAL → construction cost premium?
2. Biodiversity → clearing blocked?
3. Mining tenement → surface access restricted?
4. Dwelling entitlement → how many?
5. Minimum lot size → subdivision possible?

### What Transfers
- CREW Context Loop (Step 0 read, Final Step write)
- Gold-standard output formats (Excel, Risk Brief PDF, Property Report PDF)
- Assessment pathway logic (Code vs Impact — same under Planning Act 2016)
- The 7-layer methodology (see below)

### What Does Not Transfer
- The risk engine rules
- The overlay categories
- The data access methods (ArcGIS API vs PDF maps vs IntraMaps)
- The primary deal-breaker questions
- The development typology (400m² lots vs 50-hectare lots)

## The 7-Layer Methodology for Council Agent Builds

When building a council agent for a new local government area, follow this sequence:

**Layer 1: Council and legislation.** Confirm the exact council name (do not assume user's name is correct — Darling Downs is a region, not a council). Identify the planning scheme, governing act, and assessment framework.

**Layer 2: Property details.** Find actual Lot/Plan, land size, existing development, construction type, real estate history. Use realestate.com.au, Domain, property.com.au, and council records.

**Layer 3: Overlay mapping.** Identify every overlay in the planning scheme. Map which ones apply to this property type. Bushfire, biodiversity, flood, heritage, mining, water catchments, agricultural, airport environs, extractive resources. Determine which is the PRIMARY risk factor for this council.

**Layer 4: DA precedents.** Find actual development applications nearby. What was approved? What was refused? What conditions were imposed? Use council DA tracking, Planning Alerts, and eTrack.

**Layer 5: Entitlements and rules.** Determine dwelling entitlements, minimum lot sizes, subdivision rules, and zone-specific codes. Check council fact sheets and planning scheme codes.

**Layer 6: Risk classification.** Apply the council-specific risk engine. Classify the property into Green/Amber/Amber-Red/Red/Black based on overlay intersection. Name what is verified vs what is unknown.

**Layer 7: Document production.** Produce three gold-standard documents: Excel overview, Executive Risk Brief PDF, Property Planning Report PDF.

## Verified Council Data Patterns

### Brisbane City Council
- Planning scheme: City Plan 2014 (interactive ePlan, v14+)
- Data access: ArcGIS FeatureServer REST API (CC BY 4.0)
- DA tracking: Development.i (SPA)
- Primary risk factor: TBC + Pre-1911 overlay intersection
- Lot typology: 400-800m² residential

### Southern Downs Regional Council
- Planning scheme: Southern Downs Planning Scheme v5 (9.3MB PDF) + draft scheme pending
- Data access: TechnologyOne IntraMaps (JS web app) + PDF overlay maps
- DA tracking: eTrack (TechnologyOne) + Planning Alerts
- Primary risk factor: Bushfire BAL rating
- Lot typology: 1,000m² to 50+ hectares rural
- Council contact: 1300 697 372, mail@sdrc.qld.gov.au
- Online mapping: sdrc.spatial.t1cloud.com/spatial/intramaps/
- eTrack: sdrc-web.t1cloud.com/T1PRDefault/WebApps/eProperty/

## Pitfall: Verifying Council Names

Do not assume the user's council name is correct. "Darling Downs Council" does not exist — the Darling Downs is a region, not a local government. The council that governs Rosenthal Heights is Southern Downs Regional Council. Always verify the council name against the LGA boundary for the property address before building the agent.

## Pitfall: Assuming API Access

Brisbane's ArcGIS REST API is the exception, not the norm. Most regional Queensland councils publish planning data as PDF maps and use TechnologyOne IntraMaps for online mapping. The agent must be built for the data infrastructure that exists, not the infrastructure you wish existed. PDF parsing and IntraMaps scraping are the regional reality.

## Pitfall: Assuming Character Overlays Exist

Character overlays (TBC, DCP, Pre-1911) are a Brisbane-specific planning tool. They do not exist in most regional Queensland councils. Building a character-based risk engine for a regional council is the wrong architecture. Verify the overlay categories in the specific planning scheme before designing the risk engine.
