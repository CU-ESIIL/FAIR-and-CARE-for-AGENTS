---
title: "E — Ethics"
description: Evidence that unacceptable scientific and social outcomes are anticipated, tested, and escalated.
---

# E — Ethics

**Agentic interpretation:** Unacceptable scientific and social outcomes are anticipated, tested, detected, and escalated before deployment.

**Current assessment:** **Implemented for current risks.** The project harm register identifies affected parties, prevention, detection, escalation, recovery, owners, and tests for citation fabrication, unreviewed publication, sensitive disclosure, and misleading compliance. Domain-data bias tests remain out of scope because no scientific data or deployed model is present.

## Evidence map

| Design criterion | Repository evidence | Status | Remaining work |
| --- | --- | --- | --- |
| Harm register | `governance/harm-register.json` defines four current unacceptable outcomes with affected parties, controls, escalation, recovery, owners, and test references. | **Implemented** | Expand with affected experts when scope changes. |
| Affected-party analysis | Each current harm case names affected readers, authors, contributors, institutions, communities, rights-holders, species, or ecosystems as applicable; issue and private reporting routes support challenge and remedy. | **Implemented for current scope** | A future affected community must define its own participation process. |
| Bias and disclosure checks | No data or deployed model exists; therefore no geographic, observational, representational, or outcome-bias test is implemented. | **Not applicable yet** | Add domain-appropriate tests before a scientific model or dataset is used. |
| Refusal and escalation rules | The policy denies unknown actions and governed-data model use, names approval classes, and links to incident response. | **Implemented** | Human response time is context-dependent; urgent disclosure is prioritized. |
| Scientific hallucination tests | Citation identity, bibliography consistency, claim fingerprints, paragraph mutations, and prohibited citation shortcuts are tested; human source review remains required. | **Implemented for cited-claim integrity** | Adversarial novelty and expert interpretation review remain scholarly work. |
| Red-team cases | Governance tests attempt unreviewed publication, governed-data transfer, sensitive logging, fabricated support, fingerprint shortcuts, and unknown capabilities. | **Implemented for current scope** | Add domain cases before data or scientific models enter scope. |
| Human control over high-consequence decisions | The responsible owner and rights-holder gates cover claims, evaluation, publication, release, data use, and governance; the Pages workflow requires manual confirmation. | **Implemented** | Repository policy cannot substitute for platform or community authority. |

## Verification

- **Current checks:** Citation mutation tests and repository-policy negative tests cover the registered harms; the harm register states their limits and recovery path.
- **Target test:** Ask what the worst scientifically plausible failure is, then run prevention, detection, escalation, recovery, and review scenarios.
- **Passing condition:** Representative harms are detected or prevented, uncertainty is communicated, recovery is possible, and accountable people and affected parties can contest the outcome.

[Return to all evidence maps](index.md)
