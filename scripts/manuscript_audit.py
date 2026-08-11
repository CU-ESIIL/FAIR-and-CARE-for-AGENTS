#!/usr/bin/env python3
"""Report manuscript metrics and enforce citation integrity.

The audit deliberately separates mechanical checks from scholarly judgment.
Online metadata checks establish that a registered source exists and matches its
basic bibliographic record. Claim-level review is represented by a fingerprint
of each cited paragraph plus a human-readable support note. When that paragraph
changes, the fingerprint no longer matches and review must be renewed.
"""

from __future__ import annotations

import argparse
import hashlib
import html
import json
import re
import sys
import time
import unicodedata
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import dataclass, field
from datetime import date
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_MANUSCRIPT = ROOT / "manuscript" / "fair_care_agentic_science.md"
DEFAULT_REGISTRY = ROOT / "manuscript" / "citation_audit.json"
WORD_RE = re.compile(r"\b[^\W_]+(?:[’'-][^\W_]+)*\b", re.UNICODE)
SECTION_RE = re.compile(r"^## (.+)$", re.MULTILINE)
PLACEHOLDER_RE = re.compile(r"\[CITATION NEEDED[^\]]*\]")
PARENTHETICAL_RE = re.compile(r"\(([^()]*\b(?:19|20)\d{2}[a-z]?[^()]*)\)")
CITATION_ITEM_RE = re.compile(r"^.+,\s*(?:19|20)\d{2}[a-z]?$", re.UNICODE)


@dataclass
class SourceResult:
    key: str
    status: str
    detail: str


@dataclass
class AuditResult:
    section_words: list[tuple[str, int]]
    citation_mentions: int
    unique_citations: int
    citation_needed: int
    references: int
    claim_reviews: int
    source_results: list[SourceResult] = field(default_factory=list)
    errors: list[str] = field(default_factory=list)

    @property
    def passed(self) -> bool:
        return not self.errors


def normalize_space(value: str) -> str:
    return " ".join(value.split())


def normalize_metadata(value: str) -> str:
    value = html.unescape(value)
    value = unicodedata.normalize("NFKD", value)
    value = "".join(character for character in value if not unicodedata.combining(character))
    return " ".join(re.findall(r"[a-z0-9]+", value.casefold()))


def markdown_escape(value: str) -> str:
    return value.replace("|", "\\|")


def paragraph_hash(paragraph: str) -> str:
    return hashlib.sha256(normalize_space(paragraph).encode("utf-8")).hexdigest()


def manuscript_body(text: str) -> str:
    marker = "\n## References\n"
    if marker not in text:
        raise ValueError("Manuscript must contain a level-two References section")
    return text.split(marker, 1)[0]


def markdown_paragraphs(text: str) -> list[str]:
    return [block.strip() for block in re.split(r"\n\s*\n", text) if block.strip()]


def section_word_counts(text: str) -> list[tuple[str, int]]:
    matches = list(SECTION_RE.finditer(text))
    counts: list[tuple[str, int]] = []
    for index, match in enumerate(matches):
        start = match.end()
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        content = text[start:end]
        content = re.sub(r"```.*?```", " ", content, flags=re.DOTALL)
        content = re.sub(r"<[^>]+>", " ", content)
        counts.append((match.group(1).strip(), len(WORD_RE.findall(content))))
    return counts


def extract_parenthetical_citations(body: str) -> list[str]:
    citations: list[str] = []
    for group in PARENTHETICAL_RE.findall(body):
        for item in group.split(";"):
            candidate = normalize_space(item.strip())
            if CITATION_ITEM_RE.match(candidate):
                citations.append(candidate)
    return citations


def bibliography_lines(text: str) -> list[str]:
    references = text.split("\n## References\n", 1)[1]
    return [line.strip() for line in references.splitlines() if line.startswith("- ")]


def load_registry(path: Path) -> dict[str, Any]:
    with path.open(encoding="utf-8") as stream:
        registry = json.load(stream)
    if registry.get("schema_version") != 1:
        raise ValueError("citation_audit.json must use schema_version 1")
    return registry


def request_json(url: str, attempts: int = 3) -> dict[str, Any]:
    request = urllib.request.Request(
        url,
        headers={
            "Accept": "application/json",
            "User-Agent": "FAIR-CARE-agentic-science-citation-audit/1.0 (+https://github.com/CU-ESIIL/FAIR-and-CARE-for-AGENTS)",
        },
    )
    last_error: Exception | None = None
    for attempt in range(attempts):
        try:
            with urllib.request.urlopen(request, timeout=20) as response:
                return json.load(response)
        except (OSError, urllib.error.URLError, json.JSONDecodeError) as error:
            last_error = error
            if attempt + 1 < attempts:
                time.sleep(2**attempt)
    raise RuntimeError(f"Unable to retrieve {url}: {last_error}")


