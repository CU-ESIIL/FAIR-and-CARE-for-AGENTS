from __future__ import annotations

import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

import yaml

from scripts.manuscript_quality_check import audit_pdf, audit_source
from scripts.render_manuscript_pdf import render


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "manuscript" / "fair_care_agentic_science_v2.md"
TEMPLATE = ROOT / "templates" / "agent-workflow-spec.yml"
EXAMPLE = ROOT / "examples" / "habitat-assessment" / "specification.yml"


class ManuscriptQualityTests(unittest.TestCase):
    def test_visible_manuscript_has_no_submission_placeholders(self) -> None:
        self.assertEqual(audit_source(SOURCE), [])

    def test_figure_source_and_svg_are_reproducible(self) -> None:
        result = subprocess.run(
            [sys.executable, "scripts/build_figures.py", "--check"],
            cwd=ROOT,
            capture_output=True,
            text=True,
        )
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_reading_pdf_contains_vector_figure_and_no_placeholders(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            pdf = Path(directory) / "manuscript.pdf"
            render(SOURCE, pdf)
            self.assertEqual(audit_pdf(pdf), [])
            from pypdf import PdfReader

            text = "\n".join(page.extract_text() or "" for page in PdfReader(str(pdf)).pages)
            self.assertIn("PERMISSION BOUNDARY: WHAT THE COMPUTER MAY DO", text)

    def test_template_and_synthetic_example_have_the_core_sections(self) -> None:
        template = yaml.safe_load(TEMPLATE.read_text(encoding="utf-8"))
        example = yaml.safe_load(EXAMPLE.read_text(encoding="utf-8"))
        for document in (template, example):
            self.assertTrue({"goal", "instructions", "evaluation", "record", "governance_boundary"} <= set(document))
        self.assertEqual(example["instructions"]["external_services"], [])
        self.assertIn("synthetic://", EXAMPLE.read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
