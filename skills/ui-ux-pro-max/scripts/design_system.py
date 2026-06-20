#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Design System Generator - Aggregates search results and applies reasoning
to generate comprehensive design system recommendations.

Usage:
    from design_system import generate_design_system
    result = generate_design_system("SaaS dashboard", "My Project")
    result = generate_design_system("SaaS dashboard", "My Project", persist=True)
    result = generate_design_system("SaaS dashboard", "My Project", persist=True, page="dashboard")
"""

import csv
import json
import os
from datetime import datetime
from pathlib import Path
from core import search, DATA_DIR

REASONING_FILE = "ui-reasoning.csv"

SEARCH_CONFIG = {
    "product": {"max_results": 1},
    "style": {"max_results": 3},
    "color": {"max_results": 2},
    "landing": {"max_results": 2},
    "typography": {"max_results": 2}
}


class DesignSystemGenerator:
    def __init__(self):
        self.reasoning_data = self._load_reasoning()

    def _load_reasoning(self):
        filepath = DATA_DIR / REASONING_FILE
        if not filepath.exists():
            return []
        with open(filepath, 'r', encoding='utf-8') as f:
            return list(csv.DictReader(f))

    def _multi_domain_search(self, query, style_priority=None):
        results = {}
        for domain, config in SEARCH_CONFIG.items():
            if domain == "style" and style_priority:
                priority_query = " ".join(style_priority[:2]) if style_priority else query
                combined_query = f"{query} {priority_query}"
                results[domain] = search(combined_query, domain, config["max_results"])
            else:
                results[domain] = search(query, domain, config["max_results"])
        return results

    def _find_reasoning_rule(self, category):
        category_lower = category.lower()
        for rule in self.reasoning_data:
            if rule.get("UI_Category", "").lower() == category_lower:
                return rule
        for rule in self.reasoning_data:
            ui_cat = rule.get("UI_Category", "").lower()
            if ui_cat in category_lower or category_lower in ui_cat:
                return rule
        for rule in self.reasoning_data:
            ui_cat = rule.get("UI_Category", "").lower()
            keywords = ui_cat.replace("/", " ").replace("-", " ").split()
            if any(kw in category_lower for kw in keywords):
                return rule
        return {}

    def _apply_reasoning(self, category, search_results):
        rule = self._find_reasoning_rule(category)
        if not rule:
            return {
                "pattern": "Hero + Features + CTA",
                "style_priority": ["Minimalism", "Flat Design"],
                "color_mood": "Professional",
                "typography_mood": "Clean",
                "key_effects": "Subtle hover transitions",
                "anti_patterns": "",
                "decision_rules": {},
                "severity": "MEDIUM"
            }
        decision_rules = {}
        try:
            decision_rules = json.loads(rule.get("Decision_Rules", "{}"))
        except json.JSONDecodeError:
            pass
        return {
            "pattern": rule.get("Recommended_Pattern", ""),
            "style_priority": [s.strip() for s in rule.get("Style_Priority", "").split("+")],
            "color_mood": rule.get("Color_Mood", ""),
            "typography_mood": rule.get("Typography_Mood", ""),
            "key_effects": rule.get("Key_Effects", ""),
            "anti_patterns": rule.get("Anti_Patterns", ""),
            "decision_rules": decision_rules,
            "severity": rule.get("Severity", "MEDIUM")
        }

    def _select_best_match(self, results, priority_keywords):
        if not results:
            return {}
        if not priority_keywords:
            return results[0]
        for priority in priority_keywords:
            priority_lower = priority.lower().strip()
            for result in results:
                style_name = result.get("Style Category", "").lower()
                if priority_lower in style_name or style_name in priority_lower:
                    return result
        scored = []
        for result in results:
            result_str = str(result).lower()
            score = 0
            for kw in priority_keywords:
                kw_lower = kw.lower().strip()
                if kw_lower in result.get("Style Category", "").lower():
                    score += 10
                elif kw_lower in result.get("Keywords", "").lower():
                    score += 3
                elif kw_lower in result_str:
                    score += 1
            scored.append((score, result))
        scored.sort(key=lambda x: x[0], reverse=True)
        return scored[0][1] if scored and scored[0][0] > 0 else results[0]

    def _extract_results(self, search_result):
        return search_result.get("results", [])

    def generate(self, query, project_name=None):
        product_result = search(query, "product", 1)
        product_results = product_result.get("results", [])
        category = "General"
        if product_results:
            category = product_results[0].get("Product Type", "General")
        reasoning = self._apply_reasoning(category, {})
        style_priority = reasoning.get("style_priority", [])
        search_results = self._multi_domain_search(query, style_priority)
        search_results["product"] = product_result
        style_results = self._extract_results(search_results.get("style", {}))
        color_results = self._extract_results(search_results.get("color", {}))
        typography_results = self._extract_results(search_results.get("typography", {}))
        landing_results = self._extract_results(search_results.get("landing", {}))
        best_style = self._select_best_match(style_results, reasoning.get("style_priority", []))
        best_color = color_results[0] if color_results else {}
        best_typography = typography_results[0] if typography_results else {}
        best_landing = landing_results[0] if landing_results else {}
        style_effects = best_style.get("Effects & Animation", "")
        reasoning_effects = reasoning.get("key_effects", "")
        combined_effects = style_effects if style_effects else reasoning_effects
        return {
            "project_name": project_name or query.upper(),
            "category": category,
            "pattern": {
                "name": best_landing.get("Pattern Name", reasoning.get("pattern", "Hero + Features + CTA")),
                "sections": best_landing.get("Section Order", "Hero > Features > CTA"),
                "cta_placement": best_landing.get("Primary CTA Placement", "Above fold"),
                "color_strategy": best_landing.get("Color Strategy", ""),
                "conversion": best_landing.get("Conversion Optimization", "")
            },
            "style": {
                "name": best_style.get("Style Category", "Minimalism"),
                "type": best_style.get("Type", "General"),
                "effects": style_effects,
                "keywords": best_style.get("Keywords", ""),
                "best_for": best_style.get("Best For", ""),
                "performance": best_style.get("Performance", ""),
                "accessibility": best_style.get("Accessibility", "")
            },
            "colors": {
                "primary": best_color.get("Primary (Hex)", "#2563EB"),
                "secondary": best_color.get("Secondary (Hex)", "#3B82F6"),
                "cta": best_color.get("CTA (Hex)", "#F97316"),
                "background": best_color.get("Background (Hex)", "#F8FAFC"),
                "text": best_color.get("Text (Hex)", "#1E293B"),
                "notes": best_color.get("Notes", "")
            },
            "typography": {
                "heading": best_typography.get("Heading Font", "Inter"),
                "body": best_typography.get("Body Font", "Inter"),
                "mood": best_typography.get("Mood/Style Keywords", reasoning.get("typography_mood", "")),
                "best_for": best_typography.get("Best For", ""),
                "google_fonts_url": best_typography.get("Google Fonts URL", ""),
                "css_import": best_typography.get("CSS Import", "")
            },
            "key_effects": combined_effects,
            "anti_patterns": reasoning.get("anti_patterns", ""),
            "decision_rules": reasoning.get("decision_rules", {}),
            "severity": reasoning.get("severity", "MEDIUM")
        }


BOX_WIDTH = 90

def format_ascii_box(design_system):
    project = design_system.get("project_name", "PROJECT")
    pattern = design_system.get("pattern", {})
    style = design_system.get("style", {})
    colors = design_system.get("colors", {})
    typography = design_system.get("typography", {})
    effects = design_system.get("key_effects", "")
    anti_patterns = design_system.get("anti_patterns", "")

    def wrap_text(text, prefix, width):
        if not text:
            return []
        words = text.split()
        lines = []
        current_line = prefix
        for word in words:
            if len(current_line) + len(word) + 1 <= width - 2:
                current_line += (" " if current_line != prefix else "") + word
            else:
                if current_line != prefix:
                    lines.append(current_line)
                current_line = prefix + word
        if current_line != prefix:
            lines.append(current_line)
        return lines

    sections = pattern.get("sections", "").split(">")
    sections = [s.strip() for s in sections if s.strip()]
    lines = []
    w = BOX_WIDTH - 1
    lines.append("+" + "-" * w + "+")
    lines.append(f"|  TARGET: {project} - RECOMMENDED DESIGN SYSTEM".ljust(BOX_WIDTH) + "|")
    lines.append("+" + "-" * w + "+")
    lines.append("|" + " " * BOX_WIDTH + "|")
    lines.append(f"|  PATTERN: {pattern.get('name', '')}".ljust(BOX_WIDTH) + "|")
    if pattern.get('conversion'):
        lines.append(f"|     Conversion: {pattern.get('conversion', '')}".ljust(BOX_WIDTH) + "|")
    if pattern.get('cta_placement'):
        lines.append(f"|     CTA: {pattern.get('cta_placement', '')}".ljust(BOX_WIDTH) + "|")
    lines.append("|     Sections:".ljust(BOX_WIDTH) + "|")
    for i, section in enumerate(sections, 1):
        lines.append(f"|       {i}. {section}".ljust(BOX_WIDTH) + "|")
    lines.append("|" + " " * BOX_WIDTH + "|")
    lines.append(f"|  STYLE: {style.get('name', '')}".ljust(BOX_WIDTH) + "|")
    if style.get("keywords"):
        for line in wrap_text(f"Keywords: {style.get('keywords', '')}", "|     ", BOX_WIDTH):
            lines.append(line.ljust(BOX_WIDTH) + "|")
    if style.get("best_for"):
        for line in wrap_text(f"Best For: {style.get('best_for', '')}", "|     ", BOX_WIDTH):
            lines.append(line.ljust(BOX_WIDTH) + "|")
    lines.append("|" + " " * BOX_WIDTH + "|")
    lines.append("|  COLORS:".ljust(BOX_WIDTH) + "|")
    lines.append(f"|     Primary:    {colors.get('primary', '')}".ljust(BOX_WIDTH) + "|")
    lines.append(f"|     Secondary:  {colors.get('secondary', '')}".ljust(BOX_WIDTH) + "|")
    lines.append(f"|     CTA:        {colors.get('cta', '')}".ljust(BOX_WIDTH) + "|")
    lines.append(f"|     Background: {colors.get('background', '')}".ljust(BOX_WIDTH) + "|")
    lines.append(f"|     Text:       {colors.get('text', '')}".ljust(BOX_WIDTH) + "|")
    lines.append("|" + " " * BOX_WIDTH + "|")
    lines.append(f"|  TYPOGRAPHY: {typography.get('heading', '')} / {typography.get('body', '')}".ljust(BOX_WIDTH) + "|")
    if typography.get("mood"):
        for line in wrap_text(f"Mood: {typography.get('mood', '')}", "|     ", BOX_WIDTH):
            lines.append(line.ljust(BOX_WIDTH) + "|")
    lines.append("|" + " " * BOX_WIDTH + "|")
    if effects:
        lines.append("|  KEY EFFECTS:".ljust(BOX_WIDTH) + "|")
        for line in wrap_text(effects, "|     ", BOX_WIDTH):
            lines.append(line.ljust(BOX_WIDTH) + "|")
        lines.append("|" + " " * BOX_WIDTH + "|")
    if anti_patterns:
        lines.append("|  AVOID (Anti-patterns):".ljust(BOX_WIDTH) + "|")
        for line in wrap_text(anti_patterns, "|     ", BOX_WIDTH):
            lines.append(line.ljust(BOX_WIDTH) + "|")
        lines.append("|" + " " * BOX_WIDTH + "|")
    lines.append("|  PRE-DELIVERY CHECKLIST:".ljust(BOX_WIDTH) + "|")
    for item in ["[ ] No emojis as icons", "[ ] cursor-pointer on clickable elements",
                 "[ ] Hover states 150-300ms", "[ ] Light mode contrast 4.5:1",
                 "[ ] Focus states visible", "[ ] prefers-reduced-motion respected",
                 "[ ] Responsive: 375px, 768px, 1024px, 1440px"]:
        lines.append(f"|     {item}".ljust(BOX_WIDTH) + "|")
    lines.append("|" + " " * BOX_WIDTH + "|")
    lines.append("+" + "-" * w + "+")
    return "\n".join(lines)


def format_markdown(design_system):
    project = design_system.get("project_name", "PROJECT")
    pattern = design_system.get("pattern", {})
    style = design_system.get("style", {})
    colors = design_system.get("colors", {})
    typography = design_system.get("typography", {})
    effects = design_system.get("key_effects", "")
    anti_patterns = design_system.get("anti_patterns", "")
    lines = []
    lines.append(f"## Design System: {project}")
    lines.append("")
    lines.append("### Pattern")
    lines.append(f"- **Name:** {pattern.get('name', '')}")
    if pattern.get('conversion'):
        lines.append(f"- **Conversion Focus:** {pattern.get('conversion', '')}")
    if pattern.get('cta_placement'):
        lines.append(f"- **CTA Placement:** {pattern.get('cta_placement', '')}")
    lines.append(f"- **Sections:** {pattern.get('sections', '')}")
    lines.append("")
    lines.append("### Style")
    lines.append(f"- **Name:** {style.get('name', '')}")
    if style.get('keywords'):
        lines.append(f"- **Keywords:** {style.get('keywords', '')}")
    if style.get('best_for'):
        lines.append(f"- **Best For:** {style.get('best_for', '')}")
    lines.append("")
    lines.append("### Colors")
    lines.append("| Role | Hex |")
    lines.append("|------|-----|")
    lines.append(f"| Primary | {colors.get('primary', '')} |")
    lines.append(f"| Secondary | {colors.get('secondary', '')} |")
    lines.append(f"| CTA | {colors.get('cta', '')} |")
    lines.append(f"| Background | {colors.get('background', '')} |")
    lines.append(f"| Text | {colors.get('text', '')} |")
    lines.append("")
    lines.append("### Typography")
    lines.append(f"- **Heading:** {typography.get('heading', '')}")
    lines.append(f"- **Body:** {typography.get('body', '')}")
    if typography.get("mood"):
        lines.append(f"- **Mood:** {typography.get('mood', '')}")
    if typography.get("google_fonts_url"):
        lines.append(f"- **Google Fonts:** {typography.get('google_fonts_url', '')}")
    lines.append("")
    if effects:
        lines.append("### Key Effects")
        lines.append(f"{effects}")
        lines.append("")
    if anti_patterns:
        lines.append("### Avoid (Anti-patterns)")
        lines.append(f"- {anti_patterns.replace(' + ', chr(10) + '- ')}")
        lines.append("")
    lines.append("### Pre-Delivery Checklist")
    for item in ["No emojis as icons (use SVG: Heroicons/Lucide)",
                 "cursor-pointer on all clickable elements",
                 "Hover states with smooth transitions (150-300ms)",
                 "Light mode: text contrast 4.5:1 minimum",
                 "Focus states visible for keyboard nav",
                 "prefers-reduced-motion respected",
                 "Responsive: 375px, 768px, 1024px, 1440px"]:
        lines.append(f"- [ ] {item}")
    lines.append("")
    return "\n".join(lines)


def generate_design_system(query, project_name=None, output_format="ascii",
                           persist=False, page=None, output_dir=None):
    generator = DesignSystemGenerator()
    design_system = generator.generate(query, project_name)
    if persist:
        persist_design_system(design_system, page, output_dir, query)
    if output_format == "markdown":
        return format_markdown(design_system)
    return format_ascii_box(design_system)


def persist_design_system(design_system, page=None, output_dir=None, page_query=None):
    base_dir = Path(output_dir) if output_dir else Path.cwd()
    project_name = design_system.get("project_name", "default")
    project_slug = project_name.lower().replace(' ', '-')
    design_system_dir = base_dir / "design-system" / project_slug
    pages_dir = design_system_dir / "pages"
    created_files = []
    design_system_dir.mkdir(parents=True, exist_ok=True)
    pages_dir.mkdir(parents=True, exist_ok=True)
    master_file = design_system_dir / "MASTER.md"
    master_content = format_master_md(design_system)
    with open(master_file, 'w', encoding='utf-8') as f:
        f.write(master_content)
    created_files.append(str(master_file))
    if page:
        page_file = pages_dir / f"{page.lower().replace(' ', '-')}.md"
        page_content = format_page_override_md(design_system, page, page_query)
        with open(page_file, 'w', encoding='utf-8') as f:
            f.write(page_content)
        created_files.append(str(page_file))
    return {"status": "success", "design_system_dir": str(design_system_dir), "created_files": created_files}


def format_master_md(design_system):
    project = design_system.get("project_name", "PROJECT")
    pattern = design_system.get("pattern", {})
    style = design_system.get("style", {})
    colors = design_system.get("colors", {})
    typography = design_system.get("typography", {})
    effects = design_system.get("key_effects", "")
    anti_patterns = design_system.get("anti_patterns", "")
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    lines = []
    lines.append("# Design System Master File")
    lines.append("")
    lines.append("> **LOGIC:** When building a specific page, first check `design-system/pages/[page-name].md`.")
    lines.append("> If that file exists, its rules **override** this Master file.")
    lines.append("> If not, strictly follow the rules below.")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append(f"**Project:** {project}")
    lines.append(f"**Generated:** {timestamp}")
    lines.append(f"**Category:** {design_system.get('category', 'General')}")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## Global Rules")
    lines.append("")
    lines.append("### Color Palette")
    lines.append("")
    lines.append("| Role | Hex | CSS Variable |")
    lines.append("|------|-----|--------------|")
    lines.append(f"| Primary | `{colors.get('primary', '#2563EB')}` | `--color-primary` |")
    lines.append(f"| Secondary | `{colors.get('secondary', '#3B82F6')}` | `--color-secondary` |")
    lines.append(f"| CTA/Accent | `{colors.get('cta', '#F97316')}` | `--color-cta` |")
    lines.append(f"| Background | `{colors.get('background', '#F8FAFC')}` | `--color-background` |")
    lines.append(f"| Text | `{colors.get('text', '#1E293B')}` | `--color-text` |")
    lines.append("")
    lines.append("### Typography")
    lines.append("")
    lines.append(f"- **Heading Font:** {typography.get('heading', 'Inter')}")
    lines.append(f"- **Body Font:** {typography.get('body', 'Inter')}")
    if typography.get("mood"):
        lines.append(f"- **Mood:** {typography.get('mood', '')}")
    lines.append("")
    lines.append("### Spacing Variables")
    lines.append("")
    lines.append("| Token | Value | Usage |")
    lines.append("|-------|-------|-------|")
    for token, val, usage in [
        ("--space-xs", "4px", "Tight gaps"),
        ("--space-sm", "8px", "Icon gaps"),
        ("--space-md", "16px", "Standard padding"),
        ("--space-lg", "24px", "Section padding"),
        ("--space-xl", "32px", "Large gaps"),
        ("--space-2xl", "48px", "Section margins"),
        ("--space-3xl", "64px", "Hero padding"),
    ]:
        lines.append(f"| `{token}` | `{val}` | {usage} |")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## Anti-Patterns (Do NOT Use)")
    lines.append("")
    if anti_patterns:
        for anti in [a.strip() for a in anti_patterns.split("+") if a.strip()]:
            lines.append(f"- {anti}")
    lines.append("")
    lines.append("## Pre-Delivery Checklist")
    lines.append("")
    for item in ["No emojis used as icons", "cursor-pointer on all clickable elements",
                 "Hover states with smooth transitions (150-300ms)",
                 "Light mode: text contrast 4.5:1 minimum",
                 "Focus states visible for keyboard navigation",
                 "prefers-reduced-motion respected",
                 "Responsive: 375px, 768px, 1024px, 1440px"]:
        lines.append(f"- [ ] {item}")
    lines.append("")
    return "\n".join(lines)


def format_page_override_md(design_system, page_name, page_query=None):
    project = design_system.get("project_name", "PROJECT")
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    page_title = page_name.replace("-", " ").replace("_", " ").title()
    page_overrides = _generate_intelligent_overrides(page_name, page_query, design_system)
    lines = []
    lines.append(f"# {page_title} Page Overrides")
    lines.append("")
    lines.append(f"> **PROJECT:** {project}")
    lines.append(f"> **Generated:** {timestamp}")
    lines.append("")
    lines.append("> Rules in this file **override** the Master file (`design-system/MASTER.md`).")
    lines.append("> Only deviations are documented here. For all other rules, refer to the Master.")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## Page-Specific Rules")
    lines.append("")
    for section, key in [("Layout Overrides", "layout"), ("Spacing Overrides", "spacing"),
                         ("Typography Overrides", "typography"), ("Color Overrides", "colors"),
                         ("Component Overrides", "components")]:
        lines.append(f"### {section}")
        lines.append("")
        data = page_overrides.get(key, {})
        if isinstance(data, dict) and data:
            for k, v in data.items():
                lines.append(f"- **{k}:** {v}")
        elif isinstance(data, list) and data:
            for item in data:
                lines.append(f"- {item}")
        else:
            lines.append(f"- No overrides — use Master")
        lines.append("")
    lines.append("## Recommendations")
    lines.append("")
    for rec in page_overrides.get("recommendations", ["Refer to MASTER.md"]):
        lines.append(f"- {rec}")
    lines.append("")
    return "\n".join(lines)


def _generate_intelligent_overrides(page_name, page_query, design_system):
    from core import search
    combined_context = f"{page_name.lower()} {(page_query or '').lower()}"
    style_search = search(combined_context, "style", max_results=1)
    ux_search = search(combined_context, "ux", max_results=3)
    landing_search = search(combined_context, "landing", max_results=1)
    style_results = style_search.get("results", [])
    ux_results = ux_search.get("results", [])
    landing_results = landing_search.get("results", [])
    page_type = _detect_page_type(combined_context, style_results)
    layout = {}
    spacing = {}
    components = []
    recommendations = []
    colors = {}
    if style_results:
        keywords = style_results[0].get("Keywords", "")
        effects = style_results[0].get("Effects & Animation", "")
        if any(kw in keywords.lower() for kw in ["data", "dense", "dashboard", "grid"]):
            layout["Max Width"] = "1400px or full-width"
            layout["Grid"] = "12-column grid for data flexibility"
        elif any(kw in keywords.lower() for kw in ["minimal", "simple", "clean"]):
            layout["Max Width"] = "800px (narrow, focused)"
            layout["Layout"] = "Single column, centered"
        else:
            layout["Max Width"] = "1200px"
        if effects:
            recommendations.append(f"Effects: {effects}")
    for ux in ux_results:
        do_text = ux.get("Do", "")
        dont_text = ux.get("Don't", "")
        if do_text:
            recommendations.append(f"{ux.get('Category', '')}: {do_text}")
        if dont_text:
            components.append(f"Avoid: {dont_text}")
    if landing_results:
        sections = landing_results[0].get("Section Order", "")
        cta_placement = landing_results[0].get("Primary CTA Placement", "")
        color_strategy = landing_results[0].get("Color Strategy", "")
        if sections:
            layout["Sections"] = sections
        if cta_placement:
            recommendations.append(f"CTA Placement: {cta_placement}")
        if color_strategy:
            colors["Strategy"] = color_strategy
    if not layout:
        layout["Max Width"] = "1200px"
        layout["Layout"] = "Responsive grid"
    if not recommendations:
        recommendations = ["Refer to MASTER.md for all design rules"]
    return {"page_type": page_type, "layout": layout, "spacing": spacing,
            "typography": {}, "colors": colors, "components": components,
            "unique_components": [], "recommendations": recommendations}


def _detect_page_type(context, style_results):
    context_lower = context.lower()
    page_patterns = [
        (["dashboard", "admin", "analytics", "data", "metrics", "stats"], "Dashboard / Data View"),
        (["checkout", "payment", "cart", "purchase", "billing"], "Checkout / Payment"),
        (["settings", "profile", "account", "preferences", "config"], "Settings / Profile"),
        (["landing", "marketing", "homepage", "hero", "home"], "Landing / Marketing"),
        (["login", "signin", "signup", "register", "auth"], "Authentication"),
        (["pricing", "plans", "subscription", "tiers"], "Pricing / Plans"),
        (["blog", "article", "post", "news", "content"], "Blog / Article"),
        (["search", "results", "browse", "filter", "catalog"], "Search Results"),
    ]
    for keywords, page_type in page_patterns:
        if any(kw in context_lower for kw in keywords):
            return page_type
    if style_results:
        best_for = style_results[0].get("Best For", "").lower()
        if "dashboard" in best_for:
            return "Dashboard / Data View"
        elif "landing" in best_for:
            return "Landing / Marketing"
    return "General"


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Generate Design System")
    parser.add_argument("query", help="Search query")
    parser.add_argument("--project-name", "-p", type=str, default=None)
    parser.add_argument("--format", "-f", choices=["ascii", "markdown"], default="ascii")
    args = parser.parse_args()
    print(generate_design_system(args.query, args.project_name, args.format))
