"""Independent re-derivation of the headline band statistics (V1-V4 vs the Engineering ToolBox table).

Different code path from method.py: reads the raw table CSV directly, uses closed-form pure-math
expressions for the atmosphere and the constant-enthalpy step, and a hand-written bisection for IAPWS
(method.py uses scipy brentq). The IAPWS97 saturation function itself comes from the same library.
Compares against results/summary_by_band.json and prints the differences.
"""
import csv
import json
import math
from pathlib import Path

from iapws import IAPWS97

WS = Path(__file__).resolve().parent

def psat(T):  # Pa
    return IAPWS97(T=T, x=0).P * 1e6

def bisect_T(p):
    lo, hi = 273.16, 380.0
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if psat(mid) < p:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)

def bp(variant, h):
    g, M, R, T0, L, P0 = 9.80665, 0.0289644, 8.314462618, 288.15, 0.0065, 101325.0
    if variant in ("V1", "V2"):
        P = P0 * math.exp(-h * g * M / (R * T0))
    else:
        P = P0 * (1 - L * h / T0) ** (g * M / (R * L))
    if variant in ("V1", "V3"):
        T = 1.0 / (1.0 / 373.15 - (R / 40650.0) * math.log(P / P0))
    else:
        T = bisect_T(P)
    return T - 273.15

rows = []
with (WS / "inputs" / "engineeringtoolbox_table.csv").open() as f:
    for r in csv.DictReader(f):
        h = float(r["altitude_m"])
        if 0 <= h <= 9000:
            rows.append((h, float(r["bp_C"])))

bands = [("0-3 km", 0, 3000), ("3-6 km", 3000, 6000), ("6-9 km", 6000, 9001)]
stored = json.loads((WS / "results" / "summary_by_band.json").read_text())
worst = 0.0
print(f"{'variant':8}{'band':9}{'n':>4}{'bias_new':>10}{'bias_stored':>13}{'mae_new':>9}{'max_new':>9}")
for v in ("V1", "V2", "V3", "V4"):
    res = [(h, bp(v, h) - ref) for h, ref in rows]
    for name, lo, hi in bands:
        sel = [r for h, r in res if lo <= h < hi]
        bias = sum(sel) / len(sel)
        mae = sum(abs(x) for x in sel) / len(sel)
        mx = max(abs(x) for x in sel)
        s = stored[v][name]
        worst = max(worst, abs(bias - s["bias_K"]), abs(mae - s["mae_K"]), abs(mx - s["max_abs_K"]))
        print(f"{v:8}{name:9}{len(sel):>4}{bias:>+10.3f}{s['bias_K']:>+13.3f}{mae:>9.3f}{mx:>9.3f}")

# crossover sign check, V1-V3 and V2-V4, using the independent residuals
for a, b in (("V1", "V3"), ("V2", "V4")):
    d = [bp(a, h) - bp(b, h) - (ref - ref) for h, ref in rows]
    nz = [x for x in d if abs(x) > 1e-9]
    print(f"{a}-{b}: sign over nonzero points = {'all positive' if all(x > 0 for x in nz) else 'all negative' if all(x < 0 for x in nz) else 'changes sign'}")
    print(f"  stored crossings_m = {stored['crossover'][f'{a}_minus_{b}']['crossings_m']}")
print(f"max |new - stored| over all band statistics: {worst:.2e} K")
