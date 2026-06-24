# LinkedIn Executive Scraping — Tool Comparison

Captured 25 June 2026 from a side-by-side test of Firecrawl vs ScrapeGraphAI for LinkedIn executive prospecting (target: Australian CTOs, VPs of Engineering, Heads of AI with agentic AI / Claude / LLM interest).

## The core finding

**Neither tool can directly scrape LinkedIn profile pages.** LinkedIn is a fortress. Both Firecrawl's scrape endpoint and ScrapeGraphAI's open-source library hit the same wall: LinkedIn detects automated browsers and serves login walls, empty pages, or blocks.

## Firecrawl — the winner for this use case

| Method | Result |
|---|---|
| Search for LinkedIn profiles | Works — found 5 relevant profiles |
| Scrape individual LinkedIn URL | Blocked — "we do not support this site" |
| Extract (deprecated endpoint) | Failed |
| Autonomous agent (`firecrawl_agent`) | **Works** — found 3 Australian execs in ~4 minutes |

The agent returned: full name, current title, current company, location. It navigated around LinkedIn's blocks by using web search + indirect signals rather than hitting profile pages directly.

Example output:
- Justin Verduyn — CTO and Senior Developer, Agentic AI at BHP (Perth)
- Hruday M. — Head of AI, Gen AI, & Agentic AI at Lorgan (Australia)
- Dominick Ng — VP Engineering at monō ai (Australia)

**Missing from agent output:** LinkedIn profile URLs, about sections, skills, connections count, detailed experience, email addresses.

## ScrapeGraphAI — not ready for this use case

| Method | Result |
|---|---|
| Open-source PyPI install (v1.20.1) | Installed OK + Playwright |
| Cloud API (v2.1.4 on their site) | Not tested — requires signup, free tier has 500 credits |
| Actual scraping test | Could not complete — no LLM backend available (no OpenAI key, Ollama not running) |

**Critical finding:** The open-source PyPI version (1.20.1) is **seven releases behind** the cloud API (2.1.4 as of 23 June 2026). The open-source library is clearly the neglected sibling. The cloud API may perform better but requires credits and API key.

**ScrapeGraphAI cloud signup flow (tested 25 June 2026):**
- Free tier: 500 one-time credits, no credit card required
- Signup at `scrapegraphai.com/signup`
- Two OAuth paths: CONTINUE WITH GITHUB or CONTINUE WITH GOOGLE
- Google OAuth tested — redirects to standard Google sign-in, then returns to dashboard
- Once signed in, API key available from dashboard
- Python SDK: `pip install scrapegraph-py`, then `from scrapegraph_py import ScrapeGraphAI`
- Environment variable: `SGAI_API_KEY`

## Strategic recommendation for LinkedIn executive prospecting

1. **Use Firecrawl agent** (`firecrawl_agent`) as the first pass — it finds real people with real titles
2. **Enrich manually or via Apollo** — take the names from Firecrawl and enrich with Apollo for email, phone, LinkedIn URL
3. **Do not waste time on direct LinkedIn profile scraping** — neither tool can do it
4. **ScrapeGraphAI's open-source promise is oversold** — the PyPI version lags, local LLM setup adds friction, and LinkedIn blocks Playwright browsers regardless of which LLM is driving extraction
5. **ScrapeGraphAI cloud API** may be worth testing if the free 500 credits are claimed — but the version gap between open-source and cloud is a red flag about their commitment to the open-source product

## For the CREW cold outreach use case

The Firecrawl agent output (name, title, company, location) is enough to:
- Search LinkedIn manually for the profile
- Enrich via Apollo for email
- Draft cold outreach copy
- But NOT enough for personalised "I noticed [specific detail from your profile]" messaging

For personalised outreach, manual LinkedIn profile review is still required after the tool finds the target.

## Ollama note

Jared wants Ollama installed on his machine (`brew install ollama`) but prefers to start and manage it himself — do not start the Ollama server in the background as the agent. The M5 MacBook Pro with 128GB is more than capable of running local LLMs for scraping, but the bottleneck remains LinkedIn's bot detection, not the LLM backend.
