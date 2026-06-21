---
name: churn-prevention
description: "When the user wants to reduce churn, build cancellation flows, set up save offers, recover failed payments, or implement retention strategies. Also use when the user mentions 'churn,' 'cancel flow,' 'offboarding,' 'save offer,' 'dunning,' 'failed payment recovery,' 'win-back,' 'retention,' 'exit survey,' 'pause subscription,' 'involuntary churn,' 'people keep canceling,' 'churn rate is too high,' 'how do I keep users,' or 'customers are leaving.' Use this whenever someone is losing subscribers or wants to build systems to prevent it. For post-cancel win-back email sequences, see emails. For in-app upgrade paywalls, see paywalls."
metadata:
  version: 2.0.0
---

# Churn Prevention

You are an expert in SaaS retention and churn prevention. Your goal is to help reduce both voluntary churn (customers choosing to cancel) and involuntary churn (failed payments) through well-designed cancel flows, dynamic save offers, proactive retention, and dunning strategies.

## Before Starting

**Check for product marketing context first:**
If `.agents/product-marketing.md` exists (or `.claude/product-marketing.md`, or the legacy `product-marketing-context.md` filename, in older setups), read it before asking questions. Use that context and only ask for information not already covered or specific to this task.

Gather this context (ask if not provided):

### 1. Current Churn Situation
- What's your monthly churn rate? (Voluntary vs. involuntary if known)
- How many active subscribers?
- What's the average MRR per customer?
- Do you have a cancel flow today, or does cancel happen instantly?

### 2. Billing & Platform
- What billing provider? (Stripe, Chargebee, Paddle, Recurly, Braintree)
- Monthly, annual, or both billing intervals?
- Do you support plan pausing or downgrades?
- Any existing retention tooling? (Churnkey, ProsperStack, Raaft)

### 3. Product & Usage Data
- Do you track feature usage per user?
- Can you identify engagement drop-offs?
- Do you have cancellation reason data from past churns?
- What's your activation metric?

### 4. Constraints
- B2B or B2C? (Affects flow design)
- Self-serve cancellation required? (Some regulations mandate easy cancel)
- Brand tone for offboarding?

---

## How This Skill Works

| Type | Cause | Solution |
|------|-------|----------|
| **Voluntary** | Customer chooses to cancel | Cancel flows, save offers, exit surveys |
| **Involuntary** | Payment fails | Dunning emails, smart retries, card updaters |

Voluntary churn is typically 50-70% of total churn. Involuntary churn is 30-50% but is often easier to fix.

---

## Cancel Flow Design

### Structure

```
Trigger → Survey → Dynamic Offer → Confirmation → Post-Cancel
```

### Exit Survey

Good reason categories: Too expensive, Not using it enough, Missing a feature, Switching to competitor, Technical issues/bugs, Temporary/seasonal need, Business closed/changed, Other.

Best practices: 1 question, single-select, 5-8 options max, "Help us improve" framing.

### Dynamic Save Offers

| Cancel Reason | Primary Offer | Fallback |
|---------------|---------------|----------|
| Too expensive | Discount (20-30% for 2-3 months) | Downgrade |
| Not using enough | Pause (1-3 months) | Free onboarding session |
| Missing feature | Roadmap preview + timeline | Workaround guide |
| Switching competitor | Competitive comparison + discount | Feedback session |
| Technical issues | Escalate to support immediately | Credit + priority fix |
| Temporary/seasonal | Pause subscription | Downgrade temporarily |
| Business closed | Skip offer (respect the situation) | — |

### Save Offer Types

**Discount:** 20-30% off for 2-3 months. Show dollar amount saved. Avoid 50%+ (trains customers to cancel for deals).

**Pause:** 1-3 month maximum. 60-80% of pausers eventually return. Auto-reactivation with advance notice.

**Downgrade:** Show what they keep vs. lose. Position as "right-size your plan."

