# Barometric formula and the boiling point of water at altitude: internal research report

## Framing

This run asks how well the simple barometric formula predicts the boiling point of water at altitude, compared with published measurements. The question matters for cooking, sterilisation and physiology at altitude, where practitioners use boiling-point tables to set times and temperatures. The standard textbook model combines an atmospheric pressure profile with a Clausius-Clapeyron equation inversion from pressure to boiling temperature. The run asks whether adding the International Standard Atmosphere (ISA) lapse rate to the pressure profile improves the match, and whether any remaining error comes from the atmosphere or from the thermodynamic step.

The hypothesis under test is stated in the run's hypothesis record. The isothermal pressure profile, combined with a Clausius-Clapeyron equation that holds the molar enthalpy of vaporisation constant, is expected to reproduce a published boiling-point table to within 0.6 K from sea level to 9 km. We call this inversion with a constant molar enthalpy the constant-enthalpy approximation, and we call the model built on it the constant-enthalpy model. The ISA version is expected to be more accurate below 3 km and less accurate above 5 km, and the thermodynamic step is expected to carry most of the error above 5 km. The hypothesis also names an independent measured benchmark as the decisive test. This report records what that test could and could not use.

This is the first iteration. Its section is the whole record so far.

# Iteration 1

## Strategy

The first iteration had three jobs, in order. The first was to establish what the benchmark is. The candidate benchmark is the Engineering ToolBox table, which gives boiling temperature against altitude from sea level to 9144 m [1]. Its page states no method, formula, steam table or measured source. A table with no stated method can be a measurement or a calculation, and the two readings lead to different conclusions, so the run checked the table against a calculation before using it as a reference. The second job was to build the four model variants, so that the atmosphere choice (isothermal or ISA) and the thermodynamic choice (constant enthalpy or the saturation curve of the IAPWS industrial formulation (IAPWS-IF97), which we call the IAPWS curve) could be separated. The third job was to look for measured boiling-point and station-pressure pairs that could serve as the decisive benchmark. The measured search is the step the hypothesis depends on most, so the run recorded its outcome in full.

Three artifacts ran, in this order of dependence. A research artifact read the Engineering ToolBox page and the surrounding literature and reported on provenance [ARTIFACT:art_meMsxdA1r_bm]. A dataset artifact assembled a 250-row reference table, combining the Engineering ToolBox rows with an IAPWS curve computed at ISA pressures [ARTIFACT:art_39-uxNptYM5-]. An experiment artifact computed the four variants, their residuals against the table, band statistics and sensitivity checks [ARTIFACT:art_SznfD9DKXm93]. The experiment ran on the dataset's altitudes, so the dataset is an input to it.

## Artifact 1: provenance of the benchmark table

The research artifact found that the Engineering ToolBox page states no method, formula, steam table or measured dataset. The page gives a citation line and nothing else [1]. The artifact's own calculation, using the ISA pressure relation with a constant-enthalpy Clausius-Clapeyron equation inversion, placed the table above the model by a growing amount above about 4.5 km. It reported residuals of about +0.2 K at 4.3 km rising to about +2.8 K at 9.1 km, with the table higher. Those residuals are reproduced in Table 4 below.

The artifact did not find a measured boiling-point dataset with recorded station pressure. The summit values it found, about 68 to 72 C, come from calculators and physics-education estimates rather than observations. Keene (1995), the measured compilation the hypothesis names, was not located after two rounds of search. An ACS listing for an article on boiling at altitude (DOI 10.1021/ed067p45) returned HTTP 403, so its content is unverified and it is not used here. The IAPWS-95 saturation table in NIST NISTIR 5078 could not be parsed by the fetch tool, so the reference IAPWS inversion was not carried out in this artifact. The IAPWS-95 formulation itself is cited as [2].

The residuals of the research artifact and those of the experiment use different anchors and different sign conventions. The research artifact anchored the enthalpy at 373.124 K and reported table minus model. The experiment anchored at 373.15 K and reports model minus table. Table 4 shows that the research residuals match the experiment's ISA model with constant enthalpy once the sign is reversed. The difference in anchor shifts absolute values by a few hundredths of a kelvin and does not change the pattern.

## Artifact 2: the reference table and its benchmark comparison

The dataset artifact holds 250 rows. The first 125 rows are the Engineering ToolBox values, marked as computed by an unknown method because the page states none. The other 125 rows are IAPWS curve temperatures at ISA standard-atmosphere pressures, marked as computed reference rows [ARTIFACT:art_39-uxNptYM5-]. The table contains zero measured rows. The planned measured sources, Osborne, Stimson and Ginnings (1939) and a CRC Handbook table, were located as records but their values could not be transcribed reliably from the fetched text, so no measured row was added. The file passes schema validation with zero errors.

