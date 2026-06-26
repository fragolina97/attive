---
name: inkos-grounding-v2
description: InkOS v2 grounding layer — valuta il contesto dal Second Brain prima di autorizzare la scrittura. Implementa la no-invention rule, il context score ibrido, l'approval session e il chapter tracking. Da usare PRIMA di inkos-multi-agent-novel-writing per progetti basati su fonti reali (saggi, libri tecnici, corsi). Per fiction pura usa direttamente inkos.
triggers:
  - inkos grounding
  - valuta contesto prima di scrivere
  - source context score
  - no invention rule
  - grounding layer inkos
  - libro da wiki
  - libro da second brain
  - scrivi libro da appunti
  - inkos v2
---

# InkOS Grounding v2

Questo skill implementa il **layer di grounding** dell'architettura InkOS v2 MASTER_SPEC.

**Quando usarlo:** progetti basati su fonti reali (saggi, libri tecnici, corsi, libri di trading, guide). NON serve per fiction pura — per quella usa direttamente `/inkos-multi-agent-novel-writing`.

**Cosa fa:** valuta se hai abbastanza contesto nel tuo Second Brain prima di autorizzare la scrittura, poi passa il controllo a `inkos` per la produzione narrativa.

---

## REGOLA MADRE

InkOS non inventa mai contenuto fattuale, tecnico, economico, storico, scientifico, legale, medico, biografico o documentale senza contesto sufficiente.

Prima della scrittura mostra sempre:
```
Source Context Score: X/100
Status: sufficient | partial | insufficient
```

Soglie:
- 80–100 = sufficient → può scrivere
- 50–79  = partial   → può fare outline, non scrivere
- 0–49   = insufficient → blocca tutto

---

## PIPELINE

```
1. PROJECT INIT     — crea struttura progetto
2. INTAKE           — questionario prodotto (27 campi)
3. BRAIN SCAN       — indicizza Second Brain e cerca materiale
4. COVERAGE SCORE   — calcola context score ibrido
5. CONTRADICTION    — rileva contraddizioni esplicite tra fonti
6. GATE             — mostra score, chiede approvazione
7. HANDOFF → inkos  — passa a inkos write/audit/revise
```

---

## COMANDI PRINCIPALI

### `/inkos-grounding-v2 init <titolo>`

Inizializza un nuovo progetto InkOS con grounding abilitato.

**Azione:** Chiedi all'utente:
1. Titolo del progetto
2. Tipo prodotto: `saggio | libro_tecnico | corso | webnovel_fondato | romanzo_storico`
3. Argomento principale
4. Second Brain path (default: `~/.../2Brain/2Brain/`)
5. Genre per inkos (se narrativo): `xuanhuan | xianxia | general | horror | dushi`

Crea struttura:
```
<titolo>/
  story/
    setup/
      inkos_project_state.json
      product_intake.json
    research/
      source_context_pack.json
      writer_approval_gate.json
    chapters/
      chapter_manifest.json
    logs/
      chapter_events.jsonl
```

`inkos_project_state.json` iniziale:
```json
{
  "version": "2.5.6",
  "project_title": "<titolo>",
  "grounding_enabled": true,
  "pipeline": {
    "product_intake": "not_started",
    "knowledge_packs": "not_started",
    "second_brain_context": "not_started",
    "writer_approval": "not_started",
    "writing": "blocked_until_approval"
  },
  "hard_rules": {
    "no_invention_without_context": true,
    "show_score_before_writing": true,
    "user_must_choose_before_writing": true
  }
}
```

---

### `/inkos-grounding-v2 intake <titolo>`

Compila il questionario prodotto.

**Azione:** Fai queste domande in sequenza (accetta "random" per avere un suggerimento):

1. **Tipo prodotto** — saggio / libro tecnico / corso / romanzo fondato / altro
2. **Serializzazione** — volume unico / serie (quanti volumi?)
3. **Genere primario** — es. trading, business, finanza, storia, medicina
4. **Premessa** — in una frase: di cosa parla il libro?
5. **Promessa al lettore** — cosa impara/ottiene leggendolo?
6. **Tono** — divulgativo / accademico / narrativo / pratico-operativo
7. **Target audience** — es. trader retail, imprenditori, studenti
8. **Elementi obbligatori** — cosa non può mancare?
9. **Elementi vietati** — cosa non vuoi vedere?
10. **Opere di riferimento** — libri simili o ispiratori

Salva in `story/setup/product_intake.json`. Aggiorna pipeline status a `completed`.

---

### `/inkos-grounding-v2 scan <titolo> "<query>"`

