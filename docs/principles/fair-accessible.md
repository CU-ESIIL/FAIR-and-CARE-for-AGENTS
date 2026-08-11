---
title: "A — Accessible"
description: Evidence that authorized actors can obtain the project and the context needed to use it correctly.
---

# A — Accessible

**Agentic interpretation:** An authorized actor can obtain both research objects and the operational context needed to use them correctly; restricted access is explained rather than bypassed.

**Current assessment:** **Partial.** The manuscript, instructions, history, checks, and website are public and documented. This repository does not yet contain a reproducible scientific result, data-access procedure, named support contact, or project-specific approval workflow.

## Evidence map

| Design criterion | Repository evidence | Status | Remaining work |
| --- | --- | --- | --- |
| Human onboarding | The [README](https://github.com/CU-ESIIL/FAIR-and-CARE-for-AGENTS/blob/main/README.md) states purpose, authority, structure, setup, checks, and boundaries. | **Implemented** | Add author/contact and contribution routes. |
| Agent onboarding | [AGENTS.md](https://github.com/CU-ESIIL/FAIR-and-CARE-for-AGENTS/blob/main/AGENTS.md) defines repository workflow, documentation, testing, data-use, sovereignty, and design rules. | **Implemented** | Add project-specific action and approval boundaries as consequential workflows develop. |
| Setup and reproduction commands | The README documents website and audit commands; [requirements.txt](https://github.com/CU-ESIIL/FAIR-and-CARE-for-AGENTS/blob/main/requirements.txt) and [package-lock.json](https://github.com/CU-ESIIL/FAIR-and-CARE-for-AGENTS/blob/main/package-lock.json) describe dependencies. | **Partial** | Document one command that reproduces a named scientific result, not only repository checks. |
| Data-access procedures | The README explicitly states that no research data are included; AGENTS.md requires sources, access, format, license, and citation to be documented when data are introduced. | **Not applicable yet** | Add `data/README.md`, access conditions, contacts, and authorization steps before introducing data. |
| Tests and expected behavior | [Website tests](https://github.com/CU-ESIIL/FAIR-and-CARE-for-AGENTS/blob/main/tests/site.spec.ts), [manuscript tests](https://github.com/CU-ESIIL/FAIR-and-CARE-for-AGENTS/blob/main/tests/test_manuscript_audit.py), and the [CI workflow](https://github.com/CU-ESIIL/FAIR-and-CARE-for-AGENTS/blob/main/.github/workflows/ci.yml) make expected repository behavior executable. | **Implemented** | Add scientific and governance tests when those workflows exist. |
| Prompt and decision records | [PROMPT_LOG.md](https://github.com/CU-ESIIL/FAIR-and-CARE-for-AGENTS/blob/main/PROMPT_LOG.md) records user prompts verbatim and summarizes resulting work; AGENTS.md requires ongoing updates. | **Partial** | Add a retention/redaction policy and a separate decision log for structural or scientific decisions. |
| Constraints and approval gates | AGENTS.md prohibits silent external-data ingestion and requires uncertainty about rights to be documented. | **Partial** | Define who can approve publication, external transfers, governed-data use, and consequential scientific changes. |
| Support or governance contacts | No named support contact or governance authority is currently declared. | **Gap** | Add maintainers and, where applicable, rights-holder or governance contact routes. |

## Verification

- **Current checks:** CI reconstructs the documented website and manuscript-audit environments on clean GitHub-hosted runners.
- **Target test:** Give a fresh agent no conversation history and ask it to reproduce a named result solely through the documented onboarding path.
- **Passing condition:** Every required fact is documented or explicitly classified as a credential, approval, or human decision.

[Return to all evidence maps](index.md)