The dataset's most useful output is a direct comparison of the Engineering ToolBox values with the IAPWS curve at ISA pressures. I recomputed it from the rows. The difference is near zero below about 5 km and grows above it.

Table 3. Engineering ToolBox value minus IAPWS curve temperature at the ISA pressure for the same altitude (K). Source: full_data_out.json, altitudes sampled from the 125 paired rows [ARTIFACT:art_39-uxNptYM5-].

| Altitude (m) | ToolBox minus IAPWS curve at ISA pressure (K) |
|---|---|
| -305 | +0.11 |
| 1219 | -0.22 |
| 2743 | -0.23 |
| 4267 | -0.12 |
| 5791 | +0.32 |
| 7315 | +0.88 |
| 8839 | +1.79 |
| 9144 | +1.94 |

Across all 125 paired altitudes the difference runs from -0.31 K to +1.94 K, with a median of +0.02 K. The table therefore tracks a standard-atmosphere calculation closely below 5 km, and it is most likely computed rather than measured. The dataset does not show which calculation was used. The comparison is a finding about the benchmark, not about the physics: it shows the benchmark is not independent evidence against a physical model.

## Artifact 3: four model variants against the table

The experiment crosses two choices. The atmosphere is either isothermal, with scale height H = RT/(Mg) = 8434.66 m and pressure P = P_0 exp(-h/H), where P_0 is the sea-level pressure, or ISA, with the troposphere lapse rate of 6.5 K/km [3]. The thermodynamic step is either constant-enthalpy Clausius-Clapeyron equation, with a molar enthalpy of vaporisation of 40.65 kJ/mol anchored at 373.15 K and 101.325 kPa, or the IAPWS curve. The residual for each variant is model minus the Engineering ToolBox value at each table altitude, in kelvin. The experiment computed the residuals at the 119 table altitudes from 0 to 8992 m (40, 39 and 40 in the three bands; the dataset's 125 rows include the -305 m and 9144 m endpoints, which the experiment's bands do not cover), and summarised them in three altitude bands [ARTIFACT:art_SznfD9DKXm93].

The experiment's sanity checks pass. At 9000 m, the isothermal pressure is 34.86 kPa and the ISA pressure is 30.74 kPa. The IAPWS normal boiling point is 373.124 K (99.974 C), while the constant-enthalpy formula gives 100.00 C at sea level because it is anchored there. These checks are in the experiment's sanity file.

Table 1. Residual of each model against the Engineering ToolBox table, in kelvin, by altitude band. Each cell gives bias (mean absolute error, maximum absolute error). Source: summary_by_band.json [ARTIFACT:art_SznfD9DKXm93].

| Model | 0 to 3 km | 3 to 6 km | 6 to 9 km |
|---|---|---|---|
| Isothermal, constant enthalpy | +0.23 (0.23, 0.43) | +0.51 (0.51, 0.59) | +0.50 (0.50, 0.59) |
| Isothermal, IAPWS-IF97 | +0.29 (0.29, 0.59) | +0.79 (0.79, 0.98) | +1.04 (1.04, 1.12) |
| ISA, constant enthalpy | +0.11 (0.11, 0.20) | -0.28 (0.29, 0.77) | -1.64 (1.64, 2.60) |
| ISA, IAPWS-IF97 | +0.18 (0.18, 0.31) | +0.02 (0.15, 0.33) | -1.03 (1.03, 1.81) |

The two residual differences that compare the atmosphere choice with the enthalpy choice never change sign over 0 to 9 km. The difference between the isothermal and ISA residuals with constant enthalpy stays positive. The same difference with the IAPWS curve also stays positive. The run therefore finds no crossover altitude in this comparison, which means no altitude at which the ranking of the two atmosphere choices reverses.

Table 2. Mean residual over the sub-bands 0 to 1 km and 1 to 3 km, computed from residuals.json (K). These sub-bands test the hypothesis's claim that the error is smallest at 1 to 3 km [ARTIFACT:art_SznfD9DKXm93].

| Model | 0 to 1 km | 1 to 3 km |
|---|---|---|
| Isothermal, constant enthalpy | +0.09 | +0.30 |
| Isothermal, IAPWS-IF97 | +0.09 | +0.40 |
| ISA, constant enthalpy | +0.08 | +0.14 |
| ISA, IAPWS-IF97 | +0.08 | +0.24 |

The residual of the isothermal, constant-enthalpy model grows steadily with altitude from almost zero at the surface. Figure 1 shows the four residual curves over the full range.

[FIGURE:fig1]

