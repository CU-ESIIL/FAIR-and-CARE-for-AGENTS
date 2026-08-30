# Canonical analysis and reproduction workflow

For this manuscript project, the named reproducible result is the current second-draft PDF, its Ecology formatting proof, the Supporting Information PDF, and their citation-integrity and word-count reports. The canonical sources are the Markdown manuscript and supplement, Ecology submission metadata, and their citation-review registries; the PDFs and reports are derived products.

From a clean Python 3.12 environment:

```bash
python3 -m pip install -r requirements-pdf.txt
python3 scripts/reproduce.py --output-dir results/reproduction
```

Success means:

- the Draft 2 citation audit passes without a changed reviewed paragraph, missing source, bibliography mismatch, or excess unresolved marker;
- a readable, non-empty PDF is generated from the canonical Markdown source;
- an Ecology formatting proof is generated with the documented submission metadata and remains within its tested 30-page limit;
- a readable Supporting Information PDF is generated from its editable Markdown source and its nine-source citation audit passes;
- the manifest records input/output SHA-256 hashes, Python and ReportLab versions, the command, and whether online source identity checks were requested; and
- no external model, governed data, or unapproved publication action is used.

Add `--online` to recheck authoritative public citation records. That optional step sends only public citation identifiers and metadata to the services listed in `governance/policy.json`.
