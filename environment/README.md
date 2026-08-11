# Reproducible environment

The project uses two small, separated environments:

- `requirements.txt` pins the MkDocs website build.
- `requirements-pdf.txt` pins PDF generation.
- `package-lock.json` pins Playwright and its Node dependency graph.

Use Python 3.12 and a current Node.js LTS release, as CI does. Create a clean environment, install both Python requirement files, run `npm ci`, and install Playwright Chromium only when browser checks are needed.

The primary-output reproduction command is documented in `analysis/README.md`. CI performs the same workflow on clean GitHub-hosted infrastructure. No model call or governed data is required to reproduce the manuscript PDF or citation-audit report.

PDF generation prefers the complete local manuscript font set. When those macOS fonts are unavailable, the renderers use ReportLab's portable PDF base fonts so clean Linux builds remain executable. Run with `MANUSCRIPT_FORCE_PORTABLE_FONTS=1` to test that path explicitly; the reproduction manifest records which mode was used. The portable mode is for structural verification and does not replace the required-font review of the final journal proof.
