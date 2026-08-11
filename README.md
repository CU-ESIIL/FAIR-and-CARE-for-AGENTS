# FAIR + CARE for Agentic Science

This repository is the version-controlled working home for a scientific Perspective on designing environmental science projects for the age of agentic AI. It contains the manuscript, its citation-review record, the public project website, and automated checks for both.

The project asks a practical question: **can an independent actor understand, reproduce, evaluate, modify, and govern a scientific project without relying on undocumented knowledge?** Agentic AI makes that question inexpensive to test repeatedly, but the standard is intended to improve science for people as well as machines.

> The goal is not to make science easier for AI. It is to use AI as a test of whether we have made science explicit enough to be independently understood, reproduced, evaluated, and governed.

## Project at a glance

- **Primary output:** a Perspective / Commentary manuscript
- **Status:** concise second draft; not yet peer reviewed
- **Domain:** environmental science, scientific infrastructure, reproducibility, data governance, and agentic AI
- **Core framework:** `Goal → Instructions → Test → Record`
- **Current manuscript:** [`manuscript/fair_care_agentic_science_v2.md`](manuscript/fair_care_agentic_science_v2.md)
- **Project website:** <https://cu-esiil.github.io/FAIR-and-CARE-for-AGENTS/>
- **Repository:** <https://github.com/CU-ESIIL/FAIR-and-CARE-for-AGENTS>

## What the project contributes

The manuscript develops four connected ideas:

1. A context-free agent can act as a stress test for whether scientific intent, evidence, workflows, evaluation criteria, provenance, and authority have been made explicit.
2. Test-first scientific design should define goals and acceptable evidence before work is delegated to an agent.
3. FAIR principles can be translated into executable tests for discovering, accessing, interpreting, and reusing research objects.
4. CARE principles can be translated into operational controls for collective benefit, authority, responsibility, and ethics.

The repository also proposes a minimal “FAIR + CARE agent-ready repository” that an ordinary environmental science laboratory could realistically maintain.

## Machine-readable project metadata

The YAML block below provides stable, explicit metadata for agents, indexers, and repository tooling. Relative paths resolve from the repository root. `not-declared` and `not-assigned` are intentional values, not omissions.

<!-- machine-readable-project-metadata:start -->

```yaml
schema_version: "1.0"
project:
  name: "FAIR + CARE for Agentic Science"
  repository: "https://github.com/CU-ESIIL/FAIR-and-CARE-for-AGENTS"
  website: "https://cu-esiil.github.io/FAIR-and-CARE-for-AGENTS/"
  description: >-
    A scientific Perspective and supporting repository that use agentic AI as a
    stress test for explicit, reproducible, evaluable, and governable science.
  project_type: "scientific-perspective"
  status: "second-draft"
  peer_reviewed: false
  primary_domain: "environmental-science"
  keywords:
    - agentic-ai
    - FAIR
    - CARE
    - reproducibility
    - provenance
    - research-infrastructure
    - data-governance
  thesis: >-
    The goal is not to make science easier for AI. It is to use AI as a test of
    whether science is explicit enough to be independently understood,
    reproduced, evaluated, and governed.
artifacts:
  current_manuscript: "manuscript/fair_care_agentic_science_v2.md"
  current_manuscript_pdf: "manuscript/fair_care_agentic_science_v2.pdf"
  current_citation_review_registry: "manuscript/citation_audit_v2.json"
  draft_1_manuscript: "manuscript/fair_care_agentic_science.md"
  draft_1_manuscript_pdf: "output/pdf/fair_care_agentic_science.pdf"
  draft_1_citation_review_registry: "manuscript/citation_audit.json"
  website_source: "docs/"
  principle_evidence_maps: "docs/principles/"
  website_configuration: "mkdocs.yml"
  agent_instructions: "AGENTS.md"
  prompt_history: "PROMPT_LOG.md"
  ci_workflow: ".github/workflows/ci.yml"
interfaces:
  manuscript_format: "Markdown"
  citation_registry_format: "JSON"
  project_metadata_format: "YAML embedded in README.md"
  website_generator: "MkDocs Material"
quality_controls:
  website_build: "mkdocs build --strict"
  website_tests: "npm run test:site"
  manuscript_tests: "python3 -m unittest discover -s tests -p 'test_*.py'"
  manuscript_audit: "python3 scripts/manuscript_audit.py --check --online"
  ci_triggers:
    - push-to-main
    - pull-request-to-main
    - manual
    - weekly
governance:
  repository_is_source_of_truth: true
  website_is_rendered_view: true
  human_review_required_for_scientific_claims: true
  prompt_logging_required: true
  data_included: false
  repository_license: "not-declared"
  content_license: "not-declared"
identifiers:
  doi: "not-assigned"
```

<!-- machine-readable-project-metadata:end -->

## Repository map

