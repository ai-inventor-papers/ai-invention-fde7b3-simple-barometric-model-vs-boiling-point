# Sensitivity: anchor, enthalpy and atmosphere effects

All statistics are agreement statistics against COMPUTED references, not measured boiling points.

Effective enthalpy from fit (variant B): dH_eff = 41829.7 J/mol (fit RMS lnP = 1.15e-03).

## Reference: Engineering ToolBox table (computed_unknown_method)

### Bias (model minus reference, K) by band

| Atmosphere | Variant | 0-3 km | 3-6 km | 6-9 km | 0-9144 m |
|---|---|---|---|---|---|
| isothermal | A373.124 | +0.202 (n=40) | +0.481 (n=39) | +0.470 (n=42) | +0.385 (n=121) |
| isothermal | A373.15 | +0.227 (n=40) | +0.505 (n=39) | +0.493 (n=42) | +0.409 (n=121) |
| isothermal | B_effective | +0.338 (n=40) | +0.876 (n=39) | +1.102 (n=42) | +0.777 (n=121) |
| isothermal | C_iapws_inversion | +0.292 (n=40) | +0.788 (n=39) | +1.044 (n=42) | +0.713 (n=121) |
| isa | A373.124 | +0.089 (n=40) | -0.307 (n=39) | -1.716 (n=42) | -0.665 (n=121) |
| isa | A373.15 | +0.114 (n=40) | -0.283 (n=39) | -1.694 (n=42) | -0.642 (n=121) |
| isa | B_effective | +0.229 (n=40) | +0.108 (n=39) | -1.031 (n=42) | -0.248 (n=121) |
| isa | C_iapws_inversion | +0.182 (n=40) | +0.021 (n=39) | -1.071 (n=42) | -0.305 (n=121) |

### Anchor effect: bias(A373.124) minus bias(A373.15), K (percent of bias(A373.15))

| Atmosphere | 0-3 km | 3-6 km | 6-9 km |
|---|---|---|---|
| isothermal | -0.0253 (-11.2%) | -0.0240 (-4.8%) | -0.0228 (-4.6%) |
| isa | -0.0253 (-22.2%) | -0.0239 (+8.4%) | -0.0225 (+1.3%) |

### Enthalpy effect in 6-9 km: Z = 1 - |bias(B or C)| / |bias(A373.124)|

| Atmosphere | Z for B (%) | Z for C (%) |
|---|---|---|
| isothermal | -134.5 | -122.2 |
| isa | 39.9 | 37.6 |

### Atmosphere effect: ISA minus isothermal bias, K

| Variant | 0-3 km | 3-6 km | 6-9 km |
|---|---|---|---|
| A373.124 | -0.113 | -0.788 | -2.186 |
| A373.15 | -0.113 | -0.788 | -2.187 |
| B_effective | -0.110 | -0.768 | -2.133 |
| C_iapws_inversion | -0.110 | -0.767 | -2.115 |

## Reference: IAPWS-IF97 saturation at ISA pressures (computed_reference)

### Bias (model minus reference, K) by band

| Atmosphere | Variant | 0-3 km | 3-6 km | 6-9 km | 0-9144 m |
|---|---|---|---|---|---|
| isothermal | A373.124 | +0.020 (n=40) | +0.461 (n=39) | +1.541 (n=42) | +0.690 (n=121) |
| isothermal | A373.15 | +0.045 (n=40) | +0.485 (n=39) | +1.564 (n=42) | +0.714 (n=121) |
| isothermal | B_effective | +0.157 (n=40) | +0.855 (n=39) | +2.173 (n=42) | +1.082 (n=121) |
| isothermal | C_iapws_inversion | +0.111 (n=40) | +0.768 (n=39) | +2.116 (n=42) | +1.018 (n=121) |
| isa | A373.124 | -0.093 (n=40) | -0.328 (n=39) | -0.645 (n=42) | -0.360 (n=121) |
| isa | A373.15 | -0.067 (n=40) | -0.304 (n=39) | -0.623 (n=42) | -0.336 (n=121) |
| isa | B_effective | +0.047 (n=40) | +0.087 (n=39) | +0.040 (n=42) | +0.058 (n=121) |
| isa | C_iapws_inversion | +0.000 (n=40) | +0.000 (n=39) | +0.000 (n=42) | +0.000 (n=121) |

### Anchor effect: bias(A373.124) minus bias(A373.15), K (percent of bias(A373.15))

| Atmosphere | 0-3 km | 3-6 km | 6-9 km |
|---|---|---|---|
| isothermal | -0.0253 (n/a) | -0.0240 (-5.0%) | -0.0228 (-1.5%) |
| isa | -0.0253 (+37.5%) | -0.0239 (+7.9%) | -0.0225 (+3.6%) |

### Enthalpy effect in 6-9 km: Z = 1 - |bias(B or C)| / |bias(A373.124)|

| Atmosphere | Z for B (%) | Z for C (%) |
|---|---|---|
| isothermal | -41.0 | -37.3 |
| isa | 93.7 | 99.9 |

### Atmosphere effect: ISA minus isothermal bias, K

| Variant | 0-3 km | 3-6 km | 6-9 km |
|---|---|---|---|
| A373.124 | -0.113 | -0.788 | -2.186 |
| A373.15 | -0.113 | -0.788 | -2.187 |
| B_effective | -0.110 | -0.768 | -2.133 |
| C_iapws_inversion | -0.110 | -0.767 | -2.115 |

## Sign changes of ISA minus isothermal model Tb

- A373.124: crossovers in 0-9144 m = none; range of difference -3.130 to +0.000 K
- A373.15: crossovers in 0-9144 m = none; range of difference -3.130 to +0.000 K
- B_effective: crossovers in 0-9144 m = none; range of difference -3.056 to +0.000 K
- C_iapws_inversion: crossovers in 0-9144 m = none; range of difference -3.020 to +0.000 K

## Limitations

- Computed references only; no measured station-pressure data were available.
- Standard atmosphere only; no weather-driven pressure variation.
- Variant B is fitted to the same IAPWS curve that defines the reference, so it is not independent.
- The 6-9 km band includes 9144 m.
- Variant C against the IAPWS-at-ISA reference is zero by construction (same calculation, check 5). It is a reproduction, not evidence, and it is not an attribution result.
- Variant B against the IAPWS-at-ISA reference is not independent (same IAPWS curve).
