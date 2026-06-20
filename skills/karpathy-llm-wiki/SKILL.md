---
name: karpathy-llm-wiki
description: "Use when building or maintaining a personal LLM-powered knowledge base. Triggers: ingesting sources into a wiki, querying wiki knowledge, linting wiki quality, 'add to wiki', 'what do I know about', or any mention of 'LLM wiki' or 'Karpathy wiki'."
---

# Karpathy LLM Wiki

Build and maintain a personal knowledge base using LLMs. Two directories: `raw/` (immutable source material) and `wiki/` (compiled knowledge articles).

Core ideas from Karpathy:
- "The LLM writes and maintains the wiki; the human reads and asks questions."
- "The wiki is a persistent, compounding artifact."

## Architecture

**raw/** — Immutable source material. Never modify. Organized by topic subdirectories.

**wiki/** — Compiled knowledge articles. One level only: `wiki/<topic>/<article>.md`.
- `wiki/index.md` — Global index (link + summary + Updated date per article)
- `wiki/log.md` — Append-only operation log

Templates in `references/` relative to this file.

### Initialization (first Ingest only)

Create if missing: `raw/`, `wiki/`, `wiki/index.md`, `wiki/log.md`. Never overwrite existing.

---

## Ingest

Fetch into raw/, compile into wiki/. Both steps always.

### Fetch (raw/)
1. Get source content (WebFetch or user paste)
2. Pick topic directory (reuse existing if close enough)
3. Save as `raw/<topic>/YYYY-MM-DD-descriptive-slug.md` with metadata header
4. See `references/raw-template.md` for format

### Compile (wiki/)
- Same thesis as existing article → Merge
- New concept → New article (named after concept, not raw file)
- Spans multiple topics → Most relevant + See Also cross-references

Check factual conflicts: if new source contradicts existing, annotate with source attribution.
See `references/article-template.md` for format.

### Cascade Updates
After primary article: scan same-topic articles and index entries in other topics. Update every materially affected article. Archive pages are never cascade-updated.

### Post-Ingest
Update `wiki/index.md`. Append to `wiki/log.md`:
```
## [YYYY-MM-DD] ingest | <primary article title>
- Updated: <cascade-updated title>
```

---

## Query

1. Read `wiki/index.md` to locate relevant articles
2. Read articles and synthesize answer
3. Prefer wiki content over training knowledge. Cite with markdown links.
4. Output in conversation. Don't write files unless asked.

### Archiving
When user asks to archive: write answer as new wiki page (archive-template.md), update index, append to log.

---

## Lint

### Deterministic Checks (auto-fix)
- Index consistency: missing entries → add; missing files → mark `[MISSING]`
- Internal links: broken → search wiki/, fix if one match
- Raw references: broken → search raw/, fix if one match
- See Also: add missing cross-references, remove deleted links

### Heuristic Checks (report only)
- Factual contradictions, outdated claims, orphan pages, missing cross-topic references

### Post-Lint
```
## [YYYY-MM-DD] lint | <N> issues found, <M> auto-fixed
```
