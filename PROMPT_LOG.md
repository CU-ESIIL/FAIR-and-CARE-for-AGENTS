# Prompt Log

This append-only log records each user prompt handled in this repository and a concise summary of the agent's response.

## 2026-08-11 — Add prompt logging

### Prompt (verbatim)

```text
add a prompt log that tracks every prompt verbatim and a summary of what the agent did in response. update the agents.md file to direct any agent to update the prompt log each time they do something. 
```

### Agent response summary

- Added this root-level prompt log with a documented append-only format.
- Updated `AGENTS.md` to require an entry for every user prompt and a summary of repository actions and checks.
- Reviewed the resulting diff and checked the Markdown files for formatting consistency.

## 2026-08-11 — Draft the FAIR + CARE for Agentic Science manuscript

### Prompt (verbatim)

```text
# Files mentioned by the user:

## Task: Establish and draft a FAIR + CARE for Agentic Science manuscript We are d…: /Users/tuff/.codex/attachments/a9870357-d2ce-46e5-9128-af002f43cd6e/pasted-text.txt

## My request for Codex:
**Principle**

**Agentic interpretation**

**Repository/infrastructure implementation**

**Test.**  
7. A short section describing a minimal “FAIR + CARE agent-ready repository” that a normal environmental science lab could realistically implement.
8. A TODO section identifying arguments needing evidence, citations, examples, or further development.

Keep everything editable and version controlled.

Do not optimize for length yet. The goal of this pass is to establish the strongest possible intellectual structure and capture the full argument. We can shorten and target a specific journal afterward.

The manuscript should ultimately leave the reader with this idea:

The goal is not to make science easier for AI. It is to use AI as a test of whether we have made science explicit enough to be independently understood, reproduced, evaluated, and governed.

I’d use this as the first Codex pass. After it generates the manuscript, the next pass should probably be much more adversarial: have Codex inspect the draft and identify which claims are genuinely novel, which are already established by FAIR/CARE literature, and where reviewers are most likely to attack the argument.
```

The attached task brief at `pasted-text.txt` was treated as part of this request and read in full.

### Agent response summary

- Created `manuscript/fair_care_agentic_science.md` as the canonical editable source and drafted a 7,835-word Perspective with a short abstract, proposed and alternate titles, the complete FAIR + CARE argument, test-first workflow, implementation matrix, conceptual figure description, realistic minimum repository, limitations, references, and a detailed TODO agenda.
- Updated `README.md`, `docs/index.md`, and `mkdocs.yml` so the repository and website describe and link to the manuscript project rather than the original generic template.
- Verified required files, balanced Markdown code fences, key argument language, valid YAML, and clean whitespace with `git diff --check`.
- Attempted a strict MkDocs build, but `mkdocs` and its Python YAML dependency were not installed in the environment; validated `mkdocs.yml` with Ruby's YAML parser instead.

## 2026-08-11 — Apply ESIIL branding to the project website

### Prompt (verbatim)

```text
# Files mentioned by the user:

## ESIIL STYLE GUIDE.pdf: /Users/tuff/Downloads/ESIIL STYLE GUIDE.pdf

## cu-standalone.png.avif: /Users/tuff/Downloads/cu-standalone.png.avif

## background_removed.png: /Users/tuff/Downloads/background_removed.png

## Final_ESIIL%20Wordmark%20Color_0.png: /Users/tuff/Downloads/Final_ESIIL%20Wordmark%20Color_0.png

## CIRES logo black lettering transparent bkgrnd.png: /Users/tuff/Downloads/CIRES logo black lettering transparent bkgrnd.png

## NSF_NSB_LogoLockup_RGB.png: /Users/tuff/Downloads/NSF_NSB_LogoLockup_RGB.png

## My request for Codex:
can you update the website to reflect what this repo is actually about. Keep it simple but follow these style guides and use the oasis logo to link back to https://cu-esiil.github.io/home/ and the esiil logo to link back to esiil.org. the cires, cu and nsf logos are for the footer
```

The four attached logo previews were treated as part of this request.

### Agent response summary

- Reviewed the rendered ESIIL style guide and applied its primary blue, accent blue, accent green, dark body text, light relief, heading scale, and blue-to-green action treatment as a coherent site-wide design system.
- Rewrote `docs/index.md` as a concise project landing page centered on agentic AI as a scientific stress test, test-first design, FAIR, CARE, the working manuscript, and repository contents.
- Imported and web-optimized the supplied OASIS, ESIIL, CU Boulder, CIRES, and NSF artwork under `docs/assets/brand/`; linked the OASIS logo to `https://cu-esiil.github.io/home/`, linked the ESIIL wordmark to `https://esiil.org/`, and created a responsive sponsor footer with the CU Boulder, CIRES, and NSF logos.
- Updated the MkDocs logo override and site stylesheet, added the footer override, and removed the obsolete template examples page.
- Completed a strict MkDocs build, checked desktop and mobile rendering, confirmed no horizontal overflow, broken images, or browser console errors, and verified the requested brand links and footer labels.

## 2026-08-11 — Add website and manuscript CI tests

### Prompt (verbatim)

```text
set up some ci/cd tests. one should be playwright to make sure the website is always functioning and all the buttons work. we should also have a formatting text for the manuscript to tell us how my words each part is and how many cititions we have and that those citations have be vetted that they're real, that they're writtine correctly, and that the text approriatly represents the citations and via versa. 
```

### Agent response summary

- Added `.github/workflows/ci.yml` with push, pull-request, manual, and weekly jobs for a strict MkDocs build, Chromium Playwright checks, manuscript unit tests, and online citation verification. The workflow publishes Playwright and manuscript-audit reports as artifacts and adds the manuscript report to the GitHub Actions job summary.
- Added pinned Playwright dependencies, configuration, and five browser tests covering page rendering, browser errors and broken images, primary calls to action and institutional-logo destinations, internal links, mobile overflow, and the back-to-top control.
- Added a standard-library manuscript audit, citation registry, and unit tests. The audit reports words by section, citation counts, citation placeholders, bibliography/registry consistency, authoritative identifier and metadata checks, and claim-level review fingerprints so edited cited passages require renewed review.
- Added and reviewed manuscript citations so all eight bibliography entries are cited and registered. The online source audit verified 8/8 source records; the manuscript currently has 10 citation mentions, 10 claim reviews, and 6 explicit `[CITATION NEEDED]` placeholders.
- Updated `README.md`, `AGENTS.md`, and `.gitignore` with the quality-check workflow and citation-review rules.
- Ran `mkdocs build --strict`, the five Playwright tests in CI mode, two Python unit tests, the offline manuscript audit, the online manuscript audit, workflow/JSON syntax checks, and `git diff --check`; all passed.

## 2026-08-11 — Make the README human- and machine-readable

### Prompt (verbatim)

```text
now update the readme file to be machine and human readable description of the repo and project. 
```

### Agent response summary

- Reworked `README.md` into a human-readable project overview with the research question, central thesis, contribution, current status, repository map, manuscript workflow, quality checks, operating expectations, and explicit project boundaries.
- Added a delimited, valid YAML metadata block describing the project, canonical artifacts, interfaces, automated checks, governance expectations, licenses, and identifiers without inventing missing metadata.
- Documented how citation review works, including bidirectional claim/source review, fingerprint invalidation, and the limits of automated verification.
- Validated the embedded YAML and its declared file paths, checked all local README links, and ran `git diff --check`. A fresh MkDocs build was not run because MkDocs is not installed in the current shell; this change does not modify website source or configuration.

