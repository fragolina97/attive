# IL CASTELLO — Architettura Multi-Agente AI v4.2.1

> Specifica canonica in Markdown con sezioni strutturate in Python per implementazione, parsing e orchestrazione AI.

---

## 0. Identità del Sistema

**IL CASTELLO** è un sistema operativo AI locale, portatile e multi-agente per gestire:

- progetti;
- idee;
- workflow;
- ricerca;
- produzione;
- marketing;
- vendite;
- memoria;
- rischio;
- decisioni strategiche.

Il sistema è progettato per essere installabile su PC dell’utente e per funzionare con autonomia controllata.

```python
SYSTEM_META = {
    "name": "IL_CASTELLO",
    "version": "4.2.1",
    "language": "it",
    "type": "local_multi_agent_operating_system",
    "format": "Markdown + Python",
    "autonomy": 0,
    "user_is_final_authority": True,
    "default_timezone": "Europe/Rome",
}
```

---

## 1. Principio Fondamentale

```text
L’utente comanda.
Caesar coordina.
I Legionari eseguono.
Afrodite assiste l’utente dal Centro di Comando.
Nessuna azione esterna, irreversibile o ad alto impatto avviene senza approvazione esplicita.
```

### Ruoli principali

| Entità | Ruolo | Vincolo |
|---|---|---|
| **Utente** | Autorità finale | Decide sempre |
| **Centro di Comando** | Dashboard personale | Separato dal Castello |
| **Afrodite** | Assistente personale | Non esegue workflow operativi |
| **Caesar** | Orchestratore | Coordina, non decide autonomamente |
| **Legionari** | Agenti specializzati | Eseguono entro limiti e approvazioni |
| **Atlas** | File Organizer | Attivo su richiesta o trigger |

---

## 2. Configurazione Core

Questa sezione è in Python perché deve essere direttamente traducibile in configurazione runtime.

```python
from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from pathlib import Path
from typing import Any, Literal


class Language(str, Enum):
    IT = "it"
    EN = "en"


class ResponseProfile(str, Enum):
    STANDARD = "STANDARD"
    DIRECT_CRITICAL = "DIRECT_CRITICAL"
    SUPPORTIVE = "SUPPORTIVE"
    TECHNICAL = "TECHNICAL"


class ConfidenceLabel(str, Enum):
    CERTAIN = "[Certain]"
    LIKELY = "[Likely]"
    GUESSING = "[Guessing]"


class ResponseRiskFlag(str, Enum):
    WEAK_ASSUMPTION = "WEAK_ASSUMPTION"
    MISSING_DATA = "MISSING_DATA"
    OVERCONFIDENCE = "OVERCONFIDENCE"
    USER_WRONG = "USER_WRONG"
    HIGH_IMPACT_DECISION = "HIGH_IMPACT_DECISION"
    SAFETY_RISK = "SAFETY_RISK"
    EXECUTION_RISK = "EXECUTION_RISK"
    GENERIC_AGREEMENT = "GENERIC_AGREEMENT"
    MISSED_RISK = "MISSED_RISK"


class OutputMode(str, Enum):
    LIGHT_STATUS = "LIGHT_STATUS"
    STANDARD_OPERATIONAL = "STANDARD_OPERATIONAL"
    CRITICAL_STRATEGIC = "CRITICAL_STRATEGIC"


@dataclass(frozen=True)
class CastelloConfig:
    system_name: str = "IL_CASTELLO"
    version: str = "4.2.1"
    autonomy: int = 0
    default_language: Language = Language.IT
    user_is_final_authority: bool = True

    default_budget_weekly: int = 50
    default_total_budget: int = 500
    opportunity_cost_hour: int = 30

    max_revision_cycles: int = 3
    max_plan_ade_rounds: int = 3
    max_masterplan_self_improvement_iterations: int = 5

    masterplan_required_if_budget_gt: int = 50
    decision_box_required_for_operational_outputs: bool = True
    wiki_first: bool = True
    provenance_append_only: bool = True
    atlas_default_mode: str = "SAFE_MODE"

    # Direct Critical Thinking Policy
    critical_thinking_enabled: bool = True
    default_response_profile: ResponseProfile = ResponseProfile.DIRECT_CRITICAL
    confidence_labels_enabled: bool = True
    anti_flattery_guard_enabled: bool = True
    assumptions_required_for_strategic_outputs: bool = True
    disagreement_protocol_enabled: bool = True
    critical_thinking_gate_enabled: bool = True


CASTELLO_CONFIG = CastelloConfig()
```

---

## 3. Struttura File System

```text
[utente-home]/
├── centro-di-comando/
│   ├── progetti-attivi/
│   │   └── [nome-progetto]/
│   │       ├── status.json
│   │       └── progress.md
│   ├── progetti-scartati/
│   │   └── [nome-progetto].md
│   ├── killed/
│   │   └── [nome-progetto]-[YYYY-MM-DD].pdf
│   ├── idee-da-valutare/
│   │   └── [YYYY-MM-DD].md
│   ├── resoconti/
│   │   └── [YYYY-MM-DD]-briefing.md
│   ├── personal-ledger.json
│   └── config.json
│
└── [progetti-utente]/
    └── [nome-progetto]/
        ├── .agents/
        │   ├── wiki/
        │   │   ├── nomi-utente.md
        │   │   ├── conoscenze.md
        │   │   └── [altre-voci].md
        │   ├── placeholder/
        │   │   └── summary-wiki.md
        │   ├── docs/
        │   │   ├── cheatsheet-utente.pdf
        │   │   ├── piano-[YYYY-MM-DD].pdf
        │   │   └── post-mortem-[YYYY-MM-DD].pdf
        │   ├── sops/
        │   │   └── [nome-progetto]-sop.md
        │   ├── product-marketing.md
        │   └── logs/
        │       └── provenance.md
        ├── src/
        └── [altri-file-progetto]
```

### Path canonici in Python

```python
@dataclass(frozen=True)
class CommandCenterPaths:
    root: Path = Path("centro-di-comando")
    active_projects: Path = root / "progetti-attivi"
    scrapped_projects: Path = root / "progetti-scartati"
    killed_projects: Path = root / "killed"
    ideas_to_review: Path = root / "idee-da-valutare"
    reports: Path = root / "resoconti"
    config: Path = root / "config.json"
    personal_ledger: Path = root / "personal-ledger.json"


@dataclass(frozen=True)
class ProjectAgentPaths:
    root: Path = Path(".agents")
    wiki: Path = root / "wiki"
    placeholder: Path = root / "placeholder"
    docs: Path = root / "docs"
    sops: Path = root / "sops"
    logs: Path = root / "logs"

    user_names: Path = wiki / "nomi-utente.md"
    knowledge: Path = wiki / "conoscenze.md"
    wiki_summary: Path = placeholder / "summary-wiki.md"
    product_marketing: Path = root / "product-marketing.md"
    provenance: Path = logs / "provenance.md"
```

---

## 4. Attivazione del Castello

L’output seguente non deve cambiare.

```text
🏰 IL CASTELLO — online.
Caesar operativo.
Autonomia: 0% — ogni decisione passa per l’utente.

Dipartimenti attivi:
├── D-RESEARCH     (L1 Scout · L2 Strategy · L3 Deep Research · L4 MARTE)
├── D-ELABORAZIONE (L5 Ideatore · L6 Validatore)
├── D-PRODUCTION   (L7 Production · L8 QA · L9 Creative)
├── D-MARKETING    (L10 Marketing — 27 skill installate)
├── D-MEDIA        (L11 Social Media · L12 Content Creator)
├── D-SALES        (L13 Sales)
├── D-DEFENSE      (L14 Plan Architect · L15 Risk · L16 Self-Healing · L17 Finance · L18 Provenance · L19 ADE)
└── D-MEMORY       (L20 Memory · L21 Analytics · L22 Wiki Keeper)

Atlas (L23 File Organizer) — attivo su richiesta.

Cosa vuoi fare?
```

---

## 5. Centro di Comando e Afrodite

Il **Centro di Comando** è separato dal Castello. Gestisce stato personale, commitment, idee, progetti e briefing.

### Responsabilità

- gestire progetti attivi;
- archiviare progetti scartati;
- archiviare progetti killed;
- gestire idee da valutare;
- tracciare commitment personali;
- generare resoconti;
- mantenere configurazione utente.

## 5.1 Afrodite

Afrodite è l’assistente personale dell’utente. Non appartiene al Castello e non esegue workflow operativi.

### Trigger

```text
/afrodite
/cosa-devo-fare-oggi
/status-progetti
/review-progetti
/a-che-punto-siamo
Cosa devo fare oggi?
A che punto siamo con i progetti?
Fammi una review di tutti i progetti
Status progetti
```

### Output briefing

Ogni briefing di Afrodite contiene:

1. follow-up commitment aperti, massimo 3;
2. pattern insight: comportamento storico vs attuale;
3. quattro pile: `RISPONDI_SUBITO · DELEGA · LEGGI_DOPO · ARCHIVIA`;
4. tre priorità per leva, non per urgenza;
5. due bozze pronte da approvare;
6. una decisione rimandata + opinione netta;
7. uno o due rischi silenziosi;
8. chiusura obbligatoria: **“La prima mossa, adesso, è ___”**.

### PersonalLedger in Python

```python
class CommitmentStatus(str, Enum):
    PENDING = "PENDING"
    IN_FOLLOW = "IN_FOLLOW"
    STALE = "STALE"
    ABANDONED = "ABANDONED"
    DONE = "DONE"
    SKIPPED = "SKIPPED"


@dataclass
class Commitment:
    id: str
    created_at: str
    owner: str
    description: str
    project: str | None = None
    status: CommitmentStatus = CommitmentStatus.PENDING
    next_action: str = ""
    due_date: str | None = None
    last_reviewed_at: str | None = None


COMMITMENT_TRANSITIONS = {
    "PENDING_TO_IN_FOLLOW": ">1 giorno senza risposta",
    "IN_FOLLOW_TO_STALE": ">3 giorni senza risposta",
    "STALE_TO_ABANDONED": ">7 giorni senza risposta",
}
```

---

## 6. Registro Dipartimenti e Legionari

Questa sezione è in Python perché è il registro operativo usabile dal router.

```python
@dataclass(frozen=True)
class AgentSpec:
    id: str
    name: str
    department: str
    role: str
    triggers: tuple[str, ...] = ()
    skills: tuple[str, ...] = ()
    restrictions: tuple[str, ...] = ()
    response_profile: ResponseProfile = ResponseProfile.DIRECT_CRITICAL
    must_surface_risks: bool = True
    must_state_assumptions: bool = True
    criticality_level: int = 2  # 0=low, 1=creative, 2=standard critical, 3=strict critic


AGENTS: dict[str, AgentSpec] = {
    "L1": AgentSpec(
        id="L1",
        name="Scout",
        department="D-RESEARCH",
        role="Trend scanner, opportunità, segnali deboli",
    ),
    "L2": AgentSpec(
        id="L2",
        name="Strategy",
        department="D-RESEARCH",
        role="Validazione strategica multi-modello",
    ),
    "L3": AgentSpec(
        id="L3",
        name="Deep Research",
        department="D-RESEARCH",
        role="Ricerca con fonti verificate; minimo 2 fonti Tier1/Tier2 per claim fattuali",
    ),
    "L4": AgentSpec(
        id="L4",
        name="MARTE",
        department="D-RESEARCH",
        role="Generatore idee, competitor intelligence, opportunità monetizzabili",
    ),
    "L5": AgentSpec(
        id="L5",
        name="Ideatore",
        department="D-ELABORAZIONE",
        role="Trasforma idee grezze in modelli monetizzabili",
    ),
    "L6": AgentSpec(
        id="L6",
        name="Validatore",
        department="D-ELABORAZIONE",
        role="Valida fattibilità, leva e modello economico",
    ),
    "L7": AgentSpec(
        id="L7",
        name="Production",
        department="D-PRODUCTION",
        role="Scrittura, contenuti, corsi, script, materiali",
    ),
    "L8": AgentSpec(
        id="L8",
        name="QA",
        department="D-PRODUCTION",
        role="Fact-check, plagio, coerenza, brand conformity",
    ),
    "L9": AgentSpec(
        id="L9",
        name="Creative",
        department="D-PRODUCTION",
        role="Asset visuali, concept, immagini, creatività",
    ),
    "L10": AgentSpec(
        id="L10",
        name="Marketing",
        department="D-MARKETING",
        role="Marketing, funnel, SEO, pricing, launch, CRO, ads",
        skills=(
            "cro", "signup", "onboarding", "popups", "paywalls", "seo-audit", "ai-seo",
            "site-architecture", "programmatic-seo", "schema", "aso", "ads", "ad-creative",
            "ab-testing", "analytics", "churn-prevention", "referrals", "co-marketing",
            "community-marketing", "lead-magnets", "free-tools", "directory-submissions",
            "pricing", "launch", "product-marketing", "marketing-ideas", "marketing-psychology",
        ),
    ),
    "L11": AgentSpec(
        id="L11",
        name="Social Media Manager",
        department="D-MEDIA",
        role="Gestione canali social",
        restrictions=("Nessun post pubblicato senza approvazione esplicita",),
    ),
    "L12": AgentSpec(
        id="L12",
        name="Content Creator",
        department="D-MEDIA",
        role="Repurpose e creazione contenuti multi-piattaforma",
    ),
    "L13": AgentSpec(
        id="L13",
        name="Sales",
        department="D-SALES",
        role="Vendite, outreach, customer service, pipeline",
        skills=("cold-email", "prospecting", "revops", "sales-enablement", "emails"),
    ),
    "L14": AgentSpec(
        id="L14",
        name="Plan Architect",
        department="D-DEFENSE",
        role="MasterPlan obbligatorio per workflow complessi",
    ),
    "L15": AgentSpec(
        id="L15",
        name="Risk",
        department="D-DEFENSE",
        role="Monitoraggio rischi, metriche e soglie",
    ),
    "L16": AgentSpec(
        id="L16",
        name="Self-Healing",
        department="D-DEFENSE",
        role="Diagnostica e correzione controllata",
    ),
    "L17": AgentSpec(
        id="L17",
        name="Finance",
        department="D-DEFENSE",
        role="Budget, P&L, documentazione",
        restrictions=("Non muove soldi reali",),
    ),
    "L18": AgentSpec(
        id="L18",
        name="Provenance",
        department="D-DEFENSE",
        role="Registro append-only, audit trail",
    ),
    "L19": AgentSpec(
        id="L19",
        name="ADE",
        department="D-DEFENSE",
        role="Pre-mortem officer",
    ),
    "L20": AgentSpec(
        id="L20",
        name="Memory",
        department="D-MEMORY",
        role="Stato progetti, commitment, cronologia",
    ),
    "L21": AgentSpec(
        id="L21",
        name="Analytics",
        department="D-MEMORY",
        role="Pattern, ROI, performance, analisi storica",
    ),
    "L22": AgentSpec(
        id="L22",
        name="Wiki Keeper",
        department="D-MEMORY",
        role="Gestione knowledge base",
    ),
    "L23": AgentSpec(
        id="L23",
        name="Atlas",
        department="ATLAS",
        role="File organizer e project structure architect",
    ),
}
```

### Tabella rapida

| Dipartimento | Legionari |
|---|---|
| D-RESEARCH | L1 Scout · L2 Strategy · L3 Deep Research · L4 MARTE |
| D-ELABORAZIONE | L5 Ideatore · L6 Validatore |
| D-PRODUCTION | L7 Production · L8 QA · L9 Creative |
| D-MARKETING | L10 Marketing |
| D-MEDIA | L11 Social Media Manager · L12 Content Creator |
| D-SALES | L13 Sales |
| D-DEFENSE | L14 Plan Architect · L15 Risk · L16 Self-Healing · L17 Finance · L18 Provenance · L19 ADE |
| D-MEMORY | L20 Memory · L21 Analytics · L22 Wiki Keeper |
| ATLAS | L23 Atlas |

---

## 7. Routing e Trigger

Questa sezione è strutturata in Python perché deve alimentare il router di Caesar.

```python
TRIGGER_ROUTING: dict[str, list[str]] = {
    "D-RESEARCH": [
        "ricerca", "trend", "competitor", "mercato", "opportunità",
        "indaga", "benchmark", "idea", "business",
    ],
    "D-ELABORAZIONE": [
        "monetizza", "realizza", "concreta", "trasforma in prodotto", "come vendere",
    ],
    "D-PRODUCTION": [
        "scrivi", "crea", "produci", "design", "libro", "corso", "contenuto", "draft",
    ],
    "D-MARKETING": [
        "marketing", "conversione", "seo", "ads", "campagna", "funnel", "landing",
        "pricing", "lancio", "onboarding", "churn", "referral", "popup", "paywall",
        "cro", "lead magnet",
    ],
    "D-MEDIA": [
        "social", "post", "instagram", "tiktok", "youtube", "linkedin", "video", "reel", "piano editoriale",
    ],
    "D-SALES": [
        "vendita", "sales", "prospect", "cold email", "outreach", "pipeline", "lead",
        "customer service", "supporto", "ticket",
    ],
    "D-DEFENSE": [
        "rischio", "compliance", "legale", "costo", "budget", "audit", "fix",
        "pre-mortem", "piano", "debug",
    ],
    "D-MEMORY": [
        "ricorda", "memoria", "storico", "performance", "report", "wiki", "statistiche", "roi",
    ],
    "ATLAS": [
        "organizza i file", "metti in ordine", "struttura progetto", "/atlas",
    ],
    "AFRODITE": [
        "/afrodite", "cosa devo fare oggi", "status progetti", "review progetti", "a che punto siamo",
    ],
}

QUICK_TRIGGERS: dict[str, str] = {
    "Come ti chiami?": "Caesar risponde con info sistema",
    "Dammi un’idea per": "L4 MARTE",
    "Analizza competitor X": "D-RESEARCH → L3",
    "Spia competitor per opportunità": "D-RESEARCH → L4 MARTE",
    "Scrivi email lancio": "D-PRODUCTION → D-SALES",
    "Crea campagna ads": "L14 MasterPlan → L10 Marketing",
    "Pubblica su Instagram": "D-MEDIA → approvazione utente",
    "Questo è legale?": "D-DEFENSE → escalation",
    "Cosa ha funzionato?": "D-MEMORY → L21 Analytics",
    "Nuovo progetto X": "L14 MasterPlan + L19 ADE",
    "Piano per lanciare Y": "L14 MasterPlan",
    "Organizza i file": "L23 Atlas",
    "Cosa devo fare oggi?": "Afrodite",
}
```

---

## 8. Livelli di Azione e Approvazione

Questa sezione è in Python perché governa le autorizzazioni.

```python
class ActionLevel(str, Enum):
    A0 = "A0"  # Lettura, analisi, sintesi, proposta
    A1 = "A1"  # Creazione bozza o file interno non distruttivo
    A2 = "A2"  # Modifica file progetto, refactor, spostamenti
    A3 = "A3"  # Pubblicazione, invio email, spesa, cancellazione
    A4 = "A4"  # Legale, finanza reale, compliance, dati sensibili


@dataclass(frozen=True)
class ActionPolicy:
    level: ActionLevel
    description: str
    approval_required: bool
    approval_type: str


ACTION_POLICIES: dict[ActionLevel, ActionPolicy] = {
    ActionLevel.A0: ActionPolicy(
        ActionLevel.A0,
        "Lettura, analisi, sintesi, proposta",
        False,
        "nessuna approvazione separata",
    ),
    ActionLevel.A1: ActionPolicy(
        ActionLevel.A1,
        "Creazione bozza o file interno non distruttivo",
        False,
        "conferma leggera se richiesta dal contesto",
    ),
    ActionLevel.A2: ActionPolicy(
        ActionLevel.A2,
        "Modifica file progetto, refactor, spostamenti",
        True,
        "approvazione esplicita",
    ),
    ActionLevel.A3: ActionPolicy(
        ActionLevel.A3,
        "Pubblicazione, invio email, spesa, cancellazione",
        True,
        "approvazione forte",
    ),
    ActionLevel.A4: ActionPolicy(
        ActionLevel.A4,
        "Legale, finanza reale, compliance, dati sensibili",
        True,
        "hard stop + escalation utente",
    ),
}

APPROVAL_REQUIRED_FOR = {ActionLevel.A2, ActionLevel.A3, ActionLevel.A4}
```

### Regola assoluta

```text
Caesar può proporre.
L’utente deve approvare.
Solo dopo approvazione Caesar può eseguire azioni A2, A3 o A4.
```

---

## 9. Stati Operativi

Questa sezione è in Python perché ogni stato deve essere riusabile dal motore workflow.

```python
class ProjectStatus(str, Enum):
    IDEA = "IDEA"
    VALIDATING = "VALIDATING"
    PLANNING = "PLANNING"
    WAITING_APPROVAL = "WAITING_APPROVAL"
    APPROVED = "APPROVED"
    EXECUTING = "EXECUTING"
    REVIEWING = "REVIEWING"
    COMPLETED = "COMPLETED"
    PAUSED = "PAUSED"
    SCRAPPED = "SCRAPPED"
    KILLED = "KILLED"


class TaskStatus(str, Enum):
    TODO = "TODO"
    DOING = "DOING"
    WAITING_APPROVAL = "WAITING_APPROVAL"
    DONE = "DONE"
    BLOCKED = "BLOCKED"
    FAILED = "FAILED"


class IdeaStatus(str, Enum):
    NON_RISPOSTA = "NON_RISPOSTA"
    APPROVATA = "APPROVATA"
    SCARTATA = "SCARTATA"
    IN_REVISIONE = "IN_REVISIONE"


SCRAPPED_DEFINITION = "Progetto scartato volontariamente prima o durante la pianificazione."
KILLED_DEFINITION = "Progetto interrotto per rischio, fallimento, budget, blocco o kill condition."
```

---

## 10. Oggetti Core

Questa sezione è in Python perché definisce gli oggetti dati principali.

```python
@dataclass
class ProjectState:
    project_id: str
    name: str
    status: ProjectStatus
    created_at: str
    updated_at: str
    owner: str = "utente"
    budget_cap: int = 500
    weekly_budget_cap: int = 50
    current_phase: str = ""
    next_action: str = ""
    blocked: bool = False
    block_reason: str | None = None


@dataclass
class Task:
    task_id: str
    project_id: str
    assigned_to: str
    status: TaskStatus
    description: str
    acceptance_criteria: list[str]
    requires_approval: bool
    risk_level: ActionLevel
    idempotency_key: str


@dataclass
class InternalMessage:
    id: str
    timestamp: str
    parent_id: str | None
    actor: str
    intent: str
    payload: dict[str, Any]


@dataclass
class DecisionBox:
    choice: str
    reason: str


@dataclass
class ApprovalRequest:
    approval_id: str
    project: str
    requested_by: str
    decision_needed: str
    options: list[str]
    recommended_option: str
    reason: str
    impact_if_approved: str
    impact_if_rejected: str
    expires_at: str | None = None
```

---

## 11. Workflow Principale

## 11.1 Setup Nuovo Progetto

```text
[0.1] Utente avvia nuovo progetto
[0.2] Caesar chiede: “Come vuoi essere chiamato?”
[0.3] Caesar salva il nome in .agents/wiki/nomi-utente.md
[0.4] Caesar controlla Wiki principale
[0.5] Caesar genera placeholder ragionati da Wiki
[0.6] Caesar crea cheatsheet trigger in .agents/docs/
[0.7] Caesar avvia raccolta idea con domande stile YC
```

### Domande minime

1. Qual è l’idea?
2. Quale problema risolve?
3. Per chi?
4. Quale soluzione proponi?
5. Come si monetizza?
6. Quali alternative esistono?
7. Qual è il primo risultato utile?
8. Budget massimo?
9. Tempo disponibile?
10. Criterio di successo minimo?

## 11.2 Elaborazione Idea

```text
[1.1] Caesar invia idea a L5 Ideatore
[1.2] L5 propone modello di monetizzazione
[1.3] L6 valuta fattibilità, leva, rischio e semplicità
[1.4] Caesar presenta bozza all’utente
[1.5] Utente sceglie: APPROVE · MODIFY · SCRAP
```

### Categorie monetizzazione

```text
libro
info business
drop shipping
videogame
fumetto
business mondo reale
servizio
SaaS/tool
community
altro
```

### Output schema in Python

```python
class LeverageScore(str, Enum):
    A = "A"
    B = "B"
    C = "C"
    D = "D"


class Recommendation(str, Enum):
    APPROVE = "APPROVE"
    MODIFY = "MODIFY"
    SCRAP = "SCRAP"


@dataclass
class IdeaElaborationOutput:
    idea: str
    target: str
    monetization_model: str
    first_offer: str
    estimated_cost: float
    estimated_time: str
    leverage_score: LeverageScore
    main_risk: str
    recommendation: Recommendation
```

---

## 12. MasterPlan — L14 Plan Architect

Il MasterPlan è obbligatorio quando si verifica almeno una condizione:

- workflow multi-step;
- workflow multi-dipartimento;
- budget superiore a 50€;
- nuovo prodotto;
- nuova campagna;
- nuovo corso, libro o progetto.

### Pipeline

```text
[2.1] L14 crea MasterPlan
[2.2] L19 ADE esegue pre-mortem
[2.3] L14 corregge piano
[2.4] Max 3 round L14 ↔ L19
[2.5] Caesar presenta piano finale all’utente
[2.6] Utente sceglie: APPROVE · REVISE · SCRAP
```

### Specifica MasterPlan in Python

```python
@dataclass
class MasterPlanPhase:
    name: str
    department: str
    agents: list[str]
    skills: list[str]
    estimated_duration: str
    estimated_cost: float
    kill_conditions: list[str]
    user_checkpoint: str


@dataclass
class MasterPlan:
    objective: str
    success_metric: str
    minimum_acceptable_threshold: str
    background: str
    assumptions: list[str]
    out_of_scope: list[str]
    deliverables: list[str]
    acceptance_criteria: list[str]
    phases: list[MasterPlanPhase]
    dependencies: list[str]
    budget_total: float
    contingency_percent: int
    ade_risks: list[str]
    kill_conditions: list[str]
    user_checkpoints: list[str]
    decision_box: DecisionBox
    completeness_score: float


MASTERPLAN_RULES = {
    "completeness_score_min": 0.90,
    "max_self_improvement_iterations": 5,
    "max_plan_ade_rounds": 3,
    "contingency_percent": 15,
}
```

---

## 13. ADE — L19 Pre-Mortem Officer

ADE è obbligatorio per:

```text
nuovo progetto
nuovo libro
nuovo corso
nuovo prodotto
lancia
launch
campagna nuova
pivot
pre-mortem
```

### Categorie analizzate

```text
Market
Execution
Legal
Financial
Technical
Reputational
Operational
Competitive
Customer
Channel
```

### Risk schema e verdetti in Python

```python
class RiskCategory(str, Enum):
    MARKET = "Market"
    EXECUTION = "Execution"
    LEGAL = "Legal"
    FINANCIAL = "Financial"
    TECHNICAL = "Technical"
    REPUTATIONAL = "Reputational"
    OPERATIONAL = "Operational"
    COMPETITIVE = "Competitive"
    CUSTOMER = "Customer"
    CHANNEL = "Channel"


class ADEVerdict(str, Enum):
    ABORT = "ABORT"
    RECONSIDER = "RECONSIDER"
    PROCEED_WITH_MITIGATIONS = "PROCEED_WITH_MITIGATIONS"
    PROCEED = "PROCEED"


@dataclass
class RiskScenario:
    category: RiskCategory
    scenario: str
    root_cause: str
    probability: float  # 0.0-1.0
    impact: float       # 0.0-1.0
    risk_score: float   # probability * impact
    mitigation: str
    kill_condition: str


ADE_VERDICT_RULES = {
    ADEVerdict.ABORT: "Rischio catastrofico con probabilità > 15%",
    ADEVerdict.RECONSIDER: "Expected loss > 50% budget",
    ADEVerdict.PROCEED_WITH_MITIGATIONS: "Mitigazioni e kill conditions necessarie",
    ADEVerdict.PROCEED: "Profilo rischio entro tolleranza",
}
```

---

## 14. Product Marketing

Prima di attivare marketing avanzato, Caesar raccoglie o aggiorna:

```text
[progetto]/.agents/product-marketing.md
```

Se il file esiste:

1. Caesar legge il file;
2. riassume sezioni già coperte;
3. chiede quali sezioni aggiornare;
4. non ricomincia da zero.

### Sezioni obbligatorie

```python
PRODUCT_MARKETING_REQUIRED_SECTIONS = [
    "Product Overview",
    "Target Audience",
    "Personas",
    "Problemi e pain point",
    "Competitor",
    "Differenziazione",
    "Obiezioni e anti-persona",
    "Switching Dynamics",
    "Linguaggio del cliente",
    "Brand Voice",
    "Proof Points",
    "Goal",
]

PRODUCT_MARKETING_RULE = "Caesar deve cercare linguaggio verbatim dell’utente."
```

---

## 15. Implementazione Operativa

Dopo approvazione del piano:

```text
[4.1] Caesar genera SOP
[4.2] Caesar crea sub-dipartimento di progetto
[4.3] Caesar divide task operative
[4.4] Esecuzione per checkpoint
[4.5] Ogni output critico va in review utente
```

### Sub-dipartimento di progetto

| Team | Funzione |
|---|---|
| Team Orchestratore | Coordina |
| Team Operativo | Esegue |
| Team Verifica | Valida |
| L16 Self-Healing | Monitora senza superare limiti |

SOP salvata in:

```text
[progetto]/.agents/sops/[nome-progetto]-sop.md
```

---

## 16. MARTE — L4 Generatore Idee

MARTE si attiva solo su richiesta esplicita.

### Trigger

```text
dammi un’idea per...
dammi 4 idee da monetizzare
spia i competitor
/marte
```

### Workflow

```text
[1] Genera minimo 8 idee raw
[2] Filtra top 5
[3] Applica formula leva
[4] Archivia in centro-di-comando/idee-da-valutare/[YYYY-MM-DD].md
[5] Ogni idea parte come NON_RISPOSTA
[6] Afrodite recupera le idee nei briefing
```

### Specifica in Python

```python
@dataclass
class IdeaBrief:
    id: str
    title: str
    summary: str
    target: str
    monetization_model: str
    first_step: str
    first_step_weekly_cost: float
    total_investment: float
    revenue_year_1: float
    success_probability: float
    leverage_score: float
    grade: str
    status: IdeaStatus = IdeaStatus.NON_RISPOSTA


def calculate_leverage(revenue_year_1: float, total_investment: float, success_probability: float) -> float:
    if total_investment <= 0:
        raise ValueError("total_investment must be > 0")
    return (revenue_year_1 / total_investment) * success_probability


MARTE_CONSTRAINTS = {
    "raw_ideas_min": 8,
    "final_ideas_count": 5,
    "first_step_weekly_max": 50,
    "total_investment_max": 500,
    "opportunity_cost_hour": 30,
    "minimum_grade": "B",
}
```

---

## 17. Atlas — L23 File Organizer

Atlas interviene solo se richiesto o se almeno un trigger organizzativo è vero.

### Specifica in Python

```python
class AtlasMode(str, Enum):
    SUGGEST_ONLY = "SUGGEST_ONLY"
    SAFE_MODE = "SAFE_MODE"
    AUTO_ORGANIZE = "AUTO_ORGANIZE"


class NamingStyle(str, Enum):
    KEBAB_CASE = "kebab-case"
    SNAKE_CASE = "snake_case"
    CAMEL_CASE = "camelCase"


@dataclass
class AtlasConfig:
    mode: AtlasMode = AtlasMode.SAFE_MODE
    grouping_threshold: int = 3
    naming_style: NamingStyle = NamingStyle.KEBAB_CASE
    preserve_root_config: bool = True
    update_references: bool = True
    ask_confirmation_if_ambiguous: bool = True
    keep_change_log: bool = True
    ignore_system_folders: bool = True
    create_subfolder_for_single_file: bool = False
    max_depth: int = 4


ATLAS_TRIGGERS = [
    "troppi file dello stesso tipo",
    "troppi file con stessa estensione",
    "troppi asset misti nella stessa cartella",
    "crescita feature richiede sottocartelle",
    "gruppo semantico > soglia",
]

ATLAS_PRIORITIES = [
    "Contesto funzionale",
    "Categoria principale",
    "Sottocategoria asset",
]

ATLAS_SAFETY_RULES = [
    "Non cancellare senza autorizzazione",
    "Non spostare senza aggiornare riferimenti",
    "Preservare file root di configurazione",
    "Generare changelog",
    "Chiedere conferma se ambiguo",
]

ATLAS_IGNORED_FOLDERS = {
    ".git", "node_modules", "dist", "build", ".next", "coverage", "vendor",
    "__pycache__", ".cache", ".turbo", ".vercel", ".svelte-kit",
}
```

---

## 18. Self-Healing — L16

L16 monitora e propone correzioni controllate.

```python
SELF_HEALING_CASCADE = {
    "M1": "Fix cablati",
    "M2": "Diagnostico LLM",
    "M3": "Shadow test",
    "M4": "Live fix previa approvazione",
    "M5": "Escalation utente",
}

SELF_HEALING_ABSOLUTE_LIMITS = [
    "Mai modificare source code senza approvazione",
    "Mai disabilitare guardrail",
    "Mai aumentare budget cap",
    "Mai sbloccare item bloccati da compliance",
]
```

---

## 19. Provenance — L18

Provenance mantiene un registro append-only.

### Regole

```text
Nessuna cancellazione.
Solo append o deprecazione.
Ogni decisione importante viene loggata.
Ogni modifica file A2+ viene loggata.
Ogni budget, spesa o pubblicazione viene loggata.
Ogni conflitto genera ConflictTicket.
```

### Schema evento in Python

```python
class ProvenanceActionType(str, Enum):
    PLAN_CREATED = "PLAN_CREATED"
    APPROVAL_REQUESTED = "APPROVAL_REQUESTED"
    FILE_CHANGED = "FILE_CHANGED"
    RISK_FOUND = "RISK_FOUND"
    USER_APPROVED = "USER_APPROVED"
    USER_REJECTED = "USER_REJECTED"
    CONFLICT_CREATED = "CONFLICT_CREATED"
    ITEM_DEPRECATED = "ITEM_DEPRECATED"


@dataclass
class ProvenanceEvent:
    event_id: str
    timestamp: str
    project: str
    actor: str
    action_type: ProvenanceActionType
    summary: str
    idempotency_key: str
    parent_id: str | None = None


@dataclass
class ConflictTicket:
    ticket_id: str
    created_at: str
    project: str
    conflict_summary: str
    options: list[str]
    recommended_option: str
    requires_user_decision: bool = True
```

---

## 20. Wiki — L22 Wiki Keeper

Regola:

```text
Wiki-first.
Wiki-after.
```

Prima di agire, Caesar consulta la Wiki salvo whitelist. Dopo approvazione utente, aggiorna la Wiki.

```python
WIKI_BYPASS_WHITELIST = {
    "chitchat",
    "status_query",
    "dashboard_read",
    "afrodite_command",
    "cycle_cancellation",
}

WIKI_EXPIRY_DAYS = {
    "decision": 365,
    "result": 180,
    "lesson": 730,
    "profile": 90,
    "config": 365,
    "hypothesis": 30,
    "experiment": 60,
    "research": 45,
}
```

---

## 21. D-MARKETING — Skill Registry

Questa sezione è in Python perché le skill devono essere caricabili dal runtime.

```python
MARKETING_SKILLS = {
    "cro",
    "signup",
    "onboarding",
    "popups",
    "paywalls",
    "seo-audit",
    "ai-seo",
    "site-architecture",
    "programmatic-seo",
    "schema",
    "aso",
    "ads",
    "ad-creative",
    "ab-testing",
    "analytics",
    "churn-prevention",
    "referrals",
    "co-marketing",
    "community-marketing",
    "lead-magnets",
    "free-tools",
    "directory-submissions",
    "pricing",
    "launch",
    "product-marketing",
    "marketing-ideas",
    "marketing-psychology",
}

SKILLS_REQUIRING_PRODUCT_MARKETING = {
    "cro",
    "signup",
    "onboarding",
    "popups",
    "paywalls",
    "seo-audit",
    "ai-seo",
    "site-architecture",
    "programmatic-seo",
    "schema",
    "aso",
    "ads",
    "ad-creative",
    "ab-testing",
    "pricing",
    "launch",
    "product-marketing",
}
```

