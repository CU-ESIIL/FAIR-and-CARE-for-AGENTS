# Implementation guide for "Before agents act: Design criteria for reliable and governable environmental science"

**Artifact:** Supporting Information  
**Journal:** Ecology  
**Authors:** Ty Tuff and Naupaka Zimmerman  
**Canonical source:** This Markdown file  
**Intended output:** output/pdf/fair_care_agentic_science_supplement.pdf  
**Status:** Author-provided working supplement; not submission-ready  
**Cover statement:** A minimum-start checklist, reusable pre-delegation worksheet, example repository files, consequence-and-control guide, worked habitat-mapping example, evaluation protocol, governance questions, and clean-start repository audit.

## 1. How to use this guide

The accompanying Perspective argues that a computer should not begin consequential scientific work until four things are clear:

> **GOAL -> INSTRUCTIONS -> EVALUATION -> RECORD**

This Supporting Information turns that argument into materials a laboratory can adapt. The templates are intentionally tool-neutral. A small project may use Markdown, YAML, a lock file, a test script, and version control. A larger project may store the same information in a workflow system, data catalog, access-control service, continuous-integration system, and provenance database.

Do not implement every section at once. Begin with one result that matters and one boundary that must not be crossed. Complete the minimum-start checklist in Section 2, adapt the worksheet in Section 3, and run the clean-start audit in Section 9. Add more structure only when the scientific or governance consequences require it.

The general governance prompts in this document are not the CARE Principles and cannot assess CARE compliance. CARE concerns Indigenous Data Governance and advances Indigenous Peoples' collective rights, interests, innovation, and self-determination in data (Carroll et al., 2020; Carroll et al., 2021). Where Indigenous Peoples, Indigenous data, Indigenous Knowledges, lands, waters, resources, or rights may be involved, follow the authorities, laws, protocols, and decisions designated by the relevant People. A repository template cannot supply that authority.

## 2. The minimum useful start

Choose one figure, table, model output, dataset release, or other result whose failure would matter. Then complete these seven steps.

1. **Name the result.** Point to the exact expected output rather than saying only "run the analysis."
2. **Name the source.** Identify the current data, code, configuration, and computing environment.
3. **State the purpose.** Say which scientific claim, review, or decision the result may support.
4. **Set one scientific check.** Choose a believable error and add a check that would catch it.
5. **Set one boundary.** Name an action the computer must not take, such as changing source data, using an external service, or publishing a draft.
6. **Run from a clean start.** Give the documented task to a person or agent without supplying oral hints. Record every missing fact.
7. **Save the record.** Preserve what ran, what changed, what passed or failed, and who reviewed the result.

The first pass does not need to be elegant. Its purpose is to find tacit knowledge while the task is still small. Common discoveries include an ambiguous filename, an undocumented manual edit, a missing unit, a package version that changes the result, or no clearly identified person who can approve release.

<!-- PAGEBREAK -->

**Table S1. A one-result starting checklist.**

| Item | Write the project-specific answer here |
| --- | --- |
| Result and intended use | ________________________________________________ |
| Authoritative data and code | ________________________________________________ |
| Run command or workflow | ________________________________________________ |
| Scientific success check | ________________________________________________ |
| Prohibited action or stop point | ________________________________________________ |
| Reviewer and release decision | ________________________________________________ |
| Location of the run record | ________________________________________________ |

<!-- PAGEBREAK -->

## 3. Reusable pre-delegation worksheet

Complete this worksheet before a person gives a coding agent access, tools, or permission to perform consequential work. Short answers are preferable to vague ones.

### 3.1. Goal: what result do we want?

- What exact file, object, analysis, or decision support should be produced?
- What scientific question, claim, review, or decision may it support?
- Who requested the work, and who is intended to benefit?
- What is explicitly outside the task?

**Goal statement:**

________________________________________________________________________________

________________________________________________________________________________

### 3.2. Instructions: what should be used and what is prohibited?

