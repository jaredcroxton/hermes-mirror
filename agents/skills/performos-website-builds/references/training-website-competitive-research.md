# Training Website Competitive Research Methodology

## When to use

When building or redesigning a training/workshop landing page and the user needs competitive intelligence on how top training sites structure their pages, drive traffic, convert visitors, and use video.

## Research targets

Target 8-10 training websites across these categories:

| Category | Examples |
|---|---|
| Marketplace platforms | Maven (maven.com) |
| Enterprise training | Reforge (reforge.com), Section (sectionschool.com) |
| Career bootcamps | General Assembly (generalassemb.ly), Le Wagon (lewagon.com) |
| Creative/coding courses | SuperHi (superhi.com), IDEO U (ideou.com) |
| Challenge-based | Ship 30 for 30 (ship30for30.com) |
| Studio/agency training | AJ&Smart (ajsmart.com) |
| Direct competitor (same format) | A specific workshop page on Maven matching the user's format |

## Research methodology

### Phase 1: Surface scrape (web_extract)

Scrape all 10 homepages and key landing pages. Extract:
- Hero headline and subheadline
- Page section structure (top to bottom)
- CTA button text and placement
- Pricing model and display
- Social proof elements (testimonials, logos, numbers)
- Video presence and type
- Navigation structure

### Phase 2: Pattern extraction

Across all 10 sites, identify:

1. **Universal page structure.** What sections appear in 7+/10 sites? This is the non-negotiable template.
2. **Traffic patterns.** How do they drive visitors? Four patterns to map:
   - Free lead magnet → email nurture → book
   - Content ecosystem (YouTube, blog, podcast) → organic → book
   - Google Ads → dedicated landing page → book
   - Community (Discord, Skool) → word of mouth → book
3. **Conversion architecture.** The booking funnel. Ad → landing page → checkout → confirmation → reminder sequence.
4. **Video strategy.** What videos appear? Length, purpose, placement. Five types to catalogue.
5. **Copy patterns.** Headline formulas, CTA text, price anchoring language.

### Phase 3: Direct comparator deep dive

Find the single closest competitor (same format, same audience, similar price point) and extract their full workshop page: headline, outcomes, agenda with timings, instructor bio, testimonials, FAQ, CTA placement.

### Phase 4: Ad strategy synthesis

From the patterns, synthesise:
- Keywords to target
- Ad copy templates
- Landing page message-match requirements
- Retargeting approach

## Deliverable

A single markdown file on the user's Desktop with:

```
├── The 10 sites analysed (table: name, model, price range)
├── Universal page structure (7-section template)
├── Traffic patterns (4 types with examples)
├── Booking funnel (step by step)
├── Video strategy (5 types, lengths, purposes)
├── Landing page copy patterns (headlines, CTAs, price anchoring)
├── Recommended page structure for the user's product
├── Ad strategy (keywords, copy, message match)
└── Key takeaways (5-10 actionable bullets)
```

## Pitfalls

- **Don't just scrape homepages.** The real conversion intelligence is on individual workshop/course landing pages. Scrape those too.
- **Don't skip the direct comparator.** Finding one workshop page that matches the user's format (same duration, same audience, similar price) is worth more than all 10 homepages combined.
- **Don't produce design recommendations.** This is structure and conversion research. Design decisions belong to the user's build agent or designer.
- **Price anchoring is critical.** Always extract competitor pricing and present it in a comparison table. The gap between the user's price and the market IS the conversion copy.