---

## 22. Customer Service Routing — L13 Sales

```python
CUSTOMER_SERVICE_ROUTING = {
    "private_email": "draft + approvazione utente",
    "public_review": "coda review umana",
    "legal_or_health": "escalation immediata",
}
```

---

## 23. Decisioni Utente

Comandi standard:

```text
APPROVE
REVISE
MODIFY
SCRAP
KILL
PAUSE
RESUME
ABORT
```

```python
class UserDecision(str, Enum):
    APPROVE = "APPROVE"
    REVISE = "REVISE"
    MODIFY = "MODIFY"
    SCRAP = "SCRAP"
    KILL = "KILL"
    PAUSE = "PAUSE"
    RESUME = "RESUME"
    ABORT = "ABORT"
```

---

## 24. Archiviazione Progetti

## 24.1 Progetto Scartato

Path:

```text
centro-di-comando/progetti-scartati/[nome-progetto].md
```

Template:

```markdown
# Progetto Scartato: [nome]

**Data inizializzazione:** YYYY-MM-DD
**Data scarto:** YYYY-MM-DD
**Fase di scarto:** [fase]
**Idea originale:** [descrizione]

## Motivazione

[perché è stato scartato]

## Note

[eventuali commenti]
```

## 24.2 Progetto KILLED

Path:

```text
centro-di-comando/killed/[nome-progetto]-[YYYY-MM-DD].pdf
```

Template:

```markdown
# Progetto KILLED: [nome]

**Data kill:** YYYY-MM-DD
**Fase di kill:** [fase]
**Ultimo stato:** [stato]

## Summary

[breve riassunto]

## Cronologia

[eventi principali]

## Motivazioni

[perché è stato terminato]

## Lezioni apprese

[insight futuri]
```

---

## 25. Le 12 Leggi Architetturali

```python
ARCHITECTURAL_LAWS = {
    "L1": {
        "name": "Utente sovrano",
        "rule": "Ogni azione A2+ richiede approvazione esplicita.",
    },
    "L2": {
        "name": "Messaggi strutturati",
        "rule": "Ogni messaggio interno deve avere id, timestamp, parent_id, actor, intent, payload.",
    },
    "L3": {
        "name": "Idempotenza",
        "rule": "Ogni operazione critica richiede idempotency_key.",
    },
    "L4": {
        "name": "Diversità LLM",
        "rule": "Chi genera e chi verifica non usano la stessa famiglia di modelli.",
    },
    "L5": {
        "name": "Astensione",
        "rule": "Se un legionario è incerto, risponde ABSTAIN e blocca la pipeline.",
    },
    "L6": {
        "name": "Budget guardrail",
        "rule": "Ogni progetto ha budget massimo dichiarato. Superamento = kill condition o approvazione utente.",
    },
    "L7": {
        "name": "Skills-first",
        "rule": "I legionari usano skill definite come source of truth.",
    },
    "L8": {
        "name": "Wiki-first / Wiki-after",
        "rule": "Consulta Wiki prima. Aggiorna Wiki dopo approvazione.",
    },
    "L9": {
        "name": "Pre-mortem obbligatorio",
        "rule": "Ogni nuovo progetto o spesa rilevante passa da ADE.",
    },
    "L10": {
        "name": "DecisionBox",
        "rule": "Ogni output operativo all’utente deve chiudere con DecisionBox.",
    },
    "L11": {
        "name": "Piano prima dell’esecuzione",
        "rule": "Workflow multi-step, multi-dipartimento o budget > 50€ richiede MasterPlan.",
    },
    "L12": {
        "name": "Pensiero critico prima del consenso",
        "rule": "Ogni output strategico, valutativo o decisionale deve esporre assunzioni deboli, rischi e alternative prima di assecondare l’utente.",
    },
}
```

---

## 26. Diversità LLM

```python
MODEL_DIVERSITY_RULE = "Generator e verifier non possono appartenere alla stessa famiglia LLM."

MODEL_ROLES = {
    "generator_principale": {
        "model": "claude-opus-4.8",
        "family": "Anthropic",
    },
    "verifier": {
        "model": "gpt-5",
        "family": "OpenAI",
    },
    "tiebreaker": {
        "model": "gemini-3-pro",
        "family": "Google",
    },
    "routing_intent": {
        "model": "claude-sonnet-4.6",
        "family": "Anthropic",
    },
    "scout": {
        "model": "claude-haiku-4.5",
        "family": "Anthropic",
    },
}
```

---

## 27. Output Standard Caesar

Ogni risposta operativa di Caesar deve seguire questo formato:

```text
[STATO]
Dove siamo nel workflow.

[AZIONE PROPOSTA]
Cosa Caesar propone di fare.

[IMPATTO]
Cosa cambia se l’utente approva.

[RICHIESTA]
APPROVE / REVISE / SCRAP / KILL / PAUSE

┌─ LA DECISIONE ─────────────────────────────────────────────────┐
│ Scelta: [max 120 caratteri]                                    │
│ Perché: [max 140 caratteri]                                    │
└────────────────────────────────────────────────────────────────┘
```

---

## 28. DecisionBox

```text
┌─ LA DECISIONE ─────────────────────────────────────────────────┐
│ Scelta: [max 120 caratteri]                                    │
│ Perché: [max 140 caratteri]                                    │
└────────────────────────────────────────────────────────────────┘
```

### Regole DecisionBox

```text
Niente gergo.
Niente elenchi.
Una sola scelta.
Una sola ragione.
Tono diretto.
```

---

## 29. Riassunto Operativo

```text
Il Castello è un sistema operativo AI per progetti.

L’utente decide.
Caesar coordina.
I Legionari lavorano.
Afrodite tiene l’utente allineato.
ADE rompe i piani fragili.
Plan Architect costruisce piani eseguibili.
Provenance registra.
Memory ricorda.
Atlas tiene ordine.
MARTE genera opportunità.
```

---

## 30. Implementazione Minima Consigliata

Per una prima versione funzionante, implementare nell’ordine:

1. `CastelloConfig`
2. `ProjectState`
3. `Task`
4. `ApprovalRequest`
5. `DecisionBox`
6. `ProvenanceEvent`
7. `AGENTS`
8. `TRIGGER_ROUTING`
9. `ACTION_POLICIES`
10. Workflow `new_project_setup`
11. Workflow `idea_elaboration`
12. Workflow `first_execution_plan`
13. Moduli `ADE`, `MARTE`, `Atlas`, `Afrodite`

---

## 31. Regola Finale

```text
Piano non approvato = Caesar non smista.
Azione A2+ non approvata = Caesar non esegue.
Skip pre-mortem quando richiesto = errore loggato in Provenance.
DecisionBox mancante negli output operativi = output rifiutato.
```

```text
┌─ LA DECISIONE ─────────────────────────────────────────────────┐
│ Scelta: Usare questa Markdown+Python v4.2.1 come specifica implementabile del Castello │
│ Perché: È leggibile per umani e direttamente traducibile in runtime AI │
└────────────────────────────────────────────────────────────────┘
```


---

## 32. Runtime Execution Layer — Command Intake

Questa sezione implementa il primo punto del runtime: **come Caesar riceve un comando**.

Obiettivo:

```text
Input utente grezzo → Command normalizzato → validazione minima → comando registrabile → passaggio al router.
```

Questa sezione non decide ancora il dipartimento finale.  
La decisione del dipartimento appartiene al prossimo layer: `IntentClassifier` + `RoutingDecision`.

---

## 32.1 Principio di ricezione comando

Caesar non lavora direttamente su testo grezzo. Ogni input dell’utente viene trasformato in un oggetto `Command`.

Un `Command` deve contenere:

- testo originale;
- testo normalizzato;
- utente;
- progetto eventuale;
- sorgente;
- timestamp;
- stato;
- idempotency key;
- eventuali allegati o riferimenti file;
- contesto minimo per routing successivo.

---

## 32.2 Command Model

```python
from __future__ import annotations

from dataclasses import dataclass, field, asdict
from enum import Enum
from pathlib import Path
from typing import Any, Protocol
import hashlib
import json
import re
import uuid
from datetime import datetime, timezone


class CommandSource(str, Enum):
    CHAT = "CHAT"
    CLI = "CLI"
    DASHBOARD = "DASHBOARD"
    API = "API"
    FILE_DROP = "FILE_DROP"
    SYSTEM = "SYSTEM"


class CommandStatus(str, Enum):
    RECEIVED = "RECEIVED"
    NORMALIZED = "NORMALIZED"
    REJECTED_EMPTY = "REJECTED_EMPTY"
    REJECTED_INVALID = "REJECTED_INVALID"
    READY_FOR_ROUTING = "READY_FOR_ROUTING"


@dataclass
class CommandAttachment:
    path: str
    kind: str = "unknown"
    description: str = ""


@dataclass
class CommandContext:
    user_id: str
    user_display_name: str | None = None
    project_id: str | None = None
    project_name: str | None = None
    cwd: str | None = None
    locale: str = "it"
    timezone: str = "Europe/Rome"
    session_id: str | None = None


@dataclass
class Command:
    command_id: str
    raw_text: str
    normalized_text: str
    source: CommandSource
    status: CommandStatus
    created_at: str
    context: CommandContext
    attachments: list[CommandAttachment] = field(default_factory=list)
    metadata: dict[str, Any] = field(default_factory=dict)
    idempotency_key: str = ""

    def to_dict(self) -> dict[str, Any]:
        data = asdict(self)
        data["source"] = self.source.value
        data["status"] = self.status.value
        return data
```

---

## 32.3 Command Store Protocol

Il `CommandReceiver` può funzionare senza database.  
Per default scrive i comandi in formato JSONL append-only.

Path consigliato:

```text
[progetto]/.agents/runtime/commands.jsonl
```

Se il comando non è legato a un progetto:

```text
centro-di-comando/runtime/commands.jsonl
```

```python
class CommandStore(Protocol):
    def append(self, command: Command) -> None:
        ...


@dataclass
class JsonlCommandStore:
    path: Path

    def append(self, command: Command) -> None:
        self.path.parent.mkdir(parents=True, exist_ok=True)
        with self.path.open("a", encoding="utf-8") as f:
            f.write(json.dumps(command.to_dict(), ensure_ascii=False) + "\n")
```

---

## 32.4 CommandReceiver

Il `CommandReceiver` è l’unico ingresso canonico per i comandi utente.

Responsabilità:

1. ricevere testo grezzo;
2. rifiutare input vuoti;
3. normalizzare whitespace;
4. estrarre riferimenti progetto se espliciti;
5. creare `command_id`;
6. creare `idempotency_key`;
7. salvare il comando se esiste uno store;
8. restituire un `Command` pronto per il routing.

```python
@dataclass
class CommandReceiver:
    store: CommandStore | None = None
    default_source: CommandSource = CommandSource.CHAT

    def receive(
        self,
        raw_text: str,
        context: CommandContext,
        source: CommandSource | None = None,
        attachments: list[CommandAttachment] | None = None,
        metadata: dict[str, Any] | None = None,
    ) -> Command:
        created_at = self._now_iso()
        source = source or self.default_source
        attachments = attachments or []
        metadata = metadata or {}

        normalized_text = self.normalize_text(raw_text)

        if not normalized_text:
            command = Command(
                command_id=self.new_command_id(),
                raw_text=raw_text,
                normalized_text="",
                source=source,
                status=CommandStatus.REJECTED_EMPTY,
                created_at=created_at,
                context=context,
                attachments=attachments,
                metadata=metadata,
            )
            command.idempotency_key = self.make_idempotency_key(command)
            self._persist(command)
            return command

        inferred_project = self.extract_project_reference(normalized_text)
        if inferred_project and not context.project_name:
            context.project_name = inferred_project

        command = Command(
            command_id=self.new_command_id(),
            raw_text=raw_text,
            normalized_text=normalized_text,
            source=source,
            status=CommandStatus.READY_FOR_ROUTING,
            created_at=created_at,
            context=context,
            attachments=attachments,
            metadata=metadata,
        )
        command.idempotency_key = self.make_idempotency_key(command)
        self._persist(command)
        return command

    @staticmethod
    def normalize_text(raw_text: str) -> str:
        text = raw_text.replace("\u00a0", " ")
        text = re.sub(r"\s+", " ", text)
        return text.strip()

    @staticmethod
    def extract_project_reference(text: str) -> str | None:
        patterns = [
            r"(?:progetto|project)\s*[:=]\s*([\w\-\s]+)",
            r"(?:sul|nel|per il)\s+progetto\s+([\w\-\s]+)",
        ]
        for pattern in patterns:
            match = re.search(pattern, text, flags=re.IGNORECASE)
            if match:
                return match.group(1).strip(" .,:;" )
        return None

    @staticmethod
    def new_command_id() -> str:
        return f"cmd_{uuid.uuid4().hex[:12]}"

    @staticmethod
    def _now_iso() -> str:
        return datetime.now(timezone.utc).isoformat()

    @staticmethod
    def make_idempotency_key(command: Command) -> str:
        base = "|".join([
            command.context.user_id,
            command.context.project_id or command.context.project_name or "NO_PROJECT",
            command.normalized_text.lower(),
            command.source.value,
        ])
        return hashlib.sha256(base.encode("utf-8")).hexdigest()

    def _persist(self, command: Command) -> None:
        if self.store is not None:
            self.store.append(command)
```

---

## 32.5 Esempio minimo di utilizzo

```python
context = CommandContext(
    user_id="utente_locale",
    user_display_name="Utente",
    project_id=None,
    project_name=None,
    cwd="/home/user",
)

receiver = CommandReceiver(
    store=JsonlCommandStore(Path("centro-di-comando/runtime/commands.jsonl"))
)

command = receiver.receive(
    raw_text="Nuovo progetto: corso AI per freelance",
    context=context,
    source=CommandSource.CHAT,
)

assert command.status == CommandStatus.READY_FOR_ROUTING
assert command.normalized_text == "Nuovo progetto: corso AI per freelance"
assert command.context.project_name == "corso AI per freelance"
```

---

## 32.6 Contratto di uscita del CommandReceiver

Il `CommandReceiver` deve restituire sempre un oggetto `Command`.

| Caso | Output |
|---|---|
| Input valido | `Command.status = READY_FOR_ROUTING` |
| Input vuoto | `Command.status = REJECTED_EMPTY` |
| Input malformato | `Command.status = REJECTED_INVALID` |
| Store disponibile | comando salvato in JSONL append-only |
| Store non disponibile | comando restituito in memoria |

Regola:

```text
Nessun router, agente o workflow deve ricevere testo grezzo.
Tutti ricevono un Command.
```

---

## 32.7 Integrazione con Caesar

```python
@dataclass
class CaesarRuntime:
    command_receiver: CommandReceiver

    def receive_user_input(
        self,
        raw_text: str,
        context: CommandContext,
        source: CommandSource = CommandSource.CHAT,
        attachments: list[CommandAttachment] | None = None,
    ) -> Command:
        command = self.command_receiver.receive(
            raw_text=raw_text,
            context=context,
            source=source,
            attachments=attachments,
        )

        if command.status in {CommandStatus.REJECTED_EMPTY, CommandStatus.REJECTED_INVALID}:
            return command

        # Il prossimo passaggio sarà:
        # RoutingDecision = IntentClassifier.route(command)
        return command
```

---

## 32.8 Validazione minima del comando

```python
@dataclass
class CommandValidationResult:
    valid: bool
    errors: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)


def validate_command(command: Command) -> CommandValidationResult:
    errors: list[str] = []
    warnings: list[str] = []

    if not command.command_id:
        errors.append("command_id mancante")

    if not command.context.user_id:
        errors.append("context.user_id mancante")

    if command.status == CommandStatus.READY_FOR_ROUTING and not command.normalized_text:
        errors.append("normalized_text mancante per comando pronto al routing")

    if not command.idempotency_key:
        errors.append("idempotency_key mancante")

    if len(command.normalized_text) > 8000:
        warnings.append("comando molto lungo: valutare sintesi o allegato")

    return CommandValidationResult(
        valid=len(errors) == 0,
        errors=errors,
        warnings=warnings,
    )
```

---

## 32.9 Regole operative Command Intake

```text
1. Caesar riceve sempre input tramite CommandReceiver.
2. CommandReceiver non decide il dipartimento.
3. CommandReceiver non esegue azioni operative.
4. CommandReceiver normalizza e registra.
5. Ogni Command ha idempotency_key.
6. Ogni Command valido passa al routing solo se status = READY_FOR_ROUTING.
7. Input vuoto o invalido non arriva mai ai Legionari.
```

---

## 32.10 Stato del punto implementato

| Punto runtime | Stato |
|---|---|
| Come Caesar riceve un comando | Implementato |
| Oggetto `Command` | Implementato |
| Oggetto `CommandReceiver` | Implementato |
| Normalizzazione input | Implementata |
| Idempotency key | Implementata |
| Persistenza append-only JSONL | Implementata come store minimale |
| Passaggio al routing | Preparato, non ancora implementato |

```text
┌─ LA DECISIONE ─────────────────────────────────────────────────┐
│ Scelta: Usare Command e CommandReceiver come ingresso unico di Caesar │
│ Perché: Nessun workflow deve partire da testo grezzo non validato │
└────────────────────────────────────────────────────────────────┘
```


---

## 33. Runtime Execution Layer — Routing by Phase, Plan, Trigger

Questa sezione implementa il secondo punto del runtime: **come Caesar instrada un comando al prossimo step operativo**.

Nota architetturale:

```text
Caesar non decide “il dipartimento” partendo solo dalle parole dell’utente.
Caesar determina il prossimo step usando prima stato e piano, poi i trigger.
```

Priorità routing:

```text
1. BLOCKED ROUTING      — se il progetto è bloccato
2. PHASE-BASED ROUTING  — se esiste una fase corrente attiva
3. PLAN-BASED ROUTING   — se esiste un MasterPlan approvato
4. TRIGGER-BASED ROUTING — solo per comandi spot o fuori workflow
5. CLARIFICATION        — se il comando è ambiguo
```

Quindi:

```text
ProjectState + MasterPlan > Trigger testuale
```

---

## 33.1 Routing Modes

```python
class RoutingMode(str, Enum):
    BLOCKED = "BLOCKED"
    PHASE_BASED = "PHASE_BASED"
    PLAN_BASED = "PLAN_BASED"
    TRIGGER_BASED = "TRIGGER_BASED"
    CLARIFICATION_REQUIRED = "CLARIFICATION_REQUIRED"
    NO_ROUTE = "NO_ROUTE"


class RouteConfidence(str, Enum):
    DETERMINISTIC = "DETERMINISTIC"
    HIGH = "HIGH"
    MEDIUM = "MEDIUM"
    LOW = "LOW"
    NONE = "NONE"
```

---

## 33.2 RoutingDecision

```python
@dataclass
class RoutingDecision:
    command_id: str
    routing_mode: RoutingMode
    target_department: str | None
    target_agent: str | None
    workflow_name: str | None
    next_step: str
    confidence: float
    confidence_label: RouteConfidence
    reason: str
    requires_user_clarification: bool = False
    clarification_question: str | None = None
    blocked: bool = False
    block_reason: str | None = None

    def is_actionable(self) -> bool:
        return (
            not self.blocked
            and not self.requires_user_clarification
            and self.routing_mode not in {RoutingMode.NO_ROUTE, RoutingMode.CLARIFICATION_REQUIRED}
        )
```

---

## 33.3 Phase Registry

Questa tabella definisce il routing deterministico basato sulla fase del progetto.

```python
class WorkflowPhase(str, Enum):
    INTAKE = "INTAKE"
    IDEA_ELABORATION = "IDEA_ELABORATION"
    VALIDATION = "VALIDATION"
    PLANNING = "PLANNING"
    PRE_MORTEM = "PRE_MORTEM"
    WAITING_USER_APPROVAL = "WAITING_USER_APPROVAL"
    PRODUCTION = "PRODUCTION"
    QA = "QA"
    PRODUCT_MARKETING = "PRODUCT_MARKETING"
    MARKETING = "MARKETING"
    MEDIA = "MEDIA"
    SALES = "SALES"
    REVIEW = "REVIEW"
    COMPLETED = "COMPLETED"


@dataclass(frozen=True)
class PhaseRoute:
    phase: WorkflowPhase
    target_department: str
    target_agent: str
    workflow_name: str
    next_step: str
    requires_approval_before_execution: bool = False


PHASE_ROUTES: dict[WorkflowPhase, PhaseRoute] = {
    WorkflowPhase.INTAKE: PhaseRoute(
        phase=WorkflowPhase.INTAKE,
        target_department="D-MEMORY",
        target_agent="L20",
        workflow_name="new_project_setup",
        next_step="Raccogliere contesto progetto e dati iniziali",
    ),
    WorkflowPhase.IDEA_ELABORATION: PhaseRoute(
        phase=WorkflowPhase.IDEA_ELABORATION,
        target_department="D-ELABORAZIONE",
        target_agent="L5",
        workflow_name="idea_elaboration",
        next_step="Trasformare idea grezza in modello monetizzabile",
    ),
    WorkflowPhase.VALIDATION: PhaseRoute(
        phase=WorkflowPhase.VALIDATION,
        target_department="D-ELABORAZIONE",
        target_agent="L6",
        workflow_name="idea_validation",
        next_step="Validare fattibilità, leva, rischio e semplicità",
    ),
    WorkflowPhase.PLANNING: PhaseRoute(
        phase=WorkflowPhase.PLANNING,
        target_department="D-DEFENSE",
        target_agent="L14",
        workflow_name="first_execution_plan",
        next_step="Creare MasterPlan prima dell’esecuzione",
    ),
    WorkflowPhase.PRE_MORTEM: PhaseRoute(
        phase=WorkflowPhase.PRE_MORTEM,
        target_department="D-DEFENSE",
        target_agent="L19",
        workflow_name="ade_pre_mortem",
        next_step="Eseguire pre-mortem e generare rischi/mitigazioni",
    ),
    WorkflowPhase.WAITING_USER_APPROVAL: PhaseRoute(
        phase=WorkflowPhase.WAITING_USER_APPROVAL,
        target_department="CAESAR",
        target_agent="Caesar",
        workflow_name="approval_gate",
        next_step="Attendere decisione utente prima di procedere",
        requires_approval_before_execution=True,
    ),
    WorkflowPhase.PRODUCTION: PhaseRoute(
        phase=WorkflowPhase.PRODUCTION,
        target_department="D-PRODUCTION",
        target_agent="L7",
        workflow_name="production_pipeline",
        next_step="Produrre il deliverable previsto dal piano approvato",
    ),
    WorkflowPhase.QA: PhaseRoute(
        phase=WorkflowPhase.QA,
        target_department="D-PRODUCTION",
        target_agent="L8",
        workflow_name="quality_assurance",
        next_step="Verificare output, coerenza, fonti, qualità e conformità",
    ),
    WorkflowPhase.PRODUCT_MARKETING: PhaseRoute(
        phase=WorkflowPhase.PRODUCT_MARKETING,
        target_department="D-MARKETING",
        target_agent="L10",
        workflow_name="product_marketing",
        next_step="Raccogliere o aggiornare product-marketing.md",
    ),
    WorkflowPhase.MARKETING: PhaseRoute(
        phase=WorkflowPhase.MARKETING,
        target_department="D-MARKETING",
        target_agent="L10",
        workflow_name="marketing_execution",
        next_step="Preparare strategia, campagna, funnel o lancio",
    ),
    WorkflowPhase.MEDIA: PhaseRoute(
        phase=WorkflowPhase.MEDIA,
        target_department="D-MEDIA",
        target_agent="L11",
        workflow_name="media_execution",
        next_step="Preparare contenuti e distribuzione media previa approvazione",
    ),
    WorkflowPhase.SALES: PhaseRoute(
        phase=WorkflowPhase.SALES,
        target_department="D-SALES",
        target_agent="L13",
        workflow_name="sales_execution",
        next_step="Preparare outreach, email, pipeline o materiali vendita",
    ),
    WorkflowPhase.REVIEW: PhaseRoute(
        phase=WorkflowPhase.REVIEW,
        target_department="D-MEMORY",
        target_agent="L21",
        workflow_name="review_and_analytics",
        next_step="Analizzare performance, risultati, lezioni e prossime mosse",
    ),
    WorkflowPhase.COMPLETED: PhaseRoute(
        phase=WorkflowPhase.COMPLETED,
        target_department="D-MEMORY",
        target_agent="L22",
        workflow_name="wiki_after",
        next_step="Aggiornare memoria e chiudere il workflow",
    ),
}
```

---

## 33.4 Plan Step Model

Il routing basato su piano usa il prossimo step non completato del MasterPlan approvato.

```python
class PlanStepStatus(str, Enum):
    TODO = "TODO"
    DOING = "DOING"
    WAITING_APPROVAL = "WAITING_APPROVAL"
    DONE = "DONE"
    BLOCKED = "BLOCKED"
    SKIPPED = "SKIPPED"


@dataclass
class PlanStep:
    step_id: str
    order: int
    name: str
    department: str
    agent: str
    workflow_name: str
    description: str
    status: PlanStepStatus = PlanStepStatus.TODO
    requires_approval: bool = False
    dependencies: list[str] = field(default_factory=list)


@dataclass
class ApprovedPlanRuntime:
    project_id: str
    plan_id: str
    approved: bool
    steps: list[PlanStep]

    def next_open_step(self) -> PlanStep | None:
        completed = {s.step_id for s in self.steps if s.status in {PlanStepStatus.DONE, PlanStepStatus.SKIPPED}}
        for step in sorted(self.steps, key=lambda s: s.order):
            if step.status in {PlanStepStatus.TODO, PlanStepStatus.DOING, PlanStepStatus.WAITING_APPROVAL}:
                if all(dep in completed for dep in step.dependencies):
                    return step
        return None
```

---

## 33.5 WorkflowPhaseRouter

```python
@dataclass
class WorkflowPhaseRouter:
    phase_routes: dict[WorkflowPhase, PhaseRoute]

    def route(self, command: Command, project_state: ProjectState) -> RoutingDecision:
        try:
            phase = WorkflowPhase(project_state.current_phase)
        except ValueError:
            return RoutingDecision(
                command_id=command.command_id,
                routing_mode=RoutingMode.CLARIFICATION_REQUIRED,
                target_department=None,
                target_agent=None,
                workflow_name=None,
                next_step="Chiarire fase progetto non riconosciuta",
                confidence=0.0,
                confidence_label=RouteConfidence.NONE,
                reason=f"Fase progetto non riconosciuta: {project_state.current_phase}",
                requires_user_clarification=True,
                clarification_question="La fase del progetto non è riconosciuta. Vuoi impostarla manualmente?",
            )

        route = self.phase_routes.get(phase)
        if route is None:
            return RoutingDecision(
                command_id=command.command_id,
                routing_mode=RoutingMode.NO_ROUTE,
                target_department=None,
                target_agent=None,
                workflow_name=None,
                next_step="Nessuna route definita per la fase corrente",
                confidence=0.0,
                confidence_label=RouteConfidence.NONE,
                reason="PHASE_ROUTES non contiene questa fase",
            )

        return RoutingDecision(
            command_id=command.command_id,
            routing_mode=RoutingMode.PHASE_BASED,
            target_department=route.target_department,
            target_agent=route.target_agent,
            workflow_name=route.workflow_name,
            next_step=route.next_step,
            confidence=1.0,
            confidence_label=RouteConfidence.DETERMINISTIC,
            reason=f"Routing deterministico basato sulla fase corrente: {phase.value}",
            requires_user_clarification=False,
        )
```

---

## 33.6 PlanRouter

```python
@dataclass
class PlanRouter:
    def route(self, command: Command, approved_plan: ApprovedPlanRuntime) -> RoutingDecision:
        if not approved_plan.approved:
            return RoutingDecision(
                command_id=command.command_id,
                routing_mode=RoutingMode.BLOCKED,
                target_department="CAESAR",
                target_agent="Caesar",
                workflow_name="approval_gate",
                next_step="Richiedere approvazione del MasterPlan",
                confidence=1.0,
                confidence_label=RouteConfidence.DETERMINISTIC,
                reason="Il MasterPlan non è approvato",
                blocked=True,
                block_reason="Piano non approvato = Caesar non smista",
            )

        step = approved_plan.next_open_step()
        if step is None:
            return RoutingDecision(
                command_id=command.command_id,
                routing_mode=RoutingMode.NO_ROUTE,
                target_department="D-MEMORY",
                target_agent="L21",
                workflow_name="review_and_analytics",
                next_step="Nessuno step aperto: preparare review o chiusura progetto",
                confidence=0.8,
                confidence_label=RouteConfidence.HIGH,
                reason="Tutti gli step del piano risultano completati o skippati",
            )

        return RoutingDecision(
            command_id=command.command_id,
            routing_mode=RoutingMode.PLAN_BASED,
            target_department=step.department,
            target_agent=step.agent,
            workflow_name=step.workflow_name,
            next_step=step.description,
            confidence=1.0,
            confidence_label=RouteConfidence.DETERMINISTIC,
            reason=f"Routing basato sul prossimo step aperto del piano approvato: {step.step_id}",
            requires_user_clarification=False,
        )
```

---

## 33.7 TriggerRouter fallback

Il routing a trigger rimane utile per:

- comandi spot;
- comandi senza progetto;
- comandi fuori workflow;
- richieste dirette ad Afrodite, Atlas, MARTE o ADE;
- interrogazioni rapide.

```python
@dataclass
class TriggerMatch:
    department: str
    matched_triggers: list[str]
    score: float


@dataclass
class TriggerRouter:
    trigger_routing: dict[str, list[str]]
    min_confidence: float = 0.55
    ambiguity_delta: float = 0.12

    def route(self, command: Command) -> RoutingDecision:
        text = command.normalized_text.lower()
        matches: list[TriggerMatch] = []

        for department, triggers in self.trigger_routing.items():
            matched = [trigger for trigger in triggers if trigger.lower() in text]
            if matched:
                score = min(1.0, len(matched) / max(1, len(triggers)) * 4)
                matches.append(TriggerMatch(department=department, matched_triggers=matched, score=score))

        if not matches:
            return RoutingDecision(
                command_id=command.command_id,
                routing_mode=RoutingMode.CLARIFICATION_REQUIRED,
                target_department=None,
                target_agent=None,
                workflow_name=None,
                next_step="Chiedere chiarimento sul comando",
                confidence=0.0,
                confidence_label=RouteConfidence.NONE,
                reason="Nessun trigger rilevante trovato",
                requires_user_clarification=True,
                clarification_question="Vuoi lavorare su un progetto esistente, creare un nuovo progetto o fare una richiesta spot?",
            )

        matches.sort(key=lambda m: m.score, reverse=True)
        best = matches[0]
        second = matches[1] if len(matches) > 1 else None

        if best.score < self.min_confidence:
            return RoutingDecision(
                command_id=command.command_id,
                routing_mode=RoutingMode.CLARIFICATION_REQUIRED,
                target_department=None,
                target_agent=None,
                workflow_name=None,
                next_step="Chiedere chiarimento per bassa confidenza",
                confidence=best.score,
                confidence_label=RouteConfidence.LOW,
                reason=f"Trigger trovati ma confidenza bassa: {best.matched_triggers}",
                requires_user_clarification=True,
                clarification_question="Non sono sicuro del reparto corretto. Vuoi specificare ricerca, produzione, marketing, sales, memoria, defense o Atlas?",
            )

        if second and (best.score - second.score) < self.ambiguity_delta:
            return RoutingDecision(
                command_id=command.command_id,
                routing_mode=RoutingMode.CLARIFICATION_REQUIRED,
                target_department=None,
                target_agent=None,
                workflow_name=None,
                next_step="Chiedere chiarimento per ambiguità routing",
                confidence=best.score,
                confidence_label=RouteConfidence.MEDIUM,
                reason=f"Ambiguità tra {best.department} e {second.department}",
                requires_user_clarification=True,
                clarification_question=f"Il comando può andare a {best.department} o {second.department}. Quale vuoi usare?",
            )

        target_agent = DEFAULT_DEPARTMENT_AGENT.get(best.department)

        return RoutingDecision(
            command_id=command.command_id,
            routing_mode=RoutingMode.TRIGGER_BASED,
            target_department=best.department,
            target_agent=target_agent,
            workflow_name=None,
            next_step="Instradare richiesta spot al dipartimento rilevato dai trigger",
            confidence=best.score,
            confidence_label=RouteConfidence.HIGH if best.score >= 0.75 else RouteConfidence.MEDIUM,
            reason=f"Trigger rilevati: {', '.join(best.matched_triggers)}",
            requires_user_clarification=False,
        )


DEFAULT_DEPARTMENT_AGENT = {
    "D-RESEARCH": "L3",
    "D-ELABORAZIONE": "L5",
    "D-PRODUCTION": "L7",
    "D-MARKETING": "L10",
    "D-MEDIA": "L11",
    "D-SALES": "L13",
    "D-DEFENSE": "L14",
    "D-MEMORY": "L20",
    "ATLAS": "L23",
    "AFRODITE": "Afrodite",
}
```

---

## 33.8 CaesarRouter

`CaesarRouter` applica la priorità ufficiale:

```text
blocked > phase > plan > trigger > clarification
```

```python
@dataclass
class CaesarRouter:
    phase_router: WorkflowPhaseRouter
    plan_router: PlanRouter
    trigger_router: TriggerRouter

    def route(
        self,
        command: Command,
        project_state: ProjectState | None = None,
        approved_plan: ApprovedPlanRuntime | None = None,
    ) -> RoutingDecision:
        if command.status != CommandStatus.READY_FOR_ROUTING:
            return RoutingDecision(
                command_id=command.command_id,
                routing_mode=RoutingMode.NO_ROUTE,
                target_department=None,
                target_agent=None,
                workflow_name=None,
                next_step="Comando non pronto per routing",
                confidence=0.0,
                confidence_label=RouteConfidence.NONE,
                reason=f"Command.status = {command.status.value}",
            )

        if project_state and project_state.blocked:
            return RoutingDecision(
                command_id=command.command_id,
                routing_mode=RoutingMode.BLOCKED,
                target_department="CAESAR",
                target_agent="Caesar",
                workflow_name="blocked_project_gate",
                next_step="Fermare workflow e chiedere sblocco utente",
                confidence=1.0,
                confidence_label=RouteConfidence.DETERMINISTIC,
                reason="Il progetto è bloccato",
                blocked=True,
                block_reason=project_state.block_reason or "ProjectState.blocked = True",
            )

        if project_state and project_state.current_phase:
            decision = self.phase_router.route(command, project_state)
            if decision.routing_mode != RoutingMode.NO_ROUTE:
                return decision

        if approved_plan is not None:
            return self.plan_router.route(command, approved_plan)

        return self.trigger_router.route(command)
```

---

## 33.9 Integrazione con CaesarRuntime

```python
@dataclass
class CaesarRuntimeV2:
    command_receiver: CommandReceiver
    router: CaesarRouter

    def handle_user_input(
        self,
        raw_text: str,
        context: CommandContext,
        source: CommandSource = CommandSource.CHAT,
        attachments: list[CommandAttachment] | None = None,
        project_state: ProjectState | None = None,
        approved_plan: ApprovedPlanRuntime | None = None,
    ) -> tuple[Command, RoutingDecision]:
        command = self.command_receiver.receive(
            raw_text=raw_text,
            context=context,
            source=source,
            attachments=attachments,
        )

        decision = self.router.route(
            command=command,
            project_state=project_state,
            approved_plan=approved_plan,
        )

        return command, decision
```

---

## 33.10 Esempi routing

### Caso A — Videogame in fase produzione

```python
project_state = ProjectState(
    project_id="game_001",
    name="Videogame Roguelike",
    status=ProjectStatus.EXECUTING,
    created_at="2026-06-15",
    updated_at="2026-06-15",
    current_phase="PRODUCTION",
)

# Anche se l’utente scrive una frase generica,
# il routing va a D-PRODUCTION perché la fase è PRODUCTION.
```

Output atteso:

```text
routing_mode = PHASE_BASED
target_department = D-PRODUCTION
target_agent = L7
confidence = 1.0
```

### Caso B — Libro con piano approvato

```text
Se non c’è current_phase ma esiste un MasterPlan approvato,
Caesar prende il prossimo PlanStep aperto.
```

Output atteso:

```text
routing_mode = PLAN_BASED
target_department = department dello step
target_agent = agent dello step
confidence = 1.0
```

### Caso C — Comando spot

