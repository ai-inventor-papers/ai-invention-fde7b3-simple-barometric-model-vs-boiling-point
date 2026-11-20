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

# Iteration 2

## Why this iteration ran what it ran

The reviewer's first major finding was that the record holds no measured pair, so the question in the title has no answer. Its second and third findings were that the clause verdicts of Iteration 1 were scored as passes against a table that is most likely a computed reference, and that Table 4 presented a match between two implementations of the same ISA formula as if it were corroboration. We call the isothermal or ISA atmosphere with a constant enthalpy of vaporisation the constant-enthalpy model, as Iteration 1 does. The remaining findings concerned verification records, low-altitude coverage, the untested anchor claim, sample sizes, and the firmness of the closing summary.

The strategy named two jobs: retry the measured comparison, and attribute the residual against computed references so that the atmosphere term and the thermodynamic term are separated. Three experiment artifacts ran. [ARTIFACT:art_e7cQzFbFiEBS] put four variants against both computed references and attempted the measured comparison. [ARTIFACT:art_qQYKsNWhqlKr] attempted the measured comparison again through a separate code path. [ARTIFACT:art_Dwo3Mclnlbtv] split the residual into an atmosphere effect and a thermodynamic effect. No new research or dataset artifact ran, so the reference table is still the 250-row table of Iteration 1 [ARTIFACT:art_39-uxNptYM5-].

The altitudes used in this iteration are the 125 altitudes of that table, from -305 m to 9144 m, not the 119-point grid of Iteration 1 (0 to 8992 m, step about 76 m, plus 9144 m). The plan asked for the grid; the experiments used the dataset altitudes directly, as the plan permits when the grid differs [ARTIFACT:art_Dwo3Mclnlbtv]. Band sizes are therefore 40, 39 and 42 (0-3 km, 3-6 km, and 6 km and above, the last including 9144 m). Iteration 1's band figures used different altitudes and are not directly comparable with the figures below.

## Measured comparison: still empty

Both measured-comparison artifacts returned zero rows. [ARTIFACT:art_e7cQzFbFiEBS] reports that the NIST RP1229 PDF gave no readable table text, that the CRC Handbook table was not obtained, and that Keene (1995) was not located. Its measured_pairs.csv holds a header and no data rows, and its sources_summary.json records n_measured = 0. [ARTIFACT:art_qQYKsNWhqlKr] ran two query rounds. These found the NIST RP1229 paper but no transcribable boiling-point rows paired with station pressure, none above 5 km, and no retrievable Keene (1995) text. Its measured_records.json has n = 0, and its band summary reports no band statistic (n = 0) in every band from 0 to 9 km.

This is the second iteration in which the measured search has returned nothing. The measured clauses of the hypothesis, success criteria (a) and (b), cannot be evaluated. Criterion (c) can only be evaluated against the computed references, which are not measurements. The question in the title is therefore still unanswered.

## Four variants against the Engineering ToolBox table

[ARTIFACT:art_e7cQzFbFiEBS] reports bias, mean absolute error and maximum absolute error for each variant in each band. Each cell gives the bias, with the mean absolute error and the maximum absolute error in parentheses, all in kelvin, model minus table. The isothermal constant-enthalpy variant is the isothermal barometric formula with constant-enthalpy anchored at 373.124 K. The isothermal IAPWS-curve variant is the same isothermal formula inverted on the IAPWS curve. The ISA constant-enthalpy variant is the ISA lapse-rate formula with constant-enthalpy. The ISA IAPWS-curve variant is the ISA formula inverted on the IAPWS curve.

Table 7. Residual of each variant against the Engineering ToolBox table. Source: band_stats.csv, rows with data_type computed_unknown_method [ARTIFACT:art_e7cQzFbFiEBS].

