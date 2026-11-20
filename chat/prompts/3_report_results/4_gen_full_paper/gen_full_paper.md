# gen_full_paper — report_results

> Phase: `gen_paper_repo` · `gen_full_paper`
> Run: `run_ek8xZiRG71Qn` — Isothermal Barometric Boiling Points Match a Computed Table to 0.6 K
>
> Full, verbatim record of every prompt the AI Inventor pipeline gave this agent — system-user, human-user and skill-input — in the order they landed. Nothing truncated.

## Task: `gen_full_paper` (terminal_claude_agent)

### [1] HUMAN-USER prompt · 2026-11-20 02:44:53 UTC

````
<research_methodology>
Write like an experienced academic. Reviewers judge both the science and the writing.

- Claims must be proportional to evidence. Choose verbs carefully — "demonstrate," "observe," and "hypothesize" mean different things.
- Every result needs: what was measured, on what data, the numbers, and what they mean.
- Methodology must be specific enough to reproduce. Section placement follows <paper_structure> below.
- State limitations honestly. Avoid both overclaiming and excessive hedging.
</research_methodology>

<paper_structure>
Use the structure an expert in the field expects, in this order: Abstract; 1 Introduction; 2 Related Work; 3 Method; 4 Experimental Setup; 5 Results; 6 Discussion and Limitations; 7 Conclusion. Merge or rename a section only where the work genuinely has nothing for it — never by folding it into the Introduction.

- The Introduction contains ONLY: the problem and why it matters, the gap in existing work, the idea in one or two sentences, a contributions list carrying the headline numbers, a one-sentence pointer to the Figure 1 overview at its end, and a one-sentence roadmap of the paper.
- NO literature survey and NO method details in the Introduction. Prior work goes to Related Work, how the method works goes to Method; the Figure 1 overview shows its shape, and its caption and the Method section explain it.
- Organize Related Work by theme rather than one paragraph per paper, and close each theme with a sentence on how this work differs.
- Experimental Setup carries data, baselines, metrics and protocol — enough for an expert to rerun it. Results carries findings, not setup.
</paper_structure>

<results_first>
Ask what a reader actually wants from the paper: the results, with numbers. A reader must be able to get the main finding from the abstract, the main results table and the first results figure alone.

- State the key quantitative results, with the actual numbers, in three places: the abstract, the contributions list, and the opening of Results.
- Results opens with a main results table: the method against every baseline on the headline metric, with variance.
- Every major claim gets at least one results figure (figure_type "data"), plus an ablation or sensitivity plot wherever the artifacts hold the numbers for one.
- Past the Figure 1 overview, prefer a plot of real numbers over concept art — keep further concept figures to the pipeline diagram the method genuinely needs.
- Reference every figure and table by number in the text and interpret it there: say what the reader should take from it. Never drop one in unexplained.
</results_first>

<figure_placement>
Where a figure sits, what shape it takes and how many there are decide whether a reader can follow the paper.

- Put each [FIGURE:id] marker directly after the paragraph that first discusses the figure, inside the section that owns it: the Figure 1 overview and then the headline data figure at the end of the Introduction, method and pipeline diagrams in Method, the main comparison and the per-claim results figures in Results, ablation and sensitivity plots in Results or Discussion. Never place a figure in the Abstract, Related Work or Conclusion.
- Let the data relationship pick the chart: grouped bars for the method against baselines on one metric, lines with error bands for trends, scaling and training curves, scatter or a Pareto front for trade-offs, heatmaps for matrices and pairwise grids. A handful of numbers is a table, not a figure. Use multiple panels only when they share axes and one takeaway.
- Aim for roughly four to eight figures in a full paper, with the Figure 1 overview first and the main results figure next. Each caption stands on its own: what is plotted, on what data, and the takeaway.
</figure_placement>

<safeguard_research_reporting>
When the research concerns bypassing or removing a model's safeguards (jailbreaks, refusal
removal, abliteration, safety fine-tuning reversal, or anything whose effect is a model that
refuses less on harmful requests), report the findings as MEASUREMENTS and their implications
for EVALUATION and DEFENCE, never as operational advice for defeating safeguards.
- State what was measured, on what, and how large the effect was, as in any other result.
- Draw the implications for the people who build and test safeguards: what an evaluation misses,
  which defences are brittle and where, what a safety evaluation should measure next.
- Never frame a finding as a recommendation, a recipe or a best configuration for removing
  refusals: no "the practical recommendation is to use X to remove refusals", no "for the
  strongest bypass, edit layers X to Y", no step-by-step settings a reader could follow to make a
  model comply with harmful requests.
- This applies everywhere the finding is stated: abstract, executive summary, key results, best
  result, discussion, conclusion, captions, the website and the interactive page.
</safeguard_research_reporting>

<system_reminder>
Do not ask follow up questions and do not ask the user anything. Execute all steps independently.
You must follow the todo list provided in each prompt exactly as written.
No placeholders, stubs, or incomplete code — all code must be complete and functional.
</system_reminder>

<process_isolation>
CRITICAL: Multiple pipeline runs may execute simultaneously on this machine. `ps aux | grep method.py` matches ALL runs, not just yours.
- NEVER kill processes by name (`killall`, `pkill -f`, `ps aux | grep ... | xargs kill`). This kills OTHER runs' processes.
- NEVER monitor processes by name (`ps aux | grep method.py`). You will see other runs' processes and get confused.
- ALWAYS use PID-based process management:
  Run: `uv run method.py & PID=$!` or `timeout <seconds> uv run method.py & PID=$!`
  Check: `kill -0 $PID 2>/dev/null && echo "Running" || echo "Ended"`
  Stop: `kill $PID`
  Wait: `wait $PID; echo "Exit code: $?"`
  Monitor: `tail -f logs/run.log & TAIL_PID=$!` then `kill $TAIL_PID` when done
</process_isolation>

<flex_environment>
You run in a disposable macOS virtual machine on Apple silicon, one guest of this run on its owner's Mac. The Apple GPU is reached through `mps` in torch and through MLX. CUDA does not exist here, there is no Docker and no Linux binary runs. Run one GPU process at a time; another guest may share the GPU.
Your own machine is the `text`: 4 vCPUs, 8 GB RAM (4 GB of it for the step), no GPU work.
Start every script that uses torch with the device line: `from aii_device import DEVICE, check; check()`; where `aii_device` is not installed, `DEVICE = torch.device("mps" if torch.backends.mps.is_available() else "cpu")`. Read the `aii-use-hardware` skill before planning compute.
Instead of each CUDA habit: vLLM -> mlx-lm or llama-server; FP8 -> bf16 or MLX 8-bit; bitsandbytes -> MLX 4-bit or 8-bit; Triton kernels -> torch ops or an MLX Metal kernel; float64 on the GPU -> the CPU; torch.cuda.* -> aii_device; .cuda() -> .to(DEVICE); "cuda" if torch.cuda.is_available() else "cpu" -> DEVICE (that test silently picks the CPU); flash-attn -> sdpa; several GPUs -> one device; torch.compile -> eager mode.
Known slow spots: LSTMs, small MLPs, ops that fall back to the CPU (warned in the log), the first MPS call's warm-up, and model downloads over a home link; every step fetches its inputs again.
What executor steps get: `text_small`: 2 vCPUs, 4 GB RAM (1 GB of it for the step), no GPU work; `text`: 4 vCPUs, 8 GB RAM (4 GB of it for the step), no GPU work; `gpu`: 6 vCPUs, 24 GB RAM (20 GB of it for the step), 12.8 GiB of GPU memory; `gpu_large`: 8 vCPUs, 64 GB RAM (60 GB of it for the step), 34 GiB of GPU memory. Text agents get `text`; an executor step gets `gpu` unless its plan's `flex_guest_shape` names another shape. `gpu` fits a step within 20 GB of RAM and 12.8 GiB of GPU memory; a step that needs more sets `flex_guest_shape` to `gpu_large`, the largest guest, which fits a step within 60 GB of RAM and 34 GiB of GPU memory. At most one runs at a time on the Mac, so a `gpu_large` step may wait longer for it. `flex_guest_shape` may name any shape listed, smaller ones only for a light step that fits their RAM for the step.
One step's inputs (the run's files plus its sessions) stay under 20 GB: keep large models and datasets out of the run's files.
Use `aii-mkvenv` or a plain `uv venv` for extra packages; never reinstall or upgrade torch.
</flex_environment>

<slot_environment>
You run in the `flex_slot` environment: your own macOS account in one long-lived guest that other agents share at the same time.
Your memory share is 4 GB: going over it stops your job alone. Your disk is 20 GB; keep temp files under $TMPDIR. You have no GPU work. Use ports from $AII_PORT_BASE or port 0.
</slot_environment>

<workspace>
Your workspace: `/Volumes/aii-s20021/work/run_ek8xZiRG71Qn/4_gen_paper_repo/_4_assemble_paper/paper/workspace`

