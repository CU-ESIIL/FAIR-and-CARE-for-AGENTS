# Decision log

## 2026-08-30 — Specify consequential work before action and keep CARE distinct

**Decision.** Use **Goal → Instructions → Evaluation → Record** as the manuscript's pre-delegation specification. Keep FAIR-aligned research-object evidence distinct from a separate general governance and authorization gate. Preserve CARE as an Indigenous Data Governance framework; the general gate is not CARE and cannot assess CARE compliance or create Indigenous authority.

**Reason.** Repository access does not supply tacit scientific context, judgment, or permission. The four-part specification makes the work inspectable before action, while the conceptual separation avoids turning FAIR into an authorization framework or appropriating CARE as a generic checklist.

**Implementation.** The author-provided 30 August 2026 Ecology manuscript supersedes the interim compressed rewrite. Editable manuscript, metadata, citations, Table 1, Figure 1, templates, example, website, audits, and CI use the revised architecture. Controls scale with consequence and the minimum laboratory starting point remains one important result plus one important boundary.

**Review boundary.** The Perspective is a design proposal, not a standard, compliance framework, or empirically validated assurance system. Publication and scientific acceptance remain subject to author, editorial, scholarly, and—where applicable—Indigenous authority and review.

**Supersedes.** This decision supersedes the 12 August decision to describe the general questions as a universal CARE-informed entry screen. That earlier decision remains below as historical context.

## 2026-08-12 — Use CARE-informed questions universally without redefining CARE

**Decision.** Preserve CARE as the Indigenous Data Governance framework created to advance Indigenous rights, interests, and self-determination. Propose four CARE-informed questions—benefit and burdens, legitimate authority, accountability, and harm—as a lightweight entry screen for every scientific workflow, with a fuller specification for consequential work.

**Reason.** These governance questions should not be optional in ordinary science, but calling CARE itself universal could appropriate or flatten its continuing Indigenous purpose. The entry screen is an author-proposed operational extension, not CARE compliance, certification, restatement, or Indigenous endorsement.

**Implementation.** Distinguish the original principles from the proposed entry screen throughout the manuscript and public documentation. Map the questions directly into **Goal → Instructions → Test → Record**; separate operational ownership from governing, institutional, scientific-review, and release authority; and require safe governance tests. Context-specific authority may constitute, reshape, supersede, or prohibit a workflow.

**Review boundary.** Three simulated agent panels informed this edit but do not substitute for human peer review, Indigenous Data Governance scholarship, or appropriate Indigenous governance authority. That external review remains a release blocker.

## 2026-08-11 — Keep the website runtime self-contained

**Decision.** Disable Material for MkDocs' Google Fonts injection and dynamic repository-header integration. Use the existing local CSS system-font stack and the homepage's explicit static GitHub links.

**Reason.** The public site already specifies Arial, Helvetica, and generic sans-serif fonts. Material's repository header also requests GitHub's repository and `releases/latest` APIs at runtime; the latter can correctly return 404 while this draft has no published release. These external requests were unnecessary because the homepage already links directly to the repository. Removing them eliminates the observed failure class, improves CI reliability, and reduces third-party network dependence without hiding a broken local resource.

**Test.** The homepage test continues to reject browser console errors and broken images, rejects all externally loaded page resources, and records every response with an HTTP status of 400 or greater, including its exact URL.

## 2026-08-11 — Separate portable CI rendering from the final journal font

**Decision.** Prefer the complete Times New Roman, Verdana, and Andale Mono font set when available, but fall back to ReportLab's standard Times, Helvetica, and Courier PDF fonts on clean systems. Exercise the fallback explicitly in tests.

**Reason.** The renderers previously depended on macOS-only absolute font paths, causing both PDF structure and reproduction tests to fail on Linux GitHub Actions. ReportLab's PDF base fonts require no operating-system font installation and make the computational checks portable.

**Limit.** The portable fallback verifies rendering and document structure; it is not evidence that the journal's Times New Roman requirement is met. The canonical Ecology proof must still be rendered and visually checked on a system with Times New Roman.

## 2026-08-11 — Put better human science before agent diagnostics

**Decision.** Center the current manuscript on the claim that FAIR and CARE improve human scientific practice, while agents cannot be assumed to inherit those practices, obligations, or authorities. Agentic workflows must therefore encode them explicitly.

**Reason.** Treating AI primarily as a stress test makes the agent the organizing subject. The stronger argument begins with the quality and legitimacy of science, then asks how agents can participate without bypassing its methods, evidence, provenance, governance, and accountable judgment.

**Implementation.** Reframe the abstract, opening, workflow section, figure caption, conclusion, repository metadata, PDF cover, and website hero. Preserve agent failure or refusal as a useful secondary diagnostic. Keep the reviewed citation-bearing paragraphs unchanged unless their sources are reread and their claim reviews renewed.

## 2026-08-11 — Treat the Ecology PDF as a formatting proof

**Decision.** Preserve the journal-adapted PDF separately at `output/pdf/fair_care_agentic_science_ecology.pdf` and label it a formatting proof rather than a submission-ready Main Document.

**Reason.** Ecology prefers Word and permits a PDF Main Document only for manuscripts prepared in LaTeX with the full source bundle. This repository currently renders Markdown with ReportLab. The proof applies the journal's visible page rules without misrepresenting its file format.

**Limits.** Perspective invitation/proposal status, author declarations, funding, a finished Figure 1, reference copyediting, an archival DOI, and the final Word or LaTeX package remain human/editorial work.

## 2026-08-11 — Apply the manuscript rules to this repository

**Decision.** Treat the manuscript project itself as the first implementation case for its eight FAIR + CARE rules.

**Reason.** A project that recommends explicit, reproducible, testable, and governed repositories should expose the same evidence and boundaries in its own repository.

**Implementation.** Keep `project.json` as the machine-readable project record; make the current manuscript PDF and citation audit the named reproducible outputs; place human-readable and executable governance in `governance/`; record consequential runs in `provenance/`; and test the implementation in CI.

**Limits.** The repository contains no research data and cannot self-create a legitimate community governance relationship. A license, archival release, DOI, and external scholarly or rights-holder reviews remain human decisions and are release blockers rather than facts agents may invent.
