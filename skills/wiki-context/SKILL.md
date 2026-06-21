# Wiki Context Loader

Carica il contesto completo della wiki e rispondi con piena consapevolezza della knowledge base.

## Quando usare
Invoca `/wiki-context` quando:
- Hai bisogno di contesto completo prima di rispondere
- Stai pianificando qualcosa connesso a progetti esistenti
- Vuoi sapere cosa sa già la wiki su un argomento

## Procedura

### Step 1 — Carica indice master
Leggi `2Brain/2Brain/index.md`

### Step 2 — Carica log recente
Leggi `2Brain/2Brain/log.md`

### Step 3 — Identifica pagine rilevanti
Individua le 3-5 pagine più rilevanti e leggile.

### Step 4 — Rispondi con contesto
Integra la conoscenza wiki nella risposta. Cita le pagine usate.

### Step 5 — Aggiorna se necessario
Se la conversazione aggiunge nuova conoscenza, aggiorna le pagine wiki e il log.

## Struttura wiki
```
Indice:    2Brain/2Brain/index.md
Log:       2Brain/2Brain/log.md
Concepts:  2Brain/2Brain/wiki/concepts/
Projects:  2Brain/2Brain/wiki/projects/
Entities:  2Brain/2Brain/wiki/entities/
Sources:   2Brain/2Brain/wiki/sources/
Outputs:   2Brain/2Brain/wiki/outputs/
```