CRITICAL: Every file you create, write, or save MUST be inside this workspace directory (subdirectories OK). You MUST NOT write files anywhere outside this path — external paths are READ-ONLY. Use absolute paths for all file operations.

EVERY file write MUST start with `/Volumes/aii-s20021/work/run_ek8xZiRG71Qn/4_gen_paper_repo/_4_assemble_paper/paper/workspace/`:
GOOD: `/Volumes/aii-s20021/work/run_ek8xZiRG71Qn/4_gen_paper_repo/_4_assemble_paper/paper/workspace/file.py`, `/Volumes/aii-s20021/work/run_ek8xZiRG71Qn/4_gen_paper_repo/_4_assemble_paper/paper/workspace/results/out.json`
BAD: `/tmp/file.py`, `~/output.json`, `./file.py`, any path outside the workspace
</workspace>
<disposable_outputs>
YOUR WORKING DIRECTORY IS A DELIVERABLE. When this module ends it must read
like a GitHub repository someone else can fork, resume and run — and the bulk
it holds must be either worth keeping or restorable. This run shares a storage
volume with the database; a run that fills it stops every other run on the box.

So before you finish, produce TWO files:

1. `.aii/manifest.yaml` — one entry per heavy path, each with EXACTLY ONE decision.
   The `.aii/` directory ALREADY EXISTS in your cwd: write the file into
   it. Do not create, replace or `touch` `.aii` itself — a plain file by
   that name makes the manifest unwritable for the rest of the module.

```yaml
entries:
  - path: results/
    keep: six GPU-hours of sweep output, not reproducible inside this run
  - path: hf_cache/
    delete: redownloadable
    source: "huggingface-cli download meta-llama/Llama-3-8B"
  - path: checkpoints/
    delete: regenerable
    source: "uv run train.py --epochs 3 --seed 0"
```

   - `keep:` takes a ONE-LINE reason. Use it for the expensive and the
     irreproducible: trained weights, long-running results, datasets you
     collected yourself.
   - `delete:` takes `redownloadable` (and a `source:` naming the repo id, URL
     or command) or `regenerable` (and a `source:` that is the command which
     rebuilds it). These are deleted AFTER the round ends, never mid-step.
   - Every path is RELATIVE TO YOUR CWD and must resolve INSIDE it. Absolute
     paths, `..`, and anything resolving outside are rejected.
   - Globs and whole directories are fine. A whole `hf_cache/` is ONE entry —
     do not list files individually.

2. `README.md` — written as if your cwd were a GitHub repository: what you
   did, the layout with a line per important file/directory, how to run it,
   and a **"Restoring removed files"** section giving the install/download
   command for EVERY `delete` entry. An `install.sh` or `restore.sh` beside it
   is welcome.

A CHECKER RUNS WHEN YOU SUBMIT. If anything heavy has no decision it fails
your submission and hands you the uncovered list, grouped by directory with
sizes, and you fix the manifest and submit again.

WHAT NEEDS NO DECISION — do not write entries for these:
- text and code files, at ANY size (source, JSON, CSV, YAML, logs, markdown);
- anything under the auto-keep floor (10 MB), whatever it holds.
Only large binaries and cache directories (`hf_cache/`, `.venv/`,
`node_modules/`, `checkpoints/`, `wandb/`, `__pycache__/`, …) need one.

NEVER mark your results, figures, papers, code, logs or anything a later step
reads as `delete`. If a later step needs it, it is a `keep`.

WHAT A `keep` BUYS YOU. Anything you do not mark `delete` stays exactly where
you wrote it, on this run's storage volume, at the path it already has — it is
not moved, renamed or copied. A later round reads it there, by that absolute
workspace path, so a checkpoint you keep is a checkpoint the next round can
load instead of retraining. It is also the ONLY copy: the publish step pushes
your cwd to GitHub but skips every file of 100 MB or
more, so trained weights and large binary artifacts never leave the volume.
Name each kept artifact in your results and your `README.md` by its path
RELATIVE to your cwd, and say it stays on the run's volume rather than in the
published repository. Never write an absolute server path into a file that is
published: a reader's machine has none of them.
</disposable_outputs>

continue where you left off — reuse any partial work already written to disk. Do NOT start over.
````

### [2] SYSTEM-USER prompt · 2026-11-20 02:48:20 UTC

```
<task>
Typeset <paper_draft> as LaTeX with BibTeX, insert <available_figures>, and compile it to PDF.
</task>

<tool_use>
Maximize parallel tool calls. Parallelize independent operations, only sequentialize dependencies.
- Multiple searches/fetches on different topics → parallel in one turn
- Search then fetch results → sequential (need URLs first)
</tool_use>

<publishable_paper_rules>
This is the PUBLISHABLE PAPER. The run's internal report ships beside this paper as its own PDF
and already ho... [truncated, 58958 chars total]
```

### [3] SYSTEM-USER prompt · 2026-11-20 02:49:42 UTC

```
[Image: original 3840x2149, displayed at 2000x1119. Multiply coordinates by 1.92 to map to original image.]
```

### [4] SYSTEM-USER prompt · 2026-11-20 02:53:11 UTC

```
REFERENCE CHECK FAILED: 1 citation key(s) in paper.tex are not backed by a fetched reference:
- ICAO1993: in references.bib but never fetched (no references.json record)

For each key: fetch the paper with the aii-semscholar-bib script (`--out ./references.bib`, which also records it in ./references.json) and cite it by the key the script prints, or remove the citation. Never write a paper's BibTeX entry or edit references.json by hand, and do not use \nocite{*}. A key that is not a paper (a model card, a software repository, a dataset) may instead be a hand-written @misc entry with howpublished = {\url{<URL>}} (or url =) and note = {Accessed <date>} (or urldate =), its URL no arXiv or DOI address. Then delete paper.bbl and paper.aux and re-run pdflatex, bibtex, pdflatex, pdflatex.
```

### [5] SYSTEM-USER prompt · 2026-11-20 02:54:16 UTC

```
TERMINOLOGY CHECK FAILED: 2 naming issue(s) in paper.tex.

A reader finds this paper by searching for the field's words. A private label costs it those readers, and a bare run-internal code costs the sentence its meaning:
- Bare label codes in the body text: IF97. These are the run's own internal row labels, meaningless to a reader. Name each condition, metric or variant the way the field names it, and keep the codes in the tables only.
- Undefined coinages (16): Band-mean, Below-sea-level, Clausius-Clapeyron, IAPWS-at-ISA, altitude-to-pressure, atmosphere-model, band-level, boiling-temperature, constant-enthalpy, four-model, pre-registered, re-derivation. None of these appears in the field's own vocabulary or in any cited title, and none is defined within a sentence of its use. Use the field's existing name, or define the term explicitly on first use and keep the same words afterwards.

For each one, exactly one of these applies:
1. The field already names this — use <domain_vocabulary>'s spelling everywhere
2. It is genuinely new — define it once at first use ('we call X ...', 'we define X as ...') and keep the wording identical afterwards
3. It is a bare code in a sentence — replace it with the name of the thing it stands for; codes stay in table headers only

Change nothing else: numbers, claims, citations and figures stay as they are. Then recompile the PDF.
```

### [6] SYSTEM-USER prompt · 2026-11-20 02:57:20 UTC

```
TERMINOLOGY CHECK FAILED: 2 naming issue(s) in paper.tex.

A reader finds this paper by searching for the field's words. A private label costs it those readers, and a bare run-internal code costs the sentence its meaning:
- Bare label codes in the body text: IF97. These are the run's own internal row labels, meaningless to a reader. Name each condition, metric or variant the way the field names it, and keep the codes in the tables only.
- Undefined coinages (7): Clausius-Clapeyron, atmospheric-model, constant-enthalpy, root-finding, sea-level, standard-atmosphere, three-sample. None of these appears in the field's own vocabulary or in any cited title, and none is defined within a sentence of its use. Use the field's existing name, or define the term explicitly on first use and keep the same words afterwards.

For each one, exactly one of these applies:
1. The field already names this — use <domain_vocabulary>'s spelling everywhere
2. It is genuinely new — define it once at first use ('we call X ...', 'we define X as ...') and keep the wording identical afterwards
3. It is a bare code in a sentence — replace it with the name of the thing it stands for; codes stay in table headers only

Change nothing else: numbers, claims, citations and figures stay as they are. Then recompile the PDF.
```

### [7] SYSTEM-USER prompt · 2026-11-20 02:58:21 UTC

