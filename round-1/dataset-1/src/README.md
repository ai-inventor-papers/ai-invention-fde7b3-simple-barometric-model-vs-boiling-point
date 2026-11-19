# Water boiling point versus pressure: reference table

## What was done
Built a reference table of water boiling temperature against altitude and pressure, for testing the simple barometric formula against published values.

- **Measured rows: 0.** The planned measured sources (Osborne, Stimson and Ginnings 1939 tables; CRC Handbook vapour-pressure table; Keene 1995) were located as NIST/other records (e.g. NIST J. Res. RP1229, nvlpubs.nist.gov/nistpubs/jres/23/jresv23n2p261_a1b.pdf), but the table in the OCR text could not be transcribed reliably, so no row was entered. Per the rule against unverifiable rows, none was invented. **The measured shortfall is total; the downstream residual test has no measured points yet.**
- **Computed reference rows (125):** IAPWS-IF97 saturation temperature at the ISA pressure for each altitude, using the `iapws` package v1.5.5. These are model values, not measurements.
- **Benchmark rows (125):** Engineering ToolBox "Water - Boiling Points vs. Altitude" (https://www.engineeringtoolbox.com/boiling-points-water-altitude-d_1344.html, accessed 2026-11-19). The method is not stated, so `data_type = computed_unknown_method`.

## Key check
The ToolBox table agrees with IAPWS-at-ISA to within -0.3 to +1.9 K (median +0.02 K, n = 125 matched altitudes). It is therefore most likely computed from a standard atmosphere, and it is not independent evidence.

## Layout
- `build_dataset.py`: parses the ToolBox table and writes the full table with IAPWS reference rows.
- `validate_and_split.py`: checks the full table against the JSON schema, writes mini and preview variants, and reports the ToolBox vs IAPWS gap.
- `temp/raw/engtoolbox.md`: fetched ToolBox page text (regenerable from the URL above; text file, kept).
- `temp/raw/osborne1939_head.md`: fetched header of the NIST RP1229 PDF (text, kept for provenance).
- `temp/datasets/boiling_point_pressure_full.json`: full table (250 rows).
- `temp/datasets/mini_boiling_point_pressure.json`, `temp/datasets/preview_boiling_point_pressure.json`: first 20 and 5 rows per data_type.
- `temp/datasets/mini_computed_*.json`: per-type mini files.

Columns: altitude_m, pressure_Pa, boiling_T_K, source_id, data_type, method_note, reference_pressure_note, citation, raw_value, raw_unit. Pressure is null for ToolBox benchmark rows, because the source gives altitude only.

## Restoring removed files
- `.venv/` (Python environment): `uv venv .venv --python 3.12 && uv pip install --python .venv/bin/python iapws pymupdf python-dotenv jsonschema requests html2text`

## Limitations
- No measured data, so the question "how well does the barometric formula predict published measurements" cannot be answered from this table.
- Altitude-to-pressure for reference rows uses the ISA model, not station pressure.

## Standardized output (exp_sel_data_out format)
- `data.py`: converts the table into `full_data_out.json`, grouped by source (`engtoolbox_boiling_altitude`: 125 examples; `iapws_if97_saturation`: 125 examples). One example per row. `input` is a JSON string of altitude and pressure; `output` is boiling T in K.
- Validated against `exp_sel_data_out.json` with 0 errors.
- `mini_data_out.json` (first 3 examples per source) and `preview_data_out.json` (first 10, strings truncated to 200 chars), both written by `make_variants.py`.
- Only two sources exist, so no 8-to-4 dataset selection was made; both sources are kept, and the benchmark group is labelled as such in each example's `metadata_data_type`.
