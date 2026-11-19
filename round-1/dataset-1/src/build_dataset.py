"""Build the water boiling-point vs pressure reference table.

Rows:
  computed_unknown_method : Engineering ToolBox table (altitude, boiling T as published)
  computed_reference      : IAPWS-IF97 saturation temperature at ISA pressure for the same altitude
No measured rows were verifiably transcribed (see README), so data_type=measured has zero rows.
"""
import json
import re
from pathlib import Path

from iapws import IAPWS97

ROOT = Path(__file__).resolve().parent
RAW = ROOT / "temp" / "raw" / "engtoolbox.md"
OUT = ROOT / "temp" / "datasets" / "boiling_point_pressure_full.json"
TB_URL = "https://www.engineeringtoolbox.com/boiling-points-water-altitude-d_1344.html"
TB_CITE = ("Engineering ToolBox, 'Water - Boiling Points vs. Altitude', "
           f"{TB_URL} (accessed 2026-11-19)")
IAPWS_CITE = ("Wagner W, Pruss A (2002) The IAPWS Formulation 1995 for the Thermodynamic Properties "
              "of Ordinary Water Substance for General and Scientific Use, J Phys Chem Ref Data 31:387-535; "
              "IAPWS-IF97 evaluated with the iapws Python package v1.5.5")
ISA_NOTE = ("pressure from the ISA troposphere formula P=101325*(1-2.25577e-5*h)^5.25588 (a standard-atmosphere model, not a measurement)")

ROW_RE = re.compile(r"^(-?\d+)\s*\|\s*(-?\d+)\s*\|\s*([\d.]+)\s*\|\s*([\d.]+)\s*$", re.M)


def isa_pressure_pa(h_m: float) -> float:
    return 101325.0 * (1.0 - 2.25577e-5 * h_m) ** 5.25588


def iapws_tsat_k(p_pa: float) -> float:
    return IAPWS97(P=p_pa / 1e6, x=0).T


def main() -> None:
    text = RAW.read_text(encoding="utf-8")
    rows = []
    for m in ROW_RE.finditer(text):
        alt_ft, alt_m, t_f, t_c = m.groups()
        rows.append((int(alt_m), float(t_c), float(t_f), int(alt_ft)))
    rows = sorted(set(rows))
    out = []
    for alt_m, t_c, t_f, alt_ft in rows:
        out.append({
            "altitude_m": alt_m, "pressure_Pa": None, "boiling_T_K": round(t_c + 273.15, 2),
            "source_id": "engtoolbox_boiling_altitude", "data_type": "computed_unknown_method",
            "method_note": "Published tabulated value; the source does not state its method. Benchmark only.",
            "reference_pressure_note": "none stated",
            "citation": TB_CITE, "raw_value": t_c, "raw_unit": "C",
        })
    for alt_m, t_c, t_f, alt_ft in rows:
        p = isa_pressure_pa(alt_m)
        out.append({
            "altitude_m": alt_m, "pressure_Pa": round(p, 1), "boiling_T_K": round(iapws_tsat_k(p), 3),
            "source_id": "iapws_if97_saturation", "data_type": "computed_reference",
            "method_note": "IAPWS-IF97 Tsat(P), with " + ISA_NOTE,
            "reference_pressure_note": "pressure is the ISA model value at the altitude",
            "citation": IAPWS_CITE, "raw_value": None, "raw_unit": None,
        })
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(out, indent=1), encoding="utf-8")
    counts = {}
    for r in out:
        counts[r["data_type"]] = counts.get(r["data_type"], 0) + 1
    print("rows parsed from ToolBox:", len(rows))
    print("counts:", counts)


if __name__ == "__main__":
    main()
