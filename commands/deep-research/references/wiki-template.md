# Wiki Page Template — Completo

Template completo per la creazione di pagine nel vault 2Brain.
Usato da AG-04 (Wiki Builder) per la modalità CREATE e REBUILD.

---

## Template Completo

```markdown
---
type: [concetto|entità|progetto|fonte|output]
title: "[Titolo Pagina]"
area: "[concepts|entities|projects|sources|outputs]"
sub_area: "[eventuale sotto-area]"
tags: [#tag1 #tag2 #tag3]
source:
  - url: "[url originale]"
    title: "[titolo della fonte]"
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
[Riassunto denso in 3-5 frasi. Ogni affermazione deve essere verificabile nel raw content. Zero linguaggio vago.]

## Descrizione Approfondita
[Espansione dettagliata. Struttura in sottosezioni se necessario. Mantieni alta densità informativa.]

## Concetti Chiave
- **[[Entità 1]]** (tipo): definizione breve e contestuale
- **[[Entità 2]]** (tipo): definizione breve e contestuale

## Relazioni
- [[Soggetto]] → è_tipo_di → [[Oggetto]]
- [[Soggetto]] → causa → [[Effetto]]
- [[Soggetto]] → è_correlato_a → [[Correlato]]

## Dati e Metriche
| Metrica | Valore | Unità | Fonte |
|---|---|---|---|
| [nome] | [valore] | [unità] | [fonte] |

## Citazioni
> "[Testo della citazione diretta]"
> — [Autore], [Anno]

## Applicazioni / Esempi
1. [Esempio concreto e specifico]
2. [Altro esempio]

## Cronologia
- [YYYY]: [evento o sviluppo rilevante]
- [YYYY]: [altro evento]

## Fonti
- [[titolo fonte]](url) — [[raw/path-file-raw]]

---
*Generato da /deep-research il YYYY-MM-DD*
```

---

## Sezioni Obbligatorie

Tutte le 9 sezioni sono obbligatorie. Se i dati non sono disponibili nella fonte:

```markdown
## [Nome Sezione]
*Dato non presente nella fonte originale.*
```

Non lasciare sezioni vuote senza questa indicazione esplicita.

---

## Gestione Conflitti (modalità UPDATE/MERGE)

Quando esiste già una pagina con dati diversi:

```markdown
## ⚠️ Dati Contrastanti

### Versione A — [fonte A, data]
[Contenuto versione A]

### Versione B — [fonte B, data]
[Contenuto versione B]

> Richiede risoluzione manuale. Nessuna delle due versioni è stata rimossa.
```