```
TERMINOLOGY CHECK FAILED: 2 naming issue(s) in paper.tex.

A reader finds this paper by searching for the field's words. A private label costs it those readers, and a bare run-internal code costs the sentence its meaning:
- Bare label codes in the body text: IF97. These are the run's own internal row labels, meaningless to a reader. Name each condition, metric or variant the way the field names it, and keep the codes in the tables only.
- Undefined coinages (2): Clausius-Clapeyron, root-finding. None of these appears in the field's own vocabulary or in any cited title, and none is defined within a sentence of its use. Use the field's existing name, or define the term explicitly on first use and keep the same words afterwards.

For each one, exactly one of these applies:
1. The field already names this — use <domain_vocabulary>'s spelling everywhere
2. It is genuinely new — define it once at first use ('we call X ...', 'we define X as ...') and keep the wording identical afterwards
3. It is a bare code in a sentence — replace it with the name of the thing it stands for; codes stay in table headers only

Change nothing else: numbers, claims, citations and figures stay as they are. Then recompile the PDF.
```

### [8] HUMAN-USER prompt · 2026-11-20 03:28:33 UTC

````
<research_methodology>
Write like an experienced academic. Reviewers judge both the science and the writing.

- Claims must be proportional to evidence. Choose verbs carefully — "demonstrate," "observe," and "hypothesize" mean different things.
- Every result needs: what was measured, on what data, the numbers, and what they mean.
- Methodology must be specific enough to reproduce. Section placement follows <paper_structure> below.
- State limitations honestly. Avoid both overclaiming and excessive hedging.
</research_methodology>

<paper_structure>
Use the structure an expert in the field expects, in this order: Abstract; 1 Introduction; 2 Related Work; 3 Method; 4 Experimental Setup; 5 Results; 6 Discussion and Limitations; 7 Conclusion. Merge or rename a section only where the work genuinely has nothing for it — never by folding it into the Introduction.

- The Introduction contains ONLY: the problem and why it matters, the gap in existing work, the idea in one or two sentences, a contributions list carrying the headline numbers, a one-sentence pointer to the Figure 1 overview at its end, and a one-sentence roadmap of the paper.
- NO literature survey and NO method details in the Introduction. Prior work goes to Related Work, how the method works goes to Method; the Figure 1 overview shows its shape, and its caption and the Method section explain it.
- Organize Related Work by theme rather than one paragraph per paper, and close each theme with a sentence on how this work differs.
- Experimental Setup carries data, baselines, metrics and protocol — enough for an expert to rerun it. Results carries findings, not setup.
</paper_structure>

<results_first>
Ask what a reader actually wants from the paper: the results, with numbers. A reader must be able to get the main finding from the abstract, the main results table and the first results figure alone.

- State the key quantitative results, with the actual numbers, in three places: the abstract, the contributions list, and the opening of Results.
- Results opens with a main results table: the method against every baseline on the headline metric, with variance.
- Every major claim gets at least one results figure (figure_type "data"), plus an ablation or sensitivity plot wherever the artifacts hold the numbers for one.
- Past the Figure 1 overview, prefer a plot of real numbers over concept art — keep further concept figures to the pipeline diagram the method genuinely needs.
- Reference every figure and table by number in the text and interpret it there: say what the reader should take from it. Never drop one in unexplained.
</results_first>

<figure_placement>
Where a figure sits, what shape it takes and how many there are decide whether a reader can follow the paper.

- Put each [FIGURE:id] marker directly after the paragraph that first discusses the figure, inside the section that owns it: the Figure 1 overview and then the headline data figure at the end of the Introduction, method and pipeline diagrams in Method, the main comparison and the per-claim results figures in Results, ablation and sensitivity plots in Results or Discussion. Never place a figure in the Abstract, Related Work or Conclusion.
- Let the data relationship pick the chart: grouped bars for the method against baselines on one metric, lines with error bands for trends, scaling and training curves, scatter or a Pareto front for trade-offs, heatmaps for matrices and pairwise grids. A handful of numbers is a table, not a figure. Use multiple panels only when they share axes and one takeaway.
- Aim for roughly four to eight figures in a full paper, with the Figure 1 overview first and the main results figure next. Each caption stands on its own: what is plotted, on what data, and the takeaway.
</figure_placement>

<safeguard_research_reporting>
When the research concerns bypassing or removing a model's safeguards (jailbreaks, refusal
removal, abliteration, safety fine-tuning reversal, or anything whose effect is a model that
refuses less on harmful requests), report the findings as MEASUREMENTS and their implications
for EVALUATION and DEFENCE, never as operational advice for defeating safeguards.
- State what was measured, on what, and how large the effect was, as in any other result.
- Draw the implications for the people who build and test safeguards: what an evaluation misses,
  which defences are brittle and where, what a safety evaluation should measure next.
- Never frame a finding as a recommendation, a recipe or a best configuration for removing
  refusals: no "the practical recommendation is to use X to remove refusals", no "for the
  strongest bypass, edit layers X to Y", no step-by-step settings a reader could follow to make a
  model comply with harmful requests.
- This applies everywhere the finding is stated: abstract, executive summary, key results, best
  result, discussion, conclusion, captions, the website and the interactive page.
</safeguard_research_reporting>

<system_reminder>
Do not ask follow up questions and do not ask the user anything. Execute all steps independently.
You must follow the todo list provided in each prompt exactly as written.
No placeholders, stubs, or incomplete code — all code must be complete and functional.
</system_reminder>

<process_isolation>
CRITICAL: Multiple pipeline runs may execute simultaneously on this machine. `ps aux | grep method.py` matches ALL runs, not just yours.
- NEVER kill processes by name (`killall`, `pkill -f`, `ps aux | grep ... | xargs kill`). This kills OTHER runs' processes.
- NEVER monitor processes by name (`ps aux | grep method.py`). You will see other runs' processes and get confused.
- ALWAYS use PID-based process management:
  Run: `uv run method.py & PID=$!` or `timeout <seconds> uv run method.py & PID=$!`
  Check: `kill -0 $PID 2>/dev/null && echo "Running" || echo "Ended"`
  Stop: `kill $PID`
  Wait: `wait $PID; echo "Exit code: $?"`
  Monitor: `tail -f logs/run.log & TAIL_PID=$!` then `kill $TAIL_PID` when done
</process_isolation>

<flex_environment>
You run in a disposable macOS virtual machine on Apple silicon, one guest of this run on its owner's Mac. The Apple GPU is reached through `mps` in torch and through MLX. CUDA does not exist here, there is no Docker and no Linux binary runs. Run one GPU process at a time; another guest may share the GPU.
Your own machine is the `text`: 4 vCPUs, 8 GB RAM (4 GB of it for the step), no GPU work.
Start every script that uses torch with the device line: `from aii_device import DEVICE, check; check()`; where `aii_device` is not installed, `DEVICE = torch.device("mps" if torch.backends.mps.is_available() else "cpu")`. Read the `aii-use-hardware` skill before planning compute.
Instead of each CUDA habit: vLLM -> mlx-lm or llama-server; FP8 -> bf16 or MLX 8-bit; bitsandbytes -> MLX 4-bit or 8-bit; Triton kernels -> torch ops or an MLX Metal kernel; float64 on the GPU -> the CPU; torch.cuda.* -> aii_device; .cuda() -> .to(DEVICE); "cuda" if torch.cuda.is_available() else "cpu" -> DEVICE (that test silently picks the CPU); flash-attn -> sdpa; several GPUs -> one device; torch.compile -> eager mode.
Known slow spots: LSTMs, small MLPs, ops that fall back to the CPU (warned in the log), the first MPS call's warm-up, and model downloads over a home link; every step fetches its inputs again.
What executor steps get: `text_small`: 2 vCPUs, 4 GB RAM (1 GB of it for the step), no GPU work; `text`: 4 vCPUs, 8 GB RAM (4 GB of it for the step), no GPU work; `gpu`: 6 vCPUs, 24 GB RAM (20 GB of it for the step), 12.8 GiB of GPU memory; `gpu_large`: 8 vCPUs, 64 GB RAM (60 GB of it for the step), 34 GiB of GPU memory. Text agents get `text`; an executor step gets `gpu` unless its plan's `flex_guest_shape` names another shape. `gpu` fits a step within 20 GB of RAM and 12.8 GiB of GPU memory; a step that needs more sets `flex_guest_shape` to `gpu_large`, the largest guest, which fits a step within 60 GB of RAM and 34 GiB of GPU memory. At most one runs at a time on the Mac, so a `gpu_large` step may wait longer for it. `flex_guest_shape` may name any shape listed, smaller ones only for a light step that fits their RAM for the step.
One step's inputs (the run's files plus its sessions) stay under 20 GB: keep large models and datasets out of the run's files.
Use `aii-mkvenv` or a plain `uv venv` for extra packages; never reinstall or upgrade torch.
</flex_environment>

<slot_environment>
You run in the `flex_slot` environment: your own macOS account in one long-lived guest that other agents share at the same time.
Your memory share is 4 GB: going over it stops your job alone. Your disk is 20 GB; keep temp files under $TMPDIR. You have no GPU work. Use ports from $AII_PORT_BASE or port 0.
</slot_environment>

<workspace>
Your workspace: `/Volumes/aii-s20004/work/run_ek8xZiRG71Qn/4_gen_paper_repo/_4_assemble_paper/paper/workspace`