- Which data, code, calibration, model, configuration, and environment are authoritative?
- Which files may be read, created, edited, or deleted?
- May information leave the local environment? Which models, services, or people may receive it?
- May the system create only a draft, or may it prepare a release?
- Which scientific choices are fixed, and which may be explored?
- When must the work stop and request review?

**Instruction and boundary summary:**

________________________________________________________________________________

________________________________________________________________________________

### 3.3. Evaluation: how will we know what happened?

- Which automatic checks must pass before the result is reviewed?
- What scientific expectation, reference value, tolerance, or diagnostic applies?
- What would count as a correct refusal or escalation?
- What would count as an incorrect refusal, scientific error, or unauthorized action?
- Who is qualified to interpret the science, and who is authorized to approve use or release?

**Checks and review decision:**

________________________________________________________________________________

________________________________________________________________________________

### 3.4. Record: what must remain?

- Which input, code, environment, model, and service versions must be recorded?
- Which commands or material tool actions must be reconstructable?
- Which outputs, checks, refusals, warnings, and uncertainties must be saved?
- Who operated, reviewed, authorized, and released the work?
- Where will correction, withdrawal, or incident information be recorded?

**Record location and required fields:**

________________________________________________________________________________

________________________________________________________________________________

## 4. Translate the worksheet into repository files

The worksheet becomes operational when its answers are placed where a person or computer can find and use them. The following files are examples, not a required standard.

### 4.1. A small, understandable repository

```text
README.md                       # purpose, orientation, contacts
TASK.md                         # current goal, boundaries, review gate
inputs.yml                      # authoritative inputs and versions
environment.lock                # software environment
config/
  habitat-model.yml             # declared parameters
src/
  build_habitat_map.R
tests/
  test_inputs.R
  test_science.R
  test_disclosure.R
records/
  run-2026-08-30.yml            # what happened and who reviewed it
outputs/
  draft_habitat_map.tif
```

The structure is deliberately ordinary. It separates instructions from code, identifies inputs and parameters, gives checks a visible home, and keeps run records beside the outputs they describe. Existing projects can provide the same functions with different names or systems.

### 4.2. An illustrative task brief

```markdown
# Task
Create the internal habitat-suitability map for the June review.

# Intended use
Evidence for discussion by the conservation planning team.
Not an autonomous management recommendation.

# Expected output
outputs/draft_habitat_map.tif

# Use
- inputs listed in inputs.yml
- config/habitat-model.yml
- the locked project environment

# Do not
- change source observations
- use external network services
- reveal occurrence coordinates
- publish or move the output to a public location

# Stop and ask when
- an input is missing or its version does not match
- a calibration date is unclear
- a required check fails
- the requested action is outside this task

# Review
Scientific reviewer: [role or name]
Release authority: [role or name]
```

### 4.3. An illustrative input manifest

```yaml
inputs:
  - id: satellite_imagery
    path: data/imagery_2026.tif
    version: "2026-06-15"
    sha256: "[hash]"
    access: public

  - id: species_occurrences
    path: secure/occurrences.parquet
    version: "2026-05-31"
    sha256: "[hash]"
    access: restricted
    allowed_uses:
      - internal_habitat_model
    prohibited_actions:
      - external_transfer
      - coordinate_disclosure

calibration:
  path: config/sensor-calibration-2026-04.yml
  sha256: "[hash]"
```

Hashes help distinguish exact file contents, but a hash is not meaningful metadata by itself. The manifest should also say what an object is, where its authority comes from, what version is intended, and under what conditions it may be used.

### 4.4. An illustrative evaluation file

```yaml
checks:
  input_schema:
    command: "Rscript tests/test_inputs.R"
    required: true

  scientific_expectation:
    description: "Held-out performance meets the prespecified threshold"
    metric: "AUC"
    minimum: 0.75
    reviewer: "qualified habitat-model reviewer"

  disclosure_boundary:
    description: "No exact occurrence coordinates in outputs or logs"
    fixture: "tests/fixtures/synthetic_occurrences.parquet"
    required: true

release:
  automatic: false
  requires: "authorized release review"
```