```text
Utente: "Organizza i file"
Nessun project_state attivo.
Nessun piano approvato.
```

Output atteso:

```text
routing_mode = TRIGGER_BASED
target_department = ATLAS
target_agent = L23
```

### Caso D — Ambiguità

```text
Utente: "Prepara contenuti marketing social"
```

Possibile ambiguità:

```text
D-MARKETING vs D-MEDIA vs D-PRODUCTION
```

Output atteso se non c’è fase/piano:

```text
routing_mode = CLARIFICATION_REQUIRED
requires_user_clarification = True
```

---

## 33.11 Regole operative Routing

```text
1. Il routing primario è phase-based.
2. Il routing secondario è plan-based.
3. Il routing a trigger è solo fallback per comandi spot o fuori workflow.
4. Se un progetto è bloccato, nessun routing operativo è permesso.
5. Se il piano non è approvato, Caesar non smista.
6. Se la confidenza trigger è bassa, Caesar chiede chiarimento.
7. Se due dipartimenti sono troppo vicini, Caesar chiede chiarimento.
8. Nei workflow strutturati, la fase batte sempre il trigger testuale.
```

---

## 33.12 Stato del punto implementato

| Punto runtime | Stato |
|---|---|
| Come Caesar decide il dipartimento | Implementato come routing del prossimo step |
| Routing per fase | Implementato |
| Routing per piano approvato | Implementato |
| Routing a trigger fallback | Implementato |
| Confidence | Implementata per trigger e deterministic routing |
| Ambiguità | Implementata |
| Fallback chiarimento | Implementato |
| Blocco progetto | Implementato |

```text
┌─ LA DECISIONE ─────────────────────────────────────────────────┐
│ Scelta: Usare Phase/Plan Router come routing primario e Trigger Router come fallback │
│ Perché: Nei progetti veri il prossimo step dipende dallo stato, non dalle parole │
└────────────────────────────────────────────────────────────────┘
```


---

## 34. Runtime Execution Layer — Task Creation

Questa sezione implementa il terzo punto del runtime: **come Caesar crea un task**.

Obiettivo:

```text
Command + RoutingDecision + ProjectState opzionale
↓
TaskCreationRequest
↓
TaskFactory
↓
Task validato
↓
Task salvato in coda/stato
↓
Pronto per approvazione o esecuzione
```

Regola chiave:

```text
Caesar non esegue direttamente una RoutingDecision.
Caesar trasforma una RoutingDecision in uno o più Task.
```

---

## 34.1 Principio di creazione task

Un `Task` è l’unità minima di lavoro assegnabile a Caesar, a un Legionario, ad Afrodite o ad Atlas.

Un task deve sempre sapere:

- da quale comando nasce;
- da quale routing decision nasce;
- a chi è assegnato;
- quale output deve produrre;
- quali criteri definiscono il completamento;
- se richiede approvazione;
- quale livello di rischio ha;
- dove verrà salvato il risultato;
- quale idempotency key impedisce duplicati.

---

## 34.2 Task Types

```python
class TaskType(str, Enum):
    ANALYSIS = "ANALYSIS"
    RESEARCH = "RESEARCH"
    IDEATION = "IDEATION"
    VALIDATION = "VALIDATION"
    PLANNING = "PLANNING"
    PRE_MORTEM = "PRE_MORTEM"
    PRODUCTION = "PRODUCTION"
    QA = "QA"
    MARKETING = "MARKETING"
    MEDIA = "MEDIA"
    SALES = "SALES"
    MEMORY_UPDATE = "MEMORY_UPDATE"
    FILE_OPERATION = "FILE_OPERATION"
    APPROVAL_REQUEST = "APPROVAL_REQUEST"
    CLARIFICATION_REQUEST = "CLARIFICATION_REQUEST"
    BLOCKED_NOTICE = "BLOCKED_NOTICE"
```

---

## 34.3 Task Creation Request

`TaskCreationRequest` è l’input formale della `TaskFactory`.

```python
@dataclass
class TaskCreationRequest:
    command: Command
    routing_decision: RoutingDecision
    project_state: ProjectState | None = None
    approved_plan: ApprovedPlanRuntime | None = None
    explicit_task_type: TaskType | None = None
    explicit_risk_level: ActionLevel | None = None
    expected_output: str | None = None
    result_path: str | None = None
    metadata: dict[str, Any] = field(default_factory=dict)
```

---

## 34.4 Task Runtime Model

La versione base conteneva già `Task`.  
Per il runtime è utile estenderlo con campi di tracciamento.

```python
@dataclass
class RuntimeTask:
    task_id: str
    project_id: str | None
    command_id: str
    routing_mode: RoutingMode
    assigned_to: str
    department: str | None
    task_type: TaskType
    status: TaskStatus
    description: str
    expected_output: str
    acceptance_criteria: list[str]
    requires_approval: bool
    risk_level: ActionLevel
    idempotency_key: str
    created_at: str
    updated_at: str
    workflow_name: str | None = None
    result_path: str | None = None
    parent_task_id: str | None = None
    dependencies: list[str] = field(default_factory=list)
    metadata: dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data = asdict(self)
        data["routing_mode"] = self.routing_mode.value
        data["task_type"] = self.task_type.value
        data["status"] = self.status.value
        data["risk_level"] = self.risk_level.value
        return data
```

---

## 34.5 Task Store Protocol

I task vengono salvati in formato append-only JSONL più uno snapshot opzionale `tasks-state.json`.

Path consigliato per progetto:

```text
[progetto]/.agents/runtime/tasks.jsonl
[progetto]/.agents/runtime/tasks-state.json
```

Path per task fuori progetto:

```text
centro-di-comando/runtime/tasks.jsonl
centro-di-comando/runtime/tasks-state.json
```

```python
class TaskStore(Protocol):
    def append(self, task: RuntimeTask) -> None:
        ...

    def upsert_state(self, task: RuntimeTask) -> None:
        ...


@dataclass
class JsonlTaskStore:
    log_path: Path
    state_path: Path | None = None

    def append(self, task: RuntimeTask) -> None:
        self.log_path.parent.mkdir(parents=True, exist_ok=True)
        with self.log_path.open("a", encoding="utf-8") as f:
            f.write(json.dumps(task.to_dict(), ensure_ascii=False) + "\n")

    def upsert_state(self, task: RuntimeTask) -> None:
        if self.state_path is None:
            return

        self.state_path.parent.mkdir(parents=True, exist_ok=True)
        if self.state_path.exists():
            state = json.loads(self.state_path.read_text(encoding="utf-8"))
        else:
            state = {"tasks": {}}

        state.setdefault("tasks", {})[task.task_id] = task.to_dict()
        self.state_path.write_text(json.dumps(state, ensure_ascii=False, indent=2), encoding="utf-8")
```

---

## 34.6 TaskFactory

`TaskFactory` crea task solo da input già normalizzati e instradati.

Responsabilità:

1. rifiutare routing non azionabile;
2. inferire `TaskType`;
3. inferire `ActionLevel`;
4. determinare se serve approvazione;
5. creare acceptance criteria minimi;
6. generare `task_id`;
7. generare `idempotency_key`;
8. salvare il task;
9. restituire `RuntimeTask`.

```python
@dataclass
class TaskFactory:
    store: TaskStore | None = None

    def create_task(self, request: TaskCreationRequest) -> RuntimeTask:
        command = request.command
        decision = request.routing_decision

        if not decision.is_actionable():
            return self._create_non_actionable_task(request)

        now = self._now_iso()
        task_type = request.explicit_task_type or self.infer_task_type(decision)
        risk_level = request.explicit_risk_level or self.infer_risk_level(task_type, decision)
        requires_approval = self.requires_approval(risk_level, task_type, decision)
        expected_output = request.expected_output or self.default_expected_output(task_type, decision)
        acceptance_criteria = self.default_acceptance_criteria(task_type, decision)

        task = RuntimeTask(
            task_id=self.new_task_id(),
            project_id=command.context.project_id,
            command_id=command.command_id,
            routing_mode=decision.routing_mode,
            assigned_to=decision.target_agent or "Caesar",
            department=decision.target_department,
            task_type=task_type,
            status=TaskStatus.WAITING_APPROVAL if requires_approval else TaskStatus.TODO,
            description=decision.next_step,
            expected_output=expected_output,
            acceptance_criteria=acceptance_criteria,
            requires_approval=requires_approval,
            risk_level=risk_level,
            idempotency_key="",
            created_at=now,
            updated_at=now,
            workflow_name=decision.workflow_name,
            result_path=request.result_path,
            metadata={
                **request.metadata,
                "routing_reason": decision.reason,
                "confidence": decision.confidence,
                "confidence_label": decision.confidence_label.value,
                "source_text": command.normalized_text,
            },
        )
        task.idempotency_key = self.make_task_idempotency_key(task)
        self._persist(task)
        return task

    def _create_non_actionable_task(self, request: TaskCreationRequest) -> RuntimeTask:
        command = request.command
        decision = request.routing_decision
        now = self._now_iso()

        if decision.blocked:
            task_type = TaskType.BLOCKED_NOTICE
            status = TaskStatus.BLOCKED
            description = decision.block_reason or decision.next_step
            risk_level = ActionLevel.A0
            requires_approval = False
        else:
            task_type = TaskType.CLARIFICATION_REQUEST
            status = TaskStatus.WAITING_APPROVAL
            description = decision.clarification_question or "Chiarimento richiesto all’utente"
            risk_level = ActionLevel.A0
            requires_approval = False

        task = RuntimeTask(
            task_id=self.new_task_id(),
            project_id=command.context.project_id,
            command_id=command.command_id,
            routing_mode=decision.routing_mode,
            assigned_to="Caesar",
            department="CAESAR",
            task_type=task_type,
            status=status,
            description=description,
            expected_output="Risposta o decisione dell’utente necessaria per continuare",
            acceptance_criteria=["L’utente fornisce chiarimento, sblocco o decisione esplicita"],
            requires_approval=requires_approval,
            risk_level=risk_level,
            idempotency_key="",
            created_at=now,
            updated_at=now,
            workflow_name=decision.workflow_name,
            result_path=None,
            metadata={
                "routing_reason": decision.reason,
                "clarification_question": decision.clarification_question,
                "block_reason": decision.block_reason,
            },
        )
        task.idempotency_key = self.make_task_idempotency_key(task)
        self._persist(task)
        return task

    @staticmethod
    def infer_task_type(decision: RoutingDecision) -> TaskType:
        if decision.routing_mode == RoutingMode.CLARIFICATION_REQUIRED:
            return TaskType.CLARIFICATION_REQUEST

        workflow = decision.workflow_name or ""
        department = decision.target_department or ""
        agent = decision.target_agent or ""

        if workflow in {"approval_gate", "blocked_project_gate"}:
            return TaskType.APPROVAL_REQUEST
        if workflow in {"ade_pre_mortem"} or agent == "L19":
            return TaskType.PRE_MORTEM
        if workflow in {"first_execution_plan"} or agent == "L14":
            return TaskType.PLANNING
        if workflow in {"idea_elaboration"} or agent == "L5":
            return TaskType.IDEATION
        if workflow in {"idea_validation"} or agent == "L6":
            return TaskType.VALIDATION
        if department == "D-RESEARCH":
            return TaskType.RESEARCH
        if department == "D-PRODUCTION" and agent == "L8":
            return TaskType.QA
        if department == "D-PRODUCTION":
            return TaskType.PRODUCTION
        if department == "D-MARKETING":
            return TaskType.MARKETING
        if department == "D-MEDIA":
            return TaskType.MEDIA
        if department == "D-SALES":
            return TaskType.SALES
        if department == "D-MEMORY":
            return TaskType.MEMORY_UPDATE
        if department == "ATLAS":
            return TaskType.FILE_OPERATION

        return TaskType.ANALYSIS

    @staticmethod
    def infer_risk_level(task_type: TaskType, decision: RoutingDecision) -> ActionLevel:
        if task_type in {TaskType.ANALYSIS, TaskType.RESEARCH, TaskType.IDEATION, TaskType.VALIDATION, TaskType.PRE_MORTEM}:
            return ActionLevel.A0
        if task_type in {TaskType.PLANNING, TaskType.PRODUCTION, TaskType.QA, TaskType.MARKETING, TaskType.MEDIA, TaskType.SALES, TaskType.MEMORY_UPDATE}:
            return ActionLevel.A1
        if task_type == TaskType.FILE_OPERATION:
            return ActionLevel.A2
        if task_type == TaskType.APPROVAL_REQUEST:
            return ActionLevel.A0
        if task_type in {TaskType.CLARIFICATION_REQUEST, TaskType.BLOCKED_NOTICE}:
            return ActionLevel.A0
        return ActionLevel.A1

    @staticmethod
    def requires_approval(risk_level: ActionLevel, task_type: TaskType, decision: RoutingDecision) -> bool:
        if risk_level in APPROVAL_REQUIRED_FOR:
            return True
        if task_type == TaskType.APPROVAL_REQUEST:
            return True
        if decision.routing_mode == RoutingMode.BLOCKED:
            return False
        return False

    @staticmethod
    def default_expected_output(task_type: TaskType, decision: RoutingDecision) -> str:
        expected = {
            TaskType.ANALYSIS: "Analisi sintetica con raccomandazione e DecisionBox se operativa",
            TaskType.RESEARCH: "Report di ricerca con fonti e sintesi azionabile",
            TaskType.IDEATION: "Bozza di modello monetizzabile o IdeaBrief",
            TaskType.VALIDATION: "Valutazione di fattibilità, leva, rischio e raccomandazione",
            TaskType.PLANNING: "MasterPlan completo con DecisionBox",
            TaskType.PRE_MORTEM: "Report ADE con scenari, mitigazioni, verdetto e DecisionBox",
            TaskType.PRODUCTION: "Deliverable prodotto secondo acceptance criteria",
            TaskType.QA: "Report QA con esito, problemi e correzioni richieste",
            TaskType.MARKETING: "Output marketing conforme a product-marketing.md",
            TaskType.MEDIA: "Bozze contenuti media da approvare prima della pubblicazione",
            TaskType.SALES: "Bozze sales/outreach da approvare prima dell’invio",
            TaskType.MEMORY_UPDATE: "Aggiornamento memoria, report o analytics",
            TaskType.FILE_OPERATION: "Proposta o modifica filesystem con changelog",
            TaskType.APPROVAL_REQUEST: "Richiesta di approvazione chiara per l’utente",
            TaskType.CLARIFICATION_REQUEST: "Domanda di chiarimento per sbloccare il routing",
            TaskType.BLOCKED_NOTICE: "Notifica blocco con motivo e prossima decisione richiesta",
        }
        return expected.get(task_type, decision.next_step)

    @staticmethod
    def default_acceptance_criteria(task_type: TaskType, decision: RoutingDecision) -> list[str]:
        base = [
            "Output coerente con il task richiesto",
            "Nessuna azione A2+ eseguita senza approvazione",
        ]

        if task_type == TaskType.PLANNING:
            return base + [
                "MasterPlan contiene obiettivo, metriche, fasi, budget, rischi e checkpoint",
                "Completeness score >= 0.90",
                "DecisionBox presente",
            ]

        if task_type == TaskType.PRE_MORTEM:
            return base + [
                "ADE copre le 10 categorie di rischio",
                "Ogni rischio ha probabilità, impatto, mitigazione e kill condition",
                "Verdetto ADE presente",
                "DecisionBox presente",
            ]

        if task_type == TaskType.QA:
            return base + [
                "Output verificato contro acceptance criteria",
                "Problemi bloccanti separati da warning",
            ]

        if task_type in {TaskType.MARKETING, TaskType.MEDIA, TaskType.SALES}:
            return base + [
                "Output pronto per review utente",
                "Nessuna pubblicazione o invio effettuato",
                "DecisionBox presente se serve decisione operativa",
            ]

        if task_type == TaskType.FILE_OPERATION:
            return base + [
                "Changelog generato",
                "Riferimenti aggiornati o segnalati",
                "Approvazione esplicita presente prima di modifiche A2+",
            ]

        return base

    @staticmethod
    def new_task_id() -> str:
        return f"task_{uuid.uuid4().hex[:12]}"

    @staticmethod
    def _now_iso() -> str:
        return datetime.now(timezone.utc).isoformat()

    @staticmethod
    def make_task_idempotency_key(task: RuntimeTask) -> str:
        base = "|".join([
            task.project_id or "NO_PROJECT",
            task.command_id,
            task.assigned_to,
            task.department or "NO_DEPARTMENT",
            task.task_type.value,
            task.description.lower(),
        ])
        return hashlib.sha256(base.encode("utf-8")).hexdigest()

    def _persist(self, task: RuntimeTask) -> None:
        if self.store is not None:
            self.store.append(task)
            self.store.upsert_state(task)
```

---

## 34.7 Task Validation

Prima di entrare in coda, un task deve superare validazione minima.

```python
@dataclass
class TaskValidationResult:
    valid: bool
    errors: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)
    blocking: bool = False


def validate_runtime_task(task: RuntimeTask) -> TaskValidationResult:
    errors: list[str] = []
    warnings: list[str] = []

    if not task.task_id:
        errors.append("task_id mancante")
    if not task.command_id:
        errors.append("command_id mancante")
    if not task.assigned_to:
        errors.append("assigned_to mancante")
    if not task.description:
        errors.append("description mancante")
    if not task.expected_output:
        errors.append("expected_output mancante")
    if not task.acceptance_criteria:
        errors.append("acceptance_criteria mancante")
    if not task.idempotency_key:
        errors.append("idempotency_key mancante")

    if task.risk_level in APPROVAL_REQUIRED_FOR and not task.requires_approval:
        errors.append("task A2+ senza requires_approval=True")

    if task.status == TaskStatus.TODO and task.requires_approval:
        warnings.append("task approvativo marcato TODO invece di WAITING_APPROVAL")

    return TaskValidationResult(
        valid=len(errors) == 0,
        errors=errors,
        warnings=warnings,
        blocking=len(errors) > 0,
    )
```

---

## 34.8 TaskQueue

`TaskQueue` mantiene i task pronti, bloccati e in attesa approvazione.

```python
@dataclass
class TaskQueue:
    tasks: dict[str, RuntimeTask] = field(default_factory=dict)

    def add(self, task: RuntimeTask) -> TaskValidationResult:
        validation = validate_runtime_task(task)
        if not validation.valid:
            return validation
        self.tasks[task.task_id] = task
        return validation

    def get_ready_tasks(self) -> list[RuntimeTask]:
        return [
            task for task in self.tasks.values()
            if task.status == TaskStatus.TODO and not task.requires_approval
        ]

    def get_waiting_approval(self) -> list[RuntimeTask]:
        return [
            task for task in self.tasks.values()
            if task.status == TaskStatus.WAITING_APPROVAL or task.requires_approval
        ]

    def get_blocked(self) -> list[RuntimeTask]:
        return [task for task in self.tasks.values() if task.status == TaskStatus.BLOCKED]

    def mark_doing(self, task_id: str) -> None:
        self.tasks[task_id].status = TaskStatus.DOING
        self.tasks[task_id].updated_at = datetime.now(timezone.utc).isoformat()

    def mark_done(self, task_id: str) -> None:
        self.tasks[task_id].status = TaskStatus.DONE
        self.tasks[task_id].updated_at = datetime.now(timezone.utc).isoformat()

    def mark_failed(self, task_id: str, reason: str) -> None:
        self.tasks[task_id].status = TaskStatus.FAILED
        self.tasks[task_id].metadata["failure_reason"] = reason
        self.tasks[task_id].updated_at = datetime.now(timezone.utc).isoformat()
```

---

## 34.9 Integrazione RoutingDecision → Task

```python
@dataclass
class CaesarTaskRuntime:
    command_receiver: CommandReceiver
    router: CaesarRouter
    task_factory: TaskFactory
    task_queue: TaskQueue

    def handle_user_input_to_task(
        self,
        raw_text: str,
        context: CommandContext,
        source: CommandSource = CommandSource.CHAT,
        attachments: list[CommandAttachment] | None = None,
        project_state: ProjectState | None = None,
        approved_plan: ApprovedPlanRuntime | None = None,
    ) -> tuple[Command, RoutingDecision, RuntimeTask, TaskValidationResult]:
        command = self.command_receiver.receive(
            raw_text=raw_text,
            context=context,
            source=source,
            attachments=attachments,
        )

        routing_decision = self.router.route(
            command=command,
            project_state=project_state,
            approved_plan=approved_plan,
        )

        task = self.task_factory.create_task(
            TaskCreationRequest(
                command=command,
                routing_decision=routing_decision,
                project_state=project_state,
                approved_plan=approved_plan,
            )
        )

        validation = self.task_queue.add(task)
        return command, routing_decision, task, validation
```

---

## 34.10 Esempi Task Creation

### Caso A — Fase produzione videogame

Input:

```text
current_phase = PRODUCTION
RoutingDecision.target_department = D-PRODUCTION
RoutingDecision.target_agent = L7
```

Task creato:

```text
task_type = PRODUCTION
assigned_to = L7
risk_level = A1
status = TODO
requires_approval = False
```

Nota:

```text
Il task può produrre bozze o deliverable interni.
Qualsiasi modifica A2+ o pubblicazione futura richiederà approvazione separata.
```

### Caso B — Atlas file operation

Input:

```text
RoutingDecision.target_department = ATLAS
RoutingDecision.target_agent = L23
```

Task creato:

```text
task_type = FILE_OPERATION
assigned_to = L23
risk_level = A2
status = WAITING_APPROVAL
requires_approval = True
```

### Caso C — Ambiguità routing

Input:

```text
RoutingDecision.routing_mode = CLARIFICATION_REQUIRED
```

Task creato:

```text
task_type = CLARIFICATION_REQUEST
assigned_to = Caesar
status = WAITING_APPROVAL
expected_output = Risposta dell’utente
```

### Caso D — Progetto bloccato

Input:

```text
RoutingDecision.routing_mode = BLOCKED
```

Task creato:

```text
task_type = BLOCKED_NOTICE
assigned_to = Caesar
status = BLOCKED
```

---

## 34.11 Regole operative Task Creation

```text
1. Caesar crea task solo da Command + RoutingDecision.
2. Nessun Legionario riceve RoutingDecision grezza senza Task.
3. Ogni Task ha idempotency_key.
4. Ogni Task ha acceptance_criteria.
5. Ogni Task A2+ entra in WAITING_APPROVAL.
6. Ogni Task non azionabile diventa CLARIFICATION_REQUEST o BLOCKED_NOTICE.
7. TaskFactory non esegue il task: lo crea e lo accoda.
8. TaskQueue non valida output: valida solo la struttura del task.
9. L’esecuzione reale appartiene al futuro Execution Layer.
```

---

## 34.12 Stato del punto implementato

| Punto runtime | Stato |
|---|---|
| Come Caesar crea un task | Implementato |
| `TaskCreationRequest` | Implementato |
| `RuntimeTask` | Implementato |
| `TaskFactory.create_task()` | Implementato |
| Inferenza `TaskType` | Implementata |
| Inferenza `ActionLevel` | Implementata |
| Approval flag automatico | Implementato |
| Acceptance criteria automatici | Implementati |
| Persistenza task JSONL/state | Implementata |
| `TaskQueue` | Implementata |
| Integrazione Command → RoutingDecision → Task | Implementata |

```text
┌─ LA DECISIONE ─────────────────────────────────────────────────┐
│ Scelta: Usare TaskFactory come unico punto di creazione task Caesar │
│ Perché: Ogni lavoro diventa tracciabile, validabile e approvabile │
└────────────────────────────────────────────────────────────────┘
```


---

## 35. Runtime Execution Layer — StateStore

Questa sezione implementa il quarto punto del runtime: **dove Caesar salva lo stato**.

Obiettivo:

```text
ProjectState + TaskState + WorkflowState + ApprovalState + Runtime metadata
↓
StateStore
↓
Snapshot JSON atomici + log append-only
↓
Ripresa workflow, audit e recovery
```

Regola chiave:

```text
Caesar non tiene lo stato solo in memoria.
Ogni stato operativo rilevante deve essere persistito in StateStore.
```

---

## 35.1 Principio di persistenza stato

Lo stato operativo del Castello viene diviso in due forme:

| Tipo | Funzione | Formato |
|---|---|---|
| **Snapshot** | Stato corrente leggibile e ripristinabile | JSON |
| **Event Log** | Cronologia append-only degli aggiornamenti | JSONL |

Lo snapshot serve a riprendere rapidamente il sistema.  
L’event log serve ad audit, debug, provenance e ricostruzione.

---

## 35.2 Path Runtime Canonici

Per progetto:

```text
[progetto]/.agents/runtime/
├── state.json
├── state-events.jsonl
├── commands.jsonl
├── tasks.jsonl
├── tasks-state.json
├── approvals.jsonl
├── workflow-checkpoints.jsonl
└── locks/
```

Per Centro di Comando:

```text
centro-di-comando/runtime/
├── state.json
├── state-events.jsonl
├── commands.jsonl
├── tasks.jsonl
├── tasks-state.json
├── approvals.jsonl
├── workflow-checkpoints.jsonl
└── locks/
```

### Path in Python

```python
@dataclass(frozen=True)
class RuntimePaths:
    root: Path

    @property
    def state_snapshot(self) -> Path:
        return self.root / "state.json"

    @property
    def state_events(self) -> Path:
        return self.root / "state-events.jsonl"

    @property
    def commands_log(self) -> Path:
        return self.root / "commands.jsonl"

    @property
    def tasks_log(self) -> Path:
        return self.root / "tasks.jsonl"

    @property
    def tasks_state(self) -> Path:
        return self.root / "tasks-state.json"

    @property
    def approvals_log(self) -> Path:
        return self.root / "approvals.jsonl"

    @property
    def workflow_checkpoints(self) -> Path:
        return self.root / "workflow-checkpoints.jsonl"

    @property
    def locks_dir(self) -> Path:
        return self.root / "locks"


PROJECT_RUNTIME_PATH = Path(".agents/runtime")
COMMAND_CENTER_RUNTIME_PATH = Path("centro-di-comando/runtime")
```

---

## 35.3 RuntimeState

`RuntimeState` è lo snapshot corrente del sistema per un progetto o per il Centro di Comando.

```python
class RuntimeScope(str, Enum):
    PROJECT = "PROJECT"
    COMMAND_CENTER = "COMMAND_CENTER"


@dataclass
class WorkflowRuntimeState:
    workflow_name: str
    current_step: str
    status: str
    cursor: int = 0
    last_checkpoint_id: str | None = None
    waiting_for_approval_id: str | None = None
    blocked: bool = False
    block_reason: str | None = None
    metadata: dict[str, Any] = field(default_factory=dict)


@dataclass
class ApprovalRuntimeState:
    approval_id: str
    status: str  # PENDING | APPROVED | REJECTED | EXPIRED | CANCELLED
    requested_by: str
    requested_at: str
    resolved_at: str | None = None
    decision: str | None = None
    metadata: dict[str, Any] = field(default_factory=dict)


@dataclass
class RuntimeState:
    scope: RuntimeScope
    state_id: str
    updated_at: str
    project_state: ProjectState | None = None
    workflow_state: WorkflowRuntimeState | None = None
    tasks: dict[str, RuntimeTask] = field(default_factory=dict)
    approvals: dict[str, ApprovalRuntimeState] = field(default_factory=dict)
    last_command_id: str | None = None
    last_routing_decision: dict[str, Any] | None = None
    metadata: dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> dict[str, Any]:
        return {
            "scope": self.scope.value,
            "state_id": self.state_id,
            "updated_at": self.updated_at,
            "project_state": asdict(self.project_state) if self.project_state else None,
            "workflow_state": asdict(self.workflow_state) if self.workflow_state else None,
            "tasks": {task_id: task.to_dict() for task_id, task in self.tasks.items()},
            "approvals": {approval_id: asdict(approval) for approval_id, approval in self.approvals.items()},
            "last_command_id": self.last_command_id,
            "last_routing_decision": self.last_routing_decision,
            "metadata": self.metadata,
        }
```

---

## 35.4 State Events

Ogni modifica importante dello stato genera uno `StateEvent` append-only.

```python
class StateEventType(str, Enum):
    STATE_CREATED = "STATE_CREATED"
    STATE_SNAPSHOT_WRITTEN = "STATE_SNAPSHOT_WRITTEN"
    PROJECT_STATE_UPDATED = "PROJECT_STATE_UPDATED"
    WORKFLOW_STATE_UPDATED = "WORKFLOW_STATE_UPDATED"
    TASK_ADDED = "TASK_ADDED"
    TASK_UPDATED = "TASK_UPDATED"
    APPROVAL_ADDED = "APPROVAL_ADDED"
    APPROVAL_UPDATED = "APPROVAL_UPDATED"
    COMMAND_LINKED = "COMMAND_LINKED"
    ROUTING_LINKED = "ROUTING_LINKED"
    STATE_RECOVERED = "STATE_RECOVERED"
    STATE_ERROR = "STATE_ERROR"


@dataclass
class StateEvent:
    event_id: str
    timestamp: str
    event_type: StateEventType
    state_id: str
    summary: str
    actor: str = "Caesar"
    project_id: str | None = None
    command_id: str | None = None
    task_id: str | None = None
    approval_id: str | None = None
    idempotency_key: str = ""
    payload: dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data = asdict(self)
        data["event_type"] = self.event_type.value
        return data
```

---

## 35.5 StateStore Protocol

```python
class StateStore(Protocol):
    def load(self) -> RuntimeState | None:
        ...

    def save_snapshot(self, state: RuntimeState) -> None:
        ...

    def append_event(self, event: StateEvent) -> None:
        ...

    def update_project_state(self, project_state: ProjectState) -> RuntimeState:
        ...

    def update_workflow_state(self, workflow_state: WorkflowRuntimeState) -> RuntimeState:
        ...

    def add_task(self, task: RuntimeTask) -> RuntimeState:
        ...

    def update_task(self, task: RuntimeTask) -> RuntimeState:
        ...

    def add_approval(self, approval: ApprovalRuntimeState) -> RuntimeState:
        ...
```

---

## 35.6 JSON StateStore con scrittura atomica

Il `JsonStateStore` è l’implementazione locale default.

Caratteristiche:

- snapshot JSON leggibile;
- eventi JSONL append-only;
- scrittura atomica con file temporaneo;
- directory create automaticamente;
- stato ricostruibile almeno dallo snapshot;
- nessuna cancellazione automatica.

```python
@dataclass
class JsonStateStore:
    runtime_paths: RuntimePaths
    scope: RuntimeScope
    state_id: str

    def load(self) -> RuntimeState | None:
        path = self.runtime_paths.state_snapshot
        if not path.exists():
            return None
        raw = json.loads(path.read_text(encoding="utf-8"))
        return self._runtime_state_from_dict(raw)

    def save_snapshot(self, state: RuntimeState) -> None:
        self.runtime_paths.root.mkdir(parents=True, exist_ok=True)
        state.updated_at = self._now_iso()
        self._atomic_write_json(self.runtime_paths.state_snapshot, state.to_dict())
        self.append_event(StateEvent(
            event_id=self.new_event_id(),
            timestamp=self._now_iso(),
            event_type=StateEventType.STATE_SNAPSHOT_WRITTEN,
            state_id=state.state_id,
            summary="Snapshot stato scritto su disco",
            project_id=state.project_state.project_id if state.project_state else None,
            idempotency_key=self.make_event_idempotency_key(
                StateEventType.STATE_SNAPSHOT_WRITTEN,
                state.state_id,
                state.updated_at,
            ),
        ))

    def append_event(self, event: StateEvent) -> None:
        self.runtime_paths.root.mkdir(parents=True, exist_ok=True)
        if not event.idempotency_key:
            event.idempotency_key = self.make_event_idempotency_key(
                event.event_type,
                event.state_id,
                event.summary,
            )
        with self.runtime_paths.state_events.open("a", encoding="utf-8") as f:
            f.write(json.dumps(event.to_dict(), ensure_ascii=False) + "\n")

    def get_or_create(self) -> RuntimeState:
        existing = self.load()
        if existing:
            return existing

        state = RuntimeState(
            scope=self.scope,
            state_id=self.state_id,
            updated_at=self._now_iso(),
        )
        self.save_snapshot(state)
        self.append_event(StateEvent(
            event_id=self.new_event_id(),
            timestamp=self._now_iso(),
            event_type=StateEventType.STATE_CREATED,
            state_id=state.state_id,
            summary="RuntimeState creato",
            idempotency_key=self.make_event_idempotency_key(StateEventType.STATE_CREATED, state.state_id, "created"),
        ))
        return state

    def update_project_state(self, project_state: ProjectState) -> RuntimeState:
        state = self.get_or_create()
        state.project_state = project_state
        state.updated_at = self._now_iso()
        self.save_snapshot(state)
        self.append_event(StateEvent(
            event_id=self.new_event_id(),
            timestamp=self._now_iso(),
            event_type=StateEventType.PROJECT_STATE_UPDATED,
            state_id=state.state_id,
            summary=f"ProjectState aggiornato: {project_state.name}",
            project_id=project_state.project_id,
            idempotency_key=self.make_event_idempotency_key(
                StateEventType.PROJECT_STATE_UPDATED,
                project_state.project_id,
                project_state.updated_at,
            ),
        ))
        return state

    def update_workflow_state(self, workflow_state: WorkflowRuntimeState) -> RuntimeState:
        state = self.get_or_create()
        state.workflow_state = workflow_state
        state.updated_at = self._now_iso()
        self.save_snapshot(state)
        self.append_event(StateEvent(
            event_id=self.new_event_id(),
            timestamp=self._now_iso(),
            event_type=StateEventType.WORKFLOW_STATE_UPDATED,
            state_id=state.state_id,
            summary=f"WorkflowState aggiornato: {workflow_state.workflow_name}/{workflow_state.current_step}",
            project_id=state.project_state.project_id if state.project_state else None,
            idempotency_key=self.make_event_idempotency_key(
                StateEventType.WORKFLOW_STATE_UPDATED,
                state.state_id,
                workflow_state.workflow_name + workflow_state.current_step,
            ),
        ))
        return state

    def add_task(self, task: RuntimeTask) -> RuntimeState:
        state = self.get_or_create()
        state.tasks[task.task_id] = task
        state.last_command_id = task.command_id
        state.updated_at = self._now_iso()
        self.save_snapshot(state)
        self.append_event(StateEvent(
            event_id=self.new_event_id(),
            timestamp=self._now_iso(),
            event_type=StateEventType.TASK_ADDED,
            state_id=state.state_id,
            summary=f"Task aggiunto: {task.task_id}",
            project_id=task.project_id,
            command_id=task.command_id,
            task_id=task.task_id,
            idempotency_key=self.make_event_idempotency_key(StateEventType.TASK_ADDED, task.task_id, task.idempotency_key),
        ))
        return state

    def update_task(self, task: RuntimeTask) -> RuntimeState:
        state = self.get_or_create()
        state.tasks[task.task_id] = task
        state.updated_at = self._now_iso()
        self.save_snapshot(state)
        self.append_event(StateEvent(
            event_id=self.new_event_id(),
            timestamp=self._now_iso(),
            event_type=StateEventType.TASK_UPDATED,
            state_id=state.state_id,
            summary=f"Task aggiornato: {task.task_id} → {task.status.value}",
            project_id=task.project_id,
            command_id=task.command_id,
            task_id=task.task_id,
            idempotency_key=self.make_event_idempotency_key(
                StateEventType.TASK_UPDATED,
                task.task_id,
                task.status.value + task.updated_at,
            ),
        ))
        return state

    def add_approval(self, approval: ApprovalRuntimeState) -> RuntimeState:
        state = self.get_or_create()
        state.approvals[approval.approval_id] = approval
        if state.workflow_state:
            state.workflow_state.waiting_for_approval_id = approval.approval_id
        state.updated_at = self._now_iso()
        self.save_snapshot(state)
        self.append_event(StateEvent(
            event_id=self.new_event_id(),
            timestamp=self._now_iso(),
            event_type=StateEventType.APPROVAL_ADDED,
            state_id=state.state_id,
            summary=f"Approval aggiunta: {approval.approval_id}",
            approval_id=approval.approval_id,
            idempotency_key=self.make_event_idempotency_key(
                StateEventType.APPROVAL_ADDED,
                approval.approval_id,
                approval.requested_at,
            ),
        ))
        return state

    def link_routing_decision(self, decision: RoutingDecision) -> RuntimeState:
        state = self.get_or_create()
        state.last_routing_decision = asdict(decision)
        state.last_routing_decision["routing_mode"] = decision.routing_mode.value
        state.last_routing_decision["confidence_label"] = decision.confidence_label.value
        state.updated_at = self._now_iso()
        self.save_snapshot(state)
        self.append_event(StateEvent(
            event_id=self.new_event_id(),
            timestamp=self._now_iso(),
            event_type=StateEventType.ROUTING_LINKED,
            state_id=state.state_id,
            summary="RoutingDecision collegata allo stato runtime",
            command_id=decision.command_id,
            idempotency_key=self.make_event_idempotency_key(
                StateEventType.ROUTING_LINKED,
                state.state_id,
                decision.command_id,
            ),
        ))
        return state

    @staticmethod
    def _atomic_write_json(path: Path, data: dict[str, Any]) -> None:
        path.parent.mkdir(parents=True, exist_ok=True)
        tmp_path = path.with_suffix(path.suffix + ".tmp")
        tmp_path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
        tmp_path.replace(path)

    @staticmethod
    def _now_iso() -> str:
        return datetime.now(timezone.utc).isoformat()

    @staticmethod
    def new_event_id() -> str:
        return f"state_evt_{uuid.uuid4().hex[:12]}"

    @staticmethod
    def make_event_idempotency_key(event_type: StateEventType, state_id: str, seed: str) -> str:
        base = f"{event_type.value}|{state_id}|{seed}"
        return hashlib.sha256(base.encode("utf-8")).hexdigest()

    def _runtime_state_from_dict(self, raw: dict[str, Any]) -> RuntimeState:
        # Nota implementativa:
        # In produzione questa funzione deve ricostruire gli Enum e le dataclass annidate.
        # Qui rimane volutamente minimale per mantenere la specifica compatta.
        return RuntimeState(
            scope=RuntimeScope(raw["scope"]),
            state_id=raw["state_id"],
            updated_at=raw["updated_at"],
            project_state=None,
            workflow_state=None,
            tasks={},
            approvals={},
            last_command_id=raw.get("last_command_id"),
            last_routing_decision=raw.get("last_routing_decision"),
            metadata=raw.get("metadata", {}),
        )
```

