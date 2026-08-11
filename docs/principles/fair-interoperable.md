---
title: "I — Interoperable"
description: Evidence that scientific meaning and editable artifacts can survive changes in tools and agents.
---

# I — Interoperable

**Agentic interpretation:** Scientific meaning and editability survive changes in model, vendor, agent framework, and interface.

**Current assessment:** **Partial.** The project uses durable text formats and conventional tools, and it separates major concerns cleanly. Formal schemas, domain-level semantics, research data, scientific results, and cross-environment reproduction are not yet present.

## Evidence map

| Design criterion | Repository evidence | Status | Remaining work |
| --- | --- | --- | --- |
| Open, durable formats | The manuscript and documentation use Markdown; configuration uses YAML and JSON; checks use Python and TypeScript. All are editable outside a proprietary agent interface. | **Implemented** | Preserve plain-text canonical sources for future outputs. |
| Domain standards | The [citation registry](https://github.com/CU-ESIIL/FAIR-and-CARE-for-AGENTS/blob/main/manuscript/citation_audit.json) uses DOIs and authoritative URLs where available. | **Partial** | Adopt appropriate environmental metadata, geospatial, provenance, and packaging standards when data and workflows are added. |
| Explicit schemas, units, identifiers, and relationships | The README's YAML block and citation registry declare identifiers and relationships among current artifacts. | **Partial** | Publish schemas; document units, coordinate systems, missing values, and controlled vocabularies for future scientific data. |
| Predictable separation of concerns | The [repository map](https://github.com/CU-ESIIL/FAIR-and-CARE-for-AGENTS/blob/main/README.md#repository-map) separates manuscript, documentation, scripts, tests, workflow configuration, instructions, and history. | **Implemented** | Add separate data, analysis, results, and provenance areas only when those artifacts exist. |
| Editable source for outputs | The manuscript and website are maintained as editable source, with generated site output excluded by [.gitignore](https://github.com/CU-ESIIL/FAIR-and-CARE-for-AGENTS/blob/main/.gitignore). | **Implemented** | Require editable source and source data for future figures and tables. |
| Independence from a particular model or vendor | Repository instructions and artifacts do not require a specific AI model or chat interface. | **Partial** | Test the documented tasks with a second agent environment and a conventional non-agent workflow. |

## Verification

- **Current checks:** Git diffs expose changes to plain-text sources; CI builds the website and audits the manuscript with conventional command-line tools.
- **Target test:** Move an artifact between two agent environments and a conventional environment, then open, interpret, modify, execute, and reproduce it without proprietary conversion.
- **Passing condition:** Syntax and scientific semantics—including identifiers, units, and lineage—survive the transfer.

[Return to all evidence maps](index.md)
