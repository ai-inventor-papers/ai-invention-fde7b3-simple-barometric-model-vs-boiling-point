# gen_report_text — test_idea

> Phase: `invention_loop` · round 2 · `gen_report_text`
> Run: `run_ek8xZiRG71Qn` — Isothermal Barometric Boiling Points Match a Computed Table to 0.6 K
>
> Full, verbatim record of every prompt the AI Inventor pipeline gave this agent — system-user, human-user and skill-input — in the order they landed. Nothing truncated.

## Task: `gen_report_text` (terminal_claude_agent)

### [1] SYSTEM-USER prompt · 2026-11-19 23:10:31 UTC

```
<ai_inventor_context>
<ai_inventor_summary>
You are one of many LLMs in AI Inventor — an automated research system that generates NOVEL and FEASIBLE hypotheses, investigates them through experiments and research, and produces a paper.

Your output feeds other LLMs downstream. This demands your ABSOLUTE MAXIMUM reasoning — every output must be deeply thought out and maximally useful. Surface-level responses waste downstream computation.
</ai_inventor_summary>

<your_role>
YOU ARE: The run's resea... [truncated, 107092 chars total]
```

### [2] SYSTEM-USER prompt · 2026-11-19 23:13:49 UTC

```
<style_check>
The draft was measured against the <writing_register> in your prompt and trips it:

- 6.7 em dashes per 1,000 words; the limit is 3. Replace them with commas, colons or full stops.

Revise the PROSE of the draft in `./paper_draft.md` to fix each point, then emit the structured output again. Numbers, claims, citations, [FIGURE:...] markers and [ARTIFACT:...] markers stay exactly as they are; do not add content and do not change results. The figures array is unchanged.
</style_check>
```

### [3] SYSTEM-USER prompt · 2026-11-19 23:14:13 UTC

```
<terminology_check>
The draft was measured against <domain_vocabulary> and trips it in 2 place(s):

- Bare label codes in the body text: IF97, V1, V2, V3, V4. These are the run's own internal row labels, meaningless to a reader. Name each condition, metric or variant the way the field names it, and keep the codes in the tables only.
- Undefined coinages (25): "most likely computed", "no statistic", Clausius-Clapeyron, IAPWS-at-ISA, ISA-based, Round-trip, boiling-points-water-altitude, boiling-temperature-versus-pressure, code-level, constant-enthalpy, enthalpy-effect, from-memory. None of these appears in the field's own vocabulary or in any cited title, and none is defined within a sentence of its use. Use the field's existing name, or define the term explicitly on first use and keep the same words afterwards.

For each one, exactly one of these applies:
1. The field already names this — use <domain_vocabulary>'s spelling everywhere
2. It is genuinely new — define it once at first use ('we call X ...', 'we define X as ...') and keep the wording identical afterwards
3. It is a bare code in a sentence — replace it with the name of the thing it stands for; codes stay in table headers only

Rename in the section you wrote this iteration. An earlier section keeps its words unless the rename is a factual correction, and then it is marked as one. Numbers, claims, citations and every [FIGURE:...] and [ARTIFACT:...] marker stay exactly as they are. Save the text to `./paper_draft.md`, then emit the structured output again.
</terminology_check>
```
