# Reproducibility: boiling-point models vs measured data (gen_art_experiment_2)

## Result status
UNTESTED. The measured set is empty (n_measured = 0). No measured comparison was made and no accuracy claim is made. The computed reference is shown as context only.

## 1. Getting the artifact
This folder is published as one folder of a public GitHub repository. Clone the repository and `cd` into this folder. All paths below are relative to this folder.

## 2. Environment
- Python 3.12 (CPU only; no GPU, no torch).
- Create the venv and install the exact pinned versions listed in `pyproject.toml`:
  ```
  uv venv .venv --python 3.12
  uv pip install --python .venv/bin/python iapws==1.5.5 numpy==2.5.5 pandas==3.1.1 matplotlib==3.11.2 scipy==1.18.1 loguru==0.8.0 contourpy==1.4.0 cycler==0.12.1 fonttools==4.68.0 kiwisolver==1.5.1 packaging==26.3 pillow==13.0.0 pyparsing==3.3.3 python-dateutil==4.0.0 tzdata==2026.6
  ```
- Installed versions (from `uv pip freeze`): iapws 1.5.5, numpy 2.5.5, pandas 3.1.1, matplotlib 3.11.2, scipy 1.18.1, loguru 0.8.0 (full list in pyproject.toml).

## 3. Inputs and environment variables
- `data/full_data_out.json` and `data/preview_data_out.json` are copies of the computed reference from the sibling dataset artifact `art_39-uxNptYM5-` (gen_art_dataset_1). They are included here so the repository runs on its own.
- `data/measured_pairs.csv` is the measured-pair table: header only, zero rows in this round.
- No API keys or environment variables are needed.

## 4. Commands, in order
1. `uv venv .venv --python 3.12` and install the pins (section 2).
2. `.venv/bin/python method.py` — runs the unit checks (T1, T3, T4), the IAPWS check (T2), the sea-level check (T7), and writes results and outputs. Runtime: a few seconds on a laptop CPU.
3. `.venv/bin/python -I audit/rederive.py` — independent re-derivation of the headline band bias for the computed reference (V3, 6 km and above), via brentq root-finding and a shuffled-label placebo.

Seeds: the placebo uses `numpy.random.default_rng(0)`. Everything else is deterministic.

## 5. Expected outputs and where they appear
- `results/band_stats.csv`: band statistics (evidence = computed_context; the measured rows are absent).
- `results/per_row_residuals.csv`: per-row residuals for the 250 computed reference rows.
- `results/sources_summary.json`: n_measured = 0, sea-level check PASS, anchor shift (T_b 373.15 K vs 373.124 K) about +0.024 K, V1 vs V3 sign counts.
- `sources/source_log.json`: source attempts; 0 rows retained.
- `method_out.json` (also `full_method_out.json`, identical), `mini_method_out.json`, `preview_method_out.json`: the structured output, with status "untested".
- The headline context number, V3 bias at 6 km and above = −1.72 K (n = 42, computed reference), was re-derived by `audit/rederive.py`: −1.716 K. This is a computed-reference number, not a measured result.

## 6. Limitations
- No measured boiling-point rows were transcribed. The Osborne, Stimson and Ginnings (1939) PDF returned no readable table text, and the CRC Handbook table and Keene (1995) were not obtained.
- The 6 km and above band has no measured rows.
- The ISA pressure step and the constant-enthalpy model are not checked against measurement here.

## 7. Known deviation from the plan
The aii-json format script could not run on this workspace (it only accepts inputs under its own project root or /tmp, and the workspace is outside both). The full, mini and preview files were produced by method.py with the same truncation rules (3 and 5 items for the per-row and measured lists). `full_method_out.json` is a byte copy of `method_out.json`.
