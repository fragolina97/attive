---
name: handoff
description: Genera un file handoff.md con la fotografia tecnica e azionabile dello stato reale del lavoro, per passare contesto a una nuova sessione AI o collaboratore. Attivazione SOLO con comando esplicito /handoff. Implementa scope isolation, evidence policy anti-invenzione, validazione next step e modalità force.
triggers:
  - /handoff
---

# Skill: `/handoff`

**Version:** 1.2  
**Default language:** Italiano  
**Activation:** Solo comando esplicito `/handoff`

---

## 1. Purpose

Generare un file Markdown `handoff.md` che permetta a una nuova AI,
a un collaboratore o allo stesso utente di riprendere il lavoro
senza perdere contesto operativo.

Non è un riassunto generico.  
È una fotografia tecnica, sintetica e azionabile dello stato reale del lavoro,
riferita a uno scope preciso e ben isolato.

---

## 2. Activation

La skill si attiva **esclusivamente** se il primo token del messaggio è esattamente `/handoff`.

| Variante comando         | Comportamento                                      |
|--------------------------|-------------------------------------------------|
| `/handoff`               | Attivazione standard                               |
| `/handoff <testo>`       | Il testo viene usato come contesto aggiuntivo      |
| `/handoff force`         | Genera senza chiedere, segnala i gap con ⚠️        |
| `/handoff --force`       | Identico a `force`                                 |
| `/handoff -f`            | Identico a `force`                                 |
| `/handoff forza`         | Identico a `force`                                 |
| `/handoff scope: X`      | Usa `X` come scope prioritario                     |
| `/handoff progetto: X`   | Usa `X` come scope prioritario                     |
| `/handoff argomento: X`  | Usa `X` come scope prioritario                     |

La skill **non si attiva** se:
- `handoff` compare in una domanda teorica o descrittiva;
- la richiesta è ipotetica o condizionale;
- il primo token non è esattamente `/handoff`;
- il comando è simile ma non identico, per esempio `/handoff123`.

---

## 3. Scope

Ogni handoff deve riferirsi a **un solo progetto, task o argomento**.  
Questa sezione impedisce che il file mescoli contesti diversi presenti nella stessa chat.

**Regole di risoluzione scope:**

| Situazione                          | Comportamento                                              |
|-------------------------------------|---------------------------------------------------------|
| Scope esplicito nel comando         | Usarlo direttamente                                        |
| Un solo progetto nella conversazione| Usarlo come scope inferito                                 |
| Più progetti nella conversazione    | Chiedere chiarimento, salvo `force`                        |
| `force` attivo e scope assente      | Generare e segnalare con ⚠️                                |

**Esempi di scope validi:**
- `InkOS`
- `TradingBerry`
- `CRM`
- `FlowBoard`
- `AKOA`

---

## 4. Input Sources

Le informazioni devono provenire da:
- testo del comando `/handoff`, incluso testo inline;
- messaggi della conversazione corrente **rilevanti per lo scope risolto**;
- file o allegati esplicitamente richiamati nella conversazione corrente, se pertinenti allo scope.

> ⚠️ Non usare tutta la conversazione se contiene progetti diversi.  
> Prima risolvi lo scope, poi filtra il contesto.

---

## 5. Extraction Schema

### Critical fields

Campi bloccanti se mancanti. Richiedono chiarimento, salvo `force`.

| Campo           | Descrizione                                                              |
|-----------------|-------------------------------------------------------------------------|
| `scope`         | Progetto o argomento esatto a cui si riferisce il handoff                |
| `objective`     | Obiettivo finale del progetto o task                                     |
| `current_state` | Stato reale del lavoro, vincoli, contraddizioni, ambiguità               |
| `next_step`     | Una sola azione concreta, non ambigua e verificabile                     |

### Standard fields

Campi presenti nel file finale, anche solo con fallback testuale.

