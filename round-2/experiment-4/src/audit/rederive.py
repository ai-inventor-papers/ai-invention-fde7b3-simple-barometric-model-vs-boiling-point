#!/usr/bin/env python3
"""Independent re-derivation of headline numbers from raw residual rows.

Different code path from method.py: reads only results/residuals.json (raw
per-altitude model_K and reference values), recomputes each residual, takes
band means with the statistics module, and recomputes the constant-enthalpy
temperature with the algebraically rearranged form Tb = Ta / (1 - (Ta R/dH) ln(P/P0)).
Model pressures are re-derived from altitude with the closed forms written
in log space (not method.py's functions).
"""
import json
import math
import statistics
from pathlib import Path

WS = Path(__file__).resolve().parent.parent
raw = json.loads((WS / "results" / "residuals.json").read_text())
rows = raw["rows"]
R = 8.314462618
DH = 40650.0
P0 = 101325.0
T0 = 288.15
L = 0.0065
G0 = 9.80665
M = 0.0289644
N_ISA = G0 * M / (R * L)

def band(h):
    if h < 0: return None
    if h < 3000: return "0-3 km"
    if h < 6000: return "3-6 km"
    if h <= 9144: return "6-9 km"
    return None

# 1. Recompute pressures in log space and check against stored values
max_p_err = 0.0
for r in rows:
    h = r["altitude_m"]
    lp_iso = math.log(P0) - G0 * M * h / (R * T0)
    lp_isa = math.log(P0) + N_ISA * math.log(1 - L * h / T0)
    max_p_err = max(max_p_err, abs(math.exp(lp_iso) - r["P_isothermal_Pa"]), abs(math.exp(lp_isa) - r["P_isa_Pa"]))
print(f"max |P recomputed - stored| over altitudes: {max_p_err:.3e} Pa")

# 2. Recompute model temperatures from the stored pressure with rearranged formula
def tb_rearranged(p, ta, dh):
    return ta / (1 - (ta * R / dh) * math.log(p / P0))

variants = {"A373.124": (373.124, 40650.0), "A373.15": (373.15, 40650.0)}
max_tb_err = 0.0
for r in rows:
    for a, pkey in (("isothermal", "P_isothermal_Pa"), ("isa", "P_isa_Pa")):
        for v, (ta, dh) in variants.items():
            re = tb_rearranged(r[pkey], ta, dh)
            max_tb_err = max(max_tb_err, abs(re - r["model_K"][a][v]))
print(f"max |Tb rearranged - stored model| for variants A373.124/A373.15: {max_tb_err:.3e} K")

# 3. Band bias of residuals vs ToolBox, recomputed from raw rows with statistics module
def band_bias(atmos, variant, ref_key):
    vals = []
    for r in rows:
        b = band(r["altitude_m"])
        if b != "6-9 km":
            continue
        ref = r["ref_toolbox_K"] if ref_key == "toolbox" else r["ref_iapws_isa_K"]
        vals.append(r["model_K"][atmos][variant] - ref)
    return statistics.fmean(vals), len(vals)

results = {}
for atmos in ("isothermal", "isa"):
    for v in ("A373.124", "A373.15", "B_effective", "C_iapws_inversion"):
        m, n = band_bias(atmos, v, "toolbox")
        results[(atmos, v)] = (m, n)
        print(f"6-9 km vs ToolBox  {atmos:10s} {v:18s} bias={m:+.4f} K n={n}")

# 4. Headline quantities
anchor_iso = results[("isothermal", "A373.124")][0] - results[("isothermal", "A373.15")][0]
anchor_isa = results[("isa", "A373.124")][0] - results[("isa", "A373.15")][0]
print(f"anchor shift 6-9 km isothermal {anchor_iso:+.4f} K, ISA {anchor_isa:+.4f} K")
for atmos in ("isothermal", "isa"):
    base = abs(results[(atmos, "A373.124")][0])
    for v in ("B_effective", "C_iapws_inversion"):
        z = 100 * (1 - abs(results[(atmos, v)][0]) / base)
        print(f"Z ({v}, {atmos}) = {z:.2f}%")
# 5. Atmosphere effect 6-9 km, variant A373.15 vs ToolBox
atm = results[("isa", "A373.15")][0] - results[("isothermal", "A373.15")][0]
print(f"ISA minus isothermal 6-9 km (A373.15, ToolBox) = {atm:+.4f} K")
