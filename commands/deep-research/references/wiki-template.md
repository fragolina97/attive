# Wiki Page Template — Completo

Usato da AG-04 per modalità CREATE e REBUILD.

```markdown
---
type: [concetto|entità|progetto|fonte|output]
title: "[Titolo Pagina]"
area: "[concepts|entities|projects|sources|outputs]"
sub_area: "[eventuale sotto-area]"
tags: [#tag1 #tag2 #tag3]
source:
  - url: "[url originale]"
    title: "[titolo fonte]"
    author: "[autore]"
    date: "[YYYY-MM-DD]"
    raw_file: "[[raw/YYYY-MM-DD_slug]]"
created: "YYYY-MM-DD"
updated: "YYYY-MM-DD"
qc_score:
  fidelity: "[N.N]%"
  completeness: "[N.N]%"
status: validated
---

# [Titolo Pagina]

## Definizione
[Riassunto denso in 3-5 frasi. Ogni affermazione verificabile nel raw. Zero linguaggio vago.]

## Descrizione Approfondita
[Espansione dettagliata con sottosezioni se necessario.]

## Concetti Chiave
- **[[Entità 1]]** (tipo): definizione breve

## Relazioni
- [[Soggetto]] → è_tipo_di → [[Oggetto]]

## Dati e Metriche
| Metrica | Valore | Unità | Fonte |
|---|---|---|---|

## Citazioni
> "[Testo citazione]"
> — [Autore], [Anno]

## Applicazioni / Esempi
1. [Esempio concreto]

## Cronologia
- [YYYY]: [evento]

## Fonti
- [[titolo fonte]](url) — [[raw/path-file-raw]]

---
*Generato da /deep-research il YYYY-MM-DD*
```

## Sezioni Obbligatorie

Tutte le 9 sezioni obbligatorie. Se dati non disponibili:
```markdown
## [Nome Sezione]
*Dato non presente nella fonte originale.*
```

## Gestione Conflitti (UPDATE/MERGE)

```markdown
## ⚠️ Dati Contrastanti
### Versione A — [fonte A, data]
[Contenuto A]
### Versione B — [fonte B, data]
[Contenuto B]
> Richiede risoluzione manuale.
```