CRITICAL: Every file you create, write, or save MUST be inside this workspace directory (subdirectories OK). You MUST NOT write files anywhere outside this path — external paths are READ-ONLY. Use absolute paths for all file operations.

EVERY file write MUST start with `/Volumes/aii-s20004/work/run_ek8xZiRG71Qn/4_gen_paper_repo/_4_assemble_paper/paper/workspace/`:
GOOD: `/Volumes/aii-s20004/work/run_ek8xZiRG71Qn/4_gen_paper_repo/_4_assemble_paper/paper/workspace/file.py`, `/Volumes/aii-s20004/work/run_ek8xZiRG71Qn/4_gen_paper_repo/_4_assemble_paper/paper/workspace/results/out.json`
BAD: `/tmp/file.py`, `~/output.json`, `./file.py`, any path outside the workspace
</workspace>
<disposable_outputs>
YOUR WORKING DIRECTORY IS A DELIVERABLE. When this module ends it must read
like a GitHub repository someone else can fork, resume and run — and the bulk
it holds must be either worth keeping or restorable. This run shares a storage
volume with the database; a run that fills it stops every other run on the box.

So before you finish, produce TWO files:

1. `.aii/manifest.yaml` — one entry per heavy path, each with EXACTLY ONE decision.
   The `.aii/` directory ALREADY EXISTS in your cwd: write the file into
   it. Do not create, replace or `touch` `.aii` itself — a plain file by
   that name makes the manifest unwritable for the rest of the module.

```yaml
entries:
  - path: results/
    keep: six GPU-hours of sweep output, not reproducible inside this run
  - path: hf_cache/
    delete: redownloadable
    source: "huggingface-cli download meta-llama/Llama-3-8B"
  - path: checkpoints/
    delete: regenerable
    source: "uv run train.py --epochs 3 --seed 0"
```

   - `keep:` takes a ONE-LINE reason. Use it for the expensive and the
     irreproducible: trained weights, long-running results, datasets you
     collected yourself.
   - `delete:` takes `redownloadable` (and a `source:` naming the repo id, URL
     or command) or `regenerable` (and a `source:` that is the command which
     rebuilds it). These are deleted AFTER the round ends, never mid-step.
   - Every path is RELATIVE TO YOUR CWD and must resolve INSIDE it. Absolute
     paths, `..`, and anything resolving outside are rejected.
   - Globs and whole directories are fine. A whole `hf_cache/` is ONE entry —
     do not list files individually.

2. `README.md` — written as if your cwd were a GitHub repository: what you
   did, the layout with a line per important file/directory, how to run it,
   and a **"Restoring removed files"** section giving the install/download
   command for EVERY `delete` entry. An `install.sh` or `restore.sh` beside it
   is welcome.

A CHECKER RUNS WHEN YOU SUBMIT. If anything heavy has no decision it fails
your submission and hands you the uncovered list, grouped by directory with
sizes, and you fix the manifest and submit again.

WHAT NEEDS NO DECISION — do not write entries for these:
- text and code files, at ANY size (source, JSON, CSV, YAML, logs, markdown);
- anything under the auto-keep floor (10 MB), whatever it holds.
Only large binaries and cache directories (`hf_cache/`, `.venv/`,
`node_modules/`, `checkpoints/`, `wandb/`, `__pycache__/`, …) need one.

NEVER mark your results, figures, papers, code, logs or anything a later step
reads as `delete`. If a later step needs it, it is a `keep`.

WHAT A `keep` BUYS YOU. Anything you do not mark `delete` stays exactly where
you wrote it, on this run's storage volume, at the path it already has — it is
not moved, renamed or copied. A later round reads it there, by that absolute
workspace path, so a checkpoint you keep is a checkpoint the next round can
load instead of retraining. It is also the ONLY copy: the publish step pushes
your cwd to GitHub but skips every file of 100 MB or
more, so trained weights and large binary artifacts never leave the volume.
Name each kept artifact in your results and your `README.md` by its path
RELATIVE to your cwd, and say it stays on the run's volume rather than in the
published repository. Never write an absolute server path into a file that is
published: a reader's machine has none of them.
</disposable_outputs>

Please continue from where you stopped.
````

### [9] SYSTEM-USER prompt · 2026-11-20 03:29:18 UTC

```
<task>
Typeset <paper_draft> as LaTeX with BibTeX, insert <available_figures>, and compile it to PDF.
</task>

<tool_use>
Maximize parallel tool calls. Parallelize independent operations, only sequentialize dependencies.
- Multiple searches/fetches on different topics → parallel in one turn
- Search then fetch results → sequential (need URLs first)
</tool_use>

<publishable_paper_rules>
This is the PUBLISHABLE PAPER. The run's internal report ships beside this paper as its own PDF
and already ho... [truncated, 58816 chars total]
```

### [10] HUMAN-USER prompt · 2026-11-20 03:29:18 UTC

```
How well does the simple barometric formula predict the boiling point of water at different altitudes, compared with published measurements?
```

### [11] SKILL-INPUT — aii-paper-to-latex · 2026-11-20 03:29:28 UTC

The agent loaded the **aii-paper-to-latex** skill; its `SKILL.md` (the instructions injected into the agent's context) follows verbatim.

````
---
name: aii-paper-to-latex
description: "Assembles and compiles a LaTeX paper into paper.pdf: preamble (generic; bundled sn-jnl for Springer, BMC, Nature; else the journal's own template fetched at run time), figure floats that includegraphics pre-generated .pdf and .jpg, float-placement and width rules, and the required pdflatex, bibtex, pdflatex, pdflatex sequence. Use whenever pre-written text and figures must become a compiled PDF, and when a build misbehaves — citations printing as ??, figures drifting to the end or above the title, shrunken axis labels, undefined references. Triggers: latex, pdflatex, bibtex, natbib, sn-jnl, journal template, includegraphics, figure float, htbp, compile the paper, paper.tex, paper.pdf. NOT for: writing the text (aii-paper-writing), figure images (aii-data-fig-gen, aii-concept-fig-gen), bibliography entries (aii-semscholar-bib); NOT for reshaping a PDF — merging, splitting, forms, tables (amg-meta-computer-use); NOT for compiling a user's own .tex in Downloads or Documents; that is amg-meta-computer-use."
---

## LaTeX Paper Assembly

Assembles a research paper from paper text, pre-generated figures (vector `.pdf` for data figures, `.jpg` for concept figures) and a bibliography into a compiled PDF.

### Document Setup

Which preamble depends on the research request:

- **No target journal named**: the generic preamble below.
- **A Springer, SpringerOpen, BMC or Nature Portfolio journal named**: that journal's
  official template, see "Target journal: Springer Nature template".
- **Any other publisher's journal named** (Elsevier, IEEE, ACM, Wiley, MDPI, ...): its
  template is not bundled, so download the official one at run time:
  1. Take the class from CTAN when it is there (elsarticle, IEEEtran, acmart, llncs,
     revtex, ...): `https://mirrors.ctan.org/macros/latex/contrib/<name>.zip`, which holds
     the `.cls` (or the `.ins`/`.dtx` to build it with `latex <name>.ins`) and its `.bst`.
     Otherwise use the template download on the journal's author-guidelines page.
  2. Put the `.cls` and `.bst` at the root of the paper directory, next to `paper.tex`, and
     any `.sty` the class loads that `kpsewhich <file>.sty` does not find. Subfolders other
     than `figures/` are dropped when the paper ships.
  3. Use the class options and reference style the journal's guidelines give (e.g.
     `\documentclass[preprint,12pt]{elsarticle}` with `elsarticle-num`), plus the generic
     preamble's packages the class does not already load, and its sections.
  4. Compile with the usual sequence below.

  Only when no official template can be found, or it will not compile, use the generic
  preamble and say in the paper-writing summary that the paper is not in the journal's own
  template.

Generic preamble:

```latex
\documentclass[11pt,letterpaper]{article}
\usepackage{graphicx, geometry, amsmath, hyperref, url, natbib, booktabs, longtable, xcolor, listings}
\geometry{margin=1in}
\hypersetup{colorlinks=true, linkcolor=black, citecolor=black, urlcolor=black}
\renewcommand{\topfraction}{0.9}
\renewcommand{\bottomfraction}{0.8}
\renewcommand{\textfraction}{0.07}
\renewcommand{\floatpagefraction}{0.75}
```

- **One typeface.** Add no font package to this preamble: no mathptmx, times, helvet, courier,
  newtx, newpx, lmodern, palatino or fontspec. Text, maths and captions stay Computer Modern.
  The figures are one family too, the paper's figure style, chosen from its field's top papers:
  CMU Serif like the text, or DejaVu Sans where that field draws sans-serif figures. A paper
  that loaded Times, Helvetica and Courier beside its Computer Modern figures showed three
  typefaces on one page. A journal's own class sets its own fonts.
