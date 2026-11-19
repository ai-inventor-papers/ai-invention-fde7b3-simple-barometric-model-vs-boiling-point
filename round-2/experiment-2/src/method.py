"""Boiling-point models vs measured data, by altitude band.

Four variants: pressure model (isothermal barometric or ISA) x boiling-temperature
model (constant-enthalpy Clausius-Clapeyron, or IAPWS-IF97 saturation).

Measured set: data/measured_pairs.csv (transcribed from sources). In this round it
has zero rows, so no accuracy claim is made. The computed reference tables in
data/full_data_out.json (ToolBox table, IAPWS-at-ISA rows) are used as CONTEXT ONLY,
never labelled as measured.
"""

import csv
import json
import math
import sys
from pathlib import Path

import numpy as np
import pandas as pd
from iapws import IAPWS97
from loguru import logger

WS = Path(__file__).resolve().parent
DATA = WS / "data" / "full_data_out.json"
MEASURED = WS / "data" / "measured_pairs.csv"
RES = WS / "results"
RES.mkdir(parents=True, exist_ok=True)

# Constants (plan section STEP 3/4)
G = 9.80665
M_AIR = 0.028964
R_GAS = 8.314462
T0 = 288.15
P0 = 101325.0
LAPSE = 0.0065
H_SCALE = R_GAS * T0 / (M_AIR * G)  # about 8434 m
TB_K = 373.124
PB_PA = 101325.0
DH = 40650.0  # J/mol
TB_ALT_K = 373.15  # anchor check
BANDS = [(0.0, 3000.0, "0-3 km"), (3000.0, 6000.0, "3-6 km"), (6000.0, math.inf, "6 km and above")]


def p_iso(h):
    return P0 * math.exp(-h / H_SCALE)


def p_isa(h):
    base = 1.0 - LAPSE * h / T0
    if base <= 0:
        raise ValueError(f"altitude {h} m above ISA troposphere model range")
    return P0 * base ** (G * M_AIR / (R_GAS * LAPSE))


def h_from_p_isa(p):
    return (T0 / LAPSE) * (1.0 - (p / P0) ** (R_GAS * LAPSE / (G * M_AIR)))


def t_ce(p, tb=TB_K):
    return 1.0 / (1.0 / tb - (R_GAS / DH) * math.log(p / PB_PA))


_iapws_cache = {}


def t_iapws(p):
    key = round(p, 3)
    if key not in _iapws_cache:
        _iapws_cache[key] = float(IAPWS97(P=p / 1e6, x=0).T)
    return _iapws_cache[key]


VARIANTS = {
    "V1": ("isothermal", "constant_enthalpy_CC"),
    "V2": ("isothermal", "IAPWS_IF97"),
    "V3": ("ISA", "constant_enthalpy_CC"),
    "V4": ("ISA", "IAPWS_IF97"),
}


def model_T(variant, p):
    _, tmodel = VARIANTS[variant]
    return t_ce(p) if tmodel == "constant_enthalpy_CC" else t_iapws(p)


def model_P(variant, h):
    pmodel, _ = VARIANTS[variant]
    return p_iso(h) if pmodel == "isothermal" else p_isa(h)


def band_of(h):
    for lo, hi, name in BANDS:
        if lo <= h < hi:
            return name
    return None


def stats(res):
    res = np.asarray(res, dtype=float)
    if res.size == 0:
        return {"n": 0, "bias_K": None, "MAE_K": None, "maxAE_K": None}
    return {
        "n": int(res.size),
        "bias_K": float(res.mean()),
        "MAE_K": float(np.abs(res).mean()),
        "maxAE_K": float(np.abs(res).max()),
    }


