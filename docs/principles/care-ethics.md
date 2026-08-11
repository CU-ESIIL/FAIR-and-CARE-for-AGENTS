---
title: "E — Ethics"
description: Evidence that unacceptable scientific and social outcomes are anticipated, tested, and escalated.
---

# E — Ethics

**Agentic interpretation:** Unacceptable scientific and social outcomes are anticipated, tested, detected, and escalated before deployment.

**Current assessment:** **Early / partial.** The repository requires attention to intellectual property, privacy, Indigenous data sovereignty, citation accuracy, and human judgment. It does not yet contain a project harm register, affected-party analysis, domain bias tests, red-team cases, or a recovery process.

## Evidence map

| Design criterion | Repository evidence | Status | Remaining work |
| --- | --- | --- | --- |
| Harm register | The [manuscript Ethics section](https://github.com/CU-ESIIL/FAIR-and-CARE-for-AGENTS/blob/main/manuscript/fair_care_agentic_science.md#54-ethics-specify-unacceptable-outcomes-before-deployment) lists plausible environmental-science harms. | **Partial** | Create a project-specific register with affected parties, triggers, mitigations, detectors, escalation paths, and owners. |
| Affected-party analysis | The manuscript requires affected communities and ecosystems to be considered. | **Gap** | Identify actual affected parties and document an authorized process for participation, disagreement, and remedy. |
| Bias and disclosure checks | No data or deployed model exists; therefore no geographic, observational, representational, or outcome-bias test is implemented. | **Not applicable yet** | Add domain-appropriate tests before a scientific model or dataset is used. |
| Refusal and escalation rules | AGENTS.md requires agents to avoid assuming open reuse when rights are uncertain and requires expert review of citation claims. | **Partial** | Define project-specific refusal cases, approvers, response times, and fallback paths. |
| Scientific hallucination tests | The [manuscript audit](https://github.com/CU-ESIIL/FAIR-and-CARE-for-AGENTS/blob/main/scripts/manuscript_audit.py) verifies source identity, bibliography consistency, and reviewed-passage fingerprints; its [unit tests](https://github.com/CU-ESIIL/FAIR-and-CARE-for-AGENTS/blob/main/tests/test_manuscript_audit.py) check review invalidation. | **Partial** | Add adversarial unsupported-claim, citation-fabrication, overstatement, and uncertainty tests; retain expert source review. |
| Red-team cases | No representative scientific, security, disclosure, or governance red-team suite exists. | **Gap** | Develop cases with domain experts and, where relevant, affected rights-holders—not only generic prompts. |
| Human control over high-consequence decisions | The README and AGENTS.md state that automated checks do not replace scientific, community, or scholarly judgment. | **Partial** | Define which decisions always remain with named humans or legitimate governance authorities and enforce those gates. |

## Verification

- **Current checks:** Citation auditing catches some fabricated or altered scholarly support, but it is not a general ethics evaluation.
- **Target test:** Ask what the worst scientifically plausible failure is, then run prevention, detection, escalation, recovery, and review scenarios.
- **Passing condition:** Representative harms are detected or prevented, uncertainty is communicated, recovery is possible, and accountable people and affected parties can contest the outcome.

[Return to all evidence maps](index.md)
