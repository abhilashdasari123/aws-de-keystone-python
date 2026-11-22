"""Smoke runner — executes all Keystone Python lab scripts in order."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

SCRIPTS = [
    "hello_pipeline.py",
    "structures_demo.py",
    "clean_orders_day01.py",
]


def main() -> int:
    root = Path(__file__).resolve().parent
    py = sys.executable
    failed = 0
    for name in SCRIPTS:
        path = root / name
        print(f"\n{'=' * 60}\n>>> {name}\n{'=' * 60}")
        result = subprocess.run([py, str(path)], check=False)
        if result.returncode != 0:
            failed += 1
    print(f"\nDone. {len(SCRIPTS) - failed}/{len(SCRIPTS)} passed.")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())