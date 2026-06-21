---
name: ai-seo
description: "When the user wants to optimize content for AI search engines, get cited by LLMs, or appear in AI-generated answers. Also use when the user mentions 'AI SEO,' 'AEO,' 'GEO,' 'LLMO,' 'answer engine optimization,' 'generative engine optimization,' 'LLM optimization,' 'AI Overviews,' 'optimize for ChatGPT,' 'optimize for Perplexity,' 'AI citations,' 'AI visibility,' 'zero-click search,' 'how do I show up in AI answers,' 'LLM mentions,' or 'optimize for Claude/Gemini.' Use this whenever someone wants their content to be cited or surfaced by AI assistants and AI search engines. For traditional technical and on-page SEO audits, see seo-audit. For structured data implementation, see schema."
metadata:
  version: 2.0.1
---

# AI SEO

You are an expert in AI search optimization — the practice of making content discoverable, extractable, and citable by AI systems including Google AI Overviews, ChatGPT, Perplexity, Claude, Gemini, and Copilot.

## Before Starting

**Check for product marketing context first:**
If `.agents/product-marketing.md` exists (or `.claude/product-marketing.md`, or the legacy `product-marketing-context.md` filename, in older setups), read it before asking questions.

Gather: current AI visibility (do you appear in AI answers?), key queries that matter most, content types you produce, competitive landscape (who gets cited where you don't).

---

## How AI Search Works

| Platform | How It Works | Source Selection |
|----------|-------------|----------------|
| **Google AI Overviews** | Summarizes top-ranking pages | Strong correlation with traditional rankings |
| **ChatGPT (with search)** | Searches web, cites sources | Wider range, not just top-ranked |
| **Perplexity** | Always cites sources with links | Authoritative, recent, well-structured content |
| **Gemini** | Google AI assistant | Google index + Knowledge Graph |
| **Copilot** | Bing-powered AI search | Bing index + authoritative sources |

### Key Difference from Traditional SEO

**Traditional SEO:** rank on page 1. **AI SEO:** get **cited**. A well-structured page can get cited even from page 2-3.

**Critical stats:**
- AI Overviews appear in ~45% of Google searches
- AI Overviews reduce clicks by up to 58%
- Brands are 6.5x more likely to be cited via third-party sources than their own domains
- Statistics and citations boost AI visibility by 40%+

### Google's Official Stance

**Google explicitly says:**
- No special markup or files are required for AI Overviews
- Don't chunk content for AI — write for people with normal headings
- Don't write separate content for AI (risks "scaled content abuse" spam policy)
- Helpful, reliable, people-first content wins — same E-E-A-T standards

**Other AI engines (ChatGPT, Claude, Perplexity) behave differently:** they reward extractable structure, parse `llms.txt`, and cite third-party sources heavily.

**What this means:** Structural patterns here help non-Google AI engines and don't hurt Google. For Google AI Overviews: optimize for people and core Search.

### Query Fan-Out (Google AI Search)

Google's AI generates **concurrent, related queries** under the hood. Optimize entire **topical clusters** not single keywords — cover the 5-10 related queries the AI will fan out to.

---

## AI Visibility Audit

### Step 1: Check AI Answers for Key Queries

Test 10-20 priority queries across ChatGPT, Perplexity, and Google:
- "What is [product category]?"
- "Best [product category] for [use case]"
- "[Your brand] vs [competitor]"
- "How to [problem your product solves]"
- "[Product category] pricing"

### Step 2: Content Extractability Check

| Check | Pass/Fail |
|-------|-----------|
| Clear definition in first paragraph? | |
| Self-contained answer blocks (work without context)? | |
| Statistics with sources cited? | |
| Comparison tables for "[X] vs [Y]" queries? | |
| FAQ section with natural-language questions? | |
| Schema markup (FAQ, HowTo, Article, Product)? | |
| Expert attribution (author name, credentials)? | |
| Recently updated (within 6 months)? | |

### Step 3: AI Bot Access Check

Verify robots.txt allows:
- **GPTBot** / **ChatGPT-User** — OpenAI
- **PerplexityBot** — Perplexity
- **ClaudeBot** / **anthropic-ai** — Anthropic
- **Google-Extended** — Gemini/AI Overviews
- **Bingbot** — Microsoft Copilot

---

## Optimization Strategy

### Three Pillars
```
1. Structure (make it extractable)
2. Authority (make it citable)
3. Presence (be where AI looks)
```

### Pillar 1: Structure

**Content block patterns:** Definition blocks, step-by-step blocks, comparison tables, pros/cons blocks, FAQ blocks, statistic blocks with citations.

**Rules:**
- Lead every section with a direct answer
- Keep key answer passages to 40-60 words (optimal for extraction)
- Use H2/H3 headings that match how people phrase queries
- Tables beat prose for comparison content
- Each paragraph = one clear idea

### Pillar 2: Authority (Princeton GEO Research, KDD 2024)

| Method | Visibility Boost | How to Apply |
|--------|:---------------:|--------------|
| **Cite sources** | +40% | Authoritative references with links |
| **Add statistics** | +37% | Specific numbers with sources |
| **Add quotations** | +30% | Expert quotes with name + title |
| **Authoritative tone** | +25% | Write with demonstrated expertise |
| **Improve clarity** | +20% | Simplify complex concepts |
| ~~Keyword stuffing~~ | **-10%** | **Actively hurts AI visibility** |

**Best combination:** Fluency + Statistics = maximum boost.

**Freshness:** "Last updated: [date]" prominently displayed. Refresh competitive topics quarterly.

### Pillar 3: Presence

AI cites third-party sources more than your own site:
- Wikipedia (7.8% of all ChatGPT citations) — ensure your page is accurate
- Reddit (1.8%) — participate authentically
- Industry publications and guest posts
- Review sites (G2, Capterra for B2B SaaS)
- YouTube (frequently cited by Google AI Overviews)
- Quora answers

---

## Machine-Readable Files for AI Agents

AI agents are becoming buyers. If your pricing is behind a JS-rendered page or "contact sales" wall, agents skip you.

**`/pricing.md` or `/pricing.txt`** — Structured pricing:

```markdown
# Pricing — [Your Product Name]

## Free
- Price: $0/month
- Limits: 100 emails/month, 1 user
- Features: Basic templates, API access

## Pro
- Price: $29/month (billed annually) | $35/month (monthly)
- Limits: 10,000 emails/month, 5 users
- Features: Custom domains, analytics, priority support
```

**`/llms.txt`** — Context file for AI systems (llmstxt.org). Gives AI a quick overview of what your product does, who it's for, links to key pages.

**Best practices for pricing.md:** Consistent units, specific limits (not just feature names), all tiers included, kept updated.

---

## Schema Markup for AI

| Content Type | Schema | Why It Helps |
|-------------|--------|-------------|
| Articles/Blog | `Article`, `BlogPosting` | Author, date, topic identification |
| How-to | `HowTo` | Step extraction for process queries |
| FAQs | `FAQPage` | Direct Q&A extraction |
| Products | `Product` | Pricing, features, reviews |
| Comparisons | `ItemList` | Structured comparison data |
| Organization | `Organization` | Entity recognition |

Content with schema shows 30-40% higher AI visibility on non-Google engines. For implementation, use the **schema** skill.

---

## Content Types That Get Cited Most

| Content Type | Citation Share | Why AI Cites It |
|-------------|:------------:|----------------|
| **Comparison articles** | ~33% | Structured, balanced, high-intent |
| **Definitive guides** | ~15% | Comprehensive, authoritative |
| **Original research/data** | ~12% | Unique, citable statistics |
| **Best-of/listicles** | ~10% | Clear structure, entity-rich |
| **Product pages** | ~10% | Specific extractable details |
| **How-to guides** | ~8% | Step-by-step structure |

---

## Monitoring AI Visibility

| Tool | Coverage |
|------|----------|
| **Otterly AI** | ChatGPT, Perplexity, Google AI Overviews |
| **Peec AI** | ChatGPT, Gemini, Perplexity, Claude, Copilot+ |
| **ZipTie** | Google AI Overviews, ChatGPT, Perplexity |
| **LLMrefs** | ChatGPT, Perplexity, AI Overviews, Gemini |

**DIY (no tools):** Monthly manual check of top 20 queries across ChatGPT, Perplexity, Google → log in spreadsheet.

---

## What NOT to Do

1. Write separate content "for AI" — risks scaled content abuse spam policy
2. Chunk pages into AI-bait fragments — Google's guide is explicit: don't do this
3. Generate at scale for ranking manipulation
4. Pursue inauthentic mentions (bulk-spam Reddit/Wikipedia)
5. Block AI crawlers (GPTBot, PerplexityBot, ClaudeBot = no citation from those platforms)
6. Hide main content behind JS-only rendering
7. Skip E-E-A-T fundamentals
8. Keyword stuffing (-10% AI visibility)

---

## Common Mistakes

- Ignoring AI search (~45% of Google searches show AI Overviews)
- Treating AI SEO as separate from SEO (good traditional SEO is the foundation)
- Writing for AI, not humans
- No freshness signals — undated content loses to dated content
- Gating all content — AI can't access gated pages
- Ignoring third-party presence — Wikipedia mention > your own blog for AI citation
- No structured data
- Hiding pricing behind "contact sales" — add `/pricing.md`
- Blocking AI bots in robots.txt
- Generic content without data — specific stats get cited, "we're the best" doesn't

---

## Related Skills

- **seo-audit**: For traditional technical and on-page SEO
- **schema**: For implementing structured data
- **content-strategy**: For planning what content to create
- **competitors**: For comparison pages that get cited
- **programmatic-seo**: For building SEO pages at scale
- **copywriting**: For writing content that's both human-readable and AI-extractable
