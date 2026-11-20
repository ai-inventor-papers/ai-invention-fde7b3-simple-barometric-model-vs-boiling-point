# final_review — report_results

> Phase: `gen_paper_repo` · `final_review`
> Run: `run_ek8xZiRG71Qn` — Isothermal Barometric Boiling Points Match a Computed Table to 0.6 K
>
> Full, verbatim record of every prompt the AI Inventor pipeline gave this agent — system-user, human-user and skill-input — in the order they landed. Nothing truncated.

## Task: `final_review` (terminal_claude_agent)

### [1] SYSTEM-USER prompt · 2026-11-20 04:08:27 UTC

```
<reviewer_role>
You are the last reader before this run's work is published: an independent reviewer who wrote
none of it. Every output was written by other agents from the same run record. You review them
the way a careful journal reviewer reviews a submission, and then, unlike a journal reviewer, you
fix what you find, in place, so that what gets published is right.

THE ARTIFACTS ARE THE GROUND TRUTH
The run's artifacts (the experiments' result files, tables and logs) are what happened. Every... [truncated, 53261 chars total]
```

### [2] SYSTEM-USER prompt · 2026-11-20 04:18:30 UTC

```
[Image: original 390x9557, displayed at 82x2000. Multiply coordinates by 4.76 to map to original image.]
```

### [3] SYSTEM-USER prompt · 2026-11-20 04:18:30 UTC

```
[Image: original 1440x8879, displayed at 324x2000. Multiply coordinates by 4.44 to map to original image.]
```

### [4] SYSTEM-USER prompt · 2026-11-20 04:19:46 UTC

```
TERMINOLOGY CHECK FAILED: 1 naming issue(s) in paper.tex.

A reader finds this paper by searching for the field's words. A private label costs it those readers, and a bare run-internal code costs the sentence its meaning:
- Undefined coinages (4): Clausius-Clapeyron, constant-enthalpy, pre-stated, root-finding. None of these appears in the field's own vocabulary or in any cited title, and none is defined within a sentence of its use. Use the field's existing name, or define the term explicitly on first use and keep the same words afterwards.

For each one, exactly one of these applies:
1. The field already names this — use <domain_vocabulary>'s spelling everywhere
2. It is genuinely new — define it once at first use ('we call X ...', 'we define X as ...') and keep the wording identical afterwards
3. It is a bare code in a sentence — replace it with the name of the thing it stands for; codes stay in table headers only

Change nothing else: numbers, claims, citations and figures stay as they are. Then recompile the PDF.
```

### [5] SYSTEM-USER prompt · 2026-11-20 04:20:28 UTC

```
TERMINOLOGY CHECK FAILED: 1 naming issue(s) in paper.tex.

A reader finds this paper by searching for the field's words. A private label costs it those readers, and a bare run-internal code costs the sentence its meaning:
- Undefined coinages (1): constant-enthalpy. None of these appears in the field's own vocabulary or in any cited title, and none is defined within a sentence of its use. Use the field's existing name, or define the term explicitly on first use and keep the same words afterwards.

For each one, exactly one of these applies:
1. The field already names this — use <domain_vocabulary>'s spelling everywhere
2. It is genuinely new — define it once at first use ('we call X ...', 'we define X as ...') and keep the wording identical afterwards
3. It is a bare code in a sentence — replace it with the name of the thing it stands for; codes stay in table headers only

Change nothing else: numbers, claims, citations and figures stay as they are. Then recompile the PDF.
```

### [6] SYSTEM-USER prompt · 2026-11-20 04:20:54 UTC

```
LAYOUT CHECK FAILED in paper.tex:
- lines 163--164 of paper.tex run 25pt past the right margin, where the page cuts them off

You MUST:
1. Make each table at those lines fit \textwidth: give prose columns a `p{...}` width or use `tabularx` with `X` columns so their cells wrap, set it in \footnotesize, and split a table of more than 7 columns in two or transpose it. Never leave long text in an `l`, `c` or `r` column, and never shrink a whole table with \resizebox
2. Let a long word, URL, \texttt run or inline formula break (\url, \allowbreak, a formula split into several $...$ pieces or set as display math) instead of overrunning
3. Change nothing else: text, tables and numbers stay as they are
4. Recompile, then check: `grep 'Overfull .hbox' paper.log` lists nothing more than a few points wide, and the last page is more than a few lines
```

### [7] SYSTEM-USER prompt · 2026-11-20 04:21:12 UTC

```
LAYOUT CHECK FAILED in paper.tex:
- lines 163--164 of paper.tex run 25pt past the right margin, where the page cuts them off

You MUST:
1. Make each table at those lines fit \textwidth: give prose columns a `p{...}` width or use `tabularx` with `X` columns so their cells wrap, set it in \footnotesize, and split a table of more than 7 columns in two or transpose it. Never leave long text in an `l`, `c` or `r` column, and never shrink a whole table with \resizebox
2. Let a long word, URL, \texttt run or inline formula break (\url, \allowbreak, a formula split into several $...$ pieces or set as display math) instead of overrunning
3. Change nothing else: text, tables and numbers stay as they are
4. Recompile, then check: `grep 'Overfull .hbox' paper.log` lists nothing more than a few points wide, and the last page is more than a few lines
```
