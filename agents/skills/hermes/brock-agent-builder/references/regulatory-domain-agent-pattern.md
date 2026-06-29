# Regulatory Domain Agent Design Pattern

## When to use this reference

When designing an agent that sits on top of a government regulatory framework — council planning controls, employment legislation, building codes, licensing regimes, or any structured public-sector rule system. The pattern was proven on Brisbane City Council planning controls (30 June 2026) and generalises to any jurisdiction with open data.

## The core insight

Regulatory agents are NOT general web scrapers. They are structured data retrieval engines that query a finite number of predictable public data sources, then apply a rules engine derived from the governing legislation. The intelligence is in the cross-referencing, not the scraping.

## Design sequence (proven)

### Phase 1: Map the regulatory landscape

Before designing the agent, answer:

1. **What is the governing legislation?** (e.g. Planning Act 2016 for Qld development)
2. **What is the planning scheme / regulatory instrument?** (e.g. Brisbane City Plan 2014)
3. **What are the assessment pathways?** (e.g. Code assessable vs Impact assessable)
4. **What are the control layers?** (e.g. Zones, Overlays, Neighbourhood Plans)
5. **Which control layer is the single highest-value datapoint?** (e.g. Traditional Building Character Overlay — the Boolean that determines demolition feasibility)
6. **What is the public-facing DA/case register?** (e.g. Development.i)
7. **What open data exists?** (e.g. ArcGIS FeatureServer with CC BY 4.0 license)

### Phase 2: Identify structured data sources

Every regulatory domain has structured data somewhere. Find it before resorting to scraping:

- **Spatial data:** ArcGIS, GeoServer, WFS/WMS endpoints. Look for open data portals with REST APIs.
- **Case/application registers:** Most councils use the same few software platforms. The search interface usually hits an API.
- **Legislation/planning scheme text:** Usually PDF or structured HTML. Extract once, store in RAG, query per case. Do not live-scrape the same documents repeatedly.
- **Heritage/character registers:** Often separate databases with their own search interfaces.
- **State-level registers:** For things that cross local government boundaries (heritage listings, PDAs, state significant developments).

### Phase 3: Build the risk classification engine

The regulatory framework IS the rules engine. Translate the legislation into Boolean logic:

```
IF Pre-1911 Overlay = YES AND TBC Overlay = YES → Risk = RED (demolition prohibited)
IF TBC Overlay = YES AND Construction Date < 1946 → Risk = AMBER (renovation only, character compliance)
IF TBC Overlay = NO → Risk = GREEN (standard residential, demolition possible)
```

The risk tiers must be:
- **Grounded in the legislation** — every tier maps to specific clauses in the planning scheme
- **Boolean-first** — the highest-value signals are binary (in overlay / not in overlay)
- **Intersectional** — risk is determined by overlay combination, not single-layer analysis
- **Actionable** — each tier produces a clear acquisition/development recommendation

### Phase 4: Design the output hierarchy

Regulatory agents need three output tiers, not one:

| Tier | Format | Audience | Purpose |
|---|---|---|---|
| **1. Excel Overview** | Spreadsheet with tabs | Internal — developer/operator | Agent architecture, data sources, control matrix, workflow, risk tiers. The operational spec. |
| **2. Executive Risk Brief** | PDF, 6-8 sections | Decision-maker | Pre-acquisition filter. Risk framework, red flags, decision tree, suburb heat map. Answers: "Should I buy this?" |
| **3. Council-Submittable Report** | PDF, 8+ sections | Council / town planner | Planning controls analysis, code compliance table, DA readiness checklist, precedent cases, risk matrix. Answers: "What do I need to lodge?" |

The three documents together form the complete agent spec. They prove the agent concept before a single line of retrieval code is written.

### Phase 5: Fit into the ecosystem

Regulatory agents follow the same specialist pattern:

