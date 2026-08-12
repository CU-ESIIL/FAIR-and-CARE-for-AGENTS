# FAIR and CARE in the Age of Agents: Design Criteria for Agent-Ready Environmental Science

**Manuscript type:** Perspective / Commentary  
**Status:** Second Draft  
**Canonical source:** This Markdown file  
**Intended audience:** Ecologists, environmental scientists, environmental data scientists, and research software engineers

## Alternate titles

1. **The Agent-Ready Repository: FAIR and CARE Design for Environmental Science**
2. **Give the Agent the Repository: Eight Rules for Reproducible and Responsible Science**
3. **From Tacit Knowledge to Tested Infrastructure: FAIR and CARE for Scientific Agents**
4. **Designing FAIR and CARE into Agentic Environmental Science Workflows**

## Abstract

FAIR and CARE are not accommodations for AI. They are foundations for better science: research objects should be findable, accessible, interoperable, and reusable, while their use should advance collective benefit, respect authority, assign responsibility, and avoid harm. CARE was developed by Indigenous Data Governance leaders to advance Indigenous rights, interests, and self-determination. We do not redefine that framework as generic. Instead, we propose four CARE-informed questions as a minimum entry point for every scientific workflow: Who benefits and bears burdens? Who has legitimate authority? Who is accountable? What harms must be prevented? These questions do not constitute CARE compliance or replace the full principles and their continuing Indigenous purpose.

Coding and AI agents make this baseline urgent because they cannot be assumed to recover tacit scientific commitments. Their ability to generate plausible code or prose does not ensure that they will select authoritative inputs, preserve provenance, respect authority, or stop when judgment and permission are required. We translate FAIR and the four CARE-informed questions into eight operational repository criteria and make them evaluable through **Goal → Instructions → Test → Record**. Each criterion pairs a design rule with repository evidence, a test, and an accountable human, institutional, or community decision where automation is illegitimate. The objective is to make the practices that support understandable, reproducible, accountable, and trustworthy environmental science inspectable and enforceable before a person or agent acts.

**Keywords:** agentic AI; FAIR; CARE; reproducibility; environmental science; research software; provenance; data governance

---

## 1. Better science requires designed-in FAIR and CARE

Environmental science is stronger when a project's purpose, evidence, methods, provenance, reuse conditions, responsibilities, and limits are explicit. Those qualities help collaborators assess claims, help reviewers trace evidence, help future researchers reproduce results, and help affected people understand or contest how data and scientific products are used. FAIR and CARE matter because they make these qualities part of scientific practice rather than optional documentation.

Environmental scientists increasingly ask coding agents to inspect repositories, edit analyses, debug workflows, prepare figures, or draft documentation. These systems can read files, execute code, call services, and change version-controlled artifacts. Yet most scientific repositories were built for people who already possess substantial project knowledge. Agents can move quickly across files, tools, services, and publication surfaces, so missing context or authority can become consequential before informal human safeguards intervene. [CITATION NEEDED: empirical evidence on coding-agent reliability, tool use, provenance, and boundary following]

A familiar collaborator knows that `analysis_final_v2.R` is obsolete despite its name. They remember that a sensor threshold changed after an instrument failure, that one spreadsheet was edited manually, that the current figure comes from a different branch, or that culturally governed observations cannot be sent to an external model. This information may live in memory, messages, laboratory convention, or a conversation with the original analyst. It lets experienced people compensate for an underspecified repository.

An agent does not inherit this working knowledge, scientific judgment, or authority merely by gaining access to the repository. Give it a project URL with no previous conversation and ask: **Can it determine what the project is, how it works, what it should do, whether it succeeded, and what it is allowed to do?** Without a designed workflow, plausible action can mask the use of an obsolete file, an invalid method, an incomplete record, or an illegitimate data use.

The central design problem is therefore not how to make science easier for agents. It is how to prevent agentic work from bypassing the practices that make science reliable and legitimate. The workflow must carry scientific intent, authoritative inputs, methods, evaluation, provenance, permissions, and review gates forward into the agent's work. Building that infrastructure first improves science for people; it then gives agents an explicit scaffold within which they can contribute.