@logger.catch(reraise=True)
def main() -> None:
    logger.remove()
    logger.add(sys.stdout, level="INFO")
    logger.add(WS / "results" / "run.log", level="DEBUG", rotation="5 MB")

    # Constant sanity checks (T1, T3, T4)
    assert abs(t_ce(PB_PA) - TB_K) < 1e-9, "T1 failed"
    assert abs(p_isa(0.0) - P0) < 1e-6, "T3 failed (sea level)"
    assert abs(p_isa(11000.0) - 22632.0) < 30.0, "T3 failed (11 km)"
    assert abs(p_iso(H_SCALE) - P0 / math.e) < 1e-6, "T3 failed (isothermal)"
    assert abs(760 * 133.322 - 101325) < 1.0, "T4 failed"
    logger.info("Unit checks T1, T3, T4 passed; T2 IAPWS at 101.325 kPa = {:.4f} K", t_iapws(PB_PA))

    # Measured set (may be empty)
    measured = pd.read_csv(MEASURED) if MEASURED.exists() and MEASURED.stat().st_size > 0 else pd.DataFrame()
    n_measured = len(measured)
    logger.info("Measured rows: {}", n_measured)

    # Computed reference rows (context only)
    d = json.loads(DATA.read_text())
    ref_rows = []
    for ds in d["datasets"]:
        for ex in ds["examples"]:
            inp = json.loads(ex["input"])
            ref_rows.append({
                "data_type": ex["metadata_data_type"],
                "source_id": ex["metadata_source_id"],
                "altitude_m": float(inp["altitude_m"]),
                "T_ref_K": float(ex["output"]),
                "pressure_ref_Pa": ex["metadata_pressure_Pa"],
            })
    ref = pd.DataFrame(ref_rows)
    logger.info("Computed reference rows: {} ({})", len(ref), ref["data_type"].value_counts().to_dict())

    # Sea-level confirmation (T7): all variants at 101.325 kPa must match 373.124 K within 0.05 K
    sea = {v: model_T(v, PB_PA) for v in VARIANTS}
    sea_ok = all(abs(t - TB_K) <= 0.05 for t in sea.values())
    logger.info("Sea-level confirmation: {} {}", {k: round(v, 3) for k, v in sea.items()}, "PASS" if sea_ok else "FAIL")

    # Per-row residuals on the computed reference (context)
    rows_out = []
    for _, r in ref.iterrows():
        h = r["altitude_m"]
        rec = {
            "data_type": r["data_type"],
            "source_id": r["source_id"],
            "altitude_m": h,
            "band": band_of(h),
            "T_ref_K": r["T_ref_K"],
        }
        for v in VARIANTS:
            rec[f"{v}_resid_K"] = model_T(v, model_P(v, h)) - r["T_ref_K"]
        rows_out.append(rec)
    per_row = pd.DataFrame(rows_out)

    # Band statistics on the computed reference, labelled as context
    band_rows = []
    for dtype, grp in per_row.groupby("data_type"):
        for _, _, bname in BANDS:
            sub = grp[grp["band"] == bname]
            for v in VARIANTS:
                s = stats(sub[f"{v}_resid_K"].values)
                band_rows.append({"evidence": "computed_context", "data_type": dtype, "band": bname, "variant": v, **s})

    # Measured band statistics: only if rows exist
    meas_band_rows = []
    if n_measured > 0:
        measured["altitude_implied_m"] = measured["pressure_Pa"].apply(h_from_p_isa)
        measured["band"] = measured["altitude_implied_m"].apply(band_of)
        for _, _, bname in BANDS:
            sub = measured[measured["band"] == bname]
            for v in VARIANTS:
                res = [model_T(v, float(p)) - float(t) for p, t in zip(sub["pressure_Pa"], sub["T_measured_K"])]
                meas_band_rows.append({"evidence": "measured", "band": bname, "variant": v, **stats(res)})
    band_df = pd.DataFrame(band_rows + meas_band_rows)
    band_df.to_csv(RES / "band_stats.csv", index=False)
    per_row.to_csv(RES / "per_row_residuals.csv", index=False)

    # Anchor check (V1 and V3 with 373.15 K), computed reference only
    anchor = {}
    for v in ("V1", "V3"):
        diffs = []
        for _, r in per_row.iterrows():
            p = model_P(v, r["altitude_m"])
            diffs.append(t_ce(p, TB_ALT_K) - t_ce(p, TB_K))
        anchor[v] = float(np.mean(diffs))

    # V1 minus V3 sign per computed row
    sign = {"V1_gt_V3": 0, "V1_lt_V3": 0, "equal": 0}
    for _, r in per_row.iterrows():
        diff = r["V1_resid_K"] - r["V3_resid_K"]
        key = "V1_gt_V3" if diff > 1e-9 else ("V1_lt_V3" if diff < -1e-9 else "equal")
        sign[key] += 1

    sources = json.loads((WS / "sources" / "source_log.json").read_text())
    summary = {
        "n_measured": n_measured,
        "sources_retained": sum(1 for s in sources["sources"] if s.get("rows_retained", 0) > 0),
        "measured_claim": "none" if n_measured == 0 else "see band_stats.csv, evidence=measured",
        "sea_level_confirmation_pass": bool(sea_ok),
        "sea_level_T_K": sea,
        "anchor_shift_mean_K_373.15_minus_373.124": anchor,
        "sign_V1_minus_V3_computed_rows": sign,
        "computed_reference_rows": int(len(per_row)),
        "figure": "not drawn: no measured band has n >= 3",
    }
    (RES / "sources_summary.json").write_text(json.dumps(summary, indent=2))

    def example_from_row(row: dict, dataset_label: str) -> dict:
        """One exp_gen_sol_out example: input/output strings plus flat metadata_* and predict_* fields."""
        inp = {"altitude_m": row["altitude_m"]}
        if "pressure_Pa" in row and row.get("pressure_Pa") is not None:
            inp["pressure_Pa"] = float(row["pressure_Pa"])
        ex = {
            "input": json.dumps(inp, sort_keys=True),
            "output": f"{float(row['T_ref_K']):.4f}" if "T_ref_K" in row else f"{float(row['T_measured_K']):.4f}",
            "metadata_dataset_label": dataset_label,
            "metadata_data_type": str(row.get("data_type", "measured")),
            "metadata_source_id": str(row.get("source_id", "")),
            "metadata_band": str(row.get("band")),
        }
        for v in VARIANTS:
            key = f"{v}_resid_K"
            if key in row:
                ex[f"predict_{v}_resid_K"] = f"{float(row[key]):.4f}"
        return ex

    context_examples = [
        example_from_row(r, "computed_reference_context")
        for r in per_row.to_dict(orient="records")
    ]
    datasets = [{"dataset": "computed_reference_context", "examples": context_examples}]
    if n_measured > 0:
        measured_examples = [
            example_from_row(r, "measured")
            for r in measured.to_dict(orient="records")
        ]
        datasets.insert(0, {"dataset": "measured_pairs", "examples": measured_examples})

    out = {
        "metadata": {
            "status": "untested" if n_measured == 0 else "measured_comparison",
            "statement": (
                "No measured comparison; no accuracy claim; computed reference shown only as context."
                if n_measured == 0 else "Measured comparison computed; see band statistics and n per band."
            ),
            "n_measured": n_measured,
            "n_computed_reference": int(len(per_row)),
            "summary": summary,
            "band_statistics": band_df.to_dict(orient="records"),
        },
        "datasets": datasets,
    }

    def trimmed(n: int) -> dict:
        """Same structure, first n examples per dataset."""
        return {
            "metadata": out["metadata"],
            "datasets": [{"dataset": d["dataset"], "examples": d["examples"][:n]} for d in out["datasets"]],
        }

    (WS / "full_method_out.json").write_text(json.dumps(out, indent=2, default=str))
    (WS / "method_out.json").write_text(json.dumps(out, indent=2, default=str))
    (WS / "mini_method_out.json").write_text(json.dumps(trimmed(3), indent=2, default=str))
    (WS / "preview_method_out.json").write_text(json.dumps(trimmed(5), indent=2, default=str))
    logger.info("Wrote outputs. Status: {}, examples: {}", out["metadata"]["status"], sum(len(d["examples"]) for d in datasets))


if __name__ == "__main__":
    main()
