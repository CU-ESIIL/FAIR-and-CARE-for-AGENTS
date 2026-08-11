---
title: "R — Reusable"
description: Evidence that the project can be reused as a portable, permission-aware research object.
---

# R — Reusable

**Agentic interpretation:** The project is a portable, permission-aware executable research object rather than a collection of disconnected files.

**Current assessment:** **Partial.** Version control, documented checks, a Node lockfile, and citation provenance support reuse of the manuscript and website. The repository does not yet declare licenses, tagged releases, a fully pinned Python environment, versioned data, a scientific result, or complete agent-run provenance.

## Evidence map

| Design criterion | Repository evidence | Status | Remaining work |
| --- | --- | --- | --- |
| Version control | The Git repository is the declared source of truth, and agent work is recorded in [PROMPT_LOG.md](https://github.com/CU-ESIIL/FAIR-and-CARE-for-AGENTS/blob/main/PROMPT_LOG.md). | **Implemented** | Continue small, traceable commits and document releases. |
| Tagged releases | No release or version policy is documented. | **Gap** | Define versioning and create an archival release for manuscript milestones. |
| Licenses | The [README boundaries](https://github.com/CU-ESIIL/FAIR-and-CARE-for-AGENTS/blob/main/README.md#current-boundaries) explicitly record repository and content licenses as undeclared. | **Gap** | Choose and document appropriate code and content licenses; do not assume one license covers governed data. |
| Containers or locked environments | [package-lock.json](https://github.com/CU-ESIIL/FAIR-and-CARE-for-AGENTS/blob/main/package-lock.json) pins browser-test dependencies; [requirements.txt](https://github.com/CU-ESIIL/FAIR-and-CARE-for-AGENTS/blob/main/requirements.txt) constrains but does not fully lock Python packages. | **Partial** | Lock the Python environment or provide a container when reproducibility needs justify it. |
| Versioned or immutable data references | No research dataset is distributed or referenced as an input. | **Not applicable yet** | Record persistent identifiers, versions, checksums, access, licenses, and governance before data are used. |
| Model and inference metadata | Verbatim prompts are retained in PROMPT_LOG.md, but model identity, configuration, tools, and execution manifests are not systematically recorded. | **Partial** | Add run-level provenance for agent work that materially affects scientific conclusions. |
| Test data and expected results | Repository behavior has tests, but there is no scientific fixture or declared scientific result. | **Gap** | Add a small authorized fixture and reproduce one named figure, table, statistic, or result within stated tolerances. |
| Documented reproduction workflow | The [README quality checks](https://github.com/CU-ESIIL/FAIR-and-CARE-for-AGENTS/blob/main/README.md#run-the-quality-checks) reproduce the website and manuscript audit. | **Partial** | Add a scientific reproduction command and expected output record. |
| Provenance | The citation registry records source-review provenance and the prompt log records requested changes. | **Partial** | Add run manifests connecting inputs, code, model, tools, environment, outputs, evaluations, and reviewers. |

## Verification

- **Current checks:** CI builds the website and validates manuscript and citation integrity on clean runners.
- **Target test:** Clone a tagged release on clean infrastructure and reproduce a named result using authorized, versioned inputs.
- **Passing condition:** The result meets declared scientific tolerances and records inputs, environment, resources, agent involvement, and human decisions.

[Return to all evidence maps](index.md)