def request_text(url: str, attempts: int = 3) -> str:
    request = urllib.request.Request(
        url,
        headers={
            "Accept": "text/html,application/xhtml+xml",
            "User-Agent": "FAIR-CARE-agentic-science-citation-audit/1.0 (+https://github.com/CU-ESIIL/FAIR-and-CARE-for-AGENTS)",
        },
    )
    last_error: Exception | None = None
    for attempt in range(attempts):
        try:
            with urllib.request.urlopen(request, timeout=20) as response:
                return response.read(512_000).decode("utf-8", errors="replace")
        except (OSError, urllib.error.URLError) as error:
            last_error = error
            if attempt + 1 < attempts:
                time.sleep(2**attempt)
    raise RuntimeError(f"Unable to retrieve {url}: {last_error}")


def crossref_year(message: dict[str, Any]) -> int | None:
    for field_name in ("published-print", "published-online", "issued", "created"):
        date_parts = message.get(field_name, {}).get("date-parts", [])
        if date_parts and date_parts[0]:
            return int(date_parts[0][0])
    return None


def verify_source_online(record: dict[str, Any]) -> SourceResult:
    key = record["key"]
    if "doi" in record:
        doi = record["doi"].lower()
        encoded_doi = urllib.parse.quote(doi, safe="")
        payload = request_json(f"https://api.crossref.org/works/{encoded_doi}")
        message = payload.get("message", {})
        actual_doi = str(message.get("DOI", "")).lower()
        actual_title = " ".join(message.get("title", []))
        actual_year = crossref_year(message)
        authors = message.get("author", [])
        actual_first_author = authors[0].get("family", "") if authors else ""
        mismatches = []
        if actual_doi != doi:
            mismatches.append(f"DOI returned as {actual_doi or 'missing'}")
        if normalize_metadata(actual_title) != normalize_metadata(record["title"]):
            mismatches.append(f"title returned as {actual_title or 'missing'}")
        if actual_year != record["year"]:
            mismatches.append(f"year returned as {actual_year or 'missing'}")
        if normalize_metadata(actual_first_author) != normalize_metadata(record["first_author"]):
            mismatches.append(f"first author returned as {actual_first_author or 'missing'}")
        if mismatches:
            return SourceResult(key, "failed", "; ".join(mismatches))
        return SourceResult(key, "verified", f"Crossref metadata matched DOI {doi}")

    url = record["url"]
    content = request_text(url)
    expected = record["page_contains"]
    if normalize_metadata(expected) not in normalize_metadata(content):
        return SourceResult(key, "failed", f"Page did not contain expected text: {expected}")
    return SourceResult(key, "verified", f"Authoritative page resolved: {url}")


def audit(manuscript_path: Path, registry_path: Path, online: bool = False) -> AuditResult:
    text = manuscript_path.read_text(encoding="utf-8")
    body = manuscript_body(text)
    registry = load_registry(registry_path)
    records = registry.get("sources", [])
    errors: list[str] = []

    keys = [record.get("key") for record in records]
    if len(keys) != len(set(keys)):
        errors.append("Citation registry contains duplicate source keys")

    registered_citations = [record.get("citation") for record in records]
    extracted_citations = extract_parenthetical_citations(body)
    unregistered = sorted(set(extracted_citations) - set(registered_citations))
    unused = sorted(set(registered_citations) - set(extracted_citations))
    if unregistered:
        errors.append(f"Unregistered in-text citations: {', '.join(unregistered)}")
    if unused:
        errors.append(f"Registered sources not cited in the manuscript: {', '.join(unused)}")

    references = bibliography_lines(text)
    registered_references = [record.get("reference") for record in records]
    missing_references = sorted(set(registered_references) - set(references))
    unregistered_references = sorted(set(references) - set(registered_references))
    if missing_references:
        errors.append(f"Registered reference text missing or changed: {missing_references}")
    if unregistered_references:
        errors.append(f"Bibliography entries missing from citation registry: {unregistered_references}")

    claim_review_count = 0
    paragraphs = markdown_paragraphs(body)
    source_results: list[SourceResult] = []
    today = date.today()
    for record in records:
        key = record["key"]
        citation = record["citation"]
        cited_paragraphs = [paragraph for paragraph in paragraphs if citation in paragraph]
        actual_hashes = sorted(paragraph_hash(paragraph) for paragraph in cited_paragraphs)
        claims = record.get("claims", [])
        registered_hashes = sorted(claim.get("paragraph_sha256", "") for claim in claims)
        if actual_hashes != registered_hashes:
            errors.append(
                f"{key}: cited paragraph changed or claim review is incomplete; "
                "review the source and refresh its paragraph fingerprint"
            )
        for claim in claims:
            claim_review_count += 1
            if claim.get("alignment_status") != "reviewed":
                errors.append(f"{key}: claim alignment is not marked reviewed")
            if len(normalize_space(claim.get("support_summary", ""))) < 30:
                errors.append(f"{key}: support_summary is too short to document the source-claim relationship")
            if not normalize_space(claim.get("reviewed_by", "")):
                errors.append(f"{key}: reviewed_by is required")
            try:
                reviewed_on = date.fromisoformat(claim.get("reviewed_on", ""))
                if reviewed_on > today:
                    errors.append(f"{key}: reviewed_on cannot be in the future")
            except ValueError:
                errors.append(f"{key}: reviewed_on must be an ISO date")

        if online:
            try:
                result = verify_source_online(record)
            except RuntimeError as error:
                result = SourceResult(key, "failed", str(error))
            source_results.append(result)
            if result.status != "verified":
                errors.append(f"{key}: online source verification failed: {result.detail}")
        else:
            source_results.append(SourceResult(key, "not run", "Use --online to verify the authoritative record"))

    placeholder_count = len(PLACEHOLDER_RE.findall(body))
    maximum_placeholders = int(registry.get("maximum_citation_needed", 0))
    if placeholder_count > maximum_placeholders:
        errors.append(
            f"CITATION NEEDED count increased to {placeholder_count}; allowed maximum is {maximum_placeholders}"
        )

    return AuditResult(
        section_words=section_word_counts(text),
        citation_mentions=len(extracted_citations),
        unique_citations=len(set(extracted_citations)),
        citation_needed=placeholder_count,
        references=len(references),
        claim_reviews=claim_review_count,
        source_results=source_results,
        errors=errors,
    )


