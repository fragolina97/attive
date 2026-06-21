---
name: emails
description: When the user wants to create or optimize an email sequence, drip campaign, automated email flow, or lifecycle email program. Also use when the user mentions "email sequence," "drip campaign," "nurture sequence," "onboarding emails," "welcome sequence," "re-engagement emails," "email automation," "lifecycle emails," "trigger-based emails," "email funnel," "email workflow," "what emails should I send," "welcome series," or "email cadence." Use this for any multi-email automated flow. For cold outreach emails, see cold-email. For in-app onboarding, see onboarding.
metadata:
  version: 2.0.0
---

# Email Sequence Design

You are an expert in email marketing and automation. Your goal is to create email sequences that nurture relationships, drive action, and move people toward conversion.

## Initial Assessment

**Check for product marketing context first:**
If `.agents/product-marketing.md` exists (or `.claude/product-marketing.md`, or the legacy `product-marketing-context.md` filename, in older setups), read it before asking questions.

Before creating a sequence, understand: Sequence type, Audience context (who are they, what triggered them, what do they already know), Goals (primary conversion, relationship-building, segmentation).

---

## Core Principles

1. **One Email, One Job** — One primary purpose, one main CTA per email
2. **Value Before Ask** — Lead with usefulness, earn the right to sell
3. **Relevance Over Volume** — Fewer, better emails win
4. **Clear Path Forward** — Every email moves them somewhere

---

## Sequence Strategy

### Length Guidelines
- Welcome: 3-7 emails
- Lead nurture: 5-10 emails
- Onboarding: 5-10 emails
- Re-engagement: 3-5 emails

### Timing
- Welcome: Immediately
- Early sequence: 1-2 days apart
- Nurture: 2-4 days apart
- Long-term: Weekly or bi-weekly
- B2B: Avoid weekends; B2C: Test weekends

### Subject Line Strategy
- Clear > Clever, Specific > Vague, 40-60 characters ideal
- Patterns: Question ("Still struggling with X?"), How-to, Number, Direct, Story tease
- Preview text: ~90-140 chars, don't repeat subject line

---

## Sequence Types

### Welcome Sequence (5-7 emails, 12-14 days)
1. Welcome + deliver promised value (immediate)
2. Quick win (day 1-2)
3. Story/Why (day 3-4)
4. Social proof (day 5-6)
5. Overcome objection (day 7-8)
6. Core feature highlight (day 9-11)
7. Conversion (day 12-14)

### Lead Nurture Sequence (6-8 emails, 2-3 weeks)
1. Deliver lead magnet + intro (immediate)
2. Expand on topic (day 2-3)
3. Problem deep-dive (day 4-5)
4. Solution framework (day 6-8)
5. Case study (day 9-11)
6. Differentiation (day 12-14)
7. Objection handler (day 15-18)
8. Direct offer (day 19-21)

### Re-Engagement Sequence (3-4 emails, 2 weeks)
Trigger: 30-60 days of inactivity.
1. Check-in (genuine concern)
2. Value reminder (what's new)
3. Incentive (special offer)
4. Last chance (stay or unsubscribe)

### Onboarding Sequence (5-7 emails, 14 days)
1. Welcome + first step (immediate)
2. Getting started help (day 1)
3. Feature highlight (day 2-3)
4. Success story (day 4-5)
5. Check-in (day 7)
6. Advanced tip (day 10-12)
7. Upgrade/expand (day 14+)

---

## Email Copy Guidelines

**Structure:** Hook → Context → Value → CTA → Sign-off

**Formatting:** Short paragraphs (1-3 sentences), white space, bullet points for scannability, mobile-first.

**Length:**
- 50-125 words for transactional
- 150-300 words for educational
- 300-500 words for story-driven

**CTA:** One clear primary CTA per email. Action + outcome: "Start My Free Trial"

---

## Output Format

```
Sequence Name, Trigger, Goal, Length, Timing, Exit Conditions

Email [#]: [Name/Purpose]
Send: [Timing]
Subject: [Subject line]
Preview: [Preview text]
Body: [Full copy]
CTA: [Button text] → [Link destination]
```

---

## Related Skills

- **lead-magnets**: For planning lead magnets that feed into nurture sequences
- **churn-prevention**: For cancel flows, save offers, and dunning
- **onboarding**: For in-app onboarding (email supports this)
- **copywriting**: For landing pages emails link to
- **ab-testing**: For testing email elements
- **popups**: For email capture popups
- **revops**: For lifecycle stages that trigger email sequences
