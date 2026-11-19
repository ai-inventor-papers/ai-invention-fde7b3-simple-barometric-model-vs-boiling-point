"""Independent re-derivation of headline numbers from raw dataset rows.
Different code path from method.py: saturation T obtained by the IAPWS97 backward
equation P->T (not a root-find on T->P), ISA pressure computed inline, and the
ToolBox residual means recomputed from the raw JSON rows."""
import json
import math
from pathlib import Path
import numpy as np
from iapws import IAPWS97

WS = Path(__file__).resolve().parent.parent
doc = json.loads((WS / "data" / "full_data_out.json").read_text())
rows = {}
for ds in doc["datasets"]:
    rows[ds["dataset"]] = [(json.loads(e["input"])["altitude_m"], float(e["output"])) for e in ds["examples"]]
ref = next(v for k, v in rows.items() if k.startswith("iapws"))
tb = next(v for k, v in rows.items() if k.startswith("engtoolbox"))

R, M, g, T0, P0, L = 8.314462618, 0.0289644, 9.80665, 288.15, 101325.0, 0.0065
Tref, Pref, dH = 373.124, 101325.0, 40650.0
p_isa = lambda h: P0 * (1 - L * h / T0) ** (g * M / (R * L))
p_iso = lambda h: P0 * math.exp(-g * M * h / (R * T0))
t_cc = lambda p: 1 / (1 / Tref - R * math.log(p / Pref) / dH)
t_sat = lambda p: IAPWS97(P=p / 1e6, x=0).T  # backward P->T equation

v4 = np.array([t_sat(p_isa(h)) - T for h, T in ref])
print(f"V4 vs stored IAPWS-at-ISA rows: n={len(v4)} max|diff|={np.max(np.abs(v4)):.5f} K")
print(f"Normal boiling point via P->T: {t_sat(101325.0):.4f} K (expected 373.124)")
for name, f in [("V1 iso+CC", lambda h: t_cc(p_iso(h))), ("V3 ISA+CC", lambda h: t_cc(p_isa(h)))]:
    r = np.array([f(h) - T for h, T in tb])
    print(f"ToolBox {name}: n={len(r)} bias={r.mean():+.4f} MAE={np.abs(r).mean():.4f} max={np.abs(r).max():.4f} K")
r4 = np.array([t_sat(p_isa(h)) - T for h, T in tb])
print(f"ToolBox V4: bias={r4.mean():+.4f} max={np.abs(r4).max():.4f} K")
