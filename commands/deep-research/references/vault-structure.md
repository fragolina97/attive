# Vault Structure — 2Brain

Struttura del vault e percorsi canonici per ogni tipo di contenuto.

---

## Struttura Cartelle

```
2Brain/
├── index.md                    ← indice master di tutte le pagine
├── log.md                      ← log append-only di ogni operazione
├── raw/                        ← fonti immutabili (MAI modificare)
│   └── YYYY-MM-DD_slug.md
├── wiki/
│   ├── concepts/               ← idee, teorie, framework, metodologie
│   ├── entities/               ← persone, organizzazioni, prodotti, luoghi
│   ├── projects/               ← progetti, iniziative, piani
│   ├── sources/                ← articoli, paper, libri, video
│   └── outputs/                ← analisi generate, confronti, report
└── meta/
    └── changelog.md            ← changelog breve per --status
```

---

## Naming Convention

| Tipo | Path | Naming |
|---|---|---|
| Raw da URL | `raw/YYYY-MM-DD_[slug].md` | slug = titolo in kebab-case max 60 chars |
| Raw da testo | `raw/YYYY-MM-DD_input-[hash8].md` | hash MD5 dei primi 8 chars |
| Concetti | `wiki/concepts/[Titolo].md` | Title case |
| Entità | `wiki/entities/[Nome].md` | Nome proprio |
| Progetti | `wiki/projects/[Nome].md` | Nome progetto |
| Fonti | `wiki/sources/YYYY-MM-DD-[slug].md` | Data + slug |
| Output | `wiki/outputs/YYYY-MM-DD-[slug].md` | Data + slug |

---

## Classificazione Automatica (AG-03)

Quando il Parser classifica il contenuto, usa queste regole:

| Contenuto | Area | Path |
|---|---|---|
| Articolo, paper, post blog | `sources` | `wiki/sources/` |
| Persona, organizzazione | `entities` | `wiki/entities/` |
| Concetto, teoria, framework | `concepts` | `wiki/concepts/` |
| Progetto, prodotto, tool | `projects` | `wiki/projects/` |
| Analisi generata da Claude | `outputs` | `wiki/outputs/` |

---

## Regole di Integrità

- `raw/` è immutabile — nessun file viene mai modificato o eliminato
- `index.md` e `log.md` sono gestiti solo da AG-07
- Cartelle vuote non vengono create — solo quando necessario
- Nomi file: no spazi (usa trattini), no caratteri speciali eccetto `-` e `_`
