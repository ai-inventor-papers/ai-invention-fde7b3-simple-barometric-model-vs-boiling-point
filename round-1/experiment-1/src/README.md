# Boiling point of water vs altitude: four model variants

## What was done

A 2x2 factorial computation of the boiling point of water from 0 to 9 km (91 altitudes, 100 m steps):

| | constant-enthalpy Clausius-Clapeyron (anchored at 373.15 K, 101.325 kPa, dH = 40.65 kJ/mol) | IAPWS-IF97 saturation curve |
|---|---|---|
| isothermal barometric formula (T0 = 288.15 K) | V1 | V2 |
| ISA lapse-rate formula (6.5 K/km) | V3 | V4 |

Residuals (model minus reference, K) are reported by band (0-3, 3-6, 6-9 km) as bias, MAE and maximum absolute error, against the Engineering ToolBox table. The model is evaluated at each table altitude (no interpolation). Sensitivity runs vary dH by ±500 J/mol and sea-level pressure by ±1 kPa.

## Main results (against the Engineering ToolBox table, 0-9 km)

| Variant | 0-3 km bias / max | 3-6 km bias / max | 6-9 km bias / max |
|---|---|---|---|
| V1 iso + const. H | +0.23 / 0.43 | +0.51 / 0.59 | +0.50 / 0.59 |
| V2 iso + IAPWS | +0.29 / 0.59 | +0.79 / 0.98 | +1.04 / 1.12 |
| V3 ISA + const. H | +0.11 / 0.20 | -0.28 / 0.77 | -1.64 / 2.60 |
| V4 ISA + IAPWS | +0.18 / 0.31 | +0.02 / 0.33 | -1.03 / 1.81 |

- The isothermal formula with constant enthalpy (V1) stays within about 0.6 K of the table at all altitudes. The ISA variants drift to about -1 to -2.6 K above 6 km. This means the ISA atmosphere pulls the predicted boiling point below the table at high altitude.
- The table itself is a computed or unstated-method reference, so these residuals measure agreement with that table, not with measurements.
- V1 minus V3 and V2 minus V4 never cross zero in 0-9 km (both positive throughout, zero only at 0 m). No crossover altitude exists in this range.
- The V1-V2 difference grows with altitude (mean -0.07 K at 0-3 km, -0.28 K at 3-6 km, -0.54 K at 6-9 km), which matches the expected behaviour of the constant-enthalpy shortcut.

## Measured-data comparison: NOT performed (no verified pairs)

No independently measured boiling-point / station-pressure pairs could be verified in this run. `inputs/measured_pairs.csv` contains only a header. Specifically:
- Keene (1995) was searched for and not located, so it was not used.
- A Mount Everest summit value (~33.7 kPa, ~70 °C) appears on secondary web pages but could not be traced to a primary source. The cited PMC review contains no barometric or boiling-point values. It was not used.

Consequently `results/measured_comparison.json` has `n_points = 0`. The decisive test in the plan (path i and path ii residuals against measurements) has not been run, so no conclusion about accuracy against measurement is drawn here.

## Verification notes

- Unit checks (`results/sanity_checks.json`) pass. Two expectations in the plan were revised:
  - IAPWS-IF97 gives a normal boiling point of 373.124 K (99.974 °C) at 101.325 kPa, not 100.00 °C. The constant-enthalpy formula gives exactly 100.00 °C because it is anchored there. This 0.026 K offset is why V2 and V4 sit slightly below 100 °C at sea level.
  - The latent heat is checked against the IAPWS steam table (hg - hf at 373.15 K = 40.65 kJ/mol). The ideal-gas form R T² dlnP/dT was rejected because it ignores vapour non-ideality (about 1.6% high).
- IAPWS bracket: the plan's [273.16, 373.15] K was widened to 380 K, so P = 101.325 kPa is inside the bracket. The IAPWS region-4 saturation curve remains valid up to the critical point.
- V4 does not depend on dH (IAPWS is used directly), so its dH sensitivity rows are identical by construction.
- The sensitivity perturbation of "reference pressure" is applied to the sea-level pressure of the atmosphere models only. The thermodynamic anchor stays at 101.325 kPa at 373.15 K.
- The Engineering ToolBox table uses 0.1 K rounding, which produces the small sawtooth in the figure.
- No CoolProp cross-check was done (not installed).
- No statistical tests were run. Band results are descriptive: the grid is deterministic and there are no measured points to test against.

## Layout

- `method.py` — full pipeline: input curation, atmosphere, thermodynamics, variants, residuals, measured comparison, sensitivity, unit checks. Run with `.venv/bin/python method.py`.
- `make_figure.py` — builds the chart spec `results/residual_vs_altitude_spec.json` from `results/residuals.json`.
- `results/fig_residual_vs_altitude.pdf` / `.png` — residual vs altitude for the four variants, rendered with aii-data-fig-gen.
- `results/predictions.json` — pressure and boiling point on the 91-point grid, for each variant.
- `results/residuals.json` — residuals at each Engineering ToolBox altitude (raw values behind the figure and the bands).
- `results/summary_by_band.json` — per-variant band statistics and crossover results.
- `results/measured_comparison.json` — empty by design (see above).
- `results/sensitivity.json` — band statistics and crossovers under dH and P0 perturbations.
- `results/sanity_checks.json` — unit-check values.
- `results/run.log` — log of the last run.
- `inputs/engineeringtoolbox_raw.html` — saved source page (fetched in this run).
- `inputs/engineeringtoolbox_table.csv` — parsed table (altitude_m, bp_C, altitude_ft).
- `inputs/measured_pairs.csv` — header only; no verified pairs.
- `restore.sh` — recreates `.venv/`.

Source page: https://www.engineeringtoolbox.com/boiling-points-water-altitude-d_1344.html

Files kept on the run's volume and not published: none beyond `.venv/` (regenerable, see manifest).

## How to run

```
uv venv .venv && uv pip install -p .venv/bin/python numpy scipy pandas matplotlib requests beautifulsoup4 iapws loguru
.venv/bin/python method.py
.venv/bin/python make_figure.py
.venv/bin/python <aii-data-fig-gen>/scripts/chart_gen.py --spec results/residual_vs_altitude_spec.json --out results/fig_residual_vs_altitude
```

## Restoring removed files

- `.venv/` (regenerable): run `./restore.sh` from this folder. It runs `uv venv --python 3.12 .venv` and installs the pinned packages listed in `pyproject.toml`.

## Structured output and reproducibility

- `method_out.json` (exp_gen_sol_out format): one example per Engineering ToolBox altitude, with the table value, the four variant predictions and residuals. Validated with the aii-json schema. `full_method_out.json`, `mini_method_out.json`, and `preview_method_out.json` are generated from it.
- `reproducibility.md`: the exact commands that were run, pinned versions (`pyproject.toml`), and the environment (macOS, not Ubuntu).
- `audit_rederive.py`: an independent recomputation of the band statistics through a different code path. It matches the stored values to 2.5e-13 K.
