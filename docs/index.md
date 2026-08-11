---
title: Designing FAIR and CARE into Agentic Science
description: A scientific perspective on designing agentic workflows that strengthen responsible, reproducible environmental science.
hide:
  - navigation
  - toc
---

<div class="project-hero" markdown>

<div class="project-hero__brand">
  <span>A working scientific perspective from</span>
  <a href="https://esiil.org/" aria-label="Visit ESIIL">
    <img src="assets/brand/esiil-wordmark.png" alt="ESIIL" />
  </a>
</div>

# FAIR + CARE for Agentic Science

**FAIR and CARE help people do better science. Agents need those practices designed into their workflows.**

An agent's ability to read a repository, write code, or generate plausible results does not ensure that it will find the authoritative inputs, preserve provenance, respect governance, or stop for human judgment. Agentic workflows must carry those requirements explicitly.

<div class="project-actions">
  <a class="md-button md-button--primary" href="https://github.com/CU-ESIIL/FAIR-and-CARE-for-AGENTS/blob/main/manuscript/fair_care_agentic_science_v2.md">Read the working manuscript</a>
  <a class="md-button" href="https://github.com/CU-ESIIL/FAIR-and-CARE-for-AGENTS">Explore the repository</a>
</div>

</div>

## Better science comes first

FAIR makes scientific objects findable, accessible, interoperable, and reusable. CARE keeps collective benefit, authority to control, responsibility, and ethics in view. These are foundations for better science with or without AI.

Human collaborators often bridge weak infrastructure with memory, conversation, and unwritten laboratory conventions. An agent cannot safely be assumed to recover that context or inherit the scientific judgment and legitimate authority behind it. The workflow must make the applicable context, evidence, boundaries, and review gates explicit before an agent acts.

<div class="principle-path" role="list" aria-label="FAIR and CARE scientific workflow">
  <span role="listitem">Find</span>
  <span role="listitem">Understand</span>
  <span role="listitem">Execute</span>
  <span role="listitem">Evaluate</span>
  <span role="listitem">Modify</span>
  <span role="listitem">Reproduce</span>
  <span role="listitem">Govern</span>
</div>

## Design the test before delegating the work

Agent-ready science begins by stating what success means, what actions are allowed, and what evidence must be preserved.

<div class="workflow" role="list" aria-label="Test-first scientific workflow">
  <span role="listitem"><strong>Goal</strong><small>Define the scientific objective.</small></span>
  <span role="listitem"><strong>Instructions</strong><small>State methods and boundaries.</small></span>
  <span role="listitem"><strong>Test</strong><small>Specify scientific, computational, provenance, and governance evidence.</small></span>
  <span role="listitem"><strong>Record</strong><small>Preserve inputs, actions, outputs, evaluation, and human review.</small></span>
</div>

## From principles to operational questions

<div class="principle-grid" markdown>

<div class="principle-card principle-card--fair" markdown>

### FAIR

**Can an independent actor correctly use this science?**

Make projects findable, accessible, interoperable, and reusable through clear discovery, durable artifacts, executable environments, and reproducible results.

</div>

<div class="principle-card principle-card--care" markdown>

### CARE

**Should this actor be allowed to use it in this way?**

Make collective benefit, authority to control, responsibility, and ethics part of the operational design—not an appendix added after deployment.

</div>

<div class="principle-card principle-card--test" markdown>

### Test-first design

**How will we know whether both conditions are satisfied?**

Translate claims into inspectable evidence, runnable checks where appropriate, and explicit human or community decisions where judgment is essential.

</div>

</div>

This repository now applies the paper's rules to itself through a named reproduction command, machine-readable action policy, approved-compute boundary, accountable owner, provenance records, harm cases, and negative tests. [See the repository implementation](implementation.md) or [review each FAIR + CARE evidence map](principles/index.md).

The current manuscript also has a version-controlled [Ecology author-guidelines and submission-readiness checklist](ecology-author-guidelines.md). Its derived Ecology PDF is a review-layout proof; editorial invitation, author declarations, a finished figure, and an allowed Word or genuine LaTeX submission package remain required.

## What this repository contains

This repository is the editable working home for the Perspective. It includes the manuscript and citation record, project website, operating instructions for agents, machine-readable project and governance records, a reproducible primary-output workflow, provenance templates, negative tests, and a public prompt log.

!!! note "Current status"
    The current manuscript is a concise second draft organized around eight practical FAIR + CARE repository rules. Operational repository controls are implemented and tested for this public, manuscript-only scope. A license, archival release/DOI, and required external scholarly and Indigenous data sovereignty reviews remain explicit human release blockers.