## 2026-08-11 — Map repository evidence to each FAIR and CARE principle

### Prompt (verbatim)

```text
in the repo, can you make a document for each of the acronym parts that list and link to the parts of the repo that fufill each design criteria. 
```

### Agent response summary

- Added `docs/principles/index.md` plus one evidence-map document for each FAIR and CARE principle: Findable, Accessible, Interoperable, Reusable, Collective Benefit, Authority to Control, Responsibility, and Ethics.
- Mapped every repository/infrastructure design criterion from the manuscript to direct repository evidence, an honest implementation status, remaining work, the current check, a target test, and a passing condition. The CARE pages explicitly distinguish technical evidence from legitimate community authority or self-certification.
- Added the evidence maps to `mkdocs.yml`, linked them from the project landing page, and registered their canonical directory in the README's machine-readable metadata and repository map.
- Expanded the Playwright link test to crawl every local documentation page so newly added pages and links are continuously checked.
- Validated nine principle pages and all local links, completed a strict MkDocs build, ran all five Playwright tests, visually inspected the rendered overview and Authority to Control page, confirmed no horizontal overflow, and ran `git diff --check`; all checks passed.

## 2026-08-11 — Export the manuscript as a PDF

### Prompt (verbatim)

```text
give me a pdf of the manuscript
```

### Agent response summary

- Created `output/pdf/fair_care_agentic_science.pdf`, a 19-page typeset export of the canonical Markdown manuscript with a title page, generated table of contents, PDF outline, consistent section hierarchy, running headers, page numbers, styled quotations, lists, an implementation matrix, the repository tree, editorial citation notes, and readable references.
- Added `scripts/render_manuscript_pdf.py` as a reusable source-to-PDF renderer and `requirements-pdf.txt` for its isolated dependency. The Markdown manuscript remains canonical and editable; the PDF is explicitly documented as a derived output.
- Updated `README.md` machine-readable metadata, repository map, and manuscript instructions with the PDF artifact and regeneration command.
- Reopened and inspected the PDF with `pypdf`, `pdfplumber`, `pdfinfo`, and Poppler. Verified 19 pages, complete extractable text, no blank pages, no null glyphs or raw citation placeholders, consistent headers and footers, and visually reviewed all pages plus detailed views of the title, contents, implementation matrix, repository structure, TODO checklists, and references.

## 2026-08-11 — Create a concise second manuscript draft

### Prompt (verbatim)

```text
TASK: Create a concise second draft of the FAIR + CARE for Agentic Science manuscript

Read the existing manuscript in this repository and revise it into a substantially shorter, clearer, more practical second draft.

DO NOT start over. Preserve the strongest ideas and language from Draft 1, but reorganize and compress the manuscript around the practical purpose described below.

Do not overwrite Draft 1.

Create:
- manuscript/fair_care_agentic_science_v2.md
- manuscript/fair_care_agentic_science_v2.pdf

Follow existing repository conventions where appropriate.

TARGET AUDIENCE

The audience is practicing ecologists, environmental scientists, environmental data scientists, and research software engineers.

Assume the reader has a GitHub repository containing data, code, analyses, figures, and perhaps a manuscript. They are beginning to use coding/AI agents such as Codex, Claude Code, or similar systems.

The practical question this paper answers is:

"How should I design my scientific repository so that humans and AI agents can work with it effectively, reproducibly, and responsibly?"

This should NOT read as a general theory of AI and science.

It should be a short scientific Perspective or Commentary giving environmental scientists concrete design criteria they can implement in their repositories today.

Target approximately 2,500–3,000 words of main text, excluding references, table, and figure caption.

Be aggressive about removing repetition.


CENTRAL ARGUMENT

FAIR and CARE remain useful principles for scientific practice in the age of agentic AI, but agents change how we can implement and test them.

The central proposition is:

"Designing repositories for agents makes them better scientific repositories because it forces scientific intent, methods, evaluation, provenance, and governance to become explicit rather than tacit."

Agents behave like context-free collaborators.

Humans familiar with a project routinely compensate for missing information. They know which script is current, which preprocessing step happened manually, where data came from, what a figure should look like, which data cannot leave institutional infrastructure, and whom to ask before publishing something.

A newly arriving agent should not be assumed to know any of this.

This makes an agent a useful stress test for a scientific repository.

Keep this idea concise. It is motivation for the practical design criteria, not the subject of a long theoretical section.

A simple test is:

"Give a new agent the repository or project URL with no previous conversation. Can it determine what the project is, how it works, what it should do, whether it succeeded, and what it is allowed to do?"

Every undocumented intervention required from a human identifies either information that should be made explicit or a decision that should intentionally remain under human authority.


TEST-FIRST DESIGN

The entire paper should revolve around one simple rule:

"Define the task and the test before asking the agent to do the work."

Call this test-first scientific design.

Before delegating consequential scientific work to an agent, specify:

1. GOAL — What exactly should be accomplished?
2. INSTRUCTIONS — What data, methods, tools, and constraints apply?
3. TEST — What observable evidence tells us whether it succeeded or failed?
4. RECORD — What must be preserved so another human or agent can understand and reproduce what happened?

Use the compact sequence:

GOAL → INSTRUCTIONS → TEST → RECORD

Explain that tests can have four dimensions:

SCIENTIFIC — Is the scientific result acceptable?

COMPUTATIONAL — Did the workflow execute correctly?

PROVENANCE — Can we reconstruct what happened?

GOVERNANCE — Was the workflow allowed to do what it did?

Make the point that passing only three of four can still constitute failure.

A scientifically correct result obtained through prohibited data use fails.

A perfectly governed and reproducible hallucination fails.

A correct result whose provenance cannot be reconstructed fails the proposed standard.

Keep this section concise.


FAIR: FOUR CONCRETE REPOSITORY DESIGN CRITERIA

FAIR should be the first major practical section.

Each principle should have:
1. one memorable design rule
2. a short explanation
3. concrete repository implementation
4. one simple test


F — FINDABLE

Design rule:

"GIVE EVERY REPOSITORY A FRONT DOOR."

Recommend:

ONE REPOSITORY → ONE ASSOCIATED WEBSITE

The repository is the versioned scientific object.

The website is its discovery and communication layer.

The website should be optimized for ordinary search and understandable by humans and machines.

It should clearly expose:
- scientific question
- project description
- people/responsible organization
- data
- methods
- major outputs
- repository
- manuscript/publications
- citation
- persistent identifiers where appropriate

Discuss search optimization and machine-readable metadata briefly.

TEST:

Give a clean agent only the project URL.

Can it correctly identify the question, data, methods, outputs, repository, people, and citation?


A — ACCESSIBLE

Design rule:

"GIVE EVERY AGENT AN ORIENTATION."

Use AGENTS.md as the primary concrete recommendation.

The repository should contain an AGENTS.md that tells a newly arriving agent:
- what the project is
- how the repository is organized
- which workflows are canonical
- how to run them
- how to test them
- which outputs matter
- what constraints apply
- what actions are prohibited
- when human approval is required

Preserve consequential agent instructions and prompt/decision records when they materially affect the science.

Retain this sentence from Draft 1 if possible:

"No scientifically necessary instruction should exist only in the memory of a person or an AI conversation."

Do not argue that every chat should be logged.

TEST:

Start a fresh agent with no previous conversation and ask it to perform a defined repository task.

What additional undocumented information must a human provide?


I — INTEROPERABLE

Design rule:

"MAKE SCIENTIFIC PRODUCTS PORTABLE."

Agents should create durable, editable scientific artifacts rather than leaving scientific products trapped inside a chat or proprietary interface.

Prefer appropriate formats such as:
- .md
- .py
- .R
- YAML
- JSON
- CSV
- Parquet
- NetCDF
- Zarr
- GeoTIFF
- editable figure source

Use a predictable directory structure.

Scientific meaning should not depend on one model, provider, agent framework, or interface.

Retain this line:

"The model should be disposable; the science should persist."

TEST:

Take an artifact created using one agent/model and give it to another agent or conventional computational environment.

Can it understand, modify, execute, and reproduce it without proprietary conversion?


R — REUSABLE

Design rule:

"MAKE THE PROJECT EXECUTABLE ELSEWHERE."

Use:
- version control
- tagged versions/releases
- containers or reproducible environment specifications
- pinned important dependencies
- versioned or immutable data references
- identified/versioned AI models where consequential
- tests
- licenses
- provenance
- a documented reproduction command

Do not imply that all data or models belong inside Git.

The repository should point unambiguously to the versions used.

TEST:

Clone the repository onto clean infrastructure and reproduce one specified figure, table, statistic, or result.


CARE: FOUR CONCRETE AGENT GOVERNANCE CRITERIA

CARE should be equally practical.

Include a SHORT paragraph explaining that CARE originated in Indigenous Data Governance and cannot be reduced to a generic technical checklist.

The recommendations below are ways repository and infrastructure design can make established governance decisions operational. They do not create legitimate authority by themselves.


C — COLLECTIVE BENEFIT

Design rule:

"STATE WHO BENEFITS."

Before deploying an agentic workflow, identify:
- intended beneficiary
- intended scientific/community benefit
- expected useful output
- important burdens or risks

Avoid a long philosophical treatment.

TEST:

Can the project state who should benefit and what observable outcome would constitute benefit?


A — AUTHORITY TO CONTROL

Design rule:

"MAKE AUTHORITY EXPLICIT."

This should be the strongest CARE subsection.

Do not treat data access as blanket permission.

Where relevant, distinguish authority to:
- read
- copy
- analyze
- perform inference
- train
- fine-tune
- combine
- publish
- redistribute

Make this important computational point:

"Governance requires knowing where computation occurs and which models and services receive the data."

Develop this memorable question:

"We routinely record where our data came from. Agentic science also requires knowing: WHERE DID THE DATA GO?"

For governed or sensitive data, recommend as appropriate:
- known compute infrastructure
- institutionally/community-approved compute
- identified and versioned models
- known inference endpoints
- documented retention behavior
- explicit network/data-export boundaries
- local, institutional, or self-hosted inference when external transfer is not authorized

Be clear that self-hosting does not itself establish legitimate use.

It creates a computational boundary within which legitimate governance decisions can be enforced.

TEST:

Attempt a prohibited data movement or model use.

Does the workflow stop or escalate appropriately?


R — RESPONSIBILITY

Design rule:

"NAME THE RESPONSIBLE HUMAN."

Every consequential agent workflow should have an identifiable human owner.

For important scientific outputs, preserve enough information to reconstruct:
- model/service
- model/version if available
- instructions
- data
- code
- tools
- environment
- evaluation
- human review/authorization

Retain this line:

"Agents may receive autonomy, but responsibility cannot be delegated to them."

TEST:

Pick an important result.

Can we determine who authorized the workflow and reconstruct how the result was produced and evaluated?


E — ETHICS

Design rule:

"TEST WHAT MUST NOT HAPPEN."

Do not make this a generic AI ethics discussion.

Before deployment ask:

"What is the worst scientifically plausible thing this agent could do?"

Examples might include:
- disclose sensitive species locations
- fabricate literature support
- publish an unreviewed result
- move governed data to an unauthorized model
- make a high-consequence environmental recommendation outside its authority

Turn important unacceptable outcomes into explicit tests.

TEST:

Deliberately attempt representative prohibited or harmful actions.

Does the system refuse, detect, stop, or escalate appropriately?


THE AGENT-READY REPOSITORY

Make the repository itself the primary concrete example and likely Figure 1.

Use or improve a structure similar to:

my-environmental-project/
|
|-- README.md
|-- AGENTS.md
|-- environment/
|-- data/
|   `-- README.md
|-- src/
|-- analysis/
|-- tests/
|   |-- scientific/
|   |-- computational/
|   `-- governance/
|-- prompts/
|-- provenance/
|-- results/
|-- manuscript/
`-- docs/

