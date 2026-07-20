#!/usr/bin/env python3
"""Create a non-destructive project master record skeleton."""

from pathlib import Path
import argparse
import sys


DIRECTORIES = (
    "00-source",
    "01-requirements",
    "02-proposal",
    "03-baseline",
    "04-plan",
    "05-execution",
    "06-deliverables",
    "07-progress",
    "08-finance",
    "09-changes-risks",
    "10-acceptance",
    "11-closeout",
)

SEED_FILES = {
    "00-source/source-register.md": "# Source Register\n\n| ID | Title | Authority | Version/date | Path | Scope | Status |\n|---|---|---|---|---|---|---|\n",
    "01-requirements/requirements-matrix.md": "# Requirements Matrix\n\n| ID | Source clause | Response | Owner | Due | Output | Evidence | Status | Blocker |\n|---|---|---|---|---|---|---|---|---|\n",
    "03-baseline/indicator-evidence-matrix.md": "# Indicator and Evidence Matrix\n\n| ID | Baseline | Target | Method | Evidence | Reviewer | Result | Gap |\n|---|---|---|---|---|---|---|---|\n",
    "04-plan/task-register.md": "# Task Register\n\n| ID | Requirement/indicator | Work package | Owner | Start | Due | Output | Evidence | Status |\n|---|---|---|---|---|---|---|---|---|\n",
    "06-deliverables/deliverables-register.md": "# Deliverables Register\n\n| ID | Requirement | Version | Owner | Review gate | Submitted | Accepted | Evidence |\n|---|---|---|---|---|---|---|---|\n",
    "08-finance/budget-expense-voucher-register.md": "# Budget, Expense, and Voucher Register\n\n| Budget item | Approved | Expense | Purpose/task | Voucher | Approval | Payment/reimbursement | Evidence |\n|---|---|---|---|---|---|---|---|\n",
    "09-changes-risks/risk-issue-change-decision-register.md": "# Risks, Issues, Changes, and Decisions\n\n| ID | Type | Date | Source | Description | Owner | Action/decision | Authority | Impact | Status | Evidence |\n|---|---|---|---|---|---|---|---|---|---|---|\n",
    "10-acceptance/acceptance-matrix.md": "# Acceptance Matrix\n\n| Requirement/indicator | Deliverable | Evidence | Reviewer | Result | Gap | Remediation | Status |\n|---|---|---|---|---|---|---|---|\n",
    "11-closeout/closeout-checklist.md": "# Closeout Checklist\n\n| Gate | Requirement | Evidence | Owner | Status | Blocker |\n|---|---|---|---|---|---|\n",
}


def initialize(target: Path) -> None:
    if target.exists() and not target.is_dir():
        raise ValueError(f"Target must be a directory path: {target}")

    target.mkdir(parents=True, exist_ok=True)
    for name in DIRECTORIES:
        (target / name).mkdir(exist_ok=True)

    for relative_path, content in SEED_FILES.items():
        destination = target / relative_path
        if not destination.exists():
            destination.write_text(content, encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Create a non-destructive project master record skeleton."
    )
    parser.add_argument("target", type=Path, help="Target directory")
    args = parser.parse_args()

    try:
        initialize(args.target.expanduser().resolve())
    except (OSError, ValueError) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 2

    print(args.target.expanduser().resolve())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