| Variant | 0-3 km (n = 40) | 3-6 km (n = 39) | 6 km and above (n = 42) |
|---|---|---|---|
| V1 isothermal, constant-enthalpy | +0.202 (0.205, 0.403) | +0.481 (0.481, 0.565) | +0.470 (0.470, 0.570) |
| V2 isothermal, IAPWS-IF97 | +0.292 (0.295, 0.592) | +0.788 (0.788, 0.984) | +1.045 (1.045, 1.120) |
| V3 ISA, constant-enthalpy | +0.089 (0.092, 0.173) | -0.307 (0.311, 0.796) | -1.716 (1.716, 2.767) |
| V4 ISA, IAPWS-IF97 | +0.182 (0.185, 0.306) | +0.021 (0.152, 0.332) | -1.070 (1.070, 1.935) |

[FIGURE:fig2]

Figure 2 plots the bias in Table 7. Within the 6 km and above band, the isothermal constant-enthalpy variant has the smallest bias, and no variant has a bias below 0.4 K there. The two ISA variants are negative because the ISA atmosphere lies below the isothermal atmosphere at these altitudes.

Table 8. Residual of each variant against the IAPWS curve at ISA pressures, the computed reference of the dataset, which we call IAPWS-at-ISA below. Source: band_stats.csv, rows with data_type computed_reference [ARTIFACT:art_e7cQzFbFiEBS].

| Variant | 0-3 km (n = 40) | 3-6 km (n = 39) | 6 km and above (n = 42) |
|---|---|---|---|
| V1 isothermal, constant-enthalpy | +0.020 (0.036, 0.137) | +0.461 (0.461, 0.864) | +1.542 (1.542, 2.298) |
| V2 isothermal, IAPWS-IF97 | +0.111 (0.111, 0.326) | +0.768 (0.768, 1.290) | +2.116 (2.116, 3.021) |
| V3 ISA, constant-enthalpy | -0.093 (0.093, 0.196) | -0.327 (0.327, 0.463) | -0.645 (0.645, 0.831) |
| V4 ISA, IAPWS-IF97 | +0.0001 (0.0003, 0.0007) | +0.0004 (0.0005, 0.0011) | +0.0007 (0.0007, 0.0013) |

The ISA IAPWS-curve variant reproduces the IAPWS-at-ISA reference to within 0.0013 K, which confirms that the implementation of the IAPWS step is correct. It does not show that the IAPWS step is the right physics for the table. The same reference is what makes the ISA variants look closer, so Table 8 is a consistency check and not a comparison of independent methods.

### Does the table agree with the standard-atmosphere calculation?

Iteration 1 stated that the table lies within 0.31 K of the IAPWS-at-ISA calculation at all altitudes below 5 km. I recomputed this from the per-row residuals of the experiment [ARTIFACT:art_e7cQzFbFiEBS]. Of the 70 table rows below 5 km, the table minus IAPWS-at-ISA lies between -0.31 K and +0.11 K, with a median of -0.17 K. The Iteration 1 median of +0.02 K was taken over all 125 rows, and that statistic was not recomputed in this pass. The claim of agreement within 0.31 K below 5 km holds.

Above 5 km the agreement fails. The 55 rows at 5 km and above differ from IAPWS-at-ISA by up to 1.94 K, with the table higher. No variant matches the table in this band. The isothermal constant-enthalpy variant is closest, with a bias of +0.47 K, and the ISA IAPWS-curve variant is -1.07 K. The provenance statement must therefore be limited: the table is consistent with a standard-atmosphere calculation below 5 km, and the method used above 5 km is not identified by any of the four variants.

The point values at the top of the range make the same point. At 9144 m the experiment's ISA constant-enthalpy residual is -2.77 K, and at 8992 m it is -2.63 K with the 373.124 K anchor [ARTIFACT:art_e7cQzFbFiEBS]. The 8992 m value of -2.60 K in Iteration 1 used the 373.15 K anchor, and the difference of about 0.02 K is the anchor shift measured below.

## Attribution: atmosphere term against thermodynamic term

