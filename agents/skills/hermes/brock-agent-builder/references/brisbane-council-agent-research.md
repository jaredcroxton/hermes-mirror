# Brisbane Council Development Agent — Research & Methodology

## Source session

30 June 2026. Brock and Jared. Triggered by Jared's mate asking about a council compliance agent for property development in Brisbane.

## Key research findings

### Brisbane planning framework

Brisbane operates under a single planning scheme — **Brisbane City Plan 2014** — governed by the **Planning Act 2016 (Qld)**. This makes it significantly simpler to build an agent for compared to NSW (128 separate LEPs/DCPs across councils).

**Assessment pathways:**
- **Code assessable:** Assessed against identified codes only. No public notification. Lower risk.
- **Impact assessable:** Assessed against all of City Plan. Public notification mandatory. Higher risk, longer timeline, refusal risk.

**Key control layers:**
1. **Zones** — what land uses are permitted (LDR, LMR, CR1 Character Residential, MU, HDR, etc.)
2. **Overlays** — additional constraints (TBC, Pre-1911, Heritage, Flood, Biodiversity, Bushfire)
3. **Neighbourhood Plans** — localised provisions that may override zone controls

### The single highest-value datapoint

**Traditional Building Character Overlay + Pre-1911 Overlay intersection.**

- Pre-1911 + TBC overlay → demolition prohibited unless structurally unsound. Near-absolute constraint.
- Pre-1946 + TBC overlay → Demolition Control Precinct. Cannot demolish or remove. Renovation must retain character.
- TBC overlay, post-1946 construction → Character code may still apply but constraints are significantly lighter.
- No TBC overlay → demolition possible even for pre-war stock.

### Brisbane open data infrastructure

Brisbane City Council publishes spatial planning data as ArcGIS FeatureServer layers under CC BY 4.0 license.

**Confirmed working endpoints:**
- Zoning overlay: `services2.arcgis.com/dEKgZETqwmDAh1rP/arcgis/rest/services/Zoning_opendata/FeatureServer/0` — 26,356 records
- TBC overlay: ArcGIS FeatureServer (separate endpoint)
- Heritage overlay, Flood overlay, Pre-1911 overlay: all available as ArcGIS layers

**Data access methods:**
- ArcGIS REST API — spatial queries by geometry. JSON response. Works in browser and via programmatic calls.
- City Plan online (ePlan) — JS SPA at `cityplan.brisbane.qld.gov.au/eplan`. Browser blocked us with 403 on 30 June. Requires Firecrawl or browser automation with residential proxies.
- Development.i — JS SPA at `developmenti.brisbane.qld.gov.au`. Loaded in browser but map search did not filter to address area. Requires Firecrawl or targeted API calls.

**Confirmed working:** ArcGIS FeatureServer REST API is the primary retrieval path. City Plan online and Development.i are secondary — usable but require JS-rendering tools.

### Property assessment methodology

The agent follows seven steps per property:
1. Geocode address to Lot/Plan + coordinates
2. Query all ArcGIS overlay layers for property polygon
3. Determine TBC + Pre-1911 + DCP status (Boolean flags)
4. Query Development.i for precedent DAs within 500m
5. Generate City Plan property report (or reconstruct from ArcGIS data)
6. Cross-reference overlays with Part 5 Tables of Assessment → Code vs Impact pathway
7. Classify risk tier (Green/Amber/Amber-Red/Red/Black) based on overlay intersection rules

### The Ashgrove test — what it proved

**Property:** 30 Jubilee Terrace, Ashgrove QLD 4060
- Solid brick, double-storey, concrete suspended slabs
- 7 bed, 5 bath, 2 car
- 820m² across **two lots**
- Listed for sale ~$2M-$2.2M (Place Newmarket)

**Three things the agent spotted that a generic report would miss:**

1. **Construction type changes everything.** Brick construction = almost certainly post-WWII (1950s-1970s). Even if the property sits inside the TBC overlay, brick post-war homes are treated differently to pre-1946 timber Queenslanders. The Character Code's constraints are significantly lighter.

2. **Two lots = subdivision trigger.** The 820m² across two lots creates subdivision potential that is the primary planning consideration. A generic property report would report the land size. The agent flags the subdivision pathway and checks minimum lot size, separate titling, and whether reconfiguration triggers Impact assessment.

3. **The agent admits what it does not know.** TBC overlay status could not be verified without City Plan lookup (which was blocked). The agent said so explicitly: "Verify TBC overlay status and confirm construction date via rates notice before committing." No guessing. This is the difference between a tool and a thinking partner.

### Paddington vs Ashgrove comparison

