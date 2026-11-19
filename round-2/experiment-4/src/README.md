# Splitting the boiling-point model error by cause

This artifact attributes the residual of a barometric boiling-point model of water to two causes: the anchor value (373.124 K versus 373.15 K) and the temperature dependence of enthalpy (constant versus effective versus IAPWS-IF97 inversion). It also reports the atmosphere effect (isothermal versus ISA pressure) that dominates the result.

**Scope.** Every reference is a COMPUTED reference: the Engineering ToolBox table (method not stated) and IAPWS-IF97 saturation at ISA pressures. No measured boiling points are used, so no accuracy claim against measurement is made or implied. Results are agreement statistics only.

## Method

Two pressure models × four thermodynamic variants, residuals (model minus reference) for every altitude in the dependency, reported by altitude band as n, bias, MAE and maximum absolute error.

- Pressure, isothermal: P = P0 exp(−g0 M h / (R T0)).
- Pressure, ISA troposphere: P = P0 (1 − L h / T0)^(g0 M / (R L)), valid to 11 km.
- Variant A (constant enthalpy, anchor Ta): 1/Tb = 1/Ta − (R/ΔH) ln(P/P0), with Ta = 373.124 K and Ta = 373.15 K, ΔH = 40650 J/mol.
- Variant B (effective constant enthalpy): ΔH_eff fitted to IAPWS-IF97 saturation over 343.15–373.15 K (ΔH_eff ≈ 41 830 J/mol), then applied with Ta = 373.124 K.
- Variant C (IAPWS-IF97 inversion): root of P_sat(T) − P on [290, 380] K with `brentq`.
- Bands: 0–3 km (0 ≤ h < 3000), 3–6 km (3000 ≤ h < 6000), 6–9 km (6000 ≤ h ≤ 9144). The 6–9 km band includes 9144 m, as the plan specifies.

## Layout

- `method.py` — the full analysis (loads the dependency, checks it, computes models, residuals, band statistics, attribution, and checks; writes all results).
- `data/full_data_out.json` — copy of the dataset dependency (`art_39-uxNptYM5-`, SHA-256 `359dd085f0abc842c704fa9d2bf50b162093478d2c6eb7de5c8b7426bf18088b`). 250 rows: 125 ToolBox, 125 IAPWS-at-ISA.
- `results/constants_citation.json` — constants and their sources, and which were verified by fetch.
- `results/residuals.json` — per altitude: pressures, both references, all 8 model values and residuals against both references.
- `results/band_summary.json` — n, bias, MAE and max absolute error per band, plus all attribution quantities.
- `results/sensitivity.md` — tables of bias, anchor effect, enthalpy effect (Z), atmosphere effect and sign-change check.
- `results/implementation_checks.json` — values of the eight testing-plan checks and the grid note.
- `method_out.json` (plus `full_`, `mini_`, `preview_` variants) — per-altitude examples in the `exp_gen_sol_out` format; schema-valid.
- `reproducibility.md` — commands and environment.
- `logs/run.log` — run log.

## Headline results (ToolBox reference, 6–9 km, model minus reference, K)

| Atmosphere | A373.124 | A373.15 | B effective | C IAPWS inversion |
|---|---|---|---|---|
| isothermal | +0.470 | +0.493 | +1.102 | +1.044 |
| ISA | −1.716 | −1.694 | −1.031 | −1.071 |

- **Anchor:** the anchor shift is −0.023 to −0.026 K everywhere, which is 1–5% of the isothermal bias in the 3–9 km bands (11% at 0–3 km, where the bias is smallest) and up to ~8% of the ISA bias in the 3–6 km band. It is a minor term.
- **Enthalpy:** in the ISA model the IAPWS-consistent variants remove about 37–40% of the 6–9 km bias (Z). In the isothermal model they increase the bias (negative Z).
- **Atmosphere:** ISA minus isothermal is −2.19 K in 6–9 km (about −0.11 K at 0–3 km). It dominates the residual. No sign change in the ISA-minus-isothermal model difference occurs over 0–9144 m.
- Against the IAPWS-at-ISA reference the ISA variant B and C numbers are within 0.06 K of zero bias in the 6–9 km band, but variant C is zero by construction, so that row is a reproduction and not a finding.

## Restoring removed files

No files were marked for deletion. The only large directory is the `.venv/` created for this run. It is rebuilt with:

```
uv venv .venv --python=3.12
uv pip install --python=.venv/bin/python numpy scipy iapws loguru jsonschema
```

## Limitations

- Computed references only; no measured boiling points, so no accuracy claim.
- Standard atmosphere only; station pressure variation (weather) is not simulated.
- Variant B is fitted to the same IAPWS curve that defines the reference; it is not independent.
- The dataset altitudes (125 points, −305 to 9144 m) were used directly. The plan's grid (linspace 0–8992 m plus 9144 m) was not used, as the plan allows.
- Constants: P0, T0 and L were checked against a fetched secondary source (Wikipedia, citing ISO 2533:1975). The standard gravity, CODATA R and ΔH values were not fetched from a primary document; see `results/constants_citation.json`.
- Band 6–9 km includes 9144 m (stated in the plan).
