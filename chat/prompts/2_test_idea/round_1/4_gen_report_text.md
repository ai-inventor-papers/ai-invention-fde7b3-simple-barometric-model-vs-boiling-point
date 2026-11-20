# gen_report_text — test_idea

> Phase: `invention_loop` · round 1 · `gen_report_text`
> Run: `run_ek8xZiRG71Qn` — Isothermal Barometric Boiling Points Match a Computed Table to 0.6 K
>
> Full, verbatim record of every prompt the AI Inventor pipeline gave this agent — system-user, human-user and skill-input — in the order they landed. Nothing truncated.

## Task: `gen_report_text` (terminal_claude_agent)

### [1] SYSTEM-USER prompt · 2026-11-19 22:47:23 UTC

```
<ai_inventor_context>
<ai_inventor_summary>
You are one of many LLMs in AI Inventor — an automated research system that generates NOVEL and FEASIBLE hypotheses, investigates them through experiments and research, and produces a paper.

Your output feeds other LLMs downstream. This demands your ABSOLUTE MAXIMUM reasoning — every output must be deeply thought out and maximally useful. Surface-level responses waste downstream computation.
</ai_inventor_summary>

<your_role>
YOU ARE: The run's resea... [truncated, 65206 chars total]
```

### [2] SYSTEM-USER prompt · 2026-11-19 22:52:15 UTC

```
<style_check>
The draft was measured against the <writing_register> in your prompt and trips it:

- 6.1 em dashes per 1,000 words; the limit is 3. Replace them with commas, colons or full stops.

Revise the PROSE of the draft in `./paper_draft.md` to fix each point, then emit the structured output again. Numbers, claims, citations, [FIGURE:...] markers and [ARTIFACT:...] markers stay exactly as they are; do not add content and do not change results. The figures array is unchanged.
</style_check>
```

### [3] SYSTEM-USER prompt · 2026-11-19 22:52:45 UTC

```
<terminology_check>
The draft was measured against <domain_vocabulary> and trips it in 2 place(s):

- Bare label codes in the body text: IF97, P0. These are the run's own internal row labels, meaningless to a reader. Name each condition, metric or variant the way the field names it, and keep the codes in the tables only.
- Undefined coinages (17): "s residual values and the experiment", "s residuals and the experiment", Clausius-Clapeyron, IAPWS-at-ISA, IAPWS-based, ISA-plus-constant-enthalpy, Per-kilometre, altitude-boiling, boiling-points-water-altitude, constant-enthalpy, high-altitude, isothermal-minus-ISA. None of these appears in the field's own vocabulary or in any cited title, and none is defined within a sentence of its use. Use the field's existing name, or define the term explicitly on first use and keep the same words afterwards.

For each one, exactly one of these applies:
1. The field already names this — use <domain_vocabulary>'s spelling everywhere
2. It is genuinely new — define it once at first use ('we call X ...', 'we define X as ...') and keep the wording identical afterwards
3. It is a bare code in a sentence — replace it with the name of the thing it stands for; codes stay in table headers only

Rename in the section you wrote this iteration. An earlier section keeps its words unless the rename is a factual correction, and then it is marked as one. Numbers, claims, citations and every [FIGURE:...] and [ARTIFACT:...] marker stay exactly as they are. Save the text to `./paper_draft.md`, then emit the structured output again.
</terminology_check>
```
