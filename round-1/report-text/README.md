# Barometric formula and the boiling point of water at altitude: internal research report

This directory is the run's internal research report for iteration 1. It is a chronological lab notebook, not the paper. The question is how well the simple barometric formula predicts the boiling point of water at altitude, compared with published measurements.

## Result in one paragraph

The Engineering ToolBox boiling-point table has no stated method. On the evidence here it is a computed reference, not a measurement: it tracks an IAPWS-IF97 curve at standard-atmosphere pressures to within 0.31 K below 5 km, and it departs by up to 1.9 K at 9 km. The isothermal model with constant enthalpy of vaporisation stays within 0.6 K of that table from sea level to 9 km. No measured boiling-point and station-pressure pairs were found, so the report makes no accuracy claim against measurement.

## Layout

- `paper_draft.md`: the report. Framing, iteration 1 section, closing section, references.
- `references.bib`: BibTeX for the cited sources. One entry is fetched from Semantic Scholar (Wagner and Pruss, 2002); two web sources are hand-written `@misc` entries with access dates.
- `references.json`: the fetch record for the fetched entry.
- `figures/fig1_spec.json`: chart spec for Figure 1, copied from the experiment's residual specification.
- `figures/fig1_v0.png` and `figures/fig1_v0.pdf`: Figure 1, rendered with the data-figure generator from the spec.
- `domain_terms.json`: the field's vocabulary used in the report, with a gloss for each term.
- `field_extras.json`: empty list. No exemplar papers were read in this iteration.
- `.aii/manifest.yaml`: no heavy paths in this directory, so no entries.

## Source artifacts

The numbers in the report are read from three artifact workspaces, which are not part of this directory:

- Research artifact `art_meMsxdA1r_bm`: provenance check of the benchmark table.
- Dataset artifact `art_39-uxNptYM5-`: 250-row reference table, with 125 Engineering ToolBox rows and 125 IAPWS-IF97 rows at ISA pressures.
- Experiment artifact `art_SznfD9DKXm93`: four model variants, band statistics, sensitivity and the residual specification.

## How to run

The report is a document. To check its numbers, open the experiment artifact's `results/summary_by_band.json`, `results/sensitivity.json` and `results/residuals.json`, and the dataset artifact's `full_data_out.json`.

To re-render Figure 1 with the data-figure generator from the skill:

```
python <aii-data-fig-gen>/scripts/chart_gen.py --spec figures/fig1_spec.json --out figures/fig1_v0
```

## Restoring removed files

No files in this directory are marked for deletion. The artifact workspaces hold their own restoration commands in their `reproducibility.md` files.