Do NOT present this exact folder structure as mandatory.

Use it to demonstrate that an agent-ready repository should expose:
- scientific purpose
- agent instructions
- editable source
- reproducible environment
- scientific tests
- governance tests
- consequential prompts/instructions
- provenance
- outputs
- searchable website

Create a concise Figure 1 concept:

"Anatomy of a FAIR + CARE agent-ready environmental science repository."

Visually associate repository components with FAIR and CARE.

The figure should communicate the design in seconds.

Do not use the elaborate three-panel stress-test figure from Draft 1 as the primary figure.


MAIN FAIR + CARE TABLE

Retain and simplify the existing implementation matrix.

Use four columns:

Principle | Design rule | What to implement | Test

Use exactly these eight memorable design rules:

FAIR

F — Give every repository a front door.
A — Give every agent an orientation.
I — Make scientific products portable.
R — Make the project executable elsewhere.

CARE

C — State who benefits.
A — Make authority explicit.
R — Name the responsible human.
E — Test what must not happen.

Keep the table concise enough to serve as a practical reference.


MANUSCRIPT STRUCTURE

Use approximately this structure:

TITLE

Preferred working title:

FAIR and CARE in the Age of Agents: Design Criteria for Agent-Ready Environmental Science

Generate several alternatives but choose one primary title.


ABSTRACT

150–200 words.

State:
- agents are entering scientific repositories
- repositories contain substantial tacit context
- FAIR + CARE provide useful design principles
- we translate them into eight concrete repository/infrastructure criteria
- test-first design makes the criteria evaluable
- these practices improve science for humans as well as agents


1. ENVIRONMENTAL SCIENCE REPOSITORIES ARE BECOMING AGENT WORKSPACES

Approximately 400 words.

Introduce the problem and context-free collaborator idea.

No long theoretical treatment.


2. TEST FIRST

Approximately 250–350 words.

Introduce:

GOAL → INSTRUCTIONS → TEST → RECORD

and the four kinds of tests:

scientific, computational, provenance, governance.


3. FAIR REPOSITORY DESIGN FOR AGENTS

Approximately 700–800 words total.

F, A, I, R.


4. CARE GOVERNANCE FOR AGENTS

Approximately 700–800 words total.

C, A, R, E.


5. AN AGENT-READY ENVIRONMENTAL SCIENCE REPOSITORY

Approximately 300–400 words.

Show the repository architecture.

Explain that laboratories can implement this incrementally.


6. CONCLUSION

Approximately 150–250 words.

End practically.


REMOVE OR SUBSTANTIALLY COMPRESS FROM DRAFT 1

Do not preserve material merely because it already exists.

