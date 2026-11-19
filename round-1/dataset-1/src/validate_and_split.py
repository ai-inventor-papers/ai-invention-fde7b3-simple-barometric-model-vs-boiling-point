"""Validate the full table against a schema, write mini/preview variants, and report the ToolBox vs IAPWS gap."""
import json
from pathlib import Path

from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parent
DS = ROOT / "temp" / "datasets"
FULL = DS / "boiling_point_pressure_full.json"
SCHEMA = {
    "type": "array",
    "items": {
        "type": "object",
        "required": ["altitude_m", "pressure_Pa", "boiling_T_K", "source_id", "data_type",
                     "method_note", "reference_pressure_note", "citation", "raw_value", "raw_unit"],
        "properties": {
            "altitude_m": {"type": ["integer", "null"]},
            "pressure_Pa": {"type": ["number", "null"]},
            "boiling_T_K": {"type": "number", "minimum": 330, "maximum": 380},
            "source_id": {"type": "string", "minLength": 1},
            "data_type": {"enum": ["measured", "computed_reference", "computed_unknown_method"]},
            "method_note": {"type": "string", "minLength": 1},
            "reference_pressure_note": {"type": "string", "minLength": 1},
            "citation": {"type": "string", "minLength": 1},
            "raw_value": {"type": ["number", "null"]},
            "raw_unit": {"type": ["string", "null"]},
        },
        "additionalProperties": False,
    },
}


def main() -> None:
    data = json.loads(FULL.read_text(encoding="utf-8"))
    errs = list(Draft202012Validator(SCHEMA).iter_errors(data))
    print("schema errors:", len(errs))
    for e in errs[:5]:
        print(e.message)
    if errs:
        raise SystemExit(1)
    for kind in ["computed_unknown_method", "computed_reference", "measured"]:
        sub = [r for r in data if r["data_type"] == kind]
        if sub:
            (DS / f"mini_{kind}.json").write_text(json.dumps(sub[:20], indent=1))
    mini = []
    preview = []
    for kind in ["computed_unknown_method", "computed_reference", "measured"]:
        sub = [r for r in data if r["data_type"] == kind]
        mini += sub[:20]
        preview += sub[:5]
    (DS / "mini_boiling_point_pressure.json").write_text(json.dumps(mini, indent=1))
    trunc = [{k: (v[:200] if isinstance(v, str) else v) for k, v in r.items()} for r in preview]
    (DS / "preview_boiling_point_pressure.json").write_text(json.dumps(trunc, indent=1))
    # ToolBox vs IAPWS at matching altitude
    tb = {r["altitude_m"]: r["boiling_T_K"] for r in data if r["data_type"] == "computed_unknown_method"}
    ref = {r["altitude_m"]: r["boiling_T_K"] for r in data if r["data_type"] == "computed_reference"}
    diffs = [tb[a] - ref[a] for a in tb if a in ref]
    diffs.sort()
    n = len(diffs)
    print("matched altitudes:", n)
    print("ToolBox minus IAPWS-at-ISA (K): min %.2f median %.2f max %.2f mean %.2f" % (
        diffs[0], diffs[n // 2], diffs[-1], sum(diffs) / n))
    for a in [0, 1524, 3048, 6096, 8000]:
        if a in tb:
            print(f"  alt {a} m: ToolBox {tb[a]:.2f} K, IAPWS {ref[a]:.2f} K")


if __name__ == "__main__":
    main()
