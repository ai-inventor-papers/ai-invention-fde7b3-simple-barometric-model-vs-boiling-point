"""Assemble method_out.json (exp_gen_sol_out format) from results/ outputs.

One example per Engineering ToolBox altitude (0-9 km). input = the altitude query,
output = the table value, predict_V1..predict_V4 = the four variant predictions (strings, C),
metadata_* = numeric residuals (K) for each variant.
"""
import csv
import json
from pathlib import Path

import numpy as np

WS = Path(__file__).resolve().parent
RES = WS / "results"
table = []
with (WS / "inputs" / "engineeringtoolbox_table.csv").open() as f:
    for r in csv.DictReader(f):
        h = float(r["altitude_m"])
        if 0 <= h <= 9000:
            table.append((h, float(r["bp_C"])))
table.sort()
pred = json.loads((RES / "predictions.json").read_text())
grid_h = np.array(pred["altitude_m"])
variants = ["V1", "V2", "V3", "V4"]
bp_grid = {v: np.array(pred["variants"][v]["bp_C"]) for v in variants}

examples = []
for h, ref in table:
    # Model predictions are evaluated at the table altitude in method.py; the saved predictions.json is on the 100 m grid.
    # Use the grid values only where the table altitude falls on the grid; otherwise read the residual file.
    res = json.loads((RES / "residuals.json").read_text())["residuals"]
    ex = {
        "input": f"Boiling point of water at altitude {h:.0f} m (standard-atmosphere pressure, sea-level 101.325 kPa)",
        "output": f"{ref:.1f} C (Engineering ToolBox table)",
    }
    for v in variants:
        ex[f"predict_{v}"] = f"{res[v]['residual_K'][table.index((h, ref))] + ref:.2f} C"
    for v in variants:
        ex[f"metadata_residual_{v}_K"] = round(res[v]["residual_K"][table.index((h, ref))], 4)
    ex["metadata_altitude_m"] = h
    examples.append(ex)

out = {
    "metadata": {
        "method_name": "Boiling point vs altitude: 2x2 factorial of atmosphere model and thermodynamic model",
        "description": (
            "Four variants of water boiling point vs altitude (0-9 km): V1 isothermal + constant-enthalpy Clausius-Clapeyron; "
            "V2 isothermal + IAPWS-IF97 saturation; V3 ISA lapse-rate + constant-enthalpy; V4 ISA lapse-rate + IAPWS-IF97. "
            "Residuals (model minus Engineering ToolBox table, K) reported by band. No measured pairs could be verified; "
            "measured comparison is empty."
        ),
        "parameters": {
            "R_J_per_molK": 8.314462618, "M_air_kg_per_mol": 0.0289644, "g_m_per_s2": 9.80665,
            "lapse_rate_K_per_m": 0.0065, "T0_K": 288.15, "P_sea_Pa": 101325.0,
            "dH_J_per_mol": 40650.0, "T_anchor_K": 373.15,
        },
        "baseline": "V1 (isothermal + constant enthalpy) is the textbook shortcut; V2-V4 compared against it",
        "benchmark": "Engineering ToolBox table (method unstated; a reference curve, not a measurement)",
        "n_examples": len(examples),
        "notes": "Band statistics and crossover results are in results/summary_by_band.json. No statistical test is performed.",
    },
    "datasets": [{"dataset": "Engineering ToolBox boiling point vs altitude table (0-9 km)", "examples": examples}],
}
(WS / "method_out.json").write_text(json.dumps(out, indent=1))
print(f"wrote method_out.json with {len(examples)} examples")