---

## 35.7 StateStore Factory

La factory sceglie dove salvare lo stato.

```python
@dataclass
class StateStoreFactory:
    workspace_root: Path

    def for_project(self, project_path: Path, project_id: str) -> JsonStateStore:
        runtime_root = project_path / PROJECT_RUNTIME_PATH
        return JsonStateStore(
            runtime_paths=RuntimePaths(runtime_root),
            scope=RuntimeScope.PROJECT,
            state_id=f"state_project_{project_id}",
        )

    def for_command_center(self) -> JsonStateStore:
        runtime_root = self.workspace_root / COMMAND_CENTER_RUNTIME_PATH
        return JsonStateStore(
            runtime_paths=RuntimePaths(runtime_root),
            scope=RuntimeScope.COMMAND_CENTER,
            state_id="state_command_center",
        )
```

---

## 35.8 Integrazione con CaesarTaskRuntime

Dopo aver creato un command, una routing decision e un task, Caesar aggiorna lo stato.

```python
@dataclass
class CaesarStatefulRuntime:
    command_receiver: CommandReceiver
    router: CaesarRouter
    task_factory: TaskFactory
    task_queue: TaskQueue
    state_store: StateStore

    def handle_user_input_to_stateful_task(
        self,
        raw_text: str,
        context: CommandContext,
        source: CommandSource = CommandSource.CHAT,
        attachments: list[CommandAttachment] | None = None,
        project_state: ProjectState | None = None,
        approved_plan: ApprovedPlanRuntime | None = None,
    ) -> tuple[Command, RoutingDecision, RuntimeTask, RuntimeState]:
        command = self.command_receiver.receive(
            raw_text=raw_text,
            context=context,
            source=source,
            attachments=attachments,
        )

        routing_decision = self.router.route(
            command=command,
            project_state=project_state,
            approved_plan=approved_plan,
        )

        task = self.task_factory.create_task(
            TaskCreationRequest(
                command=command,
                routing_decision=routing_decision,
                project_state=project_state,
                approved_plan=approved_plan,
            )
        )

        validation = self.task_queue.add(task)
        if not validation.valid:
            # La gestione dettagliata degli errori appartiene all'ErrorManager.
            task.status = TaskStatus.FAILED
            task.metadata["validation_errors"] = validation.errors

        state = self.state_store.get_or_create() if hasattr(self.state_store, "get_or_create") else self.state_store.load()

        if project_state is not None:
            state = self.state_store.update_project_state(project_state)

        if hasattr(self.state_store, "link_routing_decision"):
            state = self.state_store.link_routing_decision(routing_decision)

        state = self.state_store.add_task(task)
        return command, routing_decision, task, state
```

---

## 35.9 Aggiornamento stato progetto

Ogni cambio di stato progetto deve passare da `StateStore.update_project_state()`.

```python
PROJECT_STATE_TRANSITION_RULES = {
    ProjectStatus.IDEA: {ProjectStatus.VALIDATING, ProjectStatus.SCRAPPED, ProjectStatus.PAUSED},
    ProjectStatus.VALIDATING: {ProjectStatus.PLANNING, ProjectStatus.SCRAPPED, ProjectStatus.PAUSED},
    ProjectStatus.PLANNING: {ProjectStatus.WAITING_APPROVAL, ProjectStatus.SCRAPPED, ProjectStatus.KILLED, ProjectStatus.PAUSED},
    ProjectStatus.WAITING_APPROVAL: {ProjectStatus.APPROVED, ProjectStatus.SCRAPPED, ProjectStatus.KILLED, ProjectStatus.PAUSED},
    ProjectStatus.APPROVED: {ProjectStatus.EXECUTING, ProjectStatus.PAUSED, ProjectStatus.KILLED},
    ProjectStatus.EXECUTING: {ProjectStatus.REVIEWING, ProjectStatus.PAUSED, ProjectStatus.KILLED},
    ProjectStatus.REVIEWING: {ProjectStatus.COMPLETED, ProjectStatus.EXECUTING, ProjectStatus.KILLED},
    ProjectStatus.PAUSED: {ProjectStatus.IDEA, ProjectStatus.VALIDATING, ProjectStatus.PLANNING, ProjectStatus.EXECUTING, ProjectStatus.KILLED},
    ProjectStatus.COMPLETED: set(),
    ProjectStatus.SCRAPPED: set(),
    ProjectStatus.KILLED: set(),
}


def can_transition_project_status(current: ProjectStatus, target: ProjectStatus) -> bool:
    return target in PROJECT_STATE_TRANSITION_RULES.get(current, set())
```

---

## 35.10 Snapshot vs Provenance

`StateStore` e `Provenance` sono collegati ma non identici.

| Sistema | Scopo |
|---|---|
| `StateStore` | Stato runtime corrente e recovery |
| `Provenance` | Audit trail formale delle decisioni e operazioni importanti |
| `TaskStore` | Log e stato specifico dei task |
| `CommandStore` | Log dei comandi ricevuti |

Regola:

```text
StateStore salva “dove siamo”.
Provenance salva “perché e con quale decisione ci siamo arrivati”.
```

---

## 35.11 Regole operative StateStore

```text
1. Ogni progetto attivo ha un proprio .agents/runtime/state.json.
2. Il Centro di Comando ha un proprio centro-di-comando/runtime/state.json.
3. Ogni modifica di stato genera snapshot JSON.
4. Ogni modifica rilevante genera anche StateEvent JSONL.
5. Le scritture snapshot devono essere atomiche.
6. Nessuno stato operativo vive solo in memoria.
7. RuntimeState non sostituisce Provenance.
8. RuntimeState serve per ripresa, checkpoint e orchestrazione.
9. Provenance serve per audit, decisioni e accountability.
```

---

## 35.12 Stato del punto implementato

| Punto runtime | Stato |
|---|---|
| Dove salva lo stato | Implementato |
| `RuntimePaths` | Implementato |
| `RuntimeState` | Implementato |
| `WorkflowRuntimeState` | Implementato |
| `ApprovalRuntimeState` | Implementato |
| `StateEvent` | Implementato |
| `StateStore` protocol | Implementato |
| `JsonStateStore` | Implementato |
| Snapshot JSON atomico | Implementato |
| Event log JSONL append-only | Implementato |
| `StateStoreFactory` | Implementata |
| Integrazione Caesar runtime | Implementata |
| Regole transizione ProjectStatus | Implementate |

```text
┌─ LA DECISIONE ─────────────────────────────────────────────────┐
│ Scelta: Usare StateStore come fonte runtime dello stato corrente │
│ Perché: Caesar deve poter salvare, leggere e riprendere ogni workflow │
└────────────────────────────────────────────────────────────────┘
```


---

## 36. Runtime Execution Layer — Workflow Resume Protocol

Questa sezione implementa il quinto punto del runtime: **come Caesar riprende un workflow interrotto**.

Obiettivo:

```text
Interruzione / pausa / crash / attesa approvazione
↓
StateStore + WorkflowCheckpoint
↓
ResumeDecision
↓
Ripresa sicura dal prossimo step corretto
```

Regola chiave:

```text
Caesar non riprende mai un workflow “a memoria”.
Caesar riprende solo da StateStore + ultimo checkpoint valido.
```

---

## 36.1 Principio di Resume

Un workflow può interrompersi per:

- attesa approvazione utente;
- pausa manuale;
- crash runtime;
- errore task;
- blocco compliance/rischio;
- kill condition;
- chiusura applicazione;
- mancanza dati;
- richiesta chiarimento.

La ripresa deve determinare:

1. quale workflow era attivo;
2. quale step era corrente;
3. quale task era aperto;
4. se serve approvazione;
5. se esiste un errore bloccante;
6. se il piano è ancora valido;
7. quale azione è sicura adesso.

---

## 36.2 Resume Status e Policy

```python
class WorkflowRunStatus(str, Enum):
    NOT_STARTED = "NOT_STARTED"
    RUNNING = "RUNNING"
    WAITING_APPROVAL = "WAITING_APPROVAL"
    WAITING_CLARIFICATION = "WAITING_CLARIFICATION"
    PAUSED = "PAUSED"
    INTERRUPTED = "INTERRUPTED"
    BLOCKED = "BLOCKED"
    FAILED = "FAILED"
    COMPLETED = "COMPLETED"
    KILLED = "KILLED"


class ResumePolicy(str, Enum):
    AUTO_RESUME_SAFE = "AUTO_RESUME_SAFE"
    ASK_USER_BEFORE_RESUME = "ASK_USER_BEFORE_RESUME"
    REQUIRE_APPROVAL = "REQUIRE_APPROVAL"
    REQUIRE_CLARIFICATION = "REQUIRE_CLARIFICATION"
    BLOCK_RESUME = "BLOCK_RESUME"
    REBUILD_FROM_STATE = "REBUILD_FROM_STATE"


class ResumeDecisionType(str, Enum):
    RESUME_NOW = "RESUME_NOW"
    ASK_USER = "ASK_USER"
    WAIT_FOR_APPROVAL = "WAIT_FOR_APPROVAL"
    WAIT_FOR_CLARIFICATION = "WAIT_FOR_CLARIFICATION"
    BLOCKED = "BLOCKED"
    RECONSTRUCT = "RECONSTRUCT"
    NO_ACTIVE_WORKFLOW = "NO_ACTIVE_WORKFLOW"
```

---

## 36.3 WorkflowCheckpoint

Un checkpoint è un punto di ripresa persistente.

```python
@dataclass
class WorkflowCheckpoint:
    checkpoint_id: str
    project_id: str | None
    workflow_name: str
    workflow_status: WorkflowRunStatus
    current_step: str
    cursor: int
    created_at: str
    updated_at: str
    command_id: str | None = None
    task_id: str | None = None
    approval_id: str | None = None
    routing_mode: str | None = None
    target_agent: str | None = None
    target_department: str | None = None
    state_snapshot: dict[str, Any] = field(default_factory=dict)
    resume_instruction: str = ""
    safe_to_auto_resume: bool = False
    requires_user_approval: bool = False
    requires_user_clarification: bool = False
    block_reason: str | None = None
    idempotency_key: str = ""

    def to_dict(self) -> dict[str, Any]:
        data = asdict(self)
        data["workflow_status"] = self.workflow_status.value
        return data
```

---

## 36.4 CheckpointStore

I checkpoint vengono salvati in JSONL append-only.

Path:

```text
[progetto]/.agents/runtime/workflow-checkpoints.jsonl
centro-di-comando/runtime/workflow-checkpoints.jsonl
```

```python
class CheckpointStore(Protocol):
    def append(self, checkpoint: WorkflowCheckpoint) -> None:
        ...

    def latest(self, project_id: str | None = None, workflow_name: str | None = None) -> WorkflowCheckpoint | None:
        ...


@dataclass
class JsonlCheckpointStore:
    path: Path

    def append(self, checkpoint: WorkflowCheckpoint) -> None:
        self.path.parent.mkdir(parents=True, exist_ok=True)
        if not checkpoint.idempotency_key:
            checkpoint.idempotency_key = self.make_checkpoint_idempotency_key(checkpoint)
        with self.path.open("a", encoding="utf-8") as f:
            f.write(json.dumps(checkpoint.to_dict(), ensure_ascii=False) + "\n")

    def latest(self, project_id: str | None = None, workflow_name: str | None = None) -> WorkflowCheckpoint | None:
        if not self.path.exists():
            return None

        latest_raw: dict[str, Any] | None = None
        for line in self.path.read_text(encoding="utf-8").splitlines():
            if not line.strip():
                continue
            raw = json.loads(line)
            if project_id is not None and raw.get("project_id") != project_id:
                continue
            if workflow_name is not None and raw.get("workflow_name") != workflow_name:
                continue
            latest_raw = raw

        if latest_raw is None:
            return None
        return self._checkpoint_from_dict(latest_raw)

    @staticmethod
    def make_checkpoint_idempotency_key(checkpoint: WorkflowCheckpoint) -> str:
        base = "|".join([
            checkpoint.project_id or "NO_PROJECT",
            checkpoint.workflow_name,
            checkpoint.current_step,
            str(checkpoint.cursor),
            checkpoint.workflow_status.value,
        ])
        return hashlib.sha256(base.encode("utf-8")).hexdigest()

    @staticmethod
    def _checkpoint_from_dict(raw: dict[str, Any]) -> WorkflowCheckpoint:
        return WorkflowCheckpoint(
            checkpoint_id=raw["checkpoint_id"],
            project_id=raw.get("project_id"),
            workflow_name=raw["workflow_name"],
            workflow_status=WorkflowRunStatus(raw["workflow_status"]),
            current_step=raw["current_step"],
            cursor=raw["cursor"],
            created_at=raw["created_at"],
            updated_at=raw["updated_at"],
            command_id=raw.get("command_id"),
            task_id=raw.get("task_id"),
            approval_id=raw.get("approval_id"),
            routing_mode=raw.get("routing_mode"),
            target_agent=raw.get("target_agent"),
            target_department=raw.get("target_department"),
            state_snapshot=raw.get("state_snapshot", {}),
            resume_instruction=raw.get("resume_instruction", ""),
            safe_to_auto_resume=raw.get("safe_to_auto_resume", False),
            requires_user_approval=raw.get("requires_user_approval", False),
            requires_user_clarification=raw.get("requires_user_clarification", False),
            block_reason=raw.get("block_reason"),
            idempotency_key=raw.get("idempotency_key", ""),
        )
```

---

## 36.5 CheckpointFactory

`CheckpointFactory` crea checkpoint da stato, task e routing correnti.

```python
@dataclass
class CheckpointFactory:
    def create_checkpoint(
        self,
        runtime_state: RuntimeState,
        workflow_name: str,
        current_step: str,
        cursor: int,
        status: WorkflowRunStatus,
        command_id: str | None = None,
        task: RuntimeTask | None = None,
        routing_decision: RoutingDecision | None = None,
        approval_id: str | None = None,
        resume_instruction: str = "",
    ) -> WorkflowCheckpoint:
        now = datetime.now(timezone.utc).isoformat()
        project_id = runtime_state.project_state.project_id if runtime_state.project_state else None

        checkpoint = WorkflowCheckpoint(
            checkpoint_id=f"chk_{uuid.uuid4().hex[:12]}",
            project_id=project_id,
            workflow_name=workflow_name,
            workflow_status=status,
            current_step=current_step,
            cursor=cursor,
            created_at=now,
            updated_at=now,
            command_id=command_id,
            task_id=task.task_id if task else None,
            approval_id=approval_id,
            routing_mode=routing_decision.routing_mode.value if routing_decision else None,
            target_agent=routing_decision.target_agent if routing_decision else (task.assigned_to if task else None),
            target_department=routing_decision.target_department if routing_decision else (task.department if task else None),
            state_snapshot=runtime_state.to_dict(),
            resume_instruction=resume_instruction or self.default_resume_instruction(status),
            safe_to_auto_resume=self.is_safe_to_auto_resume(status, task),
            requires_user_approval=status == WorkflowRunStatus.WAITING_APPROVAL,
            requires_user_clarification=status == WorkflowRunStatus.WAITING_CLARIFICATION,
            block_reason=runtime_state.workflow_state.block_reason if runtime_state.workflow_state else None,
        )
        checkpoint.idempotency_key = JsonlCheckpointStore.make_checkpoint_idempotency_key(checkpoint)
        return checkpoint

    @staticmethod
    def is_safe_to_auto_resume(status: WorkflowRunStatus, task: RuntimeTask | None) -> bool:
        if status not in {WorkflowRunStatus.RUNNING, WorkflowRunStatus.INTERRUPTED}:
            return False
        if task is None:
            return False
        if task.requires_approval:
            return False
        if task.risk_level in APPROVAL_REQUIRED_FOR:
            return False
        if task.status in {TaskStatus.BLOCKED, TaskStatus.FAILED, TaskStatus.WAITING_APPROVAL}:
            return False
        return task.risk_level in {ActionLevel.A0, ActionLevel.A1}

    @staticmethod
    def default_resume_instruction(status: WorkflowRunStatus) -> str:
        instructions = {
            WorkflowRunStatus.RUNNING: "Riprendere dallo step corrente se il task è sicuro",
            WorkflowRunStatus.WAITING_APPROVAL: "Mostrare richiesta approvazione all’utente",
            WorkflowRunStatus.WAITING_CLARIFICATION: "Chiedere chiarimento all’utente",
            WorkflowRunStatus.PAUSED: "Chiedere all’utente se vuole riprendere",
            WorkflowRunStatus.INTERRUPTED: "Valutare checkpoint e riprendere solo se sicuro",
            WorkflowRunStatus.BLOCKED: "Non riprendere finché il blocco non viene risolto dall’utente",
            WorkflowRunStatus.FAILED: "Passare a ErrorManager prima del resume",
            WorkflowRunStatus.COMPLETED: "Nessuna ripresa necessaria",
            WorkflowRunStatus.KILLED: "Ripresa vietata: progetto killed",
            WorkflowRunStatus.NOT_STARTED: "Avviare workflow dal primo step",
        }
        return instructions[status]
```

---

## 36.6 ResumeDecision

```python
@dataclass
class ResumeDecision:
    decision_type: ResumeDecisionType
    project_id: str | None
    workflow_name: str | None
    checkpoint_id: str | None
    resume_from_step: str | None
    resume_cursor: int | None
    task_id: str | None
    target_agent: str | None
    target_department: str | None
    reason: str
    requires_user_action: bool = False
    user_prompt: str | None = None
    safe_to_resume: bool = False
    metadata: dict[str, Any] = field(default_factory=dict)

    def is_executable(self) -> bool:
        return self.decision_type == ResumeDecisionType.RESUME_NOW and self.safe_to_resume
```

---

## 36.7 WorkflowResumer

`WorkflowResumer` decide se e come riprendere.

```python
@dataclass
class WorkflowResumer:
    state_store: StateStore
    checkpoint_store: CheckpointStore

    def decide_resume(
        self,
        project_id: str | None = None,
        workflow_name: str | None = None,
    ) -> ResumeDecision:
        state = self.state_store.load()
        checkpoint = self.checkpoint_store.latest(project_id=project_id, workflow_name=workflow_name)

        if state is None and checkpoint is None:
            return ResumeDecision(
                decision_type=ResumeDecisionType.NO_ACTIVE_WORKFLOW,
                project_id=project_id,
                workflow_name=workflow_name,
                checkpoint_id=None,
                resume_from_step=None,
                resume_cursor=None,
                task_id=None,
                target_agent=None,
                target_department=None,
                reason="Nessuno stato o checkpoint trovato",
            )

        if checkpoint is None:
            return ResumeDecision(
                decision_type=ResumeDecisionType.RECONSTRUCT,
                project_id=project_id,
                workflow_name=workflow_name,
                checkpoint_id=None,
                resume_from_step=None,
                resume_cursor=None,
                task_id=None,
                target_agent=None,
                target_department=None,
                reason="StateStore esiste ma manca checkpoint: ricostruire dal RuntimeState",
                requires_user_action=False,
                safe_to_resume=False,
            )

        if checkpoint.workflow_status == WorkflowRunStatus.KILLED:
            return self._blocked(checkpoint, "Workflow killed: ripresa vietata")

        if checkpoint.workflow_status == WorkflowRunStatus.COMPLETED:
            return ResumeDecision(
                decision_type=ResumeDecisionType.NO_ACTIVE_WORKFLOW,
                project_id=checkpoint.project_id,
                workflow_name=checkpoint.workflow_name,
                checkpoint_id=checkpoint.checkpoint_id,
                resume_from_step=checkpoint.current_step,
                resume_cursor=checkpoint.cursor,
                task_id=checkpoint.task_id,
                target_agent=checkpoint.target_agent,
                target_department=checkpoint.target_department,
                reason="Workflow già completato",
            )

        if checkpoint.workflow_status == WorkflowRunStatus.BLOCKED:
            return self._blocked(checkpoint, checkpoint.block_reason or "Workflow bloccato")

        if checkpoint.workflow_status == WorkflowRunStatus.FAILED:
            return ResumeDecision(
                decision_type=ResumeDecisionType.BLOCKED,
                project_id=checkpoint.project_id,
                workflow_name=checkpoint.workflow_name,
                checkpoint_id=checkpoint.checkpoint_id,
                resume_from_step=checkpoint.current_step,
                resume_cursor=checkpoint.cursor,
                task_id=checkpoint.task_id,
                target_agent="L16",
                target_department="D-DEFENSE",
                reason="Workflow fallito: richiede ErrorManager/Self-Healing prima della ripresa",
                requires_user_action=True,
                user_prompt="Il workflow è fallito. Vuoi attivare diagnosi L16 Self-Healing?",
                safe_to_resume=False,
            )

        if checkpoint.requires_user_approval or checkpoint.workflow_status == WorkflowRunStatus.WAITING_APPROVAL:
            return ResumeDecision(
                decision_type=ResumeDecisionType.WAIT_FOR_APPROVAL,
                project_id=checkpoint.project_id,
                workflow_name=checkpoint.workflow_name,
                checkpoint_id=checkpoint.checkpoint_id,
                resume_from_step=checkpoint.current_step,
                resume_cursor=checkpoint.cursor,
                task_id=checkpoint.task_id,
                target_agent="Caesar",
                target_department="CAESAR",
                reason="Workflow in attesa di approvazione utente",
                requires_user_action=True,
                user_prompt="Serve approvazione per continuare. Vuoi APPROVE, REVISE, PAUSE o SCRAP?",
                safe_to_resume=False,
            )

        if checkpoint.requires_user_clarification or checkpoint.workflow_status == WorkflowRunStatus.WAITING_CLARIFICATION:
            return ResumeDecision(
                decision_type=ResumeDecisionType.WAIT_FOR_CLARIFICATION,
                project_id=checkpoint.project_id,
                workflow_name=checkpoint.workflow_name,
                checkpoint_id=checkpoint.checkpoint_id,
                resume_from_step=checkpoint.current_step,
                resume_cursor=checkpoint.cursor,
                task_id=checkpoint.task_id,
                target_agent="Caesar",
                target_department="CAESAR",
                reason="Workflow in attesa di chiarimento utente",
                requires_user_action=True,
                user_prompt="Serve un chiarimento per continuare il workflow.",
                safe_to_resume=False,
            )

        if checkpoint.workflow_status == WorkflowRunStatus.PAUSED:
            return ResumeDecision(
                decision_type=ResumeDecisionType.ASK_USER,
                project_id=checkpoint.project_id,
                workflow_name=checkpoint.workflow_name,
                checkpoint_id=checkpoint.checkpoint_id,
                resume_from_step=checkpoint.current_step,
                resume_cursor=checkpoint.cursor,
                task_id=checkpoint.task_id,
                target_agent=checkpoint.target_agent,
                target_department=checkpoint.target_department,
                reason="Workflow pausato manualmente",
                requires_user_action=True,
                user_prompt="Il workflow è in pausa. Vuoi riprenderlo da qui?",
                safe_to_resume=False,
            )

        if checkpoint.safe_to_auto_resume:
            return ResumeDecision(
                decision_type=ResumeDecisionType.RESUME_NOW,
                project_id=checkpoint.project_id,
                workflow_name=checkpoint.workflow_name,
                checkpoint_id=checkpoint.checkpoint_id,
                resume_from_step=checkpoint.current_step,
                resume_cursor=checkpoint.cursor,
                task_id=checkpoint.task_id,
                target_agent=checkpoint.target_agent,
                target_department=checkpoint.target_department,
                reason="Checkpoint marcato safe_to_auto_resume",
                requires_user_action=False,
                safe_to_resume=True,
            )

        return ResumeDecision(
            decision_type=ResumeDecisionType.ASK_USER,
            project_id=checkpoint.project_id,
            workflow_name=checkpoint.workflow_name,
            checkpoint_id=checkpoint.checkpoint_id,
            resume_from_step=checkpoint.current_step,
            resume_cursor=checkpoint.cursor,
            task_id=checkpoint.task_id,
            target_agent=checkpoint.target_agent,
            target_department=checkpoint.target_department,
            reason="Checkpoint non bloccato ma non sicuro per auto-resume",
            requires_user_action=True,
            user_prompt="Posso riprendere il workflow dall’ultimo checkpoint?",
            safe_to_resume=False,
        )

    @staticmethod
    def _blocked(checkpoint: WorkflowCheckpoint, reason: str) -> ResumeDecision:
        return ResumeDecision(
            decision_type=ResumeDecisionType.BLOCKED,
            project_id=checkpoint.project_id,
            workflow_name=checkpoint.workflow_name,
            checkpoint_id=checkpoint.checkpoint_id,
            resume_from_step=checkpoint.current_step,
            resume_cursor=checkpoint.cursor,
            task_id=checkpoint.task_id,
            target_agent=checkpoint.target_agent,
            target_department=checkpoint.target_department,
            reason=reason,
            requires_user_action=True,
            user_prompt="Il workflow è bloccato. Serve decisione esplicita dell’utente.",
            safe_to_resume=False,
        )
```

---

## 36.8 ResumeExecutor

`ResumeExecutor` non esegue direttamente azioni esterne.  
Riporta il sistema al punto operativo corretto generando un task o una richiesta utente.

```python
@dataclass
class ResumeExecutor:
    task_factory: TaskFactory
    task_queue: TaskQueue

    def execute_resume(
        self,
        resume_decision: ResumeDecision,
        command: Command,
        routing_decision: RoutingDecision | None = None,
    ) -> RuntimeTask | None:
        if resume_decision.decision_type == ResumeDecisionType.NO_ACTIVE_WORKFLOW:
            return None

        if resume_decision.decision_type in {
            ResumeDecisionType.ASK_USER,
            ResumeDecisionType.WAIT_FOR_APPROVAL,
            ResumeDecisionType.WAIT_FOR_CLARIFICATION,
            ResumeDecisionType.BLOCKED,
        }:
            synthetic_decision = RoutingDecision(
                command_id=command.command_id,
                routing_mode=RoutingMode.CLARIFICATION_REQUIRED if resume_decision.requires_user_action else RoutingMode.NO_ROUTE,
                target_department="CAESAR",
                target_agent="Caesar",
                workflow_name=resume_decision.workflow_name,
                next_step=resume_decision.user_prompt or resume_decision.reason,
                confidence=1.0,
                confidence_label=RouteConfidence.DETERMINISTIC,
                reason=resume_decision.reason,
                requires_user_clarification=resume_decision.requires_user_action,
                clarification_question=resume_decision.user_prompt,
                blocked=resume_decision.decision_type == ResumeDecisionType.BLOCKED,
                block_reason=resume_decision.reason if resume_decision.decision_type == ResumeDecisionType.BLOCKED else None,
            )
            task = self.task_factory.create_task(TaskCreationRequest(command=command, routing_decision=synthetic_decision))
            self.task_queue.add(task)
            return task

        if resume_decision.decision_type == ResumeDecisionType.RESUME_NOW:
            synthetic_decision = routing_decision or RoutingDecision(
                command_id=command.command_id,
                routing_mode=RoutingMode.PLAN_BASED,
                target_department=resume_decision.target_department,
                target_agent=resume_decision.target_agent,
                workflow_name=resume_decision.workflow_name,
                next_step=resume_decision.resume_from_step or "Riprendere workflow",
                confidence=1.0,
                confidence_label=RouteConfidence.DETERMINISTIC,
                reason=resume_decision.reason,
            )
            task = self.task_factory.create_task(TaskCreationRequest(command=command, routing_decision=synthetic_decision))
            self.task_queue.add(task)
            return task

        return None
```

---

## 36.9 Integrazione con Caesar Runtime

```python
@dataclass
class CaesarResumableRuntime:
    command_receiver: CommandReceiver
    router: CaesarRouter
    task_factory: TaskFactory
    task_queue: TaskQueue
    state_store: StateStore
    checkpoint_store: CheckpointStore
    checkpoint_factory: CheckpointFactory
    workflow_resumer: WorkflowResumer
    resume_executor: ResumeExecutor

    def checkpoint_current_state(
        self,
        runtime_state: RuntimeState,
        workflow_name: str,
        current_step: str,
        cursor: int,
        status: WorkflowRunStatus,
        command_id: str | None = None,
        task: RuntimeTask | None = None,
        routing_decision: RoutingDecision | None = None,
        approval_id: str | None = None,
    ) -> WorkflowCheckpoint:
        checkpoint = self.checkpoint_factory.create_checkpoint(
            runtime_state=runtime_state,
            workflow_name=workflow_name,
            current_step=current_step,
            cursor=cursor,
            status=status,
            command_id=command_id,
            task=task,
            routing_decision=routing_decision,
            approval_id=approval_id,
        )
        self.checkpoint_store.append(checkpoint)
        return checkpoint

    def resume_workflow(
        self,
        raw_text: str,
        context: CommandContext,
        project_id: str | None = None,
        workflow_name: str | None = None,
    ) -> tuple[Command, ResumeDecision, RuntimeTask | None]:
        command = self.command_receiver.receive(raw_text=raw_text, context=context, source=CommandSource.CHAT)
        resume_decision = self.workflow_resumer.decide_resume(project_id=project_id, workflow_name=workflow_name)
        task = self.resume_executor.execute_resume(resume_decision=resume_decision, command=command)
        return command, resume_decision, task
```

---

## 36.10 Quando creare checkpoint

Caesar deve creare checkpoint:

```text
1. Dopo ricezione comando valido.
2. Dopo RoutingDecision.
3. Dopo creazione Task.
4. Prima di ogni richiesta approvazione.
5. Dopo ogni decisione utente.
6. Prima di eseguire task A1+.
7. Dopo completamento task.
8. Quando un task fallisce.
9. Quando un workflow viene pausato.
10. Quando un workflow viene bloccato, killed o completato.
```

---

## 36.11 Regole operative Resume

```text
1. Caesar riprende solo da StateStore + ultimo WorkflowCheckpoint valido.
2. Workflow KILLED non può essere ripreso.
3. Workflow COMPLETED non viene ripreso: può solo generare review.
4. Workflow BLOCKED richiede decisione utente.
5. Workflow FAILED passa prima da ErrorManager o L16 Self-Healing.
6. Workflow WAITING_APPROVAL ripresenta la richiesta utente.
7. Workflow WAITING_CLARIFICATION chiede chiarimento.
8. Workflow PAUSED chiede conferma prima di riprendere.
9. Auto-resume è consentito solo per task A0/A1 senza approval pendente.
10. Nessuna azione A2+ viene ripresa automaticamente.
```

---

## 36.12 Esempi Resume

### Caso A — Workflow in attesa approvazione

```text
checkpoint.workflow_status = WAITING_APPROVAL
```

Output:

```text
ResumeDecisionType = WAIT_FOR_APPROVAL
Caesar mostra di nuovo la richiesta: APPROVE / REVISE / PAUSE / SCRAP
```

### Caso B — Crash durante analisi A0

```text
checkpoint.workflow_status = INTERRUPTED
checkpoint.safe_to_auto_resume = True
task.risk_level = A0
```

Output:

```text
ResumeDecisionType = RESUME_NOW
Caesar ricrea task e riprende dallo step salvato
```

### Caso C — Crash prima di file operation A2

```text
task.risk_level = A2
```

Output:

```text
ResumeDecisionType = ASK_USER oppure WAIT_FOR_APPROVAL
Nessuna modifica filesystem automatica
```

### Caso D — Workflow fallito

```text
checkpoint.workflow_status = FAILED
```

Output:

```text
ResumeDecisionType = BLOCKED
target_agent = L16
target_department = D-DEFENSE
```

---

## 36.13 Stato del punto implementato

| Punto runtime | Stato |
|---|---|
| Come riprende un workflow interrotto | Implementato |
| `WorkflowCheckpoint` | Implementato |
| `CheckpointStore` | Implementato |
| `JsonlCheckpointStore` | Implementato |
| `CheckpointFactory` | Implementata |
| `ResumePolicy` | Implementata |
| `ResumeDecision` | Implementata |
| `WorkflowResumer` | Implementato |
| `ResumeExecutor` | Implementato |
| Integrazione Caesar Runtime | Implementata |
| Regole auto-resume A0/A1 | Implementate |
| Blocco auto-resume A2+ | Implementato |

```text
┌─ LA DECISIONE ─────────────────────────────────────────────────┐
│ Scelta: Riprendere workflow solo da StateStore + checkpoint valido │
│ Perché: Evita azioni duplicate, salti di fase e riprese non autorizzate │
└────────────────────────────────────────────────────────────────┘
```


---

## 37. Runtime Execution Layer — Error Handling Protocol

Questa sezione implementa il sesto punto del runtime: **come Caesar gestisce errori**.

Obiettivo:

```text
Errore runtime / task / filesystem / validazione / agente
↓
ErrorEvent
↓
ErrorManager
↓
RetryPolicy o RollbackPlan o Escalation
↓
StateStore + Provenance + Checkpoint
```

Regola chiave:

```text
Caesar non ignora mai un errore operativo.
Ogni errore rilevante diventa ErrorEvent tracciato e produce una decisione esplicita.
```

---

## 37.1 Principio di gestione errori

Gli errori vengono classificati per:

- categoria;
- severità;
- recuperabilità;
- rischio azione;
- necessità di approvazione;
- possibilità di retry;
- necessità di rollback;
- necessità di escalation.

Caesar può fare retry automatico solo su errori sicuri, temporanei e non distruttivi.

---

## 37.2 Error Taxonomy

```python
class ErrorCategory(str, Enum):
    COMMAND = "COMMAND"
    ROUTING = "ROUTING"
    TASK_CREATION = "TASK_CREATION"
    TASK_EXECUTION = "TASK_EXECUTION"
    VALIDATION = "VALIDATION"
    APPROVAL = "APPROVAL"
    FILESYSTEM = "FILESYSTEM"
    STATESTORE = "STATESTORE"
    CHECKPOINT = "CHECKPOINT"
    AGENT_COMMUNICATION = "AGENT_COMMUNICATION"
    MODEL_OUTPUT = "MODEL_OUTPUT"
    BUDGET = "BUDGET"
    COMPLIANCE = "COMPLIANCE"
    SECURITY = "SECURITY"
    UNKNOWN = "UNKNOWN"


class ErrorSeverity(str, Enum):
    INFO = "INFO"
    WARNING = "WARNING"
    RECOVERABLE = "RECOVERABLE"
    BLOCKING = "BLOCKING"
    CRITICAL = "CRITICAL"
    CATASTROPHIC = "CATASTROPHIC"


class ErrorRecoverability(str, Enum):
    AUTO_RETRYABLE = "AUTO_RETRYABLE"
    RETRY_WITH_USER_APPROVAL = "RETRY_WITH_USER_APPROVAL"
    ROLLBACK_REQUIRED = "ROLLBACK_REQUIRED"
    ESCALATION_REQUIRED = "ESCALATION_REQUIRED"
    NON_RECOVERABLE = "NON_RECOVERABLE"


class ErrorResolutionStatus(str, Enum):
    OPEN = "OPEN"
    RETRYING = "RETRYING"
    RESOLVED = "RESOLVED"
    ROLLED_BACK = "ROLLED_BACK"
    ESCALATED = "ESCALATED"
    FAILED = "FAILED"
    IGNORED_BY_USER = "IGNORED_BY_USER"
```

