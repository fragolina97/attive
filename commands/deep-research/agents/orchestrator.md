# AG-01 — Orchestrator

**Sempre attivo.** Coordina l'intera pipeline, gestisce il ContextBundle, attiva il Self-Healing su errore e assembla il report finale.

---

## ContextBundle

Il ContextBundle è il pacchetto dati condiviso tra tutti gli agenti. Ogni agente legge da qui e scrive i propri output qui.

```
ContextBundle:
  parsed_input:   { raw_command, input_content, input_type, pipeline, mode, flags }
  raw_content:    output di AG-02 (solo FULL) o None
  parsed_data:    output di AG-03
  wiki_page:      output di AG-04
  qc_report:      output di AG-05
  healing_log:    output di AG-06 (solo se attivato)
  log_entry:      output di AG-07
  agent_results:  lista { agent_id, status, warnings }
  errors:         lista di errori accumulati
```

---

## Logica di Esecuzione

1. Ricevi il ParsedInput dall'Activation Gate (classificazione già fatta in SKILL.md)
2. Seleziona la pipeline corretta (FULL o PARTIAL)
3. Per ogni agente nella pipeline:
   - Verifica se è condizionale (AG-06 lo è: si attiva solo su errore o QC FAIL)
   - Esegui l'agente e salva il risultato nel ContextBundle
   - Se l'agente fallisce → aggiungi l'errore alla lista `errors`
   - Se AG-06 fallisce → ABORT pipeline, escalate all'utente
4. Assembla il report finale e presentalo all'utente

---

## Condizione di Attivazione AG-06

AG-06 si attiva se:
- `qc_report.verdict == FAIL`
- OPPURE `errors` contiene almeno un errore da agenti precedenti

Se AG-06 si attiva e risolve il problema → riparte da AG-04 (Wiki Builder).
Se AG-06 fallisce → ABORT con messaggio di errore dettagliato all'utente.

---

## Gestione Errori

| Situazione | Azione |
|---|---|
| Agente completa con warnings | Continua pipeline, annota warnings |
| Agente fallisce con errore recuperabile | Attiva AG-06 |
| AG-06 esaurisce i retry | ABORT, escalate all'utente |
| Input vuoto o non classificabile | Chiedi chiarimento all'utente |

---

## Report Finale (da costruire)

```
pipeline:       FULL / PARTIAL
mode:           CREATE / UPDATE / MERGE / DRY_RUN
agent_results:  [ {agent_id, status, warnings} ]
raw_file:       path del file raw (o null)
wiki_path:      path della pagina wiki creata/aggiornata
qc_verdict:     PASS / PASS_WITH_WARNINGS / FAIL
fidelity:       float (percentuale)
completeness:   float (percentuale)
errors:         [] o lista errori
log_entry:      entry scritta in log.md
```
