# Agent task specification: revised manuscript architecture

## Goal

- Implement the user-directed manuscript architecture without independently changing its scientific or governance argument.
- Make the tacit-knowledge problem and pre-delegation specification central; compress the Perspective; separate FAIR, CARE, and the general governance gate; and keep controls proportional to consequence.
- Produce editable, reproducible manuscript, figure, example, template, checks, documentation, and PDFs.

## Instructions

- Canonical manuscript: `manuscript/fair_care_agentic_science_v2.md`.
- Canonical citation registry: `manuscript/citation_audit_v2.json`.
- Preserve CARE as an Indigenous Data Governance framework. The general authorization gate is the authors' proposal and is not CARE or CARE certification.
- Do not fabricate evidence, citations, author facts, consultation, approval, or declarations.
- Move submission-facing gaps out of visible manuscript prose and into `manuscript/TODO_BEFORE_SUBMISSION.md`.
- Keep the implementation compact; do not create a policy engine, benchmark suite, or evaluator.

## Test

- Manuscript is shorter and uses `Goal → Instructions → Evaluation → Record` consistently.
- Abstract and conclusion align; one ecological example remains; FAIR/CARE/governance distinctions remain accurate.
- Table 1 and editable Figure 1 are visually readable in both PDFs.
- Generated manuscript contains no submission placeholders or unresolved references.
- Citation, manuscript, repository, unit, reproducibility, strict website, and Playwright checks pass.

## Record

- Prompt record: `PROMPT_LOG.md` and this task file.
- Run record: `provenance/records/2026-08-30-revised-manuscript-architecture.json`.
- Human review remains required before publication or release.