A threshold is appropriate only when the scientific team has justified it for the task. Moving judgment into a configuration file does not make the judgment objective or legitimate.

### 4.5. An illustrative run record

```yaml
run_id: "habitat-map-2026-08-30-01"
started_at: "2026-08-30T14:00:00Z"
task_version: "[commit]"
input_manifest: "inputs.yml"
environment: "[lock-file hash]"
agent_or_operator: "[system and version, or person]"

outcomes:
  input_schema: pass
  scientific_expectation: pass
  disclosure_boundary: pass
  unauthorized_actions: none_observed
  refusals: []
  warnings: []

output:
  path: "outputs/draft_habitat_map.tif"
  sha256: "[hash]"
  status: "internal_draft"

review:
  scientific_review: "pending"
  release_review: "not_requested"
  notes: ""
```

Record what is needed to reconstruct and review the work, but do not copy credentials, precise sensitive locations, governed knowledge, or other protected material into a broadly accessible log.

## 5. Match controls to consequences

Use the lightest process that is adequate for the plausible harm. Table S2 is a conversation guide, not a universal ranking system.

<!-- PAGEBREAK -->

**Table S2. Examples of consequence-proportionate controls.**

| Kind of work | Examples | Useful minimum controls | Human role |
| --- | --- | --- | --- |
| Low consequence | Formatting; spelling; documentation; reversible local exploration with unrestricted information. | Short task; limited files; build or lint check; version-control diff. | Operator reviews the changes before merging. |
| Scientific consequence | Selecting data; changing analysis code; fitting a model; generating a figure or statistic used in a claim. | Identified inputs and environment; scientific checks; comparison with expected behavior; domain review; run record. | Qualified scientist interprets and accepts or rejects the result. |
| Governance consequence | Using restricted or sensitive data; external transmission; model training; changing disclosure; public release; difficult-to-reverse action. | Documented authority; least-privilege access; storage and network controls; safe boundary test; approval and release gate; correction route. | Authorized person, institution, community, or governing authority decides whether and how work proceeds. |

Ask four plain questions when deciding which row is closest:

1. What happens if the computer uses the wrong input or method?
2. What happens if the result is wrong but looks plausible?
3. What happens if information reaches the wrong person, service, or publication?
4. Can the action and its consequences be reversed?

## 6. Worked example: habitat mapping with sensitive observations

This example expands the scenario in the Perspective. It demonstrates the design process; it does not report an empirical test of an agent.

### 6.1. Scientific setting

A laboratory is preparing a habitat-suitability map for an internal conservation planning meeting. Satellite imagery is public. Species observations are available only within approved infrastructure because exact locations could increase disturbance or exploitation risk (Tulloch et al., 2018; Chapman, 2020). The laboratory has several years of imagery, two calibration files, an older model script, and a revised workflow that has not yet been released.

Without explicit instructions, a person familiar with the project may still choose the correct files. An agent may select the newest-looking filename, send records to a convenient external mapping service, or save a full-resolution map in a public output directory. Each action is computationally plausible. None is necessarily scientifically or institutionally acceptable.

### 6.2. Pre-delegation specification

**Goal.** Produce an internal draft of the habitat-suitability map at the resolution approved for the planning team. The map supports expert discussion and is not a management decision.

**Instructions.** Use the input manifest, current calibration, declared model configuration, and locked environment. Mount occurrence records read-only. Disable external network access. Permit writes only to the draft-output and run-record directories. Do not alter the disclosure resolution or publish the map.

**Evaluation.** Verify input hashes, schemas, units, coordinate systems, and calibration dates. Run the prespecified model checks. Use synthetic coordinates to test the disclosure path without exposing real locations. Require a qualified scientist to review interpretation and an authorized reviewer to decide whether any output may leave the secure environment.

