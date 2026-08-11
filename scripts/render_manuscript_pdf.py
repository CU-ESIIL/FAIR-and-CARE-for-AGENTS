#!/usr/bin/env python3
"""Render the canonical Markdown manuscript as a polished, reviewable PDF."""

from __future__ import annotations

import argparse
import html
import os
import re
from datetime import date
from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import LETTER
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    BaseDocTemplate,
    Frame,
    HRFlowable,
    ListFlowable,
    ListItem,
    PageBreak,
    PageTemplate,
    Paragraph,
    Preformatted,
    Spacer,
    Table,
    TableStyle,
)
from reportlab.platypus.tableofcontents import TableOfContents


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_SOURCE = ROOT / "manuscript" / "fair_care_agentic_science.md"
DEFAULT_OUTPUT = ROOT / "output" / "pdf" / "fair_care_agentic_science.pdf"

PRIMARY = colors.HexColor("#234A65")
ACCENT_BLUE = colors.HexColor("#42BCDC")
ACCENT_GREEN = colors.HexColor("#007135")
BODY = colors.HexColor("#161A19")
RELIEF = colors.HexColor("#E9EEF1")
EDITORIAL = colors.HexColor("#8A4B08")

SERIF_DIR = Path("/System/Library/Fonts/Supplemental")
FONT_FILES = {
    "ManuscriptSerif": SERIF_DIR / "Times New Roman.ttf",
    "ManuscriptSerif-Bold": SERIF_DIR / "Times New Roman Bold.ttf",
    "ManuscriptSerif-Italic": SERIF_DIR / "Times New Roman Italic.ttf",
    "ManuscriptSerif-BoldItalic": SERIF_DIR / "Times New Roman Bold Italic.ttf",
    "ManuscriptSans": SERIF_DIR / "Verdana.ttf",
    "ManuscriptSans-Bold": SERIF_DIR / "Verdana Bold.ttf",
    "ManuscriptMono": SERIF_DIR / "Andale Mono.ttf",
}
PORTABLE_FONT_ENV = "MANUSCRIPT_FORCE_PORTABLE_FONTS"

DASH_TRANSLATION = str.maketrans(
    {
        "‐": "-",
        "‑": "-",
        "‒": "-",
        "–": "-",
        "—": "-",
        "―": "-",
    }
)


def selected_font_mode() -> str:
    """Describe the font set that this environment will use."""
    use_portable = os.environ.get(PORTABLE_FONT_ENV) == "1" or not all(
        path.is_file() for path in FONT_FILES.values()
    )
    if use_portable:
        return "portable PDF base-font fallback"
    return "Times New Roman, Verdana, and Andale Mono"


def register_fonts() -> str:
    """Register manuscript fonts, with a dependency-free CI fallback.

    Local journal proofs use Times New Roman, Verdana, and Andale Mono when the
    complete macOS font set is present. Linux runners and other clean systems
    use ReportLab's portable PDF base fonts under the same internal names.
    """
    font_mode = selected_font_mode()
    use_portable = font_mode == "portable PDF base-font fallback"
    if use_portable:
        portable_faces = {
            "ManuscriptSerif": "Times-Roman",
            "ManuscriptSerif-Bold": "Times-Bold",
            "ManuscriptSerif-Italic": "Times-Italic",
            "ManuscriptSerif-BoldItalic": "Times-BoldItalic",
            "ManuscriptSans": "Helvetica",
            "ManuscriptSans-Bold": "Helvetica-Bold",
            "ManuscriptMono": "Courier",
        }
        for name, face in portable_faces.items():
            pdfmetrics.registerFont(pdfmetrics.Font(name, face, "WinAnsiEncoding"))
    else:
        for name, path in FONT_FILES.items():
            pdfmetrics.registerFont(TTFont(name, str(path)))

    pdfmetrics.registerFontFamily(
        "ManuscriptSerif",
        normal="ManuscriptSerif",
        bold="ManuscriptSerif-Bold",
        italic="ManuscriptSerif-Italic",
        boldItalic="ManuscriptSerif-BoldItalic",
    )
    pdfmetrics.registerFontFamily(
        "ManuscriptSans",
        normal="ManuscriptSans",
        bold="ManuscriptSans-Bold",
        italic="ManuscriptSans",
        boldItalic="ManuscriptSans-Bold",
    )
    pdfmetrics.registerFontFamily(
        "ManuscriptMono",
        normal="ManuscriptMono",
        bold="ManuscriptMono",
        italic="ManuscriptMono",
        boldItalic="ManuscriptMono",
    )
    return font_mode


