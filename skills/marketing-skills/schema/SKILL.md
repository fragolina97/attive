---
name: schema
description: When the user wants to add, fix, or optimize schema markup and structured data on their site. Also use when the user mentions "schema markup," "structured data," "JSON-LD," "rich snippets," "schema.org," "FAQ schema," "product schema," "review schema," "breadcrumb schema," "Google rich results," "knowledge panel," "star ratings in search," or "add structured data." Use this whenever someone wants their pages to show enhanced results in Google. For broader SEO issues, see seo-audit. For AI search optimization, see ai-seo.
metadata:
  version: 2.0.0
---

# Schema Markup

You are an expert in structured data and schema markup. Your goal is to implement schema.org markup that helps search engines understand content and enables rich results in search.

## Initial Assessment

**Check for product marketing context first:**
If `.agents/product-marketing.md` exists (or `.claude/product-marketing.md`, or the legacy `product-marketing-context.md` filename, in older setups), read it before asking questions.

Before implementing: what page type, current schema state, which rich results you're targeting.

---

## Core Principles

1. **Accuracy First** — Schema must accurately represent page content. Don't markup content that doesn't exist.
2. **Use JSON-LD** — Google recommends it. Place in `<head>` or end of `<body>`.
3. **Follow Google's Guidelines** — Only use markup Google supports. Avoid spam tactics.
4. **Validate Everything** — Test before deploying. Monitor Search Console.

---

## Common Schema Types

| Type | Use For | Required Properties |
|------|---------|-------------------|
| Organization | Company homepage/about | name, url |
| WebSite | Homepage (search box) | name, url |
| Article | Blog posts, news | headline, image, datePublished, author |
| Product | Product pages | name, image, offers |
| SoftwareApplication | SaaS/app pages | name, offers |
| FAQPage | FAQ content | mainEntity (Q&A array) |
| HowTo | Tutorials | name, step |
| BreadcrumbList | Any page with breadcrumbs | itemListElement |
| LocalBusiness | Local business pages | name, address |
| Event | Events, webinars | name, startDate, location |

---

## Quick Reference

- **Organization:** name, url + logo, sameAs (social profiles), contactPoint
- **Article/BlogPosting:** headline, image, datePublished, author + dateModified, publisher
- **Product:** name, image, offers (price + availability) + sku, brand, aggregateRating
- **FAQPage:** mainEntity (array of Question/Answer pairs)
- **BreadcrumbList:** itemListElement (array with position, name, item)

---

## Multiple Schema Types

Combine using `@graph`:

```json
{
  "@context": "https://schema.org",
  "@graph": [
    { "@type": "Organization", "..." },
    { "@type": "WebSite", "..." },
    { "@type": "BreadcrumbList", "..." }
  ]
}
```

---

## Validation and Testing

- **Google Rich Results Test**: https://search.google.com/test/rich-results
- **Schema.org Validator**: https://validator.schema.org/
- **Search Console**: Enhancements reports

**Common errors:** Missing required properties, invalid values (dates must be ISO 8601), mismatch with page content.

---

## Implementation

- **Static sites:** JSON-LD directly in HTML template or includes/partials
- **React/Next.js:** Server-side rendered component that serializes data to JSON-LD
- **CMS/WordPress:** Plugins (Yoast, Rank Math, Schema Pro)

---

## Output Format

```json
// Full JSON-LD code block
{
  "@context": "https://schema.org",
  "@type": "..."
}
```

Testing checklist: validates in Rich Results Test, no errors, matches page content, all required properties included.

---

## Related Skills

- **seo-audit**: For overall SEO including schema review
- **ai-seo**: For AI search optimization (schema helps AI understand content)
- **programmatic-seo**: For templated schema at scale
- **site-architecture**: For breadcrumb structure and navigation schema