[ARTIFACT:art_Dwo3Mclnlbtv] crosses the two atmospheres with four thermodynamic treatments. These are a constant-enthalpy treatment anchored at 373.124 K (A), a constant-enthalpy treatment anchored at 373.15 K (the old anchor), an effective-enthalpy treatment fitted to the IAPWS saturation curve over 343.15 to 373.15 K (B, dH_eff = 41829.7 J/mol, fit RMS error in ln P of 1.15e-3), and direct IAPWS inversion (C). Table 9 gives the bias against the ToolBox table in each band, with n as above and the whole 0 to 9144 m range (n = 121) in the last column.

Table 9. Bias of each atmosphere and thermodynamic treatment against the ToolBox table, in kelvin, model minus table. Source: results/sensitivity.md [ARTIFACT:art_Dwo3Mclnlbtv].

| Atmosphere | Treatment | 0-3 km | 3-6 km | 6-9 km (incl. 9144 m) | 0-9144 m |
|---|---|---|---|---|---|
| isothermal | A, 373.124 K | +0.202 | +0.481 | +0.470 | +0.385 |
| isothermal | A, 373.15 K | +0.227 | +0.505 | +0.493 | +0.409 |
| isothermal | B, effective enthalpy | +0.338 | +0.876 | +1.102 | +0.777 |
| isothermal | C, IAPWS inversion | +0.292 | +0.788 | +1.044 | +0.713 |
| ISA | A, 373.124 K | +0.089 | -0.307 | -1.716 | -0.665 |
| ISA | A, 373.15 K | +0.114 | -0.283 | -1.694 | -0.642 |
| ISA | B, effective enthalpy | +0.229 | +0.108 | -1.031 | -0.248 |
| ISA | C, IAPWS inversion | +0.182 | +0.021 | -1.071 | -0.305 |

The 6-9 km band, which covers the high-altitude clause, separates into two effects, as Table 10 shows.

Table 10. Decomposition of the 6-9 km bias against the ToolBox table, in kelvin. The atmosphere effect is ISA minus isothermal for the same treatment. The thermodynamic effect is the treatment minus treatment A for the same atmosphere. Computed from Table 9 [ARTIFACT:art_Dwo3Mclnlbtv].

| Treatment | Atmosphere effect (ISA minus isothermal) | Thermodynamic effect, isothermal | Thermodynamic effect, ISA |
|---|---|---|---|
| A, 373.124 K | -2.186 | 0 (reference) | 0 (reference) |
| B, effective enthalpy | -2.133 | +0.632 | +0.685 |
| C, IAPWS inversion | -2.115 | +0.574 | +0.645 |

Against the ToolBox table, the atmosphere effect is about -2.1 to -2.2 K and the thermodynamic effect is about +0.6 to +0.7 K. The atmosphere term is therefore roughly three times the size of the thermodynamic term at 6-9 km. Iteration 1 had stated that the thermodynamic step carries most of the high-altitude error. This reference does not support that. The result is about the table, and this iteration cannot test what the physics is.

Switching the ISA model from the constant-enthalpy treatment to the effective-enthalpy or IAPWS-inversion treatment reduces its 6-9 km bias from -1.72 K to -1.03 K or -1.07 K, a reduction of 40% or 38%. The same change moves the isothermal model further from the table, from +0.47 K to +1.10 K or +1.04 K. Success criterion (c) asked for a reduction of more than half. Against the ToolBox table, criterion (c) is not met. Against the IAPWS-at-ISA reference the reduction is 94 to 100%, but that reference uses the same curve as the corrected variants, so the figure is a reproduction and not evidence.

The anchor shift is 0.025 K at 0-3 km, and it moves the isothermal and ISA biases by up to 11% and 22% of their values in that band. Table 9 shows that the change in anchor does not alter the sign or the ranking of any of the four variants. Iteration 1's remark that the anchor does not change the pattern was not checked at the time; it is checked here, for the ranking, and it holds.

