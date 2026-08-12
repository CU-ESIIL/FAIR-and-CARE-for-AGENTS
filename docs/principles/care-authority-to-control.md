---
title: "A — Authority to Control"
description: Evidence that permissions, purposes, infrastructure, and governance authority are explicit and enforceable.
---

# A — Authority to Control

**Workflow interpretation:** Claimed authority is distinct from access or technical control; its holder, source, scope, duration, conflicts, actions, infrastructure, and revocation conditions are explicit.

**Current assessment:** **Implemented for the current public, manuscript-only scope.** The policy classifies data and actions, denies unknown actions, lists approved compute and services, prohibits governed-data model use, defines logging/retention, and gates publication. It makes clear that a future rights-holder decision cannot be supplied by maintainers or code.

## Evidence map

| Design criterion | Repository evidence | Status | Remaining work |
| --- | --- | --- | --- |
| Data classification | `governance/policy.json` distinguishes public repository, third-party, and governed/sensitive material; `data/README.md` records that no research data are approved. | **Implemented for current scope** | Add source-specific classifications before new data use. |
| Purpose and action policies | The policy separately decides reading, copying, analysis, inference, training, combining, publishing, and redistribution. | **Implemented** | Rights-holder decisions supersede maintainer policy. |
| Approved infrastructure, models, and endpoints | Owner-authorized local compute and GitHub Actions are approved for public content; listed bibliographic services receive public metadata only; no model is approved for governed data. | **Implemented** | Add an endpoint only after retention, training, location, and authority review. |
| Retention controls | The logging policy defines scope, minimization, release review, and typed redaction; public records prohibit secrets and sensitive/governed content. | **Implemented** | Follow private authorized retention when such data enter scope. |
| Boundary-crossing approval | Scientific claims, external data, publication, release, redistribution, and unknown actions have explicit human or rights-holder gates. | **Implemented** | Maintain GitHub environment protections outside the repository as defense in depth. |
| Network and export restrictions | Deny-by-default decisions and negative tests prohibit governed-data transfer, sensitive logging, and undocumented external pushes. | **Implemented at policy/test layer** | Add sandbox or egress enforcement before any sensitive-data workflow. |
| Community governance links | No community-governed data or relationship is claimed; the policy requires a legitimate decision before use. | **Not applicable yet** | Publish links or contacts only with rights-holder authorization. |

## Verification

- **Current checks:** Repository-policy tests exercise prohibited publication, governed-data transfer, sensitive logging, citation shortcuts, and unknown actions.
- **Target test:** Attempt prohibited export, disclosure, training, combination, publication, and unapproved-endpoint actions.
- **Passing condition:** Controls prevent the action, record the attempt, explain the relevant authority, and escalate ambiguity to the correct person or governance body.

!!! warning "Code does not create authority"
    Technical controls can enforce a legitimate decision; they cannot substitute for consent, governance, or continuing authority from rights-holders.

[Return to all evidence maps](index.md)