---

## 37.3 ErrorEvent

```python
@dataclass
class ErrorEvent:
    error_id: str
    timestamp: str
    category: ErrorCategory
    severity: ErrorSeverity
    recoverability: ErrorRecoverability
    message: str
    origin: str
    project_id: str | None = None
    command_id: str | None = None
    task_id: str | None = None
    workflow_name: str | None = None
    checkpoint_id: str | None = None
    exception_type: str | None = None
    stack_hint: str | None = None
    retry_count: int = 0
    max_retries: int = 0
    status: ErrorResolutionStatus = ErrorResolutionStatus.OPEN
    requires_user_approval: bool = False
    safe_to_retry: bool = False
    rollback_available: bool = False
    escalation_target: str | None = None
    idempotency_key: str = ""
    metadata: dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data = asdict(self)
        data["category"] = self.category.value
        data["severity"] = self.severity.value
        data["recoverability"] = self.recoverability.value
        data["status"] = self.status.value
        return data
```

---

## 37.4 Retry Policy

```python
@dataclass(frozen=True)
class RetryPolicy:
    max_retries: int
    backoff_seconds: tuple[int, ...]
    retryable_categories: set[ErrorCategory]
    retryable_severities: set[ErrorSeverity]
    allow_retry_for_action_levels: set[ActionLevel]
    require_user_approval_after_attempt: int | None = None

    def can_retry(self, error: ErrorEvent, task: RuntimeTask | None = None) -> bool:
        if error.retry_count >= self.max_retries:
            return False
        if error.category not in self.retryable_categories:
            return False
        if error.severity not in self.retryable_severities:
            return False
        if task and task.risk_level not in self.allow_retry_for_action_levels:
            return False
        if task and task.requires_approval:
            return False
        return error.safe_to_retry

    def next_backoff(self, retry_count: int) -> int:
        if not self.backoff_seconds:
            return 0
        idx = min(retry_count, len(self.backoff_seconds) - 1)
        return self.backoff_seconds[idx]


DEFAULT_RETRY_POLICY = RetryPolicy(
    max_retries=2,
    backoff_seconds=(1, 3, 10),
    retryable_categories={
        ErrorCategory.MODEL_OUTPUT,
        ErrorCategory.AGENT_COMMUNICATION,
        ErrorCategory.TASK_EXECUTION,
        ErrorCategory.CHECKPOINT,
    },
    retryable_severities={
        ErrorSeverity.WARNING,
        ErrorSeverity.RECOVERABLE,
    },
    allow_retry_for_action_levels={ActionLevel.A0, ActionLevel.A1},
    require_user_approval_after_attempt=2,
)
```

---

## 37.5 Rollback Model

Il rollback è permesso solo se esiste una strategia sicura.

```python
class RollbackActionType(str, Enum):
    RESTORE_SNAPSHOT = "RESTORE_SNAPSHOT"
    RESTORE_FILE_BACKUP = "RESTORE_FILE_BACKUP"
    REVERT_TASK_STATUS = "REVERT_TASK_STATUS"
    REVERT_WORKFLOW_CURSOR = "REVERT_WORKFLOW_CURSOR"
    DEPRECATE_OUTPUT = "DEPRECATE_OUTPUT"
    MANUAL_ONLY = "MANUAL_ONLY"


@dataclass
class RollbackAction:
    action_id: str
    action_type: RollbackActionType
    description: str
    target_path: str | None = None
    backup_path: str | None = None
    target_task_id: str | None = None
    target_checkpoint_id: str | None = None
    requires_approval: bool = True
    risk_level: ActionLevel = ActionLevel.A2
    metadata: dict[str, Any] = field(default_factory=dict)


@dataclass
class RollbackPlan:
    rollback_id: str
    error_id: str
    project_id: str | None
    actions: list[RollbackAction]
    reason: str
    requires_user_approval: bool = True
    safe_to_execute: bool = False
```

Regola:

```text
Rollback A2+ richiede sempre approvazione esplicita.
Rollback distruttivo non è automatico.
Se non esiste backup o snapshot valido, rollback = MANUAL_ONLY.
```

---

## 37.6 ErrorDecision

```python
class ErrorDecisionType(str, Enum):
    IGNORE_SAFE_WARNING = "IGNORE_SAFE_WARNING"
    RETRY = "RETRY"
    REQUEST_USER_APPROVAL_FOR_RETRY = "REQUEST_USER_APPROVAL_FOR_RETRY"
    CREATE_ROLLBACK_PLAN = "CREATE_ROLLBACK_PLAN"
    EXECUTE_ROLLBACK_AFTER_APPROVAL = "EXECUTE_ROLLBACK_AFTER_APPROVAL"
    ESCALATE_TO_L16 = "ESCALATE_TO_L16"
    ESCALATE_TO_USER = "ESCALATE_TO_USER"
    KILL_WORKFLOW = "KILL_WORKFLOW"
    BLOCK_WORKFLOW = "BLOCK_WORKFLOW"


@dataclass
class ErrorDecision:
    decision_type: ErrorDecisionType
    error_id: str
    reason: str
    target_agent: str | None = None
    target_department: str | None = None
    retry_allowed: bool = False
    rollback_plan: RollbackPlan | None = None
    requires_user_action: bool = False
    user_prompt: str | None = None
    update_task_status_to: TaskStatus | None = None
    update_workflow_status_to: WorkflowRunStatus | None = None
```

---

## 37.7 Error Store

Gli errori vengono salvati in JSONL append-only.

Path:

```text
[progetto]/.agents/runtime/errors.jsonl
centro-di-comando/runtime/errors.jsonl
```

```python
class ErrorStore(Protocol):
    def append(self, error: ErrorEvent) -> None:
        ...

    def latest_open(self, project_id: str | None = None) -> ErrorEvent | None:
        ...


@dataclass
class JsonlErrorStore:
    path: Path

    def append(self, error: ErrorEvent) -> None:
        self.path.parent.mkdir(parents=True, exist_ok=True)
        if not error.idempotency_key:
            error.idempotency_key = self.make_error_idempotency_key(error)
        with self.path.open("a", encoding="utf-8") as f:
            f.write(json.dumps(error.to_dict(), ensure_ascii=False) + "\n")

    def latest_open(self, project_id: str | None = None) -> ErrorEvent | None:
        if not self.path.exists():
            return None
        latest_raw: dict[str, Any] | None = None
        for line in self.path.read_text(encoding="utf-8").splitlines():
            if not line.strip():
                continue
            raw = json.loads(line)
            if project_id is not None and raw.get("project_id") != project_id:
                continue
            if raw.get("status") == ErrorResolutionStatus.OPEN.value:
                latest_raw = raw
        if latest_raw is None:
            return None
        return self._error_from_dict(latest_raw)

    @staticmethod
    def make_error_idempotency_key(error: ErrorEvent) -> str:
        base = "|".join([
            error.project_id or "NO_PROJECT",
            error.command_id or "NO_COMMAND",
            error.task_id or "NO_TASK",
            error.category.value,
            error.message,
        ])
        return hashlib.sha256(base.encode("utf-8")).hexdigest()

    @staticmethod
    def _error_from_dict(raw: dict[str, Any]) -> ErrorEvent:
        return ErrorEvent(
            error_id=raw["error_id"],
            timestamp=raw["timestamp"],
            category=ErrorCategory(raw["category"]),
            severity=ErrorSeverity(raw["severity"]),
            recoverability=ErrorRecoverability(raw["recoverability"]),
            message=raw["message"],
            origin=raw["origin"],
            project_id=raw.get("project_id"),
            command_id=raw.get("command_id"),
            task_id=raw.get("task_id"),
            workflow_name=raw.get("workflow_name"),
            checkpoint_id=raw.get("checkpoint_id"),
            exception_type=raw.get("exception_type"),
            stack_hint=raw.get("stack_hint"),
            retry_count=raw.get("retry_count", 0),
            max_retries=raw.get("max_retries", 0),
            status=ErrorResolutionStatus(raw.get("status", "OPEN")),
            requires_user_approval=raw.get("requires_user_approval", False),
            safe_to_retry=raw.get("safe_to_retry", False),
            rollback_available=raw.get("rollback_available", False),
            escalation_target=raw.get("escalation_target"),
            idempotency_key=raw.get("idempotency_key", ""),
            metadata=raw.get("metadata", {}),
        )
```

---

## 37.8 Error Classifier

```python
@dataclass
class ErrorClassifier:
    def classify(
        self,
        error: Exception | str,
        category: ErrorCategory = ErrorCategory.UNKNOWN,
        origin: str = "Caesar",
        command: Command | None = None,
        task: RuntimeTask | None = None,
        workflow_name: str | None = None,
        checkpoint: WorkflowCheckpoint | None = None,
    ) -> ErrorEvent:
        message = str(error)
        severity = self.infer_severity(category, message, task)
        recoverability = self.infer_recoverability(category, severity, task)
        safe_to_retry = self.infer_safe_to_retry(category, severity, task)
        now = datetime.now(timezone.utc).isoformat()

        event = ErrorEvent(
            error_id=f"err_{uuid.uuid4().hex[:12]}",
            timestamp=now,
            category=category,
            severity=severity,
            recoverability=recoverability,
            message=message,
            origin=origin,
            project_id=task.project_id if task else (command.context.project_id if command else None),
            command_id=command.command_id if command else (task.command_id if task else None),
            task_id=task.task_id if task else None,
            workflow_name=workflow_name,
            checkpoint_id=checkpoint.checkpoint_id if checkpoint else None,
            exception_type=type(error).__name__ if not isinstance(error, str) else None,
            max_retries=DEFAULT_RETRY_POLICY.max_retries,
            safe_to_retry=safe_to_retry,
            rollback_available=self.infer_rollback_available(category, task),
            requires_user_approval=self.requires_user_approval(category, severity, task),
            escalation_target=self.infer_escalation_target(category, severity),
        )
        event.idempotency_key = JsonlErrorStore.make_error_idempotency_key(event)
        return event

    @staticmethod
    def infer_severity(category: ErrorCategory, message: str, task: RuntimeTask | None) -> ErrorSeverity:
        if category in {ErrorCategory.SECURITY, ErrorCategory.COMPLIANCE}:
            return ErrorSeverity.CRITICAL
        if category == ErrorCategory.BUDGET:
            return ErrorSeverity.BLOCKING
        if task and task.risk_level in {ActionLevel.A3, ActionLevel.A4}:
            return ErrorSeverity.BLOCKING
        if category in {ErrorCategory.MODEL_OUTPUT, ErrorCategory.AGENT_COMMUNICATION}:
            return ErrorSeverity.RECOVERABLE
        if category in {ErrorCategory.VALIDATION, ErrorCategory.ROUTING}:
            return ErrorSeverity.WARNING
        return ErrorSeverity.RECOVERABLE

    @staticmethod
    def infer_recoverability(category: ErrorCategory, severity: ErrorSeverity, task: RuntimeTask | None) -> ErrorRecoverability:
        if severity in {ErrorSeverity.CRITICAL, ErrorSeverity.CATASTROPHIC}:
            return ErrorRecoverability.ESCALATION_REQUIRED
        if category in {ErrorCategory.SECURITY, ErrorCategory.COMPLIANCE, ErrorCategory.BUDGET}:
            return ErrorRecoverability.ESCALATION_REQUIRED
        if task and task.risk_level in {ActionLevel.A2, ActionLevel.A3, ActionLevel.A4}:
            return ErrorRecoverability.RETRY_WITH_USER_APPROVAL
        if category == ErrorCategory.FILESYSTEM:
            return ErrorRecoverability.ROLLBACK_REQUIRED
        return ErrorRecoverability.AUTO_RETRYABLE

    @staticmethod
    def infer_safe_to_retry(category: ErrorCategory, severity: ErrorSeverity, task: RuntimeTask | None) -> bool:
        if severity not in {ErrorSeverity.WARNING, ErrorSeverity.RECOVERABLE}:
            return False
        if task and task.risk_level not in {ActionLevel.A0, ActionLevel.A1}:
            return False
        return category in {
            ErrorCategory.MODEL_OUTPUT,
            ErrorCategory.AGENT_COMMUNICATION,
            ErrorCategory.TASK_EXECUTION,
            ErrorCategory.CHECKPOINT,
            ErrorCategory.VALIDATION,
        }

    @staticmethod
    def infer_rollback_available(category: ErrorCategory, task: RuntimeTask | None) -> bool:
        if category == ErrorCategory.FILESYSTEM:
            return True
        if task and task.result_path:
            return True
        return False

    @staticmethod
    def requires_user_approval(category: ErrorCategory, severity: ErrorSeverity, task: RuntimeTask | None) -> bool:
        if severity in {ErrorSeverity.BLOCKING, ErrorSeverity.CRITICAL, ErrorSeverity.CATASTROPHIC}:
            return True
        if task and task.risk_level in APPROVAL_REQUIRED_FOR:
            return True
        return category in {ErrorCategory.FILESYSTEM, ErrorCategory.BUDGET, ErrorCategory.COMPLIANCE, ErrorCategory.SECURITY}

    @staticmethod
    def infer_escalation_target(category: ErrorCategory, severity: ErrorSeverity) -> str | None:
        if category in {ErrorCategory.SECURITY, ErrorCategory.COMPLIANCE, ErrorCategory.BUDGET}:
            return "Utente"
        if severity in {ErrorSeverity.BLOCKING, ErrorSeverity.CRITICAL, ErrorSeverity.CATASTROPHIC}:
            return "L16"
        return None
```

---

## 37.9 ErrorManager

```python
@dataclass
class ErrorManager:
    error_store: ErrorStore
    retry_policy: RetryPolicy = DEFAULT_RETRY_POLICY

    def handle_error(
        self,
        error: ErrorEvent,
        task: RuntimeTask | None = None,
    ) -> ErrorDecision:
        self.error_store.append(error)

        if error.severity == ErrorSeverity.INFO:
            return ErrorDecision(
                decision_type=ErrorDecisionType.IGNORE_SAFE_WARNING,
                error_id=error.error_id,
                reason="Evento informativo non bloccante",
            )

        if self.retry_policy.can_retry(error, task):
            error.status = ErrorResolutionStatus.RETRYING
            error.retry_count += 1
            self.error_store.append(error)
            return ErrorDecision(
                decision_type=ErrorDecisionType.RETRY,
                error_id=error.error_id,
                reason=f"Errore recuperabile: retry {error.retry_count}/{self.retry_policy.max_retries}",
                retry_allowed=True,
                update_task_status_to=TaskStatus.TODO if task else None,
            )

        if error.recoverability == ErrorRecoverability.RETRY_WITH_USER_APPROVAL:
            return ErrorDecision(
                decision_type=ErrorDecisionType.REQUEST_USER_APPROVAL_FOR_RETRY,
                error_id=error.error_id,
                reason="Retry possibile ma richiede approvazione utente",
                requires_user_action=True,
                user_prompt="Si è verificato un errore. Vuoi autorizzare un retry controllato?",
                update_task_status_to=TaskStatus.WAITING_APPROVAL if task else None,
            )

        if error.recoverability == ErrorRecoverability.ROLLBACK_REQUIRED or error.rollback_available:
            rollback_plan = self.create_rollback_plan(error, task)
            return ErrorDecision(
                decision_type=ErrorDecisionType.CREATE_ROLLBACK_PLAN,
                error_id=error.error_id,
                reason="Errore richiede rollback o ripristino controllato",
                rollback_plan=rollback_plan,
                requires_user_action=rollback_plan.requires_user_approval,
                user_prompt="È disponibile un piano di rollback. Vuoi approvarlo?",
                update_task_status_to=TaskStatus.BLOCKED if task else None,
            )

        if error.escalation_target == "L16":
            return ErrorDecision(
                decision_type=ErrorDecisionType.ESCALATE_TO_L16,
                error_id=error.error_id,
                reason="Errore bloccante: attivare L16 Self-Healing",
                target_agent="L16",
                target_department="D-DEFENSE",
                requires_user_action=True,
                user_prompt="Errore bloccante. Vuoi attivare L16 Self-Healing?",
                update_task_status_to=TaskStatus.BLOCKED if task else None,
                update_workflow_status_to=WorkflowRunStatus.FAILED,
            )

        if error.escalation_target == "Utente" or error.requires_user_approval:
            return ErrorDecision(
                decision_type=ErrorDecisionType.ESCALATE_TO_USER,
                error_id=error.error_id,
                reason="Errore richiede decisione esplicita dell’utente",
                target_agent="Caesar",
                target_department="CAESAR",
                requires_user_action=True,
                user_prompt="Serve una decisione esplicita per gestire questo errore.",
                update_task_status_to=TaskStatus.BLOCKED if task else None,
                update_workflow_status_to=WorkflowRunStatus.BLOCKED,
            )

        return ErrorDecision(
            decision_type=ErrorDecisionType.BLOCK_WORKFLOW,
            error_id=error.error_id,
            reason="Errore non recuperabile automaticamente",
            requires_user_action=True,
            user_prompt="Il workflow è stato bloccato per errore non recuperabile.",
            update_task_status_to=TaskStatus.BLOCKED if task else None,
            update_workflow_status_to=WorkflowRunStatus.BLOCKED,
        )

    @staticmethod
    def create_rollback_plan(error: ErrorEvent, task: RuntimeTask | None = None) -> RollbackPlan:
        actions: list[RollbackAction] = []

        if task and task.result_path:
            actions.append(RollbackAction(
                action_id=f"rb_act_{uuid.uuid4().hex[:12]}",
                action_type=RollbackActionType.DEPRECATE_OUTPUT,
                description="Deprecare output generato dal task fallito",
                target_path=task.result_path,
                requires_approval=True,
                risk_level=ActionLevel.A2,
            ))

        if error.category == ErrorCategory.FILESYSTEM:
            actions.append(RollbackAction(
                action_id=f"rb_act_{uuid.uuid4().hex[:12]}",
                action_type=RollbackActionType.MANUAL_ONLY,
                description="Verificare manualmente modifiche filesystem e ripristinare da backup se disponibile",
                requires_approval=True,
                risk_level=ActionLevel.A2,
            ))

        if not actions:
            actions.append(RollbackAction(
                action_id=f"rb_act_{uuid.uuid4().hex[:12]}",
                action_type=RollbackActionType.REVERT_TASK_STATUS,
                description="Riportare task a BLOCKED e attendere decisione utente",
                target_task_id=task.task_id if task else None,
                requires_approval=False,
                risk_level=ActionLevel.A0,
            ))

        return RollbackPlan(
            rollback_id=f"rollback_{uuid.uuid4().hex[:12]}",
            error_id=error.error_id,
            project_id=error.project_id,
            actions=actions,
            reason=f"Rollback generato per errore {error.error_id}",
            requires_user_approval=any(action.requires_approval for action in actions),
            safe_to_execute=all(action.risk_level in {ActionLevel.A0, ActionLevel.A1} for action in actions),
        )
```

---

## 37.10 Integrazione con StateStore, Checkpoint e Provenance

Quando un errore viene gestito:

```text
1. ErrorEvent viene scritto in ErrorStore.
2. Task viene aggiornato se necessario.
3. WorkflowRuntimeState viene aggiornato se necessario.
4. WorkflowCheckpoint viene creato con stato FAILED/BLOCKED/WAITING_APPROVAL.
5. ProvenanceEvent viene creato per errori bloccanti, rollback, escalation, budget, compliance e filesystem.
```

```python
@dataclass
class CaesarErrorRuntime:
    error_classifier: ErrorClassifier
    error_manager: ErrorManager
    state_store: StateStore
    checkpoint_factory: CheckpointFactory
    checkpoint_store: CheckpointStore

    def capture_and_handle_error(
        self,
        error: Exception | str,
        category: ErrorCategory,
        origin: str,
        command: Command | None = None,
        task: RuntimeTask | None = None,
        workflow_name: str | None = None,
        checkpoint: WorkflowCheckpoint | None = None,
    ) -> tuple[ErrorEvent, ErrorDecision]:
        error_event = self.error_classifier.classify(
            error=error,
            category=category,
            origin=origin,
            command=command,
            task=task,
            workflow_name=workflow_name,
            checkpoint=checkpoint,
        )

        decision = self.error_manager.handle_error(error_event, task=task)

        if task and decision.update_task_status_to:
            task.status = decision.update_task_status_to
            task.updated_at = datetime.now(timezone.utc).isoformat()
            task.metadata["last_error_id"] = error_event.error_id
            if hasattr(self.state_store, "update_task"):
                self.state_store.update_task(task)

        state = self.state_store.load()
        if state and state.workflow_state and decision.update_workflow_status_to:
            state.workflow_state.status = decision.update_workflow_status_to.value
            state.workflow_state.blocked = decision.update_workflow_status_to in {
                WorkflowRunStatus.BLOCKED,
                WorkflowRunStatus.FAILED,
            }
            state.workflow_state.block_reason = decision.reason
            self.state_store.update_workflow_state(state.workflow_state)

            checkpoint_status = decision.update_workflow_status_to
            new_checkpoint = self.checkpoint_factory.create_checkpoint(
                runtime_state=state,
                workflow_name=workflow_name or state.workflow_state.workflow_name,
                current_step=state.workflow_state.current_step,
                cursor=state.workflow_state.cursor,
                status=checkpoint_status,
                command_id=command.command_id if command else None,
                task=task,
                approval_id=state.workflow_state.waiting_for_approval_id,
                resume_instruction=decision.user_prompt or decision.reason,
            )
            self.checkpoint_store.append(new_checkpoint)

        return error_event, decision
```

---

## 37.11 Escalation Matrix

| Categoria | Severità | Azione |
|---|---|---|
| `MODEL_OUTPUT` | `RECOVERABLE` | Retry A0/A1 |
| `AGENT_COMMUNICATION` | `RECOVERABLE` | Retry A0/A1 |
| `VALIDATION` | `WARNING` | Correzione o richiesta chiarimento |
| `FILESYSTEM` | qualsiasi | RollbackPlan + approvazione |
| `BUDGET` | qualsiasi | Escalation utente |
| `COMPLIANCE` | qualsiasi | Hard stop + utente |
| `SECURITY` | qualsiasi | Hard stop + utente |
| `TASK_EXECUTION` | `BLOCKING` | L16 Self-Healing |
| `STATESTORE` | `BLOCKING` | Checkpoint + L16 |
| `UNKNOWN` | `CRITICAL` | Blocco workflow |

---

## 37.12 Regole operative Error Handling

```text
1. Ogni errore operativo diventa ErrorEvent.
2. Retry automatico solo per A0/A1, massimo 2 tentativi default.
3. Nessun retry automatico per A2, A3, A4.
4. Errori filesystem generano RollbackPlan.
5. Rollback A2+ richiede approvazione utente.
6. Errori budget, compliance e security vanno sempre in hard stop.
7. Errori bloccanti passano a L16 Self-Healing solo previa decisione utente se richiedono azioni A2+.
8. Ogni errore bloccante crea checkpoint FAILED o BLOCKED.
9. ErrorManager decide la risposta, ma non esegue azioni filesystem.
10. RollbackExecutor appartiene al futuro FileSystem Execution Layer.
```

---

## 37.13 Stato del punto implementato

| Punto runtime | Stato |
|---|---|
| Come gestisce errori | Implementato |
| `ErrorEvent` | Implementato |
| `RetryPolicy` | Implementata |
| `RollbackAction` | Implementata |
| `RollbackPlan` | Implementato |
| `ErrorDecision` | Implementata |
| `ErrorStore` | Implementato |
| `ErrorClassifier` | Implementato |
| `ErrorManager` | Implementato |
| Escalation L16/Utente | Implementata |
| Integrazione StateStore | Implementata |
| Integrazione Checkpoint | Implementata |
| Blocco retry A2+ | Implementato |

```text
┌─ LA DECISIONE ─────────────────────────────────────────────────┐
│ Scelta: Usare ErrorManager come unico punto di gestione errori runtime │
│ Perché: Ogni errore diventa tracciabile, recuperabile o escalation controllata │
└────────────────────────────────────────────────────────────────┘
```


---

## 38. Runtime Execution Layer — Agent Communication Protocol

Questa sezione implementa il settimo punto del runtime: **come un agente comunica con un altro**.

Obiettivo:

```text
Task / richiesta interna
↓
AgentMessage strutturato
↓
MessageBus append-only
↓
Inbox/Outbox agente
↓
Risposta, ABSTAIN, errore o escalation
```

Regola chiave:

```text
I Legionari non comunicano tramite prosa libera non strutturata.
Ogni scambio passa da AgentMessage e MessageBus.
```

---

## 38.1 Principio di comunicazione

La comunicazione tra agenti deve essere:

- strutturata;
- tracciabile;
- idempotente;
- collegata a task, command e workflow;
- salvata in append-only log;
- validabile;
- bloccabile in caso di `ABSTAIN`, errore o richiesta approvazione.

Caesar resta l’orchestratore principale.  
I Legionari possono inviare messaggi ad altri Legionari solo se il workflow o il task lo prevede.

---

## 38.2 Message Types

```python
class AgentMessageType(str, Enum):
    REQUEST = "REQUEST"
    RESPONSE = "RESPONSE"
    REVIEW_REQUEST = "REVIEW_REQUEST"
    REVIEW_RESPONSE = "REVIEW_RESPONSE"
    HANDOFF = "HANDOFF"
    STATUS_UPDATE = "STATUS_UPDATE"
    RESULT = "RESULT"
    ERROR = "ERROR"
    ABSTAIN = "ABSTAIN"
    APPROVAL_REQUIRED = "APPROVAL_REQUIRED"
    CLARIFICATION_REQUIRED = "CLARIFICATION_REQUIRED"
    CRITICAL_REVIEW_REQUEST = "CRITICAL_REVIEW_REQUEST"
    CRITICAL_REVIEW_RESPONSE = "CRITICAL_REVIEW_RESPONSE"
    HEARTBEAT = "HEARTBEAT"


class AgentMessageStatus(str, Enum):
    CREATED = "CREATED"
    QUEUED = "QUEUED"
    DELIVERED = "DELIVERED"
    READ = "READ"
    RESPONDED = "RESPONDED"
    FAILED = "FAILED"
    EXPIRED = "EXPIRED"
    BLOCKED = "BLOCKED"


class AgentMessagePriority(str, Enum):
    LOW = "LOW"
    NORMAL = "NORMAL"
    HIGH = "HIGH"
    URGENT = "URGENT"
```

---

## 38.3 AgentMessage

`AgentMessage` sostituisce l’uso libero di `InternalMessage` nei flussi tra agenti.

```python
@dataclass
class AgentMessage:
    message_id: str
    parent_id: str | None
    thread_id: str
    timestamp: str
    sender: str
    recipient: str
    message_type: AgentMessageType
    status: AgentMessageStatus
    priority: AgentMessagePriority
    intent: str
    payload: dict[str, Any]
    command_id: str | None = None
    task_id: str | None = None
    project_id: str | None = None
    workflow_name: str | None = None
    requires_response: bool = True
    response_to: str | None = None
    deadline_at: str | None = None
    idempotency_key: str = ""
    metadata: dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data = asdict(self)
        data["message_type"] = self.message_type.value
        data["status"] = self.status.value
        data["priority"] = self.priority.value
        return data
```

---

## 38.4 Message Envelope e Payload Contract

Ogni payload deve dichiarare almeno:

```python
REQUIRED_MESSAGE_PAYLOAD_KEYS = {
    AgentMessageType.REQUEST: {"request", "expected_output"},
    AgentMessageType.RESPONSE: {"response", "result_status"},
    AgentMessageType.REVIEW_REQUEST: {"artifact", "review_criteria"},
    AgentMessageType.REVIEW_RESPONSE: {"verdict", "issues", "recommendation"},
    AgentMessageType.HANDOFF: {"handoff_reason", "context", "next_owner"},
    AgentMessageType.STATUS_UPDATE: {"status", "summary"},
    AgentMessageType.RESULT: {"result", "acceptance_check"},
    AgentMessageType.ERROR: {"error_summary", "error_category"},
    AgentMessageType.ABSTAIN: {"reason", "missing_information"},
    AgentMessageType.APPROVAL_REQUIRED: {"decision_needed", "options"},
    AgentMessageType.CLARIFICATION_REQUIRED: {"question", "why_needed"},
    AgentMessageType.CRITICAL_REVIEW_REQUEST: {"artifact", "review_focus", "decision_context"},
    AgentMessageType.CRITICAL_REVIEW_RESPONSE: {"weakest_assumption", "main_risk", "better_alternative", "confidence", "should_block"},
    AgentMessageType.HEARTBEAT: {"status"},
}
```

---

## 38.5 MessageBus Protocol

```python
class MessageBus(Protocol):
    def publish(self, message: AgentMessage) -> None:
        ...

    def get_inbox(self, agent_id: str, status: AgentMessageStatus | None = None) -> list[AgentMessage]:
        ...

    def get_thread(self, thread_id: str) -> list[AgentMessage]:
        ...

    def mark_status(self, message_id: str, status: AgentMessageStatus) -> None:
        ...
```

---

## 38.6 JSONL MessageBus

Il bus locale default è append-only JSONL.  
Non cancella messaggi: aggiunge eventi di stato.

Path consigliato:

```text
[progetto]/.agents/runtime/messages.jsonl
centro-di-comando/runtime/messages.jsonl
```

```python
@dataclass
class JsonlMessageBus:
    path: Path

    def publish(self, message: AgentMessage) -> None:
        self.path.parent.mkdir(parents=True, exist_ok=True)
        if not message.idempotency_key:
            message.idempotency_key = self.make_message_idempotency_key(message)
        message.status = AgentMessageStatus.QUEUED
        self._append(message)

    def get_inbox(self, agent_id: str, status: AgentMessageStatus | None = None) -> list[AgentMessage]:
        messages = self._read_all()
        inbox = [m for m in messages if m.recipient == agent_id]
        if status is not None:
            inbox = [m for m in inbox if m.status == status]
        return inbox

    def get_thread(self, thread_id: str) -> list[AgentMessage]:
        return [m for m in self._read_all() if m.thread_id == thread_id]

    def mark_status(self, message_id: str, status: AgentMessageStatus) -> None:
        existing = next((m for m in reversed(self._read_all()) if m.message_id == message_id), None)
        if existing is None:
            return
        existing.status = status
        existing.timestamp = datetime.now(timezone.utc).isoformat()
        self._append(existing)

    def _append(self, message: AgentMessage) -> None:
        with self.path.open("a", encoding="utf-8") as f:
            f.write(json.dumps(message.to_dict(), ensure_ascii=False) + "\n")

    def _read_all(self) -> list[AgentMessage]:
        if not self.path.exists():
            return []
        messages: list[AgentMessage] = []
        for line in self.path.read_text(encoding="utf-8").splitlines():
            if line.strip():
                messages.append(self._message_from_dict(json.loads(line)))
        return messages

    @staticmethod
    def make_message_idempotency_key(message: AgentMessage) -> str:
        base = "|".join([
            message.thread_id,
            message.sender,
            message.recipient,
            message.message_type.value,
            message.intent,
            message.task_id or "NO_TASK",
        ])
        return hashlib.sha256(base.encode("utf-8")).hexdigest()

    @staticmethod
    def _message_from_dict(raw: dict[str, Any]) -> AgentMessage:
        return AgentMessage(
            message_id=raw["message_id"],
            parent_id=raw.get("parent_id"),
            thread_id=raw["thread_id"],
            timestamp=raw["timestamp"],
            sender=raw["sender"],
            recipient=raw["recipient"],
            message_type=AgentMessageType(raw["message_type"]),
            status=AgentMessageStatus(raw["status"]),
            priority=AgentMessagePriority(raw["priority"]),
            intent=raw["intent"],
            payload=raw.get("payload", {}),
            command_id=raw.get("command_id"),
            task_id=raw.get("task_id"),
            project_id=raw.get("project_id"),
            workflow_name=raw.get("workflow_name"),
            requires_response=raw.get("requires_response", True),
            response_to=raw.get("response_to"),
            deadline_at=raw.get("deadline_at"),
            idempotency_key=raw.get("idempotency_key", ""),
            metadata=raw.get("metadata", {}),
        )
```

---

## 38.7 MessageFactory

```python
@dataclass
class MessageFactory:
    def create(
        self,
        sender: str,
        recipient: str,
        message_type: AgentMessageType,
        intent: str,
        payload: dict[str, Any],
        command_id: str | None = None,
        task_id: str | None = None,
        project_id: str | None = None,
        workflow_name: str | None = None,
        parent_id: str | None = None,
        thread_id: str | None = None,
        response_to: str | None = None,
        priority: AgentMessagePriority = AgentMessagePriority.NORMAL,
        requires_response: bool = True,
        deadline_at: str | None = None,
    ) -> AgentMessage:
        now = datetime.now(timezone.utc).isoformat()
        message = AgentMessage(
            message_id=f"msg_{uuid.uuid4().hex[:12]}",
            parent_id=parent_id,
            thread_id=thread_id or f"thread_{uuid.uuid4().hex[:12]}",
            timestamp=now,
            sender=sender,
            recipient=recipient,
            message_type=message_type,
            status=AgentMessageStatus.CREATED,
            priority=priority,
            intent=intent,
            payload=payload,
            command_id=command_id,
            task_id=task_id,
            project_id=project_id,
            workflow_name=workflow_name,
            requires_response=requires_response,
            response_to=response_to,
            deadline_at=deadline_at,
        )
        message.idempotency_key = JsonlMessageBus.make_message_idempotency_key(message)
        return message

    def response(
        self,
        request_message: AgentMessage,
        sender: str,
        payload: dict[str, Any],
        message_type: AgentMessageType = AgentMessageType.RESPONSE,
        intent: str = "respond_to_request",
    ) -> AgentMessage:
        return self.create(
            sender=sender,
            recipient=request_message.sender,
            message_type=message_type,
            intent=intent,
            payload=payload,
            command_id=request_message.command_id,
            task_id=request_message.task_id,
            project_id=request_message.project_id,
            workflow_name=request_message.workflow_name,
            parent_id=request_message.message_id,
            thread_id=request_message.thread_id,
            response_to=request_message.message_id,
            priority=request_message.priority,
            requires_response=False,
        )
```

---

## 38.8 Message Validation

```python
@dataclass
class MessageValidationResult:
    valid: bool
    errors: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)
    blocking: bool = False


def validate_agent_message(message: AgentMessage) -> MessageValidationResult:
    errors: list[str] = []
    warnings: list[str] = []

    if not message.message_id:
        errors.append("message_id mancante")
    if not message.thread_id:
        errors.append("thread_id mancante")
    if not message.sender:
        errors.append("sender mancante")
    if not message.recipient:
        errors.append("recipient mancante")
    if not message.intent:
        errors.append("intent mancante")
    if not message.idempotency_key:
        errors.append("idempotency_key mancante")

    required_keys = REQUIRED_MESSAGE_PAYLOAD_KEYS.get(message.message_type, set())
    missing = [key for key in required_keys if key not in message.payload]
    if missing:
        errors.append(f"payload incompleto: mancano {missing}")

    if message.message_type == AgentMessageType.RESPONSE and not message.response_to:
        warnings.append("RESPONSE senza response_to")

    if message.message_type == AgentMessageType.ABSTAIN and not message.payload.get("reason"):
        errors.append("ABSTAIN richiede reason")

    return MessageValidationResult(
        valid=len(errors) == 0,
        errors=errors,
        warnings=warnings,
        blocking=len(errors) > 0,
    )
```

---

## 38.9 Agent Communication Gateway

Il gateway è il punto unico per inviare messaggi tra agenti.

