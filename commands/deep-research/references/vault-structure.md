# Vault Structure — 2Brain

## Struttura Cartelle

```
2Brain/
├── index.md                    ← indice master
├── log.md                      ← log append-only
├── raw/                        ← fonti immutabili
│   └── YYYY-MM-DD_slug.md
├── wiki/
│   ├── concepts/
│   ├── entities/
│   ├── projects/
│   ├── sources/
│   └── outputs/
└── meta/
    └── changelog.md
```

## Naming Convention

| Tipo | Path | Naming |
|---|---|---|
| Raw da URL | `raw/YYYY-MM-DD_[slug].md` | kebab-case max 60 chars |
| Raw da testo | `raw/YYYY-MM-DD_input-[hash8].md` | hash MD5 8 chars |
| Concetti | `wiki/concepts/[Titolo].md` | Title case |
| Entità | `wiki/entities/[Nome].md` | Nome proprio |
| Progetti | `wiki/projects/[Nome].md` | Nome progetto |
| Fonti | `wiki/sources/YYYY-MM-DD-[slug].md` | Data + slug |
| Output | `wiki/outputs/YYYY-MM-DD-[slug].md` | Data + slug |

## Regole di Integrità

- `raw/` è immutabile — nessun file modificato o eliminato
- `index.md` e `log.md` gestiti solo da AG-07
- Nomi file: no spazi, no caratteri speciali eccetto `-` e `_`
