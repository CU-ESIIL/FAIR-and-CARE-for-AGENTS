# Responsibility and human review

## Accountable owner

Ty Tuff is the repository and manuscript owner, based on the public repository history. The public route for questions, corrections, and contesting tests is the repository's GitHub issue tracker. Sensitive reports must follow `SECURITY.md`.

The owner may reassign a workflow only by updating `project.json`, this file, the governance policy, and the relevant provenance record. An agent, model provider, or CI system is never the accountable owner.

## Consequential workflows

| Workflow | Human owner | Agent authority | Required review |
| --- | --- | --- | --- |
| Manuscript claims and interpretation | Ty Tuff | May draft or propose | Owner reviews evidence and approves the text |
| Citation registry fingerprints | Ty Tuff | May identify invalidation; may not refresh mechanically | Owner or delegated source reviewer rereads the source and claim |
| Test and evaluation criteria | Ty Tuff | May propose and execute | Owner approves material criteria and documented limitations |
| Website publication | Ty Tuff | May build and test locally; may not deploy | Owner manually confirms the deployment workflow |
| Versioned release, DOI, and citation record | Ty Tuff | May prepare | Owner approves tag, release, license, and archival deposit |
| External data, model, or service use | Ty Tuff plus any legitimate data authority | Must stop unless listed in `policy.json` | Owner and all applicable rights-holders approve before transfer or use |
| Governance policy and harm register | Ty Tuff plus affected authorities where applicable | May propose | Human or community authority approves changes within its scope |

## Substantive review

Approval means the reviewer can inspect the relevant source, change, tests, limitations, and provenance. A green automated check is evidence, not authorization and not proof of scientific validity. Every public release must disclose material AI assistance using `AI_DISCLOSURE.md` and include a completed run record.

Git provides rollback for source changes. Deployed or released errors follow `INCIDENT_RESPONSE.md`; correction may require a site update, amended manuscript, retraction of an artifact, notification, or a new version rather than silent replacement.
