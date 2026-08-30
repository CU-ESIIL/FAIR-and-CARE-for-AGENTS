# FAIR + CARE for Agentic Science

This repository is the version-controlled working home for a scientific Perspective on designing environmental science projects for the age of agentic AI. It contains the manuscript, its citation-review record, the public project website, and automated checks for both.

The project asks a practical question: **what must be specified before a person delegates consequential environmental-science work to a computer?**

> Giving an agent a repository does not give it the context, judgment, or authority of a collaborator. Specify the work before the computer acts.

FAIR-aligned infrastructure makes research objects and metadata understandable. A separate general governance gate determines what the workflow may do. CARE retains its original and continuing purpose in Indigenous Data Governance; the manuscript does not redefine CARE, use it as a generic gate, or claim CARE compliance.

## Project at a glance

- **Primary output:** a Perspective / Commentary manuscript
- **Status:** concise second draft; not yet peer reviewed
- **Version:** `0.2.0-draft`
- **Responsible human:** Ty Tuff, repository and manuscript owner
- **Questions and corrections:** [GitHub issues](https://github.com/CU-ESIIL/FAIR-and-CARE-for-AGENTS/issues) for non-sensitive reports
- **Domain:** environmental science, scientific infrastructure, reproducibility, data governance, and agentic AI
- **Core framework:** `Goal → Instructions → Evaluation → Record`
- **Current manuscript:** [`manuscript/fair_care_agentic_science_v2.md`](manuscript/fair_care_agentic_science_v2.md)
- **Project website:** <https://cu-esiil.github.io/FAIR-and-CARE-for-AGENTS/>
- **Repository:** <https://github.com/CU-ESIIL/FAIR-and-CARE-for-AGENTS>

## What the project contributes

The manuscript develops five connected ideas:

1. Repositories rarely contain all of the context, judgment, and authority an experienced collaborator brings.
2. **Goal → Instructions → Evaluation → Record** should be specified before consequential work begins.
3. FAIR-aligned infrastructure helps people and machines find and interpret evidence, but FAIR does not authorize an action.
4. A separate, proportionate governance gate establishes benefit, authority, accountability, relationships, and stopping conditions.
5. CARE remains an Indigenous Data Governance framework and cannot be replaced or certified by the manuscript's general gate.

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
    A scientific Perspective and supporting repository about specifying
    consequential computer-assisted environmental-science work before action.
  project_type: "scientific-perspective"
  status: "second-draft"
  version: "0.2.0-draft"
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
    An agent does not inherit project context, scientific judgment, or legitimate
    authority from repository access. Specify Goal, Instructions, Evaluation, and
    Record before consequential action; keep FAIR-aligned evidence, a general
    governance gate, and CARE Indigenous Data Governance conceptually distinct.
artifacts:
  project_record: "project.json"
  citation_file: "CITATION.cff"
  version: "VERSION"
  current_manuscript: "manuscript/fair_care_agentic_science_v2.md"
  current_manuscript_pdf: "manuscript/fair_care_agentic_science_v2.pdf"
  current_citation_review_registry: "manuscript/citation_audit_v2.json"
  figure_1_editable_source: "manuscript/figures/figure1_workflow.py"
  figure_1_generated_svg: "manuscript/figures/figure1_workflow.svg"
  workflow_specification_template: "templates/agent-workflow-spec.yml"
  synthetic_example: "examples/habitat-assessment/specification.yml"
  submission_todo: "manuscript/TODO_BEFORE_SUBMISSION.md"
  ecology_author_guidelines: "docs/ecology-author-guidelines.md"
  ecology_submission_metadata: "manuscript/ecology_submission.json"
  ecology_formatting_pdf: "output/pdf/fair_care_agentic_science_ecology.pdf"
  draft_1_manuscript: "manuscript/fair_care_agentic_science.md"
  draft_1_manuscript_pdf: "output/pdf/fair_care_agentic_science.pdf"
  draft_1_citation_review_registry: "manuscript/citation_audit.json"
  website_source: "docs/"
  principle_evidence_maps: "docs/principles/"
  website_configuration: "mkdocs.yml"
  agent_instructions: "AGENTS.md"
  governance_policy: "governance/policy.json"
  benefit_statement: "governance/BENEFIT.md"
  responsibility_record: "governance/RESPONSIBILITY.md"
  harm_register: "governance/harm-register.json"
  run_record_schema: "provenance/run-record.schema.json"
  task_template: "templates/agent-task.md"
  prompt_history: "PROMPT_LOG.md"
  ci_workflow: ".github/workflows/ci.yml"
interfaces:
  manuscript_format: "Markdown"
  citation_registry_format: "JSON"
  project_metadata_format: "YAML embedded in README.md"
  website_generator: "MkDocs Material"
quality_controls:
  repository_audit: "python3 scripts/repository_audit.py"
  primary_output_reproduction: "python3 scripts/reproduce.py --output-dir results/reproduction"
  website_build: "mkdocs build --strict"
  website_tests: "npm run test:site"
  manuscript_tests: "python3 -m unittest discover -s tests -p 'test_*.py'"
  manuscript_audit: "python3 scripts/manuscript_audit.py --check --online"
  manuscript_quality: "python3 scripts/manuscript_quality_check.py"
  figure_reproducibility: "python3 scripts/build_figures.py --check"
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
  governed_or_sensitive_data_approved: false
  default_unknown_action: "prohibited"
  publication_requires_human_confirmation: true
  responsible_human: "Ty Tuff"
  repository_license: "not-declared"
  content_license: "not-declared"
identifiers:
  doi: "not-assigned"
  repository_version: "0.2.0-draft"
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
| `docs/ecology-author-guidelines.md` | Current official Ecology requirements, project mapping, and submission blockers | Journal-targeting guide checked 11 August 2026 |
| `manuscript/ecology_submission.json` | Editable journal, author, title-page, declaration, and formatting metadata | Source for the Ecology formatting proof |
| `output/pdf/fair_care_agentic_science_ecology.pdf` | Double-spaced, line-numbered Ecology review layout | Derived formatting proof, not an allowed Main Document |
| `project.json` and `CITATION.cff` | Project identity, ownership, canonical objects, version, citation, and declared blockers | Machine-readable front door |
| `governance/` | Benefit, permissions, compute/model boundaries, responsibility, harms, disclosure, and incident response | Human and machine-readable governance record |
| `provenance/` | Run-record schema, template, and consequential-run records | Reconstructable agent and human activity |
| `templates/agent-task.md` and `templates/agent-workflow-spec.yml` | Goal → Instructions → Evaluation → Record specification | Required planning pattern and copyable machine-readable template |
| `examples/habitat-assessment/specification.yml` | Synthetic, bounded habitat-map specification | Executable documentation example; contains no real observations |
| `manuscript/figures/figure1_workflow.py` and `.svg` | Editable Figure 1 source and generated vector | Source plus reproducible derivative |
| `analysis/`, `data/`, `environment/`, and `results/` | Reproduction command, data status, environment, and output authority | Portable project workflow |

The repository is the source of truth. The website is a rendered view of repository state and should not contain authoritative material that is absent from the repository.

## Read or edit the manuscript

Open [`manuscript/fair_care_agentic_science_v2.md`](manuscript/fair_care_agentic_science_v2.md) in any Markdown-capable editor. It is the current author-provided draft transcribed from the 30 August 2026 Ecology proof. The full first draft remains preserved at [`manuscript/fair_care_agentic_science.md`](manuscript/fair_care_agentic_science.md). Draft 2 contains no drafting placeholders; unresolved author decisions are isolated in [`manuscript/TODO_BEFORE_SUBMISSION.md`](manuscript/TODO_BEFORE_SUBMISSION.md).

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

The renderer uses the specified local manuscript fonts when the complete set is available. On clean Linux systems such as GitHub Actions, it falls back to ReportLab's portable Times, Helvetica, and Courier PDF base fonts so structural tests and reproducible builds do not depend on macOS. Set `MANUSCRIPT_FORCE_PORTABLE_FONTS=1` to exercise that path locally. Final journal proofs must still be rendered and visually checked with the journal-required font.

Reproduce the named current output—the Draft 2 PDF and its citation-integrity/word-count report—with one command:

```bash
python3 -m pip install -r requirements-pdf.txt
python3 scripts/reproduce.py --output-dir results/reproduction
```

The command also creates the Ecology formatting proof and writes a manifest containing input/output hashes, the environment, and the applicable governance boundary. Add `--online` to recheck public source identities through the approved bibliographic services.

The project-specific [Ecology author guide](docs/ecology-author-guidelines.md) records the live requirements and outstanding submission decisions. The formatted PDF uses the visible Ecology review layout, but the journal permits a PDF Main Document only for a genuine LaTeX submission. This ReportLab-generated proof must therefore be converted to a checked Word document or rebuilt as LaTeX before submission.

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
python3 scripts/repository_audit.py
python3 scripts/build_figures.py --check
python3 scripts/manuscript_quality_check.py
python3 -m unittest discover -s tests -p "test_*.py"
python3 scripts/manuscript_audit.py --check --online
python3 scripts/manuscript_audit.py \
  --manuscript manuscript/fair_care_agentic_science_v2.md \
  --registry manuscript/citation_audit_v2.json \
  --check --online
```

The Playwright suite checks page rendering, links, calls to action, institutional-logo destinations, images, browser errors, mobile overflow, and the back-to-top control.

The manuscript audit reports words by section, citation mentions, unique sources, bibliography entries, reviewed claims, and unresolved citation placeholders. It also checks bibliography/registry consistency, reviewed-passage fingerprints, and authoritative source metadata. Omit `--online` when network access is unavailable; local structural checks will still run.

The repository audit checks the evidence required by all eight design rules, the deny-by-default action policy, named responsibility, approved compute/model boundaries, harm cases, run provenance, exact Python pins, and the manual publication gate. `python3 scripts/repository_audit.py --release` intentionally fails while legal, archival, or external-review decisions remain incomplete.

## Working in this repository

Before changing anything, read [`AGENTS.md`](AGENTS.md). It defines the operating contract for human-assisted and autonomous agents, including small traceable edits, synchronized documentation, citation review, testing, data sovereignty, and prompt logging.

For consequential work, define **Goal → Instructions → Evaluation → Record** using [`templates/agent-task.md`](templates/agent-task.md) or [`templates/agent-workflow-spec.yml`](templates/agent-workflow-spec.yml), consult [`governance/policy.json`](governance/policy.json), and complete a structured record in [`provenance/records/`](provenance/records/). The policy distinguishes actions agents may take, actions requiring human or rights-holder approval, and actions that are prohibited. Unknown actions are prohibited by default.

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
- No governed or sensitive data, external model, or endpoint is approved for data processing.
- Repository and manuscript-content licenses have not yet been declared; `CITATION.cff` therefore uses `NOASSERTION`, and third-party logos remain outside any future project license.
- A versioned archival release and publication DOI have not yet been assigned.
- The release-readiness audit remains blocked until the responsible human chooses licenses, approves a release and archival identifier, and completes the required scholarly and Indigenous data sovereignty review. These are explicit human decisions, not gaps an agent may silently fill.
- Ecology-specific blockers are also explicit: a Perspective invitation or accepted proposal, author-approved declarations and funding, final reference copyediting, and an allowed Word or genuine LaTeX submission package.
