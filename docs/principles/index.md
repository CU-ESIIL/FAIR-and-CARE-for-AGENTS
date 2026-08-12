---
title: FAIR + CARE evidence maps
description: Repository evidence and gaps for each FAIR and CARE design principle.
---

# FAIR + CARE evidence maps

These pages map each design criterion in the working manuscript to concrete, version-controlled evidence in this repository. They answer two questions:

1. What currently demonstrates the principle?
2. What remains absent, partial, or in need of human or community review?

The maps are an implementation snapshot, not FAIR certification, CARE compliance, or a claim that relational legitimacy can be satisfied by a technical checklist. CARE retains its Indigenous Data Governance purpose. The manuscript's four CARE-informed workflow questions are an operational entry point only; legitimate rights-holders, affected people, institutions, and accountable people determine the applicable obligations. The repository can expose evidence, decisions, controls, and gaps, but cannot certify those relationships itself.

## Status key

| Status | Meaning |
| --- | --- |
| **Implemented** | Direct repository evidence substantially fulfills this criterion. |
| **Partial** | Relevant evidence exists, but an important component is incomplete. |
| **Gap** | The repository does not yet supply the required evidence or process. |
| **Not applicable yet** | The criterion depends on data, software, deployment, or governance relationships not yet present in this manuscript-only project. |

## Principle documents

| Family | Principle | Current summary | Evidence map |
| --- | --- | --- | --- |
| FAIR | F — Findable | Working-draft discovery is implemented; an archival release and DOI remain human release decisions. | [Findable](fair-findable.md) |
| FAIR | A — Accessible | Human and agent onboarding, support, reproduction, boundaries, and approval routes are explicit for the current public scope. | [Accessible](fair-accessible.md) |
| FAIR | I — Interoperable | Canonical artifacts use durable formats and schemas and reproduce without a particular model; environmental data semantics remain out of scope. | [Interoperable](fair-interoperable.md) |
| FAIR | R — Reusable | Exact environments, named outputs, manifests, and run provenance are implemented; licenses and an archival release block public reuse claims. | [Reusable](fair-reusable.md) |
| CARE | C — Collective Benefit | Intended users, observable outcomes, burdens, contestation, and the option not to automate are explicit for this project. | [Collective Benefit](care-collective-benefit.md) |
| CARE | A — Authority to Control | A deny-by-default policy defines action, data, compute, model, logging, transfer, and publication boundaries. | [Authority to Control](care-authority-to-control.md) |
| CARE | R — Responsibility | A named human owns consequential workflows; run records, disclosure, correction, rollback, and incident procedures are present. | [Responsibility](care-responsibility.md) |
| CARE | E — Ethics | A project harm register and negative tests cover current citation, publication, disclosure, and compliance risks. | [Ethics](care-ethics.md) |

## Assessment source and maintenance

The design criteria and tests come from the second draft's [FAIR + CARE design and test matrix](https://github.com/CU-ESIIL/FAIR-and-CARE-for-AGENTS/blob/main/manuscript/fair_care_agentic_science_v2.md#table-1-fair--care-design-and-test-matrix). Each page links to the evidence it assesses and states a target test.

Update the relevant evidence map whenever a change materially alters its status. Do not upgrade a CARE status based only on a new file or automated check when legitimate authority, participation, or expert judgment is still missing.
