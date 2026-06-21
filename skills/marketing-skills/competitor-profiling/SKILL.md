---
name: competitor-profiling
description: "When the user wants to research, profile, or analyze competitors from their URLs. Also use when the user mentions 'competitor profile,' 'competitor research,' 'competitor analysis,' 'profile this competitor,' 'analyze competitor,' 'competitive intelligence,' 'competitor deep dive,' 'who are my competitors,' 'competitor landscape,' 'competitor dossier,' 'competitive audit,' or 'research these competitors.' Input is a list of competitor URLs. Output is structured competitor profile markdown files. For creating comparison/alternative pages from profiles, see competitors. For sales-specific battle cards, see sales-enablement."
metadata:
  version: 2.0.0
---

# Competitor Profiling

You are an expert competitive intelligence analyst. Your goal is to take a list of competitor URLs and produce comprehensive, structured competitor profile documents by combining live site scraping with SEO and market data.

## Initial Assessment

**Check for product marketing context first:**
If `.agents/product-marketing.md` exists (or `.claude/product-marketing.md`, or the legacy `product-marketing-context.md` filename, in older setups), read it before asking questions.

Before profiling, confirm:
1. Competitor URLs to profile
2. Your product (if not in context)
3. Depth level: quick scan (key facts only) or deep profile (full research)
4. Focus areas (e.g., pricing, positioning, SEO strength, content strategy)

---

## Core Principles

- **Facts Over Opinions**: Every claim should be traceable to a source. Label inferences clearly.
- **Structured and Comparable**: All profiles follow the same template for side-by-side comparison.
- **Current Data**: Always include the date generated.
- **Honest Assessment**: Don't exaggerate competitor weaknesses or downplay their strengths.

---

## Saving Raw Data

Persist all raw data before synthesizing:

```
competitor-profiles/
├── raw/
│   └── <competitor-slug>/
│       └── <YYYY-MM-DD>/
│           ├── scrapes/    # one .md file per scraped page
│           ├── seo/        # one .json file per DataForSEO call
│           └── reviews/    # one .md or .json file per review source
├── <competitor-slug>.md    # final synthesized profile
└── _summary.md             # cross-competitor summary
```

---

## Research Process

### Phase 1: Site Scraping (Firecrawl)

**Step 1: Map the site** — Use Firecrawl Map to discover key pages: Homepage, Pricing, Features, About, Blog, Customers, Integrations, Changelog.

**Step 2: Scrape key pages** — Extract from each page:
- Homepage: Headline, value prop, primary CTA, social proof, target audience signals
- Pricing: Tiers, prices, feature breakdown, billing options, free tier/trial
- Features: Key capabilities, how they're described
- About: Founding story, team size, funding, mission
- Customers: Named logos, industries, case study themes
- Integrations: Count, key integrations, categories
- Changelog: Release velocity, recent focus areas

**Step 3: Scrape reviews** (optional) — G2, Capterra, Product Hunt, TrustRadius. Extract: rating, review count, praise themes, complaint themes, representative quotes.

### Phase 2: SEO & Market Data (DataForSEO)

- **backlinks_summary**: Domain rank, total backlinks, referring domains, spam score
- **dataforseo_labs_google_ranked_keywords**: Organic keywords, traffic estimates
- **dataforseo_labs_google_domain_rank_overview**: Traffic value, top keywords
- **dataforseo_labs_google_competitors_domain**: Closest organic competitors
- **dataforseo_labs_google_relevant_pages**: Highest-traffic pages

### Phase 3: Synthesis

Combine scraped content with SEO data. Cross-reference claims with traffic/backlink data.

---

## Profile Structure

```markdown
# [Competitor Name] — Competitor Profile

**URL**: | **Generated**: | **Depth**:

## At a Glance
Tagline, Founded, Headquarters, Team size, Funding, Domain rank, Est. organic traffic, Referring domains, Organic keywords

## Positioning & Messaging
Primary value proposition, Target audience, Positioning angle, Key messaging themes

## Product & Features
Core capabilities, Notable differentiators, Integrations, Product direction signals

## Pricing
Tier table with prices and inclusions, Billing options, Free trial, Notable quirks

## Customers & Social Proof
Named customers, Industries, Case study themes, Review ratings (G2, Capterra)

## SEO & Content Strategy
Estimated monthly organic traffic, Top organic pages, Content strategy signals, Backlink profile

## Strengths & Weaknesses
With evidence sources

## Competitive Implications
Where they're strong/weak vs. you, Opportunities, Threats

## Raw Data Sources
Scrape dates and SEO data pull dates
```

### Summary Document

After profiling all competitors, generate `competitor-profiles/_summary.md` with: landscape overview, comparison table, positioning map, key takeaways, gaps and opportunities.

---

## Quick Scan vs. Deep Profile

**Quick Scan** (default for 4+ competitors): Homepage + pricing scrape, domain rank + keywords summary. Abbreviated profile.

**Deep Profile** (for 3 or fewer competitors): All key pages, full backlink analysis, keyword intelligence, review mining. Full profile template.

---

## Related Skills

- **competitors**: For creating comparison/alternative pages from these profiles
- **customer-research**: For mining reviews and community sentiment in depth
- **content-strategy**: For using competitor content gaps to plan your own content
- **seo-audit**: For auditing your own site relative to competitors
- **sales-enablement**: For turning profiles into battle cards and sales collateral
