---
name: ui-ux-pro-max
description: "UI/UX design intelligence. 67 styles, 96 palettes, 57 font pairings, 25 charts, 13 stacks (React, Next.js, Vue, Svelte, SwiftUI, React Native, Flutter, Tailwind, shadcn/ui). Actions: plan, build, create, design, implement, review, fix, improve, optimize, enhance, refactor, check UI/UX code. Projects: website, landing page, dashboard, admin panel, e-commerce, SaaS, portfolio, blog, mobile app, .html, .tsx, .vue, .svelte. Elements: button, modal, navbar, sidebar, card, table, form, chart. Styles: glassmorphism, claymorphism, minimalism, brutalism, neumorphism, bento grid, dark mode, responsive, skeuomorphism, flat design. Topics: color palette, accessibility, animation, layout, typography, font pairing, spacing, hover, shadow, gradient. Integrations: shadcn/ui MCP for component search and examples."
---
# UI/UX Pro Max - Design Intelligence

Comprehensive design guide for web and mobile applications. Contains 67 styles, 96 color palettes, 57 font pairings, 99 UX guidelines, and 25 chart types across 13 technology stacks.

## Rule Categories by Priority

| Priority | Category | Impact | Domain |
|----------|----------|--------|--------|
| 1 | Accessibility | CRITICAL | `ux` |
| 2 | Touch & Interaction | CRITICAL | `ux` |
| 3 | Performance | HIGH | `ux` |
| 4 | Layout & Responsive | HIGH | `ux` |
| 5 | Typography & Color | MEDIUM | `typography`, `color` |
| 6 | Animation | MEDIUM | `ux` |
| 7 | Style Selection | MEDIUM | `style`, `product` |
| 8 | Charts & Data | LOW | `chart` |

## How to Use

### Step 1: Analyze Requirements
- **Product type**: SaaS, e-commerce, portfolio, dashboard, landing page
- **Style keywords**: minimal, playful, professional, elegant, dark mode
- **Industry**: healthcare, fintech, gaming, education
- **Stack**: React, Vue, Next.js — default: `html-tailwind`

### Step 2: Generate Design System (REQUIRED)

```bash
python3 skills/ui-ux-pro-max/scripts/search.py "<product_type> <keywords>" --design-system [-p "Project Name"]
```

Searches 5 domains in parallel, applies reasoning rules, returns complete design system.

### Step 2b: Persist Design System

```bash
python3 skills/ui-ux-pro-max/scripts/search.py "<query>" --design-system --persist -p "Project Name"
```

Creates `design-system/MASTER.md` + `design-system/pages/` for page-specific overrides.

### Step 3: Domain Searches (as needed)

```bash
python3 skills/ui-ux-pro-max/scripts/search.py "<keyword>" --domain <domain>
```

Domains: `product` `style` `typography` `color` `landing` `chart` `ux` `react` `web` `prompt`

### Step 4: Stack Guidelines

```bash
python3 skills/ui-ux-pro-max/scripts/search.py "<keyword>" --stack html-tailwind
```

Stacks: `html-tailwind` `react` `nextjs` `vue` `svelte` `swiftui` `react-native` `flutter` `shadcn` `jetpack-compose`

## Common Rules for Professional UI

| Rule | Do | Don't |
|------|----|----- |
| **No emoji icons** | SVG icons (Heroicons, Lucide) | Emojis as UI icons |
| **Cursor pointer** | `cursor-pointer` su tutti i clickable | Default cursor su interattivi |
| **Glass card light** | `bg-white/80` o higher | `bg-white/10` (invisibile) |
| **Text contrast light** | `#0F172A` (slate-900) | `#94A3B8` (slate-400) |
| **Floating navbar** | `top-4 left-4 right-4` | `top-0 left-0 right-0` |

## Pre-Delivery Checklist

- [ ] No emojis as icons · All icons consistent set · Hover no layout shift
- [ ] All clickable have `cursor-pointer` · Transitions 150-300ms
- [ ] Light mode contrast ≥ 4.5:1 · Borders visible both modes
- [ ] Responsive 375/768/1024/1440px · No horizontal scroll mobile
- [ ] All images alt text · Form inputs have labels

## Prerequisites

Python 3 required for scripts. Install: `winget install Python.Python.3.12` (Windows) · `brew install python3` (macOS)
