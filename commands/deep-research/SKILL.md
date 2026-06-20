---
name: deep-research
description: Attiva il sistema multi-agente DeepSearch per acquisire, analizzare e integrare conoscenza nel vault 2Brain. Questa skill deve essere usata ESCLUSIVAMENTE quando l'utente invoca esplicitamente il comando /deep-research. NON triggerare mai in risposta a URL, testo libero, parole chiave, contesto conversazionale o qualsiasi altro input che non sia il comando diretto /deep-research.
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
  --dry-run → esegui pipeline ma non scrivere nessun file
  --rebuild → rigenera pagina esistente da zero
  --update  → forza merge su pagina esistente
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

## Agenti

### AG-01 — Orchestrator → `agents/orchestrator.md`
### AG-02 — WebFetch (solo FULL) → `agents/webfetch-parser.md`
### AG-03 — Parser Semantico → `agents/webfetch-parser.md`
### AG-04 — Wiki Builder → `agents/wiki-builder.md`
### AG-05 — QC Verifier → `agents/qc-self-healing.md`
### AG-06 — Self-Healing (solo su errore) → `agents/qc-self-healing.md`
### AG-07 — Index & Log → `agents/index-log.md`

---

## Verdetti QC

| Fidelity | Allucinazioni | Struttura | Verdict |
|---|---|---|---|
| ≥ 99% | 0 | valida | `PASS` |
| ≥ 95% | 0 | valida | `PASS_WITH_WARNINGS` |
| < 95% | qualsiasi | qualsiasi | `FAIL` |
| qualsiasi | > 0 | qualsiasi | `FAIL` |

---

## File di Riferimento

| File | Scopo |
|---|---|
| `agents/orchestrator.md` | AG-01 — coordinamento pipeline |
| `agents/webfetch-parser.md` | AG-02 WebFetch + AG-03 Parser |
| `agents/wiki-builder.md` | AG-04 Wiki Builder |
| `agents/qc-self-healing.md` | AG-05 QC + AG-06 Self-Healing |
| `agents/index-log.md` | AG-07 Index & Log |
| `references/vault-structure.md` | Struttura vault 2Brain |
| `references/wiki-template.md` | Template pagina wiki |
| `references/error-matrix.md` | Matrice errori Self-Healing |

$ARGUMENTS
