# /// script
# requires-python = ">=3.12"
# dependencies = []
# ///
"""Standardize the boiling-point reference table to the exp_sel_data_out format.

Input:  temp/datasets/boiling_point_pressure_full.json (250 rows, 2 sources)
Output: full_data_out.json (workspace root), grouped by source dataset.
One example per table row. The table has two sources only, so there are two groups,
not the eight-to-four dataset selection in the todo: no other candidate datasets exist.
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SRC = ROOT / "temp" / "datasets" / "boiling_point_pressure_full.json"
OUT = ROOT / "full_data_out.json"


def to_example(row: dict, idx: int) -> dict:
    features = {
        "altitude_m": row["altitude_m"],
        "pressure_Pa": row["pressure_Pa"],
    }
    return {
        "input": json.dumps(features, sort_keys=True),
        "output": str(row["boiling_T_K"]),
        "metadata_row_index": idx,
        "metadata_data_type": row["data_type"],
        "metadata_source_id": row["source_id"],
        "metadata_altitude_m": row["altitude_m"],
        "metadata_pressure_Pa": row["pressure_Pa"],
        "metadata_method_note": row["method_note"],
        "metadata_reference_pressure_note": row["reference_pressure_note"],
        "metadata_citation": row["citation"],
        "metadata_raw_value": row["raw_value"],
        "metadata_raw_unit": row["raw_unit"],
    }


def main() -> None:
    rows = json.loads(SRC.read_text(encoding="utf-8"))
    groups: dict[str, list[dict]] = {}
    for i, row in enumerate(rows):
        groups.setdefault(row["source_id"], []).append(to_example(row, i))
    out = {
        "metadata": {
            "description": "Water boiling temperature vs altitude/pressure reference table. "
                           "No measured rows: all rows are computed_reference or computed_unknown_method.",
            "n_measured": sum(1 for r in rows if r["data_type"] == "measured"),
            "n_computed_reference": sum(1 for r in rows if r["data_type"] == "computed_reference"),
            "n_computed_unknown_method": sum(1 for r in rows if r["data_type"] == "computed_unknown_method"),
        },
        "datasets": [{"dataset": name, "examples": ex} for name, ex in groups.items()],
    }
    OUT.write_text(json.dumps(out, indent=1, ensure_ascii=False), encoding="utf-8")
    print({d["dataset"]: len(d["examples"]) for d in out["datasets"]})


if __name__ == "__main__":
    main()
