# Error Matrix — Self-Healing

Matrice completa degli errori gestiti da AG-06, con strategie di fix e limite di tentativi.

---

## Matrice Errori

| Tipo Errore | Agente Fallito | Severità | Max Tentativi | Richiede Utente | Strategia |
|---|---|---|---|---|---|
| `url_unreachable` | AG-02 | HIGH | 3 | Solo se tutti falliscono | Retry con backoff 1s/2s/4s |
| `html_unparseable` | AG-02 | MEDIUM | 2 | No | Estrazione testo puro |
| `content_too_long` | AG-02 | LOW | 1 | No | Tronca a 50.000 chars, logga omissioni |
| `hallucination_detected` | AG-05 | CRITICAL | 2 | No | Rilancia AG-03 con istruzione zero-hallucination |
| `page_duplicate` | AG-04 | MEDIUM | 1 | No | Switch automatico a modalità MERGE |
| `data_conflict` | AG-04 | HIGH | 0 | **Sempre** | Presenta entrambe le versioni all'utente |
| `folder_missing` | AG-04 | LOW | 1 | No | Crea cartella, riprendi da AG-04 |
| `template_malformed` | AG-04 | MEDIUM | 2 | No | Ricrea pagina da template pulito |
| `qc_fidelity_low` | AG-05 | HIGH | 2 | No | Rilancia AG-03 con istruzione di maggiore fedeltà |
| `qc_structure_invalid` | AG-05 | MEDIUM | 2 | No | Rilancia AG-04 con sezioni mancanti identificate |
| `index_write_failed` | AG-07 | LOW | 2 | No | Riprova scrittura index.md |
| `all_retries_exhausted` | qualsiasi | CRITICAL | 0 | **Sempre** | ABORT + report dettagliato all'utente |

---

## Flow di Recupero

```
Errore rilevato
      ↓
AG-06 consulta la matrice
      ↓
Richiede utente?
  SÌ  → presenta il problema + entrambe le opzioni → attendi input
  NO  → applica strategia di fix
          ↓
      Verifica risoluzione (AG-05 o AG-02 ri-esegue)
          ↓
      Risolto? → riprendi pipeline dal punto di fallimento
      Non risolto? → incrementa retry_count
          ↓
      retry_count >= MAX? → ABORT + escalate all'utente
```

---

## Formato Messaggio di Escalation all'Utente

```
❌ DeepSearch — Intervento richiesto

Errore: [tipo_errore]
Agente: [AG-XX]
Tentativo: [N] di [MAX]
Motivo: [spiegazione chiara]

Situazione attuale:
[descrizione dello stato del sistema]

Opzioni disponibili:
1. [Opzione A] — [conseguenza]
2. [Opzione B] — [conseguenza]
3. Annulla operazione

Come vuoi procedere?
```

---

## Errori Non Auto-Recuperabili

Questi errori richiedono **sempre** intervento umano:

- `data_conflict` — Claude non decide quale versione è corretta
- `all_retries_exhausted` — il sistema non può procedere senza input
- Qualsiasi errore con impatto su dati esistenti non verificabili automaticamente
