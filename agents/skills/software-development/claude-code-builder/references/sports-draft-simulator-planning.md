# Sports Draft Simulator Planning

Use when Jared wants an app plan or Claude Code brief for a game inspired by roster-draft simulators such as 82-0 or 38-0.

## Pattern to study first

Capture the reference game's loop, not just the screen layout:

1. Setup choices: mode, difficulty, draft mode, era, formation or lineup size.
2. Random constraint: spin for team plus era, club plus season, or another constrained pool.
3. Pick phase: user chooses one eligible player from that pool.
4. Placement phase: user assigns the player to an open position.
5. Fit logic: natural, related, and out-of-position modifiers.
6. Completion: repeat until lineup is full.
7. Scoring: team category scores plus overall.
8. Simulation: season result, record, grade, and shareable outcome.

## AFL adaptation lesson

For AFL, start smaller than a full squad. Use an 18-player on-field team for MVP. Add bench later.

Recommended field positions:

- BP, FB, BP
- HBF, CHB, HBF
- W, C, W
- HFF, CHF, HFF
- FP, FF, FP
- RUC, RR, ROV

Recommended game name: `23-0`, because the goal is an undefeated AFL home-and-away season.

## MVP modes

- Classic: ratings and stats visible.
- Footy IQ: ratings hidden until final review.
- Hard Mode: zero rerolls, ratings hidden, position-first default.

Draft modes:

- Club First: spin club and season, then pick any eligible player.
- Position First: choose position first, then spin club and season.

Difficulty:

- Easy: three rerolls.
- Normal: one reroll.
- Hard: zero rerolls and ratings hidden.

Era filters:

- All-time.
- 2000s+.
- 2010s+.
- Modern, 2016+.
- Current era, 2020+.

## Data model

Each player-season record should include:

```ts
{
  id: string
  name: string
  club: string
  season: number
  positions: string[]
  rating: number
  attack: number
  midfield: number
  defence: number
  ruck: number
  stats: {
    disposals: number
    goals: number
    marks: number
    tackles: number
    clearances: number
    inside50s: number
    rebound50s: number
    hitouts: number
    contestedPossessions: number
  }
}
```

Use a seed file of around 120 player-season records across 18 AFL clubs for MVP. Do not start with a full scraping pipeline.

## Position fit

- Natural position: 100 percent rating.
- Related position: 92 percent rating.
- Out of position: 75 percent rating.

Related groups:

- Defensive: BP, FB, HBF, CHB.
- Midfield: W, C, RR, ROV.
- Forward: HFF, CHF, FP, FF.
- Ruck: RUC only.

## Team scoring

Calculate:

- Overall.
- Attack.
- Midfield.
- Defence.
- Ruck.

Overall weighting:

- Attack: 30 percent.
- Midfield: 35 percent.
- Defence: 25 percent.
- Ruck: 10 percent.

Line score uses players assigned to that line and applies position fit modifiers.

## Season simulation

Simulate 23 games.

For each game:

```js
teamPower = teamOverall + randomBetween(-8, 8)
opponentPower = opponentRating + randomBetween(-6, 6)
margin = Math.round((teamPower - opponentPower) * 3.2)
```

If `margin > 0`, user wins. Otherwise user loses.

Scores:

```js
teamScore = Math.round(80 + teamPower + randomBetween(-15, 20))
opponentScore = teamScore - margin
```

Result labels:

- 23-0: Perfect season.
- 20 to 22 wins: Premiership favourite.
- 15 to 19 wins: Finals lock.
- 10 to 14 wins: Middle of the ladder.
- Under 10 wins: Rebuild needed.

## Prompt vs loop distinction

When Jared or Claude Code asks for a sports game plan, separate the **prompt** from the **loop** in plain English.

- **Prompt:** the instruction given to the builder, e.g. "Build an AFL draft game."
- **Loop:** the repeated user behaviour that makes the product playable, e.g. "Spin -> choose player -> place player -> improve team -> repeat -> simulate -> share or try again."

For game builds, the loop is more important than the prompt. If the brief only says what to build, Claude Code may produce a static picker. If the brief defines the loop, Claude Code can build a real game.

Always include three loops in the brief:

1. **Primary loop:** the repeated mechanical flow.
2. **Emotional loop:** the hope, tension, payoff, and replay driver.
3. **Strategic loop:** the trade-offs the user makes.

## Build brief requirements

The Claude Code brief must specify:

- App name and goal.
- Primary gameplay loop, not just a high-level prompt.
- Emotional loop and strategic loop.
- Screen list.
- Data model.
- Draft state model.
- Scoring functions.
- Simulation functions.
- Legal constraints.
- Mobile-first visual direction.
- Unit tests for core logic.

Recommended files:

- `app/page.tsx`
- `app/layout.tsx`
- `app/globals.css`
- `data/players.ts`
- `lib/gameLogic.ts`
- `lib/scoring.ts`
- `lib/simulation.ts`
- `components/SetupScreen.tsx`
- `components/DraftScreen.tsx`
- `components/Field.tsx`
- `components/PlayerCard.tsx`
- `components/PlacementModal.tsx`
- `components/ReviewScreen.tsx`
- `components/ResultScreen.tsx`
- `types/game.ts`

## Legal guardrails

For fan sports games:

- Do not use official logos, crests, player photos, or league brand assets.
- Use plain text club and player names only.
- Make ratings clearly game-estimated, not official.
- Include an independent fan-made disclaimer in the footer.

## Acceptance criteria

- User can complete a full draft.
- Reroll limits work.
- Hidden-ratings mode works.
- Drafted players cannot be drafted twice.
- Position fit affects team score.
- Season simulation always produces the correct game count.
- Result screen shows record, category, and match list.
- Share button copies a plain-text result.
- Mobile layout works at 390px width.
- No official sports branding assets are used.