Sensitivity to the enthalpy of vaporisation is reported by [ARTIFACT:art_qQYKsNWhqlKr] and [ARTIFACT:art_e7cQzFbFiEBS]. Over the full 125-row table, moving the enthalpy by plus or minus 500 J/mol moves the bias of the isothermal constant-enthalpy variant by +0.16 K and -0.17 K, with the maximum absolute change near 0.33 K. These are full-range statistics. The 6-9 km change of 0.27 K in Iteration 1 is a band statistic from a different altitude set and is not recomputed here.

Table 11 gives the IAPWS-at-ISA reference residuals for the same treatments, for comparison. It reproduces the computed reference, not the table.

Table 11. Bias of each treatment against the IAPWS-at-ISA reference, in kelvin, model minus reference [ARTIFACT:art_Dwo3Mclnlbtv].

| Atmosphere | Treatment | 0-3 km | 3-6 km | 6-9 km |
|---|---|---|---|---|
| isothermal | A, 373.124 K | +0.020 | +0.461 | +1.541 |
| isothermal | B, effective enthalpy | +0.157 | +0.855 | +2.173 |
| isothermal | C, IAPWS inversion | +0.111 | +0.768 | +2.116 |
| ISA | A, 373.124 K | -0.093 | -0.328 | -0.645 |
| ISA | B, effective enthalpy | +0.047 | +0.087 | +0.040 |
| ISA | C, IAPWS inversion | 0 (by construction) | 0 | 0 |

Two cautions apply to Table 11. The IAPWS-inversion treatment (C) is zero by construction, because it uses the same calculation as the reference. The effective-enthalpy treatment (B) is fitted to the same curve, so its small residual is not independent. The artifact states both limitations.

## Verification

Each check below is listed with what it confirms and what it does not.

- Sea-level and unit checks, [ARTIFACT:art_e7cQzFbFiEBS]. The run log records a sea-level confirmation that passes for all four variants at 373.124 K, the IAPWS check at 101.325 kPa giving 373.1243 K, and zero measured rows. It confirms the implementation at sea level. It does not confirm any value above sea level against a measurement.
- Inversion and unit checks, [ARTIFACT:art_qQYKsNWhqlKr]. The sanity file records an ISA altitude inversion check with a maximum error of 3.6e-12 m, a Clausius-Clapeyron equation inversion check with zero error, and an ISA pressure of 22632.6 Pa at 11 km, all passing. The artifact reports that an independent re-derivation through a separate code path reproduced its headline numbers. I did not re-run that re-derivation in this pass. It confirms code consistency only.
- Independent re-derivation, [ARTIFACT:art_Dwo3Mclnlbtv]. I read audit/rederive_out.txt. Its maximum difference between recomputed and stored pressures is 1.0e-10 Pa, and its maximum difference between rearranged and stored boiling temperatures is 1.1e-13 K. It reproduces the 6-9 km ToolBox biases in Table 9 and the fractions of the bias removed by the enthalpy correction. Its implementation checks pass: the sea-level inversion agrees within 3.0e-4 K, the ISA reproduction of the IAPWS reference agrees within 5.3e-4 K using stored pressures and 9.4e-4 K using the formula, and the loop and NumPy band statistics agree within 1e-9 K. It confirms that the code computes what it says. It does not confirm the constants.
- Constants, [ARTIFACT:art_Dwo3Mclnlbtv]. The sea-level pressure, sea-level temperature and lapse rate are attributed to the ISO 2533 values as summarised on the Wikipedia ISA page, which was fetched. The gravitational acceleration, gas constant and enthalpy of vaporisation were not fetched from a document. The molar mass is the ISO 2533 value, 28.9644 g/mol, which the fetched page rounds to 28.966. The constants are therefore partly sourced. The earlier research artifact's constants were written from memory, as the reviewer records from its research_out.json; that file was not re-read in this pass, so that disclosure rests on the reviewer's reading. The ISA agreement in Table 4 is an implementation consistency check, not a corroboration.
- research_verification.json, which the reviewer cites from Iteration 1, is not among this iteration's files. The reviewer records that its passages list is empty, so no quoted claim was checked. This is not re-verified here.