- **Float fractions.** `\floatpagefraction` is the line that matters for figures: a page of
  floats alone is made only when they fill 75% of it, where LaTeX's default (0.5) left three
  float pages of one paper 35-50% blank. The `!` in every figure's `[!htbp]` already lifts the
  top, bottom and text limits, so the other three lines act only on floats placed without `!`.

### Target journal: Springer Nature template

This skill's own directory holds Springer Nature's official template (December 2024
package) in `templates/springer-nature/`: the class `sn-jnl.cls` and one BibTeX style per
reference style in `bst/`. Its `README.md` records the source and licence.

1. Pick the reference-style option from the journal's submission guidelines ("Preparing your
   manuscript", section References), which name the style and show example references:

   | the guidelines say                        | option           |
   |-------------------------------------------|------------------|
   | Basic Springer (Nature) reference style   | sn-basic         |
   | Math and Physical Sciences, numbered      | sn-mathphys-num  |
   | Math and Physical Sciences, author-year   | sn-mathphys-ay   |
   | American Physical Society (APS)           | sn-aps           |
   | Vancouver / BMC, numbered [1]             | sn-vancouver-num |
   | Vancouver, author-year                    | sn-vancouver-ay  |
   | Nature Portfolio journal                  | sn-nature        |
   | APA or Chicago style                      | not bundled      |

   `sn-basic` cites author-year, as Springer's example references do ("Smith J, Jones M
   (1999) Title. J Abbrev 965:325-329"); add the option `Numbered` only when the journal's
   published articles cite by number. When the guidelines name no style, use `sn-basic`.
   An APA or Chicago journal takes the generic preamble.
   Known journals:

   | journal                 | option   | checked                  |
   |-------------------------|----------|--------------------------|
   | Applied Network Science | sn-basic | guidelines, 2025 article |

   Applied Network Science's guidelines give "Examples of the Basic Springer reference
   style", and its articles cite "(Newman 2010)", so no `Numbered`.
2. Copy `sn-jnl.cls` and the option's `.bst` into the paper directory, next to `paper.tex`.
   The file is `bst/<option>.bst`, except `sn-aps` uses `bst/sn-APS.bst`. Both files are
   part of the paper's sources and ship with it, so the published repo rebuilds.
3. Preamble, with the journal's option:

   ```latex
   \documentclass[pdflatex,sn-basic]{sn-jnl}
   \usepackage{graphicx, amsmath, hyperref, url, booktabs, longtable, xcolor, listings}
   ```

   The class sets the page (A4, its own text block) and loads natbib and hyperref itself,
   and runs `\bibliographystyle` for the option. So no `geometry`, `\geometry`,
   `\hypersetup` or `natbib` options, and NO `\bibliographystyle` line: a second one is a
   BibTeX error ("Illegal, another \bibstyle command", exit status 2) that BibTeX then
   ignores, so it only ever adds an error to the build.
   `sn-nature` and `sn-aps` store no author names for natbib, so `\citet` prints
   "(author?) [2]" there: write the name in the sentence and cite with `\citep`.
4. Front matter, in this order after `\begin{document}`: `\title[<short running
   title>]{<full title>}`; `\author` and `\affil` only for authors the draft names (never
   placeholders); `\abstract{...}` (a command taking the abstract, not the `abstract`
   environment); `\keywords{...}`; then `\maketitle`, which prints all of them.
5. Back matter: `\backmatter`, then the journal's Declarations with each item under
   `\bmhead{<heading>}`, then `\bibliography{references}`.

Everything else in this skill (figures, code links, tables, length, compile sequence) is the
same for both setups.

### Figure Inclusion

CRITICAL: Include ALL figures. Every figure MUST appear in the paper.

```latex
\begin{figure}[!htbp]
  \centering
  \includegraphics[width=\linewidth,height=0.45\textheight,keepaspectratio]{figures/filename.pdf}
  \caption{Descriptive caption.}
  \label{fig:label}
\end{figure}
```

Rules:
- ALWAYS `[!htbp]` — all four options, so a float can never be deferred to the end of the
  document, which `[t]` or `[h]` alone risks. Do not ask for a page TOP: `[!t]` and
  `[!tbp]` both floated a figure ABOVE the paper's own title on page 1, where `[!htbp]`
  on the same document did not. Where a figure lands is decided by where it is declared
  in the text
- Use `figure`, never `figure*`. Both document setups are ONE column, so `figure*` is exactly
  as wide as `figure` (469.76pt generic, 372pt sn-jnl) and gains nothing, while restricting
  the float to a page top
- ALWAYS constrain with `width`, `height=0.45\textheight` and `keepaspectratio`.
  The height cap keeps a single plot under half a page, so it shares its page
  with text instead of standing alone on a half-empty float page. Figures are
  drawn at the 6.5 in text width, so a 16:9 or wider figure (3.7 in tall) is
  limited by its width and prints at 100%, and a 4:3 plot at 83%. A cap that
  binds harder shrinks the TEXT with the image: at `0.4\textheight` a square
  figure printed at 50.9%, putting 11 pt axis labels on the page at 5.6 pt,
  under the 7 pt minimum. So a 1:1 or taller plot is re-plotted at 16:9 or 4:3,
  never left for LaTeX to shrink. The figure generator measures legibility at
  the figure's OWN size, so it cannot see this happen
- Every figure needs `\caption`, `\label`, and a `\ref` in the text
- Do NOT convert figures to tables or describe them without inserting the image
- Do NOT skip any figures
- Never crop or trim with LaTeX options (`trim`, `clip`, `viewport`). Blank margins are cropped in
  code, in the file itself (PIL bounding box of non-white pixels), by the step that makes the figure,
  so the PDF, the repo and the website all show the same file

### Code links and footnotes

- No code link after each claim. The code is linked ONCE in the body, by a code-availability
  statement (`... are in the paper's code repository~\href{<repo URL>}{[code]}, and
  Appendix~\ref{app:code} links each result to the folder that produced it.`), and result by
  result in the last appendix section, `\section{Code for each result}\label{app:code}`: a
  `longtable` of Section | Result | Code folder, the Section cell `\S\ref{<label>}`, the Result
  cell naming the result and its figure or table, the Code folder cell
  `\href{<URL>}{\texttt{round-2/experiment-11}}`. Every Results subsection has a `\label` and a
  row. The finish check holds the table to the draft's code links and the run's code folders
- Never a footnote carrying a code URL: one paper's 33 code footnotes, each a 150-character URL
  broken mid-word, filled the foot of 12 pages
