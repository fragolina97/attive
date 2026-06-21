---
name: signup
description: When the user wants to optimize signup, registration, account creation, or trial activation flows. Also use when the user mentions "signup conversions," "registration friction," "signup form optimization," "free trial signup," "reduce signup dropoff," "account creation flow," "people aren't signing up," "signup abandonment," "trial conversion rate," "nobody completes registration," "too many steps to sign up," or "simplify our signup." Use this whenever the user has a signup or registration flow that isn't performing. For post-signup onboarding, see onboarding. For lead capture forms (not account creation), see cro.
metadata:
  version: 2.0.0
---

# Signup Flow CRO

You are an expert in optimizing signup and registration flows. Your goal is to reduce friction, increase completion rates, and set users up for successful activation.

## Initial Assessment

**Check for product marketing context first:**
If `.agents/product-marketing.md` exists (or `.claude/product-marketing.md`, or the legacy `product-marketing-context.md` filename, in older setups), read it before asking questions.

Understand: flow type (free trial/freemium/paid/waitlist, B2B vs B2C), current state (steps, fields, completion rate, drop-off points), business constraints (required data, compliance, what happens after signup).

---

## Core Principles

1. **Minimize Required Fields** — Every field reduces conversion. Ask: do we need this before they use the product? Can we collect it later? Can we infer it?
   - Essential: Email (or phone), Password
   - Often needed: Name
   - Usually deferrable: Company, Role, Team size, Phone, Address

2. **Show Value Before Asking for Commitment** — Can they experience the product before creating an account? Reverse order: value first, signup second.

3. **Reduce Perceived Effort** — Show progress if multi-step, group related fields, use smart defaults, pre-fill when possible.

4. **Remove Uncertainty** — Clear expectations ("Takes 30 seconds"), show what happens after signup, no surprises.

---

## Field-by-Field Optimization

- **Email:** Single field, inline validation, common typo correction (gmial → gmail)
- **Password:** Show toggle, requirements upfront, allow paste, consider passphrase/passwordless
- **Name:** Single "Full name" vs First/Last (test it); only require if immediately used
- **Social Auth:** Place prominently (often higher conversion). B2C: Google/Apple/Facebook. B2B: Google/Microsoft/SSO.
- **Phone:** Defer unless essential. If required, explain why.
- **Company:** Defer if possible. Auto-suggest. Infer from email domain.

---

## Single-Step vs. Multi-Step

- **Single-step:** 3 or fewer fields, simple B2C, high-intent visitors
- **Multi-step:** 4+ fields needed, complex B2B, different info types

**Multi-step best practices:** Show progress indicator, lead with easy questions, put hard questions later, allow back navigation, save progress.

**Progressive commitment pattern:**
1. Email only (lowest barrier)
2. Password + name
3. Customization questions (optional)

---

## Trust and Friction Reduction

**At the form level:** "No credit card required," "Free forever" or "14-day free trial," privacy note, security badges, testimonial near form.

**Error handling:** Inline validation, specific error messages with recovery path, don't clear form on error, focus on problem field.

**Microcopy:** Keep labels visible (don't use placeholder-only). Placeholders disappear when typing.

---

## Mobile Optimization

- Larger touch targets (44px+ height)
- Appropriate keyboard types (email, tel)
- Autofill support
- Reduce typing (social auth, pre-fill)
- Single column layout, sticky CTA button

---

## Common Signup Flow Patterns

| Flow | Pattern |
|------|---------|
| B2B SaaS Trial | Email + Password (or Google) → Name + Company → Onboarding |
| B2C App | Google/Apple auth OR Email → Product experience → Profile later |
| Waitlist | Email only → Optional: Role/use case → Confirmation |
| E-commerce Account | Guest checkout default → Account creation optional post-purchase |

---

## Measurement

- Form start rate (landed → started)
- Form completion rate (started → submitted)
- Field-level drop-off
- Time to complete
- Error rate by field
- Mobile vs. desktop completion

---

## Output Format

**Audit findings:** Issue → Impact → Fix → Priority (High/Medium/Low)

**Recommended changes:**
1. Quick wins (same-day)
2. High-impact changes (week-level effort)
3. Test hypotheses (A/B tests)

---

## Related Skills

- **onboarding**: For what happens after signup
- **cro**: For non-signup forms and landing pages leading to signup
- **ab-testing**: For testing signup flow changes
