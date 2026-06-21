# AG-02 WebFetch + AG-03 Parser Semantico

---

## AG-02 — WebFetch (solo PIPELINE FULL)

**Input**: URL dall'utente
**Output**: file raw salvato in `2Brain/raw/YYYY-MM-DD_slug.md`

### Step di Esecuzione

1. Usa il tool `WebFetch` per scaricare il contenuto dalla URL
2. Sanitizza il contenuto: rimuovi navigazione, footer, sidebar, script, stili, ads, iframe
3. Preserva la struttura semantica: titoli (h1-h6), paragrafi, liste, tabelle, codice, citazioni
4. Estrai metadati: title, author, date_published, canonical_url
5. Calcola: word_count, content_hash (sha256, primi 16 chars)
6. Salva il file raw **immutabile** con questo frontmatter:

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

# [title]

[contenuto sanitizzato]
```

**Path file**: `2Brain/raw/YYYY-MM-DD_[slug].md`
**Regola critica**: il file raw NON viene mai modificato dopo la creazione.

### Gestione Errori WebFetch

| Errore | Azione |
|---|---|
| URL non raggiungibile | Retry 3 volte con backoff, poi escalate AG-06 |
| HTML non parseable | Prova estrazione testo puro, se fallisce → AG-06 |
| Contenuto troppo lungo | Tronca a 50.000 chars, logga l'omissione |
| Redirect loop | Segui max 5 redirect, poi fail |

---

## AG-03 — Parser Semantico (sempre attivo)

**Input**: raw_content (da AG-02) oppure testo diretto dell'utente (PARTIAL)
**Output**: ParsedData con entità, relazioni, fatti, classificazione vault

### Step di Esecuzione

1. **Se PARTIAL**: salva il testo grezzo come `2Brain/raw/YYYY-MM-DD_input-[hash].md`
2. **Estrai Entità**: persone, organizzazioni, concetti, luoghi, metriche, date — con definizione e contesto
3. **Estrai Relazioni** tra entità con predicati:
   - `è_tipo_di` — tassonomia
   - `è_componente_di` — composizione
   - `causa` — causalità
   - `è_correlato_a` — associazione
   - `contraddice` — conflitto
4. **Estrai Fatti Chiave**: lista di affermazioni fattuali verificabili — ogni fatto DEVE essere presente nel raw
5. **Estrai Citazioni**: testo diretto con autore e anno
6. **Estrai Dati Strutturati**: metriche, statistiche, tabelle con valori
7. **Costruisci Knowledge Graph**: nodi (entità) + archi (relazioni con peso 0.0–1.0)
8. **Scrivi Summary**: riassunto ad alta densità informativa — zero generalizzazioni vaghe, ogni affermazione verificabile nel raw
9. **Classifica per Vault**: determina area, sub_area e path → `2Brain/wiki/{area}/{sub_area}/{Titolo}.md`

### Regola Fondamentale
Ogni fatto nel summary deve essere tracciabile verbatim o per parafrasi fedele al raw content.
Se un'informazione non è nel raw → non includerla, o marcala esplicitamente come `[inferito]`.

### Classificazione Vault

Determina il path nel vault seguendo questa logica:
- **concepts/**: idee, teorie, framework, metodologie
- **entities/**: persone, organizzazioni, prodotti, luoghi
- **projects/**: progetti, iniziative, piani
- **sources/**: articoli, libri, paper, video
- **outputs/**: analisi generate, confronti, report