def normalize_dashes(text: str) -> str:
    return text.translate(DASH_TRANSLATION)


def plain_markdown(text: str) -> str:
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
    text = re.sub(r"[*_`]", "", text)
    return normalize_dashes(text).strip()


def inline_markup(text: str) -> str:
    """Convert the small inline Markdown subset used by the manuscript."""
    text = normalize_dashes(text)
    code_spans: list[str] = []

    def save_code(match: re.Match[str]) -> str:
        if match.group(1).startswith("[CITATION NEEDED"):
            return match.group(1)
        code_spans.append(html.escape(match.group(1)))
        return f"@@CODE{len(code_spans) - 1}@@"

    text = re.sub(r"`([^`]+)`", save_code, text)
    text = html.escape(text, quote=True)
    def editorial_note(match: re.Match[str]) -> str:
        detail = f" - {match.group(1)}" if match.group(1) else ""
        return f'<font color="{EDITORIAL.hexval()}"><i>Editorial note: citation needed{detail}</i></font>'

    text = re.sub(r"\[CITATION NEEDED(?:\s*:\s*([^\]]+))?\]", editorial_note, text)
    text = re.sub(
        r"\[([^\]]+)\]\((https?://[^)]+)\)",
        rf'<link href="\2" color="{PRIMARY.hexval()}">\1</link>',
        text,
    )
    text = re.sub(r"\*\*([^*]+)\*\*", r"<b>\1</b>", text)
    text = re.sub(r"(?<!\*)\*([^*]+)\*(?!\*)", r"<i>\1</i>", text)
    for index, value in enumerate(code_spans):
        text = text.replace(
            f"@@CODE{index}@@",
            f'<font name="ManuscriptMono" backColor="#F1F3F4">{value}</font>',
        )
    return text


def parse_title_and_metadata(lines: list[str]) -> tuple[str, list[tuple[str, str]], list[str]]:
    if not lines or not lines[0].startswith("# "):
        raise ValueError("The manuscript must begin with one level-one Markdown heading")
    title = plain_markdown(lines[0][2:])
    metadata: list[tuple[str, str]] = []
    body_start = 1
    metadata_pattern = re.compile(r"^\*\*([^*]+):\*\*\s*(.*)$")
    for index, line in enumerate(lines[1:], start=1):
        if line.startswith("## "):
            body_start = index
            break
        match = metadata_pattern.match(line)
        if match:
            metadata.append((plain_markdown(match.group(1)), plain_markdown(match.group(2))))
    return title, metadata, lines[body_start:]