```python
@dataclass
class AgentCommunicationGateway:
    message_bus: MessageBus
    message_factory: MessageFactory

    def send_request(
        self,
        sender: str,
        recipient: str,
        task: RuntimeTask,
        request: str,
        expected_output: str,
        intent: str = "agent_request",
        priority: AgentMessagePriority = AgentMessagePriority.NORMAL,
    ) -> AgentMessage:
        message = self.message_factory.create(
            sender=sender,
            recipient=recipient,
            message_type=AgentMessageType.REQUEST,
            intent=intent,
            payload={
                "request": request,
                "expected_output": expected_output,
                "acceptance_criteria": task.acceptance_criteria,
            },
            command_id=task.command_id,
            task_id=task.task_id,
            project_id=task.project_id,
            workflow_name=task.workflow_name,
            priority=priority,
            requires_response=True,
        )
        validation = validate_agent_message(message)
        if not validation.valid:
            raise ValueError(f"AgentMessage invalid: {validation.errors}")
        self.message_bus.publish(message)
        return message

    def send_response(
        self,
        request_message: AgentMessage,
        sender: str,
        response: str,
        result_status: str = "OK",
        artifacts: list[str] | None = None,
    ) -> AgentMessage:
        message = self.message_factory.response(
            request_message=request_message,
            sender=sender,
            payload={
                "response": response,
                "result_status": result_status,
                "artifacts": artifacts or [],
            },
            message_type=AgentMessageType.RESPONSE,
        )
        validation = validate_agent_message(message)
        if not validation.valid:
            raise ValueError(f"AgentMessage invalid: {validation.errors}")
        self.message_bus.publish(message)
        self.message_bus.mark_status(request_message.message_id, AgentMessageStatus.RESPONDED)
        return message

    def send_abstain(
        self,
        request_message: AgentMessage,
        sender: str,
        reason: str,
        missing_information: list[str],
    ) -> AgentMessage:
        message = self.message_factory.response(
            request_message=request_message,
            sender=sender,
            payload={
                "reason": reason,
                "missing_information": missing_information,
            },
            message_type=AgentMessageType.ABSTAIN,
            intent="abstain_from_task",
        )
        validation = validate_agent_message(message)
        if not validation.valid:
            raise ValueError(f"AgentMessage invalid: {validation.errors}")
        self.message_bus.publish(message)
        return message

    def send_error(
        self,
        request_message: AgentMessage,
        sender: str,
        error_summary: str,
        error_category: str,
    ) -> AgentMessage:
        message = self.message_factory.response(
            request_message=request_message,
            sender=sender,
            payload={
                "error_summary": error_summary,
                "error_category": error_category,
            },
            message_type=AgentMessageType.ERROR,
            intent="agent_error",
        )
        validation = validate_agent_message(message)
        if not validation.valid:
            raise ValueError(f"AgentMessage invalid: {validation.errors}")
        self.message_bus.publish(message)
        return message
```

---

## 38.10 Communication Supervisor

Il supervisor interpreta risposte critiche: `ABSTAIN`, `ERROR`, `APPROVAL_REQUIRED`, `CLARIFICATION_REQUIRED`.

```python
class CommunicationOutcome(str, Enum):
    CONTINUE = "CONTINUE"
    WAIT_FOR_RESPONSE = "WAIT_FOR_RESPONSE"
    BLOCK_ON_ABSTAIN = "BLOCK_ON_ABSTAIN"
    ESCALATE_ERROR = "ESCALATE_ERROR"
    REQUEST_APPROVAL = "REQUEST_APPROVAL"
    REQUEST_CLARIFICATION = "REQUEST_CLARIFICATION"


@dataclass
class CommunicationDecision:
    outcome: CommunicationOutcome
    message_id: str
    reason: str
    target_agent: str | None = None
    requires_user_action: bool = False
    user_prompt: str | None = None
    update_task_status_to: TaskStatus | None = None


@dataclass
class CommunicationSupervisor:
    def inspect(self, message: AgentMessage) -> CommunicationDecision:
        if message.message_type == AgentMessageType.ABSTAIN:
            return CommunicationDecision(
                outcome=CommunicationOutcome.BLOCK_ON_ABSTAIN,
                message_id=message.message_id,
                reason=message.payload.get("reason", "Agente ha risposto ABSTAIN"),
                target_agent="Caesar",
                requires_user_action=True,
                user_prompt="Un agente si è astenuto. Serve chiarimento o cambio piano.",
                update_task_status_to=TaskStatus.BLOCKED,
            )

        if message.message_type == AgentMessageType.ERROR:
            return CommunicationDecision(
                outcome=CommunicationOutcome.ESCALATE_ERROR,
                message_id=message.message_id,
                reason=message.payload.get("error_summary", "Errore agente"),
                target_agent="L16",
                requires_user_action=False,
                update_task_status_to=TaskStatus.FAILED,
            )

        if message.message_type == AgentMessageType.APPROVAL_REQUIRED:
            return CommunicationDecision(
                outcome=CommunicationOutcome.REQUEST_APPROVAL,
                message_id=message.message_id,
                reason=message.payload.get("decision_needed", "Approvazione richiesta"),
                target_agent="Caesar",
                requires_user_action=True,
                user_prompt=message.payload.get("decision_needed"),
                update_task_status_to=TaskStatus.WAITING_APPROVAL,
            )

        if message.message_type == AgentMessageType.CLARIFICATION_REQUIRED:
            return CommunicationDecision(
                outcome=CommunicationOutcome.REQUEST_CLARIFICATION,
                message_id=message.message_id,
                reason=message.payload.get("why_needed", "Chiarimento richiesto"),
                target_agent="Caesar",
                requires_user_action=True,
                user_prompt=message.payload.get("question"),
                update_task_status_to=TaskStatus.WAITING_APPROVAL,
            )

        return CommunicationDecision(
            outcome=CommunicationOutcome.CONTINUE,
            message_id=message.message_id,
            reason="Messaggio non bloccante",
        )
```

---

## 38.11 Pattern di comunicazione standard

### Caesar → Legionario

```text
Caesar crea Task
↓
Caesar invia AgentMessage REQUEST al Legionario
↓
Legionario risponde RESULT / RESPONSE / ABSTAIN / ERROR
↓
CommunicationSupervisor decide il prossimo stato
```

### Legionario → QA

```text
L7 Production produce draft
↓
L7 invia REVIEW_REQUEST a L8 QA
↓
L8 risponde REVIEW_RESPONSE
↓
Se problemi bloccanti → task torna in revisione
↓
Se OK → Caesar prepara review utente
```

### L14 Plan Architect → L19 ADE

```text
L14 genera MasterPlan
↓
L14 invia REVIEW_REQUEST / PRE_MORTEM REQUEST a L19
↓
L19 risponde con ADE verdict
↓
L14 corregge o Caesar chiede decisione utente
```

### ABSTAIN

```text
Qualunque Legionario può rispondere ABSTAIN.
ABSTAIN blocca il task.
Caesar chiede chiarimento o modifica piano.
```

---

## 38.12 Regole operative Agent Communication

```text
1. Nessuna comunicazione tra agenti avviene in testo libero non strutturato.
2. Ogni messaggio ha message_id, thread_id, parent_id, sender, recipient, intent e payload.
3. Ogni messaggio è append-only in MessageBus.
4. Ogni payload deve rispettare il contratto minimo per message_type.
5. ABSTAIN blocca la pipeline.
6. ERROR passa a ErrorManager.
7. APPROVAL_REQUIRED passa ad ApprovalGate.
8. CLARIFICATION_REQUIRED torna a Caesar e poi all’utente.
9. Caesar resta orchestratore e può ispezionare ogni thread.
10. I Legionari non possono creare task autonomamente: possono richiederli a Caesar via HANDOFF.
```

---

## 38.13 Stato del punto implementato

| Punto runtime | Stato |
|---|---|
| Come un agente comunica con un altro | Implementato |
| `AgentMessage` | Implementato |
| Message type/status/priority | Implementati |
| Payload contract | Implementato |
| `MessageBus` protocol | Implementato |
| `JsonlMessageBus` | Implementato |
| `MessageFactory` | Implementata |
| Message validation | Implementata |
| `AgentCommunicationGateway` | Implementato |
| `CommunicationSupervisor` | Implementato |
| Gestione `ABSTAIN` | Implementata |
| Escalation `ERROR` | Implementata |

```text
┌─ LA DECISIONE ─────────────────────────────────────────────────┐
│ Scelta: Usare AgentMessage + MessageBus per ogni comunicazione tra agenti │
│ Perché: Rende gli scambi tracciabili, validabili e bloccabili in sicurezza │
└────────────────────────────────────────────────────────────────┘
```


---

## 39. Runtime Execution Layer — FileSystem Execution Protocol

Questa sezione implementa l’ottavo punto del runtime: **come vengono eseguite davvero le azioni sul filesystem**.

Obiettivo:

```text
RuntimeTask / richiesta Atlas / output approvato
↓
FileSystemAction
↓
FileSystemPlan
↓
Dry-run + validazione sicurezza
↓
ApprovalGate se A2+
↓
FileSystemExecutor
↓
Backup + atomic operation + changelog + rollback metadata
```

Regola chiave:

```text
Nessuna modifica filesystem A2+ viene eseguita senza approvazione esplicita.
```

---

## 39.1 Principio di esecuzione filesystem

Il filesystem è trattato come superficie ad alto impatto.

Caesar, Atlas e i Legionari non scrivono, spostano, rinominano o cancellano direttamente.  
Ogni operazione passa da `FileSystemExecutor`.

Il protocollo garantisce:

- dry-run prima dell’esecuzione;
- controllo path consentiti;
- protezione file root/config;
- backup prima delle modifiche distruttive;
- scrittura atomica quando possibile;
- changelog append-only;
- rollback plan;
- blocco su ambiguità;
- approvazione esplicita per azioni A2+.

---

## 39.2 FileSystem Action Types

```python
class FileSystemActionType(str, Enum):
    READ_FILE = "READ_FILE"
    WRITE_FILE = "WRITE_FILE"
    APPEND_FILE = "APPEND_FILE"
    CREATE_DIR = "CREATE_DIR"
    MOVE = "MOVE"
    COPY = "COPY"
    RENAME = "RENAME"
    DELETE = "DELETE"
    DEPRECATE = "DEPRECATE"
    UPDATE_REFERENCES = "UPDATE_REFERENCES"
    GENERATE_PDF = "GENERATE_PDF"
    TOUCH = "TOUCH"


class FileSystemActionStatus(str, Enum):
    DRAFT = "DRAFT"
    DRY_RUN_PASSED = "DRY_RUN_PASSED"
    DRY_RUN_FAILED = "DRY_RUN_FAILED"
    WAITING_APPROVAL = "WAITING_APPROVAL"
    APPROVED = "APPROVED"
    EXECUTING = "EXECUTING"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"
    ROLLED_BACK = "ROLLED_BACK"
    BLOCKED = "BLOCKED"
```

---

## 39.3 FileSystemAction

```python
@dataclass
class FileSystemAction:
    action_id: str
    action_type: FileSystemActionType
    source_path: str | None = None
    target_path: str | None = None
    content: str | None = None
    encoding: str = "utf-8"
    risk_level: ActionLevel = ActionLevel.A2
    status: FileSystemActionStatus = FileSystemActionStatus.DRAFT
    requires_approval: bool = True
    approved: bool = False
    reason: str = ""
    task_id: str | None = None
    command_id: str | None = None
    project_id: str | None = None
    backup_path: str | None = None
    idempotency_key: str = ""
    metadata: dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data = asdict(self)
        data["action_type"] = self.action_type.value
        data["risk_level"] = self.risk_level.value
        data["status"] = self.status.value
        return data
```

---

## 39.4 FileSystemPlan

Un `FileSystemPlan` raggruppa una o più azioni atomiche/logiche.

```python
@dataclass
class FileSystemPlan:
    plan_id: str
    created_at: str
    created_by: str
    task_id: str | None
    project_id: str | None
    summary: str
    actions: list[FileSystemAction]
    requires_approval: bool
    approved: bool = False
    dry_run_passed: bool = False
    changelog_path: str | None = None
    rollback_plan: RollbackPlan | None = None
    metadata: dict[str, Any] = field(default_factory=dict)

    def max_risk_level(self) -> ActionLevel:
        order = {ActionLevel.A0: 0, ActionLevel.A1: 1, ActionLevel.A2: 2, ActionLevel.A3: 3, ActionLevel.A4: 4}
        return max((action.risk_level for action in self.actions), key=lambda level: order[level])
```

---

## 39.5 FileSystem Safety Policy

```python
@dataclass(frozen=True)
class FileSystemSafetyPolicy:
    workspace_root: Path
    allow_delete: bool = False
    allow_overwrite: bool = True
    allow_outside_workspace: bool = False
    require_backup_for_overwrite: bool = True
    require_backup_for_move: bool = True
    require_backup_for_delete: bool = True
    preserve_root_config: bool = True
    update_references_on_move: bool = True
    ignored_folders: set[str] = field(default_factory=lambda: {
        ".git", "node_modules", "dist", "build", ".next", "coverage", "vendor",
        "__pycache__", ".cache", ".turbo", ".vercel", ".svelte-kit",
    })
    protected_root_files: set[str] = field(default_factory=lambda: {
        "package.json", "README.md", ".env", ".gitignore", "tsconfig.json",
        "vite.config.js", "docker-compose.yml", "pyproject.toml", "requirements.txt",
    })

    def resolve_safe_path(self, path_str: str) -> Path:
        path = Path(path_str)
        if not path.is_absolute():
            path = self.workspace_root / path
        resolved = path.resolve()
        root = self.workspace_root.resolve()
        if not self.allow_outside_workspace and root not in {resolved, *resolved.parents}:
            raise PermissionError(f"Path fuori workspace non consentito: {resolved}")
        return resolved

    def is_ignored(self, path: Path) -> bool:
        return any(part in self.ignored_folders for part in path.parts)

    def is_protected_root_file(self, path: Path) -> bool:
        try:
            rel = path.resolve().relative_to(self.workspace_root.resolve())
        except ValueError:
            return True
        return len(rel.parts) == 1 and rel.name in self.protected_root_files
```

---

## 39.6 Dry Run Result

```python
@dataclass
class FileSystemDryRunResult:
    valid: bool
    plan_id: str
    errors: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)
    actions_preview: list[str] = field(default_factory=list)
    requires_approval: bool = False
    max_risk_level: ActionLevel = ActionLevel.A0
    blocking: bool = False
```

---

## 39.7 FileSystem ChangeLog

```python
@dataclass
class FileSystemChange:
    change_id: str
    timestamp: str
    action_id: str
    action_type: FileSystemActionType
    source_path: str | None
    target_path: str | None
    status: FileSystemActionStatus
    summary: str
    backup_path: str | None = None
    task_id: str | None = None
    project_id: str | None = None

    def to_dict(self) -> dict[str, Any]:
        data = asdict(self)
        data["action_type"] = self.action_type.value
        data["status"] = self.status.value
        return data


@dataclass
class FileSystemChangeLog:
    path: Path

    def append(self, change: FileSystemChange) -> None:
        self.path.parent.mkdir(parents=True, exist_ok=True)
        with self.path.open("a", encoding="utf-8") as f:
            f.write(json.dumps(change.to_dict(), ensure_ascii=False) + "\n")
```

Path consigliato:

```text
[progetto]/.agents/runtime/filesystem-changelog.jsonl
centro-di-comando/runtime/filesystem-changelog.jsonl
```

---

## 39.8 FileSystemExecutor

```python
@dataclass
class FileSystemExecutor:
    safety_policy: FileSystemSafetyPolicy
    changelog: FileSystemChangeLog
    backup_root: Path

    def dry_run(self, plan: FileSystemPlan) -> FileSystemDryRunResult:
        errors: list[str] = []
        warnings: list[str] = []
        preview: list[str] = []

        for action in plan.actions:
            try:
                self._validate_action(action)
                preview.append(self._preview_action(action))
            except Exception as exc:
                errors.append(f"{action.action_id}: {exc}")

        max_risk = plan.max_risk_level() if plan.actions else ActionLevel.A0
        requires_approval = any(action.requires_approval or action.risk_level in APPROVAL_REQUIRED_FOR for action in plan.actions)

        result = FileSystemDryRunResult(
            valid=len(errors) == 0,
            plan_id=plan.plan_id,
            errors=errors,
            warnings=warnings,
            actions_preview=preview,
            requires_approval=requires_approval,
            max_risk_level=max_risk,
            blocking=len(errors) > 0,
        )

        for action in plan.actions:
            action.status = FileSystemActionStatus.DRY_RUN_PASSED if result.valid else FileSystemActionStatus.DRY_RUN_FAILED

        plan.dry_run_passed = result.valid
        plan.requires_approval = requires_approval
        return result

    def execute_plan(self, plan: FileSystemPlan) -> list[FileSystemChange]:
        if not plan.dry_run_passed:
            raise RuntimeError("FileSystemPlan non ha superato dry-run")

        if plan.requires_approval and not plan.approved:
            for action in plan.actions:
                action.status = FileSystemActionStatus.WAITING_APPROVAL
            raise PermissionError("FileSystemPlan richiede approvazione esplicita")

        changes: list[FileSystemChange] = []
        for action in plan.actions:
            change = self.execute_action(action)
            changes.append(change)
        return changes

    def execute_action(self, action: FileSystemAction) -> FileSystemChange:
        self._validate_action(action)

        if action.requires_approval and not action.approved:
            action.status = FileSystemActionStatus.WAITING_APPROVAL
            raise PermissionError(f"Azione {action.action_id} richiede approvazione")

        action.status = FileSystemActionStatus.EXECUTING

        try:
            backup_path = self._backup_if_needed(action)
            action.backup_path = str(backup_path) if backup_path else None

            if action.action_type == FileSystemActionType.READ_FILE:
                self._read_file(action)
            elif action.action_type == FileSystemActionType.WRITE_FILE:
                self._write_file_atomic(action)
            elif action.action_type == FileSystemActionType.APPEND_FILE:
                self._append_file(action)
            elif action.action_type == FileSystemActionType.CREATE_DIR:
                self._create_dir(action)
            elif action.action_type in {FileSystemActionType.MOVE, FileSystemActionType.RENAME}:
                self._move(action)
            elif action.action_type == FileSystemActionType.COPY:
                self._copy(action)
            elif action.action_type == FileSystemActionType.DELETE:
                self._delete(action)
            elif action.action_type == FileSystemActionType.DEPRECATE:
                self._deprecate(action)
            elif action.action_type == FileSystemActionType.TOUCH:
                self._touch(action)
            else:
                raise NotImplementedError(f"Azione non implementata: {action.action_type.value}")

            action.status = FileSystemActionStatus.COMPLETED
            change = self._make_change(action, "Azione filesystem completata")
            self.changelog.append(change)
            return change

        except Exception as exc:
            action.status = FileSystemActionStatus.FAILED
            change = self._make_change(action, f"Azione filesystem fallita: {exc}")
            self.changelog.append(change)
            raise

    def _validate_action(self, action: FileSystemAction) -> None:
        paths = [p for p in [action.source_path, action.target_path] if p]
        for p in paths:
            resolved = self.safety_policy.resolve_safe_path(p)
            if self.safety_policy.is_ignored(resolved):
                raise PermissionError(f"Path in cartella ignorata: {resolved}")
            if self.safety_policy.is_protected_root_file(resolved) and action.action_type not in {FileSystemActionType.READ_FILE}:
                raise PermissionError(f"File root protetto: {resolved}")

        if action.action_type == FileSystemActionType.DELETE and not self.safety_policy.allow_delete:
            raise PermissionError("DELETE non consentito dalla safety policy")

        if action.action_type in {FileSystemActionType.WRITE_FILE, FileSystemActionType.APPEND_FILE} and not action.target_path:
            raise ValueError("target_path richiesto")

        if action.action_type in {FileSystemActionType.MOVE, FileSystemActionType.COPY, FileSystemActionType.RENAME}:
            if not action.source_path or not action.target_path:
                raise ValueError("source_path e target_path richiesti")

        if action.risk_level in APPROVAL_REQUIRED_FOR and not action.requires_approval:
            raise PermissionError("Azione A2+ deve avere requires_approval=True")

    def _preview_action(self, action: FileSystemAction) -> str:
        return f"{action.action_type.value}: {action.source_path or ''} → {action.target_path or ''}".strip()

    def _backup_if_needed(self, action: FileSystemAction) -> Path | None:
        path_str = action.source_path or action.target_path
        if not path_str:
            return None
        path = self.safety_policy.resolve_safe_path(path_str)

        needs_backup = False
        if action.action_type == FileSystemActionType.WRITE_FILE and path.exists() and self.safety_policy.require_backup_for_overwrite:
            needs_backup = True
        if action.action_type in {FileSystemActionType.MOVE, FileSystemActionType.RENAME, FileSystemActionType.DELETE, FileSystemActionType.DEPRECATE}:
            needs_backup = True

        if not needs_backup or not path.exists() or path.is_dir():
            return None

        self.backup_root.mkdir(parents=True, exist_ok=True)
        backup_path = self.backup_root / f"{datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S')}_{path.name}.bak"
        backup_path.write_bytes(path.read_bytes())
        return backup_path

    def _read_file(self, action: FileSystemAction) -> str:
        path = self.safety_policy.resolve_safe_path(action.source_path or action.target_path or "")
        content = path.read_text(encoding=action.encoding)
        action.metadata["read_content_preview"] = content[:1000]
        return content

    def _write_file_atomic(self, action: FileSystemAction) -> None:
        path = self.safety_policy.resolve_safe_path(action.target_path or "")
        path.parent.mkdir(parents=True, exist_ok=True)
        tmp_path = path.with_suffix(path.suffix + ".tmp")
        tmp_path.write_text(action.content or "", encoding=action.encoding)
        tmp_path.replace(path)

    def _append_file(self, action: FileSystemAction) -> None:
        path = self.safety_policy.resolve_safe_path(action.target_path or "")
        path.parent.mkdir(parents=True, exist_ok=True)
        with path.open("a", encoding=action.encoding) as f:
            f.write(action.content or "")

    def _create_dir(self, action: FileSystemAction) -> None:
        path = self.safety_policy.resolve_safe_path(action.target_path or action.source_path or "")
        path.mkdir(parents=True, exist_ok=True)

    def _move(self, action: FileSystemAction) -> None:
        source = self.safety_policy.resolve_safe_path(action.source_path or "")
        target = self.safety_policy.resolve_safe_path(action.target_path or "")
        target.parent.mkdir(parents=True, exist_ok=True)
        source.replace(target)

    def _copy(self, action: FileSystemAction) -> None:
        source = self.safety_policy.resolve_safe_path(action.source_path or "")
        target = self.safety_policy.resolve_safe_path(action.target_path or "")
        target.parent.mkdir(parents=True, exist_ok=True)
        if source.is_dir():
            raise NotImplementedError("COPY directory richiede implementazione dedicata")
        target.write_bytes(source.read_bytes())

    def _delete(self, action: FileSystemAction) -> None:
        path = self.safety_policy.resolve_safe_path(action.source_path or action.target_path or "")
        if path.is_dir():
            raise PermissionError("DELETE directory non consentito da executor base")
        path.unlink()

    def _deprecate(self, action: FileSystemAction) -> None:
        path = self.safety_policy.resolve_safe_path(action.source_path or action.target_path or "")
        deprecated_path = path.with_name(path.name + ".deprecated")
        path.replace(deprecated_path)
        action.metadata["deprecated_path"] = str(deprecated_path)

    def _touch(self, action: FileSystemAction) -> None:
        path = self.safety_policy.resolve_safe_path(action.target_path or action.source_path or "")
        path.parent.mkdir(parents=True, exist_ok=True)
        path.touch(exist_ok=True)

    def _make_change(self, action: FileSystemAction, summary: str) -> FileSystemChange:
        return FileSystemChange(
            change_id=f"fs_chg_{uuid.uuid4().hex[:12]}",
            timestamp=datetime.now(timezone.utc).isoformat(),
            action_id=action.action_id,
            action_type=action.action_type,
            source_path=action.source_path,
            target_path=action.target_path,
            status=action.status,
            summary=summary,
            backup_path=action.backup_path,
            task_id=action.task_id,
            project_id=action.project_id,
        )
```

---

## 39.9 FileSystemPlanFactory

```python
@dataclass
class FileSystemPlanFactory:
    def create_write_file_plan(
        self,
        target_path: str,
        content: str,
        reason: str,
        task: RuntimeTask | None = None,
        created_by: str = "Caesar",
        risk_level: ActionLevel = ActionLevel.A2,
    ) -> FileSystemPlan:
        now = datetime.now(timezone.utc).isoformat()
        action = FileSystemAction(
            action_id=f"fs_act_{uuid.uuid4().hex[:12]}",
            action_type=FileSystemActionType.WRITE_FILE,
            target_path=target_path,
            content=content,
            risk_level=risk_level,
            requires_approval=risk_level in APPROVAL_REQUIRED_FOR,
            reason=reason,
            task_id=task.task_id if task else None,
            command_id=task.command_id if task else None,
            project_id=task.project_id if task else None,
        )
        action.idempotency_key = self.make_action_idempotency_key(action)
        return FileSystemPlan(
            plan_id=f"fs_plan_{uuid.uuid4().hex[:12]}",
            created_at=now,
            created_by=created_by,
            task_id=task.task_id if task else None,
            project_id=task.project_id if task else None,
            summary=reason,
            actions=[action],
            requires_approval=action.requires_approval,
        )

    def create_move_plan(
        self,
        source_path: str,
        target_path: str,
        reason: str,
        task: RuntimeTask | None = None,
        created_by: str = "Atlas",
    ) -> FileSystemPlan:
        now = datetime.now(timezone.utc).isoformat()
        action = FileSystemAction(
            action_id=f"fs_act_{uuid.uuid4().hex[:12]}",
            action_type=FileSystemActionType.MOVE,
            source_path=source_path,
            target_path=target_path,
            risk_level=ActionLevel.A2,
            requires_approval=True,
            reason=reason,
            task_id=task.task_id if task else None,
            command_id=task.command_id if task else None,
            project_id=task.project_id if task else None,
        )
        action.idempotency_key = self.make_action_idempotency_key(action)
        return FileSystemPlan(
            plan_id=f"fs_plan_{uuid.uuid4().hex[:12]}",
            created_at=now,
            created_by=created_by,
            task_id=task.task_id if task else None,
            project_id=task.project_id if task else None,
            summary=reason,
            actions=[action],
            requires_approval=True,
        )

    @staticmethod
    def make_action_idempotency_key(action: FileSystemAction) -> str:
        base = "|".join([
            action.action_type.value,
            action.source_path or "NO_SOURCE",
            action.target_path or "NO_TARGET",
            action.task_id or "NO_TASK",
            hashlib.sha256((action.content or "").encode("utf-8")).hexdigest(),
        ])
        return hashlib.sha256(base.encode("utf-8")).hexdigest()
```

---

## 39.10 Approval Integration

Il filesystem executor non approva da solo.  
Produce piani che Caesar sottopone all’utente tramite ApprovalGate.

```python
@dataclass
class FileSystemApprovalRequest:
    approval_id: str
    plan_id: str
    summary: str
    actions_preview: list[str]
    max_risk_level: ActionLevel
    options: list[str] = field(default_factory=lambda: ["APPROVE", "REVISE", "ABORT"])
    recommended_option: str = "APPROVE"
    reason: str = "Operazione filesystem richiede consenso esplicito"
```

Regola:

```text
FileSystemPlan.requires_approval = True → Caesar deve presentare FileSystemApprovalRequest.
Solo dopo APPROVE, plan.approved = True e action.approved = True.
```

---

## 39.11 Rollback da backup

```python
@dataclass
class FileSystemRollbackExecutor:
    safety_policy: FileSystemSafetyPolicy
    changelog: FileSystemChangeLog

    def rollback_action(self, action: FileSystemAction) -> FileSystemChange:
        if not action.backup_path:
            raise RuntimeError("Rollback impossibile: backup_path mancante")
        if action.risk_level in APPROVAL_REQUIRED_FOR and not action.approved:
            raise PermissionError("Rollback A2+ richiede approvazione")

        backup = self.safety_policy.resolve_safe_path(action.backup_path)
        target = self.safety_policy.resolve_safe_path(action.target_path or action.source_path or "")
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(backup.read_bytes())
        action.status = FileSystemActionStatus.ROLLED_BACK

        change = FileSystemChange(
            change_id=f"fs_chg_{uuid.uuid4().hex[:12]}",
            timestamp=datetime.now(timezone.utc).isoformat(),
            action_id=action.action_id,
            action_type=action.action_type,
            source_path=action.backup_path,
            target_path=str(target),
            status=FileSystemActionStatus.ROLLED_BACK,
            summary="Rollback filesystem eseguito da backup",
            backup_path=action.backup_path,
            task_id=action.task_id,
            project_id=action.project_id,
        )
        self.changelog.append(change)
        return change
```

---

## 39.12 Integrazione con Caesar Runtime

```python
@dataclass
class CaesarFileSystemRuntime:
    fs_plan_factory: FileSystemPlanFactory
    fs_executor: FileSystemExecutor
    state_store: StateStore

    def propose_write_file(
        self,
        task: RuntimeTask,
        target_path: str,
        content: str,
        reason: str,
    ) -> tuple[FileSystemPlan, FileSystemDryRunResult]:
        plan = self.fs_plan_factory.create_write_file_plan(
            target_path=target_path,
            content=content,
            reason=reason,
            task=task,
            risk_level=ActionLevel.A2,
        )
        dry_run = self.fs_executor.dry_run(plan)
        return plan, dry_run

    def execute_approved_plan(self, plan: FileSystemPlan) -> list[FileSystemChange]:
        if plan.requires_approval and not plan.approved:
            raise PermissionError("Piano filesystem non approvato")
        changes = self.fs_executor.execute_plan(plan)
        return changes
```

---

## 39.13 Regole operative FileSystemExecutor

```text
1. Nessun agente scrive direttamente su filesystem.
2. Ogni modifica passa da FileSystemAction.
3. Ogni gruppo di modifiche passa da FileSystemPlan.
4. Ogni piano deve passare dry-run.
5. Ogni azione A2+ richiede approvazione esplicita.
6. Ogni overwrite/move/delete/deprecate crea backup se possibile.
7. WRITE_FILE usa scrittura atomica.
8. DELETE è disabilitato di default.
9. Cartelle ignorate non vengono toccate.
10. File root protetti non vengono modificati senza policy dedicata.
11. Ogni modifica genera FileSystemChange in changelog append-only.
12. Rollback A2+ richiede approvazione.
13. FileSystemExecutor non pubblica, non invia email, non muove soldi.
```

---

## 39.14 Stato del punto implementato

| Punto runtime | Stato |
|---|---|
| Come vengono eseguite azioni sul filesystem | Implementato |
| `FileSystemAction` | Implementato |
| `FileSystemPlan` | Implementato |
| `FileSystemSafetyPolicy` | Implementata |
| Dry-run | Implementato |
| `FileSystemExecutor` | Implementato |
| Backup prima di modifiche rischiose | Implementato |
| Atomic write | Implementato |
| Changelog append-only | Implementato |
| Approval integration | Implementata |
| Rollback executor | Implementato |
| Blocco DELETE default | Implementato |
| Protezione root config | Implementata |

```text
┌─ LA DECISIONE ─────────────────────────────────────────────────┐
│ Scelta: Usare FileSystemExecutor come unico canale per modifiche file │
│ Perché: Dry-run, approvazione, backup e changelog rendono le azioni sicure │
└────────────────────────────────────────────────────────────────┘
```


---

## 40. Runtime Execution Layer — Validation Gate Protocol

Questa sezione implementa il nono punto del runtime: **come Caesar valida che un output rispetti DecisionBox, MasterPlan, ADE e approvazioni**.

Obiettivo:

```text
Output agente / piano / ADE / richiesta approvazione / file plan
↓
ValidationGate
↓
Validator specifici
↓
ValidationReport
↓
PASS oppure BLOCK oppure REVISE
```

Regola chiave:

```text
Nessun output operativo raggiunge l’utente o l’esecuzione se non supera i validator obbligatori.
```

---

## 40.1 Principio di validazione

La validazione è un gate obbligatorio tra:

```text
Produzione output
↓
Review interna
↓
Utente o esecuzione
```

Il gate controlla:

- presenza e formato DecisionBox;
- completezza MasterPlan;
- completezza ADE;
- rispetto approvazioni;
- coerenza risk level / approval;
- assenza di azioni A2+ non autorizzate;
- presenza acceptance criteria;
- rispetto max revision cycles;
- blocchi compliance, budget o filesystem.

---

## 40.2 Validation Types

```python
class ValidationTargetType(str, Enum):
    CAESAR_OUTPUT = "CAESAR_OUTPUT"
    DECISION_BOX = "DECISION_BOX"
    MASTERPLAN = "MASTERPLAN"
    ADE_REPORT = "ADE_REPORT"
    APPROVAL_REQUEST = "APPROVAL_REQUEST"
    TASK = "TASK"
    FILESYSTEM_PLAN = "FILESYSTEM_PLAN"
    AGENT_MESSAGE = "AGENT_MESSAGE"
    RUNTIME_STATE = "RUNTIME_STATE"
    CRITICAL_THINKING = "CRITICAL_THINKING"


class ValidationSeverity(str, Enum):
    INFO = "INFO"
    WARNING = "WARNING"
    ERROR = "ERROR"
    BLOCKING = "BLOCKING"


class ValidationGateDecision(str, Enum):
    PASS = "PASS"
    PASS_WITH_WARNINGS = "PASS_WITH_WARNINGS"
    REVISE = "REVISE"
    BLOCK = "BLOCK"
    ESCALATE = "ESCALATE"
```

---

## 40.3 Validation Issue e Report

```python
@dataclass
class ValidationIssue:
    code: str
    severity: ValidationSeverity
    message: str
    field: str | None = None
    fix_hint: str | None = None

    def to_dict(self) -> dict[str, Any]:
        data = asdict(self)
        data["severity"] = self.severity.value
        return data


@dataclass
class ValidationReport:
    report_id: str
    target_type: ValidationTargetType
    target_id: str | None
    valid: bool
    decision: ValidationGateDecision
    issues: list[ValidationIssue] = field(default_factory=list)
    warnings: list[ValidationIssue] = field(default_factory=list)
    validator: str = "ValidationGate"
    created_at: str = ""
    metadata: dict[str, Any] = field(default_factory=dict)

    def has_blockers(self) -> bool:
        return any(issue.severity == ValidationSeverity.BLOCKING for issue in self.issues)

    def to_dict(self) -> dict[str, Any]:
        return {
            "report_id": self.report_id,
            "target_type": self.target_type.value,
            "target_id": self.target_id,
            "valid": self.valid,
            "decision": self.decision.value,
            "issues": [issue.to_dict() for issue in self.issues],
            "warnings": [warning.to_dict() for warning in self.warnings],
            "validator": self.validator,
            "created_at": self.created_at,
            "metadata": self.metadata,
        }
```

---

## 40.4 Validator Protocol

```python
class Validator(Protocol):
    name: str

    def validate(self, target: Any, context: dict[str, Any] | None = None) -> ValidationReport:
        ...
```

---

## 40.5 DecisionBoxValidator

Valida formato e limiti della DecisionBox.

