---
title: "C — Collective Benefit"
description: Evidence that automation has a stated beneficiary and that benefits and burdens are evaluated.
---

# C — Collective Benefit

**Workflow interpretation:** Every workflow identifies who should benefit, who may bear burdens, who defined the benefit, who may contest it, and when the work must change or stop.

**Current assessment:** **Implemented for this repository's limited public purpose.** `governance/BENEFIT.md` names intended beneficiaries, repository-level outcomes, burdens, an evaluator, contestation, and the option not to proceed. It explicitly refuses to claim benefit for communities that have not defined it.

## Evidence map

| Design criterion | Repository evidence | Status | Remaining work |
| --- | --- | --- | --- |
| Benefit statement | `governance/BENEFIT.md` and `project.json` name environmental scientists, ecologists, RSEs, students, reviewers, collaborators, and maintainers and define observable outcomes. | **Implemented** | Revisit with actual users before publication. |
| Co-defined outcomes | The owner evaluates repository-level outcomes, and contributors may contest them through issues. No community-governed outcome is asserted. | **Implemented for current scope** | Any future affected community must define its own benefit before automation. |
| Contributor return plan | The public outputs, editable sources, citation and contribution routes are named; no community-provided data or labor is currently in scope. | **Not applicable yet** | Co-design return, credit, and remedy before such contributions begin. |
| Burden and access assessment | The benefit statement records CI, review, maintenance, storage, and disclosure burdens and limits logging to consequential work. | **Implemented for current scope** | Measure actual burdens as users contribute. |
| Post-deployment evaluation | No agentic scientific system is deployed from this repository. | **Not applicable yet** | Before deployment, name evaluators, measures, review dates, remedies, and a stopping rule. |
| Option not to automate | The benefit and authority policies require work to stop when benefit, permission, or legitimate authority is absent. | **Implemented** | Preserve this gate as scope expands. |

## Verification

- **Current checks:** The repository audit confirms that a benefit statement and explicit limitations exist; human and affected-party judgment determine whether benefit is real.
- **Target test:** Before deployment, identify a beneficiary, observable benefit, measurement process, time horizon, evaluator, expected burdens, and remedy.
- **Passing condition:** Affected parties recognize the outcome as beneficial, burdens are accounted for, and the workflow can be changed or stopped.

!!! warning "CARE is relational"
    A repository maintainer cannot self-certify Collective Benefit on behalf of a community. Evidence must come from a legitimate participatory process.

[Return to all evidence maps](index.md)
