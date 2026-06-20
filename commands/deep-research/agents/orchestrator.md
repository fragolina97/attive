# AG-01 — Orchestrator

**Sempre attivo.** Coordina l'intera pipeline, gestisce il ContextBundle, attiva il Self-Healing su errore.

## ContextBundle

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

## Logica di Esecuzione

1. Ricevi il ParsedInput dall'Activation Gate
2. Seleziona la pipeline corretta (FULL o PARTIAL)
3. Per ogni agente nella pipeline:
   - Esegui e salva il risultato nel ContextBundle
   - Se fallisce → aggiungi errore alla lista `errors`
   - Se AG-06 fallisce → ABORT, escalate all'utente
4. Assembla il report finale

## Condizione di Attivazione AG-06

AG-06 si attiva se `qc_report.verdict == FAIL` oppure `errors` contiene errori.
Se AG-06 risolve → riparte da AG-04. Se fallisce → ABORT.

## Gestione Errori

| Situazione | Azione |
|---|---|
| Agente completa con warnings | Continua, annota warnings |
| Agente fallisce recuperabile | Attiva AG-06 |
| AG-06 esaurisce retry | ABORT, escalate |
| Input non classificabile | Chiedi chiarimento |
