---
title: "R — Responsibility"
description: Evidence that autonomous action remains attributable to accountable people and institutions.
---

# R — Responsibility

**Agentic interpretation:** Autonomous action remains traceable to named human and institutional accountability.

**Current assessment:** **Implemented for current consequential workflows.** A named human owns manuscript, citation, test, publication, release, and governance decisions; action gates, run provenance, disclosure, correction, rollback, and incident response are explicit.

## Evidence map

| Design criterion | Repository evidence | Status | Remaining work |
| --- | --- | --- | --- |
| Workflow owners | `project.json` and `governance/RESPONSIBILITY.md` name Ty Tuff for each current consequential workflow. | **Implemented** | Reassign explicitly if roles change. |
| Permission boundaries | `AGENTS.md` and `governance/policy.json` classify allowed, proposed, human-gated, rights-holder-gated, and prohibited actions. | **Implemented** | Unknown actions remain prohibited. |
| Model, prompt, tool, and data provenance | Prompt history plus JSON Schema run records capture exposed model/service, compute, network, instructions, inputs, outputs, evaluation, and review. | **Implemented** | State when a provider withholds exact version data. |
| Review gates | Claim changes, fingerprints, evaluation criteria, publication, release, data use, and governance changes have named gates. | **Implemented** | External platform protections should reinforce the versioned policy. |
| Evaluation-suite ownership | The responsible owner, review cycle, known limitations, and issue-based contestation route are documented. | **Implemented** | Review after incidents and each release. |
| Disclosure | `governance/AI_DISCLOSURE.md` defines publication-level disclosure and validation evidence. | **Implemented** | Include a completed disclosure in the submitted manuscript package. |
| Rollback | Git supports source rollback; incident response distinguishes correction, withdrawal, and new versions for public outputs. | **Implemented** | Never use rollback to erase required accountability. |
| Incident response | `governance/INCIDENT_RESPONSE.md` defines stop, contain, notify, assess, correct, recover, and record steps. | **Implemented** | Use private channels for sensitive reports. |

## Verification

- **Current checks:** CI links changes to versioned tests, and citation fingerprints require renewed review after cited prose changes.
- **Target test:** Select a consequential output and reconstruct actor, model, instructions, data, tools, infrastructure, output, evaluation, reviewer, and authorization.
- **Passing condition:** The chain is complete and leads to named people or institutions able to inspect, correct, disclose, and respond.

[Return to all evidence maps](index.md)
