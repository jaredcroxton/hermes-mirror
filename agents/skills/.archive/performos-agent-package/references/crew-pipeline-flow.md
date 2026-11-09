# Crew — Pipeline Flow and Reporting Lines

Captured 14 June 2026 from the gstack-to-AgentOS architecture session.

## The pipeline

```
TRIGGER (client request)
  │
  ▼
PHASE 1: THINK — Brock
  Decides: real outcome, routing, definition of done
  ↓
PHASE 2: PLAN — Finn (code) / Lara (L&D) / Harry (HR) / Polly (product) / Sam (academic) / Leo (leadership)
  Reports up: "Architecture sound. Proceed."
  ↓
PHASE 3: BUILD — Bob (build) / Mira (design) / Nelly (synthesis) / Neo (sandbox setup)
  Each owns their deliverable.
  ↓
PHASE 4: REVIEW — Quinn
  Quality gate. Checks links, sources, formatting, completeness.
  PASS → proceed. BLOCK → returns to Build.
  ↓
PHASE 5: QA — Trace
  Test and debug. API responds? Page loads? Bot connects?
  WORKS → proceed. BROKEN → returns to Build with diagnosis.
  ↓
PHASE 6: SHIP — Bob
  Deploy to production. Verify live. Confirm URL.
  ↓
PHASE 7: RETRO — Pace
  Sprint state + context. Records what shipped, what blocked, what was learned.
  Stores context for next session.
  ↓
PHASE 8: SIGN-OFF — Brock
  Reviews Quinn's PASS, Trace's WORKS, Pace's summary.
  APPROVED or NEEDS WORK.
  Reports to Jared: "Here's what shipped."
```

## Reporting lines

```
                        JARED
                         │
                    ┌────┴────┐
                    │  Brock  │  CEO agent — only agent reporting directly to Jared
                    └────┬────┘
                         │
        ┌────────────────┼────────────────┐
        │                │                │
   ┌────┴────┐     ┌─────┴─────┐    ┌─────┴─────┐
   │  PLAN   │     │   BUILD   │    │  SUPPORT  │
   │  leads  │     │  agents   │    │  agents   │
   └────┬────┘     └─────┬─────┘    └─────┬─────┘
        │                │                │
   ┌────┴────┐     ┌─────┴─────┐    ┌─────┴─────┐
   │  Finn   │     │    Bob    │    │   Pace    │
   │  Lara   │     │   Mira    │    │ (context) │
   │  Harry  │     │  Nelly    │    └───────────┘
   │  Polly  │     │   Neo     │
   │   Sam   │     │  Quinn    │
   │   Leo   │     │  Trace    │
   └─────────┘     └───────────┘
```

## Phase owners

| Phase | Owner | Reports to |
|---|---|---|
| Think | Brock | Jared |
| Plan | Finn / Lara / Harry / Polly / Sam / Leo | Brock |
| Build | Bob / Mira / Nelly / Neo | Plan lead |
| Review | Quinn | Brock |
| QA | Trace | Brock |
| Ship | Bob | Brock |
| Retro | Pace | Brock |
| Sign-off | Brock | Jared |

Brock is the single agent that reports to Jared. Everyone else reports to Brock or to the Plan lead. Clean chain.

## Existing agents (keep as-is)

Brock, Lara, Bob, Mira, Harry, Nelly, Sam, Polly, Neo, Leo.

## New agents to build (4 souls)

| Agent | One job | Complexity |
|---|---|---|
| Finn | Architecture review. "Will this build work? Dependencies right?" | Light |
| Quinn | Quality inspection. "Output complete? Sources grounded? Links live?" | Light |
| Trace | Debug and test. "Why did this fail? Root cause?" | Medium |
| Pace | Sprint state + context. "Where are we? What's blocked? What happened last session?" | Light |

## Key design principle

Narrow agents perform better. One job, one context window, one definition of done. gstack splits roles this way — Crew mirrors the pattern. Brock and Bob should not wear multiple hats (strategy + review + retro, or build + deploy + debug).
