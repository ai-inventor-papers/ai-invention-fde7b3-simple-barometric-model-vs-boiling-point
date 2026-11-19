"""Boiling point of water vs altitude: 2x2 factorial of atmosphere model x thermodynamic model.

V1 isothermal + constant-enthalpy Clausius-Clapeyron
V2 isothermal + IAPWS-IF97 saturation curve
V3 ISA lapse-rate + constant-enthalpy Clausius-Clapeyron
V4 ISA lapse-rate + IAPWS-IF97 saturation curve

Residual = model - reference (K). Reference = Engineering ToolBox table (grid),
and independently measured pairs (inputs/measured_pairs.csv; none verified, see README).
"""
from __future__ import annotations

import csv
import json
import math
import sys
from pathlib import Path

import numpy as np
from bs4 import BeautifulSoup
from loguru import logger
from scipy.optimize import brentq
from iapws import IAPWS97

WS = Path(__file__).resolve().parent
INP = WS / "inputs"
RES = WS / "results"
RES.mkdir(parents=True, exist_ok=True)
INP.mkdir(parents=True, exist_ok=True)

# Constants (SI)
R = 8.314462618          # J/(mol K)
M_AIR = 0.0289644        # kg/mol
G = 9.80665              # m/s^2
LAPSE = 0.0065           # K/m (ISA)
T0 = 288.15              # K, sea-level standard temperature
P_SEA = 101325.0         # Pa, sea-level standard pressure
DH_DEFAULT = 40650.0     # J/mol, constant-enthalpy anchor
T_ANCHOR = 373.15        # K, anchor temperature at P_SEA
T_BRACKET = (273.16, 380.0)  # K; upper end widened above 373.15 K so that P = 101325 Pa is bracketed (critical point 647 K)

ALT_GRID = np.arange(0.0, 9001.0, 100.0)  # 91 points
BANDS = [("0-3 km", 0.0, 3000.0), ("3-6 km", 3000.0, 6000.0), ("6-9 km", 6000.0, 9000.0)]
VARIANTS = {
    "V1": ("isothermal", "constant_enthalpy"),
    "V2": ("isothermal", "iapws"),
    "V3": ("isa", "constant_enthalpy"),
    "V4": ("isa", "iapws"),
}


