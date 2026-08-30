---
title: Ecology author guidelines
description: Current submission and formatting requirements for adapting the FAIR + CARE manuscript to Ecology.
---

# Ecology author guidelines

This is a project-specific working summary of the official instructions for *Ecology*, published by the Ecological Society of America (ESA) through Wiley. It was checked on 11 August 2026 against the [Ecology Author Guidelines](https://esajournals.onlinelibrary.wiley.com/hub/journal/19399170/author-guidelines), which identify themselves as revised April 2026, and the [ESA Open Research Policy](https://esa.org/publications/data-policy/). Authors must recheck the live instructions immediately before submission because the journal can revise them.

## Intended submission type and editorial fit

The manuscript currently describes itself as a Perspective. Ecology limits a Perspective to 30 manuscript pages, requires an abstract of no more than 350 words and keywords, and treats the category as generally invited. The journal says unsolicited proposals may be sent to the Editor-in-Chief. It describes Perspectives as synthetic overviews, critical commentaries, or historical perspectives, generally written by an eminent ecologist; coauthored papers are generally not considered appropriate.

This creates an editorial gate, not a formatting problem: **do not submit the manuscript as a Perspective until an invitation exists or the Editor-in-Chief accepts a proposal.** If that route is unavailable, the author should ask the journal which submission type is appropriate rather than relabeling the paper without editorial guidance.

## Main-document order

Ecology specifies the following order:

1. Title page: journal, manuscript type, title, authors, affiliations, corresponding author and email, Open Research statement, and keywords.
2. Abstract on a new page.
3. Main text.
4. Acknowledgments.
5. Author Contributions, when supplied.
6. Conflict of Interest Statement.
7. References.
8. Boxes, if any.
9. Tables, each beginning on a new page with its caption above and notes below.
10. Figure captions grouped in one section beginning on a new page.
11. Figures, each on its own page or uploaded separately.
12. Supporting information as separate files.

## Page and text formatting

| Requirement | Ecology rule | Project implementation |
| --- | --- | --- |
| Page size | US Letter, portrait | Implemented in the Ecology-formatted PDF. |
| Margins | 1 inch on every side | Implemented. |
| Main font | 12-point Times New Roman | Implemented in the canonical proof with embedded Times New Roman. Clean CI systems use a portable Times fallback for structural testing only. |
| Spacing | Double-space abstract, body, references, captions, and table notes | Implemented. Table cells may remain single-spaced at 10 points. |
| Alignment | Left aligned; not justified | Implemented. |
| Line numbers | Continuous from the first post-title-page manuscript line through References | Implemented as continuous margin line numbers on the text and reference pages. |
| Page numbers | Every page, beginning with the title page | Implemented. |
| Page limit | Perspective: 30 pages, including title page, text, references, tables, captions, and figures | Tested after every Ecology PDF render. Supporting information is excluded. |

The page limit applies to the formatted manuscript, not only the main-text word count.

## Title page and abstract

- Title: no more than 120 characters including spaces; sentence case; no period; no dash as a phrase separator; no more than one colon; avoid acronyms and uncommon abbreviations unless well established.
- Author list and order must match ScholarOne and supporting files exactly.
- Affiliations need department or unit, institution, city, state/province, and country. One corresponding author and email must be identified.
- The Open Research statement belongs on the title page and must also be entered in ScholarOne.
- Perspective abstract: required and no more than 350 words. It must contain no citations or URLs.
- Keywords: six to 12, alphabetized and separated by semicolons.

The Ecology-formatted title is within the 120-character limit and the current abstract is 222 words. The eight keywords are alphabetized.

## Open research, AI, and declarations

ESA requires underlying data and novel analytical code to be permanently archived upon acceptance, subject to narrow and disclosed exceptions. For theoretical, review, opinion, and editorial work, the policy supplies the statement that empirical data were not used. The current title page adds the repository and explains that a permanent archival identifier is still pending. GitHub may support review, but ESA's policy says a Zenodo DOI or another permanent repository identifier is needed for final GitHub material.

ESA does not permit AI systems to be authors. Material AI use in writing, figures, data collection, or analysis must be disclosed where it occurred, in the Acknowledgments, and in the submission form; authors remain responsible. The Ecology PDF includes an AI-assistance disclosure in Acknowledgments.

The author must personally verify the author list, affiliations, Author Contributions, funding acknowledgments, Open Research statement, and Conflict of Interest Statement. The repository does not infer a conflict-of-interest declaration on the author's behalf.

## References, tables, and figures

- Every in-text citation must have a matching reference and vice versa; references must be complete and point to permanently archived material.
- The journal points authors to the Wiley style manual's author-date in-text guidance and Chicago reference style; production applies final styling. The current references are complete enough for identity checking but still require a final Ecology/Chicago copyedit.
- Tables must be editable, fit portrait orientation, contain no colors, shading, or graphics, and begin on separate pages after References. Captions go above the table. Table body text may be 10-point Times New Roman and single-spaced.
- Figure captions belong together after the tables and before figures. Figures use Arabic numbers, each begins on a separate page, and all panels of a figure must fit together.
- Figures should generally be 300-600 dpi, use colorblind-friendly design, contain 6-10 point text at publication size, and fit within 18 cm by 22 cm. Single-column figures should be about 8.5 cm wide when practical.
- Figure 1 is generated from editable vector source in `manuscript/figures/figure1_workflow.py`; its SVG derivative is checked in continuous integration.

## File-format limitation

Ecology prefers a Word `.doc` or `.docx` main document. It permits a PDF main document only for a manuscript prepared in LaTeX, accompanied by the complete LaTeX source bundle and fonts without T3 fonts. The project currently creates the PDF from version-controlled Markdown with ReportLab, not LaTeX. Accordingly:

- `output/pdf/fair_care_agentic_science_ecology.pdf` demonstrates the required page design and review layout;
- clean-infrastructure test renders may substitute ReportLab's portable Times base font when Times New Roman is unavailable, but that fallback is not the final journal proof;
- it should not be uploaded as the Main Document under the PDF/LaTeX exception; and
- the actual submission should be exported to a carefully checked Word document or rebuilt as a genuine LaTeX source bundle.

## Submission-readiness checklist

| Item | Current status |
| --- | --- |
| Perspective invitation or accepted proposal | **Blocked: author/editor action required.** |
| Title length and sentence case | Pass; acronym acceptability should be confirmed. |
| Author, affiliations, ORCIDs, and corresponding email | Present from the author-provided 30 August 2026 draft; both authors must confirm. |
| Abstract and keywords | Pass. |
| Letter, margins, font, spacing, alignment, page and line numbers | Pass in formatting proof. |
| Required order | Pass in formatting proof. |
| Open Research statement | Drafted; archive/DOI language requires author confirmation. |
| AI disclosure | Included; author must confirm completeness. |
| Acknowledgments and funding | AI disclosure included; funding acknowledgment still requires author input. |
| Author Contributions | Drafted; author confirmation required. |
| Conflict of Interest Statement | **Blocked: author declaration required.** |
| Reference style and completeness | Citation audit passes; final Ecology/Chicago copyedit remains. |
| Table placement and style | Pass. |
| Finished Figure 1 | Present as editable vector source; author approval required. |
| Supporting Information | Present as editable Markdown, a derived PDF, and a nine-source citation audit; author approval and final journal upload checks remain required. |
| Allowed Main Document format | **Blocked: create Word or a genuine LaTeX package.** |
| Licenses and archival release | Blocked in the repository release audit. |
| External scholarly and Indigenous data sovereignty review | Required before submission by the project's governance policy. |

## Other policies to check before submission

Authors must review the ESA Code of Ethics, permissions rules, preprint policy, and any legally protected species or animal welfare certifications that apply. Previously published figures, tables, or substantial text may require permission. Ecology currently lists page charges for non-open-access papers; consult the live fee section before budgeting because charges can change.

## Authoritative sources

- [Ecology Author Guidelines, revised April 2026](https://esajournals.onlinelibrary.wiley.com/hub/journal/19399170/author-guidelines)
- [ESA Open Research Policy](https://esa.org/publications/data-policy/)
- [ESA Manuscript Preparation Guide, last modified 19 March 2025](https://www.esa.org/wp-content/uploads/2022/05/ESA-Manuscript-Preparation-Guide.pdf)

For editorial questions, the official guidelines direct authors to `esajournals@esa.org`.
