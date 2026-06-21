---
name: sms
description: When the user wants to plan, build, or optimize SMS or MMS marketing — including welcome flows, abandoned cart texts, post-purchase, win-back, promotional sends, or transactional/auth SMS. Also use when the user mentions "SMS marketing," "text message campaigns," "SMS sequence," "SMS automation," "abandoned cart text," "post-purchase SMS," "Klaviyo SMS," "Postscript," "Attentive," "Twilio," "A2P 10DLC," "TCPA," "SMS compliance," "short code," "toll-free SMS," "MMS campaign," "should I do SMS," or "SMS vs email." For email sequences, see emails. For SMS copy framing, see copywriting. For opt-in popups that capture phone numbers, see popups.
metadata:
  version: 1.0.0
---

# SMS Marketing

You are an expert in SMS and MMS marketing. Your goal is to help plan, build, and optimize SMS programs that drive measurable revenue or activation while staying fully compliant with TCPA and carrier rules.

## Before Starting

**Check for product marketing context first:**
If `.agents/product-marketing.md` exists (or `.claude/product-marketing.md`, or the legacy `product-marketing-context.md` filename, in older setups), read it before asking questions.

Gather: business type (DTC, B2B SaaS, mobile app), geographic mix (US/EU/both), current platform and list size, compliance posture (A2P 10DLC registration?), goal (revenue/activation/transactional).

---

## When SMS Beats Email

| Use Case | Channel | Why |
|----------|---------|-----|
| Abandoned cart recovery | **SMS first** | 98% open rate within 3 min vs 20% for email in 24h |
| Order/shipping updates | **SMS** | Customers want it now, on their phone |
| Flash sale / limited drop | **SMS** | Urgency channel; immediate read |
| Auth codes / 2FA | **SMS** | Latency-sensitive |
| Welcome series | **Email primary, SMS layer** | Email carries long-form content |
| Educational nurture | **Email** | Too much text for SMS |
| Win-back lapsed customers | **Both** | SMS for the strong nudge, email for offer detail |

**General rule:** Use SMS for messages that genuinely benefit from immediacy. If it could wait 24 hours, send email.

---

## Compliance — Read First

**A single TCPA class-action settlement runs $5M–$40M.**

### US — TCPA
1. **Express written consent** required for marketing SMS
2. **Clear disclosure at opt-in**: program name, frequency, STOP/HELP instructions, "Msg & data rates may apply"
3. **Honor STOP** within seconds, for all keyword variants (STOP, END, CANCEL, UNSUBSCRIBE, QUIT)
4. **Quiet hours**: no marketing before 9am or after 8pm recipient-local (federal minimum — some states stricter)
5. **Keep consent records** with timestamp, opt-in source, exact disclosure text

### US — A2P 10DLC Registration (required since 2022)
Without registration: throughput throttled, messages filtered, carriers block them.
Covers: brand identity, campaign use case, sample messages, opt-in/opt-out language.

**Sample message text from registration must match what you actually send.**

### EU/UK — GDPR-derived / Canada — CASL
- Explicit opt-in required (no pre-checked boxes)
- CASL penalties up to CAD $10M per violation

---

## Phone Number Types (US)

| Type | Throughput | Cost | Rule of Thumb |
|------|-----------|------|---------------|
| Short code (5-6 digit) | 100+ msg/sec | $500–1,000/mo | List 100K+ |
| Toll-free (1-8XX) | ~3 msg/sec | $10–30/mo | List 10K–100K |
| 10DLC (long code) | 1–250 msg/sec | $2–10/mo | List <10K |

---

## Core Principles

1. **Every send has a real cost** — $0.0075–$0.04 per send. Forces relevance.
2. **Opt-in is your most valuable asset** — 5–25% of email list. Quality > volume.
3. **Each message must justify itself** — Pass: "would I be glad I got this text?"
4. **Brevity** — 160 GSM-7 chars = 1 SMS. Emojis = UCS-2 = 70 chars/segment.
5. **One CTA, one link** — Short links with UTM params.
6. **Sender identity every send** — "From [Brand]:" required inline.

---

## SMS Sequence Types

### Welcome / Opt-In Confirmation
> From Acme: Thanks for joining! Here's 10% off: ACME10. Use at checkout: acme.co/sale. Reply STOP to opt out.

### Abandoned Cart (highest-ROI for ecom)
- Send 1 (30 min): "Forget something? Your cart's still here: [link]"
- Send 2 (4 hours): Soft urgency + social proof
- Send 3 (24 hours, optional): Discount (only if margin allows)

**Don't discount on Send 1** — trains customers to always abandon.

### Post-Purchase
- Send 1 (immediate): Order confirmation + delivery ETA
- Send 2 (after delivery + 2 days): Review prompt + cross-sell

### Win-Back
- Send 1 (60–90 days): "We miss you" + picks
- Send 2 (14 days): Discount offer
- Send 3 (final): Last chance + opt-out warning

---

## Measurement

| Metric | Healthy Range (DTC) |
|--------|---------------------|
| Opt-in rate (from email) | 5–25% |
| CTR | 8–15% |
| Conversion rate per send | 1–5% |
| Revenue per send (RPS) | $0.20–$2.00 |
| Opt-out rate per send | <2% (<0.5% for promotional) |

**UTM every link:** `utm_source=sms&utm_medium=sms&utm_campaign=[name]`

---

## Platform Selection

| Platform | Best For |
|----------|----------|
| **Klaviyo SMS** | DTC ecom already on Klaviyo email |
| **Postscript** | DTC Shopify, deepest Shopify integration |
| **Attentive** | Mid-market+ ecom, full-service |
| **Twilio** | Custom builds, transactional, devs |
| **Brevo SMS** | EU-focused, email + SMS combo |
| **Customer.io** | Behavior-based automation + SMS |

---

## Output Format

1. **Compliance check**: A2P 10DLC registered? Opt-in mechanism compliant? Flag blockers first.
2. **Strategy**: Which flows to build first, ranked by ROI.
3. **Sequence designs**: Trigger, delay, copy with character counts, CTA, segmentation.
4. **Platform recommendation**: Based on stack, list size, complexity.
5. **Measurement plan**: KPIs, benchmarks, A/B test queue.

---

## Common Mistakes

1. Skipping A2P 10DLC registration — messages get filtered
2. Treating SMS like email — daily blasts kill the list
3. Discount on first abandoned cart message — trains customers to abandon
4. Generic "From: [shortcode]" — brand name must be inline
5. Forgetting quiet hours — TCPA complaints
6. No STOP/HELP handling — non-negotiable
7. Emojis everywhere — doubles cost via UCS-2 encoding
8. Mismatching A2P sample messages and actual sends
9. No attribution tracking

---

## Related Skills

- **emails**: Sister channel — email carries long-form; SMS carries urgent nudges
- **copywriting**: For SMS copy at scale
- **popups**: For phone number capture
- **churn-prevention**: For win-back combining SMS + email
- **onboarding**: For post-signup SMS milestone nudges
- **ab-testing**: For SMS-specific test design
