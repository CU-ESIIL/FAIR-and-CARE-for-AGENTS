#!/usr/bin/env python3
"""Audit the repository's executable FAIR + CARE implementation."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

RULE_PATHS = {
    "F — Give every project an authoritative front door": [
        "README.md",
        "project.json",
        "CITATION.cff",
        "docs/index.md",
        "docs/ecology-author-guidelines.md",
        "mkdocs.yml",
    ],
    "A — Give every agent an orientation": [
        "AGENTS.md",
        "CONTRIBUTING.md",
        "templates/agent-task.md",
    ],
    "I — Make scientific products portable": [
        "manuscript/fair_care_agentic_science_v2.md",
        "manuscript/citation_audit_v2.json",
        "provenance/run-record.schema.json",
    ],
    "R — Make the project executable elsewhere": [
        "VERSION",
        "requirements.txt",
        "requirements-pdf.txt",
        "package-lock.json",
        "analysis/README.md",
        "manuscript/ecology_submission.json",
        "scripts/render_ecology_manuscript_pdf.py",
        "scripts/reproduce.py",
    ],
    "C — State who benefits and who bears burdens": [
        "governance/BENEFIT.md",
        "project.json",
    ],
    "A — Make authority explicit": [
        "governance/policy.json",
        "data/README.md",
        "SECURITY.md",
    ],
    "R — Assign accountable people and institutions": [
        "governance/RESPONSIBILITY.md",
        "provenance/README.md",
        "provenance/records/2026-08-11-repository-alignment.json",
    ],
    "E — Identify harms and test boundaries safely": [
        "governance/harm-register.json",
        "governance/INCIDENT_RESPONSE.md",
        "tests/test_repository_policy.py",
    ],
}

REQUIRED_ACTIONS = {
    "read_public_repository": "allowed",
    "publish_website": "human_approval",
    "publish_or_release_manuscript": "human_approval",
    "ingest_external_data": "human_and_rights_holder_approval",
    "send_governed_data_to_external_model": "prohibited",
    "publish_without_review": "prohibited",
    "fabricate_or_misrepresent_citation": "prohibited",
    "record_secret_or_sensitive_content_in_public_log": "prohibited",
}


def read_json(relative_path: str) -> dict:
    with (ROOT / relative_path).open(encoding="utf-8") as handle:
        return json.load(handle)


def audit() -> tuple[list[str], list[str]]:
    errors: list[str] = []
    notes: list[str] = []

    for rule, paths in RULE_PATHS.items():
        missing = [path for path in paths if not (ROOT / path).is_file()]
        if missing:
            errors.append(f"{rule}: missing {', '.join(missing)}")
        else:
            notes.append(f"PASS — {rule}")

    project = read_json("project.json")
    if not project.get("responsible_human", {}).get("name"):
        errors.append("project.json must name a responsible human")
    if project.get("data_profile", {}).get("governed_or_sensitive_data_approved") is not False:
        errors.append("current project profile must not approve governed or sensitive data")
    if not project.get("release_blockers"):
        errors.append("project.json must make current release blockers explicit")

    policy = read_json("governance/policy.json")
    if policy.get("default_decision") != "prohibited":
        errors.append("governance policy must prohibit unknown actions by default")
    for action, expected in REQUIRED_ACTIONS.items():
        actual = policy.get("actions", {}).get(action)
        if actual != expected:
            errors.append(f"policy action {action!r}: expected {expected!r}, found {actual!r}")
    if policy.get("model_policy", {}).get("approved_for_governed_or_sensitive_data") != []:
        errors.append("no model may be pre-approved for governed or sensitive data")
    if not policy.get("publication_gate", {}).get("manual_confirmation_required"):
        errors.append("publication must require manual human confirmation")

    harm_register = read_json("governance/harm-register.json")
    required_case_fields = {
        "id",
        "unacceptable_outcome",
        "affected_parties",
        "prevention",
        "detection",
        "escalation",
        "recovery",
        "owner",
        "automated_test",
    }
    if len(harm_register.get("cases", [])) < 4:
        errors.append("harm register must include at least four project-specific cases")
    for case in harm_register.get("cases", []):
        missing = sorted(required_case_fields - set(case))
        if missing:
            errors.append(f"harm case {case.get('id', '<unknown>')} missing {', '.join(missing)}")

    run = read_json("provenance/records/2026-08-11-repository-alignment.json")
    for key in (
        "run_id",
        "goal",
        "responsible_human",
        "actor",
        "compute",
        "instructions",
        "inputs",
        "outputs",
        "evaluations",
        "human_review",
    ):
        if not run.get(key):
            errors.append(f"consequential run record missing {key}")

    for requirements_file in ("requirements.txt", "requirements-pdf.txt"):
        for line in (ROOT / requirements_file).read_text(encoding="utf-8").splitlines():
            if line.strip() and not re.match(r"^[A-Za-z0-9_.-]+==[^=<>~!]+$", line.strip()):
                errors.append(f"{requirements_file} is not exactly pinned: {line}")

    pages_workflow = (ROOT / ".github/workflows/pages.yml").read_text(encoding="utf-8")
    if "workflow_dispatch:" not in pages_workflow or "confirm_publication" not in pages_workflow:
        errors.append("website deployment must require an explicit manual confirmation input")
    if re.search(r"\n\s+push:\s*\n", pages_workflow):
        errors.append("website deployment must not run automatically on push")

    return errors, notes


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--release",
        action="store_true",
        help="Also require the legal and archival decisions needed for a public release.",
    )
    args = parser.parse_args()
    errors, notes = audit()

    project = read_json("project.json")
    release_blockers = project.get("release_blockers", [])
    if args.release and release_blockers:
        errors.extend(f"release blocker: {blocker}" for blocker in release_blockers)

    print("# FAIR + CARE repository audit")
    for note in notes:
        print(note)
    if release_blockers:
        print("\nRelease readiness: BLOCKED by declared human decisions")
        for blocker in release_blockers:
            print(f"- {blocker}")
    if errors:
        print("\nFindings:")
        for error in errors:
            print(f"- {error}")
        return 1
    print("\nOperational repository controls: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
