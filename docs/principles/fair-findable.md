---
title: "F — Findable"
description: Evidence that the project and its authoritative parts can be discovered and understood.
---

# F — Findable

**Agentic interpretation:** A context-free actor can discover the project and identify its question, people, inputs, workflow, outputs, version, and citation without unsupported guessing.

**Current assessment:** **Implemented for the working-draft scope.** The front door now names the question, responsible human, version, manuscript, website, repository, citation guidance, reproduction workflow, governance records, and limitations. An archival release and DOI remain declared release blockers.

## Evidence map

| Design criterion | Repository evidence | Status | Remaining work |
| --- | --- | --- | --- |
| One repository linked to one project website | The [README project summary](https://github.com/CU-ESIIL/FAIR-and-CARE-for-AGENTS/blob/main/README.md#project-at-a-glance) links the repository and deployed site; the [landing page](../index.md) links back to the repository and manuscript. | **Implemented** | Preserve the two-way relationship as URLs change. |
| Clear abstract and ownership | The [Draft 2 abstract](https://github.com/CU-ESIIL/FAIR-and-CARE-for-AGENTS/blob/main/manuscript/fair_care_agentic_science_v2.md#abstract), `project.json`, and `CITATION.cff` state the argument, owner, contact, and citation. | **Implemented** | Reconfirm authorship before submission. |
| Stable URLs and identifiers | Repository and website URLs plus `0.2.0-draft` are declared in `project.json`, `VERSION`, and `CITATION.cff`. | **Partial** | The owner must create an archival release and DOI; the absence is machine-readable rather than hidden. |
| Descriptive headings | The [README](https://github.com/CU-ESIIL/FAIR-and-CARE-for-AGENTS/blob/main/README.md), [website](../index.md), and [current manuscript](https://github.com/CU-ESIIL/FAIR-and-CARE-for-AGENTS/blob/main/manuscript/fair_care_agentic_science_v2.md) use semantic, descriptive headings. | **Implemented** | Maintain headings as the argument changes. |
| Machine-readable metadata | The README metadata, `project.json`, `CITATION.cff`, and `mkdocs.yml` expose identity, relationships, authority, version, and limitations. | **Implemented** | Add an archival identifier when assigned. |
| Explicit links among project objects | The repository map and `project.json` link manuscript, citation review, website, data status, reproduction, governance, tests, and provenance. | **Implemented** | Maintain the map as scope changes. |

## Verification

- **Current checks:** The [Playwright suite](https://github.com/CU-ESIIL/FAIR-and-CARE-for-AGENTS/blob/main/tests/site.spec.ts) checks rendering and local links; the strict MkDocs build checks documentation structure.
- **Target test:** Give a clean agent only the public project URL and score its identification of the question, responsible people, inputs, methods, workflow, outputs, repository, version, and preferred citation.
- **Passing condition:** Correct answers with explicit source links and no unsupported inference.

[Return to all evidence maps](index.md)