| Harry_HR (template) | Council Agent (this session) |
|---|---|
| "Which market?" | "Which address?" |
| Sourced legislation per country | Sourced planning controls per LGA |
| What you can/can't do + risks | What you can/can't build + DA triggers |
| Output: structured advice doc | Output: property intel report + risk brief + council report |

Build path:
1. **Brock** specs the agent (research, risk framework, output design)
2. **Bob_Builder** builds the retrieval engine (API calls, scraping pipelines, data normalisation)
3. **Nelly_Notebook** ingests the regulatory documents (planning scheme text into RAG)
4. The agent gets a soul file, a profile, lives in the ecosystem

## Brisbane-specific findings (reference)

These are the data sources and control layers discovered for Brisbane City Council. The pattern generalises — every jurisdiction has equivalents.

### Planning framework
- **Governing Act:** Planning Act 2016 (Qld)
- **Planning Scheme:** Brisbane City Plan 2014 (Version 14+)
- **Assessment Rules:** Development Assessment Rules (DA Rules)
- **Pathways:** Code assessable (no public notification) vs Impact assessable (public notification mandatory)

### Control layers (highest to lowest risk)
1. **Pre-1911 Building Overlay** — absolute demolition prohibition. Cannot demolish unless structurally unsound.
2. **Traditional Building Character Overlay** — Demolition Control Precinct. Pre-1946 houses cannot be demolished. Renovation must meet Character Code.
3. **Heritage Overlay** — individually listed places and heritage precincts. Conservation of significance required.
4. **Flood Overlay** — defined flood level, floor level requirements, flood assessment for basements.
5. **Commercial Character Building Overlay** — retention and complementary design.
6. **Biodiversity Overlay** — vegetation management, tree removal.
7. **Neighbourhood Plans** — localised provisions that may override zone controls.
8. **Priority Development Areas** — state-declared, different assessment pathway.

### Data sources (Brisbane-specific, CC BY 4.0)
- **ArcGIS FeatureServer REST API:** `services2.arcgis.com/dEKgZETqwmDAh1rP/arcgis/rest/services/Zoning_opendata/FeatureServer/0` — 26,356 records. Query by geometry.
- **Development.i:** `developmenti.brisbane.qld.gov.au` — DA register. Search by address, application number, map.
- **City Plan online:** `cityplan.brisbane.qld.gov.au/eplan` — Property lot reports, interactive mapping, full planning scheme text.
- **Local Heritage Places:** `heritage.brisbane.qld.gov.au` — Individual listings, significance statements.
- **Economic Development Queensland:** State PDA register.

### Risk tier logic (Brisbane-specific)
| Tier | Criteria | Path | Timeline |
|---|---|---|---|
| GREEN | Standard zone, no overlays, post-1946 | Code assessable | 2-4 months |
| AMBER | TBC overlay, NOT Pre-1911 | Code with character compliance | 4-8 months |
| AMBER/RED | TBC + potential triggers + flood | May trigger Impact | 8-14 months |
| RED | Pre-1911 + TBC, or heritage listed | Impact likely, refusal risk | 12-18+ months |
| BLACK | Pre-1911 + TBC + heritage listed | Demolition prohibited | 18+ months, likely refusal |

### The single highest-value datapoint
**Pre-1911 + TBC intersection.** If both are YES, demolition is effectively impossible. This Boolean alone is worth more than any other planning intel at acquisition stage. The agent's primary job is to surface this intersection immediately.

## Anti-patterns

- **Starting with scraping.** Find the structured data first. Brisbane's ArcGIS open data makes scraping unnecessary for spatial queries.
- **Building for every council at once.** Start with one jurisdiction. Prove the pattern. Then expand.
- **Treating all overlays equally.** The risk hierarchy matters. Pre-1911 and TBC are deal-breakers. Flood is a cost factor. Biodiversity is usually manageable.
- **Outputting raw data without synthesis.** The value is in the cross-referencing — overlay × zone × precedent × assessment pathway. Not in listing overlays.
- **Missing the pre-acquisition use case.** The agent's core value is BEFORE capital is committed. It is a filter, not a lodgement tool.
