# AG-07 — Index & Log

**Sempre attivo.** Aggiorna `2Brain/index.md` e scrive entry in `2Brain/log.md`.

## Step di Esecuzione

### 1. Aggiorna 2Brain/index.md

```markdown
- [Titolo Pagina](path/relativo.md) — [descrizione in una riga]
```

- Cerca voce esistente → aggiorna solo se descrizione cambiata
- Inserisci nella sezione corretta per area
- Aggiorna contatore `Pagine totali: [N]` e `Ultimo aggiornamento: YYYY-MM-DD`

### 2. Scrivi entry in 2Brain/log.md

```markdown
## [YYYY-MM-DD] [tipo operazione] | [titolo pagina]

**Fonte**: [url o "input diretto"]
**Pipeline**: [FULL/PARTIAL] | **Modalità**: [CREATE/UPDATE/MERGE]
**Path wiki**: [path]
**Raw file**: [path o "N/A"]
**QC**: [PASS/PASS_WITH_WARNINGS] | Fidelity: [N]% | Completeness: [N]%
**Sezioni**: [N]/9 | **Backlink**: [lista]
**Entità estratte**: [N] | **Relazioni**: [N] | **Fatti chiave**: [N]
```

Tipi: `ingest` | `update` | `merge` | `rebuild` | `lint`

## Regole di Integrità

- Log è **append-only**: non modificare voci precedenti
- Se index.md non esiste → crealo
- Se log.md non esiste → crealo
- Ogni operazione DeepSearch deve avere la sua entry — senza eccezioni
