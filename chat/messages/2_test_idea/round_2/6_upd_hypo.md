# upd_hypo — test_idea

> Phase: `invention_loop` · round 2 · `upd_hypo`
> Run: `run_ek8xZiRG71Qn` — Isothermal Barometric Boiling Points Match a Computed Table to 0.6 K
>
> Full, verbatim transcript of this agent task — every system/user prompt, assistant response, thinking block, tool call and tool result — in the order they occurred. Nothing truncated.

## Task: `upd_hypo` (terminal_claude_agent, claude-haiku-5-5)

### [1] CONFIG · 2026-11-19 23:19:30 UTC

```
model: Claude Haiku 5.5 | effort: high | permission: bypassPermissions
```

### [2] SYSTEM-USER prompt · 2026-11-19 23:19:36 UTC

```
<ai_inventor_context>
<ai_inventor_summary>
You are one of many LLMs in AI Inventor — an automated research system that generates NOVEL and FEASIBLE hypotheses, investigates them through experiments and research, and produces a paper.

Your output feeds other LLMs downstream. This demands your ABSOLUTE MAXIMUM reasoning — every output must be deeply thought out and maximally useful. Surface-level responses waste downstream computation.
</ai_inventor_summary>

<your_role>
YOU ARE: A hypothesis re... [truncated, 97985 chars total]
```

### [3] TOOL CALL — Write · 2026-11-19 23:20:32 UTC

