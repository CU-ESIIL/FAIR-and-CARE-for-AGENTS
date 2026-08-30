# Changelog

This file records material changes to the repository and its public outputs. Draft versions are not releases unless a Git tag and release record say otherwise.

## 0.2.0-draft — 2026-08-11

- Integrated the author-provided 30 August 2026 two-author Ecology manuscript as the canonical editable draft, expanded its citation registry to 25 reviewed sources, and synchronized the renderer, Table 1, Figure 1, repository guidance, example, template, and quality checks.
- Replaced the earlier universal CARE-informed screen with a separate general governance and authorization gate; CARE remains specifically an Indigenous Data Governance framework.
- Standardized the pre-delegation sequence as Goal → Instructions → Evaluation → Record and added a placeholder-leak check plus reproducible editable vector figure generation to CI.
- Added the concise second manuscript draft and its verified PDF.
- Added principle-by-principle evidence maps.
- Added explicit FAIR + CARE repository metadata, governance policies, task specifications, run provenance, negative tests, and a reproducible primary-output workflow.
- Made public website deployment a manually confirmed action.
- Added a current, cited Ecology author-guidelines summary, editable submission metadata, an Ecology-style formatting proof, and automated submission-format checks.
- Recentered the manuscript and website on designing FAIR and CARE into agentic workflows so agents strengthen the practices that support better human science; retained agent failure as a secondary diagnostic rather than the main thesis.
- Made both PDF renderers portable to Linux CI by adding a tested PDF base-font fallback while preserving Times New Roman for the canonical Ecology proof.
- Removed unnecessary runtime Google Fonts and GitHub API requests while preserving explicit static repository links; Playwright now reports the URL and status of failed homepage resources.
- Preserved the 12 August simulated-panel revision in project history; its universal CARE-informed entry-screen decision is superseded by the 30 August architecture decision recorded in `DECISIONS.md`.

## 0.1.0-draft

- Established the manuscript, project website, citation audit, prompt log, and initial continuous-integration tests.
