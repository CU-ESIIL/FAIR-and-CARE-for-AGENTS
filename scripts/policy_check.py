#!/usr/bin/env python3
"""Return the repository decision for a proposed action.

Unknown actions are prohibited. This helper enforces a versioned decision; it
does not create authority or replace the human and rights-holder review named
in governance/policy.json.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
POLICY_PATH = ROOT / "governance" / "policy.json"


def load_policy(path: Path = POLICY_PATH) -> dict:
    with path.open(encoding="utf-8") as handle:
        return json.load(handle)


def decision_for(action: str, policy: dict | None = None) -> str:
    active_policy = policy or load_policy()
    return active_policy["actions"].get(action, active_policy["default_decision"])


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("action", help="Action key to evaluate")
    args = parser.parse_args()
    decision = decision_for(args.action)
    print(json.dumps({"action": args.action, "decision": decision}))
    return 0 if decision == "allowed" else 2


if __name__ == "__main__":
    raise SystemExit(main())