```
File: /Volumes/aii-s20030/work/run_ek8xZiRG71Qn/3_invention_loop/iter_2/upd_hypo/upd_hypo/.terminal_claude_agent_struct_out.json

{
  "title": "Barometric boiling model vs measured data",
  "hypothesis": "Untested until measured pairs exist. The isothermal barometric model with a constant-enthalpy Clausius-Clapeyron step predicts independently measured boiling temperatures of water within 1 K at station pressures from sea level to about 9 km, with the residual growing with altitude. The ISA lapse-rate version is expected to be more accurate than the isothermal version below 3 km and less accurate above 5 km. The Engineering ToolBox table and every computed IAPWS-at-ISA series are reference-only: they measure agreement with a computed curve, not accuracy against measurement, and they cannot test this claim. Measured pairs must come from sources whose retrieval is logged per route (URL or record ID, fetch result, rows obtained): Osborne, Stimson and Ginnings (1939); the CRC Handbook table; Keene (1995); NIST RP1229; and station or summit records above 8 km. Each band (0-3, 3-6, 6-9 km) reports n. Supported only if measured residuals meet the bands above. Disconfirmed if the ISA version is at least as accurate as the isothermal one at all measured altitudes. If no measured rows are obtained, the result is reported as untested, with no accuracy claim.",
  "relation_rationale": "Same frame; measured benchmark kept, computed table demoted to reference-only.",
  "confidence_delta": "decreased",
  "key_changes": [
    "Reclassified this round: all three artifacts are null or broken against the ask, since each compares against a computed reference and none tests measured data; no lead survives.",
    "Kept the measured boiling-point and station-pressure comparison as the primary test and the only route that can answer the request.",
    "Required a per-route retrieval log (URL or record ID, fetch result, rows obtained) for each measured source, so the record shows what was actually attempted.",
    "Stated that the Engineering ToolBox table is a computed reference, with -0.31 to +1.94 K agreement with IAPWS-at-ISA over all 125 rows (Iteration 1 figure, not restated as a new result).",
    "Corrected the 0-3 km statement: the isothermal model is closer to the IAPWS-at-ISA reference below 3 km (bias +0.020 K vs -0.093 K), and less close at 3 km and above. The near-surface reversal reflects the reference being an ISA calculation.",
    "Dropped further computed-reference decomposition (art_Dwo3Mclnlbtv) as a direction until a measured row exists.",
    "Removed anchor sensitivity from untried candidates because it was run in two artifacts this round.",
    "Kept the empirical fit and the IAPWS-enthalpy variant as candidates, to be tested only against measured rows."
  ],
  "strands": [
    {
      "artifact": "art_e7cQzFbFiEBS",
      "state": "null",
      "why": "Measured n=0 in every band; computed V3 bias -1.72 K vs ToolBox at 6 km+ (n=42). No measured test."
    },
    {
      "artifact": "art_qQYKsNWhqlKr",
      "state": "broken",
      "why": "Never tested the claim: measured n=0 for all bands; only computed checks ran. Measured route failed again."
    },
    {
      "artifact": "art_Dwo3Mclnlbtv",
      "state": "null",
      "why": "Atmosphere term -2.2 K vs thermodynamic term at 6-9 km, against ToolBox only; repeats V1-V4 numbers; no measured rows."
    }
  ],
  "evidence_state": "weak_or_null",
  "request_ledger": [
    {
      "part": "Predict water boiling point vs altitude with the simple barometric formula",
      "status": "partial",
      "evidence": "art_SznfD9DKXm93 and art_Dwo3Mclnlbtv: isothermal constant-enthalpy predictions computed and compared to ToolBox only; not checked against measurements.",
      "closes_with": "Measured station-pressure and boiling-point pairs from Osborne 1939, CRC Handbook, Keene 1995 or NIST RP1229."
    },
    {
      "part": "Compare predictions with published measured boiling-point values",
      "status": "untested",
      "evidence": "Measured set is empty (n=0) in art_e7cQzFbFiEBS and art_qQYKsNWhqlKr; Osborne 1939, CRC and Keene 1995 not transcribed.",
      "closes_with": "Transcribed rows from Osborne 1939, CRC Handbook, Keene 1995 or NIST RP1229, each with a retrieval log entry."
    },
    {
      "part": "Accuracy across different altitudes from 0 to 9 km",
      "status": "partial",
      "evidence": "Band statistics 0-3, 3-6, 6-9 km exist only against the computed ToolBox reference; no measured band has n above 0.",
      "closes_with": "Measured pairs spanning 0 to above 8 km, with n stated per band."
    },
    {
      "part": "Whether adding the ISA lapse rate improves the barometric prediction",
      "status": "partial",
      "evidence": "art_SznfD9DKXm93 and art_e7cQzFbFiEBS: V3 better below 3 km and worse above 5 km against the computed reference only.",
      "closes_with": "Same measured set run through V1 (isothermal) and V3 (ISA) with bands reported."
    },
    {
      "part": "Attribute the error to the thermodynamic vs atmospheric approximation",
      "status": "partial",
      "evidence": "art_Dwo3Mclnlbtv splits the residual against the computed reference only; the IAPWS-enthalpy variant has no measured comparison.",
      "closes_with": "IAPWS-IF97 enthalpy variants V2 and V4 run against the same measured pairs."
    },
    {
      "part": "Boiling points at high altitude above 8 km from station or summit records",
      "status": "untested",
      "evidence": "No measured record above 5 km was found in any artifact; summit values in sources are calculations.",
      "closes_with": "Station or summit records above 8 km that report both boiling temperature and station pressure."
    }
  ],
  "direction_options": [
    {
      "move": "cover",
      "target": "Measured boiling-temperature and station-pressure pairs, 0-8 km, from Osborne 1939, CRC Handbook, Keene 1995 and NIST RP1229",
      "case_for": "This is the core of the request and is still untested after two rounds. Only measured rows can change the answer; every other artifact compares against a computed curve.",
      "case_against": "Two rounds of retrieval returned no rows. One iteration remains, so this may fail again and leave the measured comparison untested. The run would then end with no accuracy claim.",
      "share": "main"
    },
    {
      "move": "cover",
      "target": "Station or summit records above 8 km with boiling temperature and station pressure",
      "case_for": "Covers the high-altitude part of the request that no artifact has reached. Summit records are the most direct test of the 6-9 km residual.",
      "case_against": "Few published summit records report measured boiling temperature with station pressure; the search may yield nothing usable, as in Iteration 1.",
      "share": "secondary"
    },
    {
      "move": "deepen",
      "target": "Computed-reference decomposition of the ISA vs isothermal residual (art_Dwo3Mclnlbtv)",
      "case_for": "Already executed and internally consistent, with independent re-derivation matching the headline numbers.",
      "case_against": "Compares against a computed curve only; the reviewer records it repeats V1-V4 band numbers. It answers no part of the ask, and deepening a null round after round has stopped paying.",
      "share": "none"
    },
    {
      "move": "extend",
      "target": "V1-V4 on a second standard atmosphere or more computed altitudes",
      "case_for": "Cheap to run and would show whether the ISA/isothermal ordering depends on the atmosphere model.",
      "case_against": "Still computed-only and would not touch measurement. Adds more agreement statistics, which the reviewer already flagged as not an accuracy claim.",
      "share": "none"
    },
    {
      "move": "pivot",
      "target": "Empirical polynomial fit of boiling temperature to measured pressure data",
      "case_for": "Would test whether any analytic model beats a fitted curve against measurement.",
      "case_against": "Needs measured rows that do not yet exist; it cannot run in this iteration if acquisition fails, so it can only follow cover.",
      "share": "none"
    },
    {
      "move": "declare",
      "target": "Write up the run as untested for the measured comparison, with computed-reference results as context",
      "case_for": "Honest if no iteration follows this one; avoids claiming an answer that was never tested.",
      "case_against": "Gives up the one chance to answer the ask. Only valid if acquisition is not attempted, which the cover option does not assume.",
      "share": "none"
    }
  ],
  "move": "cover",
  "move_rationale": "Measured pairs are the ask and two rounds left them empty; only acquiring them can move the answer. Computed-reference work repeats prior results.",
  "direction_plan": "3 slots, all cover: 2 on measured pairs 0-8 km (Osborne 1939, CRC Handbook, Keene 1995, NIST RP1229), each route logged with URL or record ID, fetch result and rows obtained; test V1 and V3, and V2 and V4 if rows allow. 1 on station or summit records above 8 km. No computed-reference artifacts this round.",
  "untried_candidates": [
    "Osborne, Stimson and Ginnings (1939) measured vapour-pressure to boiling-point table (retrieval failed twice)",
    "CRC Handbook boiling point vs pressure table (not obtained)",
    "Keene (1995) J. Chem. Educ. compiled measured table (not located)",
    "NIST RP1229 measured boiling-point data (PDF returned no readable table text)",
    "Station and summit records above 8 km with boiling temperature and station pressure",
    "Everest summit boiling observations with station pressure",
    "Empirical polynomial fit to measured boiling-point data",
    "IAPWS-IF97 temperature-dependent enthalpy variants (V2, V4) against measured pairs",
    "ISA lapse rate with temperature-dependent enthalpy against measured pairs"
  ],
  "coverage": "partial",
  "coverage_statement": "The next iteration will answer the measured-comparison part of the ask by acquiring measured pairs with a retrieval log, then testing V1 and V3 (and V2, V4 where possible) against them, with high-altitude records above 8 km as a secondary route.",
  "candidates_considered": 6,
  "relation_type": "evolution",
  "artifact_relations": [
    {
      "from_id": "art_39-uxNptYM5-",
      "to_id": "art_e7cQzFbFiEBS",
      "relation_type": "uses",
      "relation_rationale": "Uses the 250-row reference table as the computed context for V1-V4 comparisons."
    },
    {
      "from_id": "art_meMsxdA1r_bm",
      "to_id": "art_e7cQzFbFiEBS",
      "relation_type": "background",
      "relation_rationale": "Provenance audit sets the ToolBox table as an unverified computed reference."
    },
    {
      "from_id": "art_39-uxNptYM5-",
      "to_id": "art_qQYKsNWhqlKr",
      "relation_type": "uses",
      "relation_rationale": "Runs computed checks on the reference dataset; no measured rows were available."
    },
    {
      "from_id": "art_39-uxNptYM5-",
      "to_id": "art_Dwo3Mclnlbtv",
      "relation_type": "uses",
      "relation_rationale": "Residuals are taken against the computed ToolBox and IAPWS-at-ISA series in this table."
    },
    {
      "from_id": "art_meMsxdA1r_bm",
      "to_id": "art_Dwo3Mclnlbtv",
      "relation_type": "background",
      "relation_rationale": "Provenance finding that the ToolBox method is unstated motivates the attribution split."
    }
  ]
}
```

