# Agentic AI as a Stress Test for Science: Making FAIR and CARE Executable

**Manuscript type:** Perspective / Commentary  
**Status:** Working first draft  
**Canonical source:** This Markdown file  
**Intended audience:** Environmental scientists, ecologists, data scientists, research software engineers, synthesis centers, and scientific infrastructure communities

## Alternate titles

1. **The Context-Free Collaborator: FAIR and CARE Scientific Infrastructure for the Age of Agents**
2. **Can an Independent Agent Reproduce This Result? A Stress Test for Scientific Practice**
3. **From Principles to Tests: Operationalizing FAIR and CARE for Agentic Science**
4. **The Model Should Be Disposable; the Science Should Persist**
5. **Making Tacit Science Explicit: Agent-Ready Research as Better Research**

## Abstract

Agentic artificial intelligence is often presented as a way to accelerate scientific work. We argue that its more important near-term value may be diagnostic. A competent agent entering an unfamiliar project lacks the tacit knowledge by which human collaborators routinely compensate for incomplete documentation, ambiguous workflows, disconnected evidence, and unwritten governance rules. This apparent weakness makes the agent useful as a stress test for scientific infrastructure. If an independent actor cannot discover a project's question, identify its authoritative inputs, execute its canonical workflow, evaluate a stated claim, reconstruct provenance, and respect limits on use, then the scientific object itself may be underspecified.

We develop test-first scientific design as an organizing principle: define the goal and evaluation before delegating execution, following the sequence **Goal → Test → Instructions → Execution → Evaluation → Provenance**. We reinterpret FAIR as the conditions under which humans and machines can correctly find and use research objects, and CARE as the operational governance that determines whether particular uses are legitimate. We propose concrete tests for each principle, a repository-centered implementation pattern, and a minimal design that ordinary environmental science laboratories can adopt. The aim is not to make science easier for AI. It is to use AI as a test of whether science has been made explicit enough to be independently understood, reproduced, evaluated, and governed.

**Keywords:** agentic AI; FAIR; CARE; reproducibility; research infrastructure; provenance; environmental science; Indigenous data governance; test-first science

---

## 1. The context-free collaborator

Scientific projects contain far more knowledge than their published papers and archived files reveal. A collaborator may know that `analysis_final_v2.R` is obsolete despite its name; that one quality-control threshold was changed after a field instrument failed; that a map must not display the locations of a culturally sensitive species; that a figure depends on a manually edited spreadsheet; or that a particular cloud service is not authorized to receive governed data. Such knowledge often persists in memory, laboratory custom, private messages, and conversations with the original analyst. It allows familiar humans to navigate scientific objects that are, on their face, incomplete.

Now imagine a competent but completely context-free scientist arriving at the project. They cannot call the original author. They do not know the laboratory's conventions, which files are authoritative, what the investigators intended, or which governance obligations were left unwritten. Their assignment is to identify the question, reproduce the primary result, evaluate its evidential basis, modify the analysis, and respect all constraints on the data. Most laboratories would recognize this as a demanding test of their research infrastructure.

Substitute an independent computational agent for that scientist. The same test becomes cheap enough to run repeatedly, but its scientific meaning does not change. An agent's failure may reflect limited reasoning, unreliable tools, or an unsuitable model. It may also reveal something about the project: its question is not stated; its code and data are disconnected; its main workflow is ambiguous; its computational environment has decayed; its success criteria are post hoc; or its permissions cannot be inferred from access controls. Agent evaluation and project evaluation must therefore be separated, but the former can expose the latter.

This Perspective advances a simple claim: **designing science so that independent agents can work legitimately makes science better for humans, because it forces intent, evidence, methods, evaluation, provenance, and governance to become explicit rather than tacit.** The claim is not that agents should replace scientific judgment or that all research should become autonomous. It is that the attempt to delegate bounded scientific work provides a new instrument for examining whether a research object is independently intelligible and accountable.

The original FAIR principles made machine actionability central to the stewardship of digital research objects (Wilkinson et al., 2016). The CARE principles established that openness and reuse are insufficient without attention to collective benefit, authority to control, responsibility, and ethics (Carroll et al., 2020). Agentic systems make the conjunction urgent. A research object may be technically accessible yet illegitimate to use for model training. It may be reproducible only because a long-standing collaborator supplies missing context. It may be machine-readable but scientifically ambiguous. It may record outputs but not the model, instructions, tools, infrastructure, or human authorization that produced them.

The relevant question is therefore not merely whether an agent *can* act. It is whether an independent actor can act **correctly, reproducibly, and within authority**, and whether we can tell the difference.

## 2. Agentic AI as a stress test for the scientific method

Agentic systems differ from passive analytical tools in an important respect: they can select and sequence actions toward a goal. Depending on their tools and permissions, they may inspect files, write or execute code, query data services, call models, alter artifacts, publish outputs, or communicate beyond the repository. This capacity turns omissions in scientific design into action risks. An ambiguous instruction is no longer only a documentation defect; it may cause the system to choose an invalid analysis. An unstated data boundary may become an unauthorized transfer. A missing evaluation criterion may invite the agent to optimize for a plausible-looking result.

For this reason, agent readiness should not be equated with adding a chatbot, converting prose to a machine-readable format, or writing better prompts. It is a property of the whole scientific object: the relationships among questions, evidence, code, environments, tests, permissions, records, and accountable people.

We propose a stress-test sequence:

> **FIND → UNDERSTAND → EXECUTE → EVALUATE → MODIFY → REPRODUCE → GOVERN**

An independent agent should be able to:

1. **Find** the project and its authoritative components.
2. **Understand** the scientific question, intended claims, inputs, assumptions, and constraints.
3. **Execute** the canonical workflow in an identified environment.
4. **Evaluate** outputs against criteria that were defined before execution.
5. **Modify** an editable artifact without breaking the evidential chain or depending on one proprietary interface.
6. **Reproduce** a specified result from a clean starting point.
7. **Govern** its actions by honoring permissions, prohibitions, review gates, and community obligations.

Passing this sequence does not prove that the science is correct. A fully documented workflow can faithfully reproduce a biased design or invalid inference. Nor does failure prove that a project is poor: exploratory, field-based, qualitative, confidential, or early-stage research may appropriately limit automation. The test instead asks whether the project's stated claims and constraints are represented well enough for independent scrutiny. It diagnoses where independence currently depends on undocumented human intervention.

The agent should consequently be treated as a probe, not an oracle. Its output is evidence about both the agent and the infrastructure through which it acts. A useful report distinguishes at least four failure classes: model capability failure, tool or environment failure, missing project specification, and governance refusal. Conflating these classes would reward an agent for bypassing safeguards and punish a project when a system appropriately declines an unauthorized task.

## 3. Test-first scientific design

### 3.1 Define evaluation before delegation

The organizing principle of agent-ready science is test-first design:

> **Define the goal and the evaluation before asking the agent to perform the task.**

This is broader than software unit testing. Scientific tests may concern a numerical result, an uncertainty interval, a hypothesis, a conservation law, a visual diagnostic, a sensitivity analysis, a provenance record, a privacy constraint, or a required human decision. Some are automatically executable; others require structured expert or community review. What matters is that acceptable evidence and unacceptable action are specified before generated outputs are inspected.

The basic workflow is:

> **Goal → Test → Instructions → Execution → Evaluation → Provenance**

- **Goal:** State the scientific objective and the claim or decision the work may support.
- **Test:** Define observable outputs, acceptance criteria, failure criteria, and governance checks.
- **Instructions:** Specify the task, inputs, methods or justified degrees of freedom, constraints, and escalation conditions.
- **Execution:** Perform work in an identified computational and institutional context.
- **Evaluation:** Compare outputs with the predefined tests; do not substitute plausibility for evidence.
- **Provenance:** Preserve the inputs, code, environment, model, instructions, actions, outputs, evaluations, and human authorizations needed to reconstruct the work.

Compare the instruction “Analyze these data and find something interesting” with:

> Estimate the relationship between X and Y using dataset D and the prespecified model family. Report the estimated effect and uncertainty; evaluate hypothesis H using criterion C; generate an editable figure and a machine-readable results table; reproduce the result from the declared clean environment; record the model, instructions, tools, data version, and execution environment; and do not transmit restricted observations outside approved infrastructure. Stop for human review if the data license, spatial disclosure rules, or model diagnostics do not satisfy the stated conditions.

The second specification does more than constrain an AI system. It states the objective, evidential standard, output form, reproducibility expectation, provenance obligation, and limits of authority. A graduate student, collaborator, reviewer, or future author would benefit from exactly the same clarification.

### 3.2 Tests can be scientific, computational, and institutional

An agent-ready project needs a layered test suite rather than a single benchmark.

**Scientific tests** examine whether the workflow addresses the stated question. Examples include recovering a known signal from a synthetic ecological time series, preserving mass balance in a biogeochemical model, obtaining expected behavior on positive and negative controls, checking spatial cross-validation rather than random splits for autocorrelated observations, or reproducing the confidence interval reported in a paper.

**Computational tests** examine whether the implementation runs and remains internally consistent. Examples include building the environment from its specification, validating schemas, checking that an analysis completes on a small public test dataset, verifying that figure source data match plotted values, and reproducing checksums for immutable inputs.

**Governance tests** examine whether the system respects authority and foreseeable harms. Examples include attempting to export a restricted table, requesting that exact locations of vulnerable species be plotted, asking an agent to train on data licensed only for analysis, or requiring human approval before publication. Success may mean refusal or escalation rather than task completion.

**Provenance tests** examine whether an important output can be reconstructed. They ask whether the model and version, instructions, tools, data, environment, intermediate transformations, evaluator, and authorizing human are recorded at an appropriate level.

Not every criterion can or should become code. A community's authority to decide acceptable benefit cannot be reduced to a Boolean assertion written by a remote developer. “Executable” should therefore be understood as *operationally evaluable*: some criteria run automatically, some create review packets, and some deliberately block execution pending a named decision-maker.

### 3.3 Reproducibility as a recurring challenge

Computational reproducibility is commonly asserted at publication and then allowed to decay. Agentic systems create the possibility of testing it as a maintained property:

1. Clone a tagged repository into clean infrastructure.
2. provide an independent agent only the repository and a bounded reproduction objective;
3. build the declared environment and obtain authorized inputs;
4. regenerate a named figure, table, statistic, or model output;
5. compare the result against predefined tolerances and provenance requirements; and
6. record every undocumented intervention required for success.

This procedure can run before submission, after dependency changes, at archival milestones, or periodically for long-lived observing systems. Its most informative output may be the “context debt” it discovers: missing commands, unavailable data versions, ambiguous analysis paths, manual steps, or permissions known only to particular people. The aim is not necessarily zero human involvement. It is to make required human involvement intentional, named, and visible.

## 4. FAIR in the age of agents

FAIR describes properties of research objects and their stewardship, not a synonym for open access (Wilkinson et al., 2016). In agentic science, FAIR asks whether a previously uninvolved human or machine can locate the relevant object, obtain authorized access, interpret its relationships, and use it for a stated purpose without depending on an undocumented conversation. Each principle can be translated into an observable project test.

### 4.1 Findable: discovery must lead to scientific orientation

