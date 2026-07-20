# Project Master Record

The master record is the project's unique fact source. Store open, readable files under version control when confidentiality rules permit.

## Directory Map

```text
00-source/           controlling originals and source-register.md
01-requirements/     requirements-matrix.md
02-proposal/         proposal versions, reviews, and submission evidence
03-baseline/         objectives, indicators, scope, deliverables, budget, dates
04-plan/             WBS, RACI, milestones, resources, quality plan
05-execution/        work records, experiments, development, fieldwork
06-deliverables/     versioned outputs and deliverables-register.md
07-progress/         status reports, meetings, reviews, progress evidence
08-finance/          budget-expense-voucher register and approvals
09-changes-risks/    risks, issues, changes, decisions
10-acceptance/       indicator-evidence matrix, reviews, remediation
11-closeout/         handover, archive, final reports, lessons learned
```

## Mandatory Registers

### Source register

`source ID | title | authority | version/date | retrieved | local path | controlling scope | supersedes | confidentiality`

### Requirements matrix

`requirement ID | exact source clause | interpretation | response | owner | due | output | acceptance evidence | status | blocker`

### Indicator/evidence matrix

`indicator ID | baseline value | target | method | measurement date | evidence path | reviewer | result | gap | remediation`

### Task register

`task ID | requirement/indicator | work package | owner | start | due | dependency | output | evidence | status`

### Deliverables register

`deliverable ID | controlling requirement | version | owner | review gate | submitted | accepted | acceptance evidence | location`

### Finance register

`budget item | approved amount | expense | purpose/task | voucher | approval | reimbursement/payment | variance | evidence path`

### Risk, issue, change, and decision registers

Record identifier, date, source, description, probability/impact where relevant, owner, action, decision authority, approval, downstream impact, due date, and closure evidence.

## Integrity Rules

- Use stable IDs; never reuse an ID for a different object.
- Record a new version instead of silently replacing an approved baseline.
- Link registers with IDs and paths, not approximate names.
- Preserve unknown values as `UNVERIFIED` or `MISSING`; never fill gaps by inference.
- Keep confidential data local and within the user's authorized environment.
