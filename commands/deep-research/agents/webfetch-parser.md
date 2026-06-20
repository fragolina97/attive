# AG-02 WebFetch + AG-03 Parser Semantico

## AG-02 — WebFetch (solo PIPELINE FULL)

**Input**: URL · **Output**: `2Brain/raw/YYYY-MM-DD_slug.md`

1. Usa `WebFetch` per scaricare il contenuto
2. Sanitizza: rimuovi nav, footer, script, stili, ads
3. Preserva: titoli h1-h6, paragrafi, liste, tabelle, codice, citazioni
4. Estrai metadati: title, author, date_published, canonical_url
5. Salva file raw **immutabile** con frontmatter:

```yaml
---
type: raw-source
url: "[url]"
title: "[title]"
author: "[author]"
date_published: "[data]"
date_fetched: "[ISO timestamp UTC]"
word_count: [N]
content_hash: "sha256:[hash]"
status: unprocessed
---
```

**Regola critica**: il file raw NON viene mai modificato dopo la creazione.

## AG-03 — Parser Semantico (sempre attivo)

**Input**: raw_content (da AG-02) o testo diretto (PARTIAL)

1. **Se PARTIAL**: salva testo grezzo in `2Brain/raw/YYYY-MM-DD_input-[hash].md`
2. **Estrai Entità**: persone, organizzazioni, concetti, luoghi, metriche, date
3. **Estrai Relazioni**: `è_tipo_di`, `è_componente_di`, `causa`, `è_correlato_a`, `contraddice`
4. **Estrai Fatti Chiave**: affermazioni fattuali verificabili — ogni fatto DEVE essere nel raw
5. **Estrai Citazioni**: testo diretto con autore e anno
6. **Costruisci Knowledge Graph**: nodi (entità) + archi (relazioni, peso 0.0–1.0)
7. **Scrivi Summary**: alta densità informativa, zero generalizzazioni vaghe
8. **Classifica per Vault**: area, sub_area, path → `2Brain/wiki/{area}/{sub_area}/{Titolo}.md`

**Regola**: ogni fatto deve essere tracciabile verbatim o per parafrasi fedele al raw. Se non è nel raw → non includerlo, o marcalo `[inferito]`.
