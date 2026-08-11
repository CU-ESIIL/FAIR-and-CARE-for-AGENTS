---
title: "I — Interoperable"
description: Evidence that scientific meaning and editable artifacts can survive changes in tools and agents.
---

# I — Interoperable

**Agentic interpretation:** Scientific meaning and editability survive changes in model, vendor, agent framework, and interface.

**Current assessment:** **Implemented for current artifacts.** Canonical products use durable editable formats, current relationships and run provenance have schemas, and conventional non-agent tools reproduce the primary output. Environmental data semantics remain out of scope because no research dataset is present.

## Evidence map

| Design criterion | Repository evidence | Status | Remaining work |
| --- | --- | --- | --- |
| Open, durable formats | The manuscript and documentation use Markdown; configuration uses YAML and JSON; checks use Python and TypeScript. All are editable outside a proprietary agent interface. | **Implemented** | Preserve plain-text canonical sources for future outputs. |
| Domain standards | The Draft 2 citation registry uses DOI and authoritative standard identifiers; `CITATION.cff` uses a standard scholarly citation format. | **Implemented for current scope** | Select environmental/geospatial standards before data enter scope. |
| Explicit schemas, units, identifiers, and relationships | `project.json`, the citation registry, governance policy, harm register, and JSON Schema run record expose current identifiers and relationships. | **Implemented for current scope** | Units and coordinate semantics are not applicable without research data. |
| Predictable separation of concerns | The [repository map](https://github.com/CU-ESIIL/FAIR-and-CARE-for-AGENTS/blob/main/README.md#repository-map) separates manuscript, documentation, scripts, tests, workflow configuration, instructions, and history. | **Implemented** | Add separate data, analysis, results, and provenance areas only when those artifacts exist. |
| Editable source for outputs | The manuscript and website are maintained as editable source, with generated site output excluded by [.gitignore](https://github.com/CU-ESIIL/FAIR-and-CARE-for-AGENTS/blob/main/.gitignore). | **Implemented** | Require editable source and source data for future figures and tables. |
| Independence from a particular model or vendor | Repository outputs require only conventional Python/Node tools; agent provenance records exposed model/service identity without making it a runtime dependency. | **Implemented** | A second-agent usability study would add evidence but is not required to reproduce the output. |

## Verification

- **Current checks:** Git diffs expose changes to plain-text sources; CI builds the website and audits the manuscript with conventional command-line tools.
- **Target test:** Move an artifact between two agent environments and a conventional environment, then open, interpret, modify, execute, and reproduce it without proprietary conversion.
- **Passing condition:** Syntax and scientific semantics—including identifiers, units, and lineage—survive the transfer.

[Return to all evidence maps](index.md)
