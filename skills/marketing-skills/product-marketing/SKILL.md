---
name: product-marketing
description: "When the user wants to create or update their product marketing context document. Also use when the user mentions 'product context,' 'marketing context,' 'set up context,' 'positioning,' 'who is my target audience,' 'describe my product,' 'ICP,' 'ideal customer profile,' or wants to avoid repeating foundational information across marketing tasks. Use this at the start of any new project before using other marketing skills — it creates `.agents/product-marketing.md` that all other skills reference for product, audience, and positioning context."
metadata:
  version: 2.0.0
---

# Product Marketing Context

You help users create and maintain a product marketing context document at `.agents/product-marketing.md`. This captures foundational positioning and messaging information that all other marketing skills reference automatically.

## Workflow

### Step 1: Check for Existing Context

First, check if `.agents/product-marketing.md` already exists. Also check `.claude/product-marketing.md` and the legacy `product-marketing-context.md` (in either location). If found outside `.agents/product-marketing.md`, offer to move it to the canonical location.

**If it exists:** Read it, summarize what's captured, ask which sections to update.

**If it doesn't exist, offer two options:**
1. **Auto-draft from codebase** (recommended): Study the repo (README, landing pages, marketing copy, package.json) and draft a V1. The user reviews and fills gaps. Ask: "What needs correcting? What's missing?"
2. **Start from scratch**: Walk through each section conversationally, one at a time.

### Step 2: Sections to Capture

1. **Product Overview** — One-liner, what it does, product category, type, business model
2. **Target Audience** — Company type, decision-makers, primary use case, jobs to be done, specific use cases
3. **Personas** (B2B) — User, Champion, Decision Maker, Financial Buyer, Technical Influencer + what each cares about
4. **Problems & Pain Points** — Core challenge, why alternatives fall short, what it costs, emotional tension
5. **Competitive Landscape** — Direct, secondary, indirect competitors and how each falls short
6. **Differentiation** — Key differentiators, how you do it differently, why customers choose you
7. **Objections & Anti-Personas** — Top 3 objections with responses; who is NOT a good fit
8. **Switching Dynamics** — Push (frustrations with current), Pull (what attracts to you), Habit (what keeps them stuck), Anxiety (worries about switching)
9. **Customer Language** — Exact phrases customers use for the problem and solution, words to use/avoid, glossary
10. **Brand Voice** — Tone, communication style, personality (3-5 adjectives)
11. **Proof Points** — Key metrics, notable customers, testimonials, value themes with evidence
12. **Goals** — Primary business goal, conversion action, current metrics

**Push for verbatim customer language.** Exact phrases are more valuable than polished descriptions — they reflect how customers actually think.

### Step 3: Create the Document

Save to `.agents/product-marketing.md`. After creating, tell them: "Other marketing skills will now use this context automatically. Run `/product-marketing` anytime to update it."

---

## Tips

- **Be specific**: "What's the #1 frustration that brings them to you?" not "What problem do they solve?"
- **Capture exact words**: Customer language beats polished descriptions
- **Ask for examples**: "Can you give me an example?" unlocks better answers
- **Validate as you go**: Summarize each section and confirm before moving on
- **Skip what doesn't apply**: Not every product needs all sections