FAIR makes machine actionability central to scientific data stewardship (Wilkinson et al., 2016). CARE was developed specifically for Indigenous Data Governance to bring Collective Benefit, Authority to Control, Responsibility, and Ethics—and therefore people, purpose, power, and rights—into data stewardship (Carroll et al., 2020). That origin and continuing purpose must remain visible. Our extension is a normative and contestable proposal for scientific practice: every workflow should answer four CARE-informed questions, but those questions neither restate the full principles nor authorize a project to assess CARE on behalf of Indigenous Peoples. Where Indigenous Peoples, their lands, waters, knowledge, observations, samples, cultural expressions, or derived information may be involved, the relevant Indigenous authorities determine whether and how a workflow proceeds. FAIR asks whether research objects and their metadata can be found, accessed under stated conditions, combined, and reused. Scientific tests ask whether a particular use is correct; CARE and other governance processes determine whether it is legitimate. Test-first design makes the resulting expectations inspectable.

Agent success does not prove that a scientific result is valid, and agent readiness does not imply that every task should be automated. Failed or refused tasks can still diagnose missing context, fragile infrastructure, absent evaluation, or functioning governance, but that diagnostic is a secondary benefit. The primary purpose is to design FAIR and CARE into the workflow before an agent acts.

## 2. Design the workflow before delegating the work

Telling an agent to be reproducible, responsible, or FAIR and CARE compliant is not an adequate control. The workflow itself must identify authoritative inputs, constrain permissible actions, define acceptable evidence, preserve provenance, and route consequential judgments to the people or communities with legitimate authority.

Here, an **agent** is a computational system that can pursue a delegated goal through tools or external actions; a **workflow** is the linked set of people, data, software, services, and decisions through which work is performed; and **consequential work** can support a scientific claim, affect people or ecosystems, use governed data, cross an institutional or service boundary, change evaluation criteria, train a model, publish an artifact, or take an irreversible action. Technical access is not legitimate authority, and an operational owner is not necessarily the governing authority.

The operating rule is simple:

> **Define the task and the test before asking the agent to do the work.**

We call this test-first scientific design. Before delegating consequential work, specify four elements:

1. **Goal** — What exactly should be accomplished, what claim or decision may it support, who should benefit, who may bear burdens, and who defined those expectations?
2. **Instructions** — Which data, methods, tools, degrees of freedom, and constraints apply? What is the basis and scope of authority? Which actions are prohibited, and where must work stop for review?
3. **Test** — What evidence distinguishes success, scientific or computational failure, a declared governance refusal, and a need for authorized review? Which benefit indicators, harm cases, boundaries, and stop conditions apply?
4. **Record** — What minimized and appropriately protected provenance is required? Who was operationally accountable, who held governing and release authority, what review occurred, and how can the output be corrected or withdrawn?

The compact sequence is:

> **GOAL → INSTRUCTIONS → TEST → RECORD**

A useful test has four dimensions. A **scientific** test asks whether the result addresses the question and meets domain expectations: for example, whether a model preserves mass balance or a reported confidence interval is reproduced. A **computational** test asks whether the environment builds, inputs validate, and the workflow completes. A **provenance** test asks whether another person can reconstruct what happened. A **governance** test asks whether the workflow was authorized to use those data, models, services, and publication channels.

Passing only three dimensions can still be failure. A scientifically correct result obtained through prohibited data use fails. A perfectly governed and reproducible hallucination fails. A correct result whose provenance cannot be reconstructed also fails this standard. A refusal passes only when it matches a declared boundary; inability, misunderstanding, and unpredictable failure must be recorded differently.

Consider an agent asked to flag suspect observations in a sensor network. The goal names the affected data product. The instructions identify the quality-control rules, authorized inputs, and operations the agent may propose but not publish. The test includes a labeled fixture, expected flag rates, and review of false positives. The record links the input version, code change, agent instructions, output, evaluation, and approving scientist. This specification is useful even if a person ultimately performs the analysis.

Tests need not all be software assertions. Some run automatically; others produce a review packet or block work pending an identified expert, data steward, or governance authority. Every workflow receives a lightweight screen for benefit, authority, accountability, and foreseeable harm. Consequential work receives the full specification and record. What matters is that success, refusal, review, and prohibited action are specified before an agent's plausible-looking output is available to influence the standard.

