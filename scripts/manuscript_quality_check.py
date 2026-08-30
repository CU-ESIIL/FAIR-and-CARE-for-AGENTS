#!/usr/bin/env python3
"""Reject drafting placeholders and missing assets in the visible manuscript."""

from __future__ import annotations

import argparse
import re
from pathlib import Path

from pypdf import PdfReader


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_SOURCE = ROOT / "manuscript" / "fair_care_agentic_science_v2.md"
FORBIDDEN = {
    "TODO": re.compile(r"\bTODO\b", re.IGNORECASE),
    "TBD": re.compile(r"\bTBD\b", re.IGNORECASE),
    "must be confirmed": re.compile(r"\bmust be confirmed\b", re.IGNORECASE),
    "to be supplied": re.compile(r"\bto be supplied\b", re.IGNORECASE),
    "before submission": re.compile(r"\bbefore submission\b", re.IGNORECASE),
    "author should": re.compile(r"\bauthor should\b", re.IGNORECASE),
    "authors should": re.compile(r"\bauthors should\b", re.IGNORECASE),
    "citation needed": re.compile(r"\bcitation needed\b", re.IGNORECASE),
    "XX": re.compile(r"\bXX\b"),
    "FIXME": re.compile(r"\bFIXME\b", re.IGNORECASE),
}


def forbidden_findings(text: str, label: str) -> list[str]:
    return [f"{label}: visible drafting placeholder {name!r}" for name, pattern in FORBIDDEN.items() if pattern.search(text)]


def audit_source(source: Path) -> list[str]:
    text = source.read_text(encoding="utf-8")
    errors = forbidden_findings(text, str(source.relative_to(ROOT)))
    if "GOAL → INSTRUCTIONS → EVALUATION → RECORD" not in text:
        errors.append("manuscript does not contain the canonical pre-delegation sequence")
    if "## Table 1" not in text or "**Table 1.**" not in text:
        errors.append("Table 1 is missing")
    image = re.search(r"!\[[^\]]*\]\(([^)]+\.svg)\)", text)
    if not image:
        errors.append("editable Figure 1 link is missing")
    else:
        asset = (source.parent / image.group(1)).resolve()
        if not asset.is_file():
            errors.append(f"Figure 1 SVG is missing: {asset}")
        if not asset.with_suffix(".py").is_file():
            errors.append(f"Figure 1 editable source is missing: {asset.with_suffix('.py')}")
    if re.search(r"\\(?:cite|ref)\{[^}]*\}|\?\?", text):
        errors.append("unresolved LaTeX citation/reference marker found")
    return errors


def audit_pdf(path: Path) -> list[str]:
    reader = PdfReader(str(path))
    text = "\n".join(page.extract_text() or "" for page in reader.pages)
    errors = forbidden_findings(text, str(path.relative_to(ROOT) if path.is_relative_to(ROOT) else path))
    if "GOAL" not in text or "EVALUATION" not in text or "RECORD" not in text:
        errors.append(f"{path}: canonical workflow is not extractable from the PDF")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path, default=DEFAULT_SOURCE)
    parser.add_argument("--pdf", type=Path, action="append", default=[])
    args = parser.parse_args()
    errors = audit_source(args.source.resolve())
    for pdf in args.pdf:
        errors.extend(audit_pdf(pdf.resolve()))
    if errors:
        print("# Manuscript quality check\nFAIL")
        for error in errors:
            print(f"- {error}")
        return 1
    print("# Manuscript quality check\nPASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
