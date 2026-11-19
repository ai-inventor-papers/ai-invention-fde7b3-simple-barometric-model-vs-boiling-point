# Reproducibility: how this research was actually conducted

Date of work: 2026-11-19 (single session). Question: how well does the simple barometric formula predict the boiling point of water at different altitudes, compared with published measurements?

## Tools used

- The aii-web-tools skill was loaded. Its scripts could not be run: the skill directory returned "Permission denied" and the expected venv `.ability_client_venv/bin/python` was missing. Per the skill's own guidance, I then used the built-in `WebSearch` and `WebFetch` tools, which the skill lists as the preferred path (loaded via ToolSearch).
- Local computation: `python3 -I` (isolated mode) running `analysis/cc_check.py`. No network access in that step.

## Searches and fetches, in order

1. WebFetch `https://www.engineeringtoolbox.com/boiling-points-water-altitude-d_1344.html`. Prompt asked for any method, formula, steam table, IAPWS, Clausius, measured-data or source statement, and for every table row. Note: WebFetch returns a summary produced by a small model, not raw HTML. The table values are therefore relayed and must be checked against the page directly before publication.
2. WebSearch "Keene 1995 Journal of Chemical Education boiling point water altitude barometric".
3. WebSearch "boiling point of water measured at altitude station pressure data table".
4. WebFetch `https://nvlpubs.nist.gov/nistpubs/Legacy/IR/nistir5078.pdf` (NISTIR 5078, IAPWS-95 saturation table). Failed: the tool returned compressed PDF streams and JBIG2/JPEG2000 images with no readable text. The IAPWS saturation table was NOT read.
5. WebFetch `https://pubs.acs.org/doi/abs/10.1021/ed067p45`. Failed: HTTP 403.
6. WebSearch "Keene J. Chem. Educ. 1995 ... doi 10.1021/ed072" (variant of query 2).
7. WebSearch "Wagner Pruss 2002 IAPWS formulation 1995 ... saturation pressure".
8. WebSearch "Mount Everest summit water boiling temperature measured 70 C atmospheric pressure study".
9. WebSearch "Pike's Peak water boiling point measured barometric pressure Clausius-Clapeyron comparison".
10. WebFetch `https://webbook.nist.gov/cgi/fluid.cgi?...` (NIST WebBook water saturation table, by pressure). Failed: HTTP 400.
11. WebFetch `https://en.wikipedia.org/wiki/Vapour_pressure_of_water`. Succeeded (summary).
12. WebSearch "boiling point water altitude measured data Denver Quito La Paz observed boiling temperature vs barometric pressure paper".
13. WebSearch "Dalton 1830 boiling point altitude measurements Mont Blanc Himalaya thermometer hypsometer data".
14. WebSearch "hypsometer boiling point altitude pressure measurement weather station comparison International Standard Atmosphere error study".
15. WebSearch "'boiling point' water 'station pressure' altitude measurements table kPa °C physics teacher article".
16. WebSearch "Keene J. Chem. Educ. 1995 72 'boiling point' altitude pressure paper".
17. WebSearch "Mount Everest boiling point water measured 1953 expedition or 2019 summit pressure measurement paper".
18. Local computation: `python3 -I analysis/cc_check.py` (ISA pressure from altitude, then constant-enthalpy Clausius-Clapeyron with dH = 40.65 kJ/mol anchored at 373.124 K and 101.325 kPa, compared with the ToolBox rows used in the script).

Pages fetched successfully (not just snippets): [1] ToolBox (summary), [3] Wikipedia Vapour pressure of water (summary).
Search-result snippets only (page not opened): [2] ACS listing (403), [4] arXiv 1803.01452, [5] watercalculator.us, [6] LibreTexts Vapor Pressure, [7] watervaporpressure.com IAPWS-95 page.

## Environment variables and keys

None were required by the built-in WebSearch/WebFetch tools. The skill's scripts would have needed the ability server (not reached), so no keys were set or used. No secret values are recorded here.

## Sources that were NOT located

- Keene (1995), Journal of Chemical Education: not found in two rounds of search (queries 2, 6, 16). The only altitude-boiling article returned was "The direct relation between altitude and boiling point", ACS DOI 10.1021/ed067p45 (volume 67, so not the 1995 Keene paper). Its page returned HTTP 403, so its content is unverified. Recorded as "not located".
- Measured boiling-point/station-pressure data above 5 km: no independent measured dataset was found. Every summit value found (about 68 to 72 °C) is a calculator or estimate, not a measurement.
- Dalton (1830) and expedition-era hypsometer data: no usable hits.

## How to retrace

1. Fetch the ToolBox page and check the table rows against `analysis/` and `README.md` (rows used are listed in `analysis/cc_check.py`).
2. Run `python3 -I analysis/cc_check.py` to reproduce the residuals. Inputs are the ISA pressure relation, the constant-enthalpy Clausius-Clapeyron formula, and the anchors stated above. The ISA constants (2.25577e-5 and exponent 5.25588) are the standard troposphere formula, written from memory; they are not cited from a fetched source.
3. Open NISTIR 5078 directly in a PDF reader (the fetch tool could not parse it) and compare the saturation temperatures at the ISA pressures given in the analysis.

## Confidence and what would change it

- ToolBox provenance: low-to-moderate confidence that no method is stated (the page text was relayed by a summarizer). If a direct read of the page shows a method statement, the answer changes.
- Residual pattern: the computed residuals are arithmetic on relayed values, so they are only as good as the table transcription.
- Measured-source coverage: none found, so the "measured vs predicted" question is not answered. A verified measured dataset with station pressure would change this.
