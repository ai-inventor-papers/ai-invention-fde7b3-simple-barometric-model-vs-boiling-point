# Reproducibility

This folder is one artifact of a public GitHub repository. Start from a clone of that repository and `cd` into this folder (the folder that contains `method.py`).

## 1. What was actually run

- Machine: Apple silicon Mac (macOS, arm64), CPU only. No GPU, no LLM calls, no network calls during the analysis. Runtime is about 5 seconds.
- Python 3.12.10, installed and managed by `uv`.
- Reproduction on Ubuntu has NOT been tested. The code uses only `pathlib` and relative paths, so it should run on Ubuntu with Python 3.12, but this is not verified.

## 2. System packages and Python environment

No system packages are needed beyond Python 3.12 and `uv`.

```
uv venv .venv --python=3.12
uv pip install --python=.venv/bin/python numpy==2.5.5 scipy==1.18.1 iapws==1.5.5 loguru==0.8.0 jsonschema==4.26.0
```

`pyproject.toml` pins the exact versions used:

| Package | Version |
|---|---|
| numpy | 2.5.5 |
| scipy | 1.18.1 |
| iapws | 1.5.5 |
| loguru | 0.8.0 |
| jsonschema | 4.26.0 |

Transitive packages from the same environment (for the record): attrs 26.1.0, jsonschema-specifications 2025.9.1, referencing 0.37.0, rpds-py 2026.9.1, typing-extensions 4.16.0. Torch is not used and must not be installed.

## 3. Inputs, downloads, keys

- Input: `data/full_data_out.json`. This is a copy of the output of the dataset artifact `art_39-uxNptYM5-` (water boiling point versus pressure reference table). SHA-256: `359dd085f0abc842c704fa9d2bf50b162093478d2c6eb7de5c8b7426bf18088b`. It contains 125 rows from the Engineering ToolBox table and 125 rows of IAPWS-IF97 saturation at ISA pressures, both computed references, zero measured rows.
- No input is a user upload. No model, checkpoint or dataset download is needed.
- No API keys or environment variables are required.

## 4. Commands, in order

```
.venv/bin/python method.py                  # full analysis, about 5 s; writes results/, method_out.json, logs/run.log
.venv/bin/python -I audit/rederive.py       # independent re-derivation of headline numbers; prints to stdout
```

`method.py` runs the implementation checks from the testing plan before the results are written; they are stored in `results/implementation_checks.json`. Check 6 in that file is a reproduction of the earlier round's biases, not a fitted value.

The mini and preview variants were created by taking the first three examples of `method_out.json` and truncating strings to 200 characters. The `aii-json` format script could not run in this environment (permission error reading the skill folder), so those two files were made by an equivalent step and then schema-checked against `exp_gen_sol_out`. The schema check also passed on the full file.

Seeds: none. The analysis is deterministic.

## 5. What a reader should get

- `results/constants_citation.json`: constants and sources. Sea-level pressure, sea-level temperature and lapse rate were checked against a secondary source (Wikipedia, citing ISO 2533:1975); gravity, the gas constant and the enthalpy of vaporisation were not fetched from a primary document.
- `results/residuals.json`: every altitude, both pressure models, four variants, residuals against both computed references.
- `results/band_summary.json`: n, bias, MAE and max absolute error for each band, reference, atmosphere and variant, and the attribution quantities.
- `results/sensitivity.md`: the tables. Headline values against the ToolBox reference, 6–9 km, model minus reference:
  - isothermal: A373.124 +0.470 K, A373.15 +0.493 K, B +1.102 K, C +1.044 K
  - ISA: A373.124 −1.716 K, A373.15 −1.694 K, B −1.031 K, C −1.071 K
  - Anchor shift in 6–9 km is about −0.023 K; enthalpy effect Z is about 37–40% for ISA and negative for isothermal; ISA minus isothermal is −2.19 K.
- `results/implementation_checks.json`: the testing-plan values.
- `audit/rederive_out.txt`: output of the independent re-derivation. It reproduces the 6–9 km biases and the Z and anchor values from the raw residual rows (pressures and model temperatures re-derived in log space and by a rearranged formula). Maximum discrepancy from the stored values is about 1e-10 K for pressures and 1e-13 K for the constant-enthalpy temperatures.
- `method_out.json` (plus `full_`, `mini_`, `preview_` variants): per-altitude examples in the `exp_gen_sol_out` format.

These numbers are agreement statistics against COMPUTED references. They are not accuracy claims against measured boiling points, and the paper cannot use them for that.

## 6. Limitations of this reproduction

- Only the constant-enthalpy (A) results and the pressures were re-derived independently. Variants B and C were read from the stored file, not recomputed, because they depend on the IAPWS-IF97 saturation function from the `iapws` package.
- No statistical test is used, so no shuffled-input placebo was run.
- Standard atmosphere only; no station pressure variation.

## 7. Restoring removed files

Nothing was marked for deletion. The only heavy path is `.venv/`, which is rebuilt with the commands in section 2.