| | 47 Latrobe Tce, Paddington (mock) | 30 Jubilee Tce, Ashgrove (real) |
|---|---|---|
| Construction | Timber Queenslander, c. 1925 | Solid brick, 1950s-1970s |
| Pre-1911 | No | No |
| TBC overlay | YES | Unknown — needs verification |
| Demolition | Prohibited (DCP) | Possibly permitted if outside TBC |
| Lots | Single lot | Two lots — subdivision trigger |
| Development play | Renovation + rear extension | Subdivision OR demolition-rebuild OR renovation |
| Risk tier | AMBER (renovation only) | Unknown — likely AMBER or GREEN |

The Paddington mock assumed the worst case (TBC overlay present, timber construction). The Ashgrove test showed that real properties are more nuanced — and the agent must adapt its analysis to construction type, lot configuration, and verified (not assumed) overlay status.

### Output deliverables (proven format)

Four documents produced and tested this session:

1. **Excel Overview** — Five tabs. Agent architecture, planning controls matrix, risk classification, data sources with API endpoints, complete workflow steps with error handling.
2. **Executive Risk Brief (PDF)** — Seven sections. Risk framework, critical deal-breakers, decision tree, suburb heat map, agent capability summary. The document for pre-acquisition go/no-go decisions.
3. **Council-Submittable Property Report (PDF)** — Eight sections. Planning controls table, assessment pathway, character code compliance assessment, DA readiness checklist, precedent DAs, risk matrix. The document for pre-lodgement meetings.
4. **Shareable How It Works PDF** — Seven pages. Problem, methodology, CREW Context Loop, outputs, Brisbane data sources, build plan, next steps. Written for a property developer, not a technical reader.

### Agent build plan (four layers)

| Layer | What | Who | Detail |
|---|---|---|---|
| 1: Data Retrieval | ArcGIS API calls, Development.i scraping, City Plan property report reconstruction | Bob_Builder | Address in → structured data out |
| 2: Planning Knowledge | City Plan Part 5, Character Code, Heritage Code, Dwelling House Code into RAG | Nelly_Notebook | Grounded answers to "can I do X?" questions |
| 3: Agent Soul | Identity, risk classification rules, output formats, red flag hierarchy | Brock | The thinking layer — how the agent interprets planning data for a developer |
| 4: Gold Standard QA | 15-section structural audit, adversarial review, brand-context integration, context loop wiring | CREW Framework | Every agent passes before deployment |

### Agent output format (per property)

Three outputs per property:
1. **Executive Risk Brief (PDF)** — Risk tier, red flags, decision framework. The go/no-go signal.
2. **Property Planning Report (PDF)** — Full planning analysis. Ready for town planner or pre-lodgement.
3. **Portfolio Tracking (Excel)** — Properties ranked, risk tiers compared, suburb patterns, decision tracking.

### Prerequisites before build

Four things needed from the property developer:
1. Development playbook (renovate-hold, demolish-rebuild, subdivide?)
2. Target suburbs (pre-filter for overlay density)
3. Risk appetite (filter out Amber-Red or flag it?)
4. A test property with known outcome (calibrate the rules engine)

### Key design decisions

- **Start with Brisbane only.** Single council, single planning scheme, single open data platform. Expansion to other QLD councils (Gold Coast, Sunshine Coast, Ipswich) is a subsequent phase.
- **ArcGIS as primary data path.** The REST API works reliably. City Plan online and Development.i are secondary retrieval paths that require JS rendering.
- **Construction type as a first-class signal.** Brick vs timber is not cosmetic — it changes the character code implications, the demolition pathway, and the risk tier.
- **Lot configuration as a trigger check.** Multiple lots trigger subdivision assessment, which is a different DA pathway than single-lot renovation.
- **Unknown admission as a quality gate.** The agent must explicitly state what it cannot verify and where to find that information (rates notice, title search, council Practice Note).

### Pitfalls discovered

- **City Plan online blocks headless browsers (403).** Residential proxies or Firecrawl with stealth mode may be required. ArcGIS REST API is the reliable primary path.
- **Development.i map search does not filter to address on first load.** The SPA renders all applications unfiltered. The address-based filter must be applied through the UI or via a targeted API call.
- **Do not assume TBC overlay status.** Suburbs like Ashgrove have patchy character overlay coverage. Verification per property is non-negotiable.
- **Two-lot configurations are easy to miss.** Real estate listings report total land size, not lot count. The agent must check lot configuration explicitly.
- **Brisbane methodology does not transfer to other councils.** The character overlay risk engine (TBC, Pre-1911, DCP) is Brisbane-specific. Regional councils like Southern Downs have completely different overlay categories and risk profiles. Each council requires its own risk engine. See `references/council-agent-build-methodology.md`.
