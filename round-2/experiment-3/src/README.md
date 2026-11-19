# Water boiling point vs barometric models: measured-comparison attempt

## What was done
A 2x2 set of barometric variants (isothermal or ISA pressure path, crossed with constant-enthalpy Clausius-Clapeyron or IAPWS-97 saturation) was implemented in `method.py`, together with unit checks and a computed consistency check against the reference dataset.

**Measured outcome: no measured records.** A bounded search (two rounds: Osborne, Stimson and Ginnings 1939; high-altitude station and summit measurements; Keene 1995) found the NIST RP1229 paper (J. Research NBS 23, 261, 1939) but no transcribable boiling-temperature-versus-pressure rows, no measured rows above 5 km, and no Keene 1995 text. The Everest and Pikes Peak figures found were calculations, not observations, and were excluded. Following the plan's fallback, `results/measured_records.json` is an empty list. Every band has n = 0 and no residual statistics are reported.

The question "how well does the barometric formula predict measured boiling points at altitude" therefore has no answer from this run. The result is a null outcome, not a finding.

## Computed checks (not measured evidence)
- Unit checks pass: T_cc(101325 Pa) = 373.124 K; T_IAPWS(101325 Pa) = 373.1243 K; ISA inversion round trip < 1e-11 m; P_isa(11 km) = 22632.6 Pa; Clausius-Clapeyron round trip exact.
- V4 (ISA + IAPWS-97) reproduces the 125 computed IAPWS-at-ISA reference rows to within 0.00094 K.
- The Engineering ToolBox table (computed_unknown_method) differs from the model variants by these amounts (K, model minus table): V1 bias +0.37 (max 0.57); V3 bias -0.65 (max 2.77); V4 bias -0.30 (max 1.94). The ToolBox table is treated as computed and is not evidence.
- Anchor 373.15 K changes V1 and V3 by about +0.024 K. dH plus or minus 500 J/mol changes them by about +/-0.17 K (max 0.36 K).

## Layout
- `method.py`: implementation of the variants, unit checks, consistency and sensitivity checks, and output writing.
- `data/full_data_out.json`, `mini_data_out.json`, `preview_data_out.json`: copies of the reference dataset (`art_39-uxNptYM5-`). These contain no measured rows.
- `results/measured_records.json`: empty measured set, n = 0 (kept).
- `results/residuals_thermo.json`, `results/residuals_altitude.json`: n = 0 (no measured rows).
- `results/band_summary.json`: per-band n and statistics; n = 0 everywhere.
- `results/sanity_checks.json`: unit checks, consistency and sensitivity summaries.
- `results/consistency_detail.json`: row-level computed comparisons.
- `method_out.json`: full output in exp_gen_sol_out format (passes schema validation).
- `mini_method_out.json`, `preview_method_out.json`: mini (3 examples per dataset) and preview (strings truncated to 200 characters) variants, schema-valid.
- `logs/run.log`: run log.
- `.venv/`: Python environment (regenerable, see manifest).

## How to run
    uv venv .venv --python 3.12 && uv pip install --python .venv/bin/python iapws==1.5.5 scipy numpy jsonschema loguru
    .venv/bin/python -I method.py

## Notes on deviations from the plan
- The IAPWS solve bracket is 273.16 to 647.0 K. The plan's upper bound of 373.946 K is about 100.8 C, not the critical point, and does not bracket the saturation pressure.
- Bands 3-6 km and 5-6 km overlap, as the plan specifies; a record can fall in both.
- No figures were rendered: with zero measured rows there is no measured data to plot, and the computed checks are summarised in tables.

## Restoring removed files
- `.venv/`: `uv venv .venv --python 3.12 && uv pip install --python .venv/bin/python iapws==1.5.5 scipy numpy jsonschema loguru`

## No measured comparison
This run tested only computed quantities. It did not test the barometric formula against any measured boiling observation, at any altitude, above or below 5 km. The 5 km and above question is untested. The result must be reported as a null outcome, with n = 0 for every band. Keene (1995) was not located, and its contents are not claimed.
