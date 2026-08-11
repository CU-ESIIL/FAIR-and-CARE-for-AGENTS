---
title: "R — Responsibility"
description: Evidence that autonomous action remains attributable to accountable people and institutions.
---

# R — Responsibility

**Agentic interpretation:** Autonomous action remains traceable to named human and institutional accountability.

**Current assessment:** **Partial.** Version control, prompt logging, citation-review records, tests, and human-review requirements create traceability. The repository does not yet name workflow owners, define consequential-action gates, record complete run provenance, or supply incident-response procedures.

## Evidence map

| Design criterion | Repository evidence | Status | Remaining work |
| --- | --- | --- | --- |
| Workflow owners | Institutional relationships appear on the website, but no person is named as manuscript, test-suite, citation-registry, or release owner. | **Gap** | Name accountable maintainers and backups for each consequential workflow and evaluation suite. |
| Permission boundaries | [AGENTS.md](https://github.com/CU-ESIIL/FAIR-and-CARE-for-AGENTS/blob/main/AGENTS.md) defines repository scope, cautious data use, scholarly citation review, and documentation duties. | **Partial** | Classify actions agents may perform, may propose, and may not perform; name required approvers. |
| Model, prompt, tool, and data provenance | [PROMPT_LOG.md](https://github.com/CU-ESIIL/FAIR-and-CARE-for-AGENTS/blob/main/PROMPT_LOG.md) records user instructions and response summaries; [citation_audit.json](https://github.com/CU-ESIIL/FAIR-and-CARE-for-AGENTS/blob/main/manuscript/citation_audit.json) records source-review evidence. | **Partial** | Record model/service, version, configuration, tools, infrastructure, inputs, outputs, and reviewers for consequential runs. |
| Review gates | AGENTS.md requires source reading and human scholarly judgment before updating citation-review fingerprints. | **Partial** | Add gates for publication, high-consequence outputs, governed-data actions, and irreversible external changes. |
| Evaluation-suite ownership | Tests and [CI](https://github.com/CU-ESIIL/FAIR-and-CARE-for-AGENTS/blob/main/.github/workflows/ci.yml) are versioned, but owners, review dates, and contestation procedures are absent. | **Partial** | Assign owners and review cycles; document known limits and how a test can be challenged. |
| Disclosure | The prompt log exposes agent-requested work and the manuscript contains a citation-integrity section. | **Partial** | Define publication-level disclosure of material AI contributions and human validation. |
| Rollback | Git history supports review and reversal of text and configuration changes. | **Implemented** | Define rollback procedures for deployed or published outputs. |
| Incident response | No issue classification, notification route, containment procedure, or post-incident review is documented. | **Gap** | Add a lightweight incident-response and correction policy before consequential deployment. |

## Verification

- **Current checks:** CI links changes to versioned tests, and citation fingerprints require renewed review after cited prose changes.
- **Target test:** Select a consequential output and reconstruct actor, model, instructions, data, tools, infrastructure, output, evaluation, reviewer, and authorization.
- **Passing condition:** The chain is complete and leads to named people or institutions able to inspect, correct, disclose, and respond.

[Return to all evidence maps](index.md)
