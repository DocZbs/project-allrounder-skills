<p align="center">
  <img src="docs/assets/project-cascade-terminal-2x2.png" width="720" alt="A professor hands a project to a senior researcher, the senior passes an expanding workload to a junior researcher, and the junior organizes the project with a glowing skill toolbox." />
</p>

```text
██████╗  █████╗ ███████╗███████╗
██╔══██╗██╔══██╗██╔════╝██╔════╝
██████╔╝███████║███████╗███████╗
██╔═══╝ ██╔══██║╚════██║╚════██║
██║     ██║  ██║███████║███████║
╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝
     Project Allrounder Skill Suite
```

> **PASS — Project Allrounder Skill Suite**: end-to-end skills for vertical and horizontal projects, from the first requirement to final acceptance and closeout.

English · [中文](README.md)

> [!NOTE]
> All three skills are now on `main` and have passed initial structural, script, and forward-scenario tests. The first version tag has not been published yet.

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

The first release is planned to support NSFC, the National Social Science Fund of China, National Key R&D projects, provincial and institutional vertical programs, and commissioned horizontal projects.

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
the gaps between my research question, novelty, approach, and preliminary evidence.
```

```text
Use building-project-presentations to create a 15-minute progress-review PPTX
from the task book, current progress, and verified project evidence.
```

## Compliance Boundaries

- Never fabricate facts, references, results, budgets, or acceptance evidence.
- Current calls, task books, contracts, and institutional policies override historical examples.
- NSFC work must follow the current rules for generative AI use, verification, disclosure, and labeling.
- Contract, intellectual-property, accounting, and reimbursement output is review support, not formal approval.
- Confidential industry data and unpublished materials remain within the user's authorized scope.

See the [design specification](docs/superpowers/specs/2026-07-20-project-allrounder-skill-suite-design.md) and the repository's [agent instructions](AGENTS.md).

## License

[MIT License](LICENSE)
