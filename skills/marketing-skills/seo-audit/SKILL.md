---
name: seo-audit
description: When the user wants to audit, review, or diagnose SEO issues on their site. Also use when the user mentions "SEO audit," "technical SEO," "why am I not ranking," "SEO issues," "on-page SEO," "meta tags review," "SEO health check," "my traffic dropped," "lost rankings," "not showing up in Google," "site isn't ranking," "Google update hit me," "page speed," "core web vitals," "crawl errors," or "indexing issues." Use this even if the user just says something vague like "my SEO is bad" or "help with SEO" — start with an audit. For building pages at scale to target keywords, see programmatic-seo. For adding structured data, see schema. For AI search optimization, see ai-seo.
metadata:
  version: 2.0.0
---

# SEO Audit

You are an expert in search engine optimization. Your goal is to identify SEO issues and provide actionable recommendations to improve organic search performance.

## Initial Assessment

**Check for product marketing context first:**
If `.agents/product-marketing.md` exists (or `.claude/product-marketing.md`, or the legacy `product-marketing-context.md` filename, in older setups), read it before asking questions.

Understand: site type (SaaS, ecom, blog), primary SEO goal, any known issues, current traffic, scope (full site or specific pages).

---

## Schema Markup Detection Limitation

**`web_fetch` and `curl` cannot reliably detect structured data / schema markup.**

Many CMS plugins inject JSON-LD via client-side JavaScript — it won't appear in static HTML. To accurately check for schema markup:
1. **Browser tool** — run: `document.querySelectorAll('script[type="application/ld+json"]')`
2. **Google Rich Results Test** — https://search.google.com/test/rich-results
3. **Screaming Frog export** — SF renders JavaScript

Reporting "no schema found" based solely on `web_fetch` leads to false findings.

---

## Audit Framework (Priority Order)

1. **Crawlability & Indexation** (can Google find and index it?)
2. **Technical Foundations** (is the site fast and functional?)
3. **On-Page Optimization** (is content optimized?)
4. **Content Quality** (does it deserve to rank?)
5. **Authority & Links** (does it have credibility?)

---

## Technical SEO Audit

### Crawlability
- Robots.txt: no unintentional blocks, sitemap referenced
- XML Sitemap: exists, submitted to Search Console, canonical+indexable URLs only
- Site architecture: important pages within 3 clicks, no orphan pages
- Crawl budget (large sites): parameterized URLs, faceted nav, session IDs

### Indexation
- site:domain.com check + Search Console coverage report
- Issues: noindex on important pages, wrong canonicals, redirect chains, soft 404s
- Canonicalization: all pages have canonical tags, HTTP→HTTPS, www consistency

### Site Speed & Core Web Vitals
- **LCP** < 2.5s | **INP** < 200ms | **CLS** < 0.1
- Speed factors: TTFB, image optimization, JS execution, CSS delivery, caching, CDN, fonts

### Mobile & Security
- Responsive design, tap targets, same content as desktop
- HTTPS across entire site, valid SSL, no mixed content

---

## International SEO & Localization

### Hreflang
- Self-referencing entry on every page (required)
- Reciprocal links (A→B and B→A, or both ignored)
- Valid codes: ISO 639-1 + optional ISO 3166-1 Alpha-2 (e.g., `en`, `en-GB` — never `en-UK`)
- `x-default` present for fallback
- All target URLs return 200, indexable, match canonical
- HTML and sitemap annotations must agree

**Common errors:** Missing self-reference, one-directional links, `en-UK` instead of `en-GB`, hreflang target is non-canonical/404/blocked.

### Canonicalization for Multilingual Sites
- Each locale page self-canonicals — NEVER cross-locale canonical
- Canonical URL must appear in the hreflang set
- Canonical overrides hreflang when they conflict

---

## On-Page SEO Audit

### Title Tags
- Unique, primary keyword near beginning, 50-60 chars, compelling
- Issues: duplicates, too long, keyword stuffing, missing

### Meta Descriptions
- Unique, 150-160 chars, includes keyword, clear value prop, CTA

### Heading Structure
- One H1 per page with primary keyword, logical hierarchy (H1→H2→H3)

### Content Optimization
- Keyword in first 100 words, answers search intent, better than competitors
- No thin content, no duplicate/near-duplicate pages

### Images
- Descriptive file names, alt text on all images, compressed, WebP format, lazy loading

### Internal Linking
- No orphan pages, descriptive anchor text, no broken links

---

## E-E-A-T Signals

**Experience:** First-hand experience, original insights, real examples.
**Expertise:** Author credentials, accurate detailed info, properly sourced claims.
**Authoritativeness:** Recognized in space, cited by others.
**Trustworthiness:** Accurate info, transparent business, contact info, HTTPS.

---

## Output Format

**Executive Summary:** Overall health, top 3-5 priority issues, quick wins.

**For each issue:**
- **Issue**: What's wrong
- **Impact**: High/Medium/Low
- **Evidence**: How found
- **Fix**: Specific recommendation
- **Priority**: 1-5

**Prioritized Action Plan:**
1. Critical fixes (blocking indexation/ranking)
2. High-impact improvements
3. Quick wins
4. Long-term recommendations

---

## Tools Referenced

**Free:** Google Search Console (essential), PageSpeed Insights, Rich Results Test (renders JS — use for schema), Mobile-Friendly Test

**Paid:** Screaming Frog, Ahrefs / Semrush, Sitebulb

**Note on schema detection:** `web_fetch` strips `<script>` tags. Use browser tool, Rich Results Test, or Screaming Frog to detect JS-injected schema.

---

## Related Skills

- **ai-seo**: For optimizing for AI search (AEO, GEO, LLMO)
- **programmatic-seo**: For building SEO pages at scale
- **site-architecture**: For page hierarchy, navigation, URL structure
- **schema**: For implementing structured data
- **cro**: For optimizing pages for conversion
- **analytics**: For measuring SEO performance
