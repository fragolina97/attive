# Skill Claude Code — Attive

Collezione completa di skill Claude Code installate e pronte all'uso.

## Installazione

### Installazione Rapida (Windows)

```powershell
.\install.ps1
```

### Installazione Rapida (Mac/Linux)

```bash
bash install.sh
```

### Installazione Manuale

1. Clona la repo:
   ```
   git clone https://github.com/fragolina97/attive.git
   ```

2. Copia le cartelle:
   - **Windows**: Copia `commands\*` in `%USERPROFILE%\.claude\commands\` e `skills\*` in `%USERPROFILE%\.claude\skills\`
   - **Mac/Linux**: Copia `commands/*` in `~/.claude/commands/` e `skills/*` in `~/.claude/skills/`

## Skill Incluse

### Comandi (`/nome` — invocazione esplicita)

| Skill | Comando | Descrizione |
|-------|---------|-------------|
| **omega** | `/omega` | Genera skill e progetti AI completi (Custom Instructions + Knowledge Base) |
| **deep-research** | `/deep-research` | Sistema multi-agente per ricerca web + integrazione vault 2Brain |
| **skill-creator** | `/skill-creator` | Crea, valuta e ottimizza skill Claude Code con A/B testing |
| **skill-contradiction-analyzer** | `/skill-contradiction-analyzer` | Analizza contraddizioni tra due skill AI (15 rilevatori) |
| **castello** | `/castello` | Architettura multi-agente AI OS (Caesar + 22 Legionari + Atlas + Afrodite) |

### Skill di Supporto (caricate automaticamente)

| Skill | Descrizione |
|-------|-------------|
| **karpathy-guidelines** | Guida comportamentale per coding LLM (think → simplify → surgical → goal) |
| **karpathy-llm-wiki** | Gestione knowledge base personale (raw/ + wiki/, ingest/query/lint) |
| **playwright-dev** | Guida per sviluppatori Playwright (API, MCP tools, trace system, vendor) |
| **playwright-devops** | DevOps Playwright (analisi CI failures, workflow debugging, report) |
| **ui-ux-pro-max** | Design intelligence: 67 stili, 96 palette, 57 font, 25 chart, 13 stack |
| **wiki-context** | Carica contesto wiki 2Brain prima di rispondere |
| **marketing-skills v2.2.0** | Suite completa: 42 skill di marketing (SEO, ads, email, CRO, analytics...) |

### Marketing Skills Incluse (42 skill)

`ab-testing` · `ad-creative` · `ads` · `ai-seo` · `analytics` · `aso` · `churn-prevention` · `co-marketing` · `cold-email` · `community-marketing` · `competitor-profiling` · `competitors` · `content-strategy` · `copy-editing` · `copywriting` · `cro` · `customer-research` · `directory-submissions` · `emails` · `free-tools` · `image` · `launch` · `lead-magnets` · `marketing-ideas` · `marketing-psychology` · `onboarding` · `paywalls` · `popups` · `pricing` · `product-marketing` · `programmatic-seo` · `prospecting` · `referrals` · `revops` · `sales-enablement` · `schema` · `seo-audit` · `signup` · `site-architecture` · `sms` · `social` · `video`

## Struttura della Repo

```
attive/
├── README.md
├── install.sh          ← Mac/Linux
├── install.ps1         ← Windows
├── commands/           → copia in ~/.claude/commands/
│   ├── omega.md
│   ├── castello/
│   ├── deep-research/
│   ├── skill-creator/
│   └── skill-contradiction-analyzer/
└── skills/             → copia in ~/.claude/skills/
    ├── karpathy-guidelines/
    ├── karpathy-llm-wiki/
    ├── playwright-dev/
    ├── playwright-devops/
    ├── ui-ux-pro-max/
    ├── wiki-context/
    └── marketing-skills/
        └── ... (42 sub-skill)
```

## Note

- Le skill in `commands/` si invocano con `/nome` direttamente in chat
- Le skill in `skills/` vengono caricate automaticamente in base alla loro `description` YAML
- Per `ui-ux-pro-max` è richiesto **Python 3** per gli script del design system
- Per `deep-research` e `wiki-context` è necessario configurare il vault `2Brain/` nel proprio workspace
