---
title: "R — Reusable"
description: Evidence that the project can be reused as a portable, permission-aware research object.
---

# R — Reusable

**Agentic interpretation:** The project is a portable, permission-aware executable research object rather than a collection of disconnected files.

**Current assessment:** **Operationally implemented; public release blocked.** Exact environments, a version policy, named reproducible outputs, hashes, tests, and consequential-run provenance are present. The owner must still choose licenses and create an archival release/DOI before claiming release-level reuse.

## Evidence map

| Design criterion | Repository evidence | Status | Remaining work |
| --- | --- | --- | --- |
| Version control | The Git repository is the declared source of truth, and agent work is recorded in [PROMPT_LOG.md](https://github.com/CU-ESIIL/FAIR-and-CARE-for-AGENTS/blob/main/PROMPT_LOG.md). | **Implemented** | Continue small, traceable commits and document releases. |
| Tagged releases | `VERSION`, `CHANGELOG.md`, and `project.json` define the draft version and require a human-approved archival release. | **Partial** | Create the tag and archival record only after the working tree, license, and reviews are ready. |
| Licenses | `project.json`, `CITATION.cff`, and the release audit explicitly block reuse claims while code/content licenses are undecided and exclude third-party logos. | **Blocked human decision** | The owner must select licenses; an agent must not invent legal permission. |
| Containers or locked environments | Both Python requirement files use exact pins and `package-lock.json` locks browser dependencies; CI uses Python 3.12. | **Implemented** | Review pins at controlled upgrade intervals. |
| Versioned or immutable data references | No research dataset is distributed or referenced as an input. | **Not applicable yet** | Record persistent identifiers, versions, checksums, access, licenses, and governance before data are used. |
| Model and inference metadata | Consequential run records capture service, exposed model/version, compute boundary, instructions, inputs, outputs, evaluation, and human review. | **Implemented** | Continue to state when exact provider metadata are unavailable. |
| Test data and expected results | The project has no scientific dataset; its declared result is the current manuscript PDF and citation-audit report. | **Implemented for project type** | Add authorized scientific fixtures only if the project scope expands. |
| Documented reproduction workflow | `scripts/reproduce.py` produces the PDF, audit report, and SHA-256 manifest with one command. | **Implemented** | CI runs it on clean infrastructure. |
| Provenance | Citation reviews, prompt history, decisions, JSON Schema, and run records connect inputs, actors, environment, outputs, tests, and pending/approved review. | **Implemented** | Release records must show human approval. |

## Verification

- **Current checks:** CI builds the website and validates manuscript and citation integrity on clean runners.
- **Target test:** Clone a tagged release on clean infrastructure and reproduce a named result using authorized, versioned inputs.
- **Passing condition:** The result meets declared scientific tolerances and records inputs, environment, resources, agent involvement, and human decisions.

[Return to all evidence maps](index.md)
