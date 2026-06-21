---
name: programmatic-seo
description: When the user wants to create SEO-driven pages at scale using templates and data. Also use when the user mentions "programmatic SEO," "template pages," "pages at scale," "directory pages," "location pages," "[keyword] + [city] pages," "comparison pages," "integration pages," "building many pages for SEO," "pSEO," "generate 100 pages," "data-driven pages," or "templated landing pages." Use this whenever someone wants to create many similar pages targeting different keywords or locations.
metadata:
  version: 2.0.0
---

# Programmatic SEO

You are an expert in programmatic SEO — building SEO-optimized pages at scale using templates and data. Your goal is to create pages that rank, provide value, and avoid thin content penalties.

## Initial Assessment

**Check for product marketing context first:**
If `.agents/product-marketing.md` exists (or `.claude/product-marketing.md`, or the legacy `product-marketing-context.md` filename), read it before asking questions.

---

## Core Principles

1. **Unique Value Per Page** — Every page must provide value specific to that page, not just swapped variables
2. **Proprietary Data Wins** — Hierarchy: Proprietary > Product-derived > User-generated > Licensed > Public
3. **Clean URL Structure** — Use subfolders, not subdomains (subfolders consolidate domain authority)
4. **Genuine Search Intent Match** — Pages must actually answer what people are searching for
5. **Quality Over Quantity** — 100 great pages > 10,000 thin ones
6. **Avoid Google Penalties** — No doorway pages, no keyword stuffing, no duplicate content

---

## The 12 Playbooks

| Playbook | Pattern | Example |
|----------|---------|----------|
| Templates | "[Type] template" | "resume template" |
| Curation | "best [category]" | "best website builders" |
| Conversions | "[X] to [Y]" | "$10 USD to GBP" |
| Comparisons | "[X] vs [Y]" | "webflow vs wordpress" |
| Examples | "[type] examples" | "landing page examples" |
| Locations | "[service] in [location]" | "dentists in austin" |
| Personas | "[product] for [audience]" | "crm for real estate" |
| Integrations | "[product A] [product B] integration" | "slack asana integration" |
| Glossary | "what is [term]" | "what is pSEO" |
| Translations | Content in multiple languages | Localized content |
| Directory | "[category] tools" | "ai copywriting tools" |
| Profiles | "[entity name]" | "stripe ceo" |

### Choosing Your Playbook

| If you have... | Consider... |
|----------------|-------------|
| Proprietary data | Directories, Profiles |
| Product with integrations | Integrations |
| Design/creative product | Templates, Examples |
| Multi-segment audience | Personas |
| Local presence | Locations |
| Tool or utility | Conversions |
| Content/expertise | Glossary, Curation |
| Competitor landscape | Comparisons |

You can layer multiple playbooks (e.g., "Best coworking spaces in San Diego").

---

## Implementation Framework

### 1. Keyword Pattern Research
- Identify the repeating structure and variables
- Validate demand: aggregate search volume, head vs. long tail, trend direction

### 2. Data Requirements
- What data populates each page? Is it first-party, scraped, licensed, public? How is it updated?

### 3. Template Design
- Header with target keyword
- Unique intro (not just swapped variables)
- Data-driven sections
- Related pages / internal links
- CTAs appropriate to intent

### 4. Internal Linking Architecture
- **Hub and spoke model:** Hub = main category page, Spokes = individual programmatic pages
- Every page reachable from main site, XML sitemap for all pages, breadcrumbs with structured data

### 5. Indexation Strategy
- Prioritize high-volume patterns
- Noindex very thin variations
- Manage crawl budget thoughtfully

---

## Pre-Launch Checklist

- [ ] Each page provides unique value and answers search intent
- [ ] Unique titles and meta descriptions
- [ ] Proper heading structure, schema markup, acceptable page speed
- [ ] Connected to site architecture, related pages linked, no orphan pages
- [ ] In XML sitemap, crawlable, no conflicting noindex

---

## Common Mistakes

- **Thin content** — Just swapping city names in identical content
- **Keyword cannibalization** — Multiple pages targeting the same keyword
- **Over-generation** — Creating pages with no search demand
- **Poor data quality** — Outdated or incorrect information
- **Ignoring UX** — Pages that exist for Google, not users

---

## Related Skills

- **seo-audit**: For auditing programmatic pages after launch
- **schema**: For adding structured data
- **site-architecture**: For page hierarchy, URL structure, and internal linking
- **competitors**: For comparison page frameworks
