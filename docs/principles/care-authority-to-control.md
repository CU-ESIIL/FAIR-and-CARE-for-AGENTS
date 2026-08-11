---
title: "A — Authority to Control"
description: Evidence that permissions, purposes, infrastructure, and governance authority are explicit and enforceable.
---

# A — Authority to Control

**Agentic interpretation:** Access is decomposed into permissions for reading, copying, inference, training, combining, publishing, and redistribution; computation occurs only in authorized places.

**Current assessment:** **Early / partial.** Repository-wide instructions require rights and governance uncertainty to be surfaced, but the project has no governed dataset, rights-holder agreement, action-level permission model, approved-compute policy, or governance authority record.

## Evidence map

| Design criterion | Repository evidence | Status | Remaining work |
| --- | --- | --- | --- |
| Data classification | The README states that no research data are included; [AGENTS.md](https://github.com/CU-ESIIL/FAIR-and-CARE-for-AGENTS/blob/main/AGENTS.md#data-sovereignty-and-intellectual-property-policy) requires privacy, licensing, copyright, and Indigenous data sovereignty to be considered. | **Not applicable yet** | Classify each future source by sensitivity, authority, access, permitted purposes, and prohibited actions. |
| Purpose and action policies | AGENTS.md prohibits silent external-data ingestion and instructs agents not to assume open reuse when rights are unclear. | **Partial** | Distinguish permission to read, copy, analyze, infer, train, combine, publish, and redistribute for each governed object. |
| Approved infrastructure, models, and endpoints | No project-specific approved-compute inventory exists. | **Gap** | Record approved services, model identifiers, data locations, endpoint retention/training terms, and jurisdictional constraints. |
| Retention controls | The prompt log is required, but no retention, minimization, redaction, or deletion policy is defined. | **Gap** | Define what may be logged, who may see it, how long it is retained, and how governed material is excluded or redacted. |
| Boundary-crossing approval | AGENTS.md requires uncertainty about permissions to be documented and unsafe assumptions avoided. | **Partial** | Name approvers and enforce review before external transfer, publication, or changes in purpose. |
| Network and export restrictions | No governed data or executable network/export policy is present. | **Gap** | Add technical controls and negative tests before sensitive data are introduced. |
| Community governance links | The manuscript requires community- and context-specific authority but the repository links no governing protocol or rights-holder decision. | **Gap** | Add only agreements and contacts that rights-holders authorize for publication; do not infer authority from access. |

## Verification

- **Current checks:** Repository instructions make unknown rights a stop condition, but there is no action-level enforcement test.
- **Target test:** Attempt prohibited export, disclosure, training, combination, publication, and unapproved-endpoint actions.
- **Passing condition:** Controls prevent the action, record the attempt, explain the relevant authority, and escalate ambiguity to the correct person or governance body.

!!! warning "Code does not create authority"
    Technical controls can enforce a legitimate decision; they cannot substitute for consent, governance, or continuing authority from rights-holders.

[Return to all evidence maps](index.md)