These checks do not confirm the method used to produce the ToolBox table, which is unstated. They do not confirm accuracy against any measurement, because none exists in the record.

## Responses to the review

- Measured comparison (major). Not achieved. The record still holds no measured pair, and the title question remains open. The next iteration's primary task is set below.
- Clause verdicts (major). The verdicts are restated as consistency with the computed reference. The word "holds" is no longer applied to accuracy. See the reading of the hypothesis below.
- Table 4, constants written from memory (major). The disclosure is recorded above. The 9.1 km row is now matched at a point the experiment computed. The research artifact's residuals still exist only in its summary text, so the research side of the table is not recomputed. A file of those residuals was not written, because no research artifact ran in this iteration.
- Table 4 at 9.1 km (major). The experiment's ISA constant-enthalpy residual at 9144 m is -2.77 K with the 373.124 K anchor, and the research artifact's summary gives +2.8 K as table minus model. These match to within 0.03 K. The 8992 m row matches at -2.63 K, or -2.60 K at the old anchor. Both are now computed points.
- Novelty (major). The nearest published neighbours are Osborne, Stimson and Ginnings (1939) for measured vapour pressure, which was not transcribed in this run, and the IAPWS-95 formulation [2], which the run uses only through the iapws library and has not checked against the published saturation table. What this iteration adds to them is a provenance check of one table, namely whether it is computed or measured, and a decomposition of its residual. It adds no new physical result.
- Anchor claim (minor). Run here. See the anchor paragraph above.
- Summary firmness (minor). The closing section now says "most likely a computed reference" below 5 km, matching the body. This is a wording correction to the closing section, which is rewritten each iteration.
- Verification record (minor). Added above as a subsection, with the research_verification.json caveat.
- Low-altitude research values (minor). Table 4 was not extended to 0 m. The research artifact's low-altitude residuals (about +0.03 K at 0 m and about -0.1 K at 1.5 to 2.1 km, as the reviewer records) appear only in its text, and no file holds them. The corresponding experiment values on the 125-row set are: the ISA constant-enthalpy variant gives +0.089 K at 0-3 km (band bias, model minus table), against +0.11 K on the 119-row set of Iteration 1. The difference is the altitude set, not the model.
- Sample sizes and altitude grid (minor). Stated above: 40, 39 and 42 per band, from the 125 dataset altitudes.

## Reading this iteration against the hypothesis

Each clause is read against the tables above, with the reference named each time.

Measured clauses. Success criteria (a) and (b), and the claim that residuals grow with altitude against measurement, are untested. No measured residual exists.

Computed-reference clauses. Against the ToolBox table, the isothermal constant-enthalpy model is within 0.6 K from 0 to 9144 m (largest value 0.570 K) and is consistent with the computed reference. The ISA variant with constant-enthalpy is more accurate than the isothermal one below 3 km against that table (bias +0.089 K against +0.202 K), and less accurate above 5 km (bias -1.72 K against +0.47 K). This pattern is consistent with the hypothesis's expectation, on the computed reference only. Against the IAPWS-at-ISA reference, the isothermal model is less accurate than the ISA model at every band, and the difference is the atmosphere term itself, so that comparison is not a test of the lapse rate.

Criterion (c), the reduction of the high-altitude error by more than half from the thermodynamic correction, is not met against the ToolBox table: the reduction is 38 to 40%. The hypothesis's expectation that the thermodynamic step carries most of the error is not supported by the ToolBox table, where the atmosphere term is about three times the thermodynamic term at 6-9 km.

The disconfirmation condition, that the ISA version is more accurate than the isothermal one at all altitudes against measured values, cannot be evaluated. Against the computed references, the ISA model is more accurate than the isothermal model below 3 km and less accurate above 5 km, so that condition is not met on the computed data either.

## Dead ends and blocked steps

