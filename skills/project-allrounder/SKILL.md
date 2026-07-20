---
name: project-allrounder
description: Use when taking over, planning, executing, reporting, accepting, reimbursing, handing over, closing, or rescuing a vertical or horizontal project across its full lifecycle.
---

# Project Allrounder

## Overview

Run a project from the controlling requirement to verified closeout. Keep one project master record as the fact source and preserve this traceability chain:

```text
source clause → objective → indicator → work package → task → deliverable → acceptance evidence
                                      └→ budget → expense → voucher
```

Never let a polished document outrun the evidence behind it.

## Start Every Engagement

1. Identify the project as vertical, horizontal, or mixed; identify its current lifecycle stage.
2. Collect the current call, notice, template, signed contract, task book, approval, appendices, institutional rules, and existing outputs.
3. Freeze each controlling source with title, issuing body, version/date, retrieval path, and authority. Do not silently replace a source.
4. Separate all information into verified facts, assumptions, missing evidence, and decisions awaiting an owner.
5. Create or locate the project master record. To initialize a safe local skeleton, run:

```bash
python scripts/init_project_record.py /absolute/path/to/project-master-record
```

6. Read [project-master-record.md](references/project-master-record.md) and build the requirement, indicator, task, deliverable, evidence, finance, risk, change, and decision registers.
7. Read [project-type-routing.md](references/project-type-routing.md) for the applicable project family.
8. Read [lifecycle.md](references/lifecycle.md) for the current stage and its exit gate.
9. Read [compliance-gates.md](references/compliance-gates.md) before any formal submission, external transmission, financial conclusion, acceptance claim, or closeout claim.

If controlling material is unavailable, produce a gap list and a provisional workspace clearly marked `DRAFT — UNVERIFIED`; do not impersonate a formal final deliverable.

## Operate the Lifecycle

At each stage:

1. Define the decision to be made and the exit condition.
2. Link every planned action to a controlling requirement or an approved change.
3. Assign an owner, deadline, dependency, expected output, and evidence location.
4. Record status as `not started`, `in progress`, `completed with evidence`, `blocked`, or `changed by approval`.
5. Check schedule, scope, quality, budget, risk, IP/confidentiality, and stakeholder impact.
6. Record conflicts and changes with source, difference, decision, approver, date, and downstream impact.
7. Close the stage only when its evidence gate passes; otherwise carry an explicit blocker.

Do not equate activity with completion. `Completed` requires a reviewable artifact and its evidence path.

## Route Specialized Work

- For opportunity analysis, requirements, application strategy, proposal support, proposal review, or submission checks, use **`writing-project-proposals`**.
- For proposal defense, kickoff, progress, technical review, acceptance, or closeout decks, use **`building-project-presentations`**.
- Keep shared facts in the master record. Do not let either specialized skill create a separate conflicting truth set.
- After specialized work returns, register its outputs, evidence, open questions, versions, and approvals in the master record.

## Status Output Contract

Every takeover, progress review, handoff, or closeout response must contain these sections in this order:

1. **Stage and decision** — project type, lifecycle stage, and current decision.
2. **Verified facts** — facts with source/version or evidence path.
3. **Assumptions** — provisional statements that require confirmation.
4. **Missing inputs and blockers** — impact, owner, and unblock action.
5. **Traceability status** — unmet requirements, unsupported indicators, orphan tasks, and unlinked evidence.
6. **Plan and ownership** — next actions, owners, dates, dependencies, and outputs.
7. **Risk/change/finance status** — material exceptions and evidence gaps.
8. **Human confirmations** — decisions, signatures, approvals, or external actions the agent cannot make.

## Stop Conditions

Stop and request resolution when:

- the current controlling source or template cannot be confirmed;
- eligibility, scope, ethics, security, confidentiality, IP, or data rights remain unresolved;
- a claimed result, citation, expense, voucher, deliverable, or acceptance fact lacks evidence;
- the task requests copying or redistributing leaked, confidential, or unauthorized material;
- a change would alter signed scope, price, payment, IP, schedule, or acceptance terms without an authorized decision;
- an external submission, signature, payment, approval, or stakeholder message requires human authority.

Return the exact blocker, why it matters, who can decide, and the smallest safe next step.

## Quick Reference

| Need | Action |
|---|---|
| New project | Freeze sources, initialize master record, build requirement traceability |
| Existing project rescue | Reconstruct actual baseline, compare with controlling baseline, open gaps and changes |
| Progress report | Report only evidence-backed completion; separate variance, risk, and next-stage plan |
| Reimbursement support | Link budget item → expense → voucher → approval status; defer to current institutional rules |
| Acceptance | Map every indicator and deliverable to evidence, reviewer, status, and remediation |
| Handover | Inventory artifacts, versions, access, IP/data constraints, runbooks, training, and sign-off |
| Closeout | Confirm contractual/program, technical, financial, archival, and lessons-learned gates |

## Common Mistakes

- Starting with a report instead of the controlling source and evidence map.
- Mixing proposed, in-progress, and accepted results.
- Treating an old call, template, policy, or successful example as current authority.
- Updating a deadline or deliverable without a change record.
- Declaring reimbursement, acceptance, or closeout from narrative alone.
- Sending confidential horizontal-project material outside the authorized scope.