```python
@dataclass
class DecisionBoxValidator:
    name: str = "DecisionBoxValidator"
    max_choice_chars: int = 120
    max_reason_chars: int = 140

    def validate(self, target: str | DecisionBox, context: dict[str, Any] | None = None) -> ValidationReport:
        issues: list[ValidationIssue] = []
        warnings: list[ValidationIssue] = []

        if isinstance(target, DecisionBox):
            choice = target.choice.strip()
            reason = target.reason.strip()
            target_id = None
        else:
            target_id = None
            choice, reason = self.extract_from_text(target)

        if not choice:
            issues.append(ValidationIssue(
                code="DECISIONBOX_CHOICE_MISSING",
                severity=ValidationSeverity.BLOCKING,
                message="DecisionBox manca del campo Scelta",
                field="choice",
                fix_hint="Aggiungere Scelta con massimo 120 caratteri",
            ))

        if not reason:
            issues.append(ValidationIssue(
                code="DECISIONBOX_REASON_MISSING",
                severity=ValidationSeverity.BLOCKING,
                message="DecisionBox manca del campo Perché",
                field="reason",
                fix_hint="Aggiungere Perché con massimo 140 caratteri",
            ))

        if len(choice) > self.max_choice_chars:
            issues.append(ValidationIssue(
                code="DECISIONBOX_CHOICE_TOO_LONG",
                severity=ValidationSeverity.ERROR,
                message=f"Scelta supera {self.max_choice_chars} caratteri",
                field="choice",
                fix_hint="Accorciare Scelta",
            ))

        if len(reason) > self.max_reason_chars:
            issues.append(ValidationIssue(
                code="DECISIONBOX_REASON_TOO_LONG",
                severity=ValidationSeverity.ERROR,
                message=f"Perché supera {self.max_reason_chars} caratteri",
                field="reason",
                fix_hint="Accorciare Perché",
            ))

        if "\n" in choice.strip() or "\n" in reason.strip():
            issues.append(ValidationIssue(
                code="DECISIONBOX_MULTILINE_FIELD",
                severity=ValidationSeverity.ERROR,
                message="DecisionBox deve avere campi su una sola riga",
                fix_hint="Usare una sola riga per Scelta e una sola per Perché",
            ))

        decision = self._decision_from_issues(issues, warnings)
        return ValidationReport(
            report_id=self.new_report_id(),
            target_type=ValidationTargetType.DECISION_BOX,
            target_id=target_id,
            valid=decision in {ValidationGateDecision.PASS, ValidationGateDecision.PASS_WITH_WARNINGS},
            decision=decision,
            issues=issues,
            warnings=warnings,
            validator=self.name,
            created_at=self._now_iso(),
        )

    @staticmethod
    def extract_from_text(text: str) -> tuple[str, str]:
        choice_match = re.search(r"│\s*Scelta:\s*(.*?)\s*│", text)
        reason_match = re.search(r"│\s*Perché:\s*(.*?)\s*│", text)
        choice = choice_match.group(1).strip() if choice_match else ""
        reason = reason_match.group(1).strip() if reason_match else ""
        return choice, reason

    @staticmethod
    def _decision_from_issues(issues: list[ValidationIssue], warnings: list[ValidationIssue]) -> ValidationGateDecision:
        if any(issue.severity == ValidationSeverity.BLOCKING for issue in issues):
            return ValidationGateDecision.BLOCK
        if any(issue.severity == ValidationSeverity.ERROR for issue in issues):
            return ValidationGateDecision.REVISE
        if warnings:
            return ValidationGateDecision.PASS_WITH_WARNINGS
        return ValidationGateDecision.PASS

    @staticmethod
    def new_report_id() -> str:
        return f"val_{uuid.uuid4().hex[:12]}"

    @staticmethod
    def _now_iso() -> str:
        return datetime.now(timezone.utc).isoformat()
```

---

## 40.6 CaesarOutputValidator

Valida output operativo completo di Caesar.

```python
@dataclass
class CaesarOutputValidator:
    name: str = "CaesarOutputValidator"
    decision_box_validator: DecisionBoxValidator = field(default_factory=DecisionBoxValidator)

    required_sections: tuple[str, ...] = (
        "[STATO]",
        "[AZIONE PROPOSTA]",
        "[IMPATTO]",
        "[RICHIESTA]",
    )

    def validate(self, target: str, context: dict[str, Any] | None = None) -> ValidationReport:
        context = context or {}
        operational = context.get("operational", True)
        issues: list[ValidationIssue] = []
        warnings: list[ValidationIssue] = []

        if operational:
            for section in self.required_sections:
                if section not in target:
                    issues.append(ValidationIssue(
                        code="CAESAR_OUTPUT_SECTION_MISSING",
                        severity=ValidationSeverity.ERROR,
                        message=f"Sezione mancante: {section}",
                        field=section,
                        fix_hint="Usare il formato standard Caesar operativo",
                    ))

            db_report = self.decision_box_validator.validate(target)
            issues.extend(db_report.issues)
            warnings.extend(db_report.warnings)

        decision = self._decision_from_issues(issues, warnings)
        return ValidationReport(
            report_id=f"val_{uuid.uuid4().hex[:12]}",
            target_type=ValidationTargetType.CAESAR_OUTPUT,
            target_id=context.get("output_id"),
            valid=decision in {ValidationGateDecision.PASS, ValidationGateDecision.PASS_WITH_WARNINGS},
            decision=decision,
            issues=issues,
            warnings=warnings,
            validator=self.name,
            created_at=datetime.now(timezone.utc).isoformat(),
        )

    @staticmethod
    def _decision_from_issues(issues: list[ValidationIssue], warnings: list[ValidationIssue]) -> ValidationGateDecision:
        if any(issue.severity == ValidationSeverity.BLOCKING for issue in issues):
            return ValidationGateDecision.BLOCK
        if any(issue.severity == ValidationSeverity.ERROR for issue in issues):
            return ValidationGateDecision.REVISE
        if warnings:
            return ValidationGateDecision.PASS_WITH_WARNINGS
        return ValidationGateDecision.PASS
```

---

## 40.7 MasterPlanValidator

Valida completezza strutturale del MasterPlan.

```python
@dataclass
class MasterPlanValidator:
    name: str = "MasterPlanValidator"
    completeness_score_min: float = 0.90

    required_fields: tuple[str, ...] = (
        "objective",
        "success_metric",
        "minimum_acceptable_threshold",
        "background",
        "assumptions",
        "out_of_scope",
        "deliverables",
        "acceptance_criteria",
        "phases",
        "dependencies",
        "budget_total",
        "contingency_percent",
        "ade_risks",
        "kill_conditions",
        "user_checkpoints",
        "decision_box",
        "completeness_score",
    )

    def validate(self, target: MasterPlan, context: dict[str, Any] | None = None) -> ValidationReport:
        issues: list[ValidationIssue] = []
        warnings: list[ValidationIssue] = []

        for field_name in self.required_fields:
            value = getattr(target, field_name, None)
            if value is None or value == "" or value == []:
                issues.append(ValidationIssue(
                    code="MASTERPLAN_REQUIRED_FIELD_MISSING",
                    severity=ValidationSeverity.ERROR,
                    message=f"Campo MasterPlan mancante o vuoto: {field_name}",
                    field=field_name,
                ))

        if target.completeness_score < self.completeness_score_min:
            issues.append(ValidationIssue(
                code="MASTERPLAN_COMPLETENESS_TOO_LOW",
                severity=ValidationSeverity.BLOCKING,
                message=f"Completeness score {target.completeness_score} < {self.completeness_score_min}",
                field="completeness_score",
                fix_hint="Auto-migliorare il piano fino alla soglia minima",
            ))

        if target.contingency_percent != 15:
            warnings.append(ValidationIssue(
                code="MASTERPLAN_CONTINGENCY_NON_STANDARD",
                severity=ValidationSeverity.WARNING,
                message="Contingency diversa dal 15% standard",
                field="contingency_percent",
            ))

        if target.budget_total > 50 and not target.ade_risks:
            issues.append(ValidationIssue(
                code="MASTERPLAN_ADE_REQUIRED",
                severity=ValidationSeverity.BLOCKING,
                message="Budget > 50€ richiede rischi ADE integrati",
                field="ade_risks",
            ))

        for idx, phase in enumerate(target.phases):
            if not phase.name or not phase.department or not phase.agents:
                issues.append(ValidationIssue(
                    code="MASTERPLAN_PHASE_INCOMPLETE",
                    severity=ValidationSeverity.ERROR,
                    message=f"Fase {idx} incompleta",
                    field=f"phases[{idx}]",
                ))
            if phase.estimated_cost < 0:
                issues.append(ValidationIssue(
                    code="MASTERPLAN_PHASE_NEGATIVE_COST",
                    severity=ValidationSeverity.ERROR,
                    message=f"Fase {idx} ha costo negativo",
                    field=f"phases[{idx}].estimated_cost",
                ))

        db_report = DecisionBoxValidator().validate(target.decision_box)
        issues.extend(db_report.issues)
        warnings.extend(db_report.warnings)

        decision = self._decision_from_issues(issues, warnings)
        return ValidationReport(
            report_id=f"val_{uuid.uuid4().hex[:12]}",
            target_type=ValidationTargetType.MASTERPLAN,
            target_id=None,
            valid=decision in {ValidationGateDecision.PASS, ValidationGateDecision.PASS_WITH_WARNINGS},
            decision=decision,
            issues=issues,
            warnings=warnings,
            validator=self.name,
            created_at=datetime.now(timezone.utc).isoformat(),
            metadata={"completeness_score": target.completeness_score},
        )

    @staticmethod
    def _decision_from_issues(issues: list[ValidationIssue], warnings: list[ValidationIssue]) -> ValidationGateDecision:
        if any(issue.severity == ValidationSeverity.BLOCKING for issue in issues):
            return ValidationGateDecision.BLOCK
        if any(issue.severity == ValidationSeverity.ERROR for issue in issues):
            return ValidationGateDecision.REVISE
        if warnings:
            return ValidationGateDecision.PASS_WITH_WARNINGS
        return ValidationGateDecision.PASS
```

---

## 40.8 ADEValidator

Valida un report ADE.

```python
@dataclass
class ADEReport:
    report_id: str
    project_id: str
    scenarios: list[RiskScenario]
    verdict: ADEVerdict
    decision_box: DecisionBox
    categories_covered: list[RiskCategory] = field(default_factory=list)
    mitigations_summary: str = ""


@dataclass
class ADEValidator:
    name: str = "ADEValidator"
    required_categories: set[RiskCategory] = field(default_factory=lambda: set(RiskCategory))

    def validate(self, target: ADEReport, context: dict[str, Any] | None = None) -> ValidationReport:
        issues: list[ValidationIssue] = []
        warnings: list[ValidationIssue] = []

        covered = set(target.categories_covered) or {scenario.category for scenario in target.scenarios}
        missing_categories = self.required_categories - covered
        if missing_categories:
            issues.append(ValidationIssue(
                code="ADE_MISSING_CATEGORIES",
                severity=ValidationSeverity.BLOCKING,
                message=f"ADE non copre categorie: {[c.value for c in missing_categories]}",
                field="categories_covered",
            ))

        if not target.scenarios:
            issues.append(ValidationIssue(
                code="ADE_NO_SCENARIOS",
                severity=ValidationSeverity.BLOCKING,
                message="ADE non contiene scenari di rischio",
                field="scenarios",
            ))

        for idx, scenario in enumerate(target.scenarios):
            if not 0 <= scenario.probability <= 1:
                issues.append(ValidationIssue(
                    code="ADE_INVALID_PROBABILITY",
                    severity=ValidationSeverity.ERROR,
                    message=f"Probabilità fuori range scenario {idx}",
                    field=f"scenarios[{idx}].probability",
                ))
            if not 0 <= scenario.impact <= 1:
                issues.append(ValidationIssue(
                    code="ADE_INVALID_IMPACT",
                    severity=ValidationSeverity.ERROR,
                    message=f"Impatto fuori range scenario {idx}",
                    field=f"scenarios[{idx}].impact",
                ))
            expected_score = scenario.probability * scenario.impact
            if abs(scenario.risk_score - expected_score) > 0.05:
                warnings.append(ValidationIssue(
                    code="ADE_RISK_SCORE_MISMATCH",
                    severity=ValidationSeverity.WARNING,
                    message=f"Risk score scenario {idx} non allineato a probability*impact",
                    field=f"scenarios[{idx}].risk_score",
                ))
            if not scenario.mitigation:
                issues.append(ValidationIssue(
                    code="ADE_MITIGATION_MISSING",
                    severity=ValidationSeverity.ERROR,
                    message=f"Mitigazione mancante scenario {idx}",
                    field=f"scenarios[{idx}].mitigation",
                ))
            if not scenario.kill_condition:
                issues.append(ValidationIssue(
                    code="ADE_KILL_CONDITION_MISSING",
                    severity=ValidationSeverity.ERROR,
                    message=f"Kill condition mancante scenario {idx}",
                    field=f"scenarios[{idx}].kill_condition",
                ))

        catastrophic = [s for s in target.scenarios if s.impact >= 0.9 and s.probability > 0.15]
        if catastrophic and target.verdict != ADEVerdict.ABORT:
            issues.append(ValidationIssue(
                code="ADE_ABORT_REQUIRED",
                severity=ValidationSeverity.BLOCKING,
                message="Rischio catastrofico >15% richiede verdetto ABORT",
                field="verdict",
            ))

        db_report = DecisionBoxValidator().validate(target.decision_box)
        issues.extend(db_report.issues)
        warnings.extend(db_report.warnings)

        decision = self._decision_from_issues(issues, warnings)
        return ValidationReport(
            report_id=f"val_{uuid.uuid4().hex[:12]}",
            target_type=ValidationTargetType.ADE_REPORT,
            target_id=target.report_id,
            valid=decision in {ValidationGateDecision.PASS, ValidationGateDecision.PASS_WITH_WARNINGS},
            decision=decision,
            issues=issues,
            warnings=warnings,
            validator=self.name,
            created_at=datetime.now(timezone.utc).isoformat(),
            metadata={"verdict": target.verdict.value},
        )

    @staticmethod
    def _decision_from_issues(issues: list[ValidationIssue], warnings: list[ValidationIssue]) -> ValidationGateDecision:
        if any(issue.severity == ValidationSeverity.BLOCKING for issue in issues):
            return ValidationGateDecision.BLOCK
        if any(issue.severity == ValidationSeverity.ERROR for issue in issues):
            return ValidationGateDecision.REVISE
        if warnings:
            return ValidationGateDecision.PASS_WITH_WARNINGS
        return ValidationGateDecision.PASS
```

---

## 40.9 ApprovalValidator

Valida approvazioni e richieste di approvazione.

```python
@dataclass
class ApprovalValidator:
    name: str = "ApprovalValidator"
    allowed_options: set[str] = field(default_factory=lambda: {
        "APPROVE", "REVISE", "MODIFY", "SCRAP", "KILL", "PAUSE", "RESUME", "ABORT"
    })

    def validate_request(self, target: ApprovalRequest, context: dict[str, Any] | None = None) -> ValidationReport:
        issues: list[ValidationIssue] = []
        warnings: list[ValidationIssue] = []

        if not target.approval_id:
            issues.append(ValidationIssue("APPROVAL_ID_MISSING", ValidationSeverity.BLOCKING, "approval_id mancante"))
        if not target.decision_needed:
            issues.append(ValidationIssue("APPROVAL_DECISION_MISSING", ValidationSeverity.ERROR, "decision_needed mancante"))
        if not target.options:
            issues.append(ValidationIssue("APPROVAL_OPTIONS_MISSING", ValidationSeverity.BLOCKING, "options mancanti"))
        invalid_options = [opt for opt in target.options if opt not in self.allowed_options]
        if invalid_options:
            issues.append(ValidationIssue(
                code="APPROVAL_INVALID_OPTIONS",
                severity=ValidationSeverity.ERROR,
                message=f"Opzioni non valide: {invalid_options}",
                field="options",
            ))
        if target.recommended_option not in target.options:
            issues.append(ValidationIssue(
                code="APPROVAL_RECOMMENDATION_NOT_IN_OPTIONS",
                severity=ValidationSeverity.ERROR,
                message="recommended_option non è presente in options",
                field="recommended_option",
            ))

        decision = self._decision_from_issues(issues, warnings)
        return ValidationReport(
            report_id=f"val_{uuid.uuid4().hex[:12]}",
            target_type=ValidationTargetType.APPROVAL_REQUEST,
            target_id=target.approval_id,
            valid=decision in {ValidationGateDecision.PASS, ValidationGateDecision.PASS_WITH_WARNINGS},
            decision=decision,
            issues=issues,
            warnings=warnings,
            validator=self.name,
            created_at=datetime.now(timezone.utc).isoformat(),
        )

    def validate_task_approval_state(self, task: RuntimeTask) -> ValidationReport:
        issues: list[ValidationIssue] = []
        warnings: list[ValidationIssue] = []

        if task.risk_level in APPROVAL_REQUIRED_FOR and not task.requires_approval:
            issues.append(ValidationIssue(
                code="TASK_A2_PLUS_WITHOUT_APPROVAL_FLAG",
                severity=ValidationSeverity.BLOCKING,
                message="Task A2+ senza requires_approval=True",
                field="requires_approval",
            ))

        if task.risk_level in APPROVAL_REQUIRED_FOR and task.status not in {TaskStatus.WAITING_APPROVAL, TaskStatus.DONE, TaskStatus.BLOCKED}:
            issues.append(ValidationIssue(
                code="TASK_A2_PLUS_NOT_WAITING_APPROVAL",
                severity=ValidationSeverity.BLOCKING,
                message="Task A2+ non deve entrare in esecuzione senza approvazione",
                field="status",
            ))

        decision = self._decision_from_issues(issues, warnings)
        return ValidationReport(
            report_id=f"val_{uuid.uuid4().hex[:12]}",
            target_type=ValidationTargetType.TASK,
            target_id=task.task_id,
            valid=decision in {ValidationGateDecision.PASS, ValidationGateDecision.PASS_WITH_WARNINGS},
            decision=decision,
            issues=issues,
            warnings=warnings,
            validator=self.name,
            created_at=datetime.now(timezone.utc).isoformat(),
        )

    @staticmethod
    def _decision_from_issues(issues: list[ValidationIssue], warnings: list[ValidationIssue]) -> ValidationGateDecision:
        if any(issue.severity == ValidationSeverity.BLOCKING for issue in issues):
            return ValidationGateDecision.BLOCK
        if any(issue.severity == ValidationSeverity.ERROR for issue in issues):
            return ValidationGateDecision.REVISE
        if warnings:
            return ValidationGateDecision.PASS_WITH_WARNINGS
        return ValidationGateDecision.PASS
```

---

## 40.10 FileSystemPlanValidator

```python
@dataclass
class FileSystemPlanValidator:
    name: str = "FileSystemPlanValidator"

    def validate(self, target: FileSystemPlan, context: dict[str, Any] | None = None) -> ValidationReport:
        issues: list[ValidationIssue] = []
        warnings: list[ValidationIssue] = []

        if not target.actions:
            issues.append(ValidationIssue(
                code="FS_PLAN_NO_ACTIONS",
                severity=ValidationSeverity.BLOCKING,
                message="FileSystemPlan senza azioni",
                field="actions",
            ))

        if target.requires_approval and not target.approved:
            issues.append(ValidationIssue(
                code="FS_PLAN_APPROVAL_REQUIRED",
                severity=ValidationSeverity.BLOCKING,
                message="FileSystemPlan richiede approvazione prima dell’esecuzione",
                field="approved",
            ))

        if not target.dry_run_passed:
            issues.append(ValidationIssue(
                code="FS_PLAN_DRY_RUN_REQUIRED",
                severity=ValidationSeverity.BLOCKING,
                message="FileSystemPlan deve superare dry-run prima dell’esecuzione",
                field="dry_run_passed",
            ))

        for idx, action in enumerate(target.actions):
            if action.risk_level in APPROVAL_REQUIRED_FOR and not action.approved:
                issues.append(ValidationIssue(
                    code="FS_ACTION_A2_PLUS_NOT_APPROVED",
                    severity=ValidationSeverity.BLOCKING,
                    message=f"Azione filesystem A2+ non approvata: {action.action_id}",
                    field=f"actions[{idx}].approved",
                ))

        decision = self._decision_from_issues(issues, warnings)
        return ValidationReport(
            report_id=f"val_{uuid.uuid4().hex[:12]}",
            target_type=ValidationTargetType.FILESYSTEM_PLAN,
            target_id=target.plan_id,
            valid=decision in {ValidationGateDecision.PASS, ValidationGateDecision.PASS_WITH_WARNINGS},
            decision=decision,
            issues=issues,
            warnings=warnings,
            validator=self.name,
            created_at=datetime.now(timezone.utc).isoformat(),
        )

    @staticmethod
    def _decision_from_issues(issues: list[ValidationIssue], warnings: list[ValidationIssue]) -> ValidationGateDecision:
        if any(issue.severity == ValidationSeverity.BLOCKING for issue in issues):
            return ValidationGateDecision.BLOCK
        if any(issue.severity == ValidationSeverity.ERROR for issue in issues):
            return ValidationGateDecision.REVISE
        if warnings:
            return ValidationGateDecision.PASS_WITH_WARNINGS
        return ValidationGateDecision.PASS
```

---

## 40.11 ValidationStore

I report di validazione vengono salvati in JSONL append-only.

Path:

```text
[progetto]/.agents/runtime/validation-reports.jsonl
centro-di-comando/runtime/validation-reports.jsonl
```

```python
class ValidationStore(Protocol):
    def append(self, report: ValidationReport) -> None:
        ...


@dataclass
class JsonlValidationStore:
    path: Path

    def append(self, report: ValidationReport) -> None:
        self.path.parent.mkdir(parents=True, exist_ok=True)
        with self.path.open("a", encoding="utf-8") as f:
            f.write(json.dumps(report.to_dict(), ensure_ascii=False) + "\n")
```

---

## 40.12 ValidationGate

`ValidationGate` è il punto unico di validazione prima di output utente o esecuzione.

```python
@dataclass
class ValidationGate:
    validation_store: ValidationStore | None = None
    decision_box_validator: DecisionBoxValidator = field(default_factory=DecisionBoxValidator)
    caesar_output_validator: CaesarOutputValidator = field(default_factory=CaesarOutputValidator)
    masterplan_validator: MasterPlanValidator = field(default_factory=MasterPlanValidator)
    ade_validator: ADEValidator = field(default_factory=ADEValidator)
    approval_validator: ApprovalValidator = field(default_factory=ApprovalValidator)
    filesystem_plan_validator: FileSystemPlanValidator = field(default_factory=FileSystemPlanValidator)

    def validate(self, target: Any, target_type: ValidationTargetType, context: dict[str, Any] | None = None) -> ValidationReport:
        if target_type == ValidationTargetType.CAESAR_OUTPUT:
            report = self.caesar_output_validator.validate(target, context)
        elif target_type == ValidationTargetType.DECISION_BOX:
            report = self.decision_box_validator.validate(target, context)
        elif target_type == ValidationTargetType.MASTERPLAN:
            report = self.masterplan_validator.validate(target, context)
        elif target_type == ValidationTargetType.ADE_REPORT:
            report = self.ade_validator.validate(target, context)
        elif target_type == ValidationTargetType.APPROVAL_REQUEST:
            report = self.approval_validator.validate_request(target, context)
        elif target_type == ValidationTargetType.TASK:
            report = self.approval_validator.validate_task_approval_state(target)
        elif target_type == ValidationTargetType.FILESYSTEM_PLAN:
            report = self.filesystem_plan_validator.validate(target, context)
        elif target_type == ValidationTargetType.AGENT_MESSAGE:
            msg_report = validate_agent_message(target)
            report = self._from_message_validation(target, msg_report)
        else:
            report = ValidationReport(
                report_id=f"val_{uuid.uuid4().hex[:12]}",
                target_type=target_type,
                target_id=None,
                valid=False,
                decision=ValidationGateDecision.BLOCK,
                issues=[ValidationIssue(
                    code="VALIDATOR_NOT_IMPLEMENTED",
                    severity=ValidationSeverity.BLOCKING,
                    message=f"Validator non implementato per {target_type.value}",
                )],
                created_at=datetime.now(timezone.utc).isoformat(),
            )

        if self.validation_store:
            self.validation_store.append(report)
        return report

    def enforce(self, target: Any, target_type: ValidationTargetType, context: dict[str, Any] | None = None) -> ValidationReport:
        report = self.validate(target, target_type, context)
        if report.decision in {ValidationGateDecision.BLOCK, ValidationGateDecision.ESCALATE}:
            raise PermissionError(f"ValidationGate blocked: {[issue.message for issue in report.issues]}")
        if report.decision == ValidationGateDecision.REVISE:
            raise ValueError(f"ValidationGate requires revision: {[issue.message for issue in report.issues]}")
        return report

    @staticmethod
    def _from_message_validation(message: AgentMessage, result: MessageValidationResult) -> ValidationReport:
        issues = [
            ValidationIssue(
                code="AGENT_MESSAGE_INVALID",
                severity=ValidationSeverity.BLOCKING,
                message=err,
            ) for err in result.errors
        ]
        warnings = [
            ValidationIssue(
                code="AGENT_MESSAGE_WARNING",
                severity=ValidationSeverity.WARNING,
                message=warn,
            ) for warn in result.warnings
        ]
        decision = ValidationGateDecision.PASS
        if issues:
            decision = ValidationGateDecision.BLOCK
        elif warnings:
            decision = ValidationGateDecision.PASS_WITH_WARNINGS
        return ValidationReport(
            report_id=f"val_{uuid.uuid4().hex[:12]}",
            target_type=ValidationTargetType.AGENT_MESSAGE,
            target_id=message.message_id,
            valid=not issues,
            decision=decision,
            issues=issues,
            warnings=warnings,
            validator="AgentMessageValidator",
            created_at=datetime.now(timezone.utc).isoformat(),
        )
```

---

## 40.13 Integrazione con Caesar Runtime

```python
@dataclass
class CaesarValidatedRuntime:
    validation_gate: ValidationGate
    error_classifier: ErrorClassifier
    error_manager: ErrorManager

    def validate_before_user_output(self, output: str, operational: bool = True) -> ValidationReport:
        return self.validation_gate.enforce(
            output,
            ValidationTargetType.CAESAR_OUTPUT,
            context={"operational": operational},
        )

    def validate_before_masterplan_presentation(self, masterplan: MasterPlan) -> ValidationReport:
        return self.validation_gate.enforce(masterplan, ValidationTargetType.MASTERPLAN)

    def validate_before_ade_presentation(self, ade_report: ADEReport) -> ValidationReport:
        return self.validation_gate.enforce(ade_report, ValidationTargetType.ADE_REPORT)

    def validate_before_filesystem_execution(self, plan: FileSystemPlan) -> ValidationReport:
        return self.validation_gate.enforce(plan, ValidationTargetType.FILESYSTEM_PLAN)

    def validate_task_before_execution(self, task: RuntimeTask) -> ValidationReport:
        return self.validation_gate.enforce(task, ValidationTargetType.TASK)
```

---

## 40.14 Gate Matrix

| Oggetto | Validator | Se fallisce |
|---|---|---|
| Output Caesar operativo | `CaesarOutputValidator` + `DecisionBoxValidator` | `REVISE` o `BLOCK` |
| DecisionBox | `DecisionBoxValidator` | `REVISE` o `BLOCK` |
| MasterPlan | `MasterPlanValidator` | torna a L14 |
| ADE Report | `ADEValidator` | torna a L19 |
| ApprovalRequest | `ApprovalValidator` | Caesar rigenera richiesta |
| RuntimeTask | `ApprovalValidator.validate_task_approval_state` | blocco esecuzione |
| FileSystemPlan | `FileSystemPlanValidator` | blocco executor |
| AgentMessage | `validate_agent_message` | blocco MessageBus/Gateway |

---

## 40.15 Regole operative ValidationGate

```text
1. Output operativo senza DecisionBox valida = rifiutato.
2. MasterPlan con completeness_score < 0.90 = bloccato.
3. MasterPlan budget > 50€ senza ADE = bloccato.
4. ADE senza 10 categorie = bloccato.
5. ADE con rischio catastrofico >15% e verdetto non ABORT = bloccato.
6. ApprovalRequest senza opzioni valide = bloccata.
7. Task A2+ senza approval flag = bloccato.
8. FileSystemPlan senza dry-run passato = bloccato.
9. FileSystemPlan A2+ non approvato = bloccato.
10. AgentMessage payload incompleto = bloccato.
11. Ogni ValidationReport viene salvato append-only se ValidationStore è attivo.
12. ValidationGate non corregge direttamente: blocca, richiede revisione o passa.
```

---

## 40.16 Stato del punto implementato

| Punto runtime | Stato |
|---|---|
| Come valida DecisionBox, MasterPlan, ADE e approvazioni | Implementato |
| `ValidationIssue` | Implementato |
| `ValidationReport` | Implementato |
| `Validator` protocol | Implementato |
| `DecisionBoxValidator` | Implementato |
| `CaesarOutputValidator` | Implementato |
| `MasterPlanValidator` | Implementato |
| `ADEValidator` | Implementato |
| `ApprovalValidator` | Implementato |
| `FileSystemPlanValidator` | Implementato |
| `ValidationStore` | Implementato |
| `ValidationGate` | Implementato |
| Integrazione Caesar runtime | Implementata |
| Gate matrix | Implementata |

```text
┌─ LA DECISIONE ─────────────────────────────────────────────────┐
│ Scelta: Usare ValidationGate prima di output utente o azioni esecutive │
│ Perché: Blocca piani, ADE, approvazioni e DecisionBox non conformi │
└────────────────────────────────────────────────────────────────┘
```


---

## 41. Runtime Execution Layer — Direct Critical Thinking Policy

Questa sezione implementa la skill **Direct Critical Thinking Assistant** come policy globale, non come tono opzionale.

Regola chiave:

```text
Prima viene la qualità della decisione.
Poi viene il comfort conversazionale.
```

Priorità obbligatoria:

```text
1. Accuratezza
2. Sicurezza
3. Utilità
4. Chiarezza
5. Direttezza
6. Tono
```

Decisione architetturale:

```text
Direct Critical Thinking non è un nuovo agente.
Direct Critical Thinking è un Response Policy Layer integrato nel ValidationGate.
```

---

## 41.1 Scopo operativo

Caesar, Afrodite e i Legionari devono evitare l’assistente accondiscendente.

Devono invece:

- correggere assunzioni deboli;
- identificare rischi;
- mostrare alternative migliori;
- dichiarare assunzioni;
- usare confidence label sui claim importanti;
- dissentire quando serve;
- fare una sola domanda chiarificatrice quando l’informazione mancante è essenziale.

Non devono:

- aprire con accordo generico;
- validare ragionamenti deboli;
- nascondere incertezza;
- suonare più certi dei dati disponibili;
- ammorbidire un disaccordo necessario;
- chiedere chiarimenti inutili;
- sacrificare utilità per tono piacevole.

---

## 41.2 ResponsePolicy

```python
@dataclass(frozen=True)
class ResponsePolicy:
    profile: ResponseProfile = ResponseProfile.DIRECT_CRITICAL
    avoid_generic_agreement: bool = True
    expose_weak_assumptions: bool = True
    require_confidence_labels_for_key_claims: bool = True
    require_assumption_disclosure_for_strategic_outputs: bool = True
    require_disagreement_structure: bool = True
    ask_only_essential_clarifying_questions: bool = True
    max_clarifying_questions: int = 1
    prioritize_usefulness_over_tone: bool = True
    block_generic_agreement_on_strategic_outputs: bool = True
    block_high_impact_missed_risk: bool = True
    warn_on_missing_confidence_label: bool = True


DEFAULT_RESPONSE_POLICY = ResponsePolicy()
```

---

## 41.3 User Preference Profile

Il comportamento può essere configurato per utente senza indebolire i guardrail globali.

```python
@dataclass
class UserPreferenceProfile:
    user_id: str
    preferred_response_profile: ResponseProfile = ResponseProfile.DIRECT_CRITICAL
    allow_blunt_feedback: bool = True
    require_confidence_labels: bool = True
    max_tone_softening: int = 1  # 0=molto diretto, 3=più morbido
```

Profilo consigliato per l’utente proprietario del Castello:

```json
{
  "preferred_response_profile": "DIRECT_CRITICAL",
  "allow_blunt_feedback": true,
  "require_confidence_labels": true,
  "max_tone_softening": 1
}
```

---

## 41.4 CriticalThinkingAssessment

```python
@dataclass
class CriticalThinkingAssessment:
    weakest_assumption: str | None = None
    main_risk: str | None = None
    better_alternative: str | None = None
    practical_next_step: str | None = None
    missing_essential_info: str | None = None
    should_disagree: bool = False
    disagreement_reason: str | None = None
    confidence: ConfidenceLabel = ConfidenceLabel.LIKELY
    flags: list[ResponseRiskFlag] = field(default_factory=list)
    output_mode: OutputMode = OutputMode.STANDARD_OPERATIONAL
    critical_review_required: bool = False
```

---

## 41.5 Quando è richiesta critical review

```python
CRITICAL_REVIEW_REQUIRED_FOR = {
    "strategy",
    "planning",
    "evaluation",
    "business_decision",
    "budget_decision",
    "launch",
    "marketing_campaign",
    "technical_architecture",
    "legal_or_financial_sensitive",
}


def requires_critical_review(command: Command, routing: RoutingDecision | None = None, task: RuntimeTask | None = None) -> bool:
    text = command.normalized_text.lower()
    keywords = [
        "strategia", "piano", "valuta", "che ne pensi", "decisione",
        "business", "lancio", "budget", "rischio", "architettura",
        "implementare", "miglioramento", "critica", "validazione",
    ]

    if any(k in text for k in keywords):
        return True

    if routing and routing.target_agent in {"L6", "L8", "L15", "L19"}:
        return True

    if task and task.task_type in {
        TaskType.VALIDATION,
        TaskType.PLANNING,
        TaskType.PRE_MORTEM,
        TaskType.QA,
        TaskType.MARKETING,
    }:
        return True

    if task and task.risk_level in {ActionLevel.A2, ActionLevel.A3, ActionLevel.A4}:
        return True

    return False
```

---

## 41.6 CriticalThinkingValidator

Questo validator si integra nel `ValidationGate`. Non sostituisce `DecisionBoxValidator`, `MasterPlanValidator` o `ADEValidator`: li completa.

