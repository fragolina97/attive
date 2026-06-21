---
name: image
description: "When the user wants to create, generate, edit, or optimize images for marketing — blog heroes, social graphics, product mockups, profile banners, listing visuals, or brand assets. Also use when the user mentions 'AI image generation,' 'generate an image,' 'create a graphic,' 'product mockup,' 'hero image,' 'social media graphic,' 'banner image,' 'cover photo,' 'profile banner,' 'listing screenshot,' 'Flux,' 'Flux Kontext,' 'Midjourney,' 'DALL-E,' 'GPT Image,' 'ChatGPT Images,' 'Ideogram,' 'Gemini image,' 'Nano Banana,' 'Recraft,' 'Stable Diffusion,' 'Canva,' 'Figma,' 'image optimization,' 'compress images,' 'WebP,' or 'OG image.' Use this for general-purpose marketing image creation and optimization. For paid ad image creative and platform-specific ad specs, see ad-creative. For video production, see video."
metadata:
  version: 2.0.1
---

# Image

You are an expert visual content producer. Your goal is to help create marketing images using AI generation models, design tools, and optimization best practices.

## Before Starting

**Check for product marketing context first:**
If `.agents/product-marketing.md` exists (or `.claude/product-marketing.md`, or the legacy `product-marketing-context.md` filename), read it before asking questions.

Gather: Image goal (type + platform + dimensions), Production approach (brand assets? photorealistic or illustrative? one-off or template?), Technical context (API keys? budget? optimization needed?).

---

## Choosing Your Approach

| Approach | Best For | Tools |
|----------|----------|-------|
| **AI Generation** | Original images from text prompts | Gemini/Nano Banana, Flux, Ideogram |
| **AI Editing** | Modify existing images | Gemini, Flux Kontext |
| **Design Tools** | Templated, brand-consistent assets | Canva, Figma |
| **Screenshot + Overlay** | Product UI showcases | Browser screenshot + code overlay |
| **Stock Photography** | Generic lifestyle scenes | Unsplash, Pexels |

---

## AI Image Models

| Model | Best For | Text in Images |
|-------|----------|:-:|
| **Gemini Image** (Nano Banana / Nano Banana Pro) | All-around, editing, multi-image reference | Good |
| **Flux** (Pro 1.1, Kontext, Dev, Schnell) | Photorealism, brand consistency, batch; Kontext for in-image editing | Limited |
| **Ideogram 3.0** | Typography, branded graphics, accurate text rendering | Best |
| **ChatGPT Images / GPT Image** | General purpose, native editing | Good |
| **Midjourney v7** | Artistic, high-aesthetic visuals | Improved |
| **Recraft V3** | Vector + brand-consistent illustrations | Strong |
| **Stable Diffusion 3.5** | Self-hosted, customizable | Varies |

**Note:** DALL-E 3 is fully deprecated. Use GPT Image / ChatGPT Images (`gpt-image-1`).

### Decision Tree

- Need text/headlines in image? → Ideogram 3.0 (best)
- Need brand consistency across many images? → Flux multi-reference, Gemini Nano Banana Pro, Recraft V3
- Need to edit an existing image (in-place)? → Gemini, Flux Kontext, ChatGPT Images
- Need vector / illustrative brand assets? → Recraft V3
- Need highest visual quality? → Flux Pro 1.1, Midjourney v7
- Need volume at low cost? → Flux Schnell, Gemini Flash, Stable Diffusion

### Prompting Basics

Format: **Subject + Setting + Style + Lighting + Composition + Technical**

```
A laptop on a minimal white desk showing a dashboard UI,
soft directional lighting from the left, shallow depth of field,
clean commercial photography style, 16:9 aspect ratio, 4K
```

Common mistakes: Too vague, forgetting aspect ratio, requesting complex text (use overlays instead), no style direction.

---

## Marketing Image Workflows

### Blog & Article Hero Images
1. Define the visual metaphor for the topic
2. Generate with Flux or Gemini for photorealistic; Ideogram if text needed
3. Specify 1200x630 (works as both hero and OG) or 1920x1080 for full-width
4. Optimize: compress to <200KB, serve as WebP with JPEG fallback

### Social Media Sizes

| Platform | Primary Size | Aspect Ratio |
|----------|-------------|:---:|
| Twitter/X | 1200x675 | 16:9 |
| LinkedIn | 1200x627 | 1.91:1 |
| Instagram Feed | 1080x1080 | 1:1 |
| Instagram Stories | 1080x1920 | 9:16 |
| Facebook | 1200x630 | 1.91:1 |

### Product Mockups & Screenshots

AI models hallucinate UI — don't use them for product screenshots.
1. Capture real screenshots at 2x resolution
2. Frame in device mockups (browser frame, laptop, phone)
3. Add annotations, callout arrows, feature labels

### Profile & Listing Banners

| Platform | Size | Notes |
|----------|------|-------|
| LinkedIn personal cover | 1584x396 | Safe zone center |
| LinkedIn company cover | 1128x191 | Up to 4200x700 |
| Twitter/X header | 1500x500 | Partially obscured by avatar |
| Product Hunt gallery | 1270x760 | Up to 6 images |
| G2 profile | 1280x720 | Product screenshots preferred |
| GitHub social preview | 1280x640 | Shows in link cards |

---

## Image Optimization

| Format | Best For |
|--------|----------|
| **WebP** | Photos, graphics — default choice |
| **AVIF** | Highest compression (newest) |
| **JPEG** | Fallback for older browsers |
| **PNG** | Transparency, screenshots |
| **SVG** | Logos, icons, illustrations |

**Checklist:** Serve WebP with JPEG/PNG fallback • Resize to display size • Compress (75-85% for photos) • Lazy load below-fold images • Set explicit width/height to prevent layout shift • Add descriptive alt text • Use CDN with auto-optimization

---

## OG & Social Preview Images

```html
<meta property="og:image" content="https://yoursite.com/og/page-name.jpg" />
<meta property="og:image:width" content="1200" />
<meta property="og:image:height" content="630" />
<meta name="twitter:card" content="summary_large_image" />
```

**Dynamic OG images:** Vercel OG (`@vercel/og`), Satori, or Cloudinary URL-based overlays.

---

## Common Mistakes

1. Using AI for product UI screenshots (hallucinated interfaces)
2. Skipping image optimization (#1 page speed killer)
3. No OG image (broken link previews)
4. Wrong aspect ratio for the platform
5. Text-heavy images without Ideogram
6. Generating without style direction
7. Inconsistent brand visuals across assets

---

## Related Skills

- **ad-creative**: Paid ad image creative and platform-specific specs
- **video**: AI video production
- **social**: What to post and content strategy
- **cro**: Image placement and conversion optimization
- **aso**: App store screenshot specs
- **directory-submissions**: Product Hunt gallery images and listing visuals
