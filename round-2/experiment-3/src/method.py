"""Water boiling point vs barometric models: 2x2 variants against measured records.

Variants (pressure path x enthalpy model):
  V1 iso + Clausius-Clapeyron (constant dH, anchor Tref at Pref)
  V2 iso + IAPWS-97 saturation
  V3 ISA + Clausius-Clapeyron
  V4 ISA + IAPWS-97 saturation

Measured set: results/measured_records.json (empty, n = 0, because no measured
boiling observation above 5 km could be cited after a bounded search; see README).
The Engineering ToolBox and IAPWS-at-ISA rows from the reference dataset are used only
as a labelled computed consistency check, never as measured evidence.
"""
from __future__ import annotations

import json
import math
import sys
from pathlib import Path

import numpy as np
from iapws import IAPWS97
from loguru import logger
from scipy.optimize import brentq

WS = Path(__file__).resolve().parent
DATA = WS / "data" / "full_data_out.json"
RES = WS / "results"
RES.mkdir(parents=True, exist_ok=True)

# ICAO / ISO 2533 standard atmosphere constants
R = 8.314462618  # J/(mol K)
M = 0.0289644  # kg/mol
G = 9.80665  # m/s^2
T0 = 288.15  # K
P0 = 101325.0  # Pa
LAPSE = 0.0065  # K/m
TREF = 373.124  # K, IAPWS normal boiling point
PREF = 101325.0  # Pa
DH = 40650.0  # J/mol, enthalpy of vaporization near 373 K
BANDS = [(0.0, 3000.0, "0-3 km"), (3000.0, 6000.0, "3-6 km"), (5000.0, 6000.0, "5-6 km"),
         (6000.0, 7000.0, "6-7 km"), (7000.0, 8000.0, "7-8 km"), (8000.0, math.inf, "above 8 km")]
SA_DIFF_NOTE = "Bands 3-6 km and 5-6 km overlap; a record can fall in both."


def p_iso(h: float) -> float:
    return P0 * math.exp(-G * M * h / (R * T0))


def p_isa(h: float) -> float:
    if h > 11000.0:
        raise ValueError("ISA troposphere formula used only up to 11000 m")
    return P0 * (1.0 - LAPSE * h / T0) ** (G * M / (R * LAPSE))


def h_isa(p: float) -> float:
    return (T0 / LAPSE) * (1.0 - (p / P0) ** (R * LAPSE / (G * M)))


def t_cc(p: float, tref: float = TREF, dh: float = DH) -> float:
    return 1.0 / (1.0 / tref - R * math.log(p / PREF) / dh)


def p_cc(t: float, tref: float = TREF, dh: float = DH) -> float:
    return PREF * math.exp((1.0 / tref - 1.0 / t) * dh / R)


def t_iapws(p: float) -> float:
    f = lambda t: IAPWS97(T=t, x=0).P * 1e6 - p
    # Bracket is the saturation range up to just below the IAPWS critical point (647.096 K).
    # The plan's upper bound of 373.946 K is ~100.8 C, not the critical point, and does not bracket.
    return brentq(f, 273.16, 647.0, xtol=1e-10)


def variant_predictions(h: float, tref: float = TREF, dh: float = DH) -> dict:
    """Return the four variant boiling temperatures (K) at altitude h (m)."""
    pi, pa = p_iso(h), p_isa(h)
    return {
        "V1_iso_CC": t_cc(pi, tref, dh),
        "V2_iso_IAPWS": t_iapws(pi),
        "V3_ISA_CC": t_cc(pa, tref, dh),
        "V4_ISA_IAPWS": t_iapws(pa),
    }


def load_computed_rows() -> tuple[list[dict], list[dict]]:
    doc = json.loads(DATA.read_text())
    tb, ref = [], []
    for ds in doc["datasets"]:
        for ex in ds["examples"]:
            inp = json.loads(ex["input"])
            row = {"altitude_m": float(inp["altitude_m"]),
                   "pressure_Pa": None if inp["pressure_Pa"] is None else float(inp["pressure_Pa"]),
                   "T_K": float(ex["output"]), "data_type": ex["metadata_data_type"],
                   "source": ex["metadata_source_id"]}
            (tb if row["data_type"] == "computed_unknown_method" else ref).append(row)
    return tb, ref


