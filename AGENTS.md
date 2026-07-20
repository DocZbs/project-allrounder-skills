# Project Allrounder Skills: Agent Instructions

## Purpose

This repository contains three installable Codex skills for managing vertical and horizontal projects from opportunity analysis through closeout:

- `project-allrounder`: owns the project lifecycle, master record, execution, finance evidence, acceptance, and closeout.
- `writing-project-proposals`: owns proposal analysis, authorized example comparison, proposal support, compliance checks, and pre-submission review.
- `building-project-presentations`: owns proposal, kickoff, progress, technical review, acceptance, and closeout presentations.

Read the approved design before changing scope or architecture:

- `docs/superpowers/specs/2026-07-20-project-allrounder-skill-suite-design.md`

## Repository Rules

- Keep code and instructions simple, explicit, and easy to audit.
- Keep each skill independently installable.
- Keep `SKILL.md` concise. Put detailed program rules, templates, and examples in directly linked `references/` files.
- Put deterministic, reusable operations in `scripts/` and test them.
- Put output templates and licensed reusable media in `assets/`.
- Do not add a README, changelog, installation guide, or other auxiliary documentation inside an individual skill directory.
- Keep public repository documentation at the repository root or under `docs/`.
- Use English for repository-level agent instructions and code-facing metadata. User-facing skill output may be Chinese or English according to the request.

## Required Working Sequence

1. Read this file and the relevant design section.
2. Inspect the target skill, its tests, and one similar local pattern before editing.
3. Confirm the project type, lifecycle stage, requested deliverable, and authoritative source documents.
4. Run a baseline scenario without the target skill and record the observed failure.
5. Implement or revise one skill only.
6. Validate its structure, scripts, triggers, and scenario behavior.
7. Commit the verified skill before starting the next skill.
8. Run cross-skill integration tests only after all three skills pass independently.

Do not batch-create all three skills and test them afterward.

## Source Authority

When sources conflict, use this order:

1. Current call guidelines, special notices, and the current online submission outline.
2. Signed task books, contracts, amendments, and formal approvals.
3. Current sponsor regulations and institutional policies.
4. Project facts and primary evidence confirmed by the responsible human.
5. Historical successful proposals, presentation examples, and informal advice.

Never silently resolve a material conflict. Record the sources, the conflict, the chosen interpretation, and the required human confirmation.

Rules and templates change. Verify unstable requirements against current official sources before presenting them as current.

## Successful Proposal and Presentation Examples

- Treat comparison with strong, relevant examples as a required workflow step.
- Prefer sponsor-published materials, author-authorized examples, official review summaries, public project abstracts, final reports, and user-owned historical materials.
- Record source, owner or publisher, project type, discipline, year, authorization status, and known limitations.
- Extract reusable reasoning, structure, evidence patterns, and reviewer feedback.
- Do not copy wording, figures, data, visual assets, or project-specific claims.
- Current instructions always override historical examples.
- Do not add leaked, paywalled redistribution, confidential, privacy-sensitive, or provenance-unknown proposals and decks to this repository.

The open-source repository may contain source indexes and original analysis cards. It must not redistribute copyrighted full proposals or confidential project files without explicit permission.

## Research Integrity and AI Use

- Never fabricate facts, citations, team experience, preliminary results, budgets, outputs, completion claims, or acceptance evidence.
- Mark missing information as a gap and request human input.
- Require human verification of generated references and research claims.
- Preserve a record of sources and verification status.
- Respect research ethics, biosafety, human-subject, animal, data, confidentiality, and export-control requirements when relevant.
- Follow the current sponsor policy for generative AI use.

For National Natural Science Foundation of China work, do not present AI-generated text as a final application, progress report, closeout report, or results report. Use AI for permitted research tracking, evidence organization, outlines, questions, critique, and revision support. Require the applicant to verify, disclose, label, author, and approve content as required by the current rules.

## Privacy, Contracts, and Finance

- Process only data the user is authorized to use.
- Keep confidential horizontal-project content local unless the user explicitly authorizes a specific external action.
- Never commit secrets, personal identifiers, unpublished confidential results, raw invoices, bank details, private contracts, or client data.
- Treat legal, intellectual-property, tax, procurement, accounting, and reimbursement output as review support, not final institutional approval.
- Tie financial records to project activities, budget categories, and evidence without inventing eligibility decisions.