def build_styles() -> dict[str, ParagraphStyle]:
    sample = getSampleStyleSheet()
    styles = {
        "body": ParagraphStyle(
            "ManuscriptBody",
            parent=sample["BodyText"],
            fontName="ManuscriptSerif",
            fontSize=10.2,
            leading=14.2,
            textColor=BODY,
            alignment=TA_LEFT,
            spaceAfter=7,
            allowWidows=0,
            allowOrphans=0,
        ),
        "title": ParagraphStyle(
            "ManuscriptTitle",
            fontName="ManuscriptSans-Bold",
            fontSize=27,
            leading=32,
            textColor=BODY,
            alignment=TA_LEFT,
            spaceAfter=18,
        ),
        "eyebrow": ParagraphStyle(
            "ManuscriptEyebrow",
            fontName="ManuscriptSans-Bold",
            fontSize=8.5,
            leading=11,
            textColor=ACCENT_GREEN,
            tracking=1.2,
            spaceAfter=12,
        ),
        "thesis": ParagraphStyle(
            "ManuscriptThesis",
            fontName="ManuscriptSerif-Italic",
            fontSize=13,
            leading=18,
            textColor=PRIMARY,
            leftIndent=12,
            rightIndent=12,
            borderColor=ACCENT_BLUE,
            borderWidth=0,
            borderPadding=(10, 12, 10, 12),
            backColor=colors.HexColor("#EEF8FB"),
            spaceBefore=18,
            spaceAfter=26,
        ),
        "meta": ParagraphStyle(
            "ManuscriptMeta",
            fontName="ManuscriptSans",
            fontSize=8.5,
            leading=12,
            textColor=BODY,
        ),
        "h2": ParagraphStyle(
            "ManuscriptH2",
            fontName="ManuscriptSans-Bold",
            fontSize=17,
            leading=21,
            textColor=PRIMARY,
            spaceBefore=18,
            spaceAfter=8,
            keepWithNext=True,
        ),
        "h3": ParagraphStyle(
            "ManuscriptH3",
            fontName="ManuscriptSans-Bold",
            fontSize=12.5,
            leading=16,
            textColor=ACCENT_GREEN,
            spaceBefore=13,
            spaceAfter=6,
            keepWithNext=True,
        ),
        "quote": ParagraphStyle(
            "ManuscriptQuote",
            fontName="ManuscriptSerif-Italic",
            fontSize=10.5,
            leading=15,
            textColor=PRIMARY,
            leftIndent=16,
            rightIndent=12,
            borderColor=ACCENT_BLUE,
            borderWidth=1.5,
            borderPadding=(7, 10, 7, 10),
            backColor=colors.HexColor("#F3FAFC"),
            spaceBefore=6,
            spaceAfter=11,
        ),
        "list": ParagraphStyle(
            "ManuscriptList",
            fontName="ManuscriptSerif",
            fontSize=10.1,
            leading=14,
            textColor=BODY,
            spaceAfter=2,
        ),
        "checklist": ParagraphStyle(
            "ManuscriptChecklist",
            fontName="ManuscriptSerif",
            fontSize=10.1,
            leading=14,
            textColor=BODY,
            leftIndent=20,
            firstLineIndent=-20,
            spaceAfter=3,
        ),
        "code": ParagraphStyle(
            "ManuscriptCode",
            fontName="ManuscriptMono",
            fontSize=7.4,
            leading=10.2,
            textColor=BODY,
            leftIndent=8,
            rightIndent=8,
            borderColor=colors.HexColor("#CBD5DA"),
            borderWidth=0.5,
            borderPadding=8,
            backColor=colors.HexColor("#F6F8F9"),
            spaceBefore=5,
            spaceAfter=10,
        ),
        "table": ParagraphStyle(
            "ManuscriptTable",
            fontName="ManuscriptSerif",
            fontSize=7.2,
            leading=9.2,
            textColor=BODY,
        ),
        "table_header": ParagraphStyle(
            "ManuscriptTableHeader",
            fontName="ManuscriptSans-Bold",
            fontSize=6.9,
            leading=8.7,
            textColor=colors.white,
        ),
        "reference": ParagraphStyle(
            "ManuscriptReference",
            fontName="ManuscriptSerif",
            fontSize=8.8,
            leading=12,
            textColor=BODY,
            leftIndent=14,
            firstLineIndent=-14,
            spaceAfter=7,
        ),
        "toc_title": ParagraphStyle(
            "ManuscriptTOCTitle",
            fontName="ManuscriptSans-Bold",
            fontSize=20,
            leading=24,
            textColor=PRIMARY,
            spaceAfter=18,
        ),
    }
    return styles