Table 4. Residuals of the research artifact's stated values (table minus model, as stated in its summary) beside the experiment's ISA model residual with constant enthalpy at the nearest table altitude (model minus table). The research values are as the research artifact reports them; the experiment values are read from residuals.json [ARTIFACT:art_meMsxdA1r_bm] [ARTIFACT:art_SznfD9DKXm93].

| Altitude | Research artifact (table minus model, K) | Experiment ISA, constant enthalpy (model minus table, K) |
|---|---|---|
| 4.3 km | +0.2 | -0.16 (4267 m) |
| 4.6 km | +0.3 | -0.27 (4648 m) |
| 6.1 km | +0.8 | -0.80 (6096 m) |
| 7.6 km | +1.7 | -1.65 (7620 m) |
| 8.8 to 9.1 km | +2.6 to +2.8 | -2.6 (8992 m) |

The two sets agree in magnitude and sign once the convention is reversed. The research artifact's finding that the table runs higher is therefore reproduced by the experiment. The research artifact's stated values are not in an output file I could read, so the agreement rests on the summary text.

Table 5. Sensitivity of the isothermal model with constant enthalpy and of the ISA model with the IAPWS curve to the sea-level pressure (kPa) and to the enthalpy of vaporisation (dH, J/mol). Bias by band, in kelvin. Source: sensitivity.json [ARTIFACT:art_SznfD9DKXm93].

| Enthalpy | Sea-level pressure | Isothermal, constant enthalpy: 0 to 3, 3 to 6, 6 to 9 km | ISA, IAPWS-IF97: 0 to 3, 3 to 6, 6 to 9 km |
|---|---|---|---|
| 40150 | 100.325 | -0.11, +0.07, -0.03 | -0.09, -0.23, -1.27 |
| 40150 | 101.325 | +0.17, +0.33, +0.22 | +0.18, +0.02, -1.03 |
| 40150 | 102.325 | +0.44, +0.59, +0.47 | +0.45, +0.27, -0.80 |
| 40650 | 100.325 | -0.05, +0.24, +0.25 | -0.09, -0.23, -1.27 |
| 40650 | 101.325 | +0.23, +0.51, +0.50 | +0.18, +0.02, -1.03 |
| 40650 | 102.325 | +0.50, +0.76, +0.74 | +0.45, +0.27, -0.80 |
| 41150 | 100.325 | +0.01, +0.42, +0.52 | -0.09, -0.23, -1.27 |
| 41150 | 101.325 | +0.29, +0.68, +0.77 | +0.18, +0.02, -1.03 |
| 41150 | 102.325 | +0.56, +0.93, +1.01 | +0.45, +0.27, -0.80 |

The ISA column with the IAPWS curve does not depend on the enthalpy value, because that variant does not use the constant enthalpy; its three rows repeat across the enthalpy values. Two points follow. A change of 1 kPa in sea-level pressure moves every band by roughly 0.25 K, which is as large as the residuals in Table 1. A change of 500 J/mol in enthalpy moves the 6 to 9 km bias of the isothermal, constant-enthalpy model by about 0.27 K. The table's residual pattern therefore depends on the constants at the level of the residual itself, and a "within 0.6 K" statement holds only for the stated pressure and enthalpy.

## What the measured comparison could test

The experiment's measured comparison is empty. The file records zero measured pairs, and the note states that no independently measured pairs could be verified [ARTIFACT:art_SznfD9DKXm93]. The research artifact found no measured station-pressure dataset reaching above 8 km [ARTIFACT:art_meMsxdA1r_bm]. This means the question in the run's title is not answered by any output of this iteration. The run can say how the four models compare with each other, and how they compare with a computed table. It cannot say how they compare with what water actually boils at.

The only measured-looking numbers in the record are summit estimates from calculators and an unverified textbook table of Denver, Bogota and Everest values quoted from search snippets. None was fetched in full, and none was used as a benchmark.

## Reading this iteration against the hypothesis

Each clause of the hypothesis is taken in turn, against the tables above.

The isothermal, constant-enthalpy model stays within 0.6 K of the Engineering ToolBox table from sea level to 9 km. The maximum absolute residual across all bands is 0.59 K (Table 1). This clause holds against the table. It does not test accuracy against measurement, and the table is most likely computed.

The error is not smallest in the 1 to 3 km band. The isothermal, constant-enthalpy residual has a mean of +0.09 K in the 0 to 1 km band and +0.30 K in the 1 to 3 km band (Table 2). The clause does not hold on these data. The error grows monotonically with altitude, and the smallest error is at the surface.

