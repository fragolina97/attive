---
name: inkos-multi-agent-novel-writing
description: Multi-agent CLI system for autonomous novel writing, auditing, and revision with human review gates
triggers:
  - write novel with AI agents
  - autonomous novel production
  - inkos novel writing
  - multi-agent creative writing
  - AI novel audit and revision
  - automated chapter writing TypeScript
  - inkos CLI novel agent
  - novel writing pipeline with review gates
---

# InkOS Multi-Agent Novel Writing

> Skill by [ara.so](https://ara.so) — Daily 2026 Skills collection

InkOS is a multi-agent CLI system that autonomously writes, audits, and revises novels. Agents handle the full pipeline: Writer → Validator → Auditor → Reviser, with human review gates at configurable checkpoints.

## Installation

```bash
npm install -g @actalk/inkos
# or run directly
npx @actalk/inkos --version
```

**Requirements:** Node.js ≥ 20.0.0

## Quick Start

```bash
# Create a new novel project
inkos book create --title "吞天魔帝" --genre xuanhuan

# Write the next chapter
inkos write next 吞天魔帝

# Audit a specific chapter
inkos audit 吞天魔帝 --chapter 3

# Run the full daemon (continuous production)
inkos daemon start
```

## Project Structure

After `inkos book create`, the project directory contains:

```
story/
  outline.md              # Story outline (architect agent input)
  book_rules.md           # Per-book custom rules and audit dimensions
  chapter_summaries.md    # Auto-generated per-chapter summaries
  subplot_board.md        # Subplot progress tracking (A/B/C lines)
  emotional_arcs.md       # Per-character emotional arc tracking
  character_matrix.md     # Character interaction matrix + info boundaries
  parent_canon.md         # Spinoff only: imported canon constraints
  style_profile.json      # Style fingerprint (if style import used)
  style_guide.md          # LLM-generated qualitative style guide
  chapters/
    ch001.md
    ch002.md
    ...
```

## Core Commands

### Book Management

```bash
inkos book create --title "Title" --genre xuanhuan  # genres: xuanhuan | xianxia | dushi | horror | general
inkos book list
inkos book status 吞天魔帝
```

### Writing Pipeline

```bash
inkos write next 吞天魔帝           # Write next chapter (auto-loads all context)
inkos write chapter 吞天魔帝 5      # Write specific chapter
inkos audit 吞天魔帝 --chapter 3    # Audit chapter (33 dimensions)
inkos revise 吞天魔帝 --chapter 3   # Revise based on audit results
inkos revise 吞天魔帝 --chapter 3 --mode spot-fix   # Point fix only (default)
inkos revise 吞天魔帝 --chapter 3 --mode rewrite    # Full rewrite (use cautiously)
inkos revise 吞天魔帝 --chapter 3 --mode polish     # Polish (no structural changes)
```

### Genre System

```bash
inkos genre list                        # List all built-in genres
inkos genre show xuanhuan               # View full rules for a genre
inkos genre copy xuanhuan               # Copy genre rules to project for customization
inkos genre create wuxia --name 武侠     # Create new genre from scratch
```

### Style Matching

```bash
inkos style analyze reference.txt               # Analyze style fingerprint
inkos style import reference.txt 吞天魔帝        # Import style into book
inkos style import reference.txt 吞天魔帝 --name "某作者"
```

### Spinoff (Prequel/Sequel/IF-branch)

```bash
inkos book create --title "烈焰前传" --genre xuanhuan
inkos import canon 烈焰前传 --from 吞天魔帝       # Import parent canon constraints
inkos write next 烈焰前传                         # Writer auto-reads canon constraints
```

### AIGC Detection

```bash
inkos detect 吞天魔帝 --chapter 3     # Detect AIGC markers in chapter
inkos detect 吞天魔帝 --all           # Detect all chapters
inkos detect --stats                  # View detection history statistics
```

### Daemon (Continuous Production)

```bash
inkos daemon start                    # Start scheduler (default: 15 min/cycle)
inkos daemon stop
inkos daemon status
```

## Configuration

### Global Config (`~/.inkos/config.json`)

```json
{
  "llm": {
    "provider": "openai",
    "model": "gpt-4o",
    "apiKey": "sk-...",
    "temperature": 0.8
  },
  "daemon": {
    "intervalMinutes": 15,
    "dailyChapterLimit": 10,
    "parallelBooks": 2
  },
  "webhook": {
    "url": "https://your-server.com/hooks/inkos",
    "secret": "your-hmac-secret",
    "events": ["chapter-complete", "audit-failed", "pipeline-error"]
  },
  "aigcDetection": {
    "provider": "gptzero",
    "apiKey": "...",
    "endpoint": "https://api.gptzero.me/v2/predict/text"
  }
}
```

### Per-Book Rules (`story/book_rules.md`)

````markdown
# Book Rules: 吞天魔帝

## 禁忌 (Forbidden)
- 主角不得主动求饶
- 不得出现「命运」「天意」等宿命论表述

## 高疲劳词
- 震撼, 惊骇, 恐惧, 颤抖

## additionalAuditDimensions
- 数值系统一致性: 战力数值不得前后矛盾
- 角色成长节奏: 主角突破间隔不少于3章

## 写手特别指令
- 战斗场面优先感官描写，禁止数值报告
````

## Agent Architecture

InkOS runs five specialized agents in sequence:

```
ArchitectAgent  →  outline.md, book_rules.md
     ↓
WriterAgent     →  ch00N.md (reads: outline, summaries, arcs, matrix, style_guide, canon)
     ↓
ValidatorAgent  →  11 deterministic rules, zero LLM cost
     ↓  (error found → trigger spot-fix immediately)
AuditorAgent    →  33 LLM dimensions, temperature=0 for consistency
     ↓
ReviserAgent    →  spot-fix | rewrite | polish | anti-detect
```

### Post-Write Validator Rules (Deterministic, No LLM)

| Rule | Condition |
|------|----------|
| Forbidden patterns | `不是……而是……` constructs |
| Em-dash ban | `——` character |
| Transition word density | 仿佛/忽然/竟然≤1 per 3000 chars |
| High-fatigue words | Per-book list, ≤1 per chapter |
| Meta-narrative | Screenwriter-style narration |
| Report terminology | Analytical framework terms in prose |
| Author moralizing | 显然/不言而喻 etc. |
| Collective reaction | 「全场震惊」clichés |
| Consecutive 了 | ≥4 consecutive sentences with 了 |
| Paragraph length | ≥2 paragraphs over 300 chars |
| Book-specific bans | `book_rules.md` forbidden list |

### Audit Dimensions (33 total, LLM-evaluated)

Key dimensions include:
- Dims 1–23: Core narrative quality (plot, character, pacing, foreshadowing)
- Dim 24–26: Subplot stagnation, arc flatness, rhythm monotony (all 5 genres)
- Dim 27: Sensitive content
- Dim 28–31: Spinoff-specific (canon conflicts, future info leakage, world rule consistency, foreshadowing isolation)
- Dim 32: Reader expectation management
- Dim 33: Outline deviation detection

## Code Integration Examples

### Programmatic Usage (TypeScript)

```typescript
import { BookManager } from '@actalk/inkos'
import { WriterAgent } from '@actalk/inkos/agents'
import { ValidatorAgent } from '@actalk/inkos/agents'

const manager = new BookManager()
const book = await manager.createBook({
  title: '吞天魔帝',
  genre: 'xuanhuan',
  outlinePath: './my-outline.md'
})

const writer = new WriterAgent({ temperature: 0.8 })
const chapter = await writer.writeNext(book)

const validator = new ValidatorAgent()
const validationResult = await validator.validate(chapter, book)

if (validationResult.hasErrors) {
  const reviser = new ReviserAgent({ mode: 'spot-fix' })
  const fixed = await reviser.revise(chapter, validationResult.errors, book)
}
```

## Audit Revision Loop

```
AuditorAgent (temp=0)
     ↓ critical issues found
ReviserAgent spot-fix
     ↓
AI marker count comparison
     ↓ markers increased?
  YES → discard revision, keep original
  NO  → accept revision
     ↓
Re-audit (temp=0)
```

## Spinoff Canon Constraints

When `parent_canon.md` is detected, 4 additional audit dimensions activate automatically.

## Troubleshooting

**Validator fires on every chapter** — Check `book_rules.md` fatigue word list.

**Audit results wildly inconsistent** — Confirm auditor temperature is locked to 0.

**Revision introduces more AI markers** — InkOS v0.4 auto-detects and discards. Switch to `spot-fix` mode.

**Daemon stops after repeated failures** — Run `inkos daemon resume 书名` after fixing outline/rules issues.

**Style guide not applied** — Run `inkos style import` again. Reference text must be ≥5000 chars.
