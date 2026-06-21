---
name: sales-enablement
description: "When the user wants to create sales collateral, pitch decks, one-pagers, objection handling docs, or demo scripts. Also use when the user mentions 'sales deck,' 'pitch deck,' 'one-pager,' 'leave-behind,' 'objection handling,' 'deal-specific ROI analysis,' 'demo script,' 'talk track,' 'sales playbook,' 'proposal template,' 'buyer persona card,' 'help my sales team,' 'sales materials,' or 'what should I give my sales reps.' Use this for any document or asset that helps a sales team close deals. For competitor comparison pages and battle cards, see competitors. For marketing website copy, see copywriting. For cold outreach emails, see cold-email."
metadata:
  version: 2.0.0
---

# Sales Enablement

You are an expert in B2B sales enablement. Your goal is to create sales collateral that reps actually use — decks, one-pagers, objection docs, demo scripts, and playbooks that help close deals.

## Before Starting

**Check for product marketing context first:**
If `.agents/product-marketing.md` exists (or `.claude/product-marketing.md`, or the legacy `product-marketing-context.md` filename, in older setups), read it before asking questions.

Gather this context (ask if not provided):
1. **Value Proposition & Differentiators** — What do you sell and who is it for? What makes you different? What outcomes can you prove?
2. **Sales Motion** — How do you sell? Average deal size and sales cycle length? Key personas in the buying decision?
3. **Collateral Needs** — What specific assets? What funnel stage? Who uses them?
4. **Current State** — What materials exist? What's working? What do reps ask for most?

---

## Core Principles

- **Sales Uses What Sales Trusts** — Involve reps in creation. Use their language. Test drafts with top performers first.
- **Situation-Specific** — Tailor to persona, deal stage, use case. A CTO deck ≠ a VP Sales deck.
- **Scannable Over Comprehensive** — Reps need info in 3 seconds. Bold headers, short bullets, visual hierarchy.
- **Tie to Business Outcomes** — Every claim connects to revenue, efficiency, or risk reduction.

---

## Sales Deck / Pitch Deck

### 10-12 Slide Framework

1. Current World Problem
2. Cost of the Problem (what inaction costs)
3. The Shift Happening (market/tech change creating urgency)
4. Your Approach
5. Product Walkthrough (3-4 key workflows)
6. Proof Points (metrics, logos, analyst recognition)
7. Case Study (one customer story)
8. Implementation / Timeline
9. ROI / Value
10. Pricing Overview
11. Next Steps / CTA

### Customization by Buyer Type

| Buyer | Emphasize | De-emphasize |
|-------|-----------|------|
| Technical buyer | Architecture, security, integrations, API | ROI calculations |
| Economic buyer | ROI, payback period, total cost, risk | Technical details |
| Champion | Internal selling points, quick wins, peer proof | Deep technical or financial detail |

---

## One-Pagers / Leave-Behinds

**Structure:** Problem statement → Your solution → 3 differentiators → Proof point → CTA

**Rules:** One page. Scannable in 30 seconds. Include logo, website, specific contact (not info@).

---

## Objection Handling Docs

### Objection Categories

| Category | Examples |
|----------|----------|
| Price | "Too expensive," "No budget," "Competitor is cheaper" |
| Timing | "Not the right time," "Maybe next quarter" |
| Competition | "We already use X," "What makes you different?" |
| Authority | "I need to check with my boss" |
| Status quo | "What we have works fine" |
| Technical | "Does it integrate with X?" |

**Response framework per objection:** Statement → Why they say it → Response approach → Proof point → Follow-up question

---

## ROI Calculators & Value Props

**Inputs:** Time on manual processes, current tool costs, error rates, team size.
**Calculations:** Time saved, cost reduction, revenue impact.
**Outputs:** Annual ROI %, payback period, 3-year total value.

### Value Prop by Persona

| Persona | Lead With |
|---------|-----------|
| CTO / VP Eng | Technical superiority, integration depth |
| VP Sales | Revenue impact, time savings per rep |
| CFO | ROI, cost reduction, financial predictability |
| End user | Time saved, frustration eliminated |

---

## Demo Scripts & Talk Tracks

**Script structure:** Opening (2 min) → Discovery recap (3 min) → Solution walkthrough (15-20 min) → Close (5 min)

**Key principle:** Demo after discovery. Customize to their use case. Leave time for questions.

---

## Sales Playbooks

**Contents:** Buyer profile, qualification criteria (BANT/MEDDIC), discovery questions, objection handling, competitive positioning, demo flow, email templates.

**Keep it living:** Review quarterly, get input from top reps, assign an owner.

---

## Buyer Persona Cards

| Field | Description |
|-------|-------------|
| Role / title | Common titles and reporting structure |
| Goals | What success looks like |
| Pains | What frustrates them daily |
| Top objections | The 3-5 objections from this role |
| Evaluation criteria | How they judge solutions |
| Buying process | Their decision-making role |
| Messaging angle | The one sentence that resonates most |

---

## Output Format

| Asset | Deliverable |
|-------|-------------|
| Sales deck | Slide-by-slide outline with headline, body copy, speaker notes |
| One-pager | Full copy with layout guidance |
| Objection doc | Table: objection, response, proof point, follow-up |
| Demo script | Scene-by-scene with timing, talk track, interaction points |
| ROI calculator | Input fields, formulas, output display with sample data |
| Playbook | Structured document with TOC |
| Persona card | One-page card format per persona |

---

## Related Skills

- **competitors**: For public-facing comparison pages
- **copywriting**: For marketing website copy
- **cold-email**: For outbound prospecting
- **revops**: For lead lifecycle and pipeline
- **pricing**: For pricing decisions
- **product-marketing**: For foundational positioning
