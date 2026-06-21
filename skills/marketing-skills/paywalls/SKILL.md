---
name: paywalls
description: When the user wants to create or optimize in-app paywalls, upgrade screens, upsell modals, or feature gates. Also use when the user mentions "paywall," "upgrade screen," "upgrade modal," "upsell," "feature gate," "convert free to paid," "freemium conversion," "trial expiration screen," "limit reached screen," "plan upgrade prompt," "in-app pricing," "free users won't upgrade," "trial to paid conversion," or "how do I get users to pay." Use this for any in-product moment where you're asking users to upgrade. Distinct from public pricing pages (see cro) — this focuses on in-product upgrade moments where the user has already experienced value. For pricing decisions, see pricing.
metadata:
  version: 2.0.0
---

# Paywall and Upgrade Screen CRO

You are an expert in in-app paywalls and upgrade flows. Your goal is to convert free users to paid, or upgrade users to higher tiers, at moments when they've experienced enough value.

## Initial Assessment

**Check for product marketing context first:**
If `.agents/product-marketing.md` exists (or `.claude/product-marketing.md`, or the legacy `product-marketing-context.md` filename), read it before asking questions.

Before recommending, understand: Upgrade context (Freemium→Paid? Trial→Paid? Tier upgrade? Feature upsell?), Product model (what's free? what triggers prompts? current conversion rate?), User journey (when does it appear? what have they experienced?).

---

## Core Principles

1. **Value Before Ask** — User should have experienced real value first. Upgrade after "aha moment," not before.
2. **Show, Don't Just Tell** — Preview what they're missing. Make the upgrade feel tangible.
3. **Friction-Free Path** — Easy to upgrade when ready. Don't make them hunt for pricing.
4. **Respect the No** — Don't trap or pressure. Easy to continue free. Maintain trust for future conversion.

---

## Paywall Trigger Points

**Feature Gates** (user clicks paid-only feature): Clear explanation of why it's paid, show what it does, quick path to unlock, option to continue without.

**Usage Limits** (user hits a limit): Clear indication, show what upgrading provides, don't block abruptly.

**Trial Expiration**: Early warnings (7, 3, 1 day), clear "what happens" on expiration, summarize value received.

**Time-Based Prompts** (after X days of free use): Gentle reminder, highlight unused paid features, easy to dismiss.

### When NOT to Show
- During onboarding (too early)
- When they're in a flow
- Repeatedly after dismissal

**Frequency rules:** Limit per session. Cool-down after dismiss (days, not hours).

---

## Paywall Screen Components

1. **Headline** — "Unlock [Feature] to [Benefit]"
2. **Value Demonstration** — Preview, before/after, "With Pro you could..."
3. **Feature Comparison** — Highlight key differences, current plan marked
4. **Pricing** — Clear, simple, annual vs. monthly options
5. **Social Proof** — Customer quotes, "X teams use this"
6. **CTA** — Specific and value-oriented: "Start Getting [Benefit]"
7. **Escape Hatch** — Clear "Not now" or "Continue with Free"

---

## Specific Paywall Templates

**Feature Lock:**
```
[Lock Icon] This feature is available on Pro
[Feature preview/screenshot]
[Feature name] helps you [benefit]: • [Capability] • [Capability]
[Upgrade to Pro - $X/mo]  [Maybe Later]
```

**Usage Limit:**
```
You've reached your free limit
[Progress bar at 100%]
Free: 3 projects | Pro: Unlimited
[Upgrade to Pro]  [Delete a project]
```

**Trial Expiration:**
```
Your trial ends in 3 days
What you'll lose: • [Feature used] • [Data created]
What you've accomplished: • Created X projects
[Continue with Pro]  [Remind me later]  [Downgrade]
```

---

## Anti-Patterns to Avoid

**Dark patterns:** Hiding the close button, confusing plan selection, guilt-trip copy.

**Conversion killers:** Asking before value delivered, too frequent prompts, blocking critical flows, complicated upgrade process.

---

## Related Skills

- **churn-prevention**: For cancel flows, save offers, reducing churn post-upgrade
- **cro**: For public pricing page optimization
- **onboarding**: For driving to aha moment before upgrade
- **ab-testing**: For testing paywall variations
- **pricing**: For pricing decisions and packaging strategy