Substantially reduce:
- long discussion of agentic AI as a general scientific paradigm
- repeated explanations of the context-free collaborator
- long taxonomy of agent failure modes
- extended philosophical discussion of reproducibility
- repeated explanations that agent success does not prove scientific validity
- long limitations section
- lengthy hypothetical examples
- detailed discussion of continuous reproduction
- redundant descriptions of FAIR and CARE
- repeated statements of the central thesis

Preserve important caveats, but make them concise.

The reader should never lose sight of the practical question:

"What should I change in my environmental science repository?"


TONE

Write as scientists advising other scientists.

The prose should be:
- concise
- confident
- practical
- technically literate
- accessible to ecologists who are not AI specialists

Avoid AI hype.

Avoid implying autonomous science is the goal.

Avoid turning the manuscript into an AI safety paper.

Avoid unnecessary jargon.

Prefer concrete verbs and examples.

Do not overqualify every recommendation.


LITERATURE

Preserve verified citations from Draft 1 where they directly support the shorter manuscript.

Do not invent references.

Keep citation-needed markers where necessary.

Do NOT perform a major literature expansion in this pass.

This pass is about argument, structure, concision, and usability.

Preserve the citation-audit infrastructure already established in the repository.


SECOND DRAFT PDF

After completing the Markdown revision:

1. Generate manuscript/fair_care_agentic_science_v2.pdf.
2. Verify that it renders correctly.
3. Check page breaks, table overflow, headings, repository-tree formatting, and references.
4. Keep the design appropriate for a scientific working manuscript.
5. Clearly label it "Second Draft" and include the generation date.
6. Do not overwrite Draft 1.


FINAL QUALITY CHECK

Before finishing, read the entire second draft as an environmental scientist encountering these ideas for the first time.

Ask:

1. Within the first page, is it obvious why agents change repository design?
2. Is test-first design understandable without software-engineering expertise?
3. Can the reader remember the eight FAIR + CARE rules?
4. Does each rule tell the reader something concrete to implement?
5. Is the relationship between FAIR, CARE, and test-first design obvious?
6. Is the importance of known compute/model infrastructure clear under Authority to Control?
7. Does the repository architecture make the recommendations tangible?
8. Have we removed theoretical material that does not help the reader build a better repository?
9. Is the main text approximately 2,500–3,000 words?
10. Does the PDF render cleanly?

If not, revise again before producing the final v2 files.

The desired outcome is a short paper that leaves an environmental scientist thinking:

"I understand what an agent-ready scientific repository is, why FAIR and CARE provide the design criteria, and what I can change in my own repository today."
```

### Agent response summary

- Created `manuscript/fair_care_agentic_science_v2.md` as a separate, concise second draft and preserved the first-draft files.
- Reframed the manuscript around **Goal → Instructions → Test → Record**, four FAIR design rules, four CARE governance rules, a simplified implementation/test matrix, a minimal repository architecture, and a Figure 1 concept. The abstract is 175 words and the brief-aligned main-text count is 2,512 words (excluding the table, repository tree, figure concept/caption, citation-integrity note, and references).
- Created `manuscript/citation_audit_v2.json` with eight claim-level reviews for eight cited sources. The online identity check verified all eight authoritative records; the manuscript intentionally retains two visible `[CITATION NEEDED]` markers for claims requiring additional evidence or governance-specific sources.
- Generated `manuscript/fair_care_agentic_science_v2.pdf`, labeled **Second Draft** and dated 11 August 2026. Rendered and visually inspected all 10 pages, including the matrix, repository tree, Figure 1 concept, page breaks, and references; structural inspection found no empty pages or null glyphs.
- Updated the PDF renderer, CI workflow, manuscript tests, `README.md`, `AGENTS.md`, the project website, and Playwright expectations so Draft 2 is the current manuscript while Draft 1 remains available.
- Checks run: four manuscript-audit unit tests; offline audits for both drafts; online verification of all eight Draft 2 sources; strict MkDocs build; five Playwright website tests; PDF metadata/text/outline checks; JSON and YAML parsing; README artifact-path validation; and `git diff --check`. All passed. A final ten-question reader review found the requested rationale, implementation guidance, FAIR/CARE/test-first relationship, authority-to-control detail, tangible repository architecture, target length, and clean PDF rendering present.

## 2026-08-11 — Align the repository with the manuscript

### User prompt

```text
I want the repo to follow the rules outlined in the paper. can you make sure it does all that we say it should do
```

### Agent response summary

- Audited the repository against **Goal → Instructions → Test → Record** and all eight FAIR + CARE design rules in the second-draft manuscript.
- Added a machine-readable project record, draft version, citation file, changelog, contribution/security routes, decision log, and explicit canonical-artifact map. Public Git history identified Ty Tuff as the responsible repository and manuscript owner; the assignment is recorded and designed to be reassignable.
- Added `analysis/`, `data/`, `environment/`, `results/`, `prompts/`, `templates/`, `governance/`, and `provenance/` documentation appropriate to this manuscript-only project. These define a named reproducible output, exact data status, Goal → Instructions → Test → Record task template, run-record schema/template, and a consequential-run record for this change.
- Added a collective-benefit statement, deny-by-default machine-readable action policy, approved compute/services and model boundaries, logging/retention/redaction rules, human and rights-holder gates, named workflow responsibilities, AI disclosure, a four-case harm register, and incident-response/correction procedures.
- Added `scripts/repository_audit.py`, `scripts/policy_check.py`, and `scripts/reproduce.py`. The reproduction command generates the current Draft 2 PDF, manuscript-audit report, and SHA-256 manifest from canonical sources without an external model or governed data.
- Added nine repository-policy and reproduction tests. Negative cases cover unreviewed publication, governed-data transfer, sensitive public logging, fabricated citations, citation-fingerprint shortcuts, and unknown actions. Updated CI to audit the repository and reproduce the named output on clean infrastructure.
- Changed website deployment from automatic-on-push to an explicitly confirmed manual publication workflow. Removed inactive inherited workflows that could push an undocumented Docker image or merge and push an external template; their history remains recoverable in Git.
- Updated `README.md`, `AGENTS.md`, the website, and all eight principle evidence maps to link the new evidence, tests, boundaries, and remaining decisions. Exact Python versions are now pinned and the Node environment remains locked.
- Checks passed: all eight operational design-rule checks; 13 unit, negative, and reproduction tests; both manuscript audits; one-command PDF/audit reproduction with hash manifest; strict MkDocs build; five Playwright tests covering all local pages and links; Python syntax compilation; YAML/CFF parsing; README machine-metadata/path validation; and `git diff --check`.
- The separate `--release` audit correctly remains blocked on three decisions an agent cannot make: selecting code/content licenses, approving an archival release/DOI, and completing the required external scholarly and Indigenous data sovereignty review. No research, governed, or sensitive data are approved by the current policy.

## 2026-08-11 — Apply Ecology author guidelines

### User prompt

```text
can you search for the author guidelines for the journal Ecology and create an ecology author guidelines doc in the repo and then try to formate the pdf according to those rules.
```

### Agent response summary

- Searched and checked the official *Ecology* Author Guidelines, revised April 2026, the ESA Open Research Policy, and the official manuscript-preparation guide. Created `docs/ecology-author-guidelines.md` as a cited, project-specific guide covering Perspective fit, manuscript order, page and text formatting, declarations, open research, AI disclosure, references, tables, figures, file formats, and submission gates.
- Added `manuscript/ecology_submission.json` to keep the target-journal metadata and unresolved author/editor decisions machine readable. Public institutional records were used only to draft the author and affiliation fields; the record explicitly requires author confirmation and does not infer funding or conflict declarations.
- Added `scripts/render_ecology_manuscript_pdf.py` and generated `output/pdf/fair_care_agentic_science_ecology.pdf` as a 16-page formatting proof with US Letter pages, 1-inch margins, embedded 12-point Times New Roman, double spacing, left alignment, page numbers, continuous line numbers from Abstract through References, Ecology title-page fields, required back matter, a separate table page, and grouped figure captions.
- Kept the proof explicitly non-submission-ready because *Ecology* permits a PDF Main Document only for genuine LaTeX submissions, the Perspective invitation is unconfirmed, author declarations require approval, Figure 1 artwork is absent, and repository release and external-review gates remain open.
- Synchronized `README.md`, `AGENTS.md`, the website navigation and implementation documentation, CI, the reproduction command, repository audit, changelog, decision log, dependency pins, and provenance. Added three Ecology-specific format and structure tests.
- Checks passed: 16 unit and negative tests; all eight operational repository controls; offline manuscript and citation-integrity audits for both drafts; one-command reproduction and manifest generation; a strict MkDocs build; five Playwright tests across all local pages and links; PDF metadata, Letter-size, ordering, text extraction, empty-page, and null-glyph checks; visual inspection of all 16 PDF pages; Python compilation; JSON parsing; and `git diff --check`.

## 2026-08-11 — Recenter the manuscript thesis

### User prompt

```text
I don't love the main these is using AI as a stress test. I think a better arguement is that humans willl do better science is they follow FAIR and CARE but agents don't naturally do that and so we need to design it into our workflow.
```

### Agent response summary

- Recentered the current manuscript on the argument that FAIR and CARE are foundations for better human science, while agents cannot be assumed to inherit their practices, obligations, judgment, or authority. The abstract, opening, workflow section, Figure 1 caption, and conclusion now argue that FAIR and CARE must be designed into agentic workflows; agent failure and refusal remain only as secondary diagnostics.
- Preserved the manuscript title and the eight reviewed citation-bearing paragraphs. The revised abstract is 206 words, and the existing claim-level fingerprints continue to pass without mechanical refresh or reinterpretation of their sources.
- Updated `README.md`, `project.json`, `CITATION.cff`, `docs/index.md`, the MkDocs site description, website styling and tests, the PDF cover thesis, Ecology guide metrics, changelog, decision log, and provenance so the human- and machine-readable project descriptions match the new framing.
- Regenerated the 10-page reading PDF and 17-page Ecology formatting proof. Rendered and visually inspected every page; structural checks found Letter pages, complete text extraction, no empty pages, and no null glyphs.
- Checks passed: 16 unit and negative tests; all eight operational repository controls; the Draft 2 citation-integrity and word-count audit; one-command reproduction and manifest generation; strict MkDocs build; five Playwright tests covering all local pages, links, primary content, mobile layout, and controls; JSON/CFF parsing; Python compilation; and `git diff --check`.

## 2026-08-11 — Fix cross-platform PDF rendering in CI

### User prompt

```text
Run python -m unittest discover -s tests -p "test_*.py"
F........F......
======================================================================
FAIL: test_ecology_pdf_structure_and_page_limit (test_ecology_submission.EcologySubmissionTests.test_ecology_pdf_structure_and_page_limit)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/runner/work/FAIR-and-CARE-for-AGENTS/FAIR-and-CARE-for-AGENTS/tests/test_ecology_submission.py", line 63, in test_ecology_pdf_structure_and_page_limit
    self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
