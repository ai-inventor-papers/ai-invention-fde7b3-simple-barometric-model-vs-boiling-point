# Reproducibility

This folder is one artifact of a public repository. Clone the repository, then `cd` into this folder. Every path below is relative to this folder.

## 1. Environment actually used

- Run on: macOS (Darwin 25.4, Apple silicon), CPU only. No GPU, no network services other than the one web fetch described in section 3.
- Python: 3.12.14, managed by `uv` (version 0.6.14).
- Not tested on Ubuntu. The code is pure Python with no OS-specific calls, so it should run on Ubuntu with the same pinned versions, but that has not been verified.

## 2. Create the environment

System packages: none beyond `uv`. Install `uv` from https://docs.astral.sh/uv/.

Install the core pinned packages (the full pinned list in `pyproject.toml` is what was frozen):

```
uv venv --python 3.12 .venv
uv pip install -p .venv/bin/python numpy==2.5.5 scipy==1.18.1 pandas==3.1.1 matplotlib==3.11.2 requests==2.34.2 beautifulsoup4==4.15.0 iapws==1.5.5 loguru==0.8.0 jsonschema==4.26.0
```

The full pinned list (including transitive packages) is in `pyproject.toml`. It was produced with `uv pip freeze -p .venv/bin/python`; the `pip` binary is not present in a `uv` venv, so `.venv/bin/pip freeze` was not usable.

Do not install or upgrade torch; this artifact does not use it.

## 3. Inputs and downloads

- **Engineering ToolBox page (fetched in this run).** Source: https://www.engineeringtoolbox.com/boiling-points-water-altitude-d_1344.html. Fetched 2026-11-19. The raw HTML is saved at `inputs/engineeringtoolbox_raw.html`, and `method.py` parses it into `inputs/engineeringtoolbox_table.csv`. Re-running `method.py` does not re-fetch; it reads the saved HTML. To refresh, save the page again to `inputs/engineeringtoolbox_raw.html`.
- **Measured pairs.** `inputs/measured_pairs.csv` contains only a header. No measured boiling-point / station-pressure pairs could be verified in this run, so the measured comparison is empty (`results/measured_comparison.json` has `n_points = 0`). Keene (1995) was not located.
- **User uploads.** None used. The user-upload folder was checked and is private; nothing from it is published.
- **Environment variables / API keys.** None required. No LLM calls are made.
- **Model downloads.** None. The IAPWS-IF97 saturation curve is computed by the `iapws` package.

## 4. Commands, in order

```
.venv/bin/python method.py            # inputs curation, atmosphere, thermodynamics, four variants, residuals, measured comparison (empty), sensitivity, unit checks
.venv/bin/python make_figure.py       # builds results/residual_vs_altitude_spec.json from results/residuals.json
.venv/bin/python <aii-data-fig-gen>/scripts/chart_gen.py --spec results/residual_vs_altitude_spec.json --out results/fig_residual_vs_altitude
.venv/bin/python make_method_out.py   # writes method_out.json (exp_gen_sol_out format, one example per table altitude)
.venv/bin/python <aii-json>/scripts/aii_json_validate_schema.py --format exp_gen_sol_out --file "$PWD/method_out.json"
.venv/bin/python <aii-json>/scripts/aii_json_format_mini_preview.py --input method_out.json   # full_/mini_/preview_method_out.json
.venv/bin/python audit_rederive.py    # independent re-derivation of the band statistics; prints max difference vs stored results
```

`<aii-data-fig-gen>` and `<aii-json>` are the skill scripts of the AI Inventor pipeline. They are not part of this repository. The figure PDF and PNG are reproduced from the spec with the house generator; to re-draw the figure without the skill, read `results/residual_vs_altitude_spec.json` and plot the four `series` against `x`.

Seeds: none. The computation is deterministic.

Approximate runtime: `method.py` about 4 seconds on the machine above; the whole sequence under 1 minute.

## 5. What a reader should get

- `results/summary_by_band.json`: bias, MAE and max absolute error per variant and band (see the README table). Key values: V1 bias +0.23 / +0.51 / +0.50 K in the 0-3 / 3-6 / 6-9 km bands; V3 bias +0.11 / -0.28 / -1.64 K; V1 minus V3 and V2 minus V4 never change sign (no crossover in 0-9 km).
- `results/predictions.json`: pressure and boiling point on the 91-point grid.
- `results/residuals.json`: residuals at each table altitude (raw values behind the bands and the figure).
- `results/sensitivity.json`: band residuals and crossovers under dH ±500 J/mol and sea-level pressure ±1 kPa.
- `results/sanity_checks.json`: unit checks. Note: IAPWS-IF97 gives a normal boiling point of 373.124 K (99.974 °C), not 100.00 °C; the constant-enthalpy formula gives exactly 100.00 °C because it is anchored there.
- `method_out.json`, `full_method_out.json`, `mini_method_out.json`, `preview_method_out.json`: structured output for the pipeline (exp_gen_sol_out format).
- `results/fig_residual_vs_altitude.pdf` and `.png`: residual vs altitude for the four variants.
- The README in this folder and the `results/` directory are the paper's source for these numbers.

## 6. Checking the numbers

`audit_rederive.py` recomputes every band statistic from `inputs/engineeringtoolbox_table.csv` through a separate code path (closed-form pure-math atmosphere and enthalpy steps, and a hand-written bisection for IAPWS). It agrees with the stored values to 2.5e-13 K. The IAPWS-IF97 function itself comes from the same `iapws` library in both paths, so that library is not independently verified here.

## 7. Restoring removed files

`.venv/` is removed after the round ends. Restore it with `./restore.sh` (see the README).
