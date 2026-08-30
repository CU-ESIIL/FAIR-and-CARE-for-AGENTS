from __future__ import annotations

import os
import re
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from pypdf import PdfReader


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "manuscript" / "supplementary_information.md"
REGISTRY = ROOT / "manuscript" / "supplement_citation_audit.json"


class SupplementTests(unittest.TestCase):
    def test_editable_source_contains_the_complete_guide(self) -> None:
        text = SOURCE.read_text(encoding="utf-8")
        for section in range(1, 11):
            self.assertRegex(text, rf"(?m)^## {section}\. ")
        for table in range(1, 7):
            self.assertIn(f"Table S{table}.", text)
        self.assertIn("general governance prompts in this document are not the CARE Principles", text)
        self.assertIn("does not report an empirical test of an agent", text)
        self.assertNotRegex(text, r"(?i)\b(?:TODO|TBD|FIXME|citation needed)\b")

    def test_supplement_citation_registry_passes(self) -> None:
        result = subprocess.run(
            [
                sys.executable,
                "scripts/manuscript_audit.py",
                "--manuscript",
                str(SOURCE.relative_to(ROOT)),
                "--registry",
                str(REGISTRY.relative_to(ROOT)),
                "--check",
            ],
            cwd=ROOT,
            capture_output=True,
            text=True,
        )
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("Unique cited sources | 9", result.stdout)
        self.assertIn("Bibliography entries | 9", result.stdout)
        self.assertIn("Claim-level reviews | 9", result.stdout)

    def test_supplement_pdf_renders_from_source(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            pdf = Path(directory) / "supplement.pdf"
            result = subprocess.run(
                [
                    sys.executable,
                    "scripts/render_manuscript_pdf.py",
                    "--source",
                    str(SOURCE.relative_to(ROOT)),
                    "--output",
                    str(pdf),
                ],
                cwd=ROOT,
                capture_output=True,
                text=True,
                env={**os.environ, "MANUSCRIPT_FORCE_PORTABLE_FONTS": "1"},
            )
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
            reader = PdfReader(str(pdf))
            self.assertGreaterEqual(len(reader.pages), 10)
            self.assertLessEqual(len(reader.pages), 20)
            full_text = "\n".join(page.extract_text() or "" for page in reader.pages)
            self.assertIn("SUPPORTING INFORMATION", reader.pages[0].extract_text())
            self.assertIn("Table S1.", full_text)
            self.assertIn("Table S6.", full_text)
            self.assertIn("What this guide can and cannot show", full_text)
            self.assertNotRegex(full_text, r"(?i)\b(?:TODO|TBD|FIXME|citation needed)\b")


if __name__ == "__main__":
    unittest.main()
