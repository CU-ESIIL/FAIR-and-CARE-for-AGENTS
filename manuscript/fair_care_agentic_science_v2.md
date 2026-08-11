# FAIR and CARE in the Age of Agents: Design Criteria for Agent-Ready Environmental Science

**Manuscript type:** Perspective / Commentary  
**Status:** Second Draft  
**Canonical source:** This Markdown file  
**Intended audience:** Ecologists, environmental scientists, environmental data scientists, and research software engineers

## Alternate titles

1. **The Agent-Ready Repository: FAIR and CARE Design for Environmental Science**
2. **Give the Agent the Repository: Eight Rules for Reproducible and Responsible Science**
3. **From Tacit Knowledge to Tested Infrastructure: FAIR and CARE for Scientific Agents**
4. **Can a New Agent Reproduce This Result? A Repository Design Test for Environmental Science**

## Abstract

Coding and AI agents are entering environmental science repositories built for collaborators who already know the project. Repositories often depend on tacit context: which workflow is canonical, which data version was used, what a valid result should look like, and which actions require permission. New agents lack this context, making them useful stress tests for repository design.

We use FAIR and CARE to define eight practical criteria for agent-ready environmental science. FAIR asks whether an independent actor can find, access, interpret, and reuse the scientific object. CARE asks whether a proposed use produces benefit, respects authority, remains accountable, and avoids unacceptable outcomes. We make these criteria evaluable through test-first scientific design: **Goal → Instructions → Test → Record**. Each principle becomes a memorable design rule, a repository implementation, and a simple test. These practices improve repositories for people as well as agents. The objective is not autonomous science. It is science whose intent, methods, evidence, provenance, and governance are explicit enough to inspect and challenge.

**Keywords:** agentic AI; FAIR; CARE; reproducibility; environmental science; research software; provenance; data governance

---

## 1. Environmental science repositories are becoming agent workspaces

Environmental scientists increasingly ask coding agents to inspect repositories, edit analyses, debug workflows, prepare figures, or draft documentation. These systems can read files, execute code, call services, and change version-controlled artifacts. Yet most scientific repositories were built for people who already possess substantial project knowledge.

A familiar collaborator knows that `analysis_final_v2.R` is obsolete despite its name. They remember that a sensor threshold changed after an instrument failure, that one spreadsheet was edited manually, that the current figure comes from a different branch, or that culturally governed observations cannot be sent to an external model. This information may live in memory, messages, laboratory convention, or a conversation with the original analyst. It lets experienced people compensate for an underspecified repository.

An agent behaves more like a context-free collaborator. Give it a project URL with no previous conversation and ask: **Can it determine what the project is, how it works, what it should do, whether it succeeded, and what it is allowed to do?** Every undocumented human intervention identifies either information that should become explicit or a decision that should intentionally remain under human authority.

This is the practical opportunity. Designing repositories for agents makes them better scientific repositories because it forces scientific intent, methods, evaluation, provenance, and governance to become explicit rather than tacit. The same improvements help a new graduate student, a reviewer, a future maintainer, or a collaborator outside the original laboratory.

FAIR already makes machine actionability central to scientific data stewardship (Wilkinson et al., 2016). CARE complements object-centered stewardship with Collective Benefit, Authority to Control, Responsibility, and Ethics in the context of Indigenous Data Governance (Carroll et al., 2020). Agents do not replace these principles. They change how directly repositories can implement and test them. FAIR asks whether an independent actor can use the science correctly. CARE asks whether that actor should use it in that way. Test-first design asks how either claim will be evaluated.

Agent success does not prove that a scientific result is valid, and agent readiness does not imply that every task should be automated. The narrower proposition is useful enough: a bounded agent task can expose where a repository depends on missing context, fragile infrastructure, absent evaluation, or unstated authority.

## 2. Test first

The operating rule is simple:

> **Define the task and the test before asking the agent to do the work.**

We call this test-first scientific design. Before delegating consequential work, specify four elements:

1. **Goal** — What exactly should be accomplished, and what scientific claim or decision may the work support?
2. **Instructions** — Which data, methods, tools, degrees of freedom, and constraints apply? When must the agent stop or ask for review?
3. **Test** — What observable evidence distinguishes success, failure, and appropriate refusal?
4. **Record** — What inputs, code, environment, model, instructions, actions, outputs, evaluations, and approvals must be preserved?