class ManuscriptDocTemplate(BaseDocTemplate):
    def afterFlowable(self, flowable):  # noqa: N802 - ReportLab API
        if not isinstance(flowable, Paragraph) or not hasattr(flowable, "toc_level"):
            return
        level = flowable.toc_level
        text = flowable.toc_text
        bookmark = flowable.toc_bookmark
        self.canv.bookmarkPage(bookmark)
        self.canv.addOutlineEntry(text, bookmark, level=level, closed=False)
        self.notify("TOCEntry", (level, text, self.page, bookmark))


def heading_paragraph(text: str, level: int, styles: dict[str, ParagraphStyle], sequence: int) -> Paragraph:
    paragraph = Paragraph(inline_markup(text), styles["h2" if level == 2 else "h3"])
    paragraph.toc_level = level - 2
    paragraph.toc_text = plain_markdown(text)
    paragraph.toc_bookmark = f"heading-{sequence}"
    return paragraph


def markdown_table(rows: list[str], styles: dict[str, ParagraphStyle], width: float) -> Table:
    parsed = [[cell.strip() for cell in row.strip().strip("|").split("|")] for row in rows]
    if len(parsed) > 1 and all(re.fullmatch(r":?-{3,}:?", cell) for cell in parsed[1]):
        parsed.pop(1)
    data: list[list[Paragraph]] = []
    for row_index, row in enumerate(parsed):
        style = styles["table_header"] if row_index == 0 else styles["table"]
        data.append([Paragraph(inline_markup(cell), style) for cell in row])

    column_count = len(data[0])
    if column_count == 4:
        widths = [width * 0.12, width * 0.28, width * 0.32, width * 0.28]
    else:
        widths = [width / column_count] * column_count
    table = Table(data, colWidths=widths, repeatRows=1, splitByRow=True, hAlign="LEFT")
    table.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, 0), PRIMARY),
                ("GRID", (0, 0), (-1, -1), 0.35, colors.HexColor("#B8C5CC")),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LEFTPADDING", (0, 0), (-1, -1), 5),
                ("RIGHTPADDING", (0, 0), (-1, -1), 5),
                ("TOPPADDING", (0, 0), (-1, -1), 5),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
                ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, colors.HexColor("#F7F9FA")]),
            ]
        )
    )
    return table