## 3. FAIR repository design for agents

FAIR describes properties of research objects and their stewardship, not a synonym for unrestricted openness. The rules below are operational interpretations for agent-ready repositories, not a FAIR certification or complete restatement of the principles.

### F — Give every project an authoritative front door

**Design rule: Give every project an authoritative front door.** A searchable project page or repository landing page should identify the canonical repositories and artifacts and explain how they relate. The version-controlled repository remains the source of truth; the website or landing page is its discovery and communication layer.

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

## 4. A CARE-informed governance floor for every workflow

CARE was created in Indigenous Data Governance to advance Indigenous rights, interests, innovation, and self-determination amid histories and continuing conditions of data extraction and unequal power. The full principles are relational and substantive; the four questions used here are an operational entry point, not a restatement, replacement, certification, or endorsed expansion of CARE. Applying them beyond that original context carries obligations of attribution, reciprocity, non-displacement, and continued specificity. Publication of this proposal requires review by Indigenous Data Governance scholars or appropriate Indigenous governance authorities; simulated agent review cannot provide endorsement. [CITATION NEEDED: Indigenous-led scholarship and nation- or community-specific governance protocols]

At the same time, no scientific workflow is exempt from questions of benefit, authority, responsibility, and ethics. Every project distributes benefits and burdens. Every use of data, code, infrastructure, labor, and knowledge occurs under some claimed authority—or reveals that legitimate authority is missing. Every consequential output needs accountable people or institutions. Every workflow can create foreseeable harm. We therefore propose four **CARE-informed questions as a universal governance floor**: before work begins, screen who benefits and bears burdens, who has legitimate authority, who is accountable, and what harms must be prevented.

The entry screen is universal; the obligations it reveals are contextual and proportional to consequence. A license, institutional role, or publication policy may establish some permissions in a low-risk public-data workflow, but none is interchangeable with legitimate authority. Higher-risk contexts may require consent, formal governance, funded participation, or collective decision-making that a repository owner cannot grant. Context-specific authority can constitute, reshape, supersede, or prohibit the proposed workflow rather than merely add controls to it. If authority is absent, contested, expired, or conflicting, the workflow stops and escalates.

### C — State who benefits

**Design rule: State who benefits and who bears burdens.** Before any consequential workflow, identify its intended beneficiaries, expected scientific or community benefit, distribution of benefits and burdens, and important risks. “Scientific progress” is too general when a workflow affects specific communities, contributors, field teams, future generations, or ecosystems.

A system that accelerates publication while increasing demands on data contributors may shift costs rather than create collective benefit. Benefit cannot be self-certified by a repository maintainer on behalf of a community. The record should identify who defined the benefit, what quantitative, qualitative, relational, or governance evidence will be considered, how affected parties or legitimate representatives can contest the assessment, and what remedy or stopping rule applies if benefits do not materialize.

**Test:** Can the project state who should benefit, who may bear costs or risks, what evidence or decision process will be used, who may judge and contest the result, and when the workflow must change or stop?

### A — Make authority explicit

**Design rule: Make authority explicit.** Every workflow should record the claimed source, holder, scope, legitimacy, duration, conflicts, and revocation conditions of its authority; data access is not blanket permission. Where relevant, distinguish authority to **read, copy, analyze, perform inference, train, fine-tune, combine, publish, and redistribute**. Associate governed data classes with allowed purposes, prohibited actions, required reviewers, retention limits, disclosure rules, and approved computational infrastructure. Reassess authority when purpose, recipient, model, endpoint, or publication channel changes.

Agentic workflows add a consequential question to data provenance. We routinely record where our data came from. Agentic science also requires knowing: **Where did the data go?**

Governance requires knowing where computation occurs and which models and services receive the data. For sensitive ecological or community-governed data, record the compute location, identified model or service, model version when available, inference endpoint, provider retention and training behavior, network access, logs, and jurisdictional or institutional control. External transfer may require an approved enclave, institutional endpoint, community-approved compute, or local or self-hosted inference. Self-hosting does not itself establish legitimate use. It creates a computational boundary within which legitimate governance decisions can be enforced.