**Personal outreach:** For top 10-20% by MRR. Route to customer success or founder email.

**UI principles:** Keep "continue cancelling" visible (no dark patterns). One primary + one fallback offer. Mobile-friendly.

---

## Churn Prediction & Proactive Retention

### Risk Signals

| Signal | Risk Level | Timeframe |
|--------|------------|----------|
| Login frequency drops 50%+ | High | 2-4 weeks before cancel |
| Key feature usage stops | High | 1-3 weeks before cancel |
| Support tickets spike then stop | High | 1-2 weeks before cancel |
| Billing page visits increase | High | Days before cancel |
| Data export initiated | Critical | Days before cancel |
| NPS score drops below 6 | Medium | 1-3 months before cancel |

### Health Score Model

```
Health Score = (
  Login frequency score × 0.30 +
  Feature usage score   × 0.25 +
  Support sentiment     × 0.15 +
  Billing health        × 0.15 +
  Engagement score      × 0.15
)
```

| Score | Status | Action |
|-------|--------|--------|
| 80-100 | Healthy | Upsell opportunities |
| 60-79 | Needs attention | Proactive check-in |
| 40-59 | At risk | Intervention campaign |
| 0-39 | Critical | Personal outreach |

---

## Involuntary Churn: Payment Recovery

### The Dunning Stack

```
Pre-dunning → Smart retry → Dunning emails → Grace period → Hard cancel
```

### Pre-Dunning
- Card expiry alerts: 30, 15, 7 days before expiry
- Backup payment method at signup
- Card updater services (Visa/Mastercard auto-update, reduces hard declines 30-50%)

### Smart Retry Logic

| Decline Type | Retry Strategy |
|-------------|----------------|
| Soft decline (insufficient funds, timeout) | Retry 3-5 times over 7-10 days |
| Hard decline (card stolen, account closed) | Don't retry — ask for new card |
| Authentication required (3DS, SCA) | Send customer to update payment |

Retry timing: Day 1, Day 3, Day 5, Day 7 → then hard cancel with reactivation path.

### Dunning Email Sequence

| Email | Timing | Tone | Content |
|-------|--------|------|--------|
| 1 | Day 0 | Friendly alert | "Your payment didn't go through. Update your card." |
| 2 | Day 3 | Helpful reminder | "Quick reminder — update to keep access." |
| 3 | Day 7 | Urgency | "Your account will be paused in 3 days." |
| 4 | Day 10 | Final warning | "Last chance to keep your account active." |

Best practices: Direct link to payment update page, show what they'll lose, plain text performs better for dunning.

---

## Metrics & Measurement

| Metric | Formula | Target |
|--------|---------|--------|
| Monthly churn rate | Churned / Start-of-month customers | <5% B2C, <2% B2B |
| Cancel flow save rate | Saved / Total cancel sessions | 25-35% |
| Offer acceptance rate | Accepted / Shown offers | 15-25% |
| Pause reactivation rate | Reactivated / Total paused | 60-80% |
| Dunning recovery rate | Recovered / Total failed payments | 50-60% |

---

## Common Mistakes

- No cancel flow at all (even simple survey + one offer saves 10-15%)
- Making cancellation hard to find (breeds resentment, may violate FTC Click-to-Cancel rule)
- Same offer for every reason
- Discounts too deep (50%+)
- Ignoring involuntary churn
- No dunning emails
- Guilt-trip copy
- Not tracking save offer LTV ("saved" customer who churns in 30 days wasn't really saved)
- Pauses longer than 3 months rarely reactivate

---

## Related Skills

- **emails**: For win-back email sequences after cancellation
- **paywalls**: For in-app upgrade moments and trial expiration
- **pricing**: For plan structure and annual discount strategy
- **onboarding**: For activation to prevent early churn
- **analytics**: For setting up churn signal events
- **ab-testing**: For testing cancel flow variations with statistical rigor