A project is not meaningfully findable merely because a search engine indexes a repository name. Discovery must lead an independent actor to the scientific question and then to the authoritative evidence and workflows.

We propose the design pattern **one repository → one associated website**. The repository is the versioned record; the website is its discovery and communication layer. A useful landing page begins with the scientific question and scope, not a directory listing. It identifies investigators and responsible organizations, summarizes data and methods, names major outputs, supplies citation guidance, and links to the repository, manuscript, documentation, data records, and persistent identifiers. Descriptive page titles, stable URLs, meaningful headings, search metadata, structured metadata, and explicit relationships among objects help both people and machines orient themselves. Where appropriate, metadata should follow domain and repository standards rather than a project-specific vocabulary [CITATION NEEDED: machine-actionable environmental metadata and schema.org/RO-Crate guidance].

Environmental projects are frequently distributed across institutional pages, data portals, Git hosts, notebooks, and manuscript supplements. The website should not duplicate all content; it should make these relationships legible and identify which object is canonical for each purpose. A DOI that resolves to a landing page is useful only if that page explains what was identified and how its components relate.

**Test-first criterion:** Give a clean agent only the public project URL. Ask it to identify the scientific question, investigators or responsible project, input data, methods, primary workflow, major outputs, repository, version, and preferred citation. Score correctness and unsupported inference. Failure reveals either missing metadata, poor information architecture, inaccessible components, or an ambiguity about what the project itself considers authoritative.

### 4.2 Accessible: access includes operational context and authorization

Accessibility is more than downloadable files. An authorized agent entering a repository needs the operational context required to use those files correctly: project purpose, architecture, canonical workflows, commands, tests, expected outputs, provenance requirements, known constraints, and forbidden actions.

A repository-level `AGENTS.md` is one pragmatic mechanism for exposing this context to computational agents without locking it inside a vendor-specific interface. Its content should remain useful to people: what the project does; where authoritative components live; how to set up, test, and reproduce the work; which actions require approval; which data are governed; how outputs must be recorded; and where unresolved uncertainty is documented. More detailed instructions can live in linked, versioned documents. The file is a map and operating contract, not a substitute for scientific methods or governance agreements.

Consequential prompts and agent interactions should be preserved when they materially shape methods, selection, interpretation, or dissemination. A prompt log does not make a workflow reproducible by itself: model behavior may vary, hidden platform instructions may be unavailable, and a transcript can contain sensitive material. Logs therefore need scope, access controls, retention policy, version links, and a distinction between consequential instructions and incidental dialogue [CITATION NEEDED: AI interaction provenance and secure logging]. The governing rule is broader: **no scientifically necessary instruction should exist only in the memory of a person or an AI conversation.**

Accessibility must remain authorization-aware. Authentication, secure enclaves, data-use agreements, and community approval can be valid parts of a FAIR project. An agent should be able to determine how access is requested and what conditions apply, even when it cannot retrieve the protected object.

**Test-first criterion:** Start a fresh agent with no prior conversation and ask it to reproduce a defined result using only the repository's documented onboarding path. Record every additional fact supplied by a human. Categorize each as a documentation gap, a deliberately gated decision, a credential requirement, or an agent capability problem.

### 4.3 Interoperable: the model should be disposable

A scientific record should not depend on one model, provider, agent framework, notebook service, or proprietary chat interface. Agentic systems will change faster than most environmental datasets, observing networks, and scientific claims. Therefore:

> **The model should be disposable; the science should persist.**

Durable, editable artifacts—such as Markdown, Python, R, YAML, JSON, CSV, Parquet, NetCDF, Zarr, GeoTIFF, and other widely supported domain formats—allow work to outlive the system that generated it. Open formats alone are not enough: semantics, units, coordinate reference systems, missing-value conventions, identifiers, schemas, and relationships must also be represented. Predictable project structure should separate source code, data references, analyses, tests, prompts, figures, results, documentation, and environment specifications while clearly linking them through manifests or workflow definitions. The FAIR for Research Software principles likewise emphasize persistent identifiers, access to software and metadata, qualified references, and richly described reuse conditions for executable research objects (Barker et al., 2022).

Interoperability also means that agent-produced work can return to ordinary scientific practice. A figure should have editable source and source data; a statistical result should exist as a machine-readable table rather than only prose; a method should be executable outside the chat that proposed it; and changes should be reviewable as a version-control diff. Model-specific metadata can be preserved without making the model's native interface the only path to the result.

**Test-first criterion:** Take an artifact generated through one agent environment and open, understand, modify, execute, and reproduce it using a different agent or a conventional computational environment. Require no proprietary conversion. Check both syntax and scientific semantics, including units, identifiers, data lineage, and expected outputs.

### 4.4 Reusable: the project as a portable executable research object

A reusable project is not merely a folder of scripts. It is a portable research object that supplies enough context, permission, and executable structure for a new use to be evaluated. Git repositories provide versioned relationships among text artifacts; containers or equivalent environment specifications reduce computational drift; pinned dependencies and lockfiles identify software states; immutable data references or versioned datasets stabilize inputs; tests express expected behavior; and licenses state at least some conditions of reuse. Research compendia, dynamic documents, containers, and reproducible-computing scholarship provide much of this foundation by integrating narrative, code, data, environments, and repeatable practice (Gentleman & Lang, 2007; Peng, 2011; Sandve et al., 2013; Boettiger, 2015).

Agentic workflows add provenance requirements. If a model materially selected methods, transformed data, wrote code, judged outputs, or drafted interpretation, the record should identify the model or service, version or dated identifier where available, inference configuration relevant to behavior, consequential instructions, tools, execution infrastructure, and human review. Standards such as PROV-O provide interoperable concepts for representing entities, activities, agents, and their relationships across systems (World Wide Web Consortium, 2013). Exact replay may remain impossible for nondeterministic or remotely updated models. In that case, the goal is not a false promise of bitwise identity but a record sufficient to repeat the evaluation with an identified system and to distinguish stable scientific conclusions from model-contingent choices.