| Path | Role | Authority |
| --- | --- | --- |
| `manuscript/fair_care_agentic_science_v2.md` | Concise, editable second draft | Current manuscript source |
| `manuscript/fair_care_agentic_science_v2.pdf` | Typeset second draft for reading and review | Derived from the v2 Markdown source |
| `manuscript/fair_care_agentic_science.md` | Full first draft | Preserved Draft 1 source |
| `output/pdf/fair_care_agentic_science.pdf` | Typeset first draft | Derived from the Draft 1 Markdown source |
| `manuscript/citation_audit_v2.json` and `manuscript/citation_audit.json` | Source metadata and claim-level citation reviews | Audit record for each manuscript draft |
| `scripts/manuscript_audit.py` | Word-count and citation-integrity audit | Executable quality check |
| `docs/` | Project website content and assets | Rendered communication layer |
| `docs/principles/` | FAIR + CARE criteria, repository evidence, status, and gaps | Principle-by-principle implementation map |
| `tests/` | Manuscript and website tests | Executable acceptance checks |
| `.github/workflows/ci.yml` | Continuous-integration workflow | Automated check definition |
| `AGENTS.md` | Repository operating rules for agents | Required agent instructions |
| `PROMPT_LOG.md` | Verbatim prompts and response summaries | Append-only project history |

The repository is the source of truth. The website is a rendered view of repository state and should not contain authoritative material that is absent from the repository.

## Read or edit the manuscript

Open [`manuscript/fair_care_agentic_science_v2.md`](manuscript/fair_care_agentic_science_v2.md) in any Markdown-capable editor. It is the concise current draft. The full first draft remains preserved at [`manuscript/fair_care_agentic_science.md`](manuscript/fair_care_agentic_science.md). Both drafts deliberately retain `[CITATION NEEDED]` markers so unresolved claims remain visible rather than appearing settled.

When a cited passage changes, its recorded review fingerprint becomes invalid. Update the citation registry only after rereading the source and confirming that:

- the source exists and its bibliographic metadata are correct;
- the manuscript accurately represents the source;
- the source actually supports the manuscript's claim; and
- qualifications in either the source or the manuscript have not been lost.

Automated metadata and fingerprint checks support this review; they do not replace scholarly judgment, community authority, or subject-matter expertise.

Create a typeset PDF from the canonical manuscript with:

```bash
pip install -r requirements-pdf.txt
python3 scripts/render_manuscript_pdf.py \
  --source manuscript/fair_care_agentic_science_v2.md \
  --output manuscript/fair_care_agentic_science_v2.pdf
```

Edit the Markdown source, not the PDF, and regenerate after manuscript changes. Omitting the arguments still renders Draft 1 to `output/pdf/fair_care_agentic_science.pdf`.

## Preview the website

Requirements: Python 3.12 or compatible, Node.js, and npm.

```bash
pip install -r requirements.txt
mkdocs serve
```

Open <http://127.0.0.1:8000/FAIR-and-CARE-for-AGENTS/>. The deployed site is built from `docs/` using `mkdocs.yml`.

## Run the quality checks

Install browser-test dependencies once:

```bash
npm ci
npx playwright install chromium
```

Run the same core checks used by continuous integration:

```bash
mkdocs build --strict
npm run test:site
python3 -m unittest discover -s tests -p "test_*.py"
python3 scripts/manuscript_audit.py --check --online
python3 scripts/manuscript_audit.py \
  --manuscript manuscript/fair_care_agentic_science_v2.md \
  --registry manuscript/citation_audit_v2.json \
  --check --online
```

The Playwright suite checks page rendering, links, calls to action, institutional-logo destinations, images, browser errors, mobile overflow, and the back-to-top control.

The manuscript audit reports words by section, citation mentions, unique sources, bibliography entries, reviewed claims, and unresolved citation placeholders. It also checks bibliography/registry consistency, reviewed-passage fingerprints, and authoritative source metadata. Omit `--online` when network access is unavailable; local structural checks will still run.

## Working in this repository

Before changing anything, read [`AGENTS.md`](AGENTS.md). It defines the operating contract for human-assisted and autonomous agents, including small traceable edits, synchronized documentation, citation review, testing, data sovereignty, and prompt logging.

For every user prompt handled in this repository:

1. append the prompt verbatim to [`PROMPT_LOG.md`](PROMPT_LOG.md);
2. make and test the smallest change that satisfies the request; and
3. complete the log entry with files changed and checks run.

Do not silently add external data or assume that accessible material is openly reusable. Record source, access method, format, licensing, citation requirements, and governance constraints whenever data or third-party content is introduced.

## Current boundaries

- The manuscript is an editable working argument, not a published consensus statement.
- Passing repository tests does not establish that the scientific argument is correct.
- Citation checks cannot determine community legitimacy or replace expert review.
- No research dataset is currently distributed in this repository.
- Repository and manuscript-content licenses have not yet been declared.
- A publication DOI has not yet been assigned.