### [4] TOOL RESULT — Write · 2026-11-19 23:20:32 UTC

```
{"type": "create", "filePath": "/Volumes/aii-s20030/work/run_ek8xZiRG71Qn/3_invention_loop/iter_2/upd_hypo/upd_hypo/.terminal_claude_agent_struct_out.json", "content": "{\n  \"title\": \"Barometric boiling model vs measured data\",\n  \"hypothesis\": \"Untested until measured pairs exist. The isothermal barometric model with a constant-enthalpy Clausius-Clapeyron step predicts independently measured boiling temperatures of water within 1 K at station pressures from sea level to about 9 km, with the residual growing with altitude. The ISA lapse-rate version is expected to be more accurate than the isothermal version below 3 km and less accurate above 5 km. The Engineering ToolBox table and every computed IAPWS-at-ISA series are reference-only: they measure agreement with a computed curve, not accuracy against measurement, and they cannot test this claim. Measured pairs must come from sources whose retrieval is logged per route (URL or record ID, fetch result, rows obtained): Osborne, Stimson and Ginnings (1939); the CRC Handbook table; Keene (1995); NIST RP1229; and station or summit records above 8 km. Each band (0-3, 3-6, 6-9 km) reports n. Supported only if measured residuals meet the bands above. Disconfirmed if the ISA version is at least as accurate as the isothermal one at all measured altitudes. If no measured rows are obtained, the result is reported as untested, with no accuracy claim.\",\n  \"relation_rationale\": \"Same frame; measured benchmark kept, computed table demoted to reference-only.\",\n  \"confidence_delta\": \"decreased\",\n  \"key_changes\": [\n    \"Reclassified this round: all three artifacts are null or broken against the ask, since each compares against a computed reference and none tests measured data; no lead survives.\",\n    \"Kept the measured boiling-point and station-pressure comparison as the primary test and the only route that can answer the request.\",\n    \"Required a per-route retrieval log (URL or record ID, fetch result, rows obtained) for each measured source, so the record shows what was actually attempted.\",\n    \"Stated that the Engineering ToolBox table is a computed reference, with -0.31 to +1.94 K agreement with IAPWS-at-ISA over all 125 rows (Iteration 1 figure, not restated as a new result).\",\n    \"Corrected the 0-3 km statement: the isothermal model is closer to the IAPWS-at-ISA reference below 3 km (bias +0.020 K vs -0.093 K), and less close at 3 km and above. The near-surface reversal reflects the reference being an ISA calculation.\",\n    \"Dropped further computed-reference decomposition (art_Dwo3Mclnlbtv) as a direction until a measured row exists.\",\n    \"Removed anchor sensitivity from untried candidates because it was run in two artifacts this round.\",\n    \"Kept the empirical fit and the IAPWS-enthalpy variant as candidates, to be tested only against measured rows.\"\n  ],\n  \"strands\": [\n    {\n      \"artifact\": \"art_e7cQzFbFiEBS\",\n      \"state\": \"null\",\n      \"why\": \"Measured n=0 in every band; computed V3 bias -1.72 K vs ToolBox at 6 km+ (n=42). No measured test.\"\n    },\n    {\n      \"artifact\": \"art_qQYKsNWhqlKr\",\n      \"state\": \"broken\",\n      \"why\": \"Never tested the claim: measured n=0 for all bands; only computed checks ran. Measured route failed again.\"\n    },\n    {\n      \"artifact\": \"art_Dwo3Mclnlbtv\",\n      \"state\": \"null\",\n      \"why\": \"Atmosphere term -2.2 K vs thermodynamic term at 6-9 km, against ToolBox only; repeats V1-V4 numbers; no measured rows.\"\n    }\n  ],\n  \"evidence_state\": \"weak_or_null\",\n  \"request_ledger\": [\n    {\n      \"part\": \"Predict water boiling point vs altitude with the simple barometric formula\",\n      \"status\": \"partial\",\n      \"evidence\": \"art_SznfD9DKXm93 and art_Dwo3Mclnlbtv: isothermal constant-enthalpy predictions computed and compared to ToolBox only; not checked against measurements.\",\n      \"closes_with\": \"Measured station-pressure and boiling-point pairs from Osborne 1939, CRC Handbook, Keene 1995 or NIST RP1229.\"\n    },\n    {\n      \"part\": \"Compare predictions with published measured boiling-point values\",\n      \"status\": \"untested\",\n      \"evidence\": \"Measured set is empty (n=0) in art_e7cQzFbFiEBS and art_qQYKsNWhqlKr; Osborne 1939, CRC and Keene 1995 not transcribed.\",\n      \"closes_with\": \"Transcribed rows from Osborne 1939, CRC Handbook, Keene 1995 or NIST RP1229, each with a retrieval log entry.\"\n    },\n    {\n      \"part\": \"Accuracy across different altitudes from 0 to 9 km\",\n      \"status\": \"partial\",\n      \"evidence\": \"Band statistics 0-3, 3-6, 6-9 km exist only against the computed ToolBox reference; no measured band has n above 0.\",\n      \"closes_with\": \"Measured pairs spanning 0 to above 8 km, with n stated per band.\"\n    },\n    {\n      \"part\": \"Whether adding the ISA lapse rate improves the barometric prediction\",\n      \"status\": \"partial\",\n      \"evidence\": \"art_SznfD9DKXm93 and art_e7cQzFbFiEBS: V3 better below 3 km and worse above 5 km against the computed reference only.\",\n      \"closes_with\": \"Same measured set run through V1 (isothermal) and V3 (ISA) with bands reported.\"\n    },\n    {\n      \"part\": \"Attribute the error to the thermodynamic vs atmospheric approximation\",\n      \"status\": \"partial\",\n      \"evidence\": \"art_Dwo3Mclnlbtv splits the residual against the computed reference only; the IAPWS-enthalpy variant has no measured comparison.\",\n      \"closes_with\": \"IAPWS-IF97 enthalpy variants V2 and V4 run against the same measured pairs.\"\n    },\n    {\n      \"part\": \"Boiling points at high altitude above 8 km from station or summit records\",\n      \"status\": \"untested\",\n      \"evidence\": \"No measured record above 5 km was found in any artifact; summit values in sources are calculations.\",\n      \"closes_with\": \"Station or summit records above 8 km that report both boiling temperature and station pressure.\"\n    }\n  ],\n  \"direction_options\": [\n    {\n      \"move\": \"cover\",\n      \"target\": \"Measured boiling-temperature and station-pressure pairs, 0-8 km, from Osborne 1939, CRC Handbook, Keene 1995 and NIST RP1229\",\n      \"case_for\": \"This is the core of the request and is still untested after two rounds. Only measured rows can change the answer; every other artifact compares against a computed curve.\",\n      \"case_against\": \"Two rounds of retrieval returned no rows. One iteration remains, so this may fail again and leave the measured comparison untested. The run would then end with no accuracy claim.\",\n      \"share\": \"main\"\n    },\n    {\n      \"move\": \"cover\",\n      \"target\": \"Station or summit records above 8 km with boiling temperature and station pressure\",\n      \"case_for\": \"Covers the high-altitude part of the request that no artifact has reached. Summit records are the most direct test of the 6-9 km residual.\",\n      \"case_against\": \"Few published summit records report measured boiling temperature with station pressure; the search may yield nothing usable, as in Iteration 1.\",\n      \"share\": \"secondary\"\n    },\n    {\n      \"move\": \"deepen\",\n      \"target\": \"Computed-reference decomposition of the ISA vs isothermal residual (art_Dwo3Mclnlbtv)\",\n      \"case_for\": \"Already executed and internally consistent, with independent re-derivation matching the headline numbers.\",\n      \"case_against\": \"Compares against a computed curve only; the reviewer records it repeats V1-V4 band numbers. It answers no part of the ask, and deepening a null round after round has stopped paying.\",\n      \"share\": \"none\"\n    },\n    {\n      \"move\": \"extend\",\n      \"target\": \"V1-V4 on a second standard atmosphere or more computed altitudes\",\n      \"case_for\": \"Cheap to run and would show whether the ISA/isothermal ordering depends on the atmosphere model.\",\n      \"case_against\": \"Still computed-only and would not touch measurement. Adds more agreement statistics, which the reviewer already flagged as not an accuracy claim.\",\n      \"share\": \"none\"\n    },\n    {\n      \"move\": \"pivot\",\n      \"target\": \"Empirical polynomial fit of boiling temperature to measured pressure data\",\n      \"case_for\": \"Would test whether any analytic model beats a fitted curve against measurement.\",\n      \"case_against\": \"Needs measured rows that do not yet exist; it cannot run in this iteration if acquisition fails, so it can only follow cover.\",\n      \"share\": \"none\"\n    },\n    {\n      \"move\": \"declare\",\n      \"target\": \"Write up the run as untested for the measured comparison, with computed-reference results as context\",\n      \"case_for\": \"Honest if no iteration follows this one; avoids claiming an answer that was never tested.\",\n      \"case_against\": \"Gives up the one chance to answer the ask. Only valid if acquisition is not attempted, which the cover option does not assume.\",\n      \"share\": \"none\"\n    }\n  ],\n  \"move\": \"cover\",\n  \"move_rationale\": \"Measured pairs are the ask and two rounds left them empty; only acquiring them can move the answer. Computed-reference work repeats prior results.\",\n  \"direction_plan\": \"3 slots, all cover: 2 on measured pairs 0-8 km (Osborne 1939, CRC Handbook, Keene 1995, NIST RP1229), each route logged with URL or record ID, fetch result and rows obtained; test V1 and V3, and V2 and V4 if rows allow. 1 on station or summit records above 8 km. No computed-reference artifacts this round.\",\n  \"untried_candidates\": [\n    \"Osborne, Stimson and Ginnings (1939) measured vapour-pressure to boiling-point table (retrieval failed twice)\",\n    \"CRC Handbook boiling point vs pressure table (not obtained)\",\n    \"Keene (1995) J. Chem. Educ. compiled measured table (not located)\",\n    \"NIST RP1229 measured boiling-point data (PDF returned no readable table text)\",\n    \"Station and summit records above 8 km with boiling temperature and station pressure\",\n    \"Everest summit boiling observations with station pressure\",\n    \"Empirical polynomial fit to measured boiling-point data\",\n    \"IAPWS-IF97 temperature-dependent enthalpy variants (V2, V4) against measured pairs\",\n    \"ISA lapse rate with temperature-dependent enthalpy against measured pairs\"\n  ],\n  \"coverage\": \"partial\",\n  \"coverage_statement\": \"The next iteration will answer the measured-comparison part of the ask by acquiring measured pairs with a retrieval log, then testing V1 and V3 (and V2, V4 where possible) against them, with high-altitude records above 8 km as a secondary route.\",\n  \"candidates_considered\": 6,\n  \"relation_type\": \"evolution\",\n  \"artifact_relations\": [\n    {\n      \"from_id\": \"art_39-uxNptYM5-\",\n      \"to_id\": \"art_e7cQzFbFiEBS\",\n      \"relation_type\": \"uses\",\n      \"relation_rationale\": \"Uses the 250-row reference table as the computed context for V1-V4 comparisons.\"\n    },\n    {\n      \"from_id\": \"art_meMsxdA1r_bm\",\n      \"to_id\": \"art_e7cQzFbFiEBS\",\n      \"relation_type\": \"background\",\n      \"relation_rationale\": \"Provenance audit sets the ToolBox table as an unverified computed reference.\"\n    },\n    {\n      \"from_id\": \"art_39-uxNptYM5-\",\n      \"to_id\": \"art_qQYKsNWhqlKr\",\n      \"relation_type\": \"uses\",\n      \"relation_rationale\": \"Runs computed checks on the reference dataset; no measured rows were available.\"\n    },\n    {\n      \"from_id\": \"art_39-uxNptYM5-\",\n      \"to_id\": \"art_Dwo3Mclnlbtv\",\n      \"relation_type\": \"uses\",\n      \"relation_rationale\": \"Residuals are taken against the computed ToolBox and IAPWS-at-ISA series in this table.\"\n    },\n    {\n      \"from_id\": \"art_meMsxdA1r_bm\",\n      \"to_id\": \"art_Dwo3Mclnlbtv\",\n      \"relation_type\": \"background\",\n      \"relation_rationale\": \"Provenance finding that the ToolBox method is unstated motivates the attribution split.\"\n    }\n  ]\n}\n", "structuredPatch": [], "originalFile": null, "userModified": false}
```

