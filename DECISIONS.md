# Decision log

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