- The measured comparison, against Osborne, Stimson and Ginnings (1939), the CRC Handbook, Keene (1995), the NIST RP1229 paper and high-altitude station or summit records, returned zero transcribable rows in both measured-comparison artifacts. Evidence: measured_pairs.csv has no data rows, and measured_records.json has n = 0. This route is blocked by the sources' accessibility, not by the physics, and it is recorded as a dead end for this run's search tools.
- The research artifact's residuals cannot be extended to a file. No artifact recomputed them.
- The thermodynamic method behind the ToolBox table above 5 km is not identified. The isothermal IAPWS-inversion treatment and the isothermal IAPWS-curve variant are the same calculation, and neither matches the table there (+1.04 K at 6 km and above). The ISA IAPWS-curve and ISA constant-enthalpy variants do not match it either (-1.07 K and -1.72 K). No dead end was reached by a test of the method itself; the question is open.

## Open questions after iteration 2

Can at least two measured boiling-point and station-pressure sets be obtained, with each row's source page recorded, and one of them above 8 km? Without them, neither the title question nor criterion (a) can be answered. Three routes remain untried in full: the Osborne, Stimson and Ginnings (1939) table, a CRC Handbook table, and a station or summit record above 8 km. The NIST RP1229 paper was located, but its table text was not readable.

What method produced the ToolBox table above 5 km? It agrees with a standard-atmosphere IAPWS calculation below 5 km and with none of the four variants above it.

Can the research artifact's residuals be written to a file, so that Table 4's research column can be recomputed rather than read from text?

# What we have learned so far

The measured comparison has still not been carried out. Two iterations of search have returned no transcribable measured boiling-point and station-pressure row, so the question in the title has no answer yet. Everything below is a comparison with computed references.

The Engineering ToolBox table is most likely a computed standard-atmosphere calculation below 5 km. Recomputed from per-row residuals, it lies between -0.31 K and +0.11 K from IAPWS-at-ISA at all 70 altitudes below 5 km [ARTIFACT:art_e7cQzFbFiEBS]. Above 5 km it runs up to 1.9 K higher than that reference, and none of the four variants matches it there. Its method above 5 km is not identified.

Against the table, the isothermal model with constant-enthalpy is within 0.6 K from 0 to 9144 m. The ISA model with constant-enthalpy is more accurate below 3 km and less accurate above 5 km, reaching -1.72 K in the 6 km and above band [ARTIFACT:art_Dwo3Mclnlbtv]. The atmosphere term accounts for about -2.2 K of the 6-9 km bias, and the thermodynamic term for about +0.6 K. The thermodynamic correction removes about 40% of the ISA bias, which does not meet the more-than-half target. The atmosphere term, not the thermodynamic step, is the larger error against this table.

The enthalpy of vaporisation and the sea-level anchor are both checked. Moving the anchor from 373.124 K to 373.15 K shifts the biases by about 0.025 K and leaves the ranking unchanged. A change of 500 J/mol in the enthalpy moves the full-range bias of the isothermal model by about 0.16 K [ARTIFACT:art_qQYKsNWhqlKr].

The code is checked against independent re-derivation to about 1e-10 Pa and 1e-13 K [ARTIFACT:art_Dwo3Mclnlbtv]. The ISA constants are sourced only in part, and the research artifact's constants were recorded as written from memory. These checks confirm code consistency, not the physics or the table's method.

The hypothesis is supported only in its computed-reference clauses, and only in the directions described in Iteration 2. Its measured clauses and its attribution clause are untested or not met. The next iteration's primary task is still the measured comparison.

# References

[1] Engineering ToolBox. Water - Boiling Points vs. Altitude. 2009. https://www.engineeringtoolbox.com/boiling-points-water-altitude-d_1344.html (accessed 2026-11-19).

[2] Wagner, W. and Pruss, A. The IAPWS Formulation 1995 for the Thermodynamic Properties of Ordinary Water Substance for General and Scientific Use. Journal of Physical and Chemical Reference Data, 31(2), 387-535, 2002. doi:10.1063/1.1461829.

[3] International Standard Atmosphere. Wikipedia. https://en.wikipedia.org/wiki/International_Standard_Atmosphere (accessed 2026-11-19).
