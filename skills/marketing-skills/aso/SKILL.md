---
name: aso
description: "When the user wants to audit or optimize an App Store or Google Play listing. Also use when the user mentions 'ASO audit,' 'app store optimization,' 'optimize my app listing,' 'improve app visibility,' 'app store ranking,' 'audit my listing,' 'why aren't people downloading my app,' 'improve my app conversion,' 'keyword optimization for app,' or 'compare my app to competitors.' Use when the user shares an App Store or Google Play URL and wants to improve it."
metadata:
  version: 2.0.0
---

# ASO Audit

Analyze App Store and Google Play listings against ASO best practices. Fetches
live listing data, scores metadata, visuals, and ratings, then produces a
prioritized action plan.

## When to Use

- User shares an App Store or Google Play URL
- User asks to audit or optimize an app listing
- User wants to compare their app against competitors
- User asks about app store ranking, visibility, or download conversion

## Before Auditing

**Check for product marketing context first:**
If `.agents/product-marketing.md` exists (or `.claude/product-marketing.md`, or the legacy `product-marketing-context.md` filename, in older setups), read it before asking questions. Use that context and only ask for information not already covered or specific to this task.

## Phase 1 — Identify Store & Fetch

### Detect store type from URL

```
Apple:  apps.apple.com/{country}/app/{name}/id{digits}
Google: play.google.com/store/apps/details?id={package}
```

If the user gives an app name instead of a URL, search the web for:
`site:apps.apple.com "{app name}"` or `site:play.google.com "{app name}"`

### Fetch the listing

Use WebFetch to retrieve the listing page. Extract every available field.

**Apple App Store fields:** App name (30 char limit), Subtitle (30 char limit), Description, Promotional text (170 chars), Category, Screenshots, Preview video, Rating, Reviews, Price/IAP, Developer name, Last updated, Version notes, Age rating, Size, Languages, In-app events.

**Google Play fields:** App name (30 char limit), Short description (80 char limit), Full description (4,000 chars, IS indexed), Category, Feature graphic, Screenshots, Preview video, Rating, Reviews, Price/IAP, Developer name, Last updated, What's new, Downloads range, Content rating, Data safety, Languages.

### Visual asset assessment

WebFetch cannot extract screenshot images. Take a screenshot of the listing page to assess: icon quality, screenshot count, caption text, messaging quality, preview video presence, feature graphic.

---

## Phase 1.5 — Assess Brand Maturity

| Tier | Signals | Examples |
|------|---------|----------|
| **Dominant** | Household name, 1M+ ratings, top-10 in category | Instagram, Uber, Spotify |
| **Established** | Well-known in category, 100K+ ratings | Strava, Notion, Duolingo |
| **Challenger** | Building awareness, <100K ratings | Most indie/startup apps |

Dominant apps get adjusted scoring — brand-only titles, lifestyle photography, and minimal keyword optimization are legitimate strategies, not mistakes.

---

## Phase 2 — Score Each Dimension

| # | Dimension | Weight | What It Covers |
|---|-----------|--------|----------------|
| 1 | Title & Subtitle | 20% | Character usage, keyword presence, clarity |
| 2 | Description | 15% | First 3 lines, keyword density (Google), CTA, structure |
| 3 | Visual Assets | 25% | Screenshot count/quality/messaging, video, icon |
| 4 | Ratings & Reviews | 20% | Average rating, volume, recency, developer responses |
| 5 | Metadata & Freshness | 10% | Category, update recency, localization, data safety |
| 6 | Conversion Signals | 10% | Price positioning, IAP transparency, social proof |

**Final score** = weighted sum, out of 100.

| Score | Grade |
|-------|-------|
| 85-100 | A |
| 70-84 | B |
| 50-69 | C |
| 30-49 | D |
| 0-29 | F |

---

## Phase 3 — Competitor Comparison (Optional)

Fetch 2-3 top competitors in the same category, run the same scoring, build comparison table highlighting keyword gaps and relative strengths.

---

## Phase 4 — Generate Report

The report must include:
1. **Score card** — all 6 dimensions with scores and grade
2. **Top 3 quick wins** — <1 hour changes with highest impact
3. **Detailed findings** — per-dimension breakdown with specific fixes
4. **Keyword suggestions** — based on title/description analysis and competitor gaps
5. **Visual asset recommendations** — specific screenshot/video improvements
6. **Priority action plan** — ordered by impact vs effort

Every recommendation must be **specific and actionable** ("Change subtitle from X to Y" not "Improve subtitle"). Include character counts for all text recommendations.

---

## Platform-Specific Rules

### Apple App Store
- Title (30) + Subtitle (30) + Keyword field (100 bytes, hidden) = indexed text
- Keywords field is bytes not chars — never repeat words across fields
- Long description NOT indexed for search — optimize for conversion only
- Screenshots: up to 10, first 3 visible in search
- Screenshot captions indexed since June 2025
- App preview video: up to 3, 15-30s each, +20-40% conversion lift
- In-app events: max 10 published, indexed and appear in search
- Custom Product Pages (up to 70) in organic search since July 2025

### Google Play
- Title (30) + Short description (80) + Full description (4,000) = indexed
- Full description IS indexed — target 2-3% keyword density naturally
- No hidden keyword field — all keywords must be in visible text
- Screenshots: min 2, max 8 (not 10 like Apple)
- Feature graphic (1024x500 exact) required for featured placements
- Video does NOT autoplay — only ~6% of users tap play
- Android Vitals affect ranking: crash >1.09% or ANR >0.47% = reduced visibility
- Prohibited in title: emojis, ALL CAPS, "best"/"#1"/"free", CTAs

---

## Related Skills

- **cro**: For optimizing web landing pages that drive app installs
- **ad-creative**: For App Store and Google Play ad creatives
- **analytics**: For install attribution and in-app event tracking
- **customer-research**: For user needs and language to inform listing copy