Technical policy should derive from legitimate governance and remain revisable by those with authority. Human approval should gate actions that cross data, institutional, publication, or community boundaries.

**Test:** Using synthetic fixtures, mocks, or an isolated and pre-authorized environment, simulate a prohibited data movement or model use. Does the workflow prevent the action, explain the boundary, record the safe test, and escalate ambiguity to the correct authority? A governance test must never perform the harmful real-world action it is meant to prevent.

### R — Assign accountable people and institutions

**Design rule: Assign accountable people and institutions.** Every consequential workflow should have a named operational owner, whether or not an agent participates, while separately identifying scientific reviewers, responsible institutions, governing authorities, and release authority where applicable. The owner works within—not above—those authorities, ensures that tests remain relevant, validates important outputs, and routes decisions to the people or bodies entitled to make them. Review is not meaningful if reviewers cannot inspect the evidence or understand the evaluation.

For important outputs, preserve enough information to reconstruct the model or service, version when available, instructions, data, code, tools, environment, output, evaluation, and human review or authorization. Version control supports correction, but projects also need a route for reporting problems and withdrawing or amending consequential outputs.

> **Agents may receive autonomy, but human, institutional, and collective responsibilities cannot be delegated to them.**

**Test:** Select an important result. Can we distinguish and identify operational ownership, scientific review, governing authority, and release approval, then reconstruct how the result was produced, tested, reviewed, corrected, and released?

### E — Test what must not happen

**Design rule: Test what must not happen.** Do not leave ethics as a retrospective discussion. Before deployment ask: **What reasonably foreseeable scientific, cultural, political, social, spiritual, economic, labor, ecological, and intergenerational harms do affected people, rights-holders, domain experts, and responsible institutions identify?**

For an environmental workflow, unacceptable outcomes might include disclosing a sensitive species location, fabricating literature support, publishing an unreviewed result, sending governed data to an unauthorized model, displacing field or community expertise, or presenting a fragile forecast as a high-consequence recommendation. Turn the most important cases into safe prevention, detection, refusal, escalation, remedy, withdrawal, and recovery tests. Negative tests cannot establish ethical legitimacy; affected people, relevant scientific experts, rights-holders, and responsible institutions must help define and evaluate cases that concern them.

**Test:** Safely simulate representative prohibited or harmful actions without exposing real people, data, species, or systems. Does the workflow refuse, detect, stop, or escalate appropriately—and can responsible people investigate, remedy, withdraw, and recover when a control fails?

### Table 1. FAIR + CARE design and test matrix

| Principle | Design rule | What to implement | Test |
|---|---|---|---|
| **F — Findable** | Give every project an authoritative front door. | Searchable landing page relating canonical repositories; question, people, data, methods, outputs, citation, and identifiers. | Give a clean agent only the project URL; score expected fields and require uncertainty rather than guesses. |
| **A — Accessible** | Give every agent an orientation. | `README.md`, `AGENTS.md`, canonical workflows, commands, tests, constraints, prohibitions, and approval gates. | Start a fresh agent on a defined task; record every undocumented fact it needs. |
| **I — Interoperable** | Make scientific products portable. | Durable editable formats; schemas, units, identifiers, relationships, predictable structure, and source for outputs. | Move an artifact across agents and a conventional environment; modify and reproduce it. |
| **R — Reusable** | Make the project executable elsewhere. | Versioning, release, license, environment, pinned dependencies, input references, tests, provenance, and reproduction command. | Clone a tagged version on clean infrastructure and reproduce one named result. |
| **C — Collective Benefit** | State who benefits and who bears burdens. | Beneficiaries, benefit definition, distribution, burdens, evidence, evaluator, contestation, remedy, and option not to proceed. | Determine with affected parties or legitimate representatives whether the defined benefit occurred and burdens were acceptable. |
| **A — Authority to Control** | Establish and maintain legitimate authority. | Authority holder, scope, action-level permissions, approved compute and models, duration, conflicts, revocation, and review gates. | Safely simulate an action beyond declared authority; verify prevention and escalation. |
| **R — Responsibility** | Assign accountable people and institutions. | Operational owner, governing and release authority, scientific review, provenance, disclosure, correction, and incident response. | Reconstruct a result and distinguish who operated, governed, reviewed, authorized, and released it. |
| **E — Ethics** | Identify harms and test boundaries safely. | Participatory harm cases, affected parties, benefit and bias checks, refusal rules, safe red-team tests, remedy, escalation, and recovery. | Safely simulate representative harms; verify refusal, detection, remedy, response, and review. |

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