- Every URL is copied verbatim into its `\href`
- Any other URL (a model card, a dataset, another group's repository) goes in a footnote,
  `\footnote{\url{...}}`, or in its bibliography entry, never inline in a sentence, where it runs
  into the margin. A code link, or any URL over 70 characters, in a footnote sends the paper back
- A footnote mark goes after the sentence's closing punctuation, never directly after a digit or
  another mark: "IRR 1.19)123" reads as one number

### Tables

- At most 7 columns. Split a wider table in two, or transpose it so the many items are rows; an
  11-column table of narrow wrapping cells with 3-line headers is unreadable
- A table whose cells are sentences goes in the appendix
- Never shrink a table with `\resizebox`

### Length

The body, everything before the References heading, is at most 12 pages and about 7,000 words,
figures and tables included. Per-round detail, secondary analyses, full per-condition results and
text tables go in an appendix: `\clearpage` and `\appendix` after `\bibliography{references}`,
so the appendix starts on its own page, then `\section` headings, which is not counted. Measure the compiled PDF, not the source: `pdfinfo paper.pdf` for
the pages and `pdftotext paper.pdf - | wc -w` for the words. That count includes the text inside
vector figures (axis labels, ticks, legends) and tables, so the prose alone runs somewhat under
7,000.

### Compilation Process

Run each command separately (do NOT chain with `&&` — pdflatex often exits non-zero on warnings, which would skip bibtex and leave citations as `??`):

```bash
pdflatex -interaction=nonstopmode paper.tex
bibtex paper
pdflatex -interaction=nonstopmode paper.tex
pdflatex -interaction=nonstopmode paper.tex
```

On a Mac whose shell did not run `path_helper`, `pdflatex: command not found` means MacTeX is
off PATH, not missing: `export PATH="$PATH:/Library/TeX/texbin"` first.

All four commands are required. Skipping bibtex causes `??` in all citations.
Fix any errors between runs. Verify `./paper.pdf` was created.

After ANY change to `references.bib`, delete `paper.bbl` and `paper.aux` first and rerun all four:
a stale `.bbl` keeps printing the old entries. Then read the PRINTED reference list in the PDF, not
the `.bib`: no journal article printed as "In <Journal>, volume ...", no `??`, every name, year and
venue as its Crossref record has it.

### Output Files

- `./paper.tex` — LaTeX source
- `./references.bib` — bibliography file
- `./sn-jnl.cls` and `./<option>.bst` — only with a Springer Nature target journal; they ship
  with the paper's sources
- `./paper.pdf` — compiled PDF
- `./figures/` — all figure images (pre-generated, copied into workspace). Data
  figures are `.pdf` (vector — LaTeX renders their text at page resolution, which
  is what keeps axis labels sharp in print); concept figures are `.jpg`. Use each
  file's OWN extension in `\includegraphics`; there is no conversion step.
````

### [12] SKILL-INPUT — aii-paper-writing · 2026-11-20 03:29:28 UTC

The agent loaded the **aii-paper-writing** skill; its `SKILL.md` (the instructions injected into the agent's context) follows verbatim.

````
---
name: aii-paper-writing
description: "Writes the PROSE of an AI research paper: abstract, introduction, related work, methods, experiments, discussion and conclusion, with a page budget, the 5-paragraph intro pattern, writing-quality rules, inline [FIGURE:fig_id] markers plus a structured figures array, and a MANDATORY REVISION_CHECKLIST.md pass over every finished draft. Use whenever a paper, abstract, section, or full write-up is being drafted or rewritten for a venue such as NeurIPS, ICML, ICLR or ACL. Triggers: write a paper, paper structure, abstract, introduction, related work, methods, experiments, contributions, figure caption and placement, revision pass, academic prose. NOT for: assembling or compiling .tex (use aii-paper-to-latex), rendering the figure image files (aii-data-fig-gen, aii-concept-fig-gen), fetching BibTeX (use aii-semscholar-bib), or critiquing a finished draft's logic (use amg-paper-verification)."
---

## MANDATORY: the final revision pass

**`REVISION_CHECKLIST.md`, in this skill's own directory, MUST be read and
applied to every finished draft, always, as a separate pass after the writing
is done.** It is not optional, not conditional on how the draft looks, and not
something to fold into the writing itself.

Writing and revising are different jobs and cannot be done in one pass. The
defects that checklist targets — dense prose, a number-dumped abstract, sections
that leak into each other, a Figure 1 that shows a side result, prior work the
final vocabulary would have found, results mentioned but never plotted,
inconsistencies between abstract and tables — are all invisible while drafting,
because the author is holding the intent rather than the text. Every one of them
is obvious to the first outside reader. Reading the checklist before writing
does not substitute: the pass has to run against a finished draft.

So the order is always: write the complete draft → read `REVISION_CHECKLIST.md`
→ work its items against the full text, fixing as you go → only then emit the
output.

## Technical Papers

Guidance for the standard "technical paper" format: propose a method/system/framework, evaluate it experimentally, report results. This is the main track at most CS venues (NeurIPS, ICML, ICLR, ACL, AAAI, etc.). Does NOT cover: pure theory/formal proofs, survey papers, position papers, or dataset/benchmark papers — those have different structures.

### Paper Structure

Target 6-8 pages, and never more than a body of 12 pages and about 7,000 words: the body runs
from the abstract to the end of the Conclusion, figures and tables included. Per-round detail,
secondary analyses, full per-condition results and text tables go in an Appendix after the
references, which does not count. The pipeline measures the compiled PDF and sends a longer body
back; one run with no limit printed 26 pages and 14.2k words. The Appendix describes every task
and dataset the results rest on: what the model is given, what output counts as correct, how
correctness is scored, and one example prompt verbatim. Use formal academic language, third
person. Support claims with evidence from artifacts.

#### Rough Page Budget (8-page paper)

| Section | Pages | Notes |
|---|---|---|
| Abstract | 0.3 | Problem, approach, key result |
| Introduction | 1.0-1.5 | The most important section |
| Related Work | 0.5-1.0 | Beginning or end (see below) |
| Methods | 1.5-2.0 | Architecture fig on page 1 |
| Experiments | 1.5-2.0 | Setup + results + ablations |
| Discussion | 0.5-1.0 | Limitations go here |
| Conclusion | 0.3-0.5 | Do not repeat the abstract |
| References | 0.5-1.0 | Not counted in page limit |
| Appendix | any | After the references; not counted |

**Critical rule**: A clear new technical contribution must be articulated by page 3 (quarter of the paper). If the reader doesn't know what you did by then, you've lost them.

#### Section Details

**Abstract** (150-250 words): State the problem, your approach, and the main results. Be factual and comprehensive. Do not repeat the abstract word-for-word later in the paper.

**Introduction** — Follow this 5-paragraph structure:

1. **What is the problem?** Define the task concretely.
2. **Why is it interesting and important?** Real-world impact, scale.
3. **Why is it hard?** Why do naive approaches fail?
4. **Why hasn't it been solved before?** What's wrong with prior solutions? How does yours differ?
5. **What are the key components of your approach and results?** Include specific limitations.

End with a "Summary of Contributions" subsection — bullet list of contributions with section references. This doubles as an outline, saving space.

**Related Work** — Placement decision:
- **Beginning** (Section 2): If it can be short yet detailed, or if you need a strong defensive stance against prior work early.
- **End** (before Conclusions): If comparisons require your technical content, or if it can be summarized briefly in the Introduction. Can be titled "Discussion and Related Work."

**Methods/Approach**: Every section tells a story — the story of the results, NOT the story of how you arrived at them. Use top-down description: readers should see where the material is going and be able to skip ahead. Move gory details to the Appendix.

**Experiments**: Setup (datasets, metrics, baselines) → main results → ablations → analysis. Every claim needs quantitative evidence.

**Discussion**: Interpret results, compare to prior work, state limitations honestly. Limitations should be specific and actionable, not vague disclaimers.

**Conclusion**: Short summarizing paragraph. Do NOT repeat material from the Abstract or Introduction. Make original claims more concrete (e.g., reference quantitative results). Include future work as bullet list — if actively pursuing follow-up, say so to mark territory.

#### Writing Quality Rules

- Define all notation/terminology before use, only once. Group global definitions in Preliminaries.
- Do NOT use nonreferential "this", "that", "these", "it". Always specify the referent. BAD: "This is important because..." GOOD: "This accuracy gap is important because..."
- Do NOT use "etc." unless remaining items are completely obvious. BAD: "We measure volatility, scalability, etc." GOOD: "We measure volatility and scalability."
- Do NOT write "for various reasons" — state the actual reasons.
- "That" is defining, "which" is nondefining. "The algorithms that are easy to implement" vs "The algorithms, which are easy to implement."
- Use italics for definitions and quotes, not for emphasis. Context alone should provide emphasis.

### Figure Format

Figures use a hybrid marker + structured array approach. ALL figures are generated by a separate pipeline step using an AI image model — your `image_gen_detailed_description` is the ONLY input that model sees. It cannot read files or access data. Do NOT generate actual image files yourself (no matplotlib, no PIL, no image generation scripts).

**In paper_text**: Place `[FIGURE:fig_id]` markers where figures should appear.

**In figures array**: Provide full specs as structured objects with these fields:
- `id` — matches the `[FIGURE:id]` marker in paper_text
- `title` — short descriptive title
- `caption` — LaTeX caption that appears below the figure in the paper: at most about 60 words, the takeaway in one sentence plus only the encodings the axes do not show; other detail goes in the text. The image carries no title of its own
- `image_gen_detailed_description` — what the renderer draws: for a data figure the axes, ALL values and colours; for a concept figure the layout, each panel's and object's place, colour and title, and the exact text, tokens and numbers it shows. Never a typeface: the renderers set the paper's one family
- `summary` — brief summary of what the figure communicates

Example in paper_text:
```
...our method achieves state-of-the-art results as shown below.

[FIGURE:fig_1]

The results in Figure 1 demonstrate...
```

Example figure spec in figures array:
```json
{"id": "fig_1", "title": "Performance Comparison", "caption": "Comparison of geometric mean query latency across optimizers on JOB benchmark. RLQOpt achieves 2.3x speedup over PostgreSQL.", "image_gen_detailed_description": "Grouped bar chart. X-axis: model names. Y-axis: accuracy (0.0-1.0). Values: ModelA=0.847, ModelB=0.762, Baseline=0.531. Error bars with std: 0.02, 0.03, 0.05.", "summary": "Compares accuracy of proposed methods vs baseline."}
```

Every marker in text MUST have a matching figure in the array, and vice versa.

#### Data Precision Requirement

`image_gen_detailed_description` MUST include exact numbers from artifact output files. Read the actual output files before writing figure specs.

- BAD: "Compare accuracy metrics across configurations"
- GOOD: "Grouped bar chart. X-axis: model names. Y-axis: accuracy (0.0-1.0). Values: K=3: 0.765, K=5: 0.729, Baseline: 0.121."

#### Figure vs Table Decision

Do NOT create figures for tabular data (rows/columns of text or numbers). Use `\begin{table}` in LaTeX instead. Figures are for actual visualizations only (charts, plots, diagrams).

A table has at most 7 columns: split a wider one, or transpose it so the many items are rows. A table whose cells are sentences goes in the Appendix.

#### Concept figures look like the field's Figure 1s and read at print size

Every concept figure (drawn, no dataset behind it) is 16:9, never wider than 2:1, in 2 to 4
lettered panels read left to right, each titled with what it shows. It looks like the Figure 1 of
a top recent paper in the field, which the draft finds and looks at first
(`.claude/skills/aii-concept-fig-gen/scripts/fig1_exemplars.py` fetches their Figure 1 pages) and names
at the end of the Figure 1 spec as "Style references: arXiv <id>, <id>.". That means the field's
own objects on one real worked example (a real prompt, the decisive tokens, a one-line code
snippet, a layer stack, a small result thumbnail), about 80 to 120 words inside the image, the
headline number among a few real numbers, labels of at most about 8 words, colours that each mean
one thing, and no slogan panels (a title over a generic icon or a lone word). Short plain notation
(pass@k, T = 0.8) is fine; a display equation stays in the text. The draft prompt's worked example
shows the scale. A paragraph, a formula or 13 element groups in one image still prints as an
unreadable strip, and four slogan titles over a thermometer and a question mark print legibly
and say nothing.

#### One colour map per paper

A method, condition or model has the same colour in every figure that shows it. Choose the
colours once and name the same one in every spec.

#### Figure Placement Strategy

Be intentional with figure ordering. Figure 1 is the method/idea overview: a concept figure explaining the proposed approach, marked at the end of the Introduction, with the headline data figure right after it as Figure 2, so readers can immediately orient themselves. Only a paper with no method or idea to draw opens with its data figure. Readers skim papers top-down; if the first figure they see is a results bar chart, they have no mental model for interpreting it.

Recommended ordering:
1. **Method/idea overview (Figure 1)** — end of the Introduction, then the headline data figure (so readers understand the approach before diving into details)
2. **Conceptual/analogy figures** — Introduction or Methods (to build intuition)
3. **Results figures** (bar charts, line plots, scatter plots) — Results section
4. **Analysis/ablation figures** — Discussion or later Results

#### Guidelines

- Plan 3-6 figures total across the paper
- Place [FIGURE:fig_id] markers INLINE where referenced in text
- Include axes, labels, ALL numeric values in figure descriptions
- Both data-driven figures (bar charts, line plots) and conceptual diagrams (architecture, flowcharts)
- Data figures: be as detailed as possible: all data values, axis labels, ranges, legend entries and colours. The renderer cannot read files
- Concept figures: detailed about layout, exact about text: where each panel and object sits, its colour, its title, and the exact text, tokens and numbers it shows, never a sentence the image would have to spell out

### Bibliography with Semantic Scholar

Build `./references.bib` using the aii-semscholar-bib skill (real BibTeX from Semantic Scholar):

1. Collect DOIs, ArXiv IDs, or titles for all papers you need to cite
2. Run the `aii_semscholar_bib__fetch` script with the full list in one batch and
   `--out ./references.bib`: it writes `./references.bib` and the fetch record `./references.json`
3. Cite each paper by the key the script printed

Rules:
- Papers enter `./references.bib` ONLY through the fetch script — never write a paper's BibTeX by hand
- A source that is not a paper and has no record to fetch (a model card, a software repository, a
  dataset) may be a hand-written `@misc` entry with its URL and access date, as the
  aii-semscholar-bib skill shows
- Cite each paper's published version, and check each entry against its Crossref record as the
  aii-semscholar-bib skill describes
- If a paper still isn't found after the skill's fallback procedure, do not cite it
- Use `\bibliography{references}` and `\bibliographystyle{plainnat}`
- Do NOT use inline `thebibliography` environment

### Citation Format (for Research Artifacts)

When writing research with numbered citations:

1. Every factual claim MUST have a numbered citation: `[1]`, `[2]`, `[1, 3]`, etc.
2. Each source in the "sources" array MUST have an "index" field
3. The index MUST EXACTLY MATCH citation numbers in the text
4. NEVER cite a number without a matching source index
5. Example: "LLMs show 40% improvement with multi-agent collaboration [1]."
````

### [13] SKILL-INPUT — aii-semscholar-bib · 2026-11-20 03:29:28 UTC

The agent loaded the **aii-semscholar-bib** skill; its `SKILL.md` (the instructions injected into the agent's context) follows verbatim.

````
---
name: aii-semscholar-bib
description: "Fetches real BibTeX entries in one batch from Semantic Scholar by DOI, ArXiv ID or title via aii_semscholar_bib__fetch, normalises citation keys to AuthorYYYY, injects DOIs, and merges the result into references.bib while recording each entry in references.json beside it; a paper it cannot fetch is not cited. ALWAYS use whenever a bibliography, reference list or .bib file is being built or extended, and whenever a citation needs a verified entry instead of an invented one — never hand-write BibTeX. Triggers: bibliography, references.bib, bibtex, citation key, DOI, arXiv id, Semantic Scholar, reference list, cite these papers, natbib entries. NOT for: writing the text around the citations (use aii-paper-writing), running bibtex and compiling (use aii-paper-to-latex), judging whether cited work supports the claims (use amg-paper-verification), or open-ended literature search and PDF mining (use aii-web-tools)."
---

## Tool: `aii_semscholar_bib__fetch`

Batch-fetch BibTeX entries from Semantic Scholar (OpenAlex, then Crossref, when S2 is rate-limited or down). Pass all references in a single call — the tool handles batching internally.

### How it works

1. **DOI/ArXiv refs** → batched into POST /paper/batch calls (up to 500 per API call, auto-chunked)
2. **Title-only refs** → individual GET /paper/search/match (1s delay between)
3. **Fallback when S2 is down** → if S2 still answers 429 (its shared anonymous pool saturates for every caller) or 5xx after its bounded retries, or cannot be reached, S2 is skipped for the rest of the call, and for the next 10-15 min in every call (then one probe decides whether it is back); every ref it did not answer resolves through **OpenAlex**, then **Crossref** (both keyless; set `AII_POLITE_CONTACT` for their higher-limit polite pool). DOI/arXiv hits must agree with the ref's title or first author, so a mislinked record is dropped rather than cited; title hits need a near-exact title. The BibTeX has the same layout, keys and fields as S2's, so `references.bib` cannot tell them apart; each entry's `source` (`semantic_scholar`, `openalex` or `crossref`) says which API answered.
4. **Post-process** → entry type, venue and year from the DOI's Crossref record (a preprint DOI Crossref links to its published version is cited as that version; S2's publication type decides when Crossref has no record), family names braced (`{De Domenico}`, `{DerSimonian}`); normalise fields so the entry renders cleanly (more than 10 authors keep 5 plus "and others", printed "et al."; S2's mangled accents like `Ram'e` restored; straight quotes as LaTeX quotes; arXiv records as `journal = {arXiv preprint arXiv:<id>}`, never `volume = {abs/<id>}`); fix citation key (AuthorYYYY, accents folded); inject DOI

The ability server runs a single worker (`max_threads: 1`). Multiple concurrent tool calls are queued — each runs independently (no cross-request aggregation). Batching happens within each request.

### Input format

```json
{
  "references": [
    {"doi": "10.48550/arXiv.1706.03762", "author": "Vaswani", "year": 2017},
    {"arxiv": "2201.11903", "author": "Wei", "year": 2022},
    {"title": "Tree of Thoughts", "author": "Yao", "year": 2023}
  ]
}
```

Each reference object can have:
- `doi` — DOI string (ArXiv DOIs like `10.48550/arXiv.XXXX.XXXXX` auto-convert to ArXiv IDs)
- `arxiv` — ArXiv ID (e.g. `"2305.14325"`)
- `title` — Paper title (used for search/match when no DOI/ArXiv)
- `author` — First author last name (for cleaner citation key)
- `year` — Publication year (int, for citation key)

At least one of `doi`, `arxiv`, or `title` is required per reference.

### Output format

```json
{
  "success": true,
  "bib_text": "@inproceedings{Vaswani2017, ...}\n\n@article{Wei2022, ...}",
  "total": 3,
  "found": 3,
  "failed_count": 0,
  "entries": [{"citation_key": "Vaswani2017", "bibtex": "...", "title": "...", "doi": "...", "arxiv": "", "source": "semantic_scholar"}],
  "failed": []
}
```

Called as a tool (or through `--json`), it returns these entries and writes no file. A bibliography
is built only through the CLI's `--out`, which also writes the record.

### Workflow

1. Collect DOIs, ArXiv IDs, or titles for all papers you need to cite
2. Run the CLI below with the full list in **one call** and `--out ./references.bib`
3. The script merges the fetched entries into `references.bib` (created if absent) and writes a
   record of each one to `references.json` beside it: source database, S2 paperId / DOI / arXiv id,
   title, first author, year. Later calls with `--out` append to both files and keep them in sync;
   a second paper under a key already taken gets a letter suffix (`Smith2020a`), which the output
   lists — cite the key it prints.
4. Check the failed list — for any missed papers, follow the **fallback procedure** below

`references.bib` and `references.json` are written ONLY by this script for papers. Never write or
paste a paper's BibTeX entry by hand, and never edit `references.json`: the paper step checks every
`\cite` key against `references.bib` and every entry's title and first author against its record,
and a paper entry the script did not write blocks the paper from being published.

The one exception is a source that is NOT a paper and has no record to fetch: a model card, a
software repository, a dataset. Append it to `references.bib` by hand as `@misc`, with its URL and
the date you accessed it:

```bibtex
@misc{Qwen2024,
  author = {{Qwen}},
  title = {Model card of {Qwen}'s {32B} instruction-tuned code model},
  howpublished = {\url{https://huggingface.co/Qwen/Qwen2.5-Coder-32B-Instruct}},
  note = {Hugging Face model Qwen2.5-Coder-32B-Instruct, accessed 27 October 2026},
  year = {2024}
}
```

`url = {...}` and `urldate = {...}` fields are accepted too. Anything with an arXiv, DOI or other
paper URL is a paper and must be fetched.

### Check every fetched entry against its published record (MANDATORY)

The script's entries are raw material, not proof. Reviewers rejected papers whose journal articles
printed as "In Science, volume ...", whose years were a preprint's, and whose particles dropped.

- **Cite the published version.** When a paper has a journal or proceedings version, fetch it by
  that DOI, never by its arXiv or preprint DOI. Look it up on Crossref by title
  (`curl -s "https://api.crossref.org/works?query.bibliographic=<title>&rows=3"`).
- **Compare each entry with its Crossref record** (`curl -s https://api.crossref.org/works/<DOI>`)
  and correct it in `references.bib` to match: entry type (a journal article is `@article` with
  `journal=` and no `booktitle=`), year, authors (every name, spelled and ordered as Crossref has
  them; the script's "and others" past five may stay), venue name and volume.
- **Brace-protect** particles and capitals BibTeX would mangle: `{De Domenico}` (else it prints
  "Domenico"), `{DerSimonian}`, `From {L}ouvain to {L}eiden`.
- Those are the only edits allowed. The title's words stay as fetched, bar a stray character such
  as the footnote digit in "good ideas1", and so does the first author.
  An entry whose title or first author is wrong is re-fetched by its correct DOI, and every
  `\cite` of it moves to the key the script prints.
- After compiling, check the PRINTED reference list in the PDF (see aii-paper-to-latex), not only
  the `.bib`.

### Fallback for failed references (MANDATORY)

NEVER fabricate BibTeX. For each failed reference:
1. **WebSearch** for `"Title" author year` (try `site:arxiv.org` too)
2. **WebFetch** the paper page → extract its DOI or ArXiv ID and exact title
3. Retry the script with that DOI / ArXiv ID / exact title (same `--out`)
4. Still not found → the paper is not cited. Remove the citation (and any claim that rests only on
   it); there is no hand-written fallback for a paper (only for a non-paper source, above).

---

### CLI (how to build a bibliography)

```bash
SKILL_DIR="$(realpath "$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-semscholar-bib")" && \
$SKILL_DIR/../.ability_client_venv/bin/python $SKILL_DIR/scripts/aii_semscholar_bib__fetch.py --out ./references.bib --refs '[
  {"doi": "10.48550/arXiv.1706.03762", "author": "Vaswani", "year": 2017},
  {"arxiv": "2201.11903", "author": "Wei", "year": 2022},
  {"title": "Tree of Thoughts", "author": "Yao", "year": 2023}
]'
```

`--out, -o PATH` — merge the entries into PATH and record them in `references.json` beside it (always use it for a bibliography)
`--json, -j` — output raw JSON instead of .bib text

**If the script fails** with a connection error (ability server not running): create a local `.venv`, install server deps from `server_requirements.txt` into it, then run the script with that `.venv`'s python (it falls back to the local core when the server is unreachable), `--out` included — bypassing the server:
```bash
uv venv .venv --python=3.12 && uv pip install --python=.venv/bin/python -r "$SKILL_DIR/scripts/server_requirements.txt"
```

**If it fails with `No module named 'requests'`** (the shared venv is missing or Python resolved
`..` through a symlink; `realpath` above prevents the latter), skip the venv and run the same
command through uv, `--out` and `--refs` unchanged:
```bash
uv run --no-project --python 3.12 --with-requirements "$SKILL_DIR/scripts/server_requirements.txt" python "$SKILL_DIR/scripts/aii_semscholar_bib__fetch.py" --out ./references.bib --refs '[{"arxiv": "1706.03762", "author": "Vaswani", "year": 2017}]'
```
````

### [14] SYSTEM-USER prompt · 2026-11-20 03:30:28 UTC

```
[Image: original 3840x2149, displayed at 2000x1119. Multiply coordinates by 1.92 to map to original image.]
```

### [15] SYSTEM-USER prompt · 2026-11-20 03:34:17 UTC

```
REFERENCE CHECK FAILED: 1 citation key(s) in paper.tex are not backed by a fetched reference:
- ICAO1993: in references.bib but never fetched (no references.json record)

For each key: fetch the paper with the aii-semscholar-bib script (`--out ./references.bib`, which also records it in ./references.json) and cite it by the key the script prints, or remove the citation. Never write a paper's BibTeX entry or edit references.json by hand, and do not use \nocite{*}. A key that is not a paper (a model card, a software repository, a dataset) may instead be a hand-written @misc entry with howpublished = {\url{<URL>}} (or url =) and note = {Accessed <date>} (or urldate =), its URL no arXiv or DOI address. Then delete paper.bbl and paper.aux and re-run pdflatex, bibtex, pdflatex, pdflatex.
```

### [16] SYSTEM-USER prompt · 2026-11-20 03:35:09 UTC

```
TERMINOLOGY CHECK FAILED: 2 naming issue(s) in paper.tex.

A reader finds this paper by searching for the field's words. A private label costs it those readers, and a bare run-internal code costs the sentence its meaning:
- Bare label codes in the body text: IF97. These are the run's own internal row labels, meaningless to a reader. Name each condition, metric or variant the way the field names it, and keep the codes in the tables only.
- Undefined coinages (16): Band-mean, Below-sea-level, Clausius-Clapeyron, IAPWS-at-ISA, altitude-to-pressure, atmosphere-model, band-level, boiling-temperature, constant-enthalpy, four-model, pre-registered, re-derivation. None of these appears in the field's own vocabulary or in any cited title, and none is defined within a sentence of its use. Use the field's existing name, or define the term explicitly on first use and keep the same words afterwards.

For each one, exactly one of these applies:
1. The field already names this — use <domain_vocabulary>'s spelling everywhere
2. It is genuinely new — define it once at first use ('we call X ...', 'we define X as ...') and keep the wording identical afterwards
3. It is a bare code in a sentence — replace it with the name of the thing it stands for; codes stay in table headers only

Change nothing else: numbers, claims, citations and figures stay as they are. Then recompile the PDF.
```

### [17] SYSTEM-USER prompt · 2026-11-20 03:37:07 UTC

```
REFERENCE CHECK FAILED: 1 citation key(s) in paper.tex are not backed by a fetched reference:
- ICAO1993: in references.bib but never fetched (no references.json record)

For each key: fetch the paper with the aii-semscholar-bib script (`--out ./references.bib`, which also records it in ./references.json) and cite it by the key the script prints, or remove the citation. Never write a paper's BibTeX entry or edit references.json by hand, and do not use \nocite{*}. A key that is not a paper (a model card, a software repository, a dataset) may instead be a hand-written @misc entry with howpublished = {\url{<URL>}} (or url =) and note = {Accessed <date>} (or urldate =), its URL no arXiv or DOI address. Then delete paper.bbl and paper.aux and re-run pdflatex, bibtex, pdflatex, pdflatex.
```

### [18] SYSTEM-USER prompt · 2026-11-20 03:37:41 UTC

```
TERMINOLOGY CHECK FAILED: 2 naming issue(s) in paper.tex.

A reader finds this paper by searching for the field's words. A private label costs it those readers, and a bare run-internal code costs the sentence its meaning:
- Bare label codes in the body text: IF97. These are the run's own internal row labels, meaningless to a reader. Name each condition, metric or variant the way the field names it, and keep the codes in the tables only.
- Undefined coinages (7): Clausius-Clapeyron, constant-enthalpy, pressure-from-altitude, root-finding, sea-level, standard-atmosphere, three-sample. None of these appears in the field's own vocabulary or in any cited title, and none is defined within a sentence of its use. Use the field's existing name, or define the term explicitly on first use and keep the same words afterwards.

For each one, exactly one of these applies:
1. The field already names this — use <domain_vocabulary>'s spelling everywhere
2. It is genuinely new — define it once at first use ('we call X ...', 'we define X as ...') and keep the wording identical afterwards
3. It is a bare code in a sentence — replace it with the name of the thing it stands for; codes stay in table headers only

Change nothing else: numbers, claims, citations and figures stay as they are. Then recompile the PDF.
```
