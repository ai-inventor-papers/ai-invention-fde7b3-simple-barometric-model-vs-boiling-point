"""Independent re-derivation of headline numbers (computed-context band biases).

Different code path from method.py: reads the raw dataset rows directly, uses
brentq root-finding on the Clausius-Clapeyron equation (not the closed form),
and computes ISA pressure with an explicit series-free power form in float64.
Placebo: the same statistic on shuffled reference temperatures must NOT match.
"""
from pathlib import Path
import json
import math
import numpy as np
from scipy.optimize import brentq
from iapws import IAPWS97

ROOT = Path(__file__).resolve().parent.parent
raw = json.loads((ROOT / "data" / "full_data_out.json").read_text())

rows = []
for ds in raw["datasets"]:
    for ex in ds["examples"]:
        if ex["metadata_data_type"] != "computed_unknown_method":
            continue
        rows.append((float(json.loads(ex["input"])["altitude_m"]), float(ex["output"])))
alt = np.array([r[0] for r in rows])
tref = np.array([r[1] for r in rows])

g, M, R, T0, L, P0 = 9.80665, 0.028964, 8.314462, 288.15, 0.0065, 101325.0
dH = 40650.0
Tb, Pb = 373.124, 101325.0

def p_isa(h):
    return P0 * (1 - L * h / T0) ** (g * M / (R * L))

def t_ce_root(p):
    f = lambda T: 1 / T - (1 / Tb - (R / dH) * math.log(p / Pb)) if False else (
        math.log(p / Pb) + (dH / R) * (1 / T - 1 / Tb))
    return brentq(f, 200.0, 500.0, xtol=1e-12)

def v3_bias_band(mask, tref_vec):
    res = [t_ce_root(p_isa(h)) - t for h, t in zip(alt[mask], tref_vec[mask])]
    return float(np.mean(res)), float(np.mean(np.abs(res)))

band_hi = alt >= 6000
bias_v3_hi, mae_v3_hi = v3_bias_band(band_hi, tref)
print(json.dumps({"n_6km_plus": int(band_hi.sum()), "V3_bias_K": bias_v3_hi, "V3_MAE_K": mae_v3_hi}))

# Cross-check one IAPWS value through a second path (direct IAPWS97 call at ISA pressure, 9 km)
p9 = p_isa(9000.0)
print("IAPWS-IF97 at ISA 9 km (K):", round(float(IAPWS97(P=p9 / 1e6, x=0).T), 4))

# Placebo: shuffle reference temperatures; the statistic must shift away from the real one
rng = np.random.default_rng(0)
shuf = rng.permutation(tref)
bias_shuf, mae_shuf = v3_bias_band(band_hi, shuf)
print(json.dumps({"placebo_V3_bias_K": bias_shuf, "placebo_V3_MAE_K": mae_shuf,
                  "placebo_fails_to_match": abs(bias_shuf - bias_v3_hi) > 0.5}))