Scansiona il Second Brain e calcola il context score.

**Azione:**

**Step 1 — Query expansion:** Espandi la query in 3-5 varianti semantiche.

**Step 2 — Scan 2Brain:** Leggi i file nel vault wiki/ cercando corrispondenze. Per ogni file calcola:
- `title_tag_score` (0-30)
- `heading_score` (0-15)
- `content_score` (0-30)
- `freshness` (0-10)
- `concept_density` (0-10)
- `internal_links` (0-5)

**Step 3 — Coverage analysis:** `coverage_score = (argomenti_coperti / argomenti_totali) * 100`

**Step 4 — Formula finale (HybridRetrievalFusion):**
```
final_context_score =
  coverage_score         * 0.40
+ evidence_score         * 0.25
+ semantic_score         * 0.15
+ source_quality_score   * 0.10
+ contradiction_free     * 0.10
```

**Step 5 — Contradiction detection baseline:**
Cerca contraddizioni esplicite: `direct_negation`, `directional_conflict`, `numeric_conflict` (>20%).

**REGOLA:** Non dire mai "nessuna contraddizione presente". Dire "nessuna contraddizione esplicita rilevata dal detector baseline".

**Output — mostra all'utente:**
```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SOURCE CONTEXT SCORE: 74/100
STATUS: partial

BREAKDOWN:
  coverage_score:       68  (×0.40)
  evidence_score:       80  (×0.25)
  semantic_score:       75  (×0.15)
  source_quality:       70  (×0.10)
  contradiction_free:   70  (×0.10)

FONTI TROVATE: 8 pagine
CONTRADDIZIONI: nessuna esplicita rilevata (baseline rule-based)
MISSING CONTEXT: [lista argomenti non coperti]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

Salva in `story/research/source_context_pack.json`.

---

### `/inkos-grounding-v2 gate <titolo>`

Mostra il gate e chiede l'approvazione utente.

**sufficient (≥80):**
```
[1] proceed_once    — autorizza solo il prossimo capitolo
[2] proceed_session — autorizza sessione (max 5 cap, 4 ore TTL)
[3] provide_more_context
[4] cancel
```

**partial (50-79):**
```
[1] proceed_once (forced — solo outline o capitoli descrittivi)
[2] provide_more_context
[3] cancel
```

**insufficient (<50):**
```
[1] provide_more_context
[2] cancel
```

Salva decisione in `story/research/writer_approval_gate.json`.
Aggiorna `inkos_project_state.json` → `"writing": "allowed"`.

---

### `/inkos-grounding-v2 handoff <titolo>`

Verifica il WriterContextGuard e passa a inkos.

Blocca se:
- `source_context_pack.json` mancante
- `can_write = false`
- `writer_approval_gate.json` mancante o `decision != proceed*`
- sessione scaduta (TTL o max_chapters raggiunto)

Se valido, mostra i comandi inkos disponibili:
```bash
inkos book create --title "<titolo>" --genre <genre>
inkos write next <titolo>
inkos audit <titolo> --chapter 1
```

---

### `/inkos-grounding-v2 status <titolo>`

Mostra stato completo del progetto (pipeline, score, chapter tracking, prossimo step).

---

## FLUSSO COMPLETO

```bash
/inkos-grounding-v2 init "Libro Wyckoff"
/inkos-grounding-v2 intake "Libro Wyckoff"
/inkos-grounding-v2 scan "Libro Wyckoff" "Wyckoff method accumulation distribution"
/inkos-grounding-v2 gate "Libro Wyckoff"
/inkos-grounding-v2 handoff "Libro Wyckoff"

# Da qui: inkos da terminale
inkos book create --title "Libro Wyckoff" --genre general
inkos write next "Libro Wyckoff"
inkos audit "Libro Wyckoff" --chapter 1
inkos revise "Libro Wyckoff" --chapter 1
```

---

## MODALITÀ FICTION PURA

Se il progetto è **fiction pura** (webnovel, romanzo, storia inventata):
- NON usare questo skill
- Vai direttamente a `inkos book create --genre xuanhuan` o simile

---

## INTEGRAZIONE CON 2BRAIN

Le cartelle più rilevanti per tipo di libro:
- Trading/finanza → `wiki/concepts/` (indicatori, strategie, Wyckoff, Elliott Wave)
- Business → `wiki/concepts/` (template YC, marketing skills)
- Progetti → `wiki/projects/`

Per aggiungere contesto: usa `/deep-research` per arricchire il vault, poi ri-esegui `scan`.
