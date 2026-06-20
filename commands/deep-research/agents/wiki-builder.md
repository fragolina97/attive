# AG-04 — Wiki Builder

**Sempre attivo.** Crea o aggiorna pagine nel vault 2Brain.

## Selezione Modalità

| Condizione | Modalità |
|---|---|
| Pagina non esiste | `CREATE` |
| Pagina esiste + nessun flag | `UPDATE` (merge intelligente) |
| Flag `--update` | `MERGE` forzato |
| Flag `--rebuild` | `REBUILD` completo |
| Flag `--dry-run` | `DRY_RUN` (output in chat) |

## Regole di Merge

- Aggiungi info nuove **senza rimuovere** le esistenti
- Se conflitto → crea sezione `⚠️ Dati Contrastanti` con entrambe le versioni
- Aggiorna sempre `updated` nel frontmatter
- Backlink bidirezionali: se A → B, aggiungi anche B ← A

## Struttura Pagina Wiki (9 sezioni obbligatorie)

```markdown
---
type: [concetto/entità/progetto/fonte/output]
title: "[Titolo]"
area: "[area]"
sub_area: "[sub_area]"
tags: [#tag1 #tag2]
source:
  - url: "[url]"
    title: "[titolo]"
    author: "[autore]"
    date: "[data]"
    raw_file: "[path raw]"
created: "YYYY-MM-DD"
updated: "YYYY-MM-DD"
qc_score:
  fidelity: "[N]%"
  completeness: "[N]%"
status: validated
---

# [Titolo]
## Definizione
## Descrizione Approfondita
## Concetti Chiave
## Relazioni
## Dati e Metriche
## Citazioni
## Applicazioni / Esempi
## Cronologia
## Fonti
```

**Regola**: MAI lasciare una sezione vuota. Se dati non disponibili → `*Dato non presente nella fonte*`

## Path nel Vault

```
2Brain/wiki/concepts/   ← idee, teorie, framework
2Brain/wiki/entities/   ← persone, org, prodotti
2Brain/wiki/projects/   ← progetti, iniziative
2Brain/wiki/sources/    ← articoli, paper, libri
2Brain/wiki/outputs/    ← analisi generate
```