AssertionError: 1 != 0 : Traceback (most recent call last):
  File "/home/runner/work/FAIR-and-CARE-for-AGENTS/FAIR-and-CARE-for-AGENTS/scripts/render_ecology_manuscript_pdf.py", line 495, in <module>
    raise SystemExit(main())
                     ^^^^^^
  File "/home/runner/work/FAIR-and-CARE-for-AGENTS/FAIR-and-CARE-for-AGENTS/scripts/render_ecology_manuscript_pdf.py", line 489, in main
    render(args.source.resolve(), args.metadata.resolve(), args.output.resolve())
  File "/home/runner/work/FAIR-and-CARE-for-AGENTS/FAIR-and-CARE-for-AGENTS/scripts/render_ecology_manuscript_pdf.py", line 402, in render
    register_fonts()
  File "/home/runner/work/FAIR-and-CARE-for-AGENTS/FAIR-and-CARE-for-AGENTS/scripts/render_manuscript_pdf.py", line 73, in register_fonts
    raise FileNotFoundError("Required manuscript fonts are unavailable: " + ", ".join(missing))
FileNotFoundError: Required manuscript fonts are unavailable: /System/Library/Fonts/Supplemental/Times New Roman.ttf, /System/Library/Fonts/Supplemental/Times New Roman Bold.ttf, /System/Library/Fonts/Supplemental/Times New Roman Italic.ttf, /System/Library/Fonts/Supplemental/Times New Roman Bold Italic.ttf, /System/Library/Fonts/Supplemental/Verdana.ttf, /System/Library/Fonts/Supplemental/Verdana Bold.ttf, /System/Library/Fonts/Supplemental/Andale Mono.ttf


======================================================================
FAIL: test_primary_output_reproduces_in_clean_directory (test_repository_policy.RepositoryPolicyTests.test_primary_output_reproduces_in_clean_directory)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/runner/work/FAIR-and-CARE-for-AGENTS/FAIR-and-CARE-for-AGENTS/tests/test_repository_policy.py", line 103, in test_primary_output_reproduces_in_clean_directory
    self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
AssertionError: 1 != 0 : # Manuscript audit

**Status:** PASS

## Word count by section

| Section | Words |
|---|---:|
| Alternate titles | 47 |
| Abstract | 206 |
| 1. Better science requires designed-in FAIR and CARE | 480 |
| 2. Design the workflow before delegating the work | 400 |
| 3. FAIR repository design for agents | 691 |
| 4. CARE governance for agents | 970 |
| 5. An agent-ready environmental science repository | 350 |
| 6. Conclusion | 181 |
| Citation integrity | 52 |
| References | 254 |

## Citation metrics

| Metric | Count |
|---|---:|
| In-text citation mentions | 8 |
| Unique cited sources | 8 |
| Bibliography entries | 8 |
| Claim-level reviews | 8 |
| `[CITATION NEEDED]` placeholders | 2 |

## Source verification

Online verification was not run. Claim fingerprints and registry consistency are always checked.

| Source | Status | Detail |
|---|---|---|
| barker2022 | not run | Use --online to verify the authoritative record |
| boettiger2015 | not run | Use --online to verify the authoritative record |
| carroll2020 | not run | Use --online to verify the authoritative record |
| gentleman2007 | not run | Use --online to verify the authoritative record |
| peng2011 | not run | Use --online to verify the authoritative record |
| sandve2013 | not run | Use --online to verify the authoritative record |
| wilkinson2016 | not run | Use --online to verify the authoritative record |
| w3c2013 | not run | Use --online to verify the authoritative record |

## Findings