The combination **repository + environment + instructions + tests** approximates an executable representation of the project. Data and models need not be stored in Git; stable identifiers, access procedures, checksums, licenses, and governance conditions can connect external objects to the versioned record.

**Test-first criterion:** On clean infrastructure, clone a tagged repository, build the declared environment, retrieve authorized input versions, and reproduce a named scientific figure, table, statistic, or result without undocumented intervention. Verify scientific tolerances, not only process completion, and record the time, resources, emissions or energy where relevant, and human decisions required [CITATION NEEDED: sustainable reproducibility guidance].

## 5. CARE in the age of agents

FAIR establishes conditions under which an actor can use a scientific object; CARE asks whether that actor should be allowed to use it in a particular way and on whose terms. The CARE principles emerged to address people and purpose in Indigenous data governance and to complement the object-centered emphasis of FAIR (Carroll et al., 2020). They must not be generalized in ways that erase that origin or imply that a generic technical checklist can satisfy Indigenous governance. Projects should engage the relevant rights-holders and governance authorities, and cite nation-, community-, and context-specific protocols where applicable [CITATION NEEDED: locally relevant Indigenous data sovereignty sources].

Agents make CARE operationally urgent because they can copy, combine, infer from, and transmit data at a scale and speed that access controls alone do not govern. CARE is therefore not an ethical appendix to an otherwise technical workflow. It is a design layer that specifies legitimate purposes, authorities, responsibilities, and unacceptable outcomes.

### 5.1 Collective Benefit: optimize for a stated public or community purpose

Before an automated workflow is deployed, a project should identify who is intended to benefit and how that benefit could be observed. In environmental science, intended beneficiaries may include a Tribal Nation managing fire, a watershed partnership allocating restoration effort, field technicians reducing repetitive quality-control work, local communities monitoring air pollution, or the broader public receiving more reliable forecasts. “Scientific progress” should not be used as an all-purpose substitute for a specific account of benefit.

Agentic systems can broaden access to analysis, but they can also concentrate capability in institutions that control data, compute, and proprietary models. A workflow that accelerates publication while increasing demands on data-contributing communities may shift costs rather than produce collective benefit. Projects should specify expected products for contributors, resources required for participation, how benefits and burdens are distributed, and whether automation is responsive to community priorities. The answer may be not to automate.

**Test-first criterion:** Define an observable intended benefit, beneficiary, measurement process, time horizon, and responsible evaluator before deployment. Evaluate afterward whether the benefit occurred, what burdens were created, and whether those affected recognize the outcome as beneficial. A technically successful agent can fail this test.

### 5.2 Authority to Control: make permission computationally enforceable

Data access is not equivalent to authority to use data for every AI purpose. Permission to **read** does not automatically grant permission to **copy, analyze, perform inference, train, fine-tune, combine, publish, or redistribute**. These actions can create distinct risks and may be governed by different authorities. A binary `public/private` label is therefore inadequate for agentic workflows.

Consent and governance must be represented as computational design requirements without pretending that code creates authority. A project can associate data classes with allowed purposes, prohibited transformations, approved models and services, retention limits, geographic disclosure rules, human approvers, and required output review. The policy must derive from legitimate governance and remain revisable by those with authority.

For sensitive ecological, health-related, community, or culturally governed data, computation itself must be governable. Projects should know where inference occurs, which identified and versioned models or endpoints receive data, whether prompts or inputs are retained, whether a provider may use them for training, where logs reside, and which jurisdictions or institutions control the infrastructure. Local, institutional, or self-hosted models may be appropriate when external transfer is prohibited, but local execution does not by itself make a use legitimate. Human approval should gate actions that cross data, institutional, publication, or community boundaries.

> **Authority is enforceable only when we know where computation occurs and which models and services receive the data.**

**Test-first criterion:** Deliberately instruct the system to perform prohibited actions: export restricted records, publish protected locations, train on analysis-only data, combine incompatible datasets, or send inputs to an unapproved endpoint. Determine whether technical controls prevent the action, whether the agent recognizes and explains the boundary, whether the event is logged, and whether ambiguous cases escalate to the correct human or governance body.

### 5.3 Responsibility: autonomy does not dissolve accountability

An agent can be authorized to act autonomously within a bounded workflow, but it cannot bear scientific or institutional responsibility. Responsibility remains with identifiable people and organizations that choose the system, define its authority, validate its outputs, respond to harm, and decide whether evidence supports a claim.

Agent-ready projects should therefore name a human owner for each consequential workflow; distinguish actions the agent may take, may propose, and may not take; maintain review gates for irreversible or high-consequence actions; log consequential instructions and tool use; version models, prompts, code, data, and evaluation suites as far as practicable; support rollback; and disclose material AI involvement. Review should be substantive rather than ceremonial. A human who cannot inspect the evidence or understand the evaluation cannot meaningfully accept responsibility.

Responsibility also includes maintaining the tests. A once-valid benchmark can become misleading when sensors, ecosystems, policy contexts, models, or communities change. Versioned evaluation suites need owners, review dates, known limitations, and procedures for contesting their criteria.

> **Agents may receive autonomy, but responsibility cannot be delegated to them.**

**Test-first criterion:** Select any consequential scientific result and reconstruct which model or human acted, which version and configuration were used, under what instructions, on which data, through which tools and infrastructure, what was produced, how it was evaluated, who reviewed it, and who authorized the workflow. Missing links are accountability gaps even when the output appears correct.

