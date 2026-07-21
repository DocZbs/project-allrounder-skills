<p align="center">
  <img src="docs/assets/project-cascade-terminal-2x2.png" width="720" alt="A professor hands a project to a senior researcher, the senior passes an expanding workload to a junior researcher, and the junior organizes the project with a glowing skill toolbox." />
</p>

<p align="center">🟢　🟡　🔵</p>

<p align="center"><code>██████╗&nbsp;&nbsp;█████╗&nbsp;███████╗███████╗<br>
██╔══██╗██╔══██╗██╔════╝██╔════╝<br>
██████╔╝███████║███████╗███████╗<br>
██╔═══╝&nbsp;██╔══██║╚════██║╚════██║<br>
██║&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;██║&nbsp;&nbsp;██║███████║███████║<br>
╚═╝&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;╚═╝&nbsp;&nbsp;╚═╝╚══════╝╚══════╝</code></p>

<p align="center"><strong>🟩 Project Allrounder Skill Suite 🟦</strong></p>

> **PASS — Project Allrounder Skill Suite**: end-to-end skills for vertical and horizontal projects, from the first requirement to final acceptance and closeout.

English · [中文](README.md)

## Three Skills

| Skill | Purpose |
|---|---|
| `project-allrounder` | Maintains the project record, tasks, progress, risks, financial evidence, acceptance, and closeout |
| `writing-project-proposals` | Analyzes calls and needs, compares authorized successful examples, and supports proposal review |
| `building-project-presentations` | Builds proposal, kickoff, progress, technical review, acceptance, and closeout PPTX decks |

Each skill can run independently. `project-allrounder` can also route work to the other two.

## Workflow

```text
Call document / client need
  → eligibility and requirement analysis
  → successful-example comparison
  → proposal and award handoff
  → task planning and project development
  → progress, deliverable, and financial evidence tracking
  → presentation and defense
  → acceptance, closeout, and archiving
```

The suite supports funding programs, enterprise-commissioned horizontal projects, vertical projects, and related scenarios.

## Installation

Install all three skills from `main` with Codex's built-in Skill Installer:

```bash
python "${CODEX_HOME:-$HOME/.codex}/skills/.system/skill-installer/scripts/install-skill-from-github.py" \
  --repo DocZbs/project-allrounder-skills \
  --path \
    skills/project-allrounder \
    skills/writing-project-proposals \
    skills/building-project-presentations
```

## Example Prompts

```text
Use project-allrounder to analyze this call document, initialize the project record,
and identify application requirements, assessment indicators, tasks, and acceptance evidence.
```

```text
Use writing-project-proposals to compare authorized successful examples and review
the gaps between my core problem, novelty, approach, and preliminary evidence.
```

```text
Use building-project-presentations to create a 15-minute progress-review PPTX
from the task book, current progress, and verified project evidence.
```

## Compliance Boundaries

- Never fabricate facts, references, results, budgets, or acceptance evidence.
- Current calls, task books, contracts, and institutional policies override historical examples.
- Funding and other project work must follow current requirements for generative AI use, verification, disclosure, and labeling.
- Contract, intellectual-property, accounting, and reimbursement output is review support, not formal approval.
- Confidential industry data and unpublished materials remain within the user's authorized scope.

See the [design specification](docs/superpowers/specs/2026-07-20-project-allrounder-skill-suite-design.md) and the repository's [agent instructions](AGENTS.md).

## License

[MIT License](LICENSE)