def sanity_checks() -> dict:
    checks = {}
    t_cc_sl = t_cc(PREF)
    checks["Tcc_at_101325_K"] = t_cc_sl
    checks["Tcc_at_101325_pass"] = abs(t_cc_sl - TREF) < 1e-9
    t_iap = t_iapws(PREF)
    checks["Tiapws_at_101325_K"] = t_iap
    checks["Tiapws_at_101325_pass"] = abs(t_iap - 373.124) < 0.01
    hs = np.linspace(0.0, 11000.0, 111)
    max_err = max(abs(h_isa(p_isa(h)) - h) for h in hs)
    checks["hisa_roundtrip_max_err_m"] = max_err
    checks["hisa_roundtrip_pass"] = bool(max_err < 1e-6)
    checks["Piso_at_0_Pa"] = p_iso(0.0)
    checks["Pisa_at_11000_Pa"] = p_isa(11000.0)
    checks["Pisa_at_11000_pass"] = abs(p_isa(11000.0) - 22632.0) < 5.0
    max_rt = max(abs(t_cc(p_cc(t)) - t) for t in np.linspace(343.15, 373.15, 61))
    checks["Tcc_roundtrip_max_err_K"] = max_rt
    checks["Tcc_roundtrip_pass"] = max_rt < 1e-9
    checks["all_unit_checks_pass"] = all(v for k, v in checks.items() if k.endswith("_pass"))
    return checks


def consistency_check(ref_rows: list[dict], tb_rows: list[dict]) -> dict:
    """Computed-only check. V4 must reproduce the computed_reference IAPWS-at-ISA values.
    ToolBox rows are compared against V1 and V3 at the same altitude, labelled computed."""
    v4_diffs, v4_detail = [], []
    for r in ref_rows:
        pred = t_iapws(p_isa(r["altitude_m"]))
        d = pred - r["T_K"]
        v4_diffs.append(d)
        v4_detail.append({"altitude_m": r["altitude_m"], "V4_pred_K": pred, "ref_T_K": r["T_K"], "diff_K": d})
    v4_arr = np.array(v4_diffs)
    tb_res = []
    for r in tb_rows:
        vp = variant_predictions(r["altitude_m"])
        tb_res.append({"altitude_m": r["altitude_m"], "tb_T_K": r["T_K"],
                       "resid_V1_K": vp["V1_iso_CC"] - r["T_K"],
                       "resid_V3_K": vp["V3_ISA_CC"] - r["T_K"],
                       "resid_V2_K": vp["V2_iso_IAPWS"] - r["T_K"],
                       "resid_V4_K": vp["V4_ISA_IAPWS"] - r["T_K"]})
    out = {
        "label": "COMPUTED consistency check; not measured evidence",
        "n_ref_rows": len(ref_rows),
        "V4_vs_IAPWS_at_ISA_max_abs_K": float(np.max(np.abs(v4_arr))),
        "V4_vs_IAPWS_at_ISA_pass_0p01K": bool(np.max(np.abs(v4_arr)) <= 0.01),
        "V4_detail": v4_detail,
        "ToolBox_n": len(tb_res),
        "ToolBox_detail": tb_res,
    }
    for key in ["resid_V1_K", "resid_V2_K", "resid_V3_K", "resid_V4_K"]:
        arr = np.array([x[key] for x in tb_res])
        out[f"ToolBox_{key}_bias"] = float(arr.mean())
        out[f"ToolBox_{key}_MAE"] = float(np.mean(np.abs(arr)))
        out[f"ToolBox_{key}_maxabs"] = float(np.max(np.abs(arr)))
    return out


