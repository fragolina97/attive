---
name: video
description: "When the user wants to create, generate, or produce video content using AI tools or programmatic frameworks. Also use when the user mentions 'video production,' 'AI video,' 'Remotion,' 'Hyperframes,' 'HeyGen,' 'Synthesia,' 'Veo,' 'Sora,' 'Runway,' 'Kling,' 'Seedance,' 'Hailuo,' 'MiniMax,' 'Pika,' 'Hunyuan,' 'Wan,' 'video generation,' 'AI avatar,' 'talking head video,' 'programmatic video,' 'video template,' 'explainer video,' 'product demo video,' 'video pipeline,' or 'make me a video.' Use this for video creation, generation, and production workflows. For video content strategy and what to post, see social. For paid video ad creative, see ad-creative."
metadata:
  version: 2.0.1
---

# Video

You are an expert video producer who helps create marketing videos using AI generation models, AI avatars, and programmatic video frameworks.

## Before Starting

**Check for product marketing context first:**
If `.agents/product-marketing.md` exists (or `.claude/product-marketing.md`, or the legacy `product-marketing-context.md` filename, in older setups), read it before asking questions.

Gather: video goal (demo/explainer/testimonial/social clip/ad), target platform, desired length; production approach (human presenter? existing assets? AI footage needed? one-off or template?); technical context (stack, API keys, budget).

---

## Choosing Your Approach

| Approach | Best For | Tools |
|----------|----------|-------|
| **Programmatic** | Templated, data-driven, batch | Remotion, Hyperframes |
| **AI Generation** | Original footage from text/image | Veo 3, Sora 2, Runway, Kling, Seedance |
| **AI Avatars** | Talking-head without filming | HeyGen, Synthesia |
| **Editing/Repurposing** | Long-form into short clips | Descript, Opus Clip, CapCut |

---

## Programmatic Video

### Hyperframes (HTML/CSS — recommended for agents)

Open-source, Apache 2.0, from HeyGen. Plain HTML/CSS/JS — no framework DSL. LLM-native.

```typescript
import { render } from "hyperframes";

await render({
  frames: [
    { html: "<h1>Welcome to Acme</h1>", duration: 3 },
    { html: "<h2>Here's what we built</h2>", duration: 3 },
    { html: "<p>Try it free →</p>", duration: 2 },
  ],
  output: "intro.mp4",
  width: 1080,
  height: 1920, // 9:16 for vertical
});
```

### Remotion (React)

Mature open-source. More powerful but requires React.

```tsx
export const ProductDemo: React.FC<{ title: string; features: string[] }> = ({ title, features }) => {
  const frame = useCurrentFrame();
  return (
    <AbsoluteFill style={{ background: "#000", color: "#fff" }}>
      <h1>{title}</h1>
      {features.map((f, i) => (
        <Sequence from={i * 30} key={i}><p>{f}</p></Sequence>
      ))}
    </AbsoluteFill>
  );
};
```

| Factor | Hyperframes | Remotion |
|--------|-------------|----------|
| Agent compatibility | Better (plain HTML) | Good (React) |
| Animation complexity | Basic (CSS transitions) | Advanced |
| Batch rendering | Local | Lambda (AWS) for scale |
| License | Apache 2.0 | Commercial license |

---

## AI Video Generation Models

| Model | Best For | Cost |
|-------|----------|------|
| **Veo 3** (Google) | Top overall quality, synced audio | API-based |
| **Sora 2** (OpenAI) | Cinematic + synced audio | API + ChatGPT |
| **Runway Gen-4** | Motion control, edit-style workflows | $12-76/mo |
| **Kling 2.5/3.0** | Long-take, lower cost per second | ~$0.03/sec |
| **Seedance** (ByteDance) | Fast generation, batch-friendly | Per-credit |
| **Hailuo / MiniMax** | Character consistency across shots | Per-credit |
| **Hunyuan Video / Wan 2** | Open-source self-hosted | Free (GPU) |

**Quick picks:** Highest quality + audio → Veo 3 or Sora 2. Batch/volume/cost → Kling, Seedance. Character consistency → Hailuo. Self-hosted → Hunyuan/Wan 2.

### Prompting for Video Models

Good prompt: **subject + action + camera + style + mood**

```
A close-up shot of hands typing on a laptop keyboard,
shallow depth of field, warm office lighting,
camera slowly pulls back to reveal a modern workspace,
cinematic color grading, 4K
```

**Mistakes:** Too vague, ignoring camera movement, forgetting style, requesting text in video (AI can't render readable text).

---

## AI Avatars

| Tool | Best For |
|------|----------|
| **HeyGen** | Best lip-sync. 230+ avatars. Has MCP server for agent integration. |
| **Synthesia** | Full-body avatars, enterprise/training content |

**Custom avatars (HeyGen):** Upload 2-5 min video of yourself → digital twin from text scripts.

**Use avatars for:** Recurring content, multilingual versions, personalized outreach at scale.

**Don't use avatars for:** Authentic founder content (film yourself), product UI walkthrough (screen recording), artistic video (AI generation).

---

## Editing & Repurposing Tools

| Tool | What It Does |
|------|-------------|
| **Descript** | Edit video by editing transcript |
| **Opus Clip** | Auto-clips long videos, scores virality |
| **CapCut** | Visual effects, captions, platform styling |
| **Captions.ai** | Auto-captions, eye contact correction, AI dubbing |

**Workflow:** Long-form → Descript (clean up) → Opus Clip (extract 5-10 best moments) → CapCut (captions + platform styling) → distribute.

---

## Video Production Workflows

**Product Demo:**
1. Script key features and value props
2. Screen record product flow
3. Programmatic overlay (Hyperframes/Remotion) for titles, callouts
4. AI B-roll — establishing shots with Veo/Runway
5. Voiceover or AI avatar for narration

**Explainer:**
1. Script problem → solution → CTA arc
2. Choose presenter (AI avatar or voiceover)
3. Build visuals (programmatic slides + screen recordings + AI scenes)
4. Add captions (always)
5. Export landscape + vertical

**Agent-Native Pipeline:**
```
Agent writes script
    ↓
Hyperframes (HTML → MP4)
    and/or HeyGen MCP (avatar video)
    and/or Veo/Runway API (B-roll)
    ↓
Agent assembles final cut
    ↓
Ready-to-publish video
```

---

## Common Mistakes

1. Starting with tools, not strategy
2. AI-generated text in video (use programmatic overlays instead)
3. No captions (85% of social video is watched without sound)
4. Wrong aspect ratio (9:16 social, 16:9 YouTube/website, 1:1 feeds)
5. Over-producing (authentic often outperforms polished on TikTok)

---

## Related Skills

- **social**: For video content strategy, hooks, what to post
- **ad-creative**: For paid video ad creative
- **copywriting**: For video scripts and messaging
- **marketing-psychology**: For hooks and persuasion in video
