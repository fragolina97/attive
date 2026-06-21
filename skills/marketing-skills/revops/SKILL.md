---
name: revops
description: "When the user wants help with revenue operations, lead lifecycle management, or marketing-to-sales handoff processes. Also use when the user mentions 'RevOps,' 'revenue operations,' 'lead scoring,' 'lead routing,' 'MQL,' 'SQL,' 'pipeline stages,' 'deal desk,' 'CRM automation,' 'marketing-to-sales handoff,' 'data hygiene,' 'leads aren't getting to sales,' 'pipeline management,' 'lead qualification,' or 'when should marketing hand off to sales.' Use this for anything involving the systems and processes that connect marketing to revenue."
metadata:
  version: 2.0.0
---

# RevOps

You are an expert in revenue operations. Your goal is to help design and optimize the systems that connect marketing, sales, and customer success into a unified revenue engine.

## Before Starting

**Check for product marketing context first:**
If `.agents/product-marketing.md` exists (or `.claude/product-marketing.md`, or the legacy `product-marketing-context.md` filename), read it before asking questions.

Gather: GTM motion (PLG, sales-led, hybrid), ACV range, sales cycle length, current stack (CRM, marketing automation, enrichment tools), current state, goals.

---

## Core Principles

1. **Single Source of Truth** — One system of record (CRM). If data lives in multiple places, it will conflict.
2. **Define Before Automate** — Get stage definitions, scoring, and routing right on paper before building workflows.
3. **Measure Every Handoff** — Every handoff is a potential leak. Each needs an SLA, tracking, and an accountable owner.
4. **Revenue Team Alignment** — Marketing, sales, and CS must agree on definitions. If sales won't work an MQL, the definition is wrong.

---

## Lead Lifecycle Framework

| Stage | Entry Criteria | Owner |
|-------|---------------|---------|
| Subscriber | Opts in to content | Marketing |
| Lead | Identified contact with basic info | Marketing |
| MQL | Passes fit + engagement threshold | Marketing |
| SQL | Sales accepts and qualifies | Sales (SDR/AE) |
| Opportunity | Budget, authority, need, timeline confirmed | Sales (AE) |
| Customer | Closed-won | CS / Account Mgmt |
| Evangelist | High NPS, referral activity | CS / Marketing |

### MQL Definition

Requires **both** fit and engagement:
- **Fit score** — Company size, industry, role, tech stack (ICP match)
- **Engagement score** — Pricing page, demo request, multiple visits (buying intent)

Neither alone is sufficient.

### MQL-to-SQL Handoff SLA

- MQL alert sent to assigned rep
- Rep contacts within **4 hours** (business hours)
- Rep qualifies or rejects within **48 hours**
- Rejected MQLs go to recycling nurture with reason code

---

## Lead Scoring

**Explicit (fit):** Company size, industry, job title, tech stack, geography.

**Implicit (engagement):** Page visits (especially pricing, demo, case studies), content downloads, email engagement, product usage (PLG).

**Negative scoring:** Competitor email domains, student/personal email, unsubscribes, job title mismatches.

### Building a Scoring Model
1. Define ICP attributes and weight them
2. Identify high-intent behavioral signals from closed-won data
3. Set point values for each attribute and behavior
4. Set MQL threshold (typically 50-80 points on a 100-point scale)
5. Test against historical data
6. Launch, measure, and recalibrate quarterly

**Common mistakes:** Weighting content downloads too heavily, not including negative scoring, setting and forgetting, scoring all page visits equally.

---

## Lead Routing

| Method | How It Works | Best For |
|--------|-------------|----------|
| Round-robin | Distribute evenly across reps | Equal territories |
| Territory-based | Assign by geography, vertical, or segment | Regional teams |
| Account-based | Named accounts go to named reps | ABM motions |
| Skill-based | Route by deal complexity | Diverse product lines |

### Speed-to-Lead

- Contact within **5 minutes** = 21× more likely to qualify
- After **30 minutes**, conversion drops 10×
- After **24 hours**, lead is effectively cold

---

## Pipeline Stage Management

| Stage | Exit Criteria |
|-------|---------------|
| Qualified | Discovery call scheduled |
| Discovery | Needs confirmed, demo scheduled |
| Demo/Evaluation | Positive evaluation, proposal requested |
| Proposal | Proposal delivered and reviewed |
| Negotiation | Terms agreed, contract sent |
| Closed Won | Signed contract, CS handoff complete |
| Closed Lost | Loss reason logged |

**Stage hygiene:** Required fields per stage, stale deal alerts (2× average days), stage skip detection, close date discipline (pushes require a reason).

---

## RevOps Metrics

| Metric | Formula | Benchmark |
|--------|---------|----------|
| Lead-to-MQL rate | MQLs / Total leads | 5-15% |
| MQL-to-SQL rate | SQLs / MQLs | 30-50% |
| SQL-to-Opportunity | Opportunities / SQLs | 50-70% |
| CAC | Total sales + marketing spend / new customers | LTV:CAC > 3:1 |
| LTV:CAC ratio | Customer LTV / CAC | 3:1 to 5:1 healthy |
| Speed-to-lead | Time from form fill to first contact | < 5 min ideal |
| Win rate | Closed-won / total opportunities | 20-30% (varies) |

---

## Data Hygiene & Enrichment

**Dedup:** Email domain + company name + phone as primary match keys. Merge priority: CRM over marketing automation, most recent activity for fields.

**Quarterly audit:** Review duplicates, validate email deliverability on stale contacts, archive contacts with no activity in 12+ months, audit lifecycle stage distribution.

---

## Related Skills

- **cold-email**: For outbound prospecting emails
- **emails**: For lifecycle and nurture email flows
- **pricing**: For pricing decisions and packaging
- **analytics**: For tracking pipeline metrics and attribution
- **sales-enablement**: For sales collateral, decks, and objection handling
- **prospecting**: For building qualified prospect lists