def sensitivity(tb_rows: list[dict]) -> dict:
    """Anchor and dH sensitivity for the CC variants on the computed ToolBox altitudes."""
    base = [variant_predictions(r["altitude_m"]) for r in tb_rows]
    out = {}
    for label, tref, dh in [("anchor_373.15K", 373.15, DH), ("dH_plus_500", TREF, DH + 500.0),
                            ("dH_minus_500", TREF, DH - 500.0)]:
        cc_iso, cc_isa = [], []
        for r, b in zip(tb_rows, base):
            h = r["altitude_m"]
            cc_iso.append(t_cc(p_iso(h), tref, dh) - b["V1_iso_CC"])
            cc_isa.append(t_cc(p_isa(h), tref, dh) - b["V3_ISA_CC"])
        out[label] = {"V1_change_bias_K": float(np.mean(cc_iso)), "V1_change_maxabs_K": float(np.max(np.abs(cc_iso))),
                      "V3_change_bias_K": float(np.mean(cc_isa)), "V3_change_maxabs_K": float(np.max(np.abs(cc_isa)))}
    return out


def band_summary(measured: list[dict]) -> dict:
    """Band statistics per variant. With n = 0 no statistic is written."""
    variants = ["V1_iso_CC", "V2_iso_IAPWS", "V3_ISA_CC", "V4_ISA_IAPWS"]
    bands_out = []
    for lo, hi, name in BANDS:
        members = [m for m in measured if lo <= m["band_altitude_m"] < hi]
        entry = {"band": name, "n": len(members)}
        for v in variants:
            if not members:
                entry[v] = "n=0, no statistic"
            else:
                res = np.array([m["residuals_K"][v] for m in members])
                entry[v] = {"bias_K": float(res.mean()), "MAE_K": float(np.mean(np.abs(res))),
                            "maxabs_K": float(np.max(np.abs(res)))}
        bands_out.append(entry)
    return {"note": SA_DIFF_NOTE, "bands": bands_out}