| Campo                  | Descrizione                                                         |
|------------------------|--------------------------------------------------------------------|
| `files_in_flight`      | File, documenti o componenti coinvolti                              |
| `confirmed_decisions`  | Decisioni definitive, da non riaprire salvo comando esplicito       |
| `open_questions`       | Punti ancora da decidere                                            |
| `changed`              | Modifiche, decisioni o chiarimenti emersi nella sessione corrente   |
| `failed_attempts`      | Tentativi falliti o approcci scartati, con motivo                   |

---

## 6. Next Step — Definizione di qualità

Il campo `next_step` deve essere:

| Requisito       | Descrizione                                                    |
|-----------------|---------------------------------------------------------------|
| **Unico**       | Una sola azione, non una lista                                 |
| **Concreto**    | Descrive qualcosa di specifico da fare                         |
| **Non ambiguo** | Non inizia con verbi vaghi come "continuare", "migliorare"     |
| **Verificabile**| Ha una condizione di completamento implicita o esplicita       |
| **Prioritario** | È la cosa più importante da fare subito                        |

**Esempio forte:**
> "Chiudere la scheda Party/Riserve CTB decidendo costo cambio, ingresso riserve e attacco di opportunità."

**Esempio debole:**
> "Continuare il sistema di combattimento."

---

## 7. Output Template

```md
# Handoff

## Scope
[Progetto o argomento a cui si riferisce questo handoff.]

## Goal
[Descrizione chiara dell'obiettivo finale del progetto o task in 3–6 righe.]

## Current State
[Stato attuale reale del lavoro.
Includi decisioni confermate, vincoli importanti,
ambiguità residue ed eventuali contraddizioni rilevate.]

## Confirmed Decisions
[Decisioni definitive, da non rimettere in discussione salvo comando esplicito.
Se assenti: "Nessuna decisione definitiva confermata in questa sessione."]

## Open Questions
[Punti ancora da decidere.
Se assenti: "Nessuna open question rilevata in questa sessione."]

## Files in Flight
[Per ciascun file o componente:
- Nome:
- Stato: bozza | parziale | completo | da rivedere | non determinato
- Contenuto:
- Da fare:
Se assenti: "Nessun file rilevato in questa sessione."]

## Changed
[Cosa è stato modificato, deciso o chiarito in questa sessione.
Se assente: "Nessuna modifica rilevante in questa sessione."]

## Failed Attempts
[Cosa non ha funzionato e perché.
Se assente: "Nessun tentativo fallito rilevante in questa sessione."]

## Next Step
[Una sola azione concreta, non ambigua, verificabile e prioritaria.]
```

---

## 8. Evidence Policy

```python
EVIDENCE_POLICY = [
    "Non inventare informazioni mancanti.",
    "Usare solo dati presenti nel comando o nella conversazione filtrata per scope.",
    "Dichiarare esplicitamente i dati non determinabili.",
    "Non risolvere contraddizioni arbitrariamente: riportarle.",
    "Separare nettamente dati confermati da ipotesi e punti aperti.",
]

EVIDENCE_LABELS = {
    "confirmed"  : "✓",  # dato esplicitamente confermato
    "hypothesis" : "~",  # ricavato per inferenza dal contesto
    "undecided"  : "?",  # ancora da decidere
}
```

---

## 9. Command Parsing

```python
FORCE_TOKENS = {"force", "--force", "-f", "forza", "--forza"}

SCOPE_MARKERS = ("scope:", "progetto:", "argomento:")

def parse_handoff_command(message: str) -> HandoffCommand | None:
    """
    Restituisce None se il primo token non è esattamente /handoff.
    """
    parts = message.strip().split(maxsplit=1)
    if not parts or parts[0].lower() != "/handoff":
        return None

    inline_text = parts[1].strip() if len(parts) > 1 else ""
    tokens = inline_text.lower().split()
    force = any(t in FORCE_TOKENS for t in tokens)
    inline_scope = _extract_inline_scope(inline_text)

    return HandoffCommand(raw=message, force=force,
                          inline_text=inline_text, inline_scope=inline_scope)
```

---

## 10. Scope Resolution and Context Filtering

Gli alias vengono inferiti dinamicamente dalla conversazione — non sono hardcoded.