The ISA model is more accurate than the isothermal model below 3 km against the table. Its 0 to 3 km bias is +0.11 K against +0.23 K, and its 1 to 3 km mean is +0.14 K against +0.30 K. Above 5 km it is less accurate, with a 6 to 9 km bias of -1.64 K. The clause holds against the table. The hypothesis's figure of -2.6 K near 8.8 km is matched: the experiment gives -2.53 K at 8916 m and -2.60 K at 8992 m (Table 4 and Figure 1).

The thermodynamic step is the main error source. This clause is not supported. Switching the isothermal model from constant enthalpy to the IAPWS curve increases the 6 to 9 km residual from +0.50 K to +1.04 K, so the table moves away from the model built on the IAPWS curve. For the ISA model, the change reduces the 6 to 9 km mean absolute error from 1.64 K to 1.03 K. That is a reduction of about 37 percent, not more than half. The hypothesis's success criterion (c) therefore fails for the isothermal model and falls short for the ISA model.

Above 5 km the table lies closest to the isothermal, constant-enthalpy model, whose residual is +0.50 K (Table 1). The two ISA models fall below the table, by -1.03 K with the IAPWS curve and -1.64 K with constant enthalpy. So switching to the IAPWS curve moves the ISA model toward the table, and it moves the isothermal model away from it. The table's rows above 5 km are therefore not explained by one thermodynamic choice alone. This is a statement about the benchmark's pattern, not about the physics. The hypothesis's attribution of the error to the constant-enthalpy step is a claim about the physics, and this iteration cannot test it without measurements.

The disconfirmation condition is not met. The ISA version is not more accurate than the isothermal one at all altitudes against the table; it is less accurate above 5 km. The experiment's success conditions (a) and (b) hold against the table. Condition (c) fails. Because no measured benchmark exists in this iteration, none of the three conditions can be read as an accuracy claim.

## Dead ends and blocked steps

The search for Keene (1995) failed after two rounds. It is still the intended measured benchmark, and it has not been verified as existing in the form the hypothesis describes.

The Osborne, Stimson and Ginnings (1939) and CRC Handbook tables were located as records, but their values were not transcribed reliably from the fetched text. No measured row was added, because the run's rule forbids padding the measured set with values that cannot be checked.

The IAPWS-95 saturation table (NIST NISTIR 5078) could not be parsed. The IAPWS inversion was therefore computed with the iapws Python package and was not checked against the published table.

The residuals of the research artifact and those of the experiment use different enthalpy anchors (373.124 K and 373.15 K). The effect of the anchor on the residuals was not separated from the effect of the sign convention in this iteration.

## Open questions after iteration 1

Which measured boiling-point and station-pressure pairs exist at 8 km and above, from two or more independent sites? Without them the question in the title has no answer.

Can the NIST IAPWS-95 saturation table be read directly, so the IAPWS inversion in the research artifact can be checked against the experiment's IAPWS values?

Was the Engineering ToolBox table built from a calculation, and if so with which pressure profile? The dataset comparison points to a standard-atmosphere calculation, but it does not show which thermodynamic model was used.

# What we have learned so far

The Engineering ToolBox table is not a measurement, on the evidence of this iteration. It lies within 0.31 K of a standard-atmosphere IAPWS curve at all 70 paired altitudes below 5 km, and departs from it by up to 1.9 K at 9 km [ARTIFACT:art_39-uxNptYM5-]. Above 5 km its values lie closest to the isothermal, constant-enthalpy model [ARTIFACT:art_SznfD9DKXm93].

Against that table, the isothermal, constant-enthalpy model stays within 0.6 K from sea level to 9 km, and the ISA, constant-enthalpy model is more accurate below 3 km and less accurate above 5 km [ARTIFACT:art_SznfD9DKXm93]. The residuals depend on the sea-level pressure and the enthalpy at the level of the residuals themselves, with about 0.25 K per kilopascal and about 0.27 K per 500 J/mol at 9 km.

No measured boiling-point and station-pressure pair was found or used, so the run has no accuracy claim against measurement. The question of how well the barometric formula predicts measured boiling points is open.

# References

[1] Engineering ToolBox. Water - Boiling Points vs. Altitude. 2009. https://www.engineeringtoolbox.com/boiling-points-water-altitude-d_1344.html (accessed 2026-11-19).

[2] Wagner, W. and Pruss, A. The IAPWS Formulation 1995 for the Thermodynamic Properties of Ordinary Water Substance for General and Scientific Use. Journal of Physical and Chemical Reference Data, 31(2), 387-535, 2002. doi:10.1063/1.1461829.

[3] International Standard Atmosphere. Wikipedia. https://en.wikipedia.org/wiki/International_Standard_Atmosphere (accessed 2026-11-19).