def main() -> None:
    logger.remove()
    logger.add(sys.stdout, level="INFO")
    (WS / "logs").mkdir(exist_ok=True)
    logger.add(WS / "logs" / "run.log", level="INFO", rotation="5 MB")

    measured = json.loads((RES / "measured_records.json").read_text()) if (RES / "measured_records.json").exists() else []
    logger.info(f"measured records loaded: {len(measured)}")
    if len(measured) == 0:
        logger.warning("No measured records above or below 5 km were cited; measured residuals not computed.")

    # Steps B-D: thermodynamic and altitude passes run only on measured records
    thermo, altitude = [], []
    for m in measured:
        tcc = t_cc(m["pressure_Pa"])
        tiap = t_iapws(m["pressure_Pa"])
        thermo.append({"id": m["id"], "T_pred_CC_K": tcc, "T_pred_IAPWS_K": tiap,
                       "resid_CC_K": tcc - m["T_K"], "resid_IAPWS_K": tiap - m["T_K"]})
        if m.get("altitude_m") is not None:
            h = m["altitude_m"]
            vp = variant_predictions(h)
            altitude.append({"id": m["id"], "altitude_m": h, "altitude_gap_m": h_isa(m["pressure_Pa"]) - h,
                             "residuals_K": {k: v - m["T_K"] for k, v in vp.items()},
                             "band_altitude_m": h})
        else:
            altitude.append({"id": m["id"], "altitude_m": None,
                             "altitude_gap_m": None,
                             "residuals_K": {k: None for k in ["V1_iso_CC", "V2_iso_IAPWS", "V3_ISA_CC", "V4_ISA_IAPWS"]},
                             "band_altitude_m": h_isa(m["pressure_Pa"]), "band_key": "h_isa(P_meas)"})
    altitude_clean = [a for a in altitude if a["altitude_m"] is not None or a.get("band_key")]
    band_input = [a for a in altitude_clean if all(v is not None for v in a["residuals_K"].values())]

    tb_rows, ref_rows = load_computed_rows()
    logger.info(f"computed rows: ToolBox={len(tb_rows)} IAPWS-at-ISA={len(ref_rows)}")
    checks = sanity_checks()
    logger.info(f"unit checks pass: {checks['all_unit_checks_pass']}")
    cons = consistency_check(ref_rows, tb_rows)
    logger.info(f"V4 vs IAPWS-at-ISA max abs diff: {cons['V4_vs_IAPWS_at_ISA_max_abs_K']:.5f} K")
    sens = sensitivity(tb_rows)
    bands = band_summary(band_input)

    (RES / "measured_records.json").write_text(json.dumps(measured, indent=2))
    (RES / "residuals_thermo.json").write_text(json.dumps({"n": len(thermo), "rows": thermo,
        "note": "Thermodynamic-only pass on measured records. n=0: no measured boiling observation cited."}, indent=2))
    (RES / "residuals_altitude.json").write_text(json.dumps({"n": len(altitude), "rows": altitude,
        "note": "Altitude pass on measured records with altitude given. n=0: no measured records cited."}, indent=2))
    (RES / "band_summary.json").write_text(json.dumps(bands, indent=2))
    (RES / "sanity_checks.json").write_text(json.dumps({"unit_checks": checks, "consistency_computed": {
        k: v for k, v in cons.items() if k not in ("ToolBox_detail", "V4_detail")},
        "sensitivity_computed": sens}, indent=2, default=float))
    (RES / "consistency_detail.json").write_text(json.dumps({"V4_detail": cons["V4_detail"],
        "ToolBox_detail": cons["ToolBox_detail"]}, indent=2))

    # method_out.json in exp_gen_sol_out format. Measured set is empty, so it has no dataset entry
    # (the schema requires >= 1 example); its n = 0 is recorded in metadata.
    variants = ["V1_iso_CC", "V2_iso_IAPWS", "V3_ISA_CC", "V4_ISA_IAPWS"]
    tb_examples = []
    for row, d in zip(cons["ToolBox_detail"], [variant_predictions(r["altitude_m"]) for r in tb_rows]):
        tb_examples.append({
            "input": json.dumps({"altitude_m": row["altitude_m"]}),
            "output": f"{row['tb_T_K']:.2f}",
            "metadata_source": "engtoolbox_boiling_altitude",
            "metadata_data_type": "computed_unknown_method",
            "metadata_role": "computed consistency check, not measured",
            **{f"predict_{v}": f"{d[v]:.4f}" for v in variants},
        })
    ref_examples = []
    for row in cons["V4_detail"]:
        ref_examples.append({
            "input": json.dumps({"altitude_m": row["altitude_m"]}),
            "output": f"{row['ref_T_K']:.3f}",
            "metadata_source": "iapws_if97_saturation",
            "metadata_data_type": "computed_reference",
            "metadata_role": "V4 reproduction check, not measured",
            "predict_V4_ISA_IAPWS": f"{row['V4_pred_K']:.4f}",
        })
    out = {
        "metadata": {
            "method_name": "Barometric and constant-enthalpy models of water boiling point (2x2 variants)",
            "description": "Measured set n=0 above and below 5 km: no measured boiling observation could be cited after a bounded search. Only computed consistency checks are reported.",
            "measured_n": len(measured),
            "variants": {"V1": "iso + CC", "V2": "iso + IAPWS-97", "V3": "ISA + CC", "V4": "ISA + IAPWS-97"},
            "constants": {"R": R, "M": M, "g": G, "T0": T0, "P0": P0, "L": LAPSE, "Tref_K": TREF, "Pref_Pa": PREF, "dH_J_per_mol": DH},
            "unit_checks_pass": checks["all_unit_checks_pass"],
            "V4_vs_IAPWS_at_ISA_max_abs_K": cons["V4_vs_IAPWS_at_ISA_max_abs_K"],
            "toolbox_residual_summary_computed": {k: v for k, v in cons.items() if k.startswith("ToolBox_resid")},
            "sensitivity_computed": sens,
            "band_summary_measured": bands,
            "note_iapws_bracket": "IAPWS solve bracket 273.16-647.0 K; plan's 373.946 K upper bound replaced (it is ~100.8 C, not the critical point).",
        },
        "datasets": [
            {"dataset": "engtoolbox_boiling_altitude_computed_check", "examples": tb_examples},
            {"dataset": "iapws_if97_at_isa_consistency_computed", "examples": ref_examples},
        ],
    }
    (WS / "method_out.json").write_text(json.dumps(out, indent=2, default=float))
    logger.info("wrote results and method_out.json")


if __name__ == "__main__":
    main()
