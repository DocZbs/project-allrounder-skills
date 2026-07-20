# PASS Installable Skill Suite Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Publish three independently installable, validated Codex skills and refresh the repository branding as PASS (Project Allrounder Skill Suite).

**Architecture:** `project-allrounder` owns the lifecycle and project master record, then routes proposal work to `writing-project-proposals` and deck work to `building-project-presentations`. Each skill keeps its core workflow in `SKILL.md`, moves detailed rules to one-level `references/`, and stores reusable output templates in `assets/`. Deterministic project-folder creation is implemented as a small Python script with standard-library tests.

**Tech Stack:** Markdown Agent Skills, YAML agent metadata, Python 3.9 standard library, unittest, SVG, Git.

## Global Constraints

- Skill folders are exactly `project-allrounder`, `writing-project-proposals`, and `building-project-presentations`.
- Every skill has valid `SKILL.md` frontmatter and `agents/openai.yaml`.
- Current calls, contracts, task books, institutional rules, and verified project evidence override historical examples.
- Do not fabricate facts, citations, results, budgets, financial evidence, or acceptance evidence.
- Use only authorized or openly licensed reference proposals and decks; extract patterns without copying protected expression or confidential content.
- `building-project-presentations` must require a real `.pptx`, rendering, overflow/overlap checks, speaker notes, timing, and question preparation.
- README branding uses a repository-owned green pixel SVG and the acronym PASS; the two user-requested sections are removed from both languages.
- No real confidential project material or credentials enter the repository.

---

### Task 1: PASS branding and repository assertions

**Files:**
- Create: `docs/assets/pass-logo.svg`
- Modify: `README.md`
- Modify: `README_EN.md`
- Modify: `docs/superpowers/specs/2026-07-20-project-allrounder-skill-suite-design.md`
- Create: `tests/test_repository.py`

**Interfaces:**
- Produces: a GitHub-renderable PASS logo and repository-level checks used by the final verification step.

- [ ] **Step 1: Write the failing repository test**

```python
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]

class RepositoryTest(unittest.TestCase):
    def test_expected_skills_and_pass_branding_exist(self):
        self.assertTrue((ROOT / "docs/assets/pass-logo.svg").is_file())
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        self.assertIn("Project Allrounder Skill Suite", readme)
        self.assertNotIn("$ equip project-allrounder", readme)
        self.assertNotIn("## 优秀本子与优秀 PPT", readme)
        for name in (
            "project-allrounder",
            "writing-project-proposals",
            "building-project-presentations",
        ):
            self.assertTrue((ROOT / "skills" / name / "SKILL.md").is_file())

if __name__ == "__main__":
    unittest.main()
```

- [ ] **Step 2: Run the test to verify it fails**

Run: `python3 -m unittest tests.test_repository -v`

Expected: FAIL because the logo and `skills/` files do not exist.

- [ ] **Step 3: Add the SVG and README edits**

Create a self-contained SVG with a dark terminal panel, green/teal block-letter `PASS`, and the subtitle `PROJECT ALLROUNDER SKILL SUITE`. Replace the plain heading with the image plus accessible title text. Remove the command-line cascade and the complete successful-proposal/reference-deck sections from Chinese and English README files. Mark the design status as approved.

- [ ] **Step 4: Re-run only README assertions**

Run: `python3 -m unittest tests.test_repository.RepositoryTest.test_expected_skills_and_pass_branding_exist -v`

Expected: still FAIL only on missing skill files, proving the branding conditions now pass.

### Task 2: `project-allrounder`

**Files:**
- Create: `skills/project-allrounder/SKILL.md`
- Create: `skills/project-allrounder/agents/openai.yaml`
- Create: `skills/project-allrounder/references/lifecycle.md`
- Create: `skills/project-allrounder/references/project-master-record.md`
- Create: `skills/project-allrounder/references/project-type-routing.md`
- Create: `skills/project-allrounder/references/compliance-gates.md`
- Create: `skills/project-allrounder/scripts/init_project_record.py`
- Create: `tests/test_init_project_record.py`
- Create: `tests/baselines/project-allrounder.md`
- Create: `tests/scenarios/project-allrounder.md`
- Create: `tests/results/project-allrounder.md`

**Interfaces:**
- Consumes: user-provided calls, contracts, task books, evidence, policies, and project state.
- Produces: a stage decision, project master record, traceability map, next-action plan, blockers, and routing instructions for the other two skills.

- [ ] **Step 1: Capture a baseline without the skill**

Run a fresh-context agent on a fictional horizontal project takeover. Record omissions such as missing source freeze, requirement-to-evidence traceability, financial evidence, change control, or acceptance gates in `tests/baselines/project-allrounder.md`.

