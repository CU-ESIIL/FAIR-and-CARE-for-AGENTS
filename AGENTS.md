# AGENTS.md

## Core Operating Contract
- Treat this repository as the source of truth.
- Treat the website as a rendered view of repository state.
- Read `project.json` for the project question, current version, responsible human, canonical artifacts, data profile, and release blockers.
- Read `governance/policy.json` before using external data, models, services, compute, publication channels, or other boundary-crossing capabilities. Unknown actions are prohibited by default.
- Prefer small, additive, traceable edits.
- Keep documentation synchronized with code and project structure.
- Keep the repository minimalist by default.

## Canonical Project Workflow
- The current editable manuscript is `manuscript/fair_care_agentic_science_v2.md`; its reading PDF is derived.
- The Draft 2 citation review is `manuscript/citation_audit_v2.json`.
- The editable Supporting Information is `manuscript/supplementary_information.md`; its citation review is `manuscript/supplement_citation_audit.json`; its derived PDF is `output/pdf/fair_care_agentic_science_supplement.pdf`.
- The editable Figure 1 source is `manuscript/figures/figure1_workflow.py`; `manuscript/figures/figure1_workflow.svg` is generated with `python3 scripts/build_figures.py` and must not be edited directly.
- The reusable specification is `templates/agent-workflow-spec.yml`; its bounded synthetic demonstration is `examples/habitat-assessment/specification.yml`.
- Keep unresolved author and submission decisions in `manuscript/TODO_BEFORE_SUBMISSION.md`, not in visible manuscript prose or PDFs.
- The website source is `docs/`; generated site output is not authoritative.
- The named reproducible outputs are the Draft 2 reading PDF, Ecology formatting proof, Supporting Information PDF, and their audit reports. Reproduce them with `python3 scripts/reproduce.py --output-dir results/reproduction`.
- The Ecology formatting requirements are summarized in `docs/ecology-author-guidelines.md`; editable submission metadata are in `manuscript/ecology_submission.json`; the derived formatting proof is `output/pdf/fair_care_agentic_science_ecology.pdf`.
- Do not describe the Ecology PDF as submission-ready: the journal accepts PDF Main Documents only for genuine LaTeX submissions, and the current proof is generated from Markdown with ReportLab.
- The eight principle evidence maps live in `docs/principles/` and must reflect actual repository evidence and unresolved human decisions.

## Goal → Instructions → Evaluation → Record
- Before consequential work, complete `templates/agent-task.md` or state the same four elements in an existing version-controlled issue or task record.
- Consequential work includes scientific claims, citation interpretation, evaluation criteria, public artifacts, releases, governed-data boundaries, and governance controls.
- Evaluate scientific, computational, provenance, and governance acceptance as applicable. Appropriate refusal or escalation can be a successful governance result.
- After consequential work, add or update a run record in `provenance/records/` using `provenance/run-record.schema.json`.
- A run record marked `pending` documents work but does not authorize publication.

## Default Workflow
- Inspect repository structure before editing.
- Make the smallest diff that solves the request.
- Update related docs when behavior, workflows, or outputs change.
- Update changelog, dev log, or equivalent history files for meaningful changes.
- Update `PROMPT_LOG.md` for every user prompt handled in this repository.
- Preserve existing structure and historical context.
- Do not perform destructive rewrites unless explicitly requested.

## Prompt Logging
- Append one entry to `PROMPT_LOG.md` for every user prompt, including follow-up prompts that arrive during ongoing work.
- Reproduce the user's prompt verbatim, preserving its spelling, punctuation, and formatting as closely as Markdown allows, except that secrets, personal information, governed knowledge, sensitive ecological locations, and security details must never be committed. Use a typed `[REDACTED: reason]` marker and an authorized private record when necessary.
- Do not include system or developer instructions, private reasoning, or tool output in the prompt log.
- Summarize what the agent did in response, including files changed and checks run. If no repository action was taken, state that explicitly.
- Create the entry when work begins and complete its response summary before sending the final response to the user.
- Keep prior entries append-only. Edit an earlier entry only to correct an inaccurate record of the current task.

## Documentation and Website Policy
- Treat `docs/` as project-level documentation and website source.
- Update docs whenever code, workflows, or outputs change.
- Amend existing docs when possible; do not replace whole files without need.
- Preserve navigation, readability, and consistency in website changes.
- Keep default website behavior clean and minimal unless the user asks for more expressive design.

