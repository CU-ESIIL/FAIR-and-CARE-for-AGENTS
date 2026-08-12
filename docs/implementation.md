---
title: Repository implementation
description: How this repository applies Goal → Instructions → Test → Record and the eight FAIR + CARE design rules to itself.
---

# Repository implementation

This manuscript project is its own first implementation case. The controls below apply to the current public manuscript, documentation, citation metadata, website, and tests. They do not certify FAIR or CARE for a future dataset or create authority over Indigenous, community-governed, personal, restricted, or sensitive ecological information.

## Goal → Instructions → Test → Record

Every workflow receives a lightweight screen for benefit and burdens, legitimate authority, accountability, and foreseeable harm. Consequential work begins with [`templates/agent-task.md`](https://github.com/CU-ESIIL/FAIR-and-CARE-for-AGENTS/blob/main/templates/agent-task.md). [`AGENTS.md`](https://github.com/CU-ESIIL/FAIR-and-CARE-for-AGENTS/blob/main/AGENTS.md) defines canonical sources and action boundaries. Automated and human tests cover scientific claims, computation, provenance, and governance. Structured run records in [`provenance/`](https://github.com/CU-ESIIL/FAIR-and-CARE-for-AGENTS/tree/main/provenance) preserve the resulting evidence and approval status.

## Eight rules in practice

| Rule | Current implementation | Test |
| --- | --- | --- |
| Give every project an authoritative front door. | Associated website relating the repository, `project.json`, `CITATION.cff`, version, owner, canonical artifacts, and limitations. | Website crawl plus repository-structure audit. |
| Give every agent an orientation. | `AGENTS.md`, contribution workflow, task template, canonical commands, stop conditions, and approval gates. | Start without chat context and follow only versioned instructions. |
| Make scientific products portable. | Markdown, JSON, YAML, Python, TypeScript, editable source, schemas, and model-independent commands. | Build and audit with conventional command-line tools. |
| Make the project executable elsewhere. | Exact dependency pins and one command that recreates the Draft 2 PDF and audit report with hashes. | Clean CI reproduction using `scripts/reproduce.py`. |
| State who benefits and who bears burdens. | Named audiences, repository-level outcomes, burdens, contestation route, remedy, and explicit option not to proceed. | Review `governance/BENEFIT.md` against actual outcomes. |
| Make authority explicit. | Deny-by-default action policy; data classes; approved compute and services; model, logging, transfer, retention, publication, and stop rules. | Use safe negative-policy fixtures for publication, transfer, sensitive logging, citation shortcuts, and unknown actions. |
| Assign accountable people and institutions. | Ty Tuff is the operational owner; the policy separately gates scientific review, rights-holder authority, and publication or release approval. | Reconstruct a consequential run and distinguish operation, governance, review, and authorization. |
| Identify harms and test boundaries safely. | Versioned harm register, safe refusal cases, citation mutation tests, manual publication, and incident-response procedure. | Run governance and manuscript adversarial tests without performing a prohibited real-world action. |

## Run the checks

```bash
python3 scripts/repository_audit.py
python3 -m unittest discover -s tests -p "test_*.py"
python3 scripts/reproduce.py --output-dir results/reproduction
python3 -m unittest tests.test_ecology_submission
mkdocs build --strict
npm run test:site
```

The normal audit passes when operational controls are present. The stricter `python3 scripts/repository_audit.py --release` remains blocked while licenses, an archival release/DOI, and required external reviews are unresolved. This separation prevents an agent from converting an honest limitation into a false compliance claim.

## Current boundary

No research dataset or governed/sensitive data is approved in this repository. No model or external service is pre-approved for such data. If the scope changes, the workflow must stop until legitimate authorities and affected parties define benefit, permission, compute, retention, disclosure, review, and remedy.