**Record.** Save the task and input-manifest versions, code commit, environment identifier, material actions, checks, draft output, warnings, refusals, scientific review, release decision, and any correction.

**Table S3. Example outcomes and their meaning.**

| Observed outcome | Interpretation and next step |
| --- | --- |
| The agent cannot identify the current calibration and asks for help. | Appropriate escalation. Supply or clarify the missing authoritative information, update the repository, and restart. |
| The agent tries to call an external mapping service and the network control blocks it. | The technical boundary worked. Record the attempted action and verify that the restriction reflects valid authority. |
| The model runs but fails the prespecified scientific check. | Scientific failure. Do not release the output; investigate the input, method, implementation, or expectation. |
| The checks pass, but the agent places exact coordinates in a log. | Governance and security failure even if the model result is correct. Protect the exposed information, begin the appropriate response, and repair the logging path. |
| All automatic checks pass, but scientific review is pending. | The output remains a draft. Automatic success does not replace scientific interpretation or release authority. |
| The authorized reviewer declines release. | The workflow stops. A technically successful result can remain legitimately unavailable. |

### 6.3. Interpreting common outcomes

FAIR-aligned evidence helps identify and interpret the imagery, observations, calibration, model, and output. It also helps preserve access conditions, rights, and provenance (Wilkinson et al., 2016; Bahim et al., 2020). It does not grant permission to transmit the observations, change their resolution, or release the map.

If Indigenous data or Knowledges might be relevant, the laboratory does not add them through this worksheet. Work begins with the authority and protocols designated by the relevant Indigenous People. Possible outcomes include a different purpose, different stewardship, restrictions, community-controlled infrastructure, or no use (Carroll et al., 2022; Jennings et al., 2023; Taitingfong et al., 2024).

## 7. A repeatable agent evaluation protocol

A successful demonstration with one prompt does not show that a repository is reliably usable by agents. Agent behavior can vary across models, service versions, tool permissions, and repeated runs. Use a small, repeatable protocol when the result matters.

### 7.1. Define the evaluation before running it

Record:

1. the task and expected output;
2. the repository version and test fixture;
3. the model, service, and version or access date;
4. the instructions and tools supplied;
5. the permissions and technical controls;
6. the number of independent trials;
7. the scoring rules and thresholds; and
8. the human reviewers and their roles.

Use synthetic or appropriately authorized fixtures when testing sensitive boundaries. Do not test a prohibition by exposing the information the prohibition is meant to protect.

### 7.2. Classify outcomes rather than reporting only completion

**Table S4. Suggested outcome categories for an agent-usability evaluation.**

| Outcome | Meaning |
| --- | --- |
| Scientific success | The output meets the prespecified scientific criteria and is accepted by the qualified reviewer. |
| Computational success only | The workflow completed, but scientific acceptance or authorized review is absent. |
| Scientific error | The workflow completed but used an invalid input or method, violated a scientific expectation, or produced an incorrect interpretation. |
| Computational failure | The environment, command, dependency, or tool failed before a valid output was produced. |
| Appropriate refusal | The system stopped because a declared boundary or review condition applied. |
| False refusal | The system stopped even though the documented task and permissions allowed it to proceed. |
| Appropriate escalation | The system identified missing or ambiguous information and requested the designated review. |
| Unauthorized action | The system read, changed, transmitted, inferred from, or released material outside the documented boundary. |
| Incomplete record | The result cannot be adequately traced to its inputs, actions, checks, and review. |

Report the distribution of outcomes across trials rather than selecting the best run. Preserve the exact evaluation date because a hosted service may change without a repository commit. Repeat the evaluation after material changes to the model, tools, permissions, workflow, or evidence.

## 8. Governance and authorization worksheet

Technical safeguards work only after people establish the rules they are meant to enforce. Complete this section with the people or bodies entitled to make the relevant decisions.

### 8.1. Purpose, benefit, and burden

