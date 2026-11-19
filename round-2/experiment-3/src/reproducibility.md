# Reproducibility

## 1. Get the artifact
This folder is published as one folder of a public GitHub repository. Clone the repository, then `cd` into this folder (the folder that contains `method.py`).

## 2. Environment
- Python 3.12 (`requires-python >= 3.12`).
- Pinned dependencies are in `pyproject.toml` (iapws 1.5.5, scipy 1.18.1, numpy 2.5.5, jsonschema 4.26.0, loguru 0.8.0 and their transitive pins).
- Commands:
  ```
  uv venv .venv --python 3.12
  uv pip install --python .venv/bin/python -e .
  ```
  (or `uv pip install --python .venv/bin/python -r` with the pins from `pyproject.toml`).
- The run was executed on macOS (Apple silicon) with uv 0.6.14. The code is CPU-only; no GPU is used. Linux should work with the same pins, but this was not run on Linux.

## 3. Inputs, downloads and keys
- Input: `data/full_data_out.json` is a local copy of the output of dataset artifact `art_39-uxNptYM5-` (reference table, 250 computed rows, zero measured rows). A reader can take the same file from that artifact's published folder, which the repository publishes as a sibling.
- Network: the run fetched web pages for a bounded search of measured sources; no data was downloaded by the code. The measured set is empty, so no web data enters the computation.
- No API keys, environment variables or LLM calls are used.

## 4. Commands, in order
1. `.venv/bin/python -I method.py` (deterministic, no seeds; about 3 seconds). It writes `results/*.json`, `method_out.json`, and `logs/run.log`.
2. `.venv/bin/python -I audit/rederive.py` (independent check of the headline numbers; reads the raw dataset JSON, not method.py's output).
3. Mini and preview variants: first 3 examples per dataset (`mini_method_out.json`) and the same with strings cut to 200 characters (`preview_method_out.json`). These were written with a short Python script, because the aii-json server-backed formatter was unavailable in this environment. `full_method_out.json` is a copy of `method_out.json`.
4. Schema check: `method_out.json`, `mini_method_out.json` and `preview_method_out.json` validate against the `exp_gen_sol_out` schema with jsonschema (run with `-I`).

Runtime: about 3 seconds for `method.py`; about 1 second for `audit/rederive.py`.

## 5. Expected outputs and where they appear
- `results/measured_records.json`: `[]` (n = 0). No measured boiling observation above or below 5 km was cited.
- `results/band_summary.json`: every band has n = 0 and the text "n=0, no statistic". No residual statistics are reported.
- `results/sanity_checks.json`: unit checks pass; V4 reproduces the stored IAPWS-at-ISA rows to 0.00094 K; ToolBox residuals (computed, not measured) V1 bias +0.37 K, V3 bias -0.65 K, V4 bias -0.30 K; anchor and dH sensitivity.
- `results/residuals_thermo.json`, `results/residuals_altitude.json`: n = 0.
- `method_out.json`, `full_method_out.json`, `mini_method_out.json`, `preview_method_out.json`: the same content at three sizes.
- These numbers are the basis for the README section "Computed checks (not measured evidence)". The paper's headline result is the null outcome (n = 0 for every band).

## Measured outcome and scope
No measured comparison was performed. The barometric formula was not tested against any measured boiling observation at any altitude. Keene (1995) was not located. Osborne, Stimson and Ginnings (1939) was located (NIST RP1229) but its boiling-point table was not transcribed. The results are a null outcome, not a finding.
