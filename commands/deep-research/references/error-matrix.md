# Error Matrix — Self-Healing

## Matrice Errori

| Tipo Errore | Agente | Severità | Max Tentativi | Utente | Strategia |
|---|---|---|---|---|---|
| `url_unreachable` | AG-02 | HIGH | 3 | Solo se tutti falliscono | Retry backoff 1s/2s/4s |
| `html_unparseable` | AG-02 | MEDIUM | 2 | No | Estrazione testo puro |
| `content_too_long` | AG-02 | LOW | 1 | No | Tronca a 50.000 chars |
| `hallucination_detected` | AG-05 | CRITICAL | 2 | No | Rilancia AG-03 zero-hallucination |
| `page_duplicate` | AG-04 | MEDIUM | 1 | No | Switch a MERGE |
| `data_conflict` | AG-04 | HIGH | 0 | **Sempre** | Presenta entrambe le versioni |
| `folder_missing` | AG-04 | LOW | 1 | No | Crea cartella, riprendi AG-04 |
| `template_malformed` | AG-04 | MEDIUM | 2 | No | Ricrea da template pulito |
| `qc_fidelity_low` | AG-05 | HIGH | 2 | No | Rilancia AG-03 maggiore fedeltà |
| `qc_structure_invalid` | AG-05 | MEDIUM | 2 | No | Rilancia AG-04 sezioni mancanti |
| `index_write_failed` | AG-07 | LOW | 2 | No | Riprova scrittura index.md |
| `all_retries_exhausted` | qualsiasi | CRITICAL | 0 | **Sempre** | ABORT + report |

## Errori Non Auto-Recuperabili

- `data_conflict` — Claude non decide quale versione è corretta
- `all_retries_exhausted` — sistema non può procedere
