# AG-07 — Index & Log (sempre attivo)

**Input**: wiki_page approvata da AG-05 + ContextBundle completo
**Output**: index.md aggiornato + entry in log.md

---

## Step di Esecuzione

### 1. Aggiorna 2Brain/index.md

Aggiungi o aggiorna la voce nella sezione appropriata dell'indice:

```markdown
- [Titolo Pagina](path/relativo.md) — [descrizione in una riga]
```

Regole:
- Cerca prima se la voce esiste già → aggiorna solo la descrizione se cambiata
- Inserisci nella sezione corretta in base all'area della pagina
- Aggiorna il contatore in fondo all'indice: `Pagine totali: [N]`
- Aggiorna `Ultimo aggiornamento: YYYY-MM-DD`

### 2. Scrivi entry in 2Brain/log.md

Formato obbligatorio:
```markdown
## [YYYY-MM-DD] [tipo operazione] | [titolo pagina]

**Fonte**: [url o "input diretto"]
**Pipeline**: [FULL/PARTIAL] | **Modalità**: [CREATE/UPDATE/MERGE]
**Path wiki**: [path]
**Raw file**: [path o "N/A"]
**QC**: [PASS/PASS_WITH_WARNINGS] | Fidelity: [N]% | Completeness: [N]%
**Sezioni**: [N]/9 | **Backlink**: [lista o "nessuno"]
**Entità estratte**: [N] | **Relazioni**: [N] | **Fatti chiave**: [N]

[Note: eventuali warnings o osservazioni rilevanti]
```

Tipi operazione: `ingest` | `update` | `merge` | `rebuild` | `lint`

### 3. Aggiorna changelog (se esistente)

Se `2Brain/meta/changelog.md` esiste, aggiungi voce:
```
[YYYY-MM-DD HH:MM] | [FULL/PARTIAL] | [titolo] | [PASS/WARN] | [path]
```

---

## Regole di Integrità

- Il log è **append-only**: non modificare voci precedenti
- Se index.md non esiste → crealo con struttura base
- Se log.md non esiste → crealo con header standard
- Ogni operazione DeepSearch deve avere la sua entry nel log — senza eccezioni

---

## Output da Restituire all'Orchestrator

```
log_entry: {
  timestamp:    "YYYY-MM-DD",
  operation:    "ingest/update/merge",
  page_title:   "[titolo]",
  wiki_path:    "[path]",
  raw_path:     "[path o null]",
  qc_verdict:   "PASS/PASS_WITH_WARNINGS",
  index_updated: true/false,
  log_updated:   true/false
}
```