The compact sequence is:

> **GOAL → INSTRUCTIONS → TEST → RECORD**

A useful test has four dimensions. A **scientific** test asks whether the result addresses the question and meets domain expectations: for example, whether a model preserves mass balance or a reported confidence interval is reproduced. A **computational** test asks whether the environment builds, inputs validate, and the workflow completes. A **provenance** test asks whether another person can reconstruct what happened. A **governance** test asks whether the workflow was authorized to use those data, models, services, and publication channels.

Passing only three dimensions can still be failure. A scientifically correct result obtained through prohibited data use fails. A perfectly governed and reproducible hallucination fails. A correct result whose provenance cannot be reconstructed also fails this standard. Conversely, refusal can be the correct result of a governance test.

Consider an agent asked to flag suspect observations in a sensor network. The goal names the affected data product. The instructions identify the quality-control rules, authorized inputs, and operations the agent may propose but not publish. The test includes a labeled fixture, expected flag rates, and review of false positives. The record links the input version, code change, agent instructions, output, evaluation, and approving scientist. This specification is useful even if a person ultimately performs the analysis.

Tests need not all be software assertions. Some run automatically; others produce a review packet or block work pending an identified expert, data steward, or governance authority. What matters is that success and prohibited action are specified before an agent's plausible-looking output is available to influence the standard.

## 3. FAIR repository design for agents

FAIR describes properties of research objects and their stewardship, not a synonym for unrestricted openness. For an agent-ready repository, each principle can become a concrete design rule and a test.

### F — Give every repository a front door

**Design rule: Give every repository a front door.** Use the pattern **one repository → one associated website**. The repository is the versioned scientific object; the website is its discovery and communication layer.

The landing page should state the scientific question and project scope before presenting a directory tree. It should identify the responsible people or organization, summarize data and methods, name major outputs, and link to the repository, manuscript or publications, preferred citation, and persistent identifiers. Descriptive titles, stable URLs, meaningful headings, ordinary search optimization, and machine-readable metadata help humans and tools orient themselves. The website should not duplicate every artifact. It should explain how distributed artifacts relate and which source is authoritative for each purpose. [CITATION NEEDED: machine-actionable environmental repository metadata]

**Test:** Give a clean agent only the public project URL. Can it correctly identify the question, data, methods, outputs, repository, responsible people, version, and citation without unsupported guesses?

### A — Give every agent an orientation

**Design rule: Give every agent an orientation.** Place an `AGENTS.md` at the repository root. It should explain what the project is, how the repository is organized, which workflows and outputs are canonical, how to run and test them, what constraints apply, what actions are prohibited, and when human approval is required.

Keep the file concise and link to detailed methods or governance documents rather than duplicating them. Preserve consequential prompts, decisions, or agent instructions when they materially affect methods, selection, interpretation, or dissemination. This is not an argument to log every chat: records may contain sensitive information and need deliberate scope, access, retention, and redaction. The governing rule is broader: **No scientifically necessary instruction should exist only in the memory of a person or an AI conversation.**

**Test:** Start a fresh agent with no previous conversation and ask it to perform a defined repository task. Record every additional fact a human must provide. Is that fact a documentation gap, a credential, a deliberate review gate, or a capability limitation?

### I — Make scientific products portable

**Design rule: Make scientific products portable.** Agents should produce durable, editable artifacts rather than leave scientific products trapped in chat histories or proprietary interfaces. Appropriate formats may include Markdown, Python, R, YAML, JSON, CSV, Parquet, NetCDF, Zarr, GeoTIFF, and editable figure source. The choice should preserve scientific meaning through explicit schemas, units, coordinate systems, missing-value conventions, identifiers, and relationships.

Use a predictable directory structure that separates data references, reusable source, analyses, tests, prompts, results, documentation, and environments. Keep figures connected to editable source and source data; keep numerical results in machine-readable form, not only prose. FAIR principles for research software similarly emphasize identification, access to software and metadata, qualified references, and reuse conditions (Barker et al., 2022).

> **The model should be disposable; the science should persist.**

**Test:** Move an artifact created with one agent or model to another agent and to a conventional computational environment. Can each understand, modify, execute, and reproduce it without proprietary conversion?

### R — Make the project executable elsewhere

