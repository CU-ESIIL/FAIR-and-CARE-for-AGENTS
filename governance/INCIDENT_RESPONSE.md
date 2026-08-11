# Incident response and correction

## Scope

An incident includes a fabricated or materially misrepresented citation, unreviewed publication, disclosure of sensitive information, unapproved external transfer, loss of provenance, bypassed approval, misleading FAIR/CARE claim, or failure of a repository control.

## Procedure

1. **Stop and preserve.** Stop the affected workflow and further publication. Preserve non-sensitive logs, commit identifiers, outputs, and the relevant run record. Do not copy governed material into a public report.
2. **Contain.** Revoke exposed credentials, disable the affected workflow or endpoint, restrict the artifact, or revert the public view as appropriate. Do not rewrite Git history unless the owner determines that secret removal requires it.
3. **Notify.** Notify the responsible human in `project.json` and any legitimate data authority or affected party. Use a private channel for sensitive facts.
4. **Assess.** Identify affected artifacts and people, the permission or test that failed, the scientific consequence, and whether published claims require correction or withdrawal.
5. **Correct and recover.** Amend, withdraw, or version the affected output; add a regression or governance test; update policy and documentation; and restore service only after human authorization.
6. **Record.** Add a non-sensitive incident record or decision-log entry describing what happened, the response, residual risk, and the approving human. Respect retention, confidentiality, and community decisions about what must not be public.

The owner prioritizes risks to people, communities, governed knowledge, sensitive species or locations, scientific integrity, and downstream users over preserving an automated workflow.