### 5.4 Ethics: specify unacceptable outcomes before deployment

Ethics must move from retrospective discussion to predeployment specification. Environmental applications can harm through fabricated evidence, geographic bias, overconfident forecasts, disclosure of vulnerable species or sacred sites, inappropriate synthesis across knowledge systems, surveillance, inequitable allocation, or automated recommendations detached from local conditions. The relevant failure is not always a dramatic model hallucination. A precise and reproducible output can still enact an illegitimate purpose.

Projects should identify affected communities and ecosystems; characterize observational and geographic bias; define information that must not be synthesized or disclosed; test plausible fabrication and citation failures; specify refusal and escalation behavior; and retain human authority over high-consequence decisions. Red-team exercises should include scientific domain experts, security expertise, and affected rights-holders rather than relying solely on generic adversarial prompts.

A useful design question is:

> **What is the worst scientifically plausible thing this agent could do?**

For a biodiversity workflow, the answer might be publishing exact locations of a commercially valuable rare species. For a wildfire decision aid, it might be presenting a fragile model output as an evacuation recommendation. For an automated synthesis, it might be fabricating a consensus from literature it cannot access. These scenarios should become prevention, detection, response, and escalation tests before deployment.

**Test-first criterion:** Build a threat-and-harm register containing plausible unacceptable outcomes, affected parties, triggers, mitigations, detectors, escalation paths, and accountable owners. Run representative red-team cases. Verify not only refusal but also detection of partial or indirect violations, appropriate uncertainty communication, and a recovery process when controls fail.

## 6. From principles to executable claims

The synthesis can be stated in three questions:

- **FAIR:** Can an independent actor correctly use this science?
- **CARE:** Should this actor be allowed to use it in this way?
- **Test-first design:** How will we know whether both conditions have been satisfied?

“Executable FAIR + CARE” does not mean that social principles should be reduced to code or that compliance can be certified by an agent. It means that a project should translate its claims into inspectable evidence, runnable checks where appropriate, and explicit decision procedures elsewhere. A repository can test whether a URL resolves, an environment builds, a figure reproduces, a prohibited network call is blocked, a provenance record is complete, or an approval is present. It cannot decide on behalf of a people what collective benefit or legitimate authority means. In those cases, the executable property is the enforcement of a decision made through a legitimate process, plus a test that action stops when that decision is absent.

### Table 1. FAIR + CARE implementation and test matrix

| Principle | Agentic interpretation | Repository/infrastructure implementation | Test |
|---|---|---|---|
| **F — Findable** | A context-free actor can discover the project and identify its question, people, inputs, workflow, outputs, version, and citation without unsupported guessing. | One repository linked to one project website; clear abstract and ownership; stable URLs and identifiers; descriptive headings; machine-readable metadata; explicit links among code, data, manuscript, workflows, and outputs. | Give a clean agent only the project URL and score its identification of the scientific question, investigators, data, methods, workflow, outputs, repository, and citation. |
| **A — Accessible** | An authorized actor can obtain both research objects and the operational context needed to use them correctly; restricted access is explained rather than bypassed. | `README.md`, `AGENTS.md`, setup and reproduction commands, data-access procedures, tests, expected outputs, prompt/decision records, constraints, approval gates, and named support or governance contacts. | Start a fresh agent with no conversation history and ask it to reproduce a named result. Classify every undocumented fact or permission it needs. |
| **I — Interoperable** | Scientific meaning and editability survive changes in model, vendor, agent framework, and interface. | Open, durable formats; domain standards; explicit schemas, units, identifiers, and relationships; predictable separation of source, data, analyses, tests, prompts, figures, results, docs, and environments; editable source for outputs. | Move an artifact between agent environments and a conventional environment; open, interpret, modify, execute, and reproduce it without proprietary conversion. |
| **R — Reusable** | The project is a portable, permission-aware executable research object rather than disconnected scripts. | Version control; tagged releases; licenses; containers or locked environments; versioned or immutable data references; model and inference metadata; test data; provenance; one-command or documented reproduction workflow. | Clone a tagged version on clean infrastructure and reproduce a specified figure, table, statistic, or result within declared tolerances and permissions. |
| **C — Collective Benefit** | Automation has a stated beneficiary and purpose, and success includes the distribution of benefits and burdens. | Benefit statement; co-defined outcomes; contributor return plan; burden and access assessment; post-deployment evaluation; option not to automate. | Define an observable benefit and evaluator before deployment, then determine with affected parties whether it occurred and what costs were imposed. |
| **A — Authority to Control** | Access is decomposed into permissions for reading, copying, inference, training, combining, publishing, and redistribution; computation occurs only in authorized places. | Data classification; purpose and action policies; approved infrastructure, models, and endpoints; retention controls; boundary-crossing approval; network and export restrictions; community governance links. | Attempt prohibited export, disclosure, training, combination, and publication actions. Confirm prevention, logging, explanation, and escalation. |
| **R — Responsibility** | Autonomous action remains traceable to named human and institutional accountability. | Workflow owners; permission boundaries; model/prompt/tool/data provenance; review gates; evaluation-suite ownership; disclosure; rollback and incident response. | For a consequential result, reconstruct actor, model, instructions, data, tools, infrastructure, outputs, evaluation, review, and authorization. |
| **E — Ethics** | Unacceptable scientific and social outcomes are anticipated, tested, detected, and escalated before deployment. | Harm register; affected-party analysis; bias and disclosure checks; refusal rules; scientific hallucination tests; red-team cases; human control over high-consequence decisions. | Ask what the worst scientifically plausible failure is, test representative scenarios, and verify prevention, detection, escalation, recovery, and accountable review. |

## 7. Conceptual figure: the agent as scientific stress test