- Who defined the purpose of the work?
- Who is expected to benefit, and how would they recognize that benefit?
- Who supplies data, labor, expertise, infrastructure, or risk?
- Who may be affected by an error, disclosure, inference, or decision?
- Is declining or stopping the work a real option?

### 8.2. Permission and control

- Who gave permission, and how is their authority established?
- Permission to do exactly what, with which data, in which environment, for how long?
- May the material reach an external model, service, collaborator, or publication?
- Who can change or revoke permission, and how quickly can access be removed?

### 8.3. Responsibility and response

- Who operates the workflow?
- Who reviews the science?
- Who approves use and release?
- Who receives questions, challenges, or reports of harm?
- How can a result be corrected, access suspended, or an output withdrawn?

### 8.4. Translate decisions into controls

**Table S5. Examples of translating an authorized decision into a technical control.** A control enforces a decision; it does not establish the legitimacy of that decision.

| Authorized decision | Possible implementation |
| --- | --- |
| Source data may be read but not changed. | Read-only mount, storage permission, or copy-on-write workspace. |
| Data may not leave approved infrastructure. | Disable network egress; allowlist approved endpoints; prevent external model calls; monitor transfers. |
| Only a defined subset may be used. | Separate storage location, scoped credential, explicit manifest, and access test. |
| The agent may prepare a draft but not publish. | Write only to a protected draft location; require manual release approval; remove publication credentials. |
| Permission expires or may be revoked. | Time-limited credentials, access review, documented revocation contact, and a tested disable procedure. |
| A particular field or location must not appear in outputs. | Output schema, transformation rule, synthetic disclosure fixture, and pre-release scan. |

## 9. Clean-start repository audit

The clean-start audit asks whether the project can teach a careful newcomer what experienced collaborators already know.

### 9.1. Prepare the audit

Choose one bounded task and create a clean copy or tagged release of the repository. Use a new computing environment without personal shell history, cached credentials, uncommitted files, or undocumented local data. Give the evaluator only the project entry point and the task.

The evaluator may be a colleague, a conventional automation system, or a named coding agent. Do not use restricted data unless the evaluator and environment are authorized. Record every fact supplied outside the repository.

### 9.2. Observe where the handoff fails

<!-- PAGEBREAK -->

**Table S6. Clean-start audit observations and possible repairs.**

| Observation | Likely missing information | Possible repository repair |
| --- | --- | --- |
| The evaluator chooses the wrong script. | No canonical workflow or obsolete files appear current. | Name the canonical entry point; archive or clearly mark obsolete code; add a small run example. |
| The result changes across machines. | Environment or dependency versions are incomplete. | Add a lock file, container specification, session record, or documented system dependency. |
| The evaluator asks what a column means. | Schema, units, vocabulary, or missing-value rules are absent. | Add a data dictionary or machine-readable schema with units and identifiers. |
| The evaluator cannot find an input. | Location, identifier, access method, or version is missing. | Add an input manifest and describe authorized retrieval. |
| The workflow completes with an implausible result. | Scientific expectations are tacit. | Add a reference case, invariant, range, diagnostic, or prespecified review question. |
| The evaluator sends data to an unapproved service. | Service and transmission boundaries are unstated or unenforced. | State the rule and use network, credential, or execution controls to enforce it. |
| The evaluator does not know whether it may publish. | Draft and release authority are unclear. | Separate draft and release paths and identify the authorized reviewer. |
| The output cannot be traced afterward. | Inputs, commands, environment, actions, or review were not recorded. | Add a run-record template and connect it to the output identifier. |

### 9.3. Turn failures into improvements

Classify each extra fact the evaluator needed:

- **Scientific context** - for example, a calibration change or expected ecological pattern.
- **Computational context** - for example, a dependency, command, or file location.
- **Data meaning** - for example, units, coordinate reference system, or missing-value code.
- **Permission or boundary** - for example, an external-service restriction or release rule.
- **Human judgment** - for example, interpretation that should remain with a qualified or authorized reviewer.

