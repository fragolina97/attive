# AG-05 QC Verifier + AG-06 Self-Healing

---

## AG-05 — QC Verifier (sempre attivo)

**Input**: wiki_page (da AG-04) + raw_content (da AG-02 o AG-03)
**Output**: QCReport con verdict, fidelity score, completeness score

### Step di Esecuzione

1. **Check Allucinazioni**: per ogni affermazione della wiki, verifica che sia presente nel raw content (verbatim o parafrasi fedele). Tolleranza: **ZERO**. Eccezioni: inferenze marcate `[inferito]`, definizioni universalmente accettate.

2. **Score Fidelity**: `fatti_verificati / fatti_totali × 100`. Ogni fatto deve essere tracciabile al raw.

3. **Score Completeness**: `fatti_inclusi / fatti_rilevanti × 100`. Fatti rilevanti omessi devono essere loggati con motivazione.

4. **Check Struttura**:
   - Tutti i campi frontmatter presenti: `type, title, area, sub_area, tags, source, created, updated, qc_score, status`
   - Tutte le 9 sezioni obbligatorie presenti
   - Almeno un backlink `[[...]]` presente
   - Sezione Fonti con link verificabile

5. **Check Coerenza Vault**: nessun duplicato, path coerente con la classificazione.

6. **Determina Verdict**:

| Condizione | Verdict | Azione |
|---|---|---|
| Fidelity ≥ 99%, allucinazioni = 0, struttura valida | `PASS` | → AG-07 |
| Fidelity ≥ 95%, allucinazioni = 0, struttura valida | `PASS_WITH_WARNINGS` | → AG-07 + segnala |
| Fidelity < 95% O struttura invalida | `FAIL` | BLOCCA → AG-06 |
| Allucinazioni > 0 | `FAIL` | BLOCCA IMMEDIATO → AG-06 |

7. **Aggiorna frontmatter**: scrivi i valori reali di `fidelity` e `completeness` nel frontmatter della pagina wiki.

---

## AG-06 — Self-Healing (solo su errore o QC FAIL)

**Input**: errore rilevato + ContextBundle
**Output**: artefatto corretto + healing_log

### Matrice degli Errori

| Tipo Errore | Severità | Max Tentativi | Richiede Utente |
|---|---|---|---|
| `url_unreachable` | HIGH | 3 | Solo se tutti falliscono |
| `html_unparseable` | MEDIUM | 2 | No |
| `content_too_long` | LOW | 1 | No |
| `hallucination_detected` | CRITICAL | 2 | No |
| `page_duplicate` | MEDIUM | 1 | No |
| `data_conflict` | HIGH | 0 | **Sempre** |
| `folder_missing` | LOW | 1 | No |
| `template_malformed` | MEDIUM | 2 | No |
| `all_retries_exhausted` | CRITICAL | 0 | **Sempre** |

### Strategie di Fix per Tipo

| Tipo Errore | Strategia |
|---|---|
| `url_unreachable` | Retry con backoff esponenziale (1s, 2s, 4s) |
| `html_unparseable` | Tenta estrazione testo puro senza parsing HTML |
| `content_too_long` | Tronca al limite, logga le sezioni omesse |
| `hallucination_detected` | Rilancia AG-03 (Parser) con istruzione esplicita di non aggiungere fatti non presenti nel raw |
| `page_duplicate` | Switcha automaticamente a modalità MERGE |
| `data_conflict` | **Non auto-risolvere** — presenta entrambe le versioni all'utente |
| `folder_missing` | Crea la cartella mancante, riprendi da AG-04 |
| `template_malformed` | Ricrea la pagina da template pulito con i dati già estratti |

### Healing Log Format

```
HEALING-[NNN]
Tipo errore: [tipo]
Agente fallito: [AG-XX]
Strategia applicata: [descrizione]
Tentativo: [N]/[MAX]
Esito: RISOLTO / FALLITO / ESCALATED_TO_USER
Azione successiva: [cosa fa il sistema]
```

### Dopo il Fix

Se risolto → riparte da AG-04 (Wiki Builder) con i dati corretti.
Se fallisce dopo MAX tentativi → escalate all'utente con healing_log completo.