- [ ] **Step 2: Write the failing project-record tests**

```python
from pathlib import Path
from tempfile import TemporaryDirectory
import subprocess
import unittest

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "skills/project-allrounder/scripts/init_project_record.py"

class InitProjectRecordTest(unittest.TestCase):
    def test_creates_complete_record_without_overwriting(self):
        with TemporaryDirectory() as tmp:
            target = Path(tmp) / "demo"
            subprocess.run(["python3", str(SCRIPT), str(target)], check=True)
            expected = [f"{i:02d}-{name}" for i, name in enumerate([
                "source", "requirements", "proposal", "baseline", "plan", "execution",
                "deliverables", "progress", "finance", "changes-risks", "acceptance", "closeout"
            ])]
            self.assertEqual(expected, sorted(p.name for p in target.iterdir() if p.is_dir()))
            marker = target / "01-requirements/requirements-matrix.md"
            marker.write_text("keep", encoding="utf-8")
            subprocess.run(["python3", str(SCRIPT), str(target)], check=True)
            self.assertEqual("keep", marker.read_text(encoding="utf-8"))

if __name__ == "__main__":
    unittest.main()
```

- [ ] **Step 3: Run the tests to verify RED**

Run: `python3 -m unittest tests.test_init_project_record -v`

Expected: FAIL because the initializer does not exist.

- [ ] **Step 4: Initialize and implement the skill**

Run the official `init_skill.py` with `scripts,references,assets`, remove unused placeholder assets, then implement an imperative workflow: identify project type and stage; freeze sources; build the master record; map source → objective → indicator → work package → task → deliverable → evidence; track budget → expense → voucher; control risks/changes; route proposal and PPT requests; stop on compliance blockers.

- [ ] **Step 5: Implement the deterministic initializer**

The script accepts one target path, creates the 12 numbered directories with `exist_ok=True`, seeds only missing Markdown registers, refuses a file path as the target, and never overwrites existing records.

- [ ] **Step 6: Validate and forward-test**

Run:

```bash
python3 -m unittest tests.test_init_project_record -v
python3 /Users/zbs/.codex/skills/.system/skill-creator/scripts/quick_validate.py skills/project-allrounder
```

Run the same fictional takeover with `$project-allrounder`; record whether all baseline omissions are closed in `tests/results/project-allrounder.md`.

- [ ] **Step 7: Commit the first skill**

```bash
git add skills/project-allrounder tests/test_init_project_record.py tests/baselines/project-allrounder.md tests/scenarios/project-allrounder.md tests/results/project-allrounder.md
git commit -m "feat: add project lifecycle orchestration skill"
```

### Task 3: `writing-project-proposals`

**Files:**
- Create: `skills/writing-project-proposals/SKILL.md`
- Create: `skills/writing-project-proposals/agents/openai.yaml`
- Create: `skills/writing-project-proposals/references/source-and-case-research.md`
- Create: `skills/writing-project-proposals/references/vertical-projects.md`
- Create: `skills/writing-project-proposals/references/horizontal-projects.md`
- Create: `skills/writing-project-proposals/references/proposal-quality-gates.md`
- Create: `skills/writing-project-proposals/assets/requirements-response-matrix.md`
- Create: `skills/writing-project-proposals/assets/case-comparison-matrix.md`
- Create: `tests/baselines/writing-project-proposals.md`
- Create: `tests/scenarios/writing-project-proposals.md`
- Create: `tests/results/writing-project-proposals.md`

**Interfaces:**
- Consumes: current call/template, institutional rules, verified project facts, and authorized/public proposal references.
- Produces: eligibility and requirement audit, source register, case-comparison matrix, proposal argument map, review findings, and submission gate result.

- [ ] **Step 1: Run and record a no-skill baseline**

Use a fictional multidisciplinary proposal with missing facts and a request to imitate a successful proposal. Record whether the baseline invents content, skips provenance, or fails to separate vertical and horizontal requirements.

- [ ] **Step 2: Initialize and implement the skill**

Use `init_skill.py` with `references,assets`. Require current-source verification, three-to-five authorized/open reference cases when available, a provenance-rich comparison matrix, original argument construction, fact/citation verification, and a final blocking-issue audit. Route NSFC, social-science/humanities, key-R&D, local vertical, and horizontal contracts to focused reference modules.

- [ ] **Step 3: Add reusable matrices**

The requirements matrix fields are `ID | source/version | exact requirement | response | evidence | owner | status | blocker`. The case matrix fields are `source | authorization/provenance | project type/year | argument structure | evidence strategy | reviewer signal | transferable principle | non-transferable content`.