Il sistema usa i termini tecnici, i nomi di file e i componenti citati nella chat per costruire il filtro di scope al momento della generazione. Non è necessario pre-configurare alias per ogni progetto.

Priorità risoluzione scope:
1. Scope esplicito nel comando → usa direttamente
2. Un solo candidato in chat → usa come inferito
3. Più candidati → chiedi chiarimento (o ⚠️ se force)

---

## 11. Next Step Validation

```python
WEAK_VERBS = {
    "continuare", "andare", "migliorare", "lavorare", "riprendere",
    "sistemare", "ottimizzare", "gestire", "occuparsi", "pensare", "valutare",
}

STRONG_VERBS = {
    "chiudere", "decidere", "scrivere", "aggiornare", "definire",
    "completare", "implementare", "correggere", "generare", "rivedere",
    "pubblicare", "creare", "rimuovere", "aggiungere", "testare",
    "rilasciare", "preparare", "validare", "confermare", "documentare",
    "revisionare", "finalizzare",
}

def is_valid_next_step(text: str) -> bool:
    return all([
        is_single_action(text),      # niente liste o separatori
        is_non_ambiguous(text),      # non inizia con verbo debole
        is_verifiable(text),         # contiene verbo forte o marker di completamento
    ])
```

---

## 12. Clarification Logic

- Campi critici mancanti → chiedi chiarimento (max 3 domande)
- Con `force` → genera comunque, segnala gap con ⚠️
- Max questions: 3, ordinate per priorità bloccante

---

## 13. Output Contract

L'output contiene esattamente tre elementi:
- `file` — contenuto del handoff.md
- `confirmation` — messaggio di conferma
- `warnings` — lista di ⚠️ (può essere vuota)

Nessun altra chiave. Nessun commento extra fuori dal template.

---

## 14. Edge Cases

| ID | Condizione | Azione |
|---|---|---|
| invalid_similar_trigger | Token simile ma non identico (es. /handoff123) | Non attivare |
| multiple_scopes | Più progetti in chat, scope non esplicito | Chiedi chiarimento (o ⚠️ force) |
| force_with_gaps | force + dati critici mancanti | Genera, segnala ogni gap con ⚠️ |
| inline_scope | Comando con "scope: X" | Usa scope inline con priorità assoluta |
| scope_alias_required | Messaggi pertinenti usano termini collegati, non scope esatto | Usa alias/keyword, non solo match esatto |
| incomplete_file_info | File citati ma dettagli insufficienti | Stato "non determinato" per campi mancanti |
| weak_next_step | Next step vago o non verificabile | Chiedi chiarimento (o ⚠️ force) |
| contradictions_detected | Informazioni contraddittorie nel contesto | Riporta in Current State, non risolvere |

---

## 15. Dove salvare il file

Salva `handoff.md` nella cartella radice del progetto a cui si riferisce lo scope.

Esempi:
- scope TradingBerry → cartella del progetto TradingBerry
- scope CRM → cartella del progetto CRM
- scope InkOS → cartella writer
- scope generico → directory di lavoro corrente

Se la cartella non è determinabile, salva nella directory corrente e avvisa.

---

## 16. Come usare il handoff nella sessione successiva

All'inizio di una nuova sessione, fornisci il file a Claude:

```
"Leggi handoff.md e riprendiamo da dove eravamo"
```

oppure aprilo nell'IDE prima di iniziare la chat — Claude lo leggerà automaticamente dal contesto IDE.

---

## Change Log

### v1.2
- Trigger ora deve essere esattamente `/handoff` (evita falsi positivi)
- Parser scope: token force rimossi dallo scope
- Filtro scope con alias e keyword collegate
- `FileInFlight` come modello dedicato
- Formattazione file corretta (no dizionari grezzi)
- Lista verbi forti estesa
- Validazione euristica next step migliorata
- Edge case aggiunti per trigger simili e alias di scope
- Aggiunta sezione "Dove salvare il file"
- Aggiunta sezione "Come usare nella sessione successiva"
- Alias dinamici inferiti dalla conversazione (non hardcoded)