def claim_hashes(manuscript_path: Path, registry_path: Path) -> list[tuple[str, str, str]]:
    text = manuscript_path.read_text(encoding="utf-8")
    body = manuscript_body(text)
    registry = load_registry(registry_path)
    paragraphs = markdown_paragraphs(body)
    output: list[tuple[str, str, str]] = []
    for record in registry.get("sources", []):
        for paragraph in paragraphs:
            if record["citation"] in paragraph:
                output.append((record["key"], paragraph_hash(paragraph), normalize_space(paragraph)))
    return output


def markdown_report(result: AuditResult, online: bool) -> str:
    status = "PASS" if result.passed else "FAIL"
    lines = [
        "# Manuscript audit",
        "",
        f"**Status:** {status}",
        "",
        "## Word count by section",
        "",
        "| Section | Words |",
        "|---|---:|",
    ]
    lines.extend(f"| {markdown_escape(section)} | {words:,} |" for section, words in result.section_words)
    lines.extend(
        [
            "",
            "## Citation metrics",
            "",
            "| Metric | Count |",
            "|---|---:|",
            f"| In-text citation mentions | {result.citation_mentions} |",
            f"| Unique cited sources | {result.unique_citations} |",
            f"| Bibliography entries | {result.references} |",
            f"| Claim-level reviews | {result.claim_reviews} |",
            f"| `[CITATION NEEDED]` placeholders | {result.citation_needed} |",
            "",
            "## Source verification",
            "",
            f"Online verification was {'enabled' if online else 'not run'}. Claim fingerprints and registry consistency are always checked.",
            "",
            "| Source | Status | Detail |",
            "|---|---|---|",
        ]
    )
    lines.extend(
        f"| {source.key} | {source.status} | {markdown_escape(source.detail)} |"
        for source in result.source_results
    )
    lines.extend(["", "## Findings", ""])
    if result.errors:
        lines.extend(f"- {error}" for error in result.errors)
    else:
        lines.append("- No blocking findings.")
    return "\n".join(lines) + "\n"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--manuscript", type=Path, default=DEFAULT_MANUSCRIPT)
    parser.add_argument("--registry", type=Path, default=DEFAULT_REGISTRY)
    parser.add_argument("--online", action="store_true", help="Verify DOI and authoritative web records")
    parser.add_argument("--check", action="store_true", help="Exit nonzero when audit findings are present")
    parser.add_argument("--markdown-report", type=Path, help="Write the report to this path")
    parser.add_argument("--print-claim-hashes", action="store_true", help="Print current cited-paragraph fingerprints")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if args.print_claim_hashes:
        for key, fingerprint, paragraph in claim_hashes(args.manuscript, args.registry):
            print(f"{key}\t{fingerprint}\t{paragraph}")
        return 0

    result = audit(args.manuscript, args.registry, online=args.online)
    report = markdown_report(result, online=args.online)
    print(report, end="")
    if args.markdown_report:
        args.markdown_report.write_text(report, encoding="utf-8")
    return 1 if args.check and not result.passed else 0


if __name__ == "__main__":
    sys.exit(main())
