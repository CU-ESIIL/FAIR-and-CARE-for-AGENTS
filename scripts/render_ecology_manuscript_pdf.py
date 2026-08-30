#!/usr/bin/env python3
"""Render the current manuscript as an Ecology-style review PDF.

This creates a formatting proof from Markdown. Ecology accepts a PDF main
document only for LaTeX submissions, so the output is not itself an allowable
main-document file without a genuine LaTeX source package.
"""

from __future__ import annotations

import argparse
import html
import json
import re
from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import LETTER
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import (
    BaseDocTemplate,
    Frame,
    NextPageTemplate,
    PageBreak,
    PageTemplate,
    Paragraph,
    Preformatted,
    Spacer,
    Table,
    TableStyle,
)

from render_manuscript_pdf import figure_drawing, normalize_dashes, plain_markdown, register_fonts


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_SOURCE = ROOT / "manuscript" / "fair_care_agentic_science_v2.md"
DEFAULT_METADATA = ROOT / "manuscript" / "ecology_submission.json"
DEFAULT_OUTPUT = ROOT / "output" / "pdf" / "fair_care_agentic_science_ecology.pdf"

PAGE_WIDTH, PAGE_HEIGHT = LETTER
MARGIN = inch
TEXT_WIDTH = PAGE_WIDTH - 2 * MARGIN
TEXT_HEIGHT = PAGE_HEIGHT - 2 * MARGIN
LINE_LEADING = 24
LINES_PER_REVIEW_PAGE = int(TEXT_HEIGHT // LINE_LEADING)


class NumberedParagraph(Paragraph):
    """Paragraph that draws a continuous number beside each rendered text line."""

    def draw(self) -> None:
        canvas = self.canv
        line_count = len(self.blPara.lines)
        number = getattr(canvas, "_ecology_line_number", 1)
        canvas.saveState()
        canvas.setFont("ManuscriptSerif", 8)
        canvas.setFillColor(colors.black)
        baseline_adjustment = (self.style.leading - self.style.fontSize) / 2 + 2
        for offset in range(line_count):
            y = self.height - (offset + 1) * self.style.leading + baseline_adjustment
            canvas.drawRightString(-0.28 * inch, y, str(number + offset))
        canvas.restoreState()
        canvas._ecology_line_number = number + line_count
        super().draw()


def inline(text: str) -> str:
    """Convert the manuscript's small inline Markdown subset to ReportLab XML."""
    text = normalize_dashes(text)
    code_spans: list[str] = []

    def save_code(match: re.Match[str]) -> str:
        code_spans.append(html.escape(match.group(1)))
        return f"@@CODE{len(code_spans) - 1}@@"

    text = re.sub(r"`([^`]+)`", save_code, text)
    text = html.escape(text, quote=True)
    text = re.sub(
        r"\[CITATION NEEDED(?:\s*:\s*([^\]]+))?\]",
        lambda match: (
            "<i>(supporting source required before submission"
            + (f": {match.group(1)}" if match.group(1) else "")
            + ")</i>"
        ),
        text,
    )
    text = re.sub(
        r"\[([^\]]+)\]\((https?://[^)]+)\)",
        r'<link href="\2">\1</link>',
        text,
    )
    text = re.sub(r"\*\*([^*]+)\*\*", r"<b>\1</b>", text)
    text = re.sub(r"(?<!\*)\*([^*]+)\*(?!\*)", r"<i>\1</i>", text)
    for index, value in enumerate(code_spans):
        text = text.replace(f"@@CODE{index}@@", f"<i>{value}</i>")
    return text


def styles() -> dict[str, ParagraphStyle]:
    return {
        "body": ParagraphStyle(
            "EcologyBody",
            fontName="ManuscriptSerif",
            fontSize=12,
            leading=LINE_LEADING,
            alignment=TA_LEFT,
            textColor=colors.black,
            spaceAfter=0,
            allowWidows=0,
            allowOrphans=0,
        ),
        "title": ParagraphStyle(
            "EcologyTitle",
            fontName="ManuscriptSerif-Bold",
            fontSize=12,
            leading=LINE_LEADING,
            alignment=TA_CENTER,
            textColor=colors.black,
            spaceAfter=0,
        ),
        "center": ParagraphStyle(
            "EcologyCenter",
            fontName="ManuscriptSerif",
            fontSize=12,
            leading=LINE_LEADING,
            alignment=TA_CENTER,
            textColor=colors.black,
            spaceAfter=0,
        ),
        "label": ParagraphStyle(
            "EcologyLabel",
            fontName="ManuscriptSerif-Bold",
            fontSize=12,
            leading=LINE_LEADING,
            alignment=TA_LEFT,
            textColor=colors.black,
            spaceBefore=LINE_LEADING,
            spaceAfter=0,
            keepWithNext=True,
        ),
        "h2": ParagraphStyle(
            "EcologyH2",
            fontName="ManuscriptSerif-Bold",
            fontSize=12,
            leading=LINE_LEADING,
            alignment=TA_LEFT,
            textColor=colors.black,
            spaceBefore=LINE_LEADING,
            spaceAfter=0,
            keepWithNext=True,
        ),
        "h3": ParagraphStyle(
            "EcologyH3",
            fontName="ManuscriptSerif-BoldItalic",
            fontSize=12,
            leading=LINE_LEADING,
            alignment=TA_LEFT,
            textColor=colors.black,
            spaceBefore=LINE_LEADING,
            spaceAfter=0,
            keepWithNext=True,
        ),
        "reference": ParagraphStyle(
            "EcologyReference",
            fontName="ManuscriptSerif",
            fontSize=12,
            leading=LINE_LEADING,
            alignment=TA_LEFT,
            textColor=colors.black,
            leftIndent=0.25 * inch,
            firstLineIndent=-0.25 * inch,
            spaceAfter=0,
        ),
        "table": ParagraphStyle(
            "EcologyTable",
            fontName="ManuscriptSerif",
            fontSize=10,
            leading=12,
            alignment=TA_LEFT,
            textColor=colors.black,
        ),
        "table_header": ParagraphStyle(
            "EcologyTableHeader",
            fontName="ManuscriptSerif-Bold",
            fontSize=10,
            leading=12,
            alignment=TA_LEFT,
            textColor=colors.black,
        ),
        "footer": ParagraphStyle(
            "EcologyFooter",
            fontName="ManuscriptSerif",
            fontSize=9,
            leading=11,
            alignment=TA_CENTER,
            textColor=colors.black,
        ),
    }


def section_map(lines: list[str]) -> dict[str, list[str]]:
    sections: dict[str, list[str]] = {}
    current = "metadata"
    sections[current] = []
    for line in lines[1:]:
        match = re.match(r"^##\s+(.+)$", line)
        if match:
            current = plain_markdown(match.group(1))
            sections[current] = []
        else:
            sections[current].append(line)
    return sections


def extract_table(lines: list[str]) -> tuple[list[str], str, list[str]]:
    clean: list[str] = []
    caption = "Table 1. FAIR and CARE repository design rules, implementations, and tests."
    rows: list[str] = []
    index = 0
    while index < len(lines):
        heading = re.match(r"^###\s+Table\s+1\.\s*(.+)$", lines[index])
        bold_caption = re.match(r"^\*\*Table\s+1\.\*\*\s*(.+)$", lines[index])
        if not heading and not bold_caption:
            clean.append(lines[index])
            index += 1
            continue
        caption_text = (heading or bold_caption).group(1)
        caption = f"Table 1. {plain_markdown(caption_text)}"
        if not caption.endswith("."):
            caption += "."
        index += 1
        while index < len(lines) and not lines[index].strip():
            index += 1
        while index < len(lines) and lines[index].lstrip().startswith("|"):
            rows.append(lines[index])
            index += 1
    return clean, caption, rows


def extract_figure(lines: list[str]) -> tuple[list[str], str, str]:
    clean: list[str] = []
    caption = (
        "Figure 1. An agent-ready repository makes scientific purpose, workflows, "
        "evaluation, provenance, and authority inspectable."
    )
    asset = ""
    index = 0
    while index < len(lines):
        image_match = re.fullmatch(r"!\[([^\]]*)\]\(([^)]+\.svg)\)", lines[index].strip())
        if image_match:
            asset = image_match.group(2)
            index += 1
            continue
        if lines[index].startswith("**Figure 1.**"):
            raw = re.sub(r"^\*\*Figure 1\.\*\*\s*", "", lines[index])
            caption = f"Figure 1. {plain_markdown(raw)}"
            index += 1
            continue
        clean.append(lines[index])
        index += 1
    return clean, caption, asset


def parse_table(rows: list[str], style_map: dict[str, ParagraphStyle]) -> Table:
    parsed = [[cell.strip() for cell in row.strip().strip("|").split("|")] for row in rows]
    if len(parsed) > 1 and all(re.fullmatch(r":?-{3,}:?", cell) for cell in parsed[1]):
        parsed.pop(1)
    data = []
    for row_index, row in enumerate(parsed):
        style = style_map["table_header"] if row_index == 0 else style_map["table"]
        data.append([Paragraph(inline(cell), style) for cell in row])
    widths = [TEXT_WIDTH * 0.13, TEXT_WIDTH * 0.25, TEXT_WIDTH * 0.34, TEXT_WIDTH * 0.28]
    table = Table(data, colWidths=widths, repeatRows=1, splitByRow=True, hAlign="LEFT")
    table.setStyle(
        TableStyle(
            [
                ("GRID", (0, 0), (-1, -1), 0.5, colors.black),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LEFTPADDING", (0, 0), (-1, -1), 4),
                ("RIGHTPADDING", (0, 0), (-1, -1), 4),
                ("TOPPADDING", (0, 0), (-1, -1), 4),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
            ]
        )
    )
    return table


def content_story(lines: list[str], style_map: dict[str, ParagraphStyle], section: str = "") -> list:
    story: list = []
    paragraph: list[str] = []

    def flush() -> None:
        nonlocal paragraph
        if paragraph:
            text = " ".join(item.strip() for item in paragraph)
            style = style_map["reference"] if section == "References" else style_map["body"]
            story.append(NumberedParagraph(inline(text), style))
            paragraph = []

    index = 0
    while index < len(lines):
        line = lines[index].rstrip()
        if not line.strip() or line.strip() == "---":
            flush()
            index += 1
            continue
        if section == "References" and line.startswith("- "):
            flush()
            story.append(NumberedParagraph(inline(line[2:].strip()), style_map["reference"]))
            index += 1
            continue
        heading = re.match(r"^(##|###)\s+(.+)$", line)
        if heading:
            flush()
            style = style_map["h2" if len(heading.group(1)) == 2 else "h3"]
            story.append(NumberedParagraph(inline(heading.group(2)), style))
            index += 1
            continue
        if line.startswith("```"):
            flush()
            code: list[str] = []
            index += 1
            while index < len(lines) and not lines[index].startswith("```"):
                converted = lines[index].replace("├──", "|--").replace("└──", "`--").replace("│", "|")
                code.append(normalize_dashes(converted))
                index += 1
            for code_line in code:
                preserved = html.escape(code_line).replace(" ", "&#160;") or "&#160;"
                story.append(NumberedParagraph(preserved, style_map["body"]))
            index += 1
            continue
        if line.startswith(">"):
            flush()
            quote: list[str] = []
            while index < len(lines) and lines[index].startswith(">"):
                quote.append(lines[index].lstrip("> ").strip())
                index += 1
            story.append(NumberedParagraph(f"<i>{inline(' '.join(quote))}</i>", style_map["body"]))
            continue
        list_match = re.match(r"^\s*(?:([-*])|(\d+)\.)\s+(.+)$", line)
        if list_match:
            flush()
            bullet_type = "1" if list_match.group(2) else "bullet"
            items: list[str] = []
            while index < len(lines):
                match = re.match(r"^\s*(?:([-*])|(\d+)\.)\s+(.+)$", lines[index].rstrip())
                if not match or ("1" if match.group(2) else "bullet") != bullet_type:
                    break
                items.append(match.group(3))
                index += 1
            for item_index, item in enumerate(items, start=1):
                marker = f"{item_index}." if bullet_type == "1" else "-"
                story.append(NumberedParagraph(f"{marker} {inline(item)}", style_map["body"]))
            continue
        paragraph.append(line)
        index += 1
    flush()
    return story


def draw_page_number(canvas, doc) -> None:
    canvas.saveState()
    canvas.setFont("ManuscriptSerif", 10)
    canvas.setFillColor(colors.black)
    canvas.drawCentredString(PAGE_WIDTH / 2, 0.45 * inch, str(doc.page))
    canvas.restoreState()


def draw_review_page(canvas, doc) -> None:
    draw_page_number(canvas, doc)


def title_page(metadata: dict, style_map: dict[str, ParagraphStyle]) -> list:
    authors = metadata["authors"]
    author_names = []
    for author in authors:
        markers = ",".join(str(value) for value in author["affiliations"])
        corresponding = ",*" if author.get("corresponding") else ""
        author_names.append(f"{inline(author['name'])}<super>{markers}{corresponding}</super>")
    affiliation_lines = [
        Paragraph(f"<super>{number}</super>&#160;{inline(text)}", style_map["center"])
        for number, text in metadata["affiliations"].items()
    ]
    corresponding_authors = [author for author in authors if author.get("corresponding")]
    corresponding_text = "; ".join(
        f"{author['name']}, {author['email']}" for author in corresponding_authors
    )
    orcid_text = "; ".join(
        f"{author['name']}, {author['orcid']}" for author in authors if author.get("orcid")
    )
    keywords = "; ".join(metadata["keywords"])
    story = [
        Paragraph(inline(metadata["journal"]), style_map["center"]),
        Paragraph(inline(metadata["manuscript_type"]), style_map["center"]),
        Spacer(1, LINE_LEADING),
        Paragraph(inline(metadata["title"]), style_map["title"]),
        Spacer(1, LINE_LEADING),
        Paragraph(" and ".join(author_names), style_map["center"]),
        *affiliation_lines,
        Spacer(1, LINE_LEADING),
        Paragraph(
            f"<b>Corresponding author:</b> {inline(corresponding_text)}",
            style_map["body"],
        ),
    ]
    if orcid_text:
        story.append(Paragraph("<b>ORCID:</b> " + inline(orcid_text), style_map["body"]))
    story.extend([
        Paragraph("<b>Open Research statement.</b> " + inline(metadata["open_research_statement"]), style_map["body"]),
        Paragraph("<b>Key words:</b> " + inline(keywords), style_map["body"]),
        PageBreak(),
    ])
    return story


def render(source: Path, metadata_path: Path, output: Path) -> None:
    register_fonts()
    metadata = json.loads(metadata_path.read_text(encoding="utf-8"))
    title_length = len(metadata["title"])
    if title_length > 120:
        raise ValueError(f"Ecology title is {title_length} characters; maximum is 120")
    if not 6 <= len(metadata["keywords"]) <= 12:
        raise ValueError("Ecology requires 6-12 key words")
    if metadata["keywords"] != sorted(metadata["keywords"], key=str.casefold):
        raise ValueError("Ecology key words must be alphabetized")

    lines = source.read_text(encoding="utf-8").splitlines()
    sections = section_map(lines)
    style_map = styles()

    abstract_lines = [
        line
        for line in sections["Abstract"]
        if not line.startswith("**Keywords:") and line.strip() != "---"
    ]
    body_sections = []
    table_caption = ""
    table_rows: list[str] = []
    figure_caption = ""
    figure_asset = ""
    for name, section_lines in sections.items():
        if not re.match(r"^[1-8]\. ", name):
            continue
        cleaned, found_caption, found_rows = extract_table(section_lines)
        if found_rows:
            table_caption, table_rows = found_caption, found_rows
        cleaned, found_figure_caption, found_figure_asset = extract_figure(cleaned)
        if found_figure_asset:
            figure_caption = found_figure_caption
            figure_asset = found_figure_asset
        body_sections.extend([f"## {name}", *cleaned])

    if "Table 1" in sections:
        _, table_caption, table_rows = extract_table(sections["Table 1"])
    if "Figure captions" in sections:
        _, figure_caption, figure_asset = extract_figure(sections["Figure captions"])

    reference_lines = sections["References"]
    if not table_rows:
        raise ValueError("Table 1 was not found in the manuscript")
    if not figure_asset:
        raise ValueError("Figure 1 was not found in the manuscript")

    output.parent.mkdir(parents=True, exist_ok=True)
    doc = BaseDocTemplate(
        str(output),
        pagesize=LETTER,
        leftMargin=MARGIN,
        rightMargin=MARGIN,
        topMargin=MARGIN,
        bottomMargin=MARGIN,
        title=metadata["title"],
        author=", ".join(author["name"] for author in metadata["authors"]),
        subject="Ecology-style manuscript formatting proof",
        creator="scripts/render_ecology_manuscript_pdf.py",
    )
    frame = Frame(MARGIN, MARGIN, TEXT_WIDTH, TEXT_HEIGHT, id="manuscript-frame")
    doc.addPageTemplates(
        [
            PageTemplate(id="Title", frames=[frame], onPage=draw_page_number, autoNextPageTemplate="Review"),
            PageTemplate(id="Review", frames=[frame], onPage=draw_review_page),
            PageTemplate(id="Backmatter", frames=[frame], onPage=draw_page_number),
        ]
    )

    story = title_page(metadata, style_map)
    story.append(NumberedParagraph("Abstract", style_map["h2"]))
    story.extend(content_story(abstract_lines, style_map))
    story.extend(content_story(body_sections, style_map))
    if metadata.get("ai_transparency_statement"):
        story.append(NumberedParagraph("Artificial intelligence transparency statement", style_map["h2"]))
        story.append(NumberedParagraph(inline(metadata["ai_transparency_statement"]), style_map["body"]))
    if metadata.get("acknowledgments"):
        story.append(NumberedParagraph("Acknowledgments", style_map["h2"]))
        story.append(NumberedParagraph(inline(metadata["acknowledgments"]), style_map["body"]))
    if metadata.get("author_contributions"):
        story.append(NumberedParagraph("Author Contributions", style_map["h2"]))
        story.append(NumberedParagraph(inline(metadata["author_contributions"]), style_map["body"]))
    if metadata.get("conflict_of_interest"):
        story.append(NumberedParagraph("Conflict of Interest Statement", style_map["h2"]))
        story.append(NumberedParagraph(inline(metadata["conflict_of_interest"]), style_map["body"]))
    story.append(NumberedParagraph("References", style_map["h2"]))
    story.extend(content_story(reference_lines, style_map, section="References"))
    story.extend([NextPageTemplate("Backmatter"), PageBreak()])
    story.append(Paragraph(inline(table_caption), style_map["body"]))
    story.append(parse_table(table_rows, style_map))
    story.append(PageBreak())
    story.append(Paragraph("Figure captions", style_map["h2"]))
    story.append(figure_drawing((source.parent / figure_asset).resolve(), TEXT_WIDTH * 0.72))
    story.append(Spacer(1, LINE_LEADING / 2))
    story.append(Paragraph(inline(figure_caption), style_map["body"]))
    doc.build(story)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path, default=DEFAULT_SOURCE)
    parser.add_argument("--metadata", type=Path, default=DEFAULT_METADATA)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    render(args.source.resolve(), args.metadata.resolve(), args.output.resolve())
    print(args.output.resolve())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
