#!/usr/bin/env python3
"""Reproduce the current manuscript PDF and citation-audit report."""

from __future__ import annotations

import argparse
import hashlib
import importlib.metadata
import json
import os
import platform
import subprocess
import sys
from datetime import date
from pathlib import Path

from render_manuscript_pdf import PORTABLE_FONT_ENV, selected_font_mode


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "manuscript" / "fair_care_agentic_science_v2.md"
REGISTRY = ROOT / "manuscript" / "citation_audit_v2.json"


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def run(command: list[str]) -> None:
    subprocess.run(command, cwd=ROOT, check=True)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=ROOT / "results" / "reproduction",
        help="Destination for derived outputs (default: results/reproduction)",
    )
    parser.add_argument(
        "--online",
        action="store_true",
        help="Recheck authoritative public source metadata using approved services.",
    )
    args = parser.parse_args()
    output_dir = args.output_dir.resolve()
    output_dir.mkdir(parents=True, exist_ok=True)

    audit_report = output_dir / "manuscript-audit-v2.md"
    pdf_output = output_dir / "fair_care_agentic_science_v2.pdf"
    ecology_pdf_output = output_dir / "fair_care_agentic_science_ecology.pdf"
    manifest_output = output_dir / "reproduction-manifest.json"

    run([sys.executable, "scripts/build_figures.py", "--check"])
    run([sys.executable, "scripts/manuscript_quality_check.py", "--source", str(SOURCE.relative_to(ROOT))])
    run([sys.executable, "scripts/build_figures.py"])

    audit_command = [
        sys.executable,
        "scripts/manuscript_audit.py",
        "--manuscript",
        str(SOURCE.relative_to(ROOT)),
        "--registry",
        str(REGISTRY.relative_to(ROOT)),
        "--check",
        "--markdown-report",
        str(audit_report),
    ]
    if args.online:
        audit_command.append("--online")
    run(audit_command)

    render_command = [
        sys.executable,
        "scripts/render_manuscript_pdf.py",
        "--source",
        str(SOURCE.relative_to(ROOT)),
        "--output",
        str(pdf_output),
    ]
    run(render_command)

    ecology_render_command = [
        sys.executable,
        "scripts/render_ecology_manuscript_pdf.py",
        "--source",
        str(SOURCE.relative_to(ROOT)),
        "--metadata",
        "manuscript/ecology_submission.json",
        "--output",
        str(ecology_pdf_output),
    ]
    run(ecology_render_command)

    for rendered_pdf in (pdf_output, ecology_pdf_output):
        if rendered_pdf.stat().st_size < 10_000 or not rendered_pdf.read_bytes().startswith(b"%PDF"):
            raise RuntimeError(f"Rendered manuscript is not a non-empty PDF: {rendered_pdf}")

    run(
        [
            sys.executable,
            "scripts/manuscript_quality_check.py",
            "--source",
            str(SOURCE.relative_to(ROOT)),
            "--pdf",
            str(pdf_output),
            "--pdf",
            str(ecology_pdf_output),
        ]
    )

    manifest = {
        "schema_version": "1.0",
        "date": date.today().isoformat(),
        "goal": "Reproduce the current second-draft manuscript PDF and citation-audit report.",
        "command": " ".join(sys.argv),
        "online_source_verification": args.online,
        "environment": {
            "python": platform.python_version(),
            "implementation": platform.python_implementation(),
            "platform": platform.platform(),
            "reportlab": importlib.metadata.version("reportlab"),
            "manuscript_font_mode": selected_font_mode(),
            "portable_font_mode_forced": os.environ.get(PORTABLE_FONT_ENV) == "1",
        },
        "inputs": {
            str(SOURCE.relative_to(ROOT)): sha256(SOURCE),
            str(REGISTRY.relative_to(ROOT)): sha256(REGISTRY),
            "scripts/manuscript_audit.py": sha256(ROOT / "scripts" / "manuscript_audit.py"),
            "scripts/render_manuscript_pdf.py": sha256(ROOT / "scripts" / "render_manuscript_pdf.py"),
            "scripts/build_figures.py": sha256(ROOT / "scripts" / "build_figures.py"),
            "scripts/manuscript_quality_check.py": sha256(ROOT / "scripts" / "manuscript_quality_check.py"),
            "manuscript/figures/figure1_workflow.py": sha256(
                ROOT / "manuscript" / "figures" / "figure1_workflow.py"
            ),
            "manuscript/figures/figure1_workflow.svg": sha256(
                ROOT / "manuscript" / "figures" / "figure1_workflow.svg"
            ),
            "manuscript/ecology_submission.json": sha256(ROOT / "manuscript" / "ecology_submission.json"),
            "scripts/render_ecology_manuscript_pdf.py": sha256(
                ROOT / "scripts" / "render_ecology_manuscript_pdf.py"
            ),
        },
        "outputs": {
            pdf_output.name: sha256(pdf_output),
            ecology_pdf_output.name: sha256(ecology_pdf_output),
            audit_report.name: sha256(audit_report),
        },
        "governance": {
            "data_class": "public_repository_content",
            "external_model_used": False,
            "publication_authorized": False,
            "note": "Local derived output only; publication remains human-gated.",
        },
    }
    manifest_output.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote reproducible outputs to {output_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
