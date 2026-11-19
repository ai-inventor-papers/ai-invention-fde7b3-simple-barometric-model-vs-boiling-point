# Barometric formula vs. measured boiling point of water: untested round

**Status: no measured comparison was possible in this round (0 measured rows).** The script computes four model variants (isothermal or ISA pressure, each with constant-enthalpy Clausius-Clapeyron or IAPWS-IF97 saturation) and reports residuals against the computed reference tables as context only. It makes no accuracy claim.

## Layout
- `method.py`: full pipeline (unit checks, variants, residuals, band statistics, outputs).
- `data/measured_pairs.csv`: measured-pair table; header only, zero rows.
- `data/full_data_out.json`, `data/preview_data_out.json`: computed reference inputs (copied from the dataset round).
- `sources/source_log.json`: source attempts and rows retained.
- `results/band_stats.csv`: band statistics (computed context only).
- `results/per_row_residuals.csv`: per-row residuals for the computed reference.
- `results/sources_summary.json`: summary, sea-level check, anchor check, V1 vs V3 sign counts.
- `method_out.json`, `mini_method_out.json`, `preview_method_out.json`: structured outputs.
- `reproducibility.md`: what was run and why the measured set is empty.

## How to run
    uv venv .venv --python 3.12
    uv pip install --python .venv/bin/python iapws numpy pandas matplotlib loguru
    .venv/bin/python method.py

## Restoring removed files
- `.venv/` (Python environment): `uv venv .venv --python 3.12 && uv pip install --python .venv/bin/python iapws numpy pandas matplotlib loguru`

Files kept on the run's volume (not in the published repository): none. All deliverables are text files.

## Also in this folder
- `audit/rederive.py`: independent re-derivation of the headline context number.
- `pyproject.toml`: pinned dependencies.
- `full_method_out.json`: copy of `method_out.json`.
- See `reproducibility.md` for exact steps.
