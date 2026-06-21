# AG-04 — Wiki Builder

**Sempre attivo.** Crea o aggiorna pagine nel vault 2Brain usando il template standardizzato con backlink, tag e cross-reference.

---

## Selezione Modalità

| Condizione | Modalità | Comportamento |
|---|---|---|
| Pagina non esiste | `CREATE` | Nuova pagina da template completo |
| Pagina esiste + nessun flag | `UPDATE` | Merge intelligente — aggiunge senza rimuovere |
| Flag `--update` | `MERGE` | Merge forzato con segnalazione diff |
| Flag `--rebuild` | `REBUILD` | Sovrascrittura completa |
| Flag `--dry-run` | `DRY_RUN` | Output in chat, nessuna scrittura su file |

---

## Regole di Merge (modalità UPDATE/MERGE)

- Aggiungi informazioni nuove **senza rimuovere** le esistenti
- Se conflitto tra versione esistente e nuova → crea sezione `⚠️ Dati Contrastanti` con entrambe le versioni e le rispettive fonti
- Aggiorna sempre il campo `updated` nel frontmatter
- Backlink bidirezionali: se la pagina A punta a B, aggiungi anche il backlink B←A nella pagina B

---

## Struttura Pagina Wiki (Template Obbligatorio)

```markdown
---
type: [concetto/entità/progetto/fonte/output]
title: "[Titolo]"
area: "[area]"
sub_area: "[sub_area]"
tags: [#tag1 #tag2]
source:
  - url: "[url]"
    title: "[titolo fonte]"
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
[Riassunto denso — ogni affermazione verificabile nel raw]

## Descrizione Approfondita
[Espansione dettagliata dei concetti principali]

## Concetti Chiave
- **[Entità]** ([tipo]): [definizione breve]

## Relazioni
- [[Soggetto]] → [predicato] → [[Oggetto]]

## Dati e Metriche
| Metrica | Valore | Fonte |
|---|---|---|
| [nome] | [valore] | [fonte] |

## Citazioni
> "[testo citazione]"
> — [Autore], [Anno]

## Applicazioni / Esempi
1. [Esempio concreto]

## Cronologia
- [Data]: [evento]

## Fonti
- [[titolo fonte]](url) — [[path raw]]

---
*Generato da /deep-research il YYYY-MM-DD*
```

---

## Sezioni Obbligatorie (9/9)

`Definizione` · `Descrizione Approfondita` · `Concetti Chiave` · `Relazioni` · `Dati e Metriche` · `Citazioni` · `Applicazioni / Esempi` · `Cronologia` · `Fonti`

**Regola**: MAI lasciare una sezione vuota senza motivazione esplicita. Se i dati non sono disponibili → scrivi `*Dato non presente nella fonte*` nella sezione.

---

## Backlink

Per ogni entità estratta dal Parser:
1. Crea il link `[[Nome Entità]]` nella pagina corrente
2. Se la pagina dell'entità esiste nel vault → aggiungi riferimento inverso
3. Registra tutti i backlink creati per il report finale

---

## Path nel Vault

```
2Brain/wiki/concepts/[Titolo].md     ← idee, teorie, framework
2Brain/wiki/entities/[Nome].md       ← persone, org, prodotti
2Brain/wiki/projects/[Nome].md       ← progetti, iniziative
2Brain/wiki/sources/[Titolo].md      ← articoli, paper, libri
2Brain/wiki/outputs/[Titolo].md      ← analisi generate
```
