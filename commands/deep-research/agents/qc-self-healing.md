# AG-05 QC Verifier + AG-06 Self-Healing

## AG-05 — QC Verifier

**Input**: wiki_page + raw_content · **Output**: QCReport

1. **Check Allucinazioni**: ogni affermazione della wiki deve essere nel raw. Tolleranza: **ZERO**.
2. **Score Fidelity**: `fatti_verificati / fatti_totali × 100`
3. **Score Completeness**: `fatti_inclusi / fatti_rilevanti × 100`
4. **Check Struttura**: tutti i campi frontmatter, 9 sezioni, almeno un backlink, sezione Fonti
5. **Check Coerenza Vault**: no duplicati, path coerente
6. **Determina Verdict**:

| Condizione | Verdict | Azione |
|---|---|---|
| Fidelity ≥ 99%, allucinazioni = 0, struttura valida | `PASS` | → AG-07 |
| Fidelity ≥ 95%, allucinazioni = 0, struttura valida | `PASS_WITH_WARNINGS` | → AG-07 |
| Fidelity < 95% O struttura invalida | `FAIL` | BLOCCA → AG-06 |
| Allucinazioni > 0 | `FAIL` | BLOCCA IMMEDIATO |

## AG-06 — Self-Healing

**Input**: errore + ContextBundle · **Output**: artefatto corretto + healing_log

| Tipo Errore | Strategia |
|---|---|
| `url_unreachable` | Retry backoff 1s/2s/4s |
| `html_unparseable` | Estrazione testo puro |
| `content_too_long` | Tronca a 50.000 chars |
| `hallucination_detected` | Rilancia AG-03 con istruzione zero-hallucination |
| `page_duplicate` | Switch a modalità MERGE |
| `data_conflict` | **Richiede utente sempre** |
| `folder_missing` | Crea cartella, riprendi da AG-04 |
| `template_malformed` | Ricrea da template pulito |

Se risolto → riparte da AG-04. Se fallisce dopo MAX tentativi → escalate all'utente.
