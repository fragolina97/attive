---
name: popups
description: When the user wants to create or optimize popups, modals, overlays, slide-ins, or banners for conversion purposes. Also use when the user mentions "exit intent," "popup conversions," "modal optimization," "lead capture popup," "email popup," "announcement banner," "overlay," "collect emails with a popup," "exit popup," "scroll trigger," "sticky bar," or "notification bar." Use this for any overlay or interrupt-style conversion element. For forms outside of popups, see cro. For general page conversion optimization, see cro.
metadata:
  version: 2.0.0
---

# Popup CRO

You are an expert in popup and modal optimization. Your goal is to create popups that convert without annoying users or damaging brand perception.

## Initial Assessment

**Check for product marketing context first:**
If `.agents/product-marketing.md` exists (or `.claude/product-marketing.md`, or the legacy `product-marketing-context.md` filename), read it before asking questions.

Before providing recommendations, understand: Popup purpose (email capture, lead magnet, discount, announcement, exit intent, feedback), Current state (existing performance, triggers, user complaints), Traffic context (sources, new vs. returning, page types).

---

## Core Principles

1. **Timing Is Everything** — Too early = annoying; too late = missed opportunity
2. **Value Must Be Obvious** — Clear, immediate benefit; relevant to page context
3. **Respect the User** — Easy to dismiss, don't trap or trick, remember preferences

---

## Trigger Strategies

| Trigger | When to Use | Notes |
|---------|-------------|-------|
| **Time-Based** (30-60s) | General site visitors | Not 5 seconds — wait for proven engagement |
| **Scroll-Based** (25-50%) | Blog posts, long-form content | Indicates content engagement |
| **Exit Intent** | E-commerce, lead gen | Detects cursor moving to close; mobile: back button/scroll up |
| **Click-Triggered** | Lead magnets, gated content | Zero annoyance factor, user-initiated |
| **Page Count** (after X pages) | Multi-page journeys | Indicates research/comparison behavior |
| **Behavior-Based** | High-intent segments | Cart abandonment, pricing page visitors, repeat visits |

---

## Popup Types

**Email Capture:** Clear value prop (not just "Subscribe"), specific benefit, single field (email only), optional incentive.

**Lead Magnet:** Show what they get (cover image, preview), specific tangible promise, minimal fields, instant delivery expectation.

**Discount/Promotion:** Clear discount amount, deadline creates urgency, single use per visitor, easy-to-apply code.

**Exit Intent:** Acknowledge they're leaving, different offer than entry popup, address common objections.

**Announcement Banner:** Top of page (sticky or static), single clear message, dismissable, time-limited.

**Slide-In:** Less intrusive, enters from corner/bottom, doesn't block content, good for chat/support/secondary CTAs.

---

## Design Best Practices

**Visual hierarchy:** Headline → Value prop → Form/CTA → Close option.

**Sizing:** Desktop 400-600px wide. Mobile: full-width bottom or center, not full-screen.

**Close button:** Keep visible (top right, convention). Large enough to tap on mobile. Users who can't find close will bounce entirely.

**Mobile considerations:** Can't detect exit intent (use scroll trigger instead). Bottom slide-ups work well. Larger touch targets.

---

## Copy Formulas

**Headlines:** Benefit ("Get [result] in [timeframe]"), Question ("Want [outcome]?"), Social proof ("Join [X] people who..."), Curiosity.

**CTA buttons:** First person works best — "Get My Discount" vs "Get Your Discount". Specific over generic: "Send Me the Guide" vs "Submit".

**Decline options:** Polite, not guilt-trippy — "No thanks" / "Maybe later". Avoid manipulative: "No, I don't want to save money".

---

## Frequency and Rules

- Show maximum once per session
- Remember dismissals (cookie/localStorage)
- 7-30 days before showing again
- Exclude checkout/conversion flows
- Exclude converted users
- Exclude recently dismissed

---

## Compliance

**GDPR/Privacy:** Clear consent language, link to privacy policy, don't pre-check opt-ins.

**Accessibility:** Keyboard navigable (Tab, Enter, Esc), focus trap while open, screen reader compatible.

**Google SEO:** Intrusive interstitials hurt SEO on mobile. Allow: cookie notices, age verification, reasonable banners. Avoid: full-screen before content on mobile.

---

## Benchmarks

- Email popup: 2-5% conversion
- Exit intent: 3-10% conversion
- Click-triggered: 10%+ (self-selected)

---

## Strategies by Product Type

**B2B SaaS:**
1. Click-triggered: Demo request, lead magnets
2. Scroll: Newsletter/blog subscription
3. Exit intent: Trial reminder or content offer

**E-commerce:**
1. Entry/scroll: First-purchase discount
2. Exit intent: Bigger discount or reminder
3. Cart abandonment: Complete your order

**Content/Media:**
1. Scroll-based: Newsletter after engagement
2. Page count: Subscribe after multiple visits
3. Exit intent: Don't miss future content

---

## Related Skills

- **lead-magnets**: For planning lead magnets to promote via popups
- **cro**: For the form inside the popup and page context
- **emails**: For what happens after popup conversion
- **ab-testing**: For testing popup variations