## Project Record Invariants

Maintain traceability through this chain:

```text
authoritative requirement
  -> objective
  -> assessment indicator
  -> work package
  -> task
  -> deliverable
  -> acceptance evidence
```

Maintain financial traceability through this chain:

```text
task
  -> approved budget category
  -> expenditure
  -> supporting document index
```

- A completion claim without evidence is not complete.
- A deliverable without a requirement or approved change must be flagged as out of baseline.
- A changed requirement must have a decision record.
- Reports and presentations must use the same confirmed facts as the project master record.

## Presentation Requirements

- Use `building-project-presentations` for project-specific narrative, evidence selection, scenario routing, speaker notes, and defense questions.
- Use the installed Presentations skill for actual PPTX creation and rendering unless the environment provides a newer approved presentation workflow.
- Produce a real `.pptx` when presentation tooling is available; an outline alone is not complete.
- Use at least one authorized, relevant reference deck when available and record what was learned from it.
- Give every slide one communication job and one primary claim.
- Trace acceptance slides to the indicator-evidence matrix.
- Render and inspect every final slide at full size.
- Fix unintended overlap, clipping, wrapping, crop, font, contrast, and evidence-readability problems before delivery.
- Generate speaker notes, duration guidance, and a reviewer question bank when the scenario requires oral defense.
- Do not claim that a deck passed quality review without retaining the actual validation result.

## Skill Authoring and Validation

- Initialize new skills with the official `init_skill.py` workflow.
- Use lowercase letters, digits, and hyphens for skill names.
- Keep frontmatter limited to `name` and `description` unless the governing skill specification explicitly changes.
- Start descriptions with concrete trigger conditions. Do not use the description as a shortcut summary of the entire workflow.
- Use imperative language in skill bodies.
- Keep references one level deep where practical and link every conditional reference directly from `SKILL.md`.
- Generate and validate `agents/openai.yaml` from the finished skill.
- Run the official quick validator for every skill.
- Run every added script on representative inputs.
- Keep test artifacts free of real confidential project data.

## Test Expectations

Use a RED-GREEN-REFACTOR workflow for each skill:

- RED: run realistic baseline scenarios without the skill and record exact failures.
- GREEN: add the minimum guidance and resources needed to correct those failures.
- REFACTOR: run fresh-context scenarios, close gaps, and simplify without losing behavior.

Minimum scenario coverage:

- NSFC AI-use and human-verification boundaries.
- National Social Science Fund application, change, appraisal, and closeout routing.
- National Key R&D requirement decomposition, milestones, and performance evidence.
- Horizontal-project scope, contract, intellectual property, payment, change, and acceptance analysis.
- Mandatory successful-example comparison.
- Missing-fact behavior without fabrication.
- Progress status that distinguishes complete, in progress, delayed, blocked, and at risk.
- Acceptance claims that resolve to evidence.
- Actual PPTX generation and slide-level visual quality checks.
- Correct routing between the three skills.

Do not mark a test as passed from inspection alone. Retain commands, inputs, and outputs sufficient to reproduce the result.

## Git and Release Discipline

- Work on short-lived `codex/` branches unless the user requests another branch strategy.
- Preserve unrelated user changes.
- Make small, atomic commits after verified increments.
- Use descriptive conventional commit messages.
- Review staged changes and scan for secrets before every commit.
- Do not push, create a GitHub repository, publish a release, or tag a release unless the user explicitly requests that external action.
- Use semantic versioning once the suite has consumers.
- The first validated public-ready release is planned as `v0.1.0`.

## Stop Conditions

Stop and surface the blocker when:

- the current authoritative rule or template cannot be verified;
- a material requirement is ambiguous and no project precedent resolves it;
- the task requires confidential or copyrighted material the user has not authorized;
- a factual claim, citation, budget statement, result, or acceptance claim cannot be verified;
- a requested action would publish, send, submit, sign, approve, or spend without explicit authorization;
- a high-severity test or presentation defect remains unresolved.

When stopping, provide the exact missing input, affected output, and safest next action.