def markdown_story(lines: list[str], styles: dict[str, ParagraphStyle], width: float) -> list:
    story: list = []
    paragraph_lines: list[str] = []
    heading_sequence = 0
    section = ""

    def flush_paragraph() -> None:
        nonlocal paragraph_lines
        if not paragraph_lines:
            return
        text = " ".join(part.strip() for part in paragraph_lines)
        style = styles["reference"] if section == "References" else styles["body"]
        story.append(Paragraph(inline_markup(text), style))
        paragraph_lines = []

    index = 0
    while index < len(lines):
        line = lines[index].rstrip()

        if not line.strip():
            flush_paragraph()
            index += 1
            continue

        heading = re.match(r"^(##|###)\s+(.+)$", line)
        if heading:
            flush_paragraph()
            level = len(heading.group(1))
            text = heading.group(2).strip()
            if level == 2:
                section = plain_markdown(text)
            heading_sequence += 1
            story.append(heading_paragraph(text, level, styles, heading_sequence))
            index += 1
            continue

        if line.strip() == "---":
            flush_paragraph()
            story.append(HRFlowable(width="100%", thickness=0.7, color=ACCENT_BLUE, spaceBefore=4, spaceAfter=10))
            index += 1
            continue

        if line.startswith("```"):
            flush_paragraph()
            code_lines: list[str] = []
            index += 1
            while index < len(lines) and not lines[index].startswith("```"):
                code_lines.append(lines[index].rstrip("\n"))
                index += 1
            code = "\n".join(code_lines)
            code = code.replace("├──", "|--").replace("└──", "`--").replace("│", "|")
            story.append(Preformatted(normalize_dashes(code), styles["code"], maxLineLength=95))
            index += 1
            continue

        if line.startswith("|"):
            flush_paragraph()
            table_rows: list[str] = []
            while index < len(lines) and lines[index].lstrip().startswith("|"):
                table_rows.append(lines[index])
                index += 1
            story.append(markdown_table(table_rows, styles, width))
            story.append(Spacer(1, 10))
            continue

        if line.startswith(">"):
            flush_paragraph()
            quote_lines: list[str] = []
            while index < len(lines) and lines[index].startswith(">"):
                quote_lines.append(lines[index].lstrip("> ").strip())
                index += 1
            story.append(Paragraph(inline_markup(" ".join(quote_lines)), styles["quote"]))
            continue

        list_match = re.match(r"^\s*(?:([-*])|(\d+)\.)\s+(.+)$", line)
        if list_match:
            flush_paragraph()
            bullet_type = "1" if list_match.group(2) else "bullet"
            checklist = list_match.group(3).startswith("[ ] ")
            item_texts: list[str] = []
            while index < len(lines):
                item_match = re.match(r"^\s*(?:([-*])|(\d+)\.)\s+(.+)$", lines[index].rstrip())
                if not item_match:
                    break
                if ("1" if item_match.group(2) else "bullet") != bullet_type:
                    break
                item_text = item_match.group(3)
                if item_text.startswith("[ ] "):
                    item_text = item_text[4:]
                item_texts.append(item_text)
                index += 1
            if checklist:
                story.extend(
                    Paragraph(f'<font name="ManuscriptMono">[ ]</font> {inline_markup(item)}', styles["checklist"])
                    for item in item_texts
                )
                story.append(Spacer(1, 4))
            else:
                items = [
                    ListItem(Paragraph(inline_markup(item), styles["list"]), leftIndent=12)
                    for item in item_texts
                ]
                story.append(
                    ListFlowable(
                        items,
                        bulletType=bullet_type,
                        start="1" if bullet_type == "1" else None,
                        leftIndent=20,
                        bulletFontName="ManuscriptSerif",
                        bulletFontSize=9,
                        spaceAfter=7,
                    )
                )
            continue

        paragraph_lines.append(line)
        index += 1

    flush_paragraph()
    return story


def draw_later_page(canvas, doc) -> None:
    canvas.saveState()
    width, height = LETTER
    canvas.setStrokeColor(ACCENT_BLUE)
    canvas.setLineWidth(1.2)
    canvas.line(doc.leftMargin, height - 0.48 * inch, width - doc.rightMargin, height - 0.48 * inch)
    canvas.setFont("ManuscriptSans", 7.2)
    canvas.setFillColor(PRIMARY)
    canvas.drawString(doc.leftMargin, height - 0.38 * inch, "FAIR + CARE for Agentic Science")
    canvas.setFillColor(colors.HexColor("#56636A"))
    canvas.drawRightString(
        width - doc.rightMargin,
        0.42 * inch,
        f"{getattr(doc, 'draft_label', 'Working manuscript')}  |  {doc.page}",
    )
    canvas.restoreState()


