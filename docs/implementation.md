---
title: Repository implementation
description: How this repository applies Goal → Instructions → Evaluation → Record, FAIR-aligned evidence, and a separate governance gate.
---

# Repository implementation

This manuscript project is its own first implementation case. The controls below apply to the current public manuscript, documentation, citation metadata, website, and tests. They do not certify FAIR or CARE for a future dataset or create authority over Indigenous, community-governed, personal, restricted, or sensitive ecological information.

## Goal → Instructions → Evaluation → Record

Consequential work begins with [`templates/agent-task.md`](https://github.com/CU-ESIIL/FAIR-and-CARE-for-AGENTS/blob/main/templates/agent-task.md) or the copyable [`agent-workflow-spec.yml`](https://github.com/CU-ESIIL/FAIR-and-CARE-for-AGENTS/blob/main/templates/agent-workflow-spec.yml). [`AGENTS.md`](https://github.com/CU-ESIIL/FAIR-and-CARE-for-AGENTS/blob/main/AGENTS.md) defines canonical sources and action boundaries. Automated and human evaluation covers scientific claims, computation, provenance, and governance. Structured run records in [`provenance/`](https://github.com/CU-ESIIL/FAIR-and-CARE-for-AGENTS/tree/main/provenance) preserve the resulting evidence and approval status.

The editable [Supporting Information implementation guide](https://github.com/CU-ESIIL/FAIR-and-CARE-for-AGENTS/blob/main/manuscript/supplementary_information.md) provides the minimum-start checklist, reusable worksheet, machine-readable examples, consequence guide, evaluation protocol, governance questions, and clean-start audit in a form laboratories can adapt.

## Three layers in practice

| Layer | Current implementation | Quick check |
| --- | --- | --- |
| FAIR-aligned evidence | `project.json`, `CITATION.cff`, canonical files, rich citation metadata, identifiers, versions, access conditions, provenance, and exact environments. | Locate one intended input and trace it to one output. |
| Agent orientation and execution | `AGENTS.md`, task and workflow templates, the synthetic habitat example, build commands, evaluation scripts, editable Figure 1 source, and run records. | Start clean and reproduce the named output from versioned instructions. |
| General governance and authorization | A deny-by-default policy, responsible human, benefit and harm records, service/data limits, safe refusal tests, and manual release gates. | Confirm who can authorize, stop, review, release, correct, or withdraw the work. |

CARE is not the third layer. CARE remains an Indigenous Data Governance framework. If Indigenous Peoples, data, Knowledges, lands, waters, resources, or rights enter scope, the general gate does not establish permission; the relevant Indigenous authority and protocols govern whether and how work proceeds.

## Run the checks

```bash
python3 scripts/repository_audit.py
python3 scripts/build_figures.py --check
python3 scripts/manuscript_quality_check.py
python3 -m unittest discover -s tests -p "test_*.py"
python3 scripts/reproduce.py --output-dir results/reproduction
python3 scripts/manuscript_audit.py --manuscript manuscript/supplementary_information.md --registry manuscript/supplement_citation_audit.json --check
python3 -m unittest tests.test_ecology_submission
mkdocs build --strict
npm run test:site
```

The normal audit passes when operational controls are present. The stricter `python3 scripts/repository_audit.py --release` remains blocked while licenses, an archival release/DOI, and required external reviews are unresolved. This separation prevents an agent from converting an honest limitation into a false compliance claim.

## Current boundary

No research dataset or governed/sensitive data is approved in this repository. No model or external service is pre-approved for such data. If the scope changes, the workflow must stop until legitimate authorities and affected parties define benefit, permission, compute, retention, disclosure, review, and remedy.
