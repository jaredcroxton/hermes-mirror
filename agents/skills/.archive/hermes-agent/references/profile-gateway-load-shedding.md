# Profile gateway load shedding on macOS

Use this when Hermes feels slow because too many specialist profile gateways are always running.

## Why it helps
Each profile-backed specialist can keep its own Hermes Python process and gateway alive. On a memory-pressured Mac, leaving many profiles running at once adds latency even before any real task work starts.

## Quick triage
1. Check what is running:
   `hermes profile list`
2. Stop non-essential specialist gateways:
   `hermes --profile <name> gateway stop`
3. Stop the default gateway if needed:
   `hermes gateway stop`
4. Start only the profile you need:
   `hermes --profile <name> gateway start`
5. Re-check:
   `hermes profile list`

## Example
```bash
hermes --profile laralearning gateway stop
hermes --profile nellynotebook gateway stop
hermes --profile samstudynerd gateway stop
hermes --profile pollyperformos gateway stop
hermes --profile harryhr gateway stop
hermes --profile atticuscounsel gateway stop
```

Keep the default profile and the one specialist you actively need. Add others back only when required.

## Decision rule
If the user is actively working through one main lane, prefer a lean live stack over keeping every specialist always on.

## Verification
`hermes profile list` should show fewer profiles with `Gateway running`.