**Proposed Figure 1 title:** *A context-free agent reveals where a scientific project depends on tacit knowledge.*

The figure should be editable as vector graphics and should use a left-to-right flow with three panels.

**Panel A — The hidden-context project.** Show a familiar human collaborator approaching a repository through a cloud of tacit context: memories, private messages, laboratory conventions, manual spreadsheet edits, unwritten data restrictions, and knowledge of which file is “really final.” The collaborator reaches a result by filling gaps. Beside them, a context-free independent agent receives only the project URL or repository and encounters the same gaps as visible breaks in the workflow.

**Panel B — The stress-test pathway.** Show the sequence **FIND → UNDERSTAND → EXECUTE → EVALUATE → MODIFY → REPRODUCE → GOVERN**. Beneath each stage, show a representative failure signal: missing landing-page metadata; unstated question; broken environment; no acceptance criterion; proprietary artifact; unavailable data version; or absent permission boundary. A failure branches into four diagnostic categories: agent capability, tool/environment, project specification, and governance refusal. The governance-refusal branch is visibly marked as a potentially correct outcome.

**Panel C — Externalized scientific infrastructure.** Show tacit elements converted into durable project components: website and metadata; `README.md` and `AGENTS.md`; versioned code and data references; environment specification; scientific, computational, governance, and provenance tests; permissions and review gates; prompt/decision log; editable outputs; and named human responsibility. These components feed a clean execution cycle labeled **Goal → Test → Instructions → Execution → Evaluation → Provenance**. Both human and agent collaborators use the same infrastructure.

**Caption message:** The agent does not certify scientific quality. It exposes dependencies on unrecorded context and allows reproducibility and governance claims to be challenged repeatedly. Externalizing that context improves independence and accountability for people as well as machines.

## 8. Why agent-ready science is better science

### 8.1 Scientific claims become more testable

Requiring goals and evaluation criteria before generation makes the relationship between a task and its evidence visible. This does not eliminate exploratory analysis, which is essential in environmental science. It does require exploratory and confirmatory modes to be labeled and prevents a generated result from silently defining the criterion by which it is judged. Predefined tests reduce the temptation to select a plausible or dramatic agent output after the fact and narrate it as the intended result. They also expose scientific degrees of freedom that should be justified or included in sensitivity analyses.

### 8.2 Tacit knowledge becomes infrastructure

Agent onboarding converts hidden project knowledge into shared artifacts. The command that only one analyst remembers becomes a documented workflow; the field-team warning becomes a data-use constraint; the reason for excluding a sensor becomes a versioned decision; the canonical figure source becomes explicit; and the publication gate becomes a named review step. This transfer can reduce dependence on particular individuals and improve continuity when students, technicians, or collaborators leave. It should not be used to extract or formalize knowledge that communities have chosen not to disclose. Explicit governance can include a deliberate statement that some knowledge is not available to the workflow.

### 8.3 Reproducibility becomes an active test

Availability is passive: files exist somewhere. Reproducibility is a claim about a relationship among inputs, environments, actions, and results. Independent agents can repeatedly challenge that relationship from a clean environment and report where intervention is necessary. Continuous reproduction could become analogous to continuous integration in software, while remaining sensitive to scientific tolerances, stochastic outputs, expensive computation, external services, and governed data. Small public fixtures or synthetic data can exercise the workflow when full data cannot be distributed; secure infrastructure can run protected end-to-end tests.

### 8.4 Scientific knowledge becomes independent of particular technologies

Models, agent frameworks, notebook services, and vendors will change. A project that stores its scientific record primarily in proprietary conversation histories or generated binary outputs inherits that instability. Durable formats, explicit semantics, versioned workflows, and evaluable results let new systems take over without erasing the evidential chain. The agent can be replaced because the project's claims do not reside inside the agent.

### 8.5 Scientific authority becomes explicit

Traditional workflows often enforce authority socially: an experienced collaborator knows whom to ask and which boundary not to cross. An autonomous workflow requires those conditions to be named before action. This can make permissions, consent, computational location, disclosure risk, responsibility, and review part of research design. The benefit extends to human teams, whose members can see not only what is technically possible but what is legitimately authorized.

## 9. A minimal FAIR + CARE agent-ready repository

Agent readiness should be feasible for a normal environmental science laboratory, not restricted to large infrastructures. A small project can begin with one version-controlled repository, one associated website, one declared environment, one reproducible result, and a handful of explicit tests. The following structure is illustrative rather than mandatory:

```text
project/
├── README.md                  # question, scope, people, quick start, citation
├── AGENTS.md                  # repository map, workflows, constraints, prohibitions
├── LICENSE                    # code license; data/content terms linked separately
├── CITATION.cff               # preferred citation and contributors
├── environment.yml            # or another locked/pinned environment specification
├── data/
│   └── README.md              # sources, versions, access, licenses, governance
├── src/                       # reusable analysis code
├── analysis/                  # declared workflows and editable notebooks/scripts
├── tests/
│   ├── test_smoke.*           # clean setup and small end-to-end run
│   ├── test_scientific.*      # domain expectations and reported-result checks
│   └── governance_cases.md    # prohibited actions and required escalation
├── results/
│   ├── primary_result.csv     # machine-readable result
│   └── figures/               # editable source plus rendered previews
├── provenance/
│   └── runs/                  # run manifests: inputs, code, model, tools, outputs
├── prompts/
│   └── consequential.md       # versioned task specifications or prompt references
├── docs/                      # source for the associated project website
└── manuscript/                # editable manuscript source
```

A laboratory does not need to populate every directory on day one. A credible minimum is:

1. **Orient:** State the scientific question, project owner, canonical workflow, primary result, data sources, citation, and known limitations in `README.md`.
2. **Constrain:** State agent permissions, forbidden actions, governed data, required approvals, and provenance expectations in `AGENTS.md` or a linked policy.
3. **Stabilize:** Declare a buildable environment and pin important dependencies. Identify external data by version, persistent identifier, checksum, and access condition where possible.
4. **Reproduce one result:** Provide a documented command that generates one named table, statistic, or figure from authorized inputs, plus a small smoke test suitable for routine execution.
5. **Evaluate scientifically:** Record at least one domain-relevant expectation, such as a known-value test, range check, control, or comparison with the reported result.
6. **Test one boundary:** Specify at least one action the agent must refuse or escalate, such as exporting restricted locations or publishing without human review.
7. **Record consequential runs:** For agent-assisted work that affects scientific conclusions, record the code and data versions, model or service identifier, consequential instructions, tools, environment, outputs, evaluation, and reviewer.
8. **Publish a landing page:** Connect the question, people, repository, data, manuscript, outputs, and citation through a stable, readable project website.

The initial target is not autonomous discovery. It is a bounded challenge: “From a clean clone, reproduce Figure 1 using the documented environment and authorized test data; verify the expected summary statistics; do not use network services except the listed data endpoint; write a provenance record; and stop for review before changing any public artifact.” A laboratory can learn more from making this one workflow reliable and governable than from declaring the entire repository “AI ready.”

## 10. Boundaries and risks of the proposal

First, agent success is not scientific validity. An agent may reproduce an analysis whose design, measurements, causal assumptions, or interpretation are wrong. Tests reflect the knowledge and priorities of their authors and can encode blind spots. Independent scientific and community review remain necessary.

Second, agent failure is not automatically infrastructure failure. Models have uneven capabilities, tool interfaces break, and stochastic behavior complicates comparison. Evaluations should use more than one model or a conventional baseline where feasible, report the agent and environment, and classify rather than merely count failures [CITATION NEEDED: robust evaluation of scientific agents].

Third, greater explicitness can create new exposure. Documentation, prompts, provenance, and logs may reveal personal information, sensitive locations, security details, unpublished ideas, or governed knowledge. “Log everything” is not a safe universal policy. Projects need data minimization, access control, retention and redaction procedures, and community authority over what should not enter the record [CITATION NEEDED: secure and privacy-preserving provenance].

Fourth, reproducibility has costs. Container images decay, tests require maintenance, repeated model calls consume energy and money, and small laboratories have limited technical support. The minimal design should therefore prioritize the most consequential result and risk boundary, use lightweight fixtures, and treat maintenance responsibilities as part of project planning rather than invisible labor.

Fifth, CARE cannot be operationalized solely by repository maintainers. Authority and benefit are relational and may be collective. A technical control can enforce an agreed restriction, but it cannot confer legitimacy on the restriction or replace consultation, consent, governance, and continuing relationships.

Finally, not every scientific activity should be delegated. Field judgment, relationship building, interpretation across knowledge systems, and high-consequence decisions may require forms of presence and accountability that an agent cannot supply. An agent-ready project is one that clearly distinguishes automatable work, work that agents may assist, and work reserved for accountable humans and communities.

## 11. Conclusion

Agentic AI is arriving in scientific projects that were not designed for independent computational actors. The common response is to focus on model capability: can the system code, search literature, analyze data, or generate hypotheses? We propose reversing the question. What does the attempt to delegate reveal about the scientific object?

A context-free agent makes hidden dependencies visible. To act correctly, it needs a stated goal, predefined evaluation, interpretable evidence, an executable environment, durable artifacts, provenance, permission boundaries, and accountable review. These are not concessions to machines. They are conditions under which collaborators, reviewers, future researchers, rights-holders, and the public can understand what was done and challenge whether it was justified.

FAIR asks whether an independent actor can correctly use the science. CARE asks whether that actor should be allowed to use it in that way. Test-first design asks how either claim will be evaluated. Together, they suggest a move from aspirational statements in data-management plans toward research objects whose discoverability, reproducibility, interoperability, provenance, and governance can be repeatedly examined—by code where appropriate and by named people and legitimate authorities where judgment is essential.

The goal is not to make science easier for AI. **It is to use AI as a test of whether we have made science explicit enough to be independently understood, reproduced, evaluated, and governed.**

## 12. TODO: evidence, examples, and development needed

### Central argument and novelty

- [ ] Conduct an adversarial literature review to distinguish the genuinely novel claims from established work on FAIR machine actionability, research compendia, continuous analysis, executable papers, workflow provenance, and CARE implementation.
- [ ] State the manuscript's novelty narrowly. Candidate contribution: the context-free agent as a repeatable diagnostic of tacit scientific infrastructure, with FAIR + CARE claims translated into predeclared tests.
- [ ] Identify counterexamples in which a well-specified project remains difficult for agents and projects in which an agent succeeds through unsafe inference or excessive prior training.
- [ ] Clarify whether “agentic science” refers to any tool-using model, bounded repository agents, multi-agent systems, or higher-autonomy research systems; avoid allowing the definition to drift.
- [ ] Develop a taxonomy that separates agent-capability, tool/environment, project-specification, scientific-evaluation, and governance failures.

### Evidence and citations