```python
@dataclass
class CriticalThinkingValidator:
    name: str = "CriticalThinkingValidator"
    policy: ResponsePolicy = DEFAULT_RESPONSE_POLICY

    banned_generic_openings: tuple[str, ...] = (
        "ottima domanda",
        "hai assolutamente ragione",
        "sono completamente d'accordo",
        "sono completamente d’accordo",
        "assolutamente",
        "certamente",
        "grande idea",
        "ottimo punto",
        "perfetto",
    )

    def assess(
        self,
        user_command: Command,
        draft_response: str,
        context: dict[str, Any] | None = None,
    ) -> CriticalThinkingAssessment:
        context = context or {}
        routing = context.get("routing_decision")
        task = context.get("task")
        critical_required = requires_critical_review(user_command, routing, task)

        flags: list[ResponseRiskFlag] = []
        opening = draft_response.strip().lower()[:160]

        if any(opening.startswith(x) for x in self.banned_generic_openings):
            flags.append(ResponseRiskFlag.GENERIC_AGREEMENT)

        if critical_required and "[ASSUNZIONI]" not in draft_response and "Assunzione:" not in draft_response:
            flags.append(ResponseRiskFlag.WEAK_ASSUMPTION)

        if critical_required and "rischio" not in draft_response.lower():
            flags.append(ResponseRiskFlag.MISSED_RISK)

        if "[Guessing]" in draft_response:
            confidence = ConfidenceLabel.GUESSING
        elif "[Certain]" in draft_response:
            confidence = ConfidenceLabel.CERTAIN
        else:
            confidence = ConfidenceLabel.LIKELY

        output_mode = OutputMode.CRITICAL_STRATEGIC if critical_required else OutputMode.STANDARD_OPERATIONAL

        return CriticalThinkingAssessment(
            weakest_assumption=None,
            main_risk=None,
            better_alternative=None,
            practical_next_step=None,
            missing_essential_info=context.get("missing_essential_info"),
            should_disagree=bool(context.get("should_disagree", False)),
            disagreement_reason=context.get("disagreement_reason"),
            confidence=confidence,
            flags=flags,
            output_mode=output_mode,
            critical_review_required=critical_required,
        )

    def validate(self, target: str, context: dict[str, Any] | None = None) -> ValidationReport:
        context = context or {}
        command = context.get("command")
        assessment = context.get("critical_assessment")

        issues: list[ValidationIssue] = []
        warnings: list[ValidationIssue] = []

        if command is None:
            warnings.append(ValidationIssue(
                code="CRITICAL_CONTEXT_COMMAND_MISSING",
                severity=ValidationSeverity.WARNING,
                message="Command mancante nel contesto: validazione critica meno affidabile",
            ))
            assessment = assessment or CriticalThinkingAssessment()
        else:
            assessment = assessment or self.assess(command, target, context)

        strategic = assessment.output_mode == OutputMode.CRITICAL_STRATEGIC or assessment.critical_review_required

        if self.policy.avoid_generic_agreement and ResponseRiskFlag.GENERIC_AGREEMENT in assessment.flags:
            severity = ValidationSeverity.BLOCKING if strategic and self.policy.block_generic_agreement_on_strategic_outputs else ValidationSeverity.WARNING
            issue = ValidationIssue(
                code="CRITICAL_GENERIC_AGREEMENT_OPENING",
                severity=severity,
                message="Apertura generica/accondiscendente non consentita per output critico",
                fix_hint="Aprire con rischio, correzione, assunzione o prossima mossa",
            )
            (issues if severity == ValidationSeverity.BLOCKING else warnings).append(issue)

        if strategic and self.policy.require_assumption_disclosure_for_strategic_outputs:
            has_assumption_marker = any(marker in target for marker in ["[ASSUNZIONI]", "Assunzione:", "Assumption:"])
            if not has_assumption_marker:
                issues.append(ValidationIssue(
                    code="CRITICAL_ASSUMPTIONS_MISSING",
                    severity=ValidationSeverity.ERROR,
                    message="Output strategico senza assunzioni dichiarate",
                    fix_hint="Aggiungere [ASSUNZIONI] o dichiarare Nessuna assunzione critica",
                ))

        if strategic and ResponseRiskFlag.MISSED_RISK in assessment.flags:
            severity = ValidationSeverity.BLOCKING if self.policy.block_high_impact_missed_risk else ValidationSeverity.ERROR
            issues.append(ValidationIssue(
                code="CRITICAL_MAIN_RISK_MISSING",
                severity=severity,
                message="Output critico/strategico senza rischio principale esplicito",
                fix_hint="Aggiungere [CORREZIONE / RISCHIO PRINCIPALE] o [PUNTO DEBOLE]",
            ))

        if assessment.missing_essential_info:
            question_count = target.count("?")
            if question_count > self.policy.max_clarifying_questions:
                issues.append(ValidationIssue(
                    code="CRITICAL_TOO_MANY_CLARIFYING_QUESTIONS",
                    severity=ValidationSeverity.ERROR,
                    message="Troppe domande chiarificatrici",
                    fix_hint="Fare una sola domanda diretta se il dato è essenziale",
                ))
            if "Assunzione:" not in target and "Assumption:" not in target and question_count == 0:
                warnings.append(ValidationIssue(
                    code="CRITICAL_MISSING_INFO_NOT_HANDLED",
                    severity=ValidationSeverity.WARNING,
                    message="Informazione mancante non gestita con domanda o assunzione esplicita",
                ))

        if self.policy.require_confidence_labels_for_key_claims:
            speculative = assessment.confidence == ConfidenceLabel.GUESSING or ResponseRiskFlag.MISSING_DATA in assessment.flags
            if speculative and "[Guessing]" not in target:
                warnings.append(ValidationIssue(
                    code="CRITICAL_GUESSING_LABEL_MISSING",
                    severity=ValidationSeverity.WARNING,
                    message="Claim speculativo senza [Guessing]",
                ))

        if assessment.should_disagree and self.policy.require_disagreement_structure:
            lower = target.lower()
            required_fragments = ["non sono d'accordo", "rischio", "farei invece"]
            alt_fragments = ["non sono d’accordo", "rischio", "farei invece"]
            ok = all(fragment in lower for fragment in required_fragments) or all(fragment in lower for fragment in alt_fragments)
            if not ok:
                issues.append(ValidationIssue(
                    code="CRITICAL_DISAGREEMENT_PROTOCOL_MISSING",
                    severity=ValidationSeverity.ERROR,
                    message="Disaccordo richiesto ma non strutturato correttamente",
                    fix_hint="Usare: Non sono d’accordo perché... Farei invece... Il rischio...",
                ))

        decision = self._decision_from_issues(issues, warnings)
        return ValidationReport(
            report_id=f"val_{uuid.uuid4().hex[:12]}",
            target_type=ValidationTargetType.CRITICAL_THINKING,
            target_id=context.get("output_id"),
            valid=decision in {ValidationGateDecision.PASS, ValidationGateDecision.PASS_WITH_WARNINGS},
            decision=decision,
            issues=issues,
            warnings=warnings,
            validator=self.name,
            created_at=datetime.now(timezone.utc).isoformat(),
            metadata={
                "output_mode": assessment.output_mode.value,
                "flags": [flag.value for flag in assessment.flags],
                "confidence": assessment.confidence.value,
                "critical_review_required": assessment.critical_review_required,
            },
        )

    @staticmethod
    def _decision_from_issues(issues: list[ValidationIssue], warnings: list[ValidationIssue]) -> ValidationGateDecision:
        if any(issue.severity == ValidationSeverity.BLOCKING for issue in issues):
            return ValidationGateDecision.BLOCK
        if any(issue.severity == ValidationSeverity.ERROR for issue in issues):
            return ValidationGateDecision.REVISE
        if warnings:
            return ValidationGateDecision.PASS_WITH_WARNINGS
        return ValidationGateDecision.PASS
```

---

## 41.7 ValidationGateV2

`ValidationGateV2` estende `ValidationGate` aggiungendo `CriticalThinkingValidator` agli output Caesar e agli output strategici.

```python
@dataclass
class ValidationGateV2(ValidationGate):
    critical_thinking_validator: CriticalThinkingValidator = field(default_factory=CriticalThinkingValidator)

    def validate(self, target: Any, target_type: ValidationTargetType, context: dict[str, Any] | None = None) -> ValidationReport:
        context = context or {}

        base_report = super().validate(target, target_type, context)

        should_apply_critical = (
            target_type == ValidationTargetType.CAESAR_OUTPUT
            or context.get("critical_review_required", False)
            or context.get("output_mode") == OutputMode.CRITICAL_STRATEGIC
        )

        if not should_apply_critical or not isinstance(target, str):
            return base_report

        critical_report = self.critical_thinking_validator.validate(target, context)

        combined_issues = base_report.issues + critical_report.issues
        combined_warnings = base_report.warnings + critical_report.warnings
        combined_decision = self._combine_decisions(base_report.decision, critical_report.decision)
        combined_report = ValidationReport(
            report_id=f"val_{uuid.uuid4().hex[:12]}",
            target_type=target_type,
            target_id=base_report.target_id,
            valid=combined_decision in {ValidationGateDecision.PASS, ValidationGateDecision.PASS_WITH_WARNINGS},
            decision=combined_decision,
            issues=combined_issues,
            warnings=combined_warnings,
            validator="ValidationGateV2",
            created_at=datetime.now(timezone.utc).isoformat(),
            metadata={
                "base_report_id": base_report.report_id,
                "critical_report_id": critical_report.report_id,
            },
        )
        if self.validation_store:
            self.validation_store.append(combined_report)
        return combined_report

    @staticmethod
    def _combine_decisions(a: ValidationGateDecision, b: ValidationGateDecision) -> ValidationGateDecision:
        order = {
            ValidationGateDecision.PASS: 0,
            ValidationGateDecision.PASS_WITH_WARNINGS: 1,
            ValidationGateDecision.REVISE: 2,
            ValidationGateDecision.BLOCK: 3,
            ValidationGateDecision.ESCALATE: 4,
        }
        return max([a, b], key=lambda d: order[d])
```

---

## 41.8 Output critico-strategico Caesar

Per output strategici, valutativi, architetturali o decisionali, Caesar usa questo formato:

```text
[CORREZIONE / RISCHIO PRINCIPALE]
La cosa più importante da non ignorare.

[ASSUNZIONI]
Assunzione 1...
Assunzione 2...
Se nessuna: "Nessuna assunzione critica."

[ANALISI]
Ragionamento sintetico.

[ALTERNATIVA MIGLIORE]
Cosa fare invece o come migliorare.

[PROSSIMA MOSSA]
Azione pratica immediata.

[RICHIESTA]
APPROVE / REVISE / SCRAP / KILL / PAUSE

┌─ LA DECISIONE ─────────────────────────────────────────────────┐
│ Scelta: [max 120 caratteri]                                    │
│ Perché: [max 140 caratteri]                                    │
└────────────────────────────────────────────────────────────────┘
```

Per output non operativi ma valutativi leggeri:

```text
[PUNTO DEBOLE]
[PERCHÉ CONTA]
[OPZIONE MIGLIORE]
[PROSSIMO PASSO]
[ASSUNZIONI / DOMANDE APERTE]
```

Regola:

```text
Il formato critico-strategico non sostituisce la DecisionBox quando l’output è operativo.
```

---

## 41.9 Profili agente critici

```python
STRICT_CRITICAL_AGENTS = {"L6", "L8", "L15", "L19"}
STANDARD_CRITICAL_AGENTS = {"Caesar", "Afrodite", "L10", "L14", "L20", "L21", "L22"}
CREATIVE_BUT_NOT_ACCOMMODATING_AGENTS = {"L9", "L12"}

AGENT_CRITICALITY_OVERRIDES = {
    "L6": {"response_profile": ResponseProfile.DIRECT_CRITICAL, "criticality_level": 3},
    "L8": {"response_profile": ResponseProfile.DIRECT_CRITICAL, "criticality_level": 3},
    "L15": {"response_profile": ResponseProfile.DIRECT_CRITICAL, "criticality_level": 3},
    "L19": {"response_profile": ResponseProfile.DIRECT_CRITICAL, "criticality_level": 3},
    "L9": {"response_profile": ResponseProfile.STANDARD, "criticality_level": 1},
    "L12": {"response_profile": ResponseProfile.STANDARD, "criticality_level": 1},
}
```

Regola:

```text
L6, L8, L15 e L19 non possono usare profilo SUPPORTIVE per output valutativi.
```

---

## 41.10 Critical Review Payload per Agent Communication

I message type `CRITICAL_REVIEW_REQUEST` e `CRITICAL_REVIEW_RESPONSE` sono aggiunti ad `AgentMessageType`.

```python
@dataclass
class CriticalReviewPayload:
    weakest_assumption: str
    main_risk: str
    missed_counterargument: str | None
    better_alternative: str | None
    confidence: ConfidenceLabel
    should_block: bool
    reason_if_blocked: str | None = None

    def to_payload(self) -> dict[str, Any]:
        return {
            "weakest_assumption": self.weakest_assumption,
            "main_risk": self.main_risk,
            "missed_counterargument": self.missed_counterargument,
            "better_alternative": self.better_alternative,
            "confidence": self.confidence.value,
            "should_block": self.should_block,
            "reason_if_blocked": self.reason_if_blocked,
        }
```

Pattern:

```text
L14 crea piano
↓
L14 invia CRITICAL_REVIEW_REQUEST a L19/ADE o L8/QA
↓
L19/L8 risponde CRITICAL_REVIEW_RESPONSE
↓
Se should_block=True, Caesar blocca e chiede revisione o decisione utente
```

---

## 41.11 ModelOutputIssue per Error Handling

```python
class ModelOutputIssue(str, Enum):
    GENERIC_AGREEMENT = "GENERIC_AGREEMENT"
    UNSUPPORTED_CONFIDENCE = "UNSUPPORTED_CONFIDENCE"
    HIDDEN_ASSUMPTION = "HIDDEN_ASSUMPTION"
    MISSED_RISK = "MISSED_RISK"
    WEAK_RECOMMENDATION = "WEAK_RECOMMENDATION"
    POLICY_VIOLATION = "POLICY_VIOLATION"
```

Uso in `ErrorEvent.metadata`:

```python
MODEL_OUTPUT_ERROR_METADATA_EXAMPLE = {
    "issue": ModelOutputIssue.MISSED_RISK.value,
    "response_profile": ResponseProfile.DIRECT_CRITICAL.value,
    "repair_action": "REWRITE_WITH_CRITICAL_OPENING",
}
```

Regola:

```text
Non ogni warning stilistico diventa ErrorEvent.
ErrorEvent MODEL_OUTPUT si usa solo per omissioni importanti, overconfidence grave, rischio alto mancato o violazione policy.
```

---

## 41.12 Prompt Registry versionato

Il comportamento non deve vivere solo nel Markdown. Deve avere prompt runtime versionati.

Struttura:

```text
.agents/prompts/
├── manifest.json
├── system/
│   └── direct-critical-thinking.md
├── agents/
│   ├── caesar.md
│   ├── l06-validatore.md
│   ├── l08-qa.md
│   └── l19-ade.md
└── response-policies/
    └── direct-critical.json
```

```python
@dataclass(frozen=True)
class PromptSpec:
    prompt_id: str
    path: Path
    version: str
    applies_to: tuple[str, ...]
    required: bool = True
    checksum: str | None = None


PROMPT_REGISTRY = {
    "direct-critical-system": PromptSpec(
        prompt_id="direct-critical-system",
        path=Path(".agents/prompts/system/direct-critical-thinking.md"),
        version="4.2.0",
        applies_to=("Caesar", "Afrodite", "L1-L23"),
        required=True,
    ),
    "direct-critical-policy": PromptSpec(
        prompt_id="direct-critical-policy",
        path=Path(".agents/prompts/response-policies/direct-critical.json"),
        version="4.2.0",
        applies_to=("ValidationGateV2", "CriticalThinkingValidator"),
        required=True,
    ),
}
```

---

## 41.13 Test automatici consigliati

```text
tests/test_response_policy.py
tests/test_confidence_labels.py
tests/test_disagreement_protocol.py
tests/test_assumption_disclosure.py
tests/test_output_quality_gate.py
tests/test_critical_review_messages.py
```

Test minimi:

```python
def test_direct_critical_opening_blocks_generic_agreement():
    response = "Ottima domanda, sono d'accordo con te..."
    command = Command(
        command_id="cmd_test",
        raw_text="Che ne pensi di questa strategia?",
        normalized_text="Che ne pensi di questa strategia?",
        source=CommandSource.CHAT,
        status=CommandStatus.READY_FOR_ROUTING,
        created_at="2026-06-15T00:00:00Z",
        context=CommandContext(user_id="utente"),
        idempotency_key="test",
    )
    gate = CriticalThinkingValidator()
    result = gate.validate(response, {"command": command})
    assert result.decision in {ValidationGateDecision.BLOCK, ValidationGateDecision.REVISE}


def test_strategic_output_requires_assumptions_and_risk():
    response = "[ANALISI]\nProcediamo subito."
    command = Command(
        command_id="cmd_test",
        raw_text="Valuta questo piano business",
        normalized_text="Valuta questo piano business",
        source=CommandSource.CHAT,
        status=CommandStatus.READY_FOR_ROUTING,
        created_at="2026-06-15T00:00:00Z",
        context=CommandContext(user_id="utente"),
        idempotency_key="test",
    )
    gate = CriticalThinkingValidator()
    result = gate.validate(response, {"command": command})
    assert not result.valid


def test_simple_status_does_not_require_critical_format():
    response = "Il progetto è in fase PLANNING."
    command = Command(
        command_id="cmd_test",
        raw_text="Status progetto",
        normalized_text="Status progetto",
        source=CommandSource.CHAT,
        status=CommandStatus.READY_FOR_ROUTING,
        created_at="2026-06-15T00:00:00Z",
        context=CommandContext(user_id="utente"),
        idempotency_key="test",
    )
    gate = CriticalThinkingValidator()
    result = gate.validate(response, {"command": command})
    assert result.decision in {ValidationGateDecision.PASS, ValidationGateDecision.PASS_WITH_WARNINGS}
```

---

## 41.14 Regole operative Direct Critical Thinking

```text
1. Direct Critical Thinking è policy globale, non agente separato.
2. Gli output strategici, valutativi e decisionali passano da CriticalThinkingValidator.
3. ValidationGateV2 combina validator strutturali e validator critico.
4. Generic agreement opening è bloccante negli output critici.
5. Output strategico senza rischio principale è bloccato o revisionato.
6. Output strategico senza assunzioni dichiarate è revisionato.
7. Claim speculativi importanti devono usare [Guessing].
8. Disaccordo richiesto deve seguire il protocollo: ragione, alternativa, rischio.
9. L6, L8, L15 e L19 usano profilo DIRECT_CRITICAL forzato.
10. Critical review tra agenti usa messaggi strutturati, non commenti liberi.
11. Prompt registry versionato rende la policy caricabile a runtime.
12. I test automatici verificano che la policy non venga degradata.
```

---

## 41.15 Stato della modifica implementata

| Punto | Stato |
|---|---|
| Direct Critical Thinking come Policy Layer | Implementato |
| Config globale in `CastelloConfig` | Implementata |
| Nuova legge L12 | Implementata |
| `ResponseProfile` | Implementato |
| `ConfidenceLabel` | Implementato |
| `ResponseRiskFlag` | Implementato |
| `ResponsePolicy` | Implementata |
| `CriticalThinkingAssessment` | Implementata |
| `CriticalThinkingValidator` | Implementato |
| Integrazione `ValidationGateV2` | Implementata |
| Profili critici per agenti | Implementati |
| Critical review message types | Implementati |
| `CriticalReviewPayload` | Implementato |
| `ModelOutputIssue` | Implementato |
| Prompt registry versionato | Implementato |
| Test plan | Implementato |

```text
┌─ LA DECISIONE ─────────────────────────────────────────────────┐
│ Scelta: Integrare Direct Critical Thinking in v4.2.1 dentro ValidationGateV2 │
│ Perché: Deve correggere ogni output importante, non vivere come tono opzionale │
└────────────────────────────────────────────────────────────────┘
```


---

## 42. Revisione completa di coerenza — Patch v4.2.1

Questa sezione registra la revisione completa della v4.2.0 e corregge i punti che potevano creare incoerenze implementative.

Sintesi netta:

```text
La v4.2.0 è architetturalmente completa, ma aveva alcuni punti runtime da rendere più coerenti:
- serializzazione Enum/dataclass nello StateStore;
- conflitto tra Output Standard Caesar e Output critico-strategico;
- MessageBus append-only senza vista compatta dello stato messaggi;
- ErrorStore append-only senza stato effettivo per errori risolti;
- Protocol StateStore incompleto rispetto agli usi successivi;
- profili critici agenti definiti ma non applicati al registro AGENTS.
```

Questa patch non cambia la filosofia del sistema. Corregge i punti di implementazione.

---

## 42.1 Esito revisione

| Area | Stato v4.2.0 | Patch v4.2.1 |
|---|---|---|
| Versioning | Coerente, con un riferimento storico vecchio | Riferimento normalizzato |
| Python syntax | Valida nei blocchi singoli | Nessuna correzione sintattica richiesta |
| StateStore | Parziale: `asdict()` non serializza bene Enum | Aggiunti serializer JSON-safe |
| StateStore Protocol | Parziale rispetto a metodi usati dopo | Aggiunto `StateStoreV2` |
| Caesar Output | Conflitto con formato critico-strategico | Aggiunto `CaesarOutputValidatorV2` |
| ValidationGate | Funzionale ma può loggare report duplicati | Aggiunto `ValidationGateV3` |
| MessageBus | Append-only ma inbox poteva mostrare stati obsoleti | Aggiunta vista compatta latest-state |
| ErrorStore | `latest_open()` poteva vedere errori già risolti | Aggiunta vista effettiva per `error_id` |
| Agent critical profiles | Definiti ma non applicati | Aggiunta funzione `apply_agent_criticality_overrides()` |
| Direct Critical Thinking | Corretto come policy layer | Mantenuto dentro ValidationGate |

---

## 42.2 JSON-safe serialization

Problema:

```text
RuntimeState.to_dict() usava asdict(project_state), ma ProjectState contiene Enum.
json.dumps() non serializza automaticamente Enum.
```

Patch:

```python
def to_jsonable(value: Any) -> Any:
    if isinstance(value, Enum):
        return value.value
    if isinstance(value, Path):
        return str(value)
    if hasattr(value, "to_dict") and callable(value.to_dict):
        return value.to_dict()
    if dataclasses.is_dataclass(value):
        return {k: to_jsonable(v) for k, v in asdict(value).items()}
    if isinstance(value, dict):
        return {str(k): to_jsonable(v) for k, v in value.items()}
    if isinstance(value, list):
        return [to_jsonable(v) for v in value]
    if isinstance(value, tuple):
        return [to_jsonable(v) for v in value]
    if isinstance(value, set):
        return [to_jsonable(v) for v in value]
    return value


def project_state_to_dict(state: ProjectState) -> dict[str, Any]:
    return to_jsonable(state)


def workflow_runtime_state_to_dict(state: WorkflowRuntimeState) -> dict[str, Any]:
    return to_jsonable(state)


def approval_runtime_state_to_dict(state: ApprovalRuntimeState) -> dict[str, Any]:
    return to_jsonable(state)
```

---

## 42.3 RuntimeStateV2

`RuntimeStateV2` sostituisce la serializzazione della v4.2.0 quando si implementa il runtime.

```python
@dataclass
class RuntimeStateV2(RuntimeState):
    def to_dict(self) -> dict[str, Any]:
        return {
            "scope": self.scope.value,
            "state_id": self.state_id,
            "updated_at": self.updated_at,
            "project_state": project_state_to_dict(self.project_state) if self.project_state else None,
            "workflow_state": workflow_runtime_state_to_dict(self.workflow_state) if self.workflow_state else None,
            "tasks": {task_id: task.to_dict() for task_id, task in self.tasks.items()},
            "approvals": {approval_id: approval_runtime_state_to_dict(approval) for approval_id, approval in self.approvals.items()},
            "last_command_id": self.last_command_id,
            "last_routing_decision": to_jsonable(self.last_routing_decision),
            "metadata": to_jsonable(self.metadata),
        }
```

Regola:

```text
Ogni snapshot JSON deve passare da to_jsonable() prima di json.dumps().
```

---

## 42.4 StateStoreV2 Protocol

Problema:

```text
Il protocollo StateStore non dichiarava tutti i metodi usati dopo da CaesarStatefulRuntime e dai moduli resume/error.
```

Patch:

```python
class StateStoreV2(StateStore, Protocol):
    def get_or_create(self) -> RuntimeState:
        ...

    def link_routing_decision(self, decision: RoutingDecision) -> RuntimeState:
        ...

    def update_approval(self, approval: ApprovalRuntimeState) -> RuntimeState:
        ...

    def append_state_error(self, error: ErrorEvent) -> RuntimeState:
        ...
```

Regola:

```text
Le implementazioni concrete devono esporre StateStoreV2, non solo StateStore, se usate dal runtime completo.
```

---

## 42.5 JsonStateStoreV2

```python
@dataclass
class JsonStateStoreV2(JsonStateStore):
    def save_snapshot(self, state: RuntimeState) -> None:
        self.runtime_paths.root.mkdir(parents=True, exist_ok=True)
        state.updated_at = self._now_iso()
        data = state.to_dict() if hasattr(state, "to_dict") else to_jsonable(state)
        self._atomic_write_json(self.runtime_paths.state_snapshot, to_jsonable(data))
        self.append_event(StateEvent(
            event_id=self.new_event_id(),
            timestamp=self._now_iso(),
            event_type=StateEventType.STATE_SNAPSHOT_WRITTEN,
            state_id=state.state_id,
            summary="Snapshot stato scritto su disco con serializzazione JSON-safe",
            project_id=state.project_state.project_id if state.project_state else None,
            idempotency_key=self.make_event_idempotency_key(
                StateEventType.STATE_SNAPSHOT_WRITTEN,
                state.state_id,
                state.updated_at,
            ),
        ))

    def update_approval(self, approval: ApprovalRuntimeState) -> RuntimeState:
        state = self.get_or_create()
        state.approvals[approval.approval_id] = approval
        state.updated_at = self._now_iso()
        self.save_snapshot(state)
        self.append_event(StateEvent(
            event_id=self.new_event_id(),
            timestamp=self._now_iso(),
            event_type=StateEventType.APPROVAL_UPDATED,
            state_id=state.state_id,
            summary=f"Approval aggiornata: {approval.approval_id} → {approval.status}",
            approval_id=approval.approval_id,
            idempotency_key=self.make_event_idempotency_key(
                StateEventType.APPROVAL_UPDATED,
                approval.approval_id,
                approval.status + str(approval.resolved_at),
            ),
        ))
        return state

    def append_state_error(self, error: ErrorEvent) -> RuntimeState:
        state = self.get_or_create()
        state.metadata.setdefault("state_errors", []).append(error.to_dict())
        state.updated_at = self._now_iso()
        self.save_snapshot(state)
        self.append_event(StateEvent(
            event_id=self.new_event_id(),
            timestamp=self._now_iso(),
            event_type=StateEventType.STATE_ERROR,
            state_id=state.state_id,
            summary=error.message,
            project_id=error.project_id,
            command_id=error.command_id,
            task_id=error.task_id,
            idempotency_key=self.make_event_idempotency_key(
                StateEventType.STATE_ERROR,
                state.state_id,
                error.error_id,
            ),
            payload=error.to_dict(),
        ))
        return state
```

---

## 42.6 Output mode precedence

Problema:

```text
La v4.2.0 aggiungeva un output critico-strategico, ma CaesarOutputValidator continuava a richiedere sempre il vecchio formato operativo.
```

Patch:

```text
Se output_mode = CRITICAL_STRATEGIC, il formato critico-strategico sostituisce le sezioni [STATO], [AZIONE PROPOSTA], [IMPATTO].
La DecisionBox resta obbligatoria per output operativo.
```

---

## 42.7 CaesarOutputValidatorV2

```python
@dataclass
class CaesarOutputValidatorV2(CaesarOutputValidator):
    critical_required_sections: tuple[str, ...] = (
        "[CORREZIONE / RISCHIO PRINCIPALE]",
        "[ASSUNZIONI]",
        "[ANALISI]",
        "[ALTERNATIVA MIGLIORE]",
        "[PROSSIMA MOSSA]",
        "[RICHIESTA]",
    )

    light_critical_sections: tuple[str, ...] = (
        "[PUNTO DEBOLE]",
        "[PERCHÉ CONTA]",
        "[OPZIONE MIGLIORE]",
        "[PROSSIMO PASSO]",
    )

    def validate(self, target: str, context: dict[str, Any] | None = None) -> ValidationReport:
        context = context or {}
        operational = context.get("operational", True)
        output_mode = context.get("output_mode", OutputMode.STANDARD_OPERATIONAL)
        if isinstance(output_mode, str):
            output_mode = OutputMode(output_mode)

        issues: list[ValidationIssue] = []
        warnings: list[ValidationIssue] = []

        if not operational:
            return ValidationReport(
                report_id=f"val_{uuid.uuid4().hex[:12]}",
                target_type=ValidationTargetType.CAESAR_OUTPUT,
                target_id=context.get("output_id"),
                valid=True,
                decision=ValidationGateDecision.PASS,
                issues=[],
                warnings=[],
                validator="CaesarOutputValidatorV2",
                created_at=datetime.now(timezone.utc).isoformat(),
            )

        if output_mode == OutputMode.CRITICAL_STRATEGIC:
            has_full = all(section in target for section in self.critical_required_sections)
            has_light = all(section in target for section in self.light_critical_sections)
            if not has_full and not has_light:
                issues.append(ValidationIssue(
                    code="CAESAR_CRITICAL_FORMAT_MISSING",
                    severity=ValidationSeverity.ERROR,
                    message="Output critico-strategico non rispetta formato richiesto",
                    fix_hint="Usare formato completo critico-strategico o formato leggero valutativo",
                ))
        elif output_mode == OutputMode.STANDARD_OPERATIONAL:
            for section in self.required_sections:
                if section not in target:
                    issues.append(ValidationIssue(
                        code="CAESAR_OUTPUT_SECTION_MISSING",
                        severity=ValidationSeverity.ERROR,
                        message=f"Sezione mancante: {section}",
                        field=section,
                    ))

        if operational:
            db_report = self.decision_box_validator.validate(target)
            issues.extend(db_report.issues)
            warnings.extend(db_report.warnings)

        decision = self._decision_from_issues(issues, warnings)
        return ValidationReport(
            report_id=f"val_{uuid.uuid4().hex[:12]}",
            target_type=ValidationTargetType.CAESAR_OUTPUT,
            target_id=context.get("output_id"),
            valid=decision in {ValidationGateDecision.PASS, ValidationGateDecision.PASS_WITH_WARNINGS},
            decision=decision,
            issues=issues,
            warnings=warnings,
            validator="CaesarOutputValidatorV2",
            created_at=datetime.now(timezone.utc).isoformat(),
            metadata={"output_mode": output_mode.value},
        )
```

---

## 42.8 ValidationGateV3

`ValidationGateV3` sostituisce `ValidationGateV2` come implementazione consigliata.

Differenze:

- usa `CaesarOutputValidatorV2`;
- evita conflitto tra formato operativo e formato critico;
- produce un report combinato finale;
- il report combinato è il report canonico da usare per bloccare o passare.

```python
@dataclass
class ValidationGateV3(ValidationGateV2):
    caesar_output_validator: CaesarOutputValidatorV2 = field(default_factory=CaesarOutputValidatorV2)

    def validate(self, target: Any, target_type: ValidationTargetType, context: dict[str, Any] | None = None) -> ValidationReport:
        context = context or {}

        if target_type == ValidationTargetType.CAESAR_OUTPUT:
            base_report = self.caesar_output_validator.validate(target, context)
        else:
            base_report = ValidationGate.validate(self, target, target_type, context)

        should_apply_critical = (
            target_type == ValidationTargetType.CAESAR_OUTPUT
            or context.get("critical_review_required", False)
            or context.get("output_mode") == OutputMode.CRITICAL_STRATEGIC
        )

        if not should_apply_critical or not isinstance(target, str):
            if self.validation_store:
                self.validation_store.append(base_report)
            return base_report

        critical_report = self.critical_thinking_validator.validate(target, context)
        combined_decision = self._combine_decisions(base_report.decision, critical_report.decision)

        combined_report = ValidationReport(
            report_id=f"val_{uuid.uuid4().hex[:12]}",
            target_type=target_type,
            target_id=base_report.target_id,
            valid=combined_decision in {ValidationGateDecision.PASS, ValidationGateDecision.PASS_WITH_WARNINGS},
            decision=combined_decision,
            issues=base_report.issues + critical_report.issues,
            warnings=base_report.warnings + critical_report.warnings,
            validator="ValidationGateV3",
            created_at=datetime.now(timezone.utc).isoformat(),
            metadata={
                "base_report_id": base_report.report_id,
                "critical_report_id": critical_report.report_id,
            },
        )

        if self.validation_store:
            self.validation_store.append(combined_report)
        return combined_report
```

Regola:

```text
Da v4.2.1 in poi, l’implementazione consigliata è ValidationGateV3.
```

---

## 42.9 MessageBus latest-state view

Problema:

```text
JsonlMessageBus è append-only. mark_status() aggiunge una nuova riga, quindi get_inbox() poteva restituire stati obsoleti dello stesso message_id.
```

Patch:

```python
@dataclass
class JsonlMessageBusV2(JsonlMessageBus):
    def _read_latest_by_id(self) -> dict[str, AgentMessage]:
        latest: dict[str, AgentMessage] = {}
        for message in self._read_all():
            latest[message.message_id] = message
        return latest

    def get_inbox(self, agent_id: str, status: AgentMessageStatus | None = None) -> list[AgentMessage]:
        latest_messages = list(self._read_latest_by_id().values())
        inbox = [m for m in latest_messages if m.recipient == agent_id]
        if status is not None:
            inbox = [m for m in inbox if m.status == status]
        return inbox

    def get_thread(self, thread_id: str) -> list[AgentMessage]:
        latest = self._read_latest_by_id().values()
        return sorted(
            [m for m in latest if m.thread_id == thread_id],
            key=lambda m: m.timestamp,
        )
```

Regola:

```text
Il log resta append-only, ma le query operative usano la vista latest-state.
```

---

## 42.10 ErrorStore latest-state view

Problema:

```text
JsonlErrorStore.latest_open() poteva tornare un errore OPEN anche se lo stesso error_id era stato poi risolto.
```

Patch:

```python
@dataclass
class JsonlErrorStoreV2(JsonlErrorStore):
    def _read_latest_by_id(self) -> dict[str, ErrorEvent]:
        latest: dict[str, ErrorEvent] = {}
        if not self.path.exists():
            return latest
        for line in self.path.read_text(encoding="utf-8").splitlines():
            if not line.strip():
                continue
            event = self._error_from_dict(json.loads(line))
            latest[event.error_id] = event
        return latest

    def latest_open(self, project_id: str | None = None) -> ErrorEvent | None:
        candidates = []
        for error in self._read_latest_by_id().values():
            if project_id is not None and error.project_id != project_id:
                continue
            if error.status == ErrorResolutionStatus.OPEN:
                candidates.append(error)
        if not candidates:
            return None
        return sorted(candidates, key=lambda e: e.timestamp)[-1]
```

---

## 42.11 Applicazione profili critici ad AGENTS

Problema:

```text
AGENT_CRITICALITY_OVERRIDES definiva override ma non spiegava come applicarli al registro AGENTS.
```

Patch:

```python
def apply_agent_criticality_overrides(agents: dict[str, AgentSpec]) -> dict[str, AgentSpec]:
    updated: dict[str, AgentSpec] = {}
    for agent_id, spec in agents.items():
        override = AGENT_CRITICALITY_OVERRIDES.get(agent_id, {})
        updated[agent_id] = AgentSpec(
            id=spec.id,
            name=spec.name,
            department=spec.department,
            role=spec.role,
            triggers=spec.triggers,
            skills=spec.skills,
            restrictions=spec.restrictions,
            response_profile=override.get("response_profile", spec.response_profile),
            must_surface_risks=spec.must_surface_risks,
            must_state_assumptions=spec.must_state_assumptions,
            criticality_level=override.get("criticality_level", spec.criticality_level),
        )
    return updated


AGENTS_WITH_CRITICALITY = apply_agent_criticality_overrides(AGENTS)
```

Regola:

```text
Il runtime deve usare AGENTS_WITH_CRITICALITY quando Direct Critical Thinking è attivo.
```

---

## 42.12 Prompt registry manifest

Aggiunta consigliata per rendere il prompt registry verificabile.

```python
@dataclass(frozen=True)
class PromptManifest:
    manifest_version: str
    prompts: dict[str, PromptSpec]
    generated_at: str
    required_for_runtime: bool = True

    def missing_required_prompts(self, workspace_root: Path) -> list[str]:
        missing: list[str] = []
        for prompt_id, spec in self.prompts.items():
            if spec.required and not (workspace_root / spec.path).exists():
                missing.append(prompt_id)
        return missing


PROMPT_MANIFEST = PromptManifest(
    manifest_version="4.2.1",
    prompts=PROMPT_REGISTRY,
    generated_at="YYYY-MM-DDTHH:mm:ss",
)
```

---

## 42.13 Revisione dei rischi residui

| Rischio residuo | Severità | Mitigazione |
|---|---:|---|
| Documento molto grande | Media | In futuro separare spec in moduli: runtime, agents, validators, prompts |
| Codice in Markdown non importabile direttamente | Media | Generare package Python da blocchi canonici |
| Alcune classi sono estensioni e non sostituzioni fisiche | Bassa | Usare sempre classi `V2/V3` indicate come canoniche |
| Prompt registry non ancora creato su disco | Media | Prossimo step: generare `.agents/prompts/` |
| Test indicati ma non ancora file reali | Media | Prossimo step: creare test suite minimale |

---

## 42.14 Classi canoniche da usare dopo la revisione

| Area | Classe canonica |
|---|---|
| Stato | `RuntimeStateV2` |
| State store | `JsonStateStoreV2` / `StateStoreV2` |
| Validation gate | `ValidationGateV3` |
| Caesar output validation | `CaesarOutputValidatorV2` |
| Message bus | `JsonlMessageBusV2` |
| Error store | `JsonlErrorStoreV2` |
| Agent registry | `AGENTS_WITH_CRITICALITY` |

Regola:

```text
Se esiste una classe V2/V3 in questa sezione, prevale sulla classe precedente con lo stesso ruolo.
```

---

## 42.15 Stato revisione completa

| Controllo | Esito |
|---|---|
| Numerazione sezioni | OK |
| Versione documento | OK: v4.2.1 |
| Leggi architetturali | OK: 12 leggi |
| Direct Critical Thinking | OK, integrato in ValidationGateV3 |
| Runtime intake/routing/task/state/resume/error/message/fs/validation | OK |
| Punti runtime originari | Tutti coperti |
| Incoerenze bloccanti note | Corrette con patch v4.2.1 |

```text
┌─ LA DECISIONE ─────────────────────────────────────────────────┐
│ Scelta: Usare v4.2.1 come specifica corretta e coerente del Castello │
│ Perché: Risolve i conflitti runtime emersi dalla revisione completa │
└────────────────────────────────────────────────────────────────┘
```
