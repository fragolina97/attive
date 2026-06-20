---
name: skill-contradiction-analyzer
description: >-
  Analizza e confronta due skill AI per rilevare ogni contraddizione tra di loro.
  Usa quando: verificare se due skill sono compatibili, unire due skill in un agente,
  validare una nuova skill contro policy aziendali, due team hanno skill separate che
  devono coesistere. Comandi: /analizza (report completo) e /confronta (verdetto CI/CD).
  Rileva 15 categorie di contraddizioni. Score compatibilità 0-100.
compatibility: standalone
---

# Skill Contradiction Analyzer

Confrontra **due skill AI** e trova **ogni contraddizione**: punti in cui una skill dice di fare una cosa e l'altra l'opposto.

## Comandi

### `/analizza <skillA> <skillB>`
Analisi completa: carica, scompone in istruzioni atomiche, normalizza, confronta con 15 rilevatori in accumulation mode. Output: report strutturato con severity, impatto, suggerimento.

### `/confronta <skillA> <skillB>`
Verdetto rapido per CI/CD: numero contraddizioni, quante bloccanti, score compatibilità.

## Flusso Operativo

1. **Carica e Preprocessa** — rileva sorgente (file/URL/testo), formato, lingua; segmenta in istruzioni atomiche
2. **Estrai Entità** — 9 estrattori: regole deontiche, frasi passive, vincoli numerici, direttive, condizioni, sequenze, dipendenze, priorità, assunzioni
3. **Normalizza** — forma canonica: `[SOGGETTO] MODALITÀ [PREDICATO] [OGGETTO] [CONDIZIONI]`
4. **Rileva Contraddizioni** — ACCUMULATION MODE: tutti i 15 rilevatori su ogni coppia
5. **Assegna Scoring** — Severity 1-10, Confidence 0-1, Impact (BLOCKING→NEGLIGIBLE), Fix Difficulty
6. **Genera Report** — 3 livelli: Executive Summary → Tabella → Dettaglio completo

## I 15 Rilevatori

| # | Rilevatore | Cosa cerca |
|---|---|---|
| 1 | Opposizione Diretta | "Devi X" vs "Non devi X" |
| 2 | Mutua Esclusione | JSON vs solo XML |
| 3 | Conflitto Numerico | Range incompatibili |
| 4 | Conflitto Temporale | Ordine invertito |
| 5 | Conflitto Condizionale | Stessa condizione, azione opposta |
| 6 | Conflitto Priorità | Entrambe rivendicano supremazia |
| 7 | Opposizione Semantica | "conciso" vs "dettagliato" |
| 8 | Conflitto Scope | Globale vs eccezione locale |
| 9 | Conflitto Risorse | Lock esclusivo stessa risorsa |
| 10 | Conflitto Assunzioni | stateless vs stateful |
| 11 | Conflitto Side Effect | Effetto distrugge ciò che serve all'altra |
| 12 | Conflitto Compatibilità | Versioni incompatibili |
| 13 | Meta-Contraddizione | "ignora tutte le altre skill" |
| 14 | Contraddizione per Inferenza | Conflitto via catena logica |
| 15 | Conflitto Default | Default opposti |

## Note

- Read-only: non modifica mai le skill originali
- Italiano e inglese con rilevamento automatico
- Accumulation mode: non si ferma al primo conflitto
- Input sanitizzato contro prompt injection

*v2.0.0 — 2026*