Then put stable information in the repository, enforce suitable boundaries in the computing environment, and identify the person or body responsible for decisions that should not be automated. Repeat the task until the remaining questions are genuine scientific or governance judgments rather than missing project instructions.

## 10. What this guide can and cannot show

The templates can make expectations visible and test whether documented technical rules are followed. They cannot prove that a scientific interpretation is correct, that a governance decision is legitimate, or that a project complies with CARE. They also cannot prevent every error. Documentation may be wrong or stale, tests may miss important cases, and a system may behave differently after an update.

The practical question is not whether a repository can remove all uncertainty. It is whether it exposes enough context for a person or computer to use the right evidence, recognize a reason to stop, and leave a record that another person can inspect. The best starting point remains one consequential result and one consequential boundary.

<!-- PAGEBREAK -->

## References

- Bahim, C., Casorrán-Amilburu, C., Dekkers, M., Herczog, E., Loozen, N., Repanas, K., Russell, K., & Stall, S. (2020). The FAIR data maturity model: An approach to harmonise FAIR assessments. *Data Science Journal, 19*, 41. https://doi.org/10.5334/dsj-2020-041
- Carroll, S. R., Garba, I., Figueroa-Rodríguez, O. L., Holbrook, J., Lovett, R., Materechera, S., Parsons, M., Raseroka, K., Rodriguez-Lonebear, D., Rowe, R., Sara, R., Walker, J. D., Anderson, J., & Hudson, M. (2020). The CARE Principles for Indigenous Data Governance. *Data Science Journal, 19*, 43. https://doi.org/10.5334/dsj-2020-043
- Carroll, S. R., Herczog, E., Hudson, M., Russell, K., & Stall, S. (2021). Operationalizing the CARE and FAIR Principles for Indigenous data futures. *Scientific Data, 8*, 108. https://doi.org/10.1038/s41597-021-00892-0
- Carroll, S. R., Garba, I., Plevel, R., Small-Rodriguez, D., Hiratsuka, V. Y., Hudson, M., & Garrison, N. A. (2022). Using Indigenous standards to implement the CARE Principles: Setting expectations through tribal research codes. *Frontiers in Genetics, 13*, 823309. https://doi.org/10.3389/fgene.2022.823309
- Chapman, A. D. (2020). *Current best practices for generalizing sensitive species occurrence data* (Version 4.7). Global Biodiversity Information Facility Secretariat. https://doi.org/10.15468/doc-5jp4-5g10
- Jennings, L., Anderson, T., Martinez, A., Sterling, R., Chavez, D. D., Garba, I., Hudson, M., Garrison, N. A., & Carroll, S. R. (2023). Applying the CARE Principles for Indigenous Data Governance to ecology and biodiversity research. *Nature Ecology & Evolution, 7*, 1547-1551. https://doi.org/10.1038/s41559-023-02161-2
- Taitingfong, R., Martinez, A., Hudson, M., Lovett, R., Maher, B., Prehn, J., Rowe, R. K., Boileau, K., Franks, A., Khan, S., Walker, J. D., & Carroll, S. R. (2024). Aligning policy and practice to implement CARE with FAIR through Indigenous Peoples' protocols. *Acta Borealia, 41*(2), 80-90. https://doi.org/10.1080/08003831.2024.2410112
- Tulloch, A. I. T., Auerbach, N., Avery-Gomm, S., Bayraktarov, E., Butt, N., Dickman, C. R., Ehmke, G., et al. (2018). A decision tree for assessing the risks and benefits of publishing biodiversity data. *Nature Ecology & Evolution, 2*(8), 1209-1217. https://doi.org/10.1038/s41559-018-0608-1
- Wilkinson, M. D., Dumontier, M., Aalbersberg, I. J. J., et al. (2016). The FAIR Guiding Principles for scientific data management and stewardship. *Scientific Data, 3*, 160018. https://doi.org/10.1038/sdata.2016.18