# ---------- Step 0: input curation ----------
def curate_inputs() -> list[dict]:
    raw = INP / "engineeringtoolbox_raw.html"
    if not raw.exists():
        raise FileNotFoundError(f"missing {raw}")
    soup = BeautifulSoup(raw.read_text(encoding="utf-8", errors="replace"), "html.parser")
    table = soup.find("table", class_="small")
    if table is None:
        raise ValueError("Engineering ToolBox table not found in saved HTML")
    rows = []
    for tr in table.find_all("tr"):
        cells = [c.get_text(" ", strip=True) for c in tr.find_all(["td", "th"])]
        if len(cells) != 4:
            continue
        try:
            alt_m = float(cells[1])
            bp_c = float(cells[3])
        except ValueError:
            continue  # header rows
        rows.append({"altitude_m": alt_m, "bp_C": bp_c, "altitude_ft": float(cells[0])})
    if len(rows) < 50:
        raise ValueError(f"parsed only {len(rows)} table rows; expected about 120")
    out = INP / "engineeringtoolbox_table.csv"
    with out.open("w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["altitude_m", "bp_C", "altitude_ft"])
        w.writeheader()
        w.writerows(rows)
    logger.info(f"Engineering ToolBox table: {len(rows)} rows -> {out.name}")
    return rows


def load_table() -> tuple[np.ndarray, np.ndarray]:
    with (INP / "engineeringtoolbox_table.csv").open() as f:
        rows = list(csv.DictReader(f))
    h = np.array([float(r["altitude_m"]) for r in rows])
    t = np.array([float(r["bp_C"]) for r in rows])
    keep = (h >= 0) & (h <= 9000)
    return h[keep], t[keep]


def load_measured() -> list[dict]:
    path = INP / "measured_pairs.csv"
    if not path.exists():
        return []
    with path.open() as f:
        return [r for r in csv.DictReader(f) if r.get("boiling_point_C", "").strip()]


# ---------- Step 1: atmosphere ----------
def scale_height() -> float:
    return R * T0 / (M_AIR * G)


def p_isothermal(h, p0=P_SEA):
    return p0 * np.exp(-np.asarray(h, float) / scale_height())


def p_isa(h, p0=P_SEA):
    expo = G * M_AIR / (R * LAPSE)
    return p0 * (1.0 - LAPSE * np.asarray(h, float) / T0) ** expo


# ---------- Step 2: thermodynamics ----------
def t_constant_enthalpy(p, dh=DH_DEFAULT):
    """Boiling temperature (K) from pressure (Pa), single anchored enthalpy."""
    p = np.asarray(p, float)
    inv = 1.0 / T_ANCHOR - (R / dh) * np.log(p / P_SEA)
    return 1.0 / inv


def psat_pa(T: float) -> float:
    return IAPWS97(T=T, x=0).P * 1e6


_iapws_cache: dict[float, float] = {}


def t_iapws(p):
    """Boiling temperature (K) from pressure (Pa) by inverting the IAPWS-IF97 saturation curve."""
    out = []
    lo, hi = T_BRACKET
    for pi in np.atleast_1d(np.asarray(p, float)):
        f = lambda T, pi=pi: psat_pa(T) - pi
        flo, fhi = f(lo), f(hi)
        if flo > 0 or fhi < 0:
            raise ValueError(f"P={pi:.1f} Pa outside IAPWS bracket {lo}-{hi} K (f_lo={flo:.3g}, f_hi={fhi:.3g})")
        out.append(brentq(f, lo, hi, xtol=1e-10))
    return np.array(out)


def bp_model(h, variant: str, dh=DH_DEFAULT, p0=P_SEA) -> np.ndarray:
    atm, thermo = VARIANTS[variant]
    p = p_isothermal(h, p0) if atm == "isothermal" else p_isa(h, p0)
    T = t_constant_enthalpy(p, dh) if thermo == "constant_enthalpy" else t_iapws(p)
    return T - 273.15


# ---------- Steps 3-4: variants, residuals ----------
def band_stats(h, resid) -> dict:
    out = {}
    for name, lo, hi in BANDS:
        m = (h >= lo) & (h < hi) if hi < 9000 else (h >= lo) & (h <= hi)
        r = resid[m]
        out[name] = {
            "n": int(m.sum()),
            "bias_K": float(np.mean(r)),
            "mae_K": float(np.mean(np.abs(r))),
            "max_abs_K": float(np.max(np.abs(r))),
        }
    return out


def crossings(h, d) -> list[float]:
    """Altitudes where d changes sign, by linear interpolation."""
    xs = []
    for i in range(len(h) - 1):
        if d[i] * d[i + 1] < 0:
            xs.append(float(h[i] + (0 - d[i]) * (h[i + 1] - h[i]) / (d[i + 1] - d[i])))
    return xs


def sign_summary(h, d) -> str:
    nz = d[np.abs(d) > 1e-12]  # ignore exact zeros (e.g. both at 100 C at sea level)
    if np.all(nz > 0):
        return "positive over whole range (zero only at 0 m)"
    if np.all(nz < 0):
        return "negative over whole range (zero only at 0 m)"
    return "changes sign (see crossings_m)"


# ---------- Step 5: measured pairs ----------
def measured_comparison(measured: list[dict], dh=DH_DEFAULT) -> dict:
    rows = []
    for m in measured:
        ref = float(m["boiling_point_C"])
        row = {"source": m.get("source", ""), "reference_C": ref, "altitude_m": m.get("altitude_m", ""),
               "station_pressure_kPa": m.get("station_pressure_kPa", ""), "altitude_only": m.get("altitude_only", "")}
        if row["station_pressure_kPa"] and not row["altitude_only"]:
            p = float(row["station_pressure_kPa"]) * 1000.0
            # Path (i): station pressure -> boiling temperature, thermodynamic step only
            row["path_i_station_pressure"] = {
                "constant_enthalpy": float(t_constant_enthalpy(p, dh) - 273.15 - ref),
                "iapws": float(t_iapws(p)[0] - 273.15 - ref),
            }
        if row["altitude_m"]:
            ha = np.array([float(row["altitude_m"])])
            row["path_ii_altitude"] = {v: float(bp_model(ha, v, dh)[0] - ref) for v in VARIANTS}
        rows.append(row)
    return {"n_points": len(rows), "points": rows,
            "note": "No independently measured pairs could be verified (see README). Counts are descriptive; no significance test is possible."}


# ---------- Unit checks ----------
def sanity_checks() -> dict:
    checks = {}
    checks["H_isothermal_m"] = scale_height()
    checks["P_iso_9000_kPa"] = float(p_isothermal(9000.0) / 1000)
    checks["P_isa_9000_kPa"] = float(p_isa(9000.0) / 1000)
    checks["P_iso_0_equals_P0"] = bool(np.isclose(p_isothermal(0.0), P_SEA))
    checks["P_isa_0_equals_P0"] = bool(np.isclose(p_isa(0.0), P_SEA))
    checks["CE_at_101325_C"] = float(t_constant_enthalpy(P_SEA) - 273.15)
    checks["IAPWS_at_101325_C"] = float(t_iapws(P_SEA)[0] - 273.15)
    checks["IAPWS_psat_90C_kPa"] = float(psat_pa(363.15) / 1000)
    # Latent heat at 373.15 K from IAPWS steam table: enthalpy difference hg - hf (kJ/kg) times molar mass.
    # (The ideal-gas form R T^2 dlnP/dT is NOT used: it ignores vapour non-ideality, Z ~ 0.985 at 1 atm.)
    hg = IAPWS97(T=373.15, x=1).h
    hf = IAPWS97(T=373.15, x=0).h
    dh_iapws = (hg - hf) * 1000.0 * 0.01801528  # J/mol
    checks["dH_IAPWS_100C_J_per_mol"] = dh_iapws
    checks["dH_anchor_J_per_mol"] = DH_DEFAULT
    checks["dH_relative_diff"] = abs(DH_DEFAULT - dh_iapws) / dh_iapws
    checks["IAPWS_normal_boiling_point_K"] = float(brentq(lambda T: psat_pa(T) - P_SEA, *T_BRACKET, xtol=1e-10))
    checks["scale_height_check_ok"] = bool(abs(scale_height() - 8434) < 10)
    checks["P_iso_9000_check_ok"] = bool(abs(checks["P_iso_9000_kPa"] - 34.8) < 0.2)
    checks["P_isa_9000_check_ok"] = bool(abs(checks["P_isa_9000_kPa"] - 30.7) < 0.2)
    checks["CE_sea_level_ok"] = bool(abs(checks["CE_at_101325_C"] - 100.0) < 0.01)
    # IAPWS-IF97 normal boiling point is 373.124 K (99.974 C); the plan's 100.00 C expectation is not what this formulation gives.
    checks["IAPWS_sea_level_ok"] = bool(abs(checks["IAPWS_normal_boiling_point_K"] - 373.124) < 0.01)
    checks["IAPWS_90C_ok"] = bool(abs(checks["IAPWS_psat_90C_kPa"] - 70.1) < 0.2)
    checks["dH_within_1pct_ok"] = bool(checks["dH_relative_diff"] < 0.01)
    # monotone decreasing bp with altitude
    for v in VARIANTS:
        bp = bp_model(ALT_GRID, v)
        checks[f"monotone_decreasing_{v}"] = bool(np.all(np.diff(bp) < 0))
    logger.info(f"sanity: {json.dumps({k: v for k, v in checks.items() if isinstance(v, (bool, float))}, default=float)}")
    return checks


def main() -> None:
    logger.remove()
    logger.add(sys.stdout, level="INFO")
    logger.add(WS / "results" / "run.log", level="DEBUG", rotation="5 MB")

    rows = curate_inputs()
    sanity = sanity_checks()
    bad = [k for k, v in sanity.items() if k.endswith(("_ok", "_equals_P0", "decreasing_V1", "decreasing_V2", "decreasing_V3", "decreasing_V4")) and v is not True]
    if bad:
        raise SystemExit(f"unit checks failed: {bad}")

    h_tab, t_tab = load_table()
    # Sea-level check against table
    sea = float(t_tab[np.argmin(h_tab)])
    logger.info(f"table value at lowest altitude: {sea} C at {h_tab.min()} m")

    # predictions on grid
    preds = {"altitude_m": ALT_GRID.tolist(), "variants": {}}
    grid = {}
    for v in VARIANTS:
        bp = bp_model(ALT_GRID, v)
        p_kpa = (p_isothermal(ALT_GRID) if VARIANTS[v][0] == "isothermal" else p_isa(ALT_GRID)) / 1000
        grid[v] = bp
        preds["variants"][v] = {"atmosphere": VARIANTS[v][0], "thermodynamics": VARIANTS[v][1],
                                "pressure_kPa": p_kpa.tolist(), "bp_C": bp.tolist()}
    (RES / "predictions.json").write_text(json.dumps(preds, indent=1))

    # residuals vs Engineering ToolBox at its own altitudes (model evaluated at table altitude)
    resid_tab = {}
    summary = {}
    for v in VARIANTS:
        model_at_tab = bp_model(h_tab, v)
        r = model_at_tab - t_tab  # K == C differences
        resid_tab[v] = {"altitude_m": h_tab.tolist(), "residual_K": r.tolist()}
        summary[v] = band_stats(h_tab, r)
        logger.info(f"{v} bands: " + ", ".join(f"{b}: bias {s['bias_K']:+.2f} MAE {s['mae_K']:.2f} max {s['max_abs_K']:.2f}" for b, s in summary[v].items()))
    (RES / "residuals.json").write_text(json.dumps({"benchmark": "Engineering ToolBox table (method unstated)",
                                                    "comparison_grid": "table altitudes 0-9000 m, model evaluated at table altitude (not interpolated)",
                                                    "residuals": resid_tab}, indent=1))

    d13 = np.array(resid_tab["V1"]["residual_K"]) - np.array(resid_tab["V3"]["residual_K"])
    d24 = np.array(resid_tab["V2"]["residual_K"]) - np.array(resid_tab["V4"]["residual_K"])
    cross = {"V1_minus_V3": {"crossings_m": crossings(h_tab, d13), "sign": sign_summary(h_tab, d13)},
             "V2_minus_V4": {"crossings_m": crossings(h_tab, d24), "sign": sign_summary(h_tab, d24)}}
    # growth of constant-enthalpy error with altitude (confirmation signal)
    d12 = bp_model(h_tab, "V1") - bp_model(h_tab, "V2")
    cross["V1_minus_V2_by_band_bias_K"] = {b: float(np.mean(d12[(h_tab >= lo) & (h_tab < hi if hi < 9000 else h_tab <= hi)]))
                                            for b, lo, hi in BANDS}
    cross["V1_minus_V2_grows_with_altitude"] = bool(abs(d12[h_tab >= 6000].mean()) > abs(d12[h_tab < 3000].mean()))
    summary["crossover"] = cross
    (RES / "summary_by_band.json").write_text(json.dumps(summary, indent=1))
    logger.info(f"crossover: {json.dumps(cross, default=float)}")

    # measured pairs
    meas = measured_comparison(load_measured())
    (RES / "measured_comparison.json").write_text(json.dumps(meas, indent=1, default=float))
    logger.info(f"measured pairs: {meas['n_points']}")

    # sensitivity: dH +-500 J/mol; sea-level atmospheric pressure +-1 kPa (thermodynamic anchor kept at 101.325 kPa, 373.15 K)
    sens = {}
    for v in ("V1", "V4"):
        sens[v] = {}
        for dh in (DH_DEFAULT - 500, DH_DEFAULT, DH_DEFAULT + 500):
            for dp in (-1000.0, 0.0, 1000.0):
                key = f"dH={dh:.0f}_P0={(P_SEA + dp) / 1000:.3f}kPa"
                r = bp_model(h_tab, v, dh=dh, p0=P_SEA + dp) - t_tab
                sens[v][key] = {"band_stats": band_stats(h_tab, r)}
    # crossover sensitivity for V1 vs V3 and V2 vs V4 under the same perturbations
    sens_cross = {}
    for dh in (DH_DEFAULT - 500, DH_DEFAULT, DH_DEFAULT + 500):
        for dp in (-1000.0, 0.0, 1000.0):
            key = f"dH={dh:.0f}_P0={(P_SEA + dp) / 1000:.3f}kPa"
            d13s = bp_model(h_tab, "V1", dh, P_SEA + dp) - bp_model(h_tab, "V3", dh, P_SEA + dp)
            d24s = bp_model(h_tab, "V2", dh, P_SEA + dp) - bp_model(h_tab, "V4", dh, P_SEA + dp)
            sens_cross[key] = {"V1_minus_V3_crossings_m": crossings(h_tab, d13s), "V2_minus_V4_crossings_m": crossings(h_tab, d24s)}
    (RES / "sensitivity.json").write_text(json.dumps({"variants": sens, "crossover": sens_cross,
                                                      "note": "Perturbations: dH +-500 J/mol (both thermodynamic steps via V1/V4 with CE), sea-level P0 +-1 kPa in the atmosphere models only."}, indent=1))

    # sanity to file
    (RES / "sanity_checks.json").write_text(json.dumps(sanity, indent=1, default=float))
    logger.info("done")


if __name__ == "__main__":
    main()