- [ ] **Step 4: Validate and forward-test**

Run `quick_validate.py`, then repeat the baseline with the skill. The result must refuse copying, preserve missing-fact markers, verify sources, and distinguish contractual acceptance/payment/IP from vertical-program scoring and compliance.

- [ ] **Step 5: Commit the proposal skill**

```bash
git add skills/writing-project-proposals tests/baselines/writing-project-proposals.md tests/scenarios/writing-project-proposals.md tests/results/writing-project-proposals.md
git commit -m "feat: add proposal development skill"
```

### Task 4: `building-project-presentations`

**Files:**
- Create: `skills/building-project-presentations/SKILL.md`
- Create: `skills/building-project-presentations/agents/openai.yaml`
- Create: `skills/building-project-presentations/references/deck-router.md`
- Create: `skills/building-project-presentations/references/evidence-and-story.md`
- Create: `skills/building-project-presentations/references/visual-quality-gates.md`
- Create: `skills/building-project-presentations/assets/deck-brief.md`
- Create: `skills/building-project-presentations/assets/slide-evidence-matrix.md`
- Create: `tests/baselines/building-project-presentations.md`
- Create: `tests/scenarios/building-project-presentations.md`
- Create: `tests/results/building-project-presentations.md`

**Interfaces:**
- Consumes: presentation scene, decision audience, time limit, project baseline, verified evidence, approved brand/template assets, and authorized/public deck references.
- Produces: a real `.pptx`, rendered slide images, coverage/evidence audit, speaker notes, timing plan, and expert-question bank.

- [ ] **Step 1: Run and record a no-skill baseline**

Ask for a 15-minute acceptance deck from fictional evidence. Record whether the baseline stops at an outline, uses generic sections, omits indicator-to-evidence mapping, or skips visual inspection.

- [ ] **Step 2: Initialize and implement the skill**

Use `init_skill.py` with `references,assets`. Require the installed `presentations` skill for file creation and rendering. Route proposal defense, kickoff, progress, technical review, acceptance, and closeout to different evidence-led narratives. Require at least one authorized/open same-scene deck reference when available without copying its visual assets.

- [ ] **Step 3: Add PPT quality contracts**

Every deck brief records audience, decision, duration, scene, thesis, required evidence, forbidden claims, template, and output path. Every slide row records `slide | claim | evidence/source | visual form | speaker-note purpose | time | status`. The final gate requires `.pptx` existence, render success, no overlap/overflow/cropping, legibility at full-slide view, content coverage, consistency, notes, timing, and anticipated questions.

- [ ] **Step 4: Validate and forward-test**

Run `quick_validate.py`; then repeat the baseline. Confirm it invokes presentation tooling, plans a real file, maps every acceptance indicator to evidence, and includes render-based QA rather than declaring success from source code alone.

- [ ] **Step 5: Commit the presentation skill**

```bash
git add skills/building-project-presentations tests/baselines/building-project-presentations.md tests/scenarios/building-project-presentations.md tests/results/building-project-presentations.md
git commit -m "feat: add evidence-led project presentation skill"
```

### Task 5: Integration, installation, and publication

**Files:**
- Modify: `README.md`
- Modify: `README_EN.md`
- Modify: `AGENTS.md`
- Create: `.gitignore`
- Create: `tests/test_skill_suite.py`

**Interfaces:**
- Consumes: all three validated skill directories.
- Produces: executable installation instructions and a clean public repository ready for GitHub and Hugging Face mirroring.

- [ ] **Step 1: Add suite-structure tests**

Test that every skill has frontmatter, matching directory/name, `agents/openai.yaml`, no nested README, no placeholder markers, and no broken relative Markdown links. Assert that the orchestrator names both sub-skills and the presentation skill requires a `.pptx` plus rendering.

- [ ] **Step 2: Run all tests and validators**

```bash
python3 -m unittest discover -s tests -v
for skill in skills/*; do
  python3 /Users/zbs/.codex/skills/.system/skill-creator/scripts/quick_validate.py "$skill"
done
```

Expected: all tests pass and all three validators report valid skills.

- [ ] **Step 3: Test installation into a temporary directory**

Copy each skill into a temporary Codex skills root, verify `SKILL.md` and metadata remain intact, and remove the temporary directory after the check.

- [ ] **Step 4: Review and commit integration**

Inspect `git diff --check`, search staged changes for credentials and placeholder markers, then commit the logo, README, test suite, and repository guidance as one documentation/integration change.

- [ ] **Step 5: Push and verify GitHub**

Push `main`, compare local and remote commit IDs, and confirm the GitHub repository renders the PASS logo and exposes all three `skills/<name>/SKILL.md` files.