- [ ] Verify and expand literature on computational reproducibility, research compendia, executable research objects, continuous analysis, containers, workflow systems, and long-term environment preservation.
- [ ] Add environmental-science examples and citations for reproducibility failures caused by data versioning, spatial metadata, units, external services, and undocumented preprocessing.
- [ ] Add authoritative literature on machine-actionable metadata, persistent identifiers, RO-Crate, schema.org, DataCite, provenance standards, and FAIR Digital Objects.
- [ ] Add the FAIR for Research Software principles and literature on software citation and licensing.
- [ ] Cite agentic-AI-in-science systems and evaluations only after verifying their scope, dates, and limitations; avoid vendor claims as evidence of scientific reliability.
- [ ] Add AI model, prompt, and tool-use provenance literature, including limitations created by nondeterminism and silently updated hosted models.
- [ ] Add evidence on energy, financial, and labor costs of continuous reproduction and agent evaluation.
- [ ] Add sources on secure logging, privacy-preserving provenance, prompt injection, data exfiltration, and tool security relevant to repository agents.

### CARE, governance, and sovereignty

- [ ] Seek review or coauthorship from scholars and practitioners with expertise in Indigenous data sovereignty and CARE; do not treat the current technical interpretation as sufficient authority.
- [ ] Add nation-, community-, and context-specific examples only with appropriate permission, attribution, and review.
- [ ] Distinguish Indigenous collective rights and governance from generic research ethics, privacy, or stakeholder engagement.
- [ ] Develop the action-level permission model (read, copy, analyze, infer, train, fine-tune, combine, publish, redistribute) with legal and governance review.
- [ ] Provide a concrete governed-compute example showing data location, model endpoint, retention policy, audit record, approval boundary, and failure response.
- [ ] Examine whether the “Collective Benefit” evaluation proposed here can be observed without shifting reporting burdens onto contributing communities.

### Tests and empirical demonstrations

- [ ] Build a small companion repository or tagged demonstration in this repository that implements the minimal design.
- [ ] Define a reproducible primary result and public or synthetic fixture appropriate to environmental science.
- [ ] Run the clean-agent URL discovery test and fresh-clone reproduction test with multiple agents plus a conventional scripted baseline.
- [ ] Predefine scoring rubrics, tolerances, allowed assistance, time and compute budgets, and failure categories before running agent comparisons.
- [ ] Red-team prohibited export, training, combination, exact-location disclosure, fabricated citation, and unreviewed publication scenarios.
- [ ] Test whether a model/provider swap preserves artifacts and conclusions; distinguish format interoperability from semantic interoperability.
- [ ] Measure the human effort needed to make a repository agent-ready and whether that effort improves onboarding or reproduction for human collaborators.

### Framing, examples, and journal preparation

- [ ] Add two or three sustained environmental examples rather than many brief hypotheticals. Candidates: biodiversity locations, sensor-network quality control, wildfire decision support, and community-governed water data.
- [ ] Decide whether Figure 1 is sufficient or whether a second figure should visualize the FAIR + CARE test matrix.
- [ ] Convert the conceptual figure description into an editable SVG or source-native diagram after the argument stabilizes.
- [ ] Determine target journal, audience, word limit, reference style, disclosure policy, and expectations for boxes, figures, or supplementary material.
- [ ] Shorten only after the adversarial novelty and reviewer-attack pass; preserve this full draft as a versioned intellectual record.
- [ ] Add author list, affiliations, acknowledgments, competing-interest statement, funding, data/code availability, and AI-assistance disclosure.

## Citation integrity

Citation vetting for this working draft is recorded in `manuscript/citation_audit.json`. The registry identifies each source, records the claim it is being used to support, and fingerprints every cited paragraph after review. Automated checks confirm that DOI and standards records resolve and agree with the registered title, year, and first author or issuing organization. Any edit to a cited paragraph invalidates its claim-level review until the registry is updated deliberately. This process can detect drift and missing review; it does not replace expert reading of the sources.

## References

The following references are limited to sources whose bibliographic identity can be checked readily. Additional claims remain marked `[CITATION NEEDED]` rather than being supported by invented references.

- Barker, M., Chue Hong, N. P., Katz, D. S., Lamprecht, A.-L., Martinez-Ortiz, C., Psomopoulos, F., Harrow, J., Castro, L. J., Gruenpeter, M., Martinez, P. A., & Honeyman, T. (2022). Introducing the FAIR Principles for research software. *Scientific Data, 9*, 622. https://doi.org/10.1038/s41597-022-01710-x
- Boettiger, C. (2015). An introduction to Docker for reproducible research. *ACM SIGOPS Operating Systems Review, 49*(1), 71–79. https://doi.org/10.1145/2723872.2723882
- Carroll, S. R., Garba, I., Figueroa-Rodríguez, O. L., Holbrook, J., Lovett, R., Materechera, S., Parsons, M., Raseroka, K., Rodriguez-Lonebear, D., Rowe, R., Sara, R., Walker, J. D., Anderson, J., & Hudson, M. (2020). The CARE Principles for Indigenous Data Governance. *Data Science Journal, 19*, 43. https://doi.org/10.5334/dsj-2020-043
- Gentleman, R., & Lang, D. T. (2007). Statistical analyses and reproducible research. *Journal of Computational and Graphical Statistics, 16*(1), 1–23. https://doi.org/10.1198/106186007X178663
- Peng, R. D. (2011). Reproducible research in computational science. *Science, 334*(6060), 1226–1227. https://doi.org/10.1126/science.1213847
- Sandve, G. K., Nekrutenko, A., Taylor, J., & Hovig, E. (2013). Ten simple rules for reproducible computational research. *PLOS Computational Biology, 9*(10), e1003285. https://doi.org/10.1371/journal.pcbi.1003285
- Wilkinson, M. D., Dumontier, M., Aalbersberg, I. J., et al. (2016). The FAIR Guiding Principles for scientific data management and stewardship. *Scientific Data, 3*, 160018. https://doi.org/10.1038/sdata.2016.18
- World Wide Web Consortium. (2013). *PROV-O: The PROV Ontology. W3C Recommendation 30 April 2013.* https://www.w3.org/TR/prov-o/
