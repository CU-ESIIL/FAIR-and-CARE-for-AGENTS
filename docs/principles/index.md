---
title: FAIR + CARE evidence maps
description: Repository evidence and gaps for each FAIR and CARE design principle.
---

# FAIR + CARE evidence maps

These pages map each design criterion in the working manuscript to concrete, version-controlled evidence in this repository. They answer two questions:

1. What currently demonstrates the principle?
2. What remains absent, partial, or in need of human or community review?

The maps are an implementation snapshot, not a FAIR certification or a claim that CARE can be satisfied by a technical checklist. CARE judgments require legitimate rights-holders, affected communities, and accountable people; the repository can only expose evidence, decisions, controls, and gaps.

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
| FAIR | F — Findable | Strong discovery structure; people, citation, and persistent identifiers remain incomplete. | [Findable](fair-findable.md) |
| FAIR | A — Accessible | Core artifacts and operating context are public; scientific reproduction and support paths remain incomplete. | [Accessible](fair-accessible.md) |
| FAIR | I — Interoperable | Durable formats and clean separation are present; formal schemas and domain semantics remain limited. | [Interoperable](fair-interoperable.md) |
| FAIR | R — Reusable | Versioning, tests, and a lockfile are present; licenses, releases, scientific results, and full provenance are gaps. | [Reusable](fair-reusable.md) |
| CARE | C — Collective Benefit | The manuscript argues for benefit and the option not to automate; no co-defined project benefit process is recorded. | [Collective Benefit](care-collective-benefit.md) |
| CARE | A — Authority to Control | General rights-aware operating rules exist; no project-specific permission model or governance authority is recorded. | [Authority to Control](care-authority-to-control.md) |
| CARE | R — Responsibility | Work and prompts are traceable; named owners, incident response, and consequential-workflow accountability remain gaps. | [Responsibility](care-responsibility.md) |
| CARE | E — Ethics | Human review and rights cautions exist; a harm register, red-team cases, and affected-party review remain gaps. | [Ethics](care-ethics.md) |

## Assessment source and maintenance

The design criteria and tests come from the manuscript's [FAIR + CARE implementation and test matrix](https://github.com/CU-ESIIL/FAIR-and-CARE-for-AGENTS/blob/main/manuscript/fair_care_agentic_science.md#6-from-principles-to-executable-claims). Each page links to the evidence it assesses and states a target test.

Update the relevant evidence map whenever a change materially alters its status. Do not upgrade a CARE status based only on a new file or automated check when legitimate authority, participation, or expert judgment is still missing.
