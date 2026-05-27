# Bob profile auth for GitHub and Vercel

Use this when Bob_Builder can build locally but fails at GitHub push or Vercel deploy.

## Core rule

Bob runs inside the `bobbuilder` Hermes profile with an isolated profile home:

- profile env: `~/.hermes/profiles/bobbuilder/.env`
- profile home: `~/.hermes/profiles/bobbuilder/home`

Do not assume host-shell auth carries across to Bob.

## What to verify

Check both auth paths from Bob's profile context:

```bash
HOME=/Users/jc/.hermes/profiles/bobbuilder/home gh auth status
HOME=/Users/jc/.hermes/profiles/bobbuilder/home vercel whoami
```

A host-level success like `gh auth status` or `vercel whoami` from the main shell is not enough.

## Durable fix pattern

If Bob cannot push or deploy because profile auth is missing:

1. Ensure Bob has token-based auth in `~/.hermes/profiles/bobbuilder/.env`.
2. Prefer env-driven auth for automation:
   - `GH_TOKEN`
   - `GITHUB_TOKEN`
   - `VERCEL_TOKEN`
3. Restart Bob's gateway after updating the profile env.

## Why this matters

Observed failure mode:
- GitHub host login missing inside Bob profile
- Vercel credentials missing inside Bob profile
- Build succeeded but publish/deploy failed

Working pattern:
- `GH_TOKEN` in Bob profile env satisfied GitHub CLI
- `VERCEL_TOKEN` in Bob profile env satisfied Vercel CLI
- gateway restart picked up the new env

## Notes

- A stale default GitHub account entry in Bob's isolated home can still show a warning in `gh auth status`. If `GH_TOKEN` is active and Git operations work, that warning alone is not the blocker.
- Capture the fix as profile-auth setup. Do not encode a lasting claim that Bob or Vercel is broken.