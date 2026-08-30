#!/usr/bin/env python3
"""Editable vector source for Figure 1."""

from __future__ import annotations

from reportlab.graphics.shapes import Drawing, Group, Line, Rect, String
from reportlab.lib import colors


BASE_WIDTH = 540
BASE_HEIGHT = 560
INK = colors.HexColor("#151515")
PURPLE = colors.HexColor("#6A4C93")
ORANGE = colors.HexColor("#E79B48")
BLUE = colors.HexColor("#3478A8")
TEAL = colors.HexColor("#2F8F8A")
GREEN = colors.HexColor("#2D8A57")
PALE_PURPLE = colors.HexColor("#F3ECF8")
PALE_BLUE = colors.HexColor("#EDF5FB")
PALE_TEAL = colors.HexColor("#EAF6F4")
PALE_GRAY = colors.HexColor("#F4F4F4")
PALE_GREEN = colors.HexColor("#EAF5EE")


def label(group: Group, x: float, y: float, text: str, size: float = 11, *, bold: bool = False, color=INK) -> None:
    group.add(
        String(
            x,
            y,
            text,
            fontName="Helvetica-Bold" if bold else "Helvetica",
            fontSize=size,
            fillColor=color,
            textAnchor="middle",
        )
    )


def box(group: Group, y: float, height: float, fill, stroke, title: str, details: list[str]) -> None:
    x = 66
    width = BASE_WIDTH - 132
    group.add(Rect(x, y, width, height, rx=5, ry=5, fillColor=fill, strokeColor=stroke, strokeWidth=1.5))
    label(group, BASE_WIDTH / 2, y + height - 21, title, 13, bold=True)
    detail_y = y + height - 40
    for detail in details:
        label(group, BASE_WIDTH / 2, detail_y, detail, 9)
        detail_y -= 12


def build_figure(width: float = BASE_WIDTH) -> Drawing:
    """Return a scalable ReportLab vector drawing."""
    scale = width / BASE_WIDTH
    drawing = Drawing(width, BASE_HEIGHT * scale)
    group = Group()

    box(
        group,
        462,
        76,
        PALE_PURPLE,
        PURPLE,
        "PEOPLE SET PURPOSE AND PERMISSION",
        ["Who wants the work, who may approve it,", "and what is out of bounds?"],
    )

    boundary_x = 52
    boundary_y = 24
    boundary_width = BASE_WIDTH - 104
    boundary_height = 420
    group.add(
        Rect(
            boundary_x,
            boundary_y,
            boundary_width,
            boundary_height,
            fillColor=None,
            strokeColor=ORANGE,
            strokeWidth=1.7,
            strokeDashArray=[5, 4],
        )
    )
    group.add(Rect(88, 424, BASE_WIDTH - 176, 24, fillColor=colors.white, strokeColor=None))
    label(group, BASE_WIDTH / 2, 432, "PERMISSION BOUNDARY: WHAT THE COMPUTER MAY DO", 9, bold=True, color=ORANGE)

    box(
        group,
        332,
        78,
        PALE_BLUE,
        BLUE,
        "THE REPOSITORY MAKES EVIDENCE CLEAR",
        ["Current data and code - meaning -", "access conditions - rights - history"],
    )

    group.add(Rect(66, 260, BASE_WIDTH - 132, 46, rx=5, ry=5, fillColor=PALE_TEAL, strokeColor=TEAL, strokeWidth=1.5))
    label(group, BASE_WIDTH / 2, 278, "GOAL  →  INSTRUCTIONS  →  EVALUATION  →  RECORD", 10, bold=True)

    box(
        group,
        142,
        92,
        PALE_GRAY,
        colors.HexColor("#808080"),
        "PEOPLE + COMPUTERS DO THE WORK",
        ["Use the stated evidence, tools, checks,", "permissions, and stopping rules"],
    )

    group.add(Rect(66, 54, BASE_WIDTH - 132, 62, rx=5, ry=5, fillColor=PALE_GREEN, strokeColor=GREEN, strokeWidth=1.5))
    label(group, BASE_WIDTH / 2, 78, "REVIEW  →  RELEASE OR CORRECT", 12, bold=True)

    if scale != 1:
        group.scale(scale, scale)
    drawing.add(group)
    return drawing


if __name__ == "__main__":
    from reportlab.graphics import renderSVG

    renderSVG.drawToFile(build_figure(), "figure1_workflow.svg")