### [5] ASSISTANT · 2026-11-19 23:20:36 UTC

```
I wrote the revision to `.terminal_claude_agent_struct_out.json` in the workspace. The main move is `cover`: acquire measured boiling-point and station-pressure pairs, because that is the part of the request still untested.

**Round classification (one strand per artifact):**
- `art_e7cQzFbFiEBS`: **null**. Measured n=0 in every band; the only numbers are computed V3 bias against the ToolBox table.
- `art_qQYKsNWhqlKr`: **broken**. It never tested the claim, because the measured set was empty and only computed checks ran.
- `art_Dwo3Mclnlbtv`: **null**. The ISA-versus-isothermal split is against a computed reference only.

Round summary: `weak_or_null`. No genuine positive and no lead survives.

**Main choices:**
- **Direction:** `cover` on measured pairs from 0 to 8 km (Osborne 1939, CRC Handbook, Keene 1995, NIST RP1229), each route logged. `cover` on station or summit records above 8 km is secondary. `deepen` on the computed decomposition is rejected because it repeats earlier numbers and does not touch the ask.
- **Slot split:** two slots on measured pairs, one on records above 8 km, no computed-reference artifacts.
- **Coverage:** `partial`. Every ledger row is partial or untested, and none is done.
- **Reviewer points:** the 0–3 km sentence is corrected (the isothermal model is closer there, which reflects the ISA-built reference), and the 0.31 K figure is no longer presented as a restated result.

**Points to check:**
- The run says this is the final iteration, but the task still asks for a steering move for a next iteration. I chose `cover` rather than `declare`. If no iteration follows, the honest outcome is that the measured comparison stays untested, and `declare` would be the correct label.
- I did not re-fetch any source or verify the ToolBox transcription, as the reviewer asked. The revision relies on the reviewer's and the artifacts' own statements.
```
