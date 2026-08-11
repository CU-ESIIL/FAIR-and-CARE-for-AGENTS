# AGENTS.md

## Core Operating Contract
- Treat this repository as the source of truth.
- Treat the website as a rendered view of repository state.
- Prefer small, additive, traceable edits.
- Keep documentation synchronized with code and project structure.
- Keep the repository minimalist by default.

## Default Workflow
- Inspect repository structure before editing.
- Make the smallest diff that solves the request.
- Update related docs when behavior, workflows, or outputs change.
- Update changelog, dev log, or equivalent history files for meaningful changes.
- Update `PROMPT_LOG.md` for every user prompt handled in this repository.
- Preserve existing structure and historical context.
- Do not perform destructive rewrites unless explicitly requested.

## Prompt Logging
- Append one entry to `PROMPT_LOG.md` for every user prompt, including follow-up prompts that arrive during ongoing work.
- Reproduce the user's prompt verbatim, preserving its spelling, punctuation, and formatting as closely as Markdown allows.
- Do not include system or developer instructions, private reasoning, or tool output in the prompt log.
- Summarize what the agent did in response, including files changed and checks run. If no repository action was taken, state that explicitly.
- Create the entry when work begins and complete its response summary before sending the final response to the user.
- Keep prior entries append-only. Edit an earlier entry only to correct an inaccurate record of the current task.

## Documentation and Website Policy
- Treat `docs/` as project-level documentation and website source.
- Update docs whenever code, workflows, or outputs change.
- Amend existing docs when possible; do not replace whole files without need.
- Preserve navigation, readability, and consistency in website changes.
- Keep default website behavior clean and minimal unless the user asks for more expressive design.

## Testing Policy
- Assume `tests/` may exist before a full testing framework is defined.
- Do not invent domain-specific tests when expected behavior is unclear.
- Add the smallest meaningful tests when behavior is known.
- Prefer early-stage checks such as smoke tests, import tests, CLI tests, schema checks, or example-based checks.
- Run `mkdocs build --strict` and `npm run test:site` after website changes.
- Run `python3 -m unittest discover -s tests -p "test_*.py"` and `python3 scripts/manuscript_audit.py --check` after manuscript or citation changes.
- For Draft 2, pass `--manuscript manuscript/fair_care_agentic_science_v2.md --registry manuscript/citation_audit_v2.json` to the manuscript audit.
- Add `--online` to the manuscript audit when network access is available so authoritative source records are rechecked.
- Register every in-text citation and bibliography entry in the citation-audit registry associated with that manuscript draft.
- Treat claim review as scholarly judgment: read the source, document how it supports the cited paragraph, and update the paragraph fingerprint only after review. Never refresh fingerprints mechanically to silence CI.
- If tests are deferred, document the gap; do not imply coverage that does not exist.

## Package and Structure Separation Policy
- Keep website structure and package structure clearly separated.
- Do not automatically repurpose `docs/` for package-native docs or build artifacts.
- For Python packaging requests, prefer standard Python layout, typically `src/`.
- For R packaging requests, follow standard R conventions (`R/`, `man/`, `DESCRIPTION`, `NAMESPACE`, optional `vignettes/`).
- For other ecosystems, follow ecosystem conventions.
- If structural conflicts arise, choose a durable long-term structure and document the decision.

## Data Discovery and Data Use Policy
- Prefer open and FAIR data when possible.
- Prefer streaming or lazy-access workflows over bulk downloads when feasible.
- Use standards-based discovery systems (for example STAC) when relevant.
- When relevant, consider streaming-friendly tooling such as xarray, zarr, GDAL, rasterio, pystac-client, stackstac, gdalcubes, terra, stars, cubo, or equivalent tools.
- When introducing data, document source, access method, format, license, and citation requirements.
- Do not silently ingest external data into the project.

## Data Sovereignty and Intellectual Property Policy
- Consider licensing, copyright, privacy, Indigenous data sovereignty, and related restrictions for all data and content.
- If rights or permissions are unclear, document uncertainty and avoid assuming open reuse.

## Design and Usability Policy
- Keep the website simple, readable, and easy to extend by default.
- When design improvements are requested, prioritize system-level improvements (layout, spacing, typography, hierarchy, navigation, consistency).
- Do not use scattered one-off styling hacks.
- If direct site inspection is possible, verify readability, navigation, link integrity, and that docs still reflect repository state.

## Decision Logging
- Reflect meaningful structural, architectural, documentation, data-source, or design decisions in changelog, dev log, roadmap, or equivalent history files when appropriate.
