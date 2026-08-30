---
title: "A — Accessible"
description: Evidence that authorized actors can obtain the project and the context needed to use it correctly.
---

# A — Accessible

**Agentic interpretation:** An authorized actor can obtain both research objects and the operational context needed to use them correctly; restricted access is explained rather than bypassed.

**Current assessment:** **Implemented for the current public, manuscript-only scope.** Human and agent onboarding, a named reproducible output, data-status instructions, tests, records, support, constraints, and approval gates are version controlled.

## Evidence map

| Design criterion | Repository evidence | Status | Remaining work |
| --- | --- | --- | --- |
| Human onboarding | The README, `CONTRIBUTING.md`, `SECURITY.md`, and `project.json` state purpose, owner, contact, structure, setup, checks, and boundaries. | **Implemented** | Maintain as ownership changes. |
| Agent onboarding | `AGENTS.md` defines canonical artifacts, Goal → Instructions → Evaluation → Record, checks, action permissions, stop conditions, and human gates. | **Implemented** | Keep concise and synchronized. |
| Setup and reproduction commands | Exact Python and Node dependencies plus `scripts/reproduce.py` recreate the named Draft 2 PDF and audit report. | **Implemented** | Recheck on clean infrastructure in CI. |
| Data-access procedures | `data/README.md` states that no research or governed data are approved and enumerates required metadata and authority before that can change. | **Implemented for current scope** | Add dataset-specific records only after legitimate approval. |
| Tests and expected behavior | [Website tests](https://github.com/CU-ESIIL/FAIR-and-CARE-for-AGENTS/blob/main/tests/site.spec.ts), [manuscript tests](https://github.com/CU-ESIIL/FAIR-and-CARE-for-AGENTS/blob/main/tests/test_manuscript_audit.py), and the [CI workflow](https://github.com/CU-ESIIL/FAIR-and-CARE-for-AGENTS/blob/main/.github/workflows/ci.yml) make expected repository behavior executable. | **Implemented** | Add scientific and governance tests when those workflows exist. |
| Prompt and decision records | `PROMPT_LOG.md`, `DECISIONS.md`, the logging policy, task template, and structured run records separate request, decision, and provenance evidence. | **Implemented** | Apply minimization and redaction rules. |
| Constraints and approval gates | `governance/policy.json` classifies allowed, human-gated, rights-holder-gated, and prohibited actions; unknown actions are prohibited. | **Implemented** | Legitimate authority must approve any future governed-data policy. |
| Support or governance contacts | `project.json` names Ty Tuff and the issue tracker; sensitive reports follow `SECURITY.md`. | **Implemented for current scope** | Add rights-holder contacts only with authorization. |

## Verification

- **Current checks:** CI reconstructs the documented website and manuscript-audit environments on clean GitHub-hosted runners.
- **Target test:** Give a fresh agent no conversation history and ask it to reproduce a named result solely through the documented onboarding path.
- **Passing condition:** Every required fact is documented or explicitly classified as a credential, approval, or human decision.

[Return to all evidence maps](index.md)
