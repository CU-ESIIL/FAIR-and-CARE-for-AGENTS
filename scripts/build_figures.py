#!/usr/bin/env python3
"""Regenerate editable manuscript figures from their version-controlled source."""

from __future__ import annotations

import argparse
import importlib.util
import tempfile
from pathlib import Path

from reportlab.graphics import renderSVG


ROOT = Path(__file__).resolve().parents[1]
FIGURE_SOURCE = ROOT / "manuscript" / "figures" / "figure1_workflow.py"
FIGURE_OUTPUT = ROOT / "manuscript" / "figures" / "figure1_workflow.svg"


def load_builder():
    spec = importlib.util.spec_from_file_location("figure1_workflow", FIGURE_SOURCE)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Unable to load figure source: {FIGURE_SOURCE}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.build_figure


def build(output: Path = FIGURE_OUTPUT) -> Path:
    output.parent.mkdir(parents=True, exist_ok=True)
    renderSVG.drawToFile(load_builder()(), str(output))
    return output


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=FIGURE_OUTPUT)
    parser.add_argument("--check", action="store_true", help="Fail when the committed SVG is stale")
    args = parser.parse_args()
    if args.check:
        if not FIGURE_OUTPUT.is_file():
            raise SystemExit(f"Missing generated figure: {FIGURE_OUTPUT}")
        with tempfile.TemporaryDirectory() as directory:
            candidate = Path(directory) / FIGURE_OUTPUT.name
            build(candidate)
            if candidate.read_bytes() != FIGURE_OUTPUT.read_bytes():
                raise SystemExit("Figure 1 SVG is stale; run python3 scripts/build_figures.py")
        print("Figure 1 source and SVG agree")
        return 0
    output = build(args.output.resolve())
    print(output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