**Design rule: Make the project executable elsewhere.** A reusable project combines version control, tagged versions, licenses, tests, a documented reproduction command, and a container or reproducible environment specification with important dependencies pinned. Data and models do not all belong in Git. The repository should point unambiguously to the immutable or versioned inputs used, including identifiers, checksums, access procedures, licenses, and governance conditions.

Research compendia, dynamic documents, containers, and established reproducible-computing practices already connect narrative, code, inputs, environments, and repeatable results (Gentleman & Lang, 2007; Peng, 2011; Sandve et al., 2013; Boettiger, 2015). Agent-assisted work adds a need to identify consequential models or services and to preserve sufficient instructions and evaluation evidence. Interoperable provenance concepts such as entities, activities, agents, and their relationships can support that record (World Wide Web Consortium, 2013).

**Test:** Clone a tagged repository onto clean infrastructure, obtain the authorized input versions, and run one documented command. Can it reproduce a specified figure, table, statistic, or result within declared scientific tolerances?

## 4. CARE governance for agents

CARE originated in Indigenous Data Governance and cannot be reduced to a generic technical checklist. The criteria below describe ways repository and computational infrastructure can make established governance decisions operational. They do not create legitimate authority. Projects working with Indigenous data should follow the decisions and protocols of the relevant rights-holders and governance bodies, including when those decisions limit what becomes explicit or machine accessible. [CITATION NEEDED: nation- and community-specific governance protocols]

### C — State who benefits

**Design rule: State who benefits.** Before deploying an agentic workflow, identify its intended beneficiary, intended scientific or community benefit, expected useful output, and important burdens or risks. “Scientific progress” is too general when a workflow affects specific communities, contributors, field teams, or ecosystems.

A system that accelerates publication while increasing demands on data contributors may shift costs rather than create collective benefit. Benefit cannot be self-certified by a repository maintainer on behalf of a community. The record should identify who defined the benefit, how affected parties can evaluate it, and whether not automating is a legitimate outcome.

**Test:** Can the project state who should benefit, what observable outcome would constitute benefit, who will evaluate it, and what burdens must also be assessed?

### A — Make authority explicit

**Design rule: Make authority explicit.** Data access is not blanket permission. Where relevant, distinguish authority to **read, copy, analyze, perform inference, train, fine-tune, combine, publish, and redistribute**. Associate governed data classes with allowed purposes, prohibited actions, required reviewers, retention limits, disclosure rules, and approved computational infrastructure.

Agentic workflows add a consequential question to data provenance. We routinely record where our data came from. Agentic science also requires knowing: **Where did the data go?**

Governance requires knowing where computation occurs and which models and services receive the data. For sensitive ecological or community-governed data, record the compute location, identified model or service, model version when available, inference endpoint, provider retention and training behavior, network access, logs, and jurisdictional or institutional control. External transfer may require an approved enclave, institutional endpoint, community-approved compute, or local or self-hosted inference. Self-hosting does not itself establish legitimate use. It creates a computational boundary within which legitimate governance decisions can be enforced.

Technical policy should derive from legitimate governance and remain revisable by those with authority. Human approval should gate actions that cross data, institutional, publication, or community boundaries.

**Test:** Attempt a prohibited data movement or model use: for example, send restricted locations to an unapproved endpoint or use analysis-only data for training. Does the workflow prevent the action, explain the boundary, record the attempt, and escalate ambiguity to the correct authority?

### R — Name the responsible human

**Design rule: Name the responsible human.** Every consequential agent workflow should have an identifiable human owner. The owner defines its authority, ensures that its tests remain relevant, validates important outputs, and decides whether evidence supports a scientific claim. Review is not meaningful if the reviewer cannot inspect the evidence or understand the evaluation.

For important outputs, preserve enough information to reconstruct the model or service, version when available, instructions, data, code, tools, environment, output, evaluation, and human review or authorization. Version control supports correction, but projects also need a route for reporting problems and withdrawing or amending consequential outputs.

> **Agents may receive autonomy, but responsibility cannot be delegated to them.**

**Test:** Select an important result. Can we determine who authorized the workflow and reconstruct how the result was produced, tested, reviewed, and released?

### E — Test what must not happen

**Design rule: Test what must not happen.** Do not leave ethics as a retrospective discussion. Before deployment ask: **What is the worst scientifically plausible thing this agent could do?**