## Testing Policy
- Assume `tests/` may exist before a full testing framework is defined.
- Do not invent domain-specific tests when expected behavior is unclear.
- Add the smallest meaningful tests when behavior is known.
- Prefer early-stage checks such as smoke tests, import tests, CLI tests, schema checks, or example-based checks.
- Run `mkdocs build --strict` and `npm run test:site` after website changes.
- Run `python3 scripts/repository_audit.py` and `python3 -m unittest discover -s tests -p "test_*.py"` after governance, structure, workflow, or provenance changes.
- Run `python3 scripts/manuscript_audit.py --check` after manuscript or citation changes.
- For Draft 2, pass `--manuscript manuscript/fair_care_agentic_science_v2.md --registry manuscript/citation_audit_v2.json` to the manuscript audit.
- For Supporting Information, pass `--manuscript manuscript/supplementary_information.md --registry manuscript/supplement_citation_audit.json` to the manuscript audit.
- After changing the Ecology guide, submission metadata, manuscript structure, or renderer, run `python3 scripts/render_ecology_manuscript_pdf.py` and `python3 -m unittest tests.test_ecology_submission` and visually inspect every rendered page.
- PDF renderers must work on clean Linux infrastructure without macOS fonts. Keep the `MANUSCRIPT_FORCE_PORTABLE_FONTS=1` test path working; use and visually inspect the required Times New Roman fonts for the canonical Ecology proof.
- Add `--online` to the manuscript audit when network access is available so authoritative source records are rechecked.
- Register every in-text citation and bibliography entry in the citation-audit registry associated with that manuscript draft.
- Run `python3 scripts/build_figures.py --check` and `python3 scripts/manuscript_quality_check.py` before generating manuscript PDFs.
- Generate PDFs only from editable source through the documented renderers; never edit a derived PDF directly.
- Preserve the distinction among FAIR-aligned evidence, the separate general governance and authorization gate, and CARE as an Indigenous Data Governance framework. Never describe the general gate as CARE or as a CARE assessment.
- Treat claim review as scholarly judgment: read the source, document how it supports the cited paragraph, and update the paragraph fingerprint only after review. Never refresh fingerprints mechanically to silence CI.
- If tests are deferred, document the gap; do not imply coverage that does not exist.

## Authority and Action Boundaries
- Agents may read public repository content, edit version-controlled source locally, run documented local checks, and propose changes.
- Human approval is required before changing accepted scientific claims or evaluation criteria, refreshing citation-review fingerprints, publishing the website, releasing the manuscript, assigning a license, or making an irreversible external change.
- Human and legitimate rights-holder approval is required before ingesting, combining, inferring from, publishing, or redistributing externally governed data.
- Never send governed or sensitive data to an external model; publish without review; fabricate or misrepresent a citation; refresh a citation fingerprint without source review; record sensitive content in a public log; or push an undocumented external artifact.
- No model or service is pre-approved for governed or sensitive data. Stop and escalate when authority, data class, endpoint, retention, provider training, or jurisdiction is unclear.
- Website deployment is a manually confirmed publication action. A passing build is not permission to deploy.

## Responsibility, Disclosure, and Incidents
- The accountable owner and workflow responsibilities are named in `project.json` and `governance/RESPONSIBILITY.md`.
- Disclose material AI assistance according to `governance/AI_DISCLOSURE.md`.
- Follow `governance/INCIDENT_RESPONSE.md` for citation, disclosure, publication, provenance, permission, or control failures.
- Use GitHub issues for non-sensitive corrections or challenges. Never disclose sensitive incident details publicly.

## Package and Structure Separation Policy
- Keep website structure and package structure clearly separated.
- Do not automatically repurpose `docs/` for package-native docs or build artifacts.
- For Python packaging requests, prefer standard Python layout, typically `src/`.
- For R packaging requests, follow standard R conventions (`R/`, `man/`, `DESCRIPTION`, `NAMESPACE`, optional `vignettes/`).
- For other ecosystems, follow ecosystem conventions.
- If structural conflicts arise, choose a durable long-term structure and document the decision.

## Data Discovery and Data Use Policy
- Prefer open and FAIR data when possible.
- Prefer streaming or lazy-access workflows over bulk downloads when feasible.
- Use standards-based discovery systems (for example STAC) when relevant.
- When relevant, consider streaming-friendly tooling such as xarray, zarr, GDAL, rasterio, pystac-client, stackstac, gdalcubes, terra, stars, cubo, or equivalent tools.
- When introducing data, document source, access method, format, license, and citation requirements.
- Do not silently ingest external data into the project.
- This repository currently approves no research, governed, or sensitive dataset. Follow `data/README.md` before changing that status.

## Data Sovereignty and Intellectual Property Policy
- Consider licensing, copyright, privacy, Indigenous data sovereignty, and related restrictions for all data and content.
- If rights or permissions are unclear, document uncertainty and avoid assuming open reuse.

## Design and Usability Policy
- Keep the website simple, readable, and easy to extend by default.
- When design improvements are requested, prioritize system-level improvements (layout, spacing, typography, hierarchy, navigation, consistency).
- Do not use scattered one-off styling hacks.
- If direct site inspection is possible, verify readability, navigation, link integrity, and that docs still reflect repository state.

## Decision Logging
- Reflect meaningful structural, architectural, documentation, data-source, or design decisions in changelog, dev log, roadmap, or equivalent history files when appropriate.
- Update `DECISIONS.md` for consequential project decisions and `CHANGELOG.md` for material repository or public-output changes.