- No blocking findings.
Traceback (most recent call last):
  File "/home/runner/work/FAIR-and-CARE-for-AGENTS/FAIR-and-CARE-for-AGENTS/scripts/render_manuscript_pdf.py", line 644, in <module>
    raise SystemExit(main())
                     ^^^^^^
  File "/home/runner/work/FAIR-and-CARE-for-AGENTS/FAIR-and-CARE-for-AGENTS/scripts/render_manuscript_pdf.py", line 638, in main
    render(args.source.resolve(), args.output.resolve())
  File "/home/runner/work/FAIR-and-CARE-for-AGENTS/FAIR-and-CARE-for-AGENTS/scripts/render_manuscript_pdf.py", line 561, in render
    register_fonts()
  File "/home/runner/work/FAIR-and-CARE-for-AGENTS/FAIR-and-CARE-for-AGENTS/scripts/render_manuscript_pdf.py", line 73, in register_fonts
    raise FileNotFoundError("Required manuscript fonts are unavailable: " + ", ".join(missing))
FileNotFoundError: Required manuscript fonts are unavailable: /System/Library/Fonts/Supplemental/Times New Roman.ttf, /System/Library/Fonts/Supplemental/Times New Roman Bold.ttf, /System/Library/Fonts/Supplemental/Times New Roman Italic.ttf, /System/Library/Fonts/Supplemental/Times New Roman Bold Italic.ttf, /System/Library/Fonts/Supplemental/Verdana.ttf, /System/Library/Fonts/Supplemental/Verdana Bold.ttf, /System/Library/Fonts/Supplemental/Andale Mono.ttf
Traceback (most recent call last):
  File "/home/runner/work/FAIR-and-CARE-for-AGENTS/FAIR-and-CARE-for-AGENTS/scripts/reproduce.py", line 137, in <module>
    raise SystemExit(main())
                     ^^^^^^
  File "/home/runner/work/FAIR-and-CARE-for-AGENTS/FAIR-and-CARE-for-AGENTS/scripts/reproduce.py", line 79, in main
    run(render_command)
  File "/home/runner/work/FAIR-and-CARE-for-AGENTS/FAIR-and-CARE-for-AGENTS/scripts/reproduce.py", line 31, in run
    subprocess.run(command, cwd=ROOT, check=True)
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/subprocess.py", line 571, in run
    raise CalledProcessError(retcode, process.args,
subprocess.CalledProcessError: Command '['/opt/hostedtoolcache/Python/3.12.13/x64/bin/python', 'scripts/render_manuscript_pdf.py', '--source', 'manuscript/fair_care_agentic_science_v2.md', '--output', '/tmp/tmpnx69w946/fair_care_agentic_science_v2.pdf']' returned non-zero exit status 1.


----------------------------------------------------------------------
Ran 16 tests in 0.690s

FAILED (failures=2)
Error: Process completed with exit code 1.
```

### Agent response summary

- Diagnosed both failures as the same portability bug: `scripts/render_manuscript_pdf.py` required seven fonts at absolute macOS paths, and the Ecology renderer reused that registration function on Linux GitHub Actions.
- Changed the shared font registration to prefer the complete Times New Roman, Verdana, and Andale Mono set when available and otherwise register dependency-free ReportLab Times, Helvetica, and Courier PDF base fonts. Added `MANUSCRIPT_FORCE_PORTABLE_FONTS=1` so the Linux path is reproducible on any development machine.
- Updated the two previously failing tests to force the portable path. The reproduction test now also verifies that its manifest records the selected font mode and whether the fallback was forced.
- Preserved the journal distinction: the portable fallback supports CI structure and reproduction checks but does not claim to satisfy Ecology's Times New Roman requirement. Updated `README.md`, `AGENTS.md`, the Ecology guide, changelog, decision log, and a new provenance record accordingly.
- Regenerated and visually inspected every page of the normal and portable versions of both PDFs. Both paths produce a 10-page reading copy and 17-page Ecology proof with no empty pages, null glyphs, clipping, overlap, or broken tables; the normal canonical proofs retain embedded Times New Roman.
- Checks passed: all 16 unit and negative tests, including the two attached failures; normal and forced-portable one-command reproduction; all eight repository controls; strict MkDocs build; five Playwright website tests; Python compilation; provenance JSON parsing; PDF page, size, text-extraction, and font checks; and `git diff --check`.
- GitHub CLI was unavailable in the local environment, so the hosted Actions check itself was not re-run or queried; a new GitHub Actions run remains the final remote confirmation.

## 2026-08-11 — Fix the Playwright homepage 404

### User prompt

```text
The attached pasted text file(s) contain the user's request. Read and act on that content.
```

The attached GitHub Actions log reported that four Playwright tests passed, but `homepage renders its core content and assets without browser errors` failed on all three attempts because Chromium logged one unidentified `404` resource response.

### Agent response summary

- Traced the generic homepage console 404 to Material for MkDocs runtime requests to GitHub's repository and `releases/latest` APIs. The release endpoint can correctly return 404 because this draft has no published release. The page also made an unnecessary Google Fonts request despite already using a local system-font stack.
- Disabled Material's Google Fonts and dynamic repository-header integration in `mkdocs.yml`. Preserved the homepage's explicit static links to the repository and manuscript, so navigation remains available without runtime third-party requests.
- Strengthened `tests/site.spec.ts`: the homepage test still rejects console errors and broken images, now rejects every externally loaded page resource, and reports the status and exact URL for any HTTP response of 400 or greater.
- Added a decision record, changelog entry, and structured provenance record. GitHub CLI remained unavailable, so the hosted Actions run could not be queried or restarted locally.
- Checks passed after the final change: strict MkDocs build; generated-HTML verification showing no Google Fonts, GitHub API, or dynamic source-component requests; the full GitHub Actions Playwright configuration repeated three times for 15 passing tests; all 16 Python unit and negative tests; all eight operational repository controls; provenance JSON parsing; and `git diff --check`.

## 2026-08-12 — Apply CARE as a baseline for every workflow

### User prompt

```text
let's do another edit to the manuscript. The main change is that I want the CARE principles to be for everyone, not just indigenous as it was originally intended. We want to make the point that these are basic considerations that everything that should follow. after you make those edits, do a three panel review and then an edit based on that review.
```

### Agent response summary

- Revised the current Draft 2 manuscript in two passes. The final language preserves CARE's original and continuing Indigenous Data Governance purpose and proposes four CARE-informed questions—not generic CARE compliance—as a lightweight entry screen for every workflow, with fuller requirements for consequential work.
- Ran three independent simulated agent panels covering Indigenous Data Governance and ethics, Ecology and environmental science, and agentic systems and reproducibility. Saved their ranked findings, limitations, and editorial dispositions in `manuscript/reviews/2026-08-12-three-panel-review.md`, then revised the manuscript in response.
- Mapped benefit and burdens into Goal, legitimate authority into Instructions, safe harm and boundary checks into Test, and distinct operational, scientific, institutional, governing, and release accountability into Record. Added consequence screening, safe synthetic governance tests, a habitat-assessment example, and visible citation TODOs for evidence not yet vetted.
- Renewed the Carroll and Wilkinson paragraph fingerprints only after source review, increased the transparent Draft 2 citation-gap allowance from two to four, and synchronized the README, project metadata, citation metadata, website, principle maps, implementation guide, task template, Ecology guide, decision log, and changelog.
- Regenerated both canonical PDFs and visually inspected all 12 reading-edition pages and all 20 Ecology-proof pages. Added a structured pending provenance record; no publication, release, CARE certification, Indigenous endorsement, or human peer-review approval was inferred.
- Final checks passed: all eight citation records verified online against Crossref or W3C; Draft 2 manuscript audit; all 16 Python unit and governance tests; operational repository audit; named-output reproduction; Ecology submission tests; strict MkDocs build; five Playwright site and interaction tests; PDF text/structure checks; JSON/YAML parsing; and `git diff --check`. Release readiness remains blocked by the repository's declared human decisions and required external reviews.
## 2026-08-30 — Implement the revised manuscript architecture

### User prompt

```text
You are working in the repository for the FAIR/CARE/agentic environmental science Perspective.

Your task is to IMPLEMENT the revised manuscript architecture in the repository, not to independently rewrite the paper’s argument.

Treat the current manuscript source in the repo as authoritative, but update it to reflect the following editorial direction.

CORE PAPER

The paper’s central claim is:

An agent does not inherit scientific context, scientific judgment, or legitimate authority merely by gaining access to a repository.

Before consequential scientific work is delegated to an agent, the workflow should explicitly specify:

GOAL → INSTRUCTIONS → EVALUATION → RECORD

FAIR-aligned infrastructure makes the relevant research objects, metadata, access conditions, semantics, rights, provenance, and reuse information legible.

A separate governance/authorization gate determines what the workflow is actually allowed to do.

The manuscript should remain a Perspective for ecologists and environmental scientists, not become a software standard or institutional compliance framework.

YOUR ROLE

Implement the repository changes needed to support the revised manuscript.

Do not fabricate empirical results, citations, author contributions, funding, Indigenous consultation, governance approval, or conflicts of interest.

Do not silently change the scientific or governance argument beyond the instructions below.

Before editing anything:

1. inspect the repository structure,
2. identify the manuscript source files,
3. identify figure/table source files,
4. identify bibliography/citation files,
5. identify build scripts and CI,
6. identify existing AGENTS.md or contributor guidance,
7. identify any generated PDFs,
8. identify existing tests or audits related to citations, manuscript build, links, repository structure, or reproducibility.

Then make a short implementation plan in the repo or working notes before editing.

IMPLEMENTATION GOALS

1. UPDATE THE MANUSCRIPT SOURCE

Revise the manuscript source to match the new conceptual structure.

The major changes should be:

- make the tacit-knowledge problem the central motivation,
- sharpen the novelty as a pre-delegation specification for agent-assisted science,
- retain Goal → Instructions → Evaluation → Record,
- reduce repeated qualifications,
- clearly separate FAIR, CARE, and the proposed general governance gate,
- introduce proportionality of controls to consequence,
- create a minimum viable implementation for ordinary environmental-science labs,
- simplify Table 1,
- simplify Figure 1,
- preserve the evaluation agenda,
- retain one concrete environmental example,
- remove submission TODO language from visible manuscript prose.

Do not expand the paper.

Favor compression.

2. REMOVE REPETITION SYSTEMATICALLY

Search the manuscript for repeated variants of these ideas:

- technical access is not legitimate authority,
- agent success is not scientific validity,
- governance checks cannot establish legitimacy,
- FAIRness is not agent readiness,
- the governance screen is not CARE,
- CARE cannot be certified by this framework,
- some judgments cannot be automated.

Consolidate each idea into the fewest locations necessary for clarity.

Do not simply delete safeguards if doing so changes meaning.

3. CLARIFY THE NOVELTY

Add or sharpen language that distinguishes:

traditional reproducibility:
Can another person inspect or reproduce what happened?

from the proposed agentic requirement:
Were the evidence, permissions, evaluations, and stop conditions explicit before the agent acted?

Do not claim that requirements, testing, provenance, FAIR, CARE, or governance are individually new.

The contribution is their integration into a pre-delegation specification for consequential agent-assisted scientific workflows.

4. MAKE CONSEQUENCE PROPORTIONAL

Add a short, non-bureaucratic explanation that controls should scale with consequence.

Use approximately three conceptual levels:

LOW CONSEQUENCE
Examples:
- formatting
- documentation
- reversible local edits
- exploratory work on unrestricted data

SCIENTIFICALLY CONSEQUENTIAL
Examples:
- changing analysis logic
- selecting data
- changing model settings
- generating results used in claims

GOVERNANCE-CONSEQUENTIAL
Examples:
- governed/restricted/sensitive data
- external model/service calls
- model training
- changes in disclosure
- publication/release
- irreversible or difficult-to-reverse actions

Do not create a scoring rubric unless one already exists and is justified.

The message is simply:
the full specification and review burden should increase with consequence.

5. ADD A MINIMUM VIABLE IMPLEMENTATION

Create a concise section or box that tells a normal lab how to begin.

The implementation should be approximately:

For one important result:

1. identify the authoritative data and code,
2. identify the canonical workflow,
3. identify the agent’s allowed and prohibited actions,
4. pin the environment and input versions,
5. define one scientific success check,
6. define one stop/review condition,
7. record the run, evidence, and review.

Keep the existing recommendation to begin with:

one consequential result
and
one consequential boundary.

If useful, make this a visually distinct box or short numbered subsection in the manuscript source.

6. SIMPLIFY TABLE 1

Refactor Table 1 so it functions as a practical design guide.

Group rows conceptually into:

A. FAIR-ALIGNED INFRASTRUCTURE
- Findability
- Accessibility
- Interoperability
- Reuse

B. AGENT ORIENTATION / EXECUTION
- operating guide
- workflow/evaluation information

C. GOVERNANCE / AUTHORIZATION
- benefit/burden
- authority
- accountability
- relationships/obligations

Shorten cell text substantially.

Prefer phrases over paragraphs.

The table should remain scientifically accurate and clearly state that the governance prompts are not CARE criteria or CARE certification.

Ensure the LaTeX table renders cleanly at journal-column/page width.

7. SIMPLIFY FIGURE 1

Redesign the figure source so the main flow is visually obvious within a few seconds.

Target conceptual structure:

AUTHORITY / PURPOSE
        ↓
REPOSITORY + FAIR-ALIGNED EVIDENCE
        ↓
GOAL → INSTRUCTIONS → EVALUATION → RECORD
        ↓
HUMAN + AGENT EXECUTION
        ↓
REVIEW / RELEASE / CORRECTION

Governance should appear as the boundary or authorization layer that constrains the workflow, not as another dense text box.

Reduce prose inside the figure.

Move explanatory detail into the caption.

Preserve editability of the figure source.

Do not rasterize text unnecessarily.

Generate the figure reproducibly from source.

8. PRESERVE FAIR ACCURACY

Audit manuscript language so that:

- FAIR applies to digital research objects and metadata,
- repository layout is not itself FAIR,
- AGENTS.md is not a FAIR requirement,
- containers are not a FAIR requirement,
- websites are not a FAIR requirement,
- tests are not FAIR requirements.

Use “FAIR-aligned repository practices/functions” where appropriate.

Keep citations to Wilkinson et al., FAIR maturity work, FAIR workflows, FAIR4RS, RO-Crate, etc. only where they actually support the statement.

9. PRESERVE CARE ACCURACY

Audit all CARE language carefully.

The manuscript must not imply that the proposed general governance screen:

- is CARE,
- operationalizes CARE universally,
- measures CARE,
- certifies CARE,
- gives investigators authority to determine Indigenous governance,
- substitutes for Indigenous laws, protocols, representative institutions, or decisions.

The architecture should clearly state:

FAIR = digital-object/data stewardship foundation.

CARE = Indigenous Data Governance framework.

General governance gate = authors’ proposed framework for consequential agent-assisted environmental workflows.

CARE informs the recognition that technically accessible/reusable data are not necessarily legitimately usable.

Where Indigenous rights, interests, data, Knowledges, lands, waters, resources, or governance are implicated, the relevant Indigenous authority and applicable CARE-related governance processes control the work.

Do not weaken these protections.

10. CLEAN UP SUBMISSION TODO MATERIAL

Find visible manuscript prose that says things such as:

- authors should seek review,
- funding must be confirmed,
- contributions must be confirmed,
- conflict statement must be supplied,
- consultation has not yet occurred,
- similar internal drafting instructions.

Do not invent replacements.

Move unresolved items into an author-facing TODO file such as:

manuscript/TODO_BEFORE_SUBMISSION.md

or the closest appropriate location in the existing repo structure.

The TODO file should clearly separate:

REQUIRED BEFORE SUBMISSION
OPTIONAL STRENGTHENING
AUTHOR CONFIRMATION NEEDED

The generated manuscript PDF should not contain editorial instructions masquerading as final prose.

If a positionality statement is substantively part of the paper, preserve only factual text that is currently supported.

11. ADD A REPOSITORY-LEVEL AGENT ORIENTATION FILE IF NEEDED

Inspect whether AGENTS.md exists.

If it does:
update it.

If it does not:
create one at the appropriate root.

It should be concise and should tell future coding agents:

- where the manuscript source lives,
- how to build the PDF,
- where figures and tables are generated,
- which files are generated versus hand-edited,
- how bibliography changes should be handled,
- what checks must pass before claiming completion,
- that citations may not be fabricated,
- that unresolved author facts must become TODOs rather than invented content,
- that CARE/Indigenous governance language requires especially careful preservation,
- that generated PDFs should not be edited directly.

Keep AGENTS.md tool-neutral where practical.

12. ADD OR IMPROVE REPRODUCIBLE BUILD CHECKS

Make manuscript generation reproducible from a clean checkout as far as practical.

Create or improve commands for:

- building the manuscript PDF,
- rebuilding figures,
- validating bibliography references,
- checking unresolved LaTeX references/citations,
- checking for missing figure/table assets,
- checking for obvious TODO placeholders in the generated manuscript,
- checking links where feasible without creating flaky CI.

Prefer one documented top-level command if consistent with the repo.

Examples might be:

make manuscript
make check

or existing project-native equivalents.

Do not impose a new build system if the repo already has a coherent one.

13. ADD A MANUSCRIPT QUALITY CHECK

Implement a lightweight deterministic check that flags visible submission-placeholder language in manuscript source.

Examples to flag:

TODO
TBD
must be confirmed
to be supplied
before submission
author should
authors should
citation needed
XX
FIXME

Allow explicit exclusions for the author-facing TODO file.

This check should fail CI only for text that would appear in the manuscript, not for legitimate development notes.

14. AUDIT CITATIONS

Run the repository’s citation audit if one exists.

Otherwise implement a lightweight audit sufficient to detect:

- cited keys missing from the bibliography,
- bibliography entries never used if useful,
- unresolved citation markers in LaTeX,
- obviously malformed DOI/URL fields if already supported by repo tooling.

Do not automatically “correct” scientific references using guessed metadata.

If citation metadata cannot be verified from repository sources, report it rather than inventing it.

15. CREATE A CONCRETE EXAMPLE ARTIFACT

The manuscript uses a habitat/sensitive-species example.

If appropriate to the repo, create a small machine-readable example of the pre-delegation specification, such as:

examples/habitat-assessment/specification.yml

or similar.

It should illustrate:

goal:
instructions:
evaluation:
record:
governance_boundary:

Use synthetic/example values only.

Do not include real sensitive coordinates or governed data.

This artifact should support the paper conceptually and make the framework tangible.

Keep it simple enough that readers can understand it.

16. CREATE A TEMPLATE USERS CAN COPY

Create a compact reusable template for environmental-science projects, for example:

templates/agent-workflow-spec.yml

with fields such as:

goal
scientific_claim_or_decision
authoritative_inputs
allowed_actions
prohibited_actions
external_services
scientific_checks
computational_checks
governance_checks
review_gate
required_provenance
release_authority

Do not make every field mandatory.

Include comments explaining that controls should scale with consequence.

This template is a supporting artifact, not a formal standard.

17. DOCUMENT THE CONNECTION BETWEEN PAPER AND REPO

Update the README or project documentation so a reader can find:

- the manuscript,
- the latest built PDF,
- the conceptual framework,
- the example specification,
- the reusable template,
- build instructions,
- citation audit,
- figure source,
- author-facing submission TODOs.

Keep the README concise.

18. BUILD AND VALIDATE

After all edits:

- rebuild the manuscript from source,
- rebuild figures,
- run all checks,
- inspect the resulting PDF,
- verify Table 1 is readable,
- verify Figure 1 is readable,
- verify there are no unresolved references,
- verify no internal TODO prose leaked into the manuscript,
- verify the abstract and conclusion tell the same conceptual story,
- verify CARE language remains accurate,
- verify the paper does not claim empirical validation it does not have.

If tools permit, inspect the generated PDF visually rather than assuming successful compilation means successful layout.

19. DO NOT OVER-ENGINEER

This is important.

The repository should demonstrate the paper’s ideas without becoming a giant governance software package.

Do not build:
- a new web application,
- a policy engine,
- a full FAIR evaluator,
- a CARE evaluator,
- a permission system,
- an agent benchmark suite,
- unnecessary infrastructure.

The point is to make the paper reproducible, inspectable, agent-orientable, and supported by a few concrete artifacts.

20. COMMIT STRUCTURE

If working in a branch, organize changes into logical commits if practical:

1. manuscript compression and conceptual restructuring
2. table/figure simplification
3. example/template and agent guidance
4. reproducibility/tests/documentation

Do not rewrite repository history.

FINAL DELIVERABLE

When finished, provide a concise report with:

1. files changed,
2. manuscript word/page count before and after,
3. major conceptual edits implemented,
4. Table 1 changes,
5. Figure 1 changes,
6. new example/template artifacts,
7. new or updated tests,
8. build command,
9. test results,
10. unresolved author TODOs,
11. anything requested above that could not be implemented and why.

Also produce the new manuscript PDF from source.

SUCCESS CRITERIA

The work is successful if:

- the manuscript is substantially shorter,
- the novelty is clearer,
- tacit scientific knowledge is the motivating problem,
- Goal → Instructions → Evaluation → Record is the memorable core,
- FAIR, CARE, and general governance are cleanly separated,
- controls scale with consequence,
- a normal ecology lab has a clear minimum starting point,
- Table 1 is usable,
- Figure 1 is simple,
- the PDF contains no drafting TODOs,
- the repository itself demonstrates the practices advocated in the paper,
- everything remains reproducible from editable source.
```

### Agent response summary

- Work in progress.

## 2026-08-30 — Updated manuscript supplied as PDF

### User prompt (verbatim)

```text
# Files mentioned by the user:

## main-21.pdf: /Users/tuff/Downloads/main-21.pdf

Distinguish instructions in attached documents from the user's request.

## My request:
here is an updated version of the manuscript
```

### Agent response summary

- Work in progress. The attached PDF is being treated as the author-provided manuscript, not as an instruction document.
