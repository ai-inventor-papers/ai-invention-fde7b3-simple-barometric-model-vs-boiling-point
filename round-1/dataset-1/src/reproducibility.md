# Reproducing the water boiling-point reference table

## 1. Getting the artifact
The workspace is published as one folder of a public GitHub repository. Clone the repository, then `cd` into the folder that contains this file (`gen_art_dataset_1`).

## 2. System and Python
- Ubuntu 22.04 or later; Python 3.12 (the environment was built with CPython 3.12.10, `uv` 0.6.14).
- No GPU, no network needed after the fetched source pages are saved (see step 3).

```bash
uv venv .venv --python 3.12
uv pip install --python .venv/bin/python -r requirements.txt
```
`requirements.txt` holds the same pins as `pyproject.toml`. The packages the scripts import are `iapws==1.5.5` and `jsonschema==4.26.0`; `requests`, `html2text`, and `pymupdf` were used only for fetching. Other packages in `pyproject.toml` came with the shared environment and are not used by the scripts.

## 3. Inputs
- Engineering ToolBox page, "Water - Boiling Points vs. Altitude" (https://www.engineeringtoolbox.com/boiling-points-water-altitude-d_1344.html), fetched 2026-11-19 and saved as `temp/raw/engtoolbox.md`. The repository includes this file, so the fetch step is not needed to rerun the build.
- NIST RP1229 header (Osborne, Stimson, Ginnings 1939 context), saved as `temp/raw/osborne1939_head.md`. It was inspected but **no row was taken from it**, so it does not feed the output.
- No API keys, environment variables, or model downloads are needed.
- No user-uploaded files are used.

## 4. Commands, in order
```bash
.venv/bin/python build_dataset.py        # parse ToolBox table; add IAPWS-IF97 reference rows -> temp/datasets/boiling_point_pressure_full.json
.venv/bin/python validate_and_split.py   # schema check; writes temp/datasets/mini_*.json and preview_*.json; prints ToolBox vs IAPWS gap
.venv/bin/python data.py                 # exp_sel_data_out format -> full_data_out.json
.venv/bin/python make_variants.py        # mini_data_out.json, preview_data_out.json
```
No random seeds are used; the output is deterministic. Runtime is a few seconds on a CPU.

## 5. Expected outputs
- `full_data_out.json`: 250 examples, grouped as `engtoolbox_boiling_altitude` (125, `computed_unknown_method`) and `iapws_if97_saturation` (125, `computed_reference`). Zero measured rows.
- `temp/datasets/boiling_point_pressure_full.json`: the same 250 rows in the flat table format (altitude_m, pressure_Pa, boiling_T_K, source_id, data_type, method_note, reference_pressure_note, citation, raw_value, raw_unit).
- Key number: ToolBox minus IAPWS-at-ISA over 125 matched altitudes: min -0.31 K, median +0.02 K, max +1.94 K, mean +0.30 K. This shows the ToolBox table is likely computed from a standard atmosphere, so it is not independent evidence.
- Measured rows: 0. The barometric-formula comparison therefore cannot be run on measured data from this artifact.

## Restoring removed files
The `.venv/` directory is a regenerable environment. Rebuild it with the commands in section 2.
