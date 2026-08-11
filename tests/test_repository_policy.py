from __future__ import annotations

import json
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from policy_check import decision_for, load_policy  # noqa: E402


class RepositoryPolicyTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.policy = load_policy()

    def test_safe_local_work_is_allowed(self) -> None:
        self.assertEqual(decision_for("read_public_repository", self.policy), "allowed")
        self.assertEqual(decision_for("run_documented_local_tests", self.policy), "allowed")

    def test_publication_requires_human_approval(self) -> None:
        self.assertEqual(decision_for("publish_website", self.policy), "human_approval")
        self.assertEqual(
            decision_for("publish_or_release_manuscript", self.policy), "human_approval"
        )
        self.assertEqual(decision_for("publish_without_review", self.policy), "prohibited")

    def test_sensitive_external_transfer_is_prohibited(self) -> None:
        self.assertEqual(
            decision_for("send_governed_data_to_external_model", self.policy), "prohibited"
        )
        self.assertEqual(
            decision_for("record_secret_or_sensitive_content_in_public_log", self.policy),
            "prohibited",
        )

    def test_unknown_actions_default_to_prohibited(self) -> None:
        self.assertEqual(decision_for("unlisted_new_capability", self.policy), "prohibited")

    def test_citation_shortcuts_are_prohibited(self) -> None:
        self.assertEqual(
            decision_for("fabricate_or_misrepresent_citation", self.policy), "prohibited"
        )
        self.assertEqual(
            decision_for("refresh_citation_fingerprint_without_source_review", self.policy),
            "prohibited",
        )

    def test_repository_audit_passes_operational_controls(self) -> None:
        result = subprocess.run(
            [sys.executable, "scripts/repository_audit.py"],
            cwd=ROOT,
            capture_output=True,
            text=True,
        )
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("Operational repository controls: PASS", result.stdout)

    def test_release_readiness_reports_blockers(self) -> None:
        result = subprocess.run(
            [sys.executable, "scripts/repository_audit.py", "--release"],
            cwd=ROOT,
            capture_output=True,
            text=True,
        )
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("release blocker", result.stdout)

    def test_consequential_run_record_has_reconstructable_fields(self) -> None:
        record_path = ROOT / "provenance" / "records" / "2026-08-11-repository-alignment.json"
        record = json.loads(record_path.read_text(encoding="utf-8"))
        for field in (
            "goal",
            "responsible_human",
            "actor",
            "compute",
            "instructions",
            "inputs",
            "outputs",
            "evaluations",
            "human_review",
        ):
            self.assertTrue(record[field], field)
        self.assertFalse(record["human_review"]["publication_authorized"])

    def test_primary_output_reproduces_in_clean_directory(self) -> None:
        try:
            __import__("reportlab")
        except ImportError:
            self.skipTest("ReportLab is installed by requirements-pdf.txt in CI")
        with tempfile.TemporaryDirectory() as directory:
            result = subprocess.run(
                [sys.executable, "scripts/reproduce.py", "--output-dir", directory],
                cwd=ROOT,
                capture_output=True,
                text=True,
                env={**os.environ, "MANUSCRIPT_FORCE_PORTABLE_FONTS": "1"},
            )
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
            output = Path(directory)
            self.assertGreater((output / "fair_care_agentic_science_v2.pdf").stat().st_size, 10_000)
            self.assertGreater(
                (output / "fair_care_agentic_science_ecology.pdf").stat().st_size,
                10_000,
            )
            self.assertTrue((output / "manuscript-audit-v2.md").is_file())
            self.assertTrue((output / "reproduction-manifest.json").is_file())
            manifest = json.loads(
                (output / "reproduction-manifest.json").read_text(encoding="utf-8")
            )
            self.assertEqual(
                manifest["environment"]["manuscript_font_mode"],
                "portable PDF base-font fallback",
            )
            self.assertTrue(manifest["environment"]["portable_font_mode_forced"])


if __name__ == "__main__":
    unittest.main()
