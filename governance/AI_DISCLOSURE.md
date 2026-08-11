# AI-assistance disclosure

Material AI assistance must be disclosed when it affects manuscript wording, scientific claims, citation selection or interpretation, software, evaluation criteria, governance controls, or a public release.

A disclosure should state:

- the model or service and version when exposed;
- the task and consequential instructions;
- the inputs and tools the system was allowed to use;
- the outputs or files materially affected;
- the automated and human evaluations performed;
- the responsible human who accepted, revised, or rejected the result; and
- important limits, including model/version information that the service did not expose.

`PROMPT_LOG.md` provides request-level traceability. A record conforming to `provenance/run-record.schema.json` provides run-level evidence for consequential work. Neither record may include secrets, governed content, personal data, or sensitive ecological locations merely for completeness.
