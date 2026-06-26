# README Brand Leak — Fresh-Install Bug

## The bug

When a business clones the CREW GitHub repo and opens Claude Code in the repo directory, Claude reads `README.md` and `CLAUDE.md` into the session context before any skill loads. If the README contains brand identification (`"Built by PerformOS,"` founder name, product names), Claude offers that as context to the user.

The skill's Step 0 cannot prevent this. Claude has already read the README before the skill text is processed.

## The symptom

Claude says: `"I noticed the repo you installed was built by PerformOS — but I shouldn't assume. Which business are we onboarding?"`

A new business sees PerformOS assumed as their business. Even when Claude asks permission, the brand has already leaked into the conversation.

## The fix

The repo README must contain **zero brand identification**. No company names. No founder names. No brand story. No product names.

- README: technical content only (architecture, packs, installation, quality standards)
- ABOUT.md: brand story, founder, company philosophy (Claude does NOT auto-load this file)
- The repo is the installer, not a marketing asset

## Commands

```bash
# Strip brand from README
# Move to ABOUT.md
```

## Verification

```bash
grep -i "performos\|croxton\|brand" README.md  # Must return 0
```

## Date

Discovered 26 June 2026 during Mac Mini fresh-install test.