For an environmental workflow, unacceptable outcomes might include disclosing a sensitive species location, fabricating literature support, publishing an unreviewed result, sending governed data to an unauthorized model, or presenting a fragile forecast as a high-consequence recommendation. Turn the most important cases into explicit prevention, detection, refusal, escalation, and recovery tests. Define affected parties and accountable owners, and include relevant scientific experts and rights-holders when designing and evaluating the cases.

**Test:** Deliberately attempt representative prohibited or harmful actions. Does the system refuse, detect, stop, or escalate appropriately—and can responsible people investigate and recover when a control fails?

### Table 1. FAIR + CARE design and test matrix

| Principle | Design rule | What to implement | Test |
|---|---|---|---|
| **F — Findable** | Give every repository a front door. | One repository linked to one searchable website; question, people, data, methods, outputs, citation, and identifiers. | Give a clean agent only the project URL; score what it identifies correctly. |
| **A — Accessible** | Give every agent an orientation. | `README.md`, `AGENTS.md`, canonical workflows, commands, tests, constraints, prohibitions, and approval gates. | Start a fresh agent on a defined task; record every undocumented fact it needs. |
| **I — Interoperable** | Make scientific products portable. | Durable editable formats; schemas, units, identifiers, relationships, predictable structure, and source for outputs. | Move an artifact across agents and a conventional environment; modify and reproduce it. |
| **R — Reusable** | Make the project executable elsewhere. | Versioning, release, license, environment, pinned dependencies, input references, tests, provenance, and reproduction command. | Clone a tagged version on clean infrastructure and reproduce one named result. |
| **C — Collective Benefit** | State who benefits. | Beneficiary, purpose, expected output, benefit measure, burdens, evaluator, and option not to automate. | State the observable benefit and determine with affected parties whether it occurred. |
| **A — Authority to Control** | Make authority explicit. | Action-level permissions, approved compute and models, retention, network boundaries, review gates, and governance links. | Attempt prohibited movement or model use; verify prevention and escalation. |
| **R — Responsibility** | Name the responsible human. | Workflow owner, run provenance, substantive review, authorization, disclosure, correction, and incident response. | Reconstruct an important result and identify who authorized and reviewed it. |
| **E — Ethics** | Test what must not happen. | Harm cases, affected parties, bias and disclosure checks, refusal rules, red-team tests, escalation, and recovery. | Attempt representative harmful actions; verify refusal, detection, response, and review. |

## 5. An agent-ready environmental science repository

An ordinary laboratory can implement these criteria incrementally. The following architecture is illustrative, not mandatory:

```text
my-environmental-project/
|-- README.md              # question, scope, people, outputs, citation
|-- AGENTS.md              # orientation, workflows, constraints, approvals
|-- environment/           # reproducible environment and dependency records
|-- data/
|   `-- README.md          # sources, versions, access, licenses, governance
|-- src/                   # reusable analysis code
|-- analysis/              # declared workflows and editable analyses
|-- tests/
|   |-- scientific/        # domain expectations and result checks
|   |-- computational/     # setup, schema, smoke, and regression checks
|   `-- governance/        # prohibited actions and required escalation
|-- prompts/               # consequential task specifications or references
|-- provenance/            # run records: inputs, models, tools, reviews
|-- results/               # machine-readable outputs and editable figures
|-- manuscript/            # editable scientific narrative
`-- docs/                  # searchable associated website
```

The directories matter less than the functions they expose: scientific purpose, agent orientation, editable source, a reproducible environment, scientific and computational tests, governance boundaries, consequential instructions, provenance, outputs, and a public front door. A smaller project can begin with four changes:

1. Add a useful `README.md` and `AGENTS.md` that identify the project, canonical workflow, important result, and action boundaries.
2. Pin the important environment and data versions, then document one command that reproduces one result.
3. Add one scientific expectation and one governance boundary test.
4. Publish a landing page that connects the question, people, repository, data, outputs, and citation.

The first target should be bounded: “From a clean clone, reproduce Figure 1 using the declared environment and authorized test data; check the expected statistics; do not call unapproved network services; write a provenance record; and stop for review before changing a public artifact.” A laboratory will learn more from making one workflow reliable and governable than from labeling an entire repository “AI ready.”

### Figure 1 concept: Anatomy of a FAIR + CARE agent-ready environmental science repository

Show the repository at the center as a versioned scientific object. Associate its website, metadata, `README.md`, `AGENTS.md`, editable formats, environment, input identifiers, tests, and reproduction command with FAIR. Associate its benefit statement, action-level permissions, approved compute and model boundaries, human owners, governance tests, and review gates with CARE. Connect both groups to the central sequence **Goal → Instructions → Test → Record**. The image should make clear that the same infrastructure supports human and agent collaborators.

**Figure 1 caption.** An agent-ready repository makes scientific purpose, workflows, evaluation, provenance, and authority inspectable. FAIR components help an independent actor find and correctly use the scientific object. CARE components constrain whether a proposed use is legitimate and accountable. Test-first design connects both sets of principles to observable evidence and explicit human or community decisions. The layout is illustrative rather than a required directory standard.

## 6. Conclusion

Environmental scientists do not need to redesign every project for autonomous research. They need repositories that make bounded delegation understandable, testable, reproducible, and legitimate. A context-free agent provides a direct diagnostic: give it the project or repository URL, a defined task, and no prior conversation. The assistance it requests reveals missing context; the actions it refuses can reveal functioning governance.

The practical program is compact. Define **Goal → Instructions → Test → Record** before consequential work. Give the repository a front door and the agent an orientation. Require portable products and an executable project. State who benefits, make authority explicit, name the responsible human, and test what must not happen. Implement these practices first for one important result and one important boundary.

FAIR asks whether an independent actor can correctly use the science. CARE asks whether that use is legitimate and accountable. Test-first design makes both questions operational without pretending that code can replace scientific judgment or community authority. The aim is not to make science easier for AI. It is to use agents to reveal whether a scientific repository is explicit enough for people and machines to understand, reproduce, evaluate, and govern.

## Citation integrity

Citation vetting for this second draft is recorded in `manuscript/citation_audit_v2.json`. The registry identifies each source, records the claim it supports, and fingerprints every cited paragraph after review. Automated checks confirm bibliographic identity and detect changes that require renewed claim-level review. They do not replace expert reading, Indigenous governance, or community authority.

## References

- Barker, M., Chue Hong, N. P., Katz, D. S., Lamprecht, A.-L., Martinez-Ortiz, C., Psomopoulos, F., Harrow, J., Castro, L. J., Gruenpeter, M., Martinez, P. A., & Honeyman, T. (2022). Introducing the FAIR Principles for research software. *Scientific Data, 9*, 622. https://doi.org/10.1038/s41597-022-01710-x
- Boettiger, C. (2015). An introduction to Docker for reproducible research. *ACM SIGOPS Operating Systems Review, 49*(1), 71–79. https://doi.org/10.1145/2723872.2723882
- Carroll, S. R., Garba, I., Figueroa-Rodríguez, O. L., Holbrook, J., Lovett, R., Materechera, S., Parsons, M., Raseroka, K., Rodriguez-Lonebear, D., Rowe, R., Sara, R., Walker, J. D., Anderson, J., & Hudson, M. (2020). The CARE Principles for Indigenous Data Governance. *Data Science Journal, 19*, 43. https://doi.org/10.5334/dsj-2020-043
- Gentleman, R., & Lang, D. T. (2007). Statistical analyses and reproducible research. *Journal of Computational and Graphical Statistics, 16*(1), 1–23. https://doi.org/10.1198/106186007X178663
- Peng, R. D. (2011). Reproducible research in computational science. *Science, 334*(6060), 1226–1227. https://doi.org/10.1126/science.1213847
- Sandve, G. K., Nekrutenko, A., Taylor, J., & Hovig, E. (2013). Ten simple rules for reproducible computational research. *PLOS Computational Biology, 9*(10), e1003285. https://doi.org/10.1371/journal.pcbi.1003285
- Wilkinson, M. D., Dumontier, M., Aalbersberg, I. J., et al. (2016). The FAIR Guiding Principles for scientific data management and stewardship. *Scientific Data, 3*, 160018. https://doi.org/10.1038/sdata.2016.18
- World Wide Web Consortium. (2013). *PROV-O: The PROV Ontology. W3C Recommendation 30 April 2013.* https://www.w3.org/TR/prov-o/
