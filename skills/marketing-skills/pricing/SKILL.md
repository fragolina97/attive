---
name: pricing
description: "When the user wants help with pricing decisions, packaging, or monetization strategy. Also use when the user mentions 'pricing,' 'pricing tiers,' 'freemium,' 'free trial,' 'packaging,' 'price increase,' 'value metric,' 'Van Westendorp,' 'willingness to pay,' 'monetization,' 'how much should I charge,' 'my pricing is wrong,' 'pricing page,' 'annual vs monthly,' 'per seat pricing,' or 'should I offer a free plan.' Use this whenever someone is figuring out what to charge or how to structure their plans. For in-app upgrade screens, see paywalls."
metadata:
  version: 2.0.0
---

# Pricing Strategy

You are an expert in SaaS pricing and monetization strategy. Your goal is to help design pricing that captures value, drives growth, and aligns with customer willingness to pay.

## Before Starting

**Check for product marketing context first:**
If `.agents/product-marketing.md` exists (or `.claude/product-marketing.md`, or the legacy `product-marketing-context.md` filename), read it before asking questions.

---

## Pricing Fundamentals

### The Three Pricing Axes
1. **Packaging** — What's included at each tier (features, limits, support level)
2. **Pricing Metric** — What you charge for (per user, per usage, flat fee)
3. **Price Point** — The actual dollar amounts

### Value-Based Pricing
- **Customer's perceived value** — The ceiling
- **Your price** — Between alternatives and perceived value
- **Next best alternative** — The floor for differentiation
- **Your cost to serve** — Only a baseline, not the basis

---

## Value Metrics

The value metric is what you charge for — it should scale with the value customers receive.

| Metric | Best For | Example |
|--------|----------|---------|
| Per user/seat | Collaboration tools | Slack, Notion |
| Per usage | Variable consumption | AWS, Twilio |
| Per feature | Modular products | HubSpot add-ons |
| Per contact/record | CRM, email tools | Mailchimp |
| Per transaction | Payments, marketplaces | Stripe |
| Flat fee | Simple products | Basecamp |

**Choose wisely:** Ask "As a customer uses more of [metric], do they get more value?" If yes → good value metric.

---

## Tier Structure: Good-Better-Best

- **Good (Entry):** Core features, limited usage, low price
- **Better (Recommended):** Full features, reasonable limits, anchor price
- **Best (Premium):** Everything, advanced features, 2-3× Better price

**Tier differentiation:** Feature gating, usage limits, support level (email → priority → dedicated), access (API, SSO, custom branding).

---

## Pricing Research

**Van Westendorp Method** — Four questions:
1. Too expensive (wouldn't consider)
2. Too cheap (question quality)
3. Expensive but might consider
4. A bargain

Analyze intersections to find optimal pricing zone.

**MaxDiff Analysis** — Identifies which features customers value most for packaging decisions.

---

## When to Raise Prices

**Market signals:** Competitors raised prices, prospects don't flinch, "It's so cheap!" feedback.

**Business signals:** Very high conversion (>40%), very low churn (<3% monthly), strong unit economics.

**Strategies:** Grandfather existing customers | Announce 3-6 months out | Tie to added value | Plan restructure.

---

## Pricing Page Best Practices

**Above the fold:** Clear tier comparison table, recommended tier highlighted, monthly/annual toggle, primary CTA per tier.

**Common elements:** Feature comparison table, FAQ, annual discount callout (17-20%), money-back guarantee, customer logos.

**Psychology:** Anchoring (show higher-priced option first), Decoy effect (middle tier = best value), Charm pricing ($49 for value-focused), Round pricing ($50 for premium).

---

## Related Skills

- **churn-prevention**: For cancel flows and reducing revenue churn
- **cro**: For optimizing pricing page conversion
- **copywriting**: For pricing page copy
- **marketing-psychology**: For pricing psychology principles
- **paywalls**: For in-app upgrade screens
- **ab-testing**: For testing pricing changes
- **revops**: For deal desk and pipeline pricing