def title_story(
    title: str,
    metadata: list[tuple[str, str]],
    styles: dict[str, ParagraphStyle],
    source: Path,
) -> list:
    thesis = (
        "FAIR and CARE help people do better science. Agents do not automatically inherit "
        "those practices or obligations, so agentic workflows must encode them explicitly."
    )
    display_metadata = [
        (
            label,
            str(source.relative_to(ROOT)) if label == "Canonical source" and value == "This Markdown file" else value,
        )
        for label, value in metadata
    ]
    status = next((value for label, value in display_metadata if label == "Status"), "Working manuscript")
    meta_rows = [
        [Paragraph(f"<b>{inline_markup(label)}</b>", styles["meta"]), Paragraph(inline_markup(value), styles["meta"])]
        for label, value in display_metadata
    ]
    meta_rows.append(
        [
            Paragraph("<b>PDF export</b>", styles["meta"]),
            Paragraph(date.today().strftime("%d %B %Y"), styles["meta"]),
        ]
    )
    meta_table = Table(meta_rows, colWidths=[1.35 * inch, 4.75 * inch], hAlign="LEFT")
    meta_table.setStyle(
        TableStyle(
            [
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LEFTPADDING", (0, 0), (-1, -1), 0),
                ("RIGHTPADDING", (0, 0), (-1, -1), 8),
                ("TOPPADDING", (0, 0), (-1, -1), 3),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
                ("LINEBELOW", (0, -1), (-1, -1), 0.4, colors.HexColor("#C7D1D6")),
            ]
        )
    )
    return [
        Spacer(1, 0.9 * inch),
        Paragraph(f"{inline_markup(status.upper())} | SCIENTIFIC PERSPECTIVE", styles["eyebrow"]),
        Paragraph(inline_markup(title), styles["title"]),
        HRFlowable(width="34%", thickness=4, color=ACCENT_BLUE, hAlign="LEFT", spaceAfter=18),
        Paragraph(inline_markup(thesis), styles["thesis"]),
        meta_table,
        Spacer(1, 0.35 * inch),
        Paragraph(
            "Generated from the canonical, version-controlled Markdown manuscript. "
            "Editorial citation notes identify unresolved work in this draft.",
            styles["meta"],
        ),
        PageBreak(),
    ]


def render(source: Path, output: Path) -> None:
    register_fonts()
    lines = source.read_text(encoding="utf-8").splitlines()
    title, metadata, body_lines = parse_title_and_metadata(lines)
    draft_label = next((value for label, value in metadata if label == "Status"), "Working manuscript")
    styles = build_styles()

    output.parent.mkdir(parents=True, exist_ok=True)
    page_width, page_height = LETTER
    left_margin = 0.72 * inch
    right_margin = 0.72 * inch
    top_margin = 0.68 * inch
    bottom_margin = 0.64 * inch
    frame_width = page_width - left_margin - right_margin
    frame_height = page_height - top_margin - bottom_margin

    doc = ManuscriptDocTemplate(
        str(output),
        pagesize=LETTER,
        leftMargin=left_margin,
        rightMargin=right_margin,
        topMargin=top_margin,
        bottomMargin=bottom_margin,
        title=title,
        author="FAIR + CARE for Agentic Science project",
        subject=f"{draft_label} scientific Perspective on FAIR, CARE, and agentic science",
        creator="scripts/render_manuscript_pdf.py",
    )
    doc.draft_label = draft_label
    first_frame = Frame(left_margin, bottom_margin, frame_width, frame_height, id="first-frame")
    later_frame = Frame(left_margin, bottom_margin, frame_width, frame_height, id="later-frame")
    doc.addPageTemplates(
        [
            PageTemplate(id="First", frames=[first_frame], autoNextPageTemplate="Later"),
            PageTemplate(id="Later", frames=[later_frame], onPage=draw_later_page),
        ]
    )

    toc = TableOfContents()
    toc.levelStyles = [
        ParagraphStyle(
            "TOCLevel0",
            fontName="ManuscriptSans-Bold",
            fontSize=9.3,
            leading=13,
            textColor=PRIMARY,
            leftIndent=0,
            firstLineIndent=0,
            spaceBefore=4,
        ),
        ParagraphStyle(
            "TOCLevel1",
            fontName="ManuscriptSerif",
            fontSize=8.8,
            leading=12,
            textColor=BODY,
            leftIndent=16,
            firstLineIndent=0,
        ),
    ]

    story = title_story(title, metadata, styles, source)
    story.extend(
        [
            Paragraph("Contents", styles["toc_title"]),
            toc,
            PageBreak(),
        ]
    )
    story.extend(markdown_story(body_lines, styles, frame_width))
    doc.multiBuild(story)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path, default=DEFAULT_SOURCE)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    render(args.source.resolve(), args.output.resolve())
    print(args.output.resolve())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
