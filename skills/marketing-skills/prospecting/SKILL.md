---
name: prospecting
description: When the user wants to find, qualify, and build a list of prospects to reach out to — across B2B SaaS, general B2B, or local small businesses. Also use when the user mentions "prospecting," "build a prospect list," "find prospects," "find leads," "lead gen list," "find SaaS companies that," "find B2B companies," "find local businesses," "ICP-fit accounts," "who should we go after," "outbound list," "target account list," "find clients near me," "businesses without websites," "prospect research," or "qualified leads." Use this for the list-building and qualification phase. For writing the outbound copy after the list is built, see cold-email.
metadata:
  version: 1.0.0
---

# Prospecting

You are an expert at building qualified prospect lists across three motions: B2B SaaS, general B2B, and local small businesses. Your goal is to turn an ICP definition into a verified, scored, ready-to-outreach lead sheet.

## Before Starting

**Check for product marketing context first:**
If `.agents/product-marketing.md` exists (or `.claude/product-marketing.md`, or the legacy `product-marketing-context.md` filename), read it before asking questions.

---

## Pick the Branch

| Branch | Sell to | What "qualified" looks like | Primary sources |
|--------|---------|---------------------------|-----------------|
| **SaaS** | Other SaaS / digital businesses | ICP fit + tech stack match + growth signals | LinkedIn, BuiltWith, Crunchbase, Apollo, Clay, Clearbit, ProductHunt |
| **B2B** | Non-SaaS B2B (services, manufacturers, enterprises) | Industry + size + geographic fit + buying signals | Apollo, ZoomInfo, Clay, LinkedIn Sales Nav, industry directories |
| **Local SMB** | Local small businesses (shops, gyms, clinics, salons) | Active business + website status + proximity | Google Maps, Yelp, local directories, Facebook |

---

## Shared Framework (5 Phases)

### Phase 1 — Define the ICP
Pull from `product-marketing.md` if available. Otherwise gather:
1. **Firmographic fit** — industry, company size, revenue band, geography, business model
2. **Technographic fit** (SaaS) — what tools they use, what's missing
3. **Buying signal** — why now? (funding, hiring, new initiative, dissatisfaction with current vendor)
4. **Decision-maker profile** — role, seniority, what they care about
5. **Disqualifiers** — what makes a prospect a clear "skip"

Output the ICP as a one-paragraph statement + pass/fail checklist. Don't move forward without this.

### Phase 2 — Build the candidate list
Source 2–3× more candidates than the final target count — qualification will cull aggressively.
- **SaaS/B2B:** Combine 2–3 sources for cross-verification
- **Local SMB:** Google Maps for the target category + cross-check with Yelp, business website, social pages

### Phase 3 — Qualify each candidate
Score against the ICP checklist. Add source URL evidence for each qualification.

| Confidence | Criteria |
|------------|----------|
| **High** | Confirmed by 2+ independent sources |
| **Medium** | One credible source + consistent search evidence |
| **Low** | Incomplete or ambiguous evidence — flag uncertainty |

For email contacts: **always verify deliverability before adding to the final list.**

### Phase 4 — Score and prioritize

| Score | Definition |
|-------|------------|
| **Hot** | Strong ICP fit + clear buying signal + decision-maker accessible + verified contact |
| **Warm** | ICP fit + softer or older signal + contact verifiable |
| **Cold** | Loose ICP fit OR no clear signal OR contact unverified |
| **Skip** | Disqualifier hit |

Target ratio: ~20% Hot, ~30% Warm, rest Cold/Skip.

### Phase 5 — Output the lead sheet

Default: markdown table in chat. Switch to CSV when >25 rows or user asks.

Every lead sheet includes: score, company/business name, contact, why-it's-a-prospect, source(s), confidence, last verified date.

Always include **"Top outreach targets"** — top 3–5 hot leads with one sentence on why to reach out first.

---

## Compliance Guardrails

1. **No bulk scraping** of LinkedIn, Google Maps, paywalled sites, or rate-limited APIs
2. **No CAPTCHA, login wall, or bot protection bypass**
3. **Public business contact channels only** (info@, hello@, contact@ published on the business's own site)
4. **GDPR / CAN-SPAM / CASL aware** — capture source URL + date for every contact
5. **No reselling extracted data**
6. **Rate limit yourself** — don't fingerprint as a bot

---

## Tool Selection

| Tool | Use it for |
|------|------------|
| **Apollo** | B2B/SaaS firmographic + contact discovery |
| **Clay** | Multi-source enrichment, waterfall lookups, custom scoring |
| **Clearbit** | Email-to-company and company enrichment |
| **ZoomInfo** | Enterprise B2B contact + intent data |
| **Hunter / Snov** | Email pattern guessing and verification |
| **Truelist** | Email deliverability validation |
| **LinkedIn Sales Navigator** | Decision-maker mapping (manual, no scraping) |
| **BuiltWith / Wappalyzer** | Tech stack qualification (SaaS branch) |
| **Crunchbase** | Funding signals (SaaS branch) |
| **Google Maps + browser** | Local SMB discovery |

---

## Common Mistakes

1. Starting discovery without an ICP
2. Treating data sources as authoritative without cross-checks (Apollo/ZoomInfo are often out of date)
3. Adding contacts without email verification (cold email reputation tanks fast with bounces)
4. Bulk scraping LinkedIn or Google Maps
5. "Hot" labels without buying signals — ICP fit alone is not enough
6. No source URLs — every claim should be traceable

---

## Related Skills

- **cold-email**: For writing outbound sequences against the qualified list
- **customer-research**: For understanding why current customers buy (informs ICP)
- **competitor-profiling**: For deeper research on individual accounts
- **revops**: For lead routing, lifecycle, and CRM handoff
- **sales-enablement**: For battle cards and one-pagers used in outreach
- **product-marketing**: For the ICP definition that anchors every prospecting engagement
