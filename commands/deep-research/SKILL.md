---
name: deep-research
description: Attiva il sistema multi-agente DeepSearch per acquisire, analizzare e integrare conoscenza nel vault 2Brain. Questa skill deve essere usata ESCLUSIVAMENTE quando l'utente invoca esplicitamente il comando /deep-research. NON triggerare mai in risposta a URL, testo libero, parole chiave, contesto conversazionale o qualsiasi altro input che non sia il comando diretto /deep-research. Se l'utente non ha scritto esplicitamente /deep-research, NON usare questa skill.
---

# DEEP RESEARCH — DeepSearch v4.0

Sistema multi-agente per l'acquisizione e l'integrazione di conoscenza nel vault 2Brain.

---

## Attivazione e Classificazione Input

Appena invocata, classifica l'input dell'utente (`$ARGUMENTS`):

```
URL (inizia con http/https/www) → PIPELINE FULL
  AG-01 → AG-02 → AG-03 → AG-04 → AG-05 → [AG-06 se errore] → AG-07

TESTO (concetto, paragrafo, nota) → PIPELINE PARTIAL
  AG-01 → AG-03 → AG-04 → AG-05 → [AG-06 se errore] → AG-07

FLAG standalone:
  --status  → mostra ultimo changelog da 2Brain/meta/changelog.md
  --dry-run → esegui pipeline ma non scrivere nessun file (output in chat)
  --rebuild → rigenera pagina esistente da zero
  --update  → forza merge su pagina esistente
```

Mostra subito all'utente:
```
🔍 DeepSearch v4.0 attivato
Input: [URL/TESTO/FLAG]
Pipeline: [FULL/PARTIAL]
Modalità: [CREATE/UPDATE/MERGE/DRY_RUN]
Agenti attivi: [lista]
```

---

## Principi Fondamentali (Non Violabili)

| Principio | Regola operativa |
|---|---|
| **Zero Hallucination** | Ogni fatto nella wiki deve essere tracciabile al raw content |
| **Zero Data Loss** | Nessun contenuto scartato senza log esplicito |
| **Idempotenza** | Stesso input → stesso output sempre |
| **Incrementalità** | Aggiorna senza duplicare, arricchisce senza sovrascrivere |
| **Immutabilità Raw** | I file raw salvati non vengono mai modificati |

---

## Esecuzione Pipeline

### AG-01 — Orchestrator (sempre attivo)
Leggi **`agents/orchestrator.md`** per le istruzioni operative.
Coordina tutti gli agenti, passa il ContextBundle, attiva il Self-Healing su errore.

### AG-02 — WebFetch (solo PIPELINE FULL)
Leggi **`agents/webfetch-parser.md`** → sezione WebFetch.
Scarica, sanitizza e salva il raw content in `2Brain/raw/YYYY-MM-DD_slug.md`.

### AG-03 — Parser Semantico (sempre attivo)
Leggi **`agents/webfetch-parser.md`** → sezione Parser.
Estrae: entità, relazioni, fatti chiave, citazioni, knowledge graph, classificazione vault.

### AG-04 — Wiki Builder (sempre attivo)
Leggi **`agents/wiki-builder.md`**.
Crea o aggiorna la pagina nel vault 2Brain con template standardizzato.

### AG-05 — QC Verifier (sempre attivo)
Leggi **`agents/qc-self-healing.md`** → sezione QC Verifier.
Verifica: fidelity ≥ 99%, zero allucinazioni, struttura completa.
Se FAIL → attiva AG-06.

### AG-06 — Self-Healing (solo su errore o QC FAIL)
Leggi **`agents/qc-self-healing.md`** → sezione Self-Healing.
Recupera automaticamente da fallimenti con strategia specifica per tipo di errore.

### AG-07 — Index & Log (sempre attivo)
Leggi **`agents/index-log.md`**.
Aggiorna `2Brain/index.md` e scrive entry in `2Brain/log.md`.

---

## Verdetti QC

| Fidelity | Allucinazioni | Struttura | Verdict | Azione |
|---|---|---|---|---|
| ≥ 99% | 0 | valida | `PASS` | → AG-07 |
| ≥ 95% | 0 | valida | `PASS_WITH_WARNINGS` | → AG-07 + segnala |
| < 95% | qualsiasi | qualsiasi | `FAIL` | BLOCCA → AG-06 |
| qualsiasi | > 0 | qualsiasi | `FAIL` | BLOCCA IMMEDIATO |

---

## Output Finale all'Utente

Al termine presenta sempre:
```
✅ DeepSearch completato
Pipeline: [FULL/PARTIAL] | Modalità: [CREATE/UPDATE]
Raw salvato: [path o "N/A"]
Wiki page: [path]
QC: [PASS/PASS_WITH_WARNINGS] | Fidelity: [N]% | Completeness: [N]%
Sezioni popolate: [N]/9
Backlink creati: [lista]
Log: 2Brain/log.md aggiornato
```

Se FAIL non recuperabile:
```
❌ DeepSearch — Errore non recuperabile
Tipo: [tipo errore]
Motivo: [spiegazione]
Azione richiesta: [cosa deve fare l'utente]
```

---

## File di Riferimento

| File | Leggi quando |
|---|---|
| `agents/orchestrator.md` | Prima di iniziare qualsiasi pipeline |
| `agents/webfetch-parser.md` | Per AG-02 (WebFetch) e AG-03 (Parser) |
| `agents/wiki-builder.md` | Per AG-04 (Wiki Builder) |
| `agents/qc-self-healing.md` | Per AG-05 (QC) e AG-06 (Self-Healing) |
| `agents/index-log.md` | Per AG-07 (Index & Log) |
| `references/vault-structure.md` | Per path e struttura del vault 2Brain |
| `references/wiki-template.md` | Template completo pagina wiki |
| `references/error-matrix.md` | Matrice errori Self-Healing con strategie di fix |

---

## Input

$ARGUMENTS
