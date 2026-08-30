from __future__ import annotations

import json
import os
import re
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from pypdf import PdfReader


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "manuscript" / "fair_care_agentic_science_v2.md"
METADATA = ROOT / "manuscript" / "ecology_submission.json"
SUBMISSION_TODO = ROOT / "manuscript" / "TODO_BEFORE_SUBMISSION.md"


def abstract_text() -> str:
    manuscript = SOURCE.read_text(encoding="utf-8")
    abstract = manuscript.split("## Abstract", 1)[1].split("## 1.", 1)[0]
    abstract = abstract.split("**Keywords:**", 1)[0]
    return re.sub(r"[*_`#]", "", abstract).strip()


class EcologySubmissionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.metadata = json.loads(METADATA.read_text(encoding="utf-8"))

    def test_title_abstract_and_keywords_meet_perspective_limits(self) -> None:
        self.assertLessEqual(len(self.metadata["title"]), 120)
        abstract = abstract_text()
        self.assertLessEqual(len(re.findall(r"\b[\w'-]+\b", abstract)), 350)
        self.assertNotRegex(abstract, r"https?://")
        self.assertNotRegex(abstract, r"\([A-Z][A-Za-z-]+ et al\.,? \d{4}\)")
        keywords = self.metadata["keywords"]
        self.assertGreaterEqual(len(keywords), 6)
        self.assertLessEqual(len(keywords), 12)
        self.assertEqual(keywords, sorted(keywords, key=str.casefold))

    def test_submission_blockers_are_not_silently_filled(self) -> None:
        self.assertIn("unconfirmed", self.metadata["invitation_status"])
        self.assertEqual(self.metadata["conflict_of_interest"], "")
        self.assertEqual(self.metadata["author_contributions"], "")
        self.assertIn("generated reproducibly", self.metadata["figure_status"])
        self.assertIn("Word or a genuine LaTeX package", self.metadata["main_document_format_status"])
        todo = SUBMISSION_TODO.read_text(encoding="utf-8")
        self.assertIn("## Required before submission", todo)
        self.assertIn("## Optional strengthening", todo)
        self.assertIn("## Author confirmation needed", todo)
        self.assertIn("conflict-of-interest", todo)

    def test_ecology_pdf_structure_and_page_limit(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            pdf = Path(directory) / "ecology.pdf"
            result = subprocess.run(
                [
                    sys.executable,
                    "scripts/render_ecology_manuscript_pdf.py",
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
            self.assertLessEqual(len(reader.pages), 30)
            self.assertGreater(len(reader.pages), 3)
            for page in reader.pages:
                self.assertEqual(tuple(float(v) for v in page.mediabox[2:]), (612.0, 792.0))

            title_page = reader.pages[0].extract_text()
            self.assertIn("Ecology", title_page)
            self.assertIn("Perspective", title_page)
            self.assertIn(
                self.metadata["title"],
                re.sub(r"\s+", " ", title_page),
            )
            self.assertIn("Open Research statement", title_page)
            self.assertIn("Key words", title_page)

            review_text = "\n".join(page.extract_text() for page in reader.pages[1:-2])
            self.assertIn("Abstract", reader.pages[1].extract_text())
            self.assertIn("Acknowledgments", review_text)
            self.assertNotIn("Author Contributions", review_text)
            self.assertNotIn("Conflict of Interest Statement", review_text)
            self.assertIn("References", review_text)

            self.assertIn("Table 1.", reader.pages[-2].extract_text())
            self.assertIn("Figure captions", reader.pages[-1].extract_text())
            self.assertIn("PERMISSION BOUNDARY: WHAT THE COMPUTER MAY DO", reader.pages[-1].extract_text())
            full_text = "\n".join(page.extract_text() or "" for page in reader.pages)
            self.assertNotRegex(
                full_text,
                r"(?i)\b(?:TODO|TBD|FIXME|citation needed|must be confirmed|before submission)\b",
            )


if __name__ == "__main__":
    unittest.main()