The first target should be bounded: “From a clean clone, reproduce Figure 1 using the declared environment and authorized test data; check the expected statistics; do not call unapproved network services; write a minimized provenance record; and stop for review before changing a public artifact.” A laboratory will learn more from making one workflow reliable and governable than from labeling an entire repository “AI ready.” Institutions can supply shared identity, secure compute, data stewardship, community-engagement, and incident-response services that a small laboratory cannot maintain alone; inability to establish the necessary authority or safeguards means the work does not proceed.

Consider a habitat assessment that combines public remote sensing, sensitive biodiversity observations, and knowledge or observations associated with an Indigenous People or local community. The goal identifies the intended conservation decision, beneficiaries, burdens, and who defined them. Instructions separate public from governed inputs, encode permitted inference and disclosure, and route unresolved authority to the relevant governing body. Tests evaluate habitat-model performance with authorized fixtures and safely verify that sensitive locations cannot leave the approved environment. The record distinguishes operational ownership, scientific review, governing authority, and release approval. FAIR-oriented infrastructure makes the products traceable and reusable under stated conditions; the CARE-informed screen exposes questions that can change the method, restrict the output, or stop the assessment. [CITATION NEEDED: ecological data governance, environmental justice, and sensitive-biodiversity examples]

### Figure 1 concept: Anatomy of a FAIR + CARE agent-ready environmental science repository

Show the repository at the center as a versioned scientific object. Associate its website, metadata, `README.md`, `AGENTS.md`, editable formats, environment, input identifiers, tests, and reproduction command with FAIR. Associate its benefit statement, action-level permissions, approved compute and model boundaries, human owners, governance tests, and review gates with CARE. Connect both groups to the central sequence **Goal → Instructions → Test → Record**. The image should make clear that the same infrastructure supports human and agent collaborators.

**Figure 1 caption.** A FAIR + CARE workflow makes scientific purpose, inputs, methods, evaluation, provenance, and authority inspectable. FAIR components make scientific objects usable and reusable under stated conditions. The manuscript's CARE-informed entry screen asks every workflow to address benefit, authority, responsibility, and ethics without replacing the full CARE Principles. Context-specific rights and protocols may constitute, reshape, supersede, or prohibit a workflow. Test-first design connects both sets of principles to observable evidence and explicit human, institutional, or community decisions. The same infrastructure improves science for people and constrains how agents participate. The layout is illustrative rather than a required directory standard.

## 6. Conclusion

FAIR and CARE are principles for better human science, not special accommodations for AI. CARE's continuing purpose is to advance Indigenous rights, interests, and self-determination in data governance. With attribution and without claiming equivalence or compliance, we propose that every scientific workflow begin with four CARE-informed questions about benefit, authority, accountability, and harm. The answers are not merely stronger controls layered onto a generic workflow: rights, relationships, risks, and legitimate authority may determine whether and how the workflow exists.

The practical program is compact. Apply a lightweight CARE-informed screen to every workflow, then design **Goal → Instructions → Test → Record** into consequential work. Give the project an authoritative front door and every agent an orientation. Require portable products and an executable project. State who benefits and bears burdens, make legitimate authority explicit, assign accountable people and institutions, and identify harms before testing boundaries safely. Implement these practices first for one important result and one important boundary.

FAIR makes research objects and metadata more findable, accessible under stated conditions, interoperable, and reusable. Scientific tests evaluate whether a proposed use is correct. CARE and other governance processes address whether that use is beneficial, authorized, responsible, and ethical; our entry screen makes those questions harder to bypass without pretending to answer them automatically. The aim is to build scientific workflows that help people do better science and ensure that agents operate within—rather than outside—the practices and authorities that make that science trustworthy.

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
