# Provenance

Consequential work must leave a run record connecting the goal, instructions, inputs, agent or human actor, model/service, tools, compute context, outputs, evaluations, and human review. Use `run-record.template.json`, validate against `run-record.schema.json`, and place completed records in `records/`.

Record model and service versions when they are exposed. If a provider does not expose an exact version or configuration, say so rather than guessing. Do not put private reasoning, secrets, personal information, governed knowledge, or sensitive locations in a public record.

A run record marked `pending` may document work under review, but it does not authorize publication. Release records must be marked `approved` by the responsible human and satisfy `governance/policy.json`.
