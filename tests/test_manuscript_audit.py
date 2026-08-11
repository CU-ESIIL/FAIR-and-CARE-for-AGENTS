import json
import tempfile
import unittest
from pathlib import Path

from scripts.manuscript_audit import DEFAULT_MANUSCRIPT, DEFAULT_REGISTRY, audit

ROOT = Path(__file__).resolve().parents[1]
V2_MANUSCRIPT = ROOT / "manuscript" / "fair_care_agentic_science_v2.md"
V2_REGISTRY = ROOT / "manuscript" / "citation_audit_v2.json"


class ManuscriptAuditTests(unittest.TestCase):
    def test_current_manuscript_passes_offline_integrity_checks(self):
        result = audit(DEFAULT_MANUSCRIPT, DEFAULT_REGISTRY)

        self.assertTrue(result.passed, result.errors)
        self.assertEqual(result.unique_citations, 8)
        self.assertEqual(result.references, 8)
        self.assertEqual(result.claim_reviews, 10)
        self.assertEqual(result.citation_needed, 6)
        self.assertGreater(dict(result.section_words)["Abstract"], 0)

    def test_second_draft_passes_offline_integrity_checks(self):
        result = audit(V2_MANUSCRIPT, V2_REGISTRY)

        self.assertTrue(result.passed, result.errors)
        self.assertEqual(result.unique_citations, 8)
        self.assertEqual(result.references, 8)
        self.assertEqual(result.claim_reviews, 8)
        self.assertEqual(result.citation_needed, 2)
        self.assertEqual(dict(result.section_words)["Abstract"], 206)

    def test_editing_a_cited_paragraph_expires_claim_review(self):
        manuscript = DEFAULT_MANUSCRIPT.read_text(encoding="utf-8")
        manuscript = manuscript.replace(
            "The original FAIR principles made machine actionability central",
            "The original FAIR principles made automated reuse central",
            1,
        )
        registry = json.loads(DEFAULT_REGISTRY.read_text(encoding="utf-8"))

        with tempfile.TemporaryDirectory() as directory:
            temporary = Path(directory)
            manuscript_path = temporary / "manuscript.md"
            registry_path = temporary / "citation_audit.json"
            manuscript_path.write_text(manuscript, encoding="utf-8")
            registry_path.write_text(json.dumps(registry), encoding="utf-8")

            result = audit(manuscript_path, registry_path)

        self.assertFalse(result.passed)
        self.assertTrue(
            any("cited paragraph changed" in error for error in result.errors),
            result.errors,
        )

    def test_editing_a_second_draft_cited_paragraph_expires_claim_review(self):
        manuscript = V2_MANUSCRIPT.read_text(encoding="utf-8")
        manuscript = manuscript.replace(
            "FAIR already makes machine actionability central",
            "FAIR already makes automated reuse central",
            1,
        )
        registry = json.loads(V2_REGISTRY.read_text(encoding="utf-8"))

        with tempfile.TemporaryDirectory() as directory:
            temporary = Path(directory)
            manuscript_path = temporary / "manuscript_v2.md"
            registry_path = temporary / "citation_audit_v2.json"
            manuscript_path.write_text(manuscript, encoding="utf-8")
            registry_path.write_text(json.dumps(registry), encoding="utf-8")

            result = audit(manuscript_path, registry_path)

        self.assertFalse(result.passed)
        self.assertTrue(
            any("cited paragraph changed" in error for error in result.errors),
            result.errors,
        )


if __name__ == "__main__":
    unittest.main()
