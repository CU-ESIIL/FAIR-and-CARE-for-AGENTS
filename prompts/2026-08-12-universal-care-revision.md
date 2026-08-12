# Agent task specification: universal CARE revision

## Goal

- Exact outcome: Revise the current manuscript so four CARE-informed questions about benefit, authority, accountability, and harm are proposed as baseline considerations for every scientific and agentic workflow, while accurately preserving CARE's origin and continuing purpose in Indigenous Data Governance. Conduct three independent panel reviews and revise again in response.
- Scientific claim or decision affected: The manuscript's intended scope for applying CARE beyond its originating context.
- Intended beneficiary: Environmental scientists, affected people and communities, research stewards, reviewers, and agent-workflow designers.
- Responsible human: Ty Tuff.

## Instructions

- Canonical inputs and versions: `manuscript/fair_care_agentic_science_v2.md`, `manuscript/citation_audit_v2.json`, Carroll et al. (2020), official CARE Principles materials, and the repository's governance records.
- Allowed tools, models, services, and compute: Owner-authorized local Codex workspace; read-only retrieval of public authoritative source pages; three independent agent review panels using only public repository content.
- Methods and degrees of freedom: Amend the abstract, framing, CARE section, matrix, implementation language, figure caption, conclusion, website, and metadata as needed. Preserve or renew citation fingerprints only after reviewing the cited source. Make the manuscript's universal extension explicit as the authors' normative proposal, not as the original intent of CARE's creators.
- Prohibited actions: Do not erase CARE's Indigenous origins; imply generic project governance supersedes Indigenous sovereignty or community-specific protocols; fabricate consensus; refresh a claim fingerprint without source review; publish or release the manuscript.
- Conditions requiring stop or human review: Any claim that purports to redefine CARE on behalf of its creators, any use of governed knowledge, or any publication action.

## Test

- Scientific acceptance evidence: A reader can distinguish (1) CARE's origin and specific force in Indigenous Data Governance, (2) the manuscript's proposal that every workflow undergo a four-question CARE-informed entry screen, and (3) the fact that the screen is not CARE compliance and cannot substitute for rights-holder authority.
- Computational acceptance evidence: Manuscript/citation audits, repository tests, strict website build, Playwright tests, and both PDF renders pass.
- Provenance acceptance evidence: Verbatim prompt log, saved three-panel review, change record, and structured consequential-run record.
- Governance acceptance evidence, including a valid refusal case: Review explicitly tests for appropriation, dilution, false equivalence, and self-certification. The workflow must stop rather than infer consent or authority for Indigenous or other governed data.

## Record

- Task or prompt record: This file and `PROMPT_LOG.md`.
- Required run manifest: `provenance/records/2026-08-12-universal-care-revision.json`.
- Outputs and canonical destination: Revised manuscript, citation registry, review record, synchronized website/docs/metadata, and regenerated PDFs.
- Human reviewer and approval required before publication: Ty Tuff plus the repository's required external scholarly and Indigenous Data Sovereignty review.
