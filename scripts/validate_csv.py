from __future__ import annotations

import csv
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA_FILE = ROOT / "data" / "processed" / "simulation_parameters_long.csv"
REQUIRED_COLUMNS = ["material", "property", "value_and_source", "review_status"]


def main() -> int:
    errors: list[str] = []

    with DATA_FILE.open(newline="", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        if reader.fieldnames != REQUIRED_COLUMNS:
            errors.append(f"Expected columns {REQUIRED_COLUMNS}, got {reader.fieldnames}")

        for line_number, row in enumerate(reader, start=2):
            for column in ["material", "property"]:
                if not (row.get(column) or "").strip():
                    errors.append(f"Line {line_number}: missing {column}")

    if errors:
        print("Validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"Validation passed: {DATA_FILE}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

