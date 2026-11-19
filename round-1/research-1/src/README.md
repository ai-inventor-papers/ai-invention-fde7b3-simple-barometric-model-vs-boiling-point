# Barometric formula vs measured boiling point of water

## What this is
A research artifact that checks how a popular Engineering ToolBox table of water's boiling point by altitude was produced, and tests its values against a simple pressure-based model. It also searches for independent measured boiling-point data.

## Layout
- `research_report.md`: short written summary of findings.
- `research_out.json`: structured answer with numbered sources (published result).
- `reproducibility.md`: exact searches, fetches and failures, in order.
- `analysis/cc_check.py`: ISA pressure plus constant-enthalpy Clausius-Clapeyron comparison (runs with `python3 -I analysis/cc_check.py`).
- `.aii/manifest.yaml`: no heavy paths.

## How to run
`python3 -I analysis/cc_check.py` prints altitude, ISA pressure, model boiling point and the ToolBox residual.

## Restoring removed files
Nothing was deleted; no entries are marked for deletion.
