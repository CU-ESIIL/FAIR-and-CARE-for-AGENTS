---
title: "F — Findable"
description: Evidence that the project and its authoritative parts can be discovered and understood.
---

# F — Findable

**Agentic interpretation:** A context-free actor can discover the project and identify its question, people, inputs, workflow, outputs, version, and citation without unsupported guessing.

**Current assessment:** **Partial.** The repository, website, thesis, manuscript, and quality controls are easy to locate. Named contributors, a preferred citation, releases, and a persistent project identifier are not yet recorded.

## Evidence map

| Design criterion | Repository evidence | Status | Remaining work |
| --- | --- | --- | --- |
| One repository linked to one project website | The [README project summary](https://github.com/CU-ESIIL/FAIR-and-CARE-for-AGENTS/blob/main/README.md#project-at-a-glance) links the repository and deployed site; the [landing page](../index.md) links back to the repository and manuscript. | **Implemented** | Preserve the two-way relationship as URLs change. |
| Clear abstract and ownership | The [manuscript abstract](https://github.com/CU-ESIIL/FAIR-and-CARE-for-AGENTS/blob/main/manuscript/fair_care_agentic_science.md#abstract) states the argument, and the site identifies ESIIL and supporting institutions. | **Partial** | Add named authors, roles, responsible contact, and project ownership. |
| Stable URLs and identifiers | Repository and website URLs are declared in the [machine-readable metadata](https://github.com/CU-ESIIL/FAIR-and-CARE-for-AGENTS/blob/main/README.md#machine-readable-project-metadata). | **Partial** | Create a release and add a DOI or other persistent identifier; the README correctly records the DOI as `not-assigned`. |
| Descriptive headings | The [README](https://github.com/CU-ESIIL/FAIR-and-CARE-for-AGENTS/blob/main/README.md), [website](../index.md), and [manuscript](https://github.com/CU-ESIIL/FAIR-and-CARE-for-AGENTS/blob/main/manuscript/fair_care_agentic_science.md) use semantic, descriptive headings. | **Implemented** | Maintain headings as the argument changes. |
| Machine-readable metadata | The README contains a delimited YAML project record; [mkdocs.yml](https://github.com/CU-ESIIL/FAIR-and-CARE-for-AGENTS/blob/main/mkdocs.yml) supplies site name, description, URL, and repository metadata. | **Implemented** | Consider a standard scholarly record such as `CITATION.cff` and structured web metadata. |
| Explicit links among project objects | The [repository map](https://github.com/CU-ESIIL/FAIR-and-CARE-for-AGENTS/blob/main/README.md#repository-map) identifies the authoritative manuscript, citation registry, website, tests, agent instructions, and prompt history. | **Partial** | Add and link data, scientific workflows, results, and provenance if they enter scope. |

## Verification

- **Current checks:** The [Playwright suite](https://github.com/CU-ESIIL/FAIR-and-CARE-for-AGENTS/blob/main/tests/site.spec.ts) checks rendering and local links; the strict MkDocs build checks documentation structure.
- **Target test:** Give a clean agent only the public project URL and score its identification of the question, responsible people, inputs, methods, workflow, outputs, repository, version, and preferred citation.
- **Passing condition:** Correct answers with explicit source links and no unsupported inference.

[Return to all evidence maps](index.md)
