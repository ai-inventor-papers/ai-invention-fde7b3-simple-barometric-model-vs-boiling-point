# gen_demo_art_experiment_2 — report_results

> Phase: `gen_paper_repo` · `gen_demo_art`
> Run: `run_ek8xZiRG71Qn` — Isothermal Barometric Boiling Points Match a Computed Table to 0.6 K
>
> Full, verbatim transcript of this agent task — every system/user prompt, assistant response, thinking block, tool call and tool result — in the order they occurred. Nothing truncated.

## Task: `gen_demo_art_experiment_2` (terminal_claude_agent, claude-haiku-5-5)

### [1] CONFIG · 2026-11-20 02:06:42 UTC

```
model: Claude Haiku 5.5 | effort: high | permission: bypassPermissions
```

### [2] SYSTEM-USER prompt · 2026-11-20 02:06:48 UTC

````
<conversion_philosophy>
**MINIMAL CHANGES — PRESERVE THE ORIGINAL CODE**

The goal is to make the artifact's code READABLE, UNDERSTANDABLE, and RUNNABLE in a short time
to someone reviewing the research, with the option to easily scale parameters back to original
values for a full run (which can take much longer). Think of this as annotating and reformatting,
not refactoring.

**DO:**
- Split the original script into logical notebook cells (imports, setup, processing, results)
- Open with a markdown cell that explains the setup: the question this artifact answers, the
  data and model it runs on, and what the reader will see when it runs
- Add markdown cells BETWEEN code cells explaining what each section does and why
- Add inline comments where the logic is non-obvious
- Add a visualization/summary cell at the end showing key outputs, plotted from the real numbers
  the code computes
- Close with a markdown cell that interprets the results: what the printed numbers and plots
  show, and what they mean for the claim the artifact tests
- Fix hardcoded file paths to use the GitHub data loading pattern

**DO NOT:**
- Rewrite functions or change algorithms
- Rename variables or restructure logic
- Add error handling, type hints, or "improvements" that weren't in the original
- Simplify or "clean up" the original code
- Remove any original comments or logic
- Change the computational approach

The reader should recognize the original script when looking at the notebook — it's the
same code, just split into cells with explanatory markdown between sections.
</conversion_philosophy>

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
Your own machine is the `gpu`: 6 vCPUs, 24 GB RAM (20 GB of it for the step), 12.8 GiB of GPU memory.
Start every script that uses torch with the device line: `from aii_device import DEVICE, check; check()`; where `aii_device` is not installed, `DEVICE = torch.device("mps" if torch.backends.mps.is_available() else "cpu")`. Read the `aii-use-hardware` skill before planning compute.
Instead of each CUDA habit: vLLM -> mlx-lm or llama-server; FP8 -> bf16 or MLX 8-bit; bitsandbytes -> MLX 4-bit or 8-bit; Triton kernels -> torch ops or an MLX Metal kernel; float64 on the GPU -> the CPU; torch.cuda.* -> aii_device; .cuda() -> .to(DEVICE); "cuda" if torch.cuda.is_available() else "cpu" -> DEVICE (that test silently picks the CPU); flash-attn -> sdpa; several GPUs -> one device; torch.compile -> eager mode.
Known slow spots: LSTMs, small MLPs, ops that fall back to the CPU (warned in the log), the first MPS call's warm-up, and model downloads over a home link; every step fetches its inputs again.
What executor steps get: `text_small`: 2 vCPUs, 4 GB RAM (1 GB of it for the step), no GPU work; `text`: 4 vCPUs, 8 GB RAM (4 GB of it for the step), no GPU work; `gpu`: 6 vCPUs, 24 GB RAM (20 GB of it for the step), 12.8 GiB of GPU memory; `gpu_large`: 8 vCPUs, 64 GB RAM (60 GB of it for the step), 34 GiB of GPU memory. Text agents get `text`; an executor step gets `gpu` unless its plan's `flex_guest_shape` names another shape. `gpu` fits a step within 20 GB of RAM and 12.8 GiB of GPU memory; a step that needs more sets `flex_guest_shape` to `gpu_large`, the largest guest, which fits a step within 60 GB of RAM and 34 GiB of GPU memory. At most one runs at a time on the Mac, so a `gpu_large` step may wait longer for it. `flex_guest_shape` may name any shape listed, smaller ones only for a light step that fits their RAM for the step.
One step's inputs (the run's files plus its sessions) stay under 20 GB: keep large models and datasets out of the run's files.
Use `aii-mkvenv` or a plain `uv venv` for extra packages; never reinstall or upgrade torch.
</flex_environment>

<slot_environment>
You run in the `flex_slot` environment: your own macOS account in one long-lived guest that other agents share at the same time.
Your memory share is 20 GB: going over it stops your job alone. Your disk is 40 GB; keep temp files under $TMPDIR. You have 12.8 GB of GPU memory. Use ports from $AII_PORT_BASE or port 0.
</slot_environment>

<workspace>
Your workspace: `/Volumes/aii-s20005/work/run_ek8xZiRG71Qn/4_gen_paper_repo/_4_gen_demo_art/notebook_workspaces/iter_2/art_e7cQzFbFiEBS`

CRITICAL: Every file you create, write, or save MUST be inside this workspace directory (subdirectories OK). You MUST NOT write files anywhere outside this path — external paths are READ-ONLY. Use absolute paths for all file operations.

EVERY file write MUST start with `/Volumes/aii-s20005/work/run_ek8xZiRG71Qn/4_gen_paper_repo/_4_gen_demo_art/notebook_workspaces/iter_2/art_e7cQzFbFiEBS/`:
GOOD: `/Volumes/aii-s20005/work/run_ek8xZiRG71Qn/4_gen_paper_repo/_4_gen_demo_art/notebook_workspaces/iter_2/art_e7cQzFbFiEBS/file.py`, `/Volumes/aii-s20005/work/run_ek8xZiRG71Qn/4_gen_paper_repo/_4_gen_demo_art/notebook_workspaces/iter_2/art_e7cQzFbFiEBS/results/out.json`
BAD: `/tmp/file.py`, `~/output.json`, `./file.py`, any path outside the workspace
</workspace>
<disposable_outputs>
A SHARED CACHE ALREADY EXISTS FOR THIS RUN: `/Volumes/aii-s20005/work/run_ek8xZiRG71Qn/.shared_cache`
`HF_HOME`, `HF_HUB_CACHE`, `TRANSFORMERS_CACHE`, `HF_DATASETS_CACHE`,
`TORCH_HOME`, `PIP_CACHE_DIR` and `UV_CACHE_DIR` are ALREADY set to point
there. Every step and every iteration of this run shares it, so a model or
dataset an earlier experiment downloaded is already on disk for you.

DO NOT override those variables. In particular do NOT write the common
pattern `os.environ["HF_HOME"] = <workspace>/hf_cache` — `HF_HOME` and
`TRANSFORMERS_CACHE` are read differently by `huggingface_hub` (one has
`/hub` appended, the other does not), so pointing both at one directory
stores every weight TWICE. That mistake cost one run 25 GB of identical
blobs. If you must set them, use the values above verbatim.

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

<human_message>
Please continue from where you stopped.
</human_message>

<tool_use>
Maximize parallel tool calls. Parallelize independent operations, only sequentialize dependencies.
- Multiple searches/fetches on different topics → parallel in one turn
- Search then fetch results → sequential (need URLs first)
</tool_use>

<task>
Convert this artifact's Python script into a demo notebook with MINIMAL changes to the original code.
Split into cells, add markdown explanations between sections, add a visualization cell at the end.
Output: mini_demo_data.json + code_demo.ipynb (notebook that loads data from GitHub URL)
</task>

<artifact_info>
id: art_e7cQzFbFiEBS
type: experiment
title: Checking boiling-point formulas against measured data
summary: >-
  Experiment artifact for the question: how well does the simple barometric formula predict the boiling point of water at
  altitude, compared with published measurements? The plan transcribes measured boiling-temperature and pressure pairs from
  Osborne, Stimson and Ginnings (1939) and the CRC Handbook, then compares four model variants (isothermal or ISA pressure,
  each inverted to boiling temperature by a constant-enthalpy Clausius-Clapeyron step or by IAPWS-IF97 saturation) by altitude
  band. In this round the measured set is EMPTY: the NIST RP1229 PDF returned no readable table text, the CRC Handbook table
  was not obtained, and Keene (1995) was not located. No row was padded from computed tables. The output is therefore labelled
  untested, with the statement: no measured comparison; no accuracy claim; computed reference shown only as context. The computed
  context uses the 250-row reference table (125 Engineering ToolBox rows and 125 IAPWS-IF97 at ISA pressure rows), which is
  not measured data. Unit checks pass: IAPWS-IF97 at 101.325 kPa gives 373.1243 K, the ISA and isothermal pressure formulas
  return their expected values, and all four variants agree with 373.124 K at sea-level pressure within 0.05 K. On the computed
  reference, the constant-enthalpy ISA variant (V3) runs about 1.7 K below the ToolBox values at 6 km and above (n = 42, bias
  -1.72 K; independently re-derived as -1.716 K, and a shuffled-label placebo does not reproduce it). Moving the anchor from
  373.124 K to 373.15 K shifts V1 and V3 by about +0.024 K. Outputs are full, mini and preview JSON files, band statistics,
  per-row residuals, a source log with zero rows retained, and reproducibility notes with pinned dependencies. The high-altitude
  question (6 to 9 km) remains unanswered because no measured rows exist there.
workspace_path: >-
  /Volumes/aii-s20005/work/run_ek8xZiRG71Qn/3_invention_loop/iter_2/gen_art/gen_art_experiment_2
out_expected_files:
- method.py
- full_method_out.json
- mini_method_out.json
- preview_method_out.json
- reproducibility.md
out_demo_files:
- path: method.py
  description: Research methodology implementation
</artifact_info>

<github_repo>
Repo URL: https://github.com/ai-inventor-papers/ai-invention-fde7b3-simple-barometric-model-vs-boiling-point
Raw data URL: https://raw.githubusercontent.com/ai-inventor-papers/ai-invention-fde7b3-simple-barometric-model-vs-boiling-point/main/round-2/experiment-2/demo/mini_demo_data.json

URLs won't work yet — files pushed to GitHub AFTER notebook creation.
Use local fallback pattern so notebook works locally (now) and in Colab (after deployment).
</github_repo>

<data_file_sizes>
Data files come in three sizes:
- preview_*_out.json — READ THIS to inspect the data structure
- mini_*_out.json (~3 examples) — use for prototyping/testing
- full_*_out.json (complete) — use for the final production run. NEVER open it directly (too large to read into context). Instead, extract values programmatically with shell commands (e.g. grep) or a Python script (use aii-long-running-tasks skill for scripts).
</data_file_sizes>

<install_dependencies_pattern>
Follow the aii-colab skill exactly. It has the install cell pattern, pre-installed package list, numpy 2.0 compat shims, and all Colab-specific rules.
</install_dependencies_pattern>

<data_loading_pattern>
`mini_demo_data.json` = curated subset for the demo.
Use this pattern for Colab compatibility (GitHub URL with local fallback):
```python
GITHUB_DATA_URL = "https://raw.githubusercontent.com/ai-inventor-papers/ai-invention-fde7b3-simple-barometric-model-vs-boiling-point/main/round-2/experiment-2/demo/mini_demo_data.json"
import http.client
import json
import urllib.request
from pathlib import Path

def load_data():
    try:
        with urllib.request.urlopen(GITHUB_DATA_URL, timeout=15) as response:
            return json.loads(response.read().decode())
    # Network errors, timeouts, a placeholder URL, bad JSON, a cut-off response.
    except (OSError, ValueError, http.client.HTTPException) as e:
        print("GitHub data unavailable, using local mini_demo_data.json:", e)
    local = Path("mini_demo_data.json")
    if local.exists(): return json.loads(local.read_text())
    raise FileNotFoundError("Could not load mini_demo_data.json")
```
</data_loading_pattern>

<figure_style>
Every plot in every notebook of this run shares one style. Paste this block, verbatim, at the end
of the imports cell:
```python
import matplotlib.pyplot as plt

# One colour per role, the same in every notebook of this run and in the paper's figures.
COLOURS = {
    "method": "#0173B2",  # the paper's own method, model or condition
    "baseline": "#949494",  # the main baseline, control or reference
    "other_1": "#DE8F05",  # the first further comparator
    "other_2": "#029E73",  # the second
    "other_3": "#CC78BC",  # the third
    "other_4": "#CA9161",  # the fourth
    "other_5": "#56B4E9",  # the fifth
}
plt.rcParams.update({
    "font.family": "serif",
    "font.serif": ["CMU Serif", "Computer Modern Roman", "DejaVu Serif"],
    "mathtext.fontset": "cm",
    "font.size": 11,
    "axes.spines.top": False,
    "axes.spines.right": False,
    "axes.grid": True,
    "axes.grid.axis": "y",
    "grid.color": "#CCCCCC",
    "grid.alpha": 0.6,
    "axes.axisbelow": True,
    "axes.prop_cycle": plt.cycler(color=list(COLOURS.values())),
    "image.cmap": "cividis",
    "legend.frameon": False,
    "figure.constrained_layout.use": True,
    "figure.dpi": 120,
})
```
Colour each series by its ROLE from `COLOURS` (the proposed method `COLOURS["method"]`, the main
baseline `COLOURS["baseline"]`, further comparators `other_1`, `other_2`, ... in order). Use the
default colormap (cividis) for magnitudes and "RdBu_r" for signed values. Set no colours, fonts,
sizes or style sheets of your own.
</figure_style>

<notebook_structure>
--- Setup ---
Cell 1 (markdown): Title, description, what this artifact does.
Cell 2 (code): Install dependencies — follow the aii-colab skill's install cell pattern exactly. Fill in all packages imported by the artifact's code.
Cell 3 (code): Imports — copy original import block as-is, plus any additional imports needed for the notebook (e.g. matplotlib for visualization), then the <figure_style> block.
Cell 4 (code): Data loading helper — use the <data_loading_pattern> above.
Cell 5 (code): `data = load_data()`

--- Config ---
Config cell (code): Define ALL tunable parameters (iterations, epochs, n_samples, hidden_size, etc.) as variables at the top of this cell. Start with the ABSOLUTE MINIMUM values — the smallest that produce any output at all (e.g. 1 iteration, 2 samples, smallest array size). These get gradually increased during testing — see TODOs.

--- Processing ---
Remaining cells: One code cell per logical section of the original script. Add a markdown cell BEFORE each code cell. Copy code as closely as possible, with these changes:
  1. Replace file paths to use the loaded `data` variable.
  2. Use the config variables from the config cell (NOT hardcoded values).
  3. Minimal fixes are allowed if something doesn't work in notebook context (e.g. adjusting paths, removing CLI args, fixing imports), but keep changes to the absolute minimum.

--- Results ---
Visualization cell (code): Print key results in a readable table, plot numeric data with matplotlib if appropriate, in the <figure_style> style.
</notebook_structure>

<priority>
WORKING > OPTIMIZED. A small-scale demo that runs correctly is the goal. Once the notebook passes with minimum config values, scale up only if time permits — do NOT spend multiple retries chasing larger parameters. If a working version exists, finish and move on.
</priority>

<max_notebook_total_runtime>600s (10 min)</max_notebook_total_runtime>

<test_environment>
To test-run the notebook in a clean environment (simulating Colab), use the disposable venv at `/tmp/aii_nb_test_envs/art_e7cQzFbFiEBS-dfe09672d5d0`. It is on this machine's local disk, outside your workspace, which is on a slow network volume: never create a venv inside your workspace.
```bash
UV_VENV_CLEAR=1 UV_CACHE_DIR=/tmp/aii_nb_test_envs/uv-cache uv venv -q --seed --python /usr/local/bin/python3.12 /tmp/aii_nb_test_envs/art_e7cQzFbFiEBS-dfe09672d5d0
UV_CACHE_DIR=/tmp/aii_nb_test_envs/uv-cache uv pip install -q --python /tmp/aii_nb_test_envs/art_e7cQzFbFiEBS-dfe09672d5d0/bin/python jupyter ipykernel
/tmp/aii_nb_test_envs/art_e7cQzFbFiEBS-dfe09672d5d0/bin/jupyter nbconvert --to notebook --execute --ExecutePreprocessor.timeout=600 code_demo.ipynb --output code_demo.ipynb
```
The timeout is set to <max_notebook_total_runtime>. The entire notebook must finish within this time.
`UV_VENV_CLEAR=1` recreates the venv empty at the start of every test, so each test starts clean. Do NOT delete it yourself: the pipeline removes it after you finish. If you run a test in the background, wait for its result before starting the next test.

What happens: the venv starts with only pip, jupyter and ipykernel. When the notebook's install cell runs, `google.colab` is NOT in sys.modules, so ALL packages get installed — non-Colab packages unconditionally, and Colab packages (numpy, pandas, etc.) at Colab's exact versions via the guard block. The result mirrors Colab's environment as closely as possible. If a cell fails, fix the notebook and re-run.
</test_environment>

FIRST, add ALL of these to your todo list using your task/todo-tracking tool:

CRITICAL: Todo content must be copied exactly as is written here, with NO CHANGES. These todos are intentionally detailed so that another LLM could read each one without any external context and understand exactly what it has to do.


<todos>
TODO 1. Read and STRICTLY follow these skills: aii-colab, aii-long-running-tasks.
TODO 2. Read demo file and relevant preview_* files (preview only). Understand script structure: imports, setup, processing, output. Identify ALL tunable parameters (iterations, epochs, n_samples, hidden_size, batch_size, etc.) — these go in the config cell.
TODO 3. Create `mini_demo_data.json`: curated subset from at most ONE dataset (no more than 100 diverse examples). CRITICAL: do NOT read/grep full output file — may crash. Use `head -c 5000` or stream first entries with Python to pick examples.
TODO 4. Create `code_demo.ipynb` via NotebookEdit following <notebook_structure>. Set ALL config parameters to ABSOLUTE MINIMUM values — the smallest that produce any output (e.g. 1 iteration, 2 samples, smallest array sizes). Test-run using <test_environment>. Fix all errors until it passes.
TODO 5. GRADUALLY SCALE (but don't overdo it): increase config params step by step (e.g. ~2x each round). After each increase: test-run, record runtime, fix errors. STOP SCALING as soon as results look meaningful — a working small-scale demo beats a failed large-scale one. If full original params fit within <max_notebook_total_runtime> (10% margin), use them. Otherwise keep whatever works and comment out the true original values. Do NOT spend more than 2-3 scaling rounds.
TODO 6. Verify: (1) code_demo.ipynb contains GITHUB_DATA_URL = "https://raw.githubusercontent.com/ai-inventor-papers/ai-invention-fde7b3-simple-barometric-model-vs-boiling-point/main/round-2/experiment-2/demo/mini_demo_data.json" exactly, (2) mini_demo_data.json exists, (3) uses GitHub URL pattern not just open('mini_demo_data.json').
</todos>

---

Output the result as JSON to: `./.terminal_claude_agent_struct_out.json`

JSON Schema:
```json
{
  "$defs": {
    "DemoExpectedFiles": {
      "description": "Expected output files from code demo notebook generation.",
      "properties": {
        "notebook": {
          "default": "",
          "description": "Path to the generated demo notebook. Example: 'code_demo.ipynb'",
          "title": "Notebook",
          "type": "string"
        },
        "mini_data_file": {
          "default": "",
          "description": "Path to the mini demo data JSON (curated subset). Example: 'mini_demo_data.json'",
          "title": "Mini Data File",
          "type": "string"
        }
      },
      "title": "DemoExpectedFiles",
      "type": "object"
    }
  },
  "description": "Dataset/experiment/evaluation \u2192 Jupyter notebook demo.\n\nTitle and summary come from the parent artifact (gen_art step),\nnot from the demo agent. The agent only outputs expected files.",
  "properties": {
    "out_expected_files": {
      "$ref": "#/$defs/DemoExpectedFiles",
      "description": "All output files you created. Must include the demo notebook."
    }
  },
  "required": [],
  "title": "CodeDemo",
  "type": "object"
}
```

IMPORTANT: this task is NOT complete until `./.terminal_claude_agent_struct_out.json` exists and contains JSON matching the schema above.

How well does the simple barometric formula predict the boiling point of water at different altitudes, compared with published measurements?
````

### [3] TOOL CALL — Bash · 2026-11-20 02:06:52 UTC

```
List workspace and source artifact directory:
ls -la && ls -la .aii 2>/dev/null; find . -maxdepth 2 -type f | head -50; echo "---"; ls -la /Volumes/aii-s20005/work/run_ek8xZiRG71Qn/3_invention_loop/iter_2/gen_art/gen_art_experiment_2 2>&1 | head -30
```

### [4] TOOL CALL — Skill · 2026-11-20 02:06:52 UTC

```
aii-colab
```

### [5] TOOL CALL — Skill · 2026-11-20 02:06:52 UTC

```
aii-long-running-tasks
```

### [6] TOOL RESULT — Bash · 2026-11-20 02:06:52 UTC

```
{"stdout": "total 220\ndrwx------  8 s20005 s20005    256 Nov 19 18:06 .\ndrwx------  5 s20005 s20005    160 Nov 19 18:06 ..\ndrwx------  4 s20005 s20005    128 Nov 19 18:06 .aii\n-rw-r-----  1 root   s20005  20607 Nov 19 18:06 .repl_agent.ptylog\n-rw-------  1 s20005 s20005 115195 Dec 31  1969 code_demo.ipynb\n-rw-------  1 s20005 s20005  74718 Dec 31  1969 mini_demo_data.json\n-rw-------  1 s20005 s20005   1773 Dec 31  1969 README.md\ndrwx------ 10 s20005 s20005    320 Nov 19 18:06 results\ntotal 8\ndrwx------ 4 s20005 s20005 128 Nov 19 18:06 .\ndrwx------ 8 s20005 s20005 256 Nov 19 18:06 ..\n-rw------- 1 s20005 s20005  12 Dec 31  1969 manifest.yaml\n-rw------- 1 s20005 s20005 143 Dec 31  1969 module_end.json\n./code_demo.ipynb\n./mini_demo_data.json\n./.repl_agent.ptylog\n./README.md\n./.aii/module_end.json\n./.aii/manifest.yaml\n./results/full_method_out.json\n./results/sources_summary.json\n./results/run.log\n./results/mini_method_out.json\n./results/preview_method_out.json\n./results/per_row_residuals.csv\n./results/method_out.json\n./results/band_stats.csv\n---\ntotal 344\ndrwx------ 17 s20005 s20005    544 Nov 19 18:06 .\ndrwx------  5 s20005 s20005    160 Nov 19 18:06 ..\ndrwx------  4 s20005 s20005    128 Nov 19 18:06 .aii\n-rw-------  1 s20005 s20005   2460 Dec 31  1969 .terminal_claude_agent_struct_out.json\ndrwx------  3 s20005 s20005     96 Nov 19 18:06 audit\ndrwx------  5 s20005 s20005    160 Nov 19 18:06 data\n-rw-------  1 s20005 s20005 130457 Dec 31  1969 full_method_out.json\n-rw-------  1 s20005 s20005 130457 Dec 31  1969 method_out.json\n-rw-------  1 s20005 s20005  10453 Dec 31  1969 method.py\n-rw-------  1 s20005 s20005   9376 Dec 31  1969 mini_method_out.json\n-rw-------  1 s20005 s20005  10361 Dec 31  1969 preview_method_out.json\n-rw-------  1 s20005 s20005    466 Dec 31  1969 pyproject.toml\n-rw-------  1 s20005 s20005   1851 Dec 31  1969 README.md\n-rw-------  1 s20005 s20005   3658 Dec 31  1969 reproducibility.md\ndrwx------  6 s20005 s20005    192 Nov 19 18:06 results\ndrwx------  3 s20005 s20005     96 Nov 19 18:06 sources\n-rw-------  1 s20005 s20005  35707 Dec 31  1969 uv.lock", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [7] TOOL RESULT — Skill · 2026-11-20 02:06:52 UTC

```
{"success": true, "commandName": "aii-colab"}
```

### [8] TOOL RESULT — Skill · 2026-11-20 02:06:52 UTC

```
{"success": true, "commandName": "aii-long-running-tasks"}
```

### [9] ASSISTANT · 2026-11-20 02:06:56 UTC

```
The workspace already has a notebook, mini data, a README and a manifest from the earlier pass. I'll check their state before doing anything else.
```

### [10] TOOL CALL — Bash · 2026-11-20 02:06:56 UTC

```
Inspect manifest, README, notebook cells and results:
echo "--- manifest"; cat .aii/manifest.yaml; echo; echo "--- module_end"; cat .aii/module_end.json; echo; echo "--- README"; cat README.md; echo; echo "--- notebook cells"; python3 -c "
import json
nb=json.load(open('code_demo.ipynb'))
for i,c in enumerate(nb['cells']):
    src=''.join(c['source'])
    print(f'== cell {i} [{c[\"cell_type\"]}] outputs={len(c.get(\"outputs\",[]))} exec={c.get(\"execution_count\")}')
    print(src[:300])
"; echo "--- URL check"; grep -c 'ai-invention-fde7b3-simple-barometric-model-vs-boiling-point/main/round-2/experiment-2/demo/mini_demo_data.json' code_demo.ipynb; ls -la results | head -30
```

### [11] TOOL RESULT — Bash · 2026-11-20 02:06:56 UTC

```
{"stdout": "--- manifest\nentries: []\n\n--- module_end\n{\n  \"schema\": 1,\n  \"at\": 1795135588.235478,\n  \"passed\": true,\n  \"attempts\": 1,\n  \"default_policy\": false,\n  \"keep_bytes\": 0,\n  \"problems\": []\n}\n--- README\n# Boiling point of water vs altitude: barometric models against reference data\n\n**Status: untested.** This round has no measured boiling-point data. The notebook compares four model variants against a computed reference table only. It makes no accuracy claim.\n\n## What it does\nFour variants pair a pressure model (isothermal barometric or ISA) with a boiling-temperature model (constant-enthalpy Clausius-Clapeyron or IAPWS-IF97). Predictions are compared with the Engineering ToolBox boiling-point-vs-altitude table, grouped into altitude bands. The question is how well the simple barometric formula predicts measured boiling points. That remains unanswered here.\n\n## Layout\n- `code_demo.ipynb`: the demo notebook, split from the original `method.py`. It has been run end to end at `N_ROWS = 100`.\n- `mini_demo_data.json`: 100 evenly spaced rows of the ToolBox table (one dataset), the source log, and an empty `measured_pairs` list.\n- `results/`: outputs written by the notebook run (band statistics, per-row residuals, run log, summary and JSON outputs).\n- `.aii/manifest.yaml`: artifact manifest (no heavy entries).\n\n## How to run\nOpen `code_demo.ipynb` in Jupyter or Colab and run all cells. The install cell installs `iapws` and `loguru`, and on a local machine also pins numpy, pandas and matplotlib to Colab's versions. The notebook reads the GitHub raw URL and falls back to the local `mini_demo_data.json`. The run takes about one minute.\n\n## Restoring removed files\nNothing was marked for deletion. To rebuild the outputs, run the notebook. To rebuild `mini_demo_data.json`, take 100 evenly spaced rows of the `engtoolbox_boiling_altitude` dataset in the source workspace's `data/full_data_out.json`, and copy the `sources` list from `sources/source_log.json`.\n\n--- notebook cells\n== cell 0 [markdown] outputs=0 exec=None\n# Boiling point of water against altitude: barometric models vs reference data\n\n**Question.** How well does the simple barometric formula predict the boiling point of water at altitude, compared with published measurements?\n\n**What this notebook does.** It compares four model variants. Each pairs a \n== cell 1 [markdown] outputs=0 exec=None\n## Install dependencies\n\nPackages that are not pre-installed on Colab are always installed. Pre-installed packages are installed locally only, at Colab's exact versions, so that the local environment matches Colab.\n== cell 2 [code] outputs=0 exec=1\nimport subprocess, sys\ndef _pip(*a): subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-q', *a])\n\n# Not pre-installed on Colab: always install\n_pip('iapws==1.5.5')\n_pip('loguru==0.8.0')\n\n# Pre-installed on Colab: install locally only, at Colab's exact versions\nif 'google.colab' not in \n== cell 3 [markdown] outputs=0 exec=None\n## Imports and figure style\n\nThe original import block is kept as written. `matplotlib` is added for the plots, together with the shared figure style.\n== cell 4 [code] outputs=0 exec=2\nimport csv\nimport json\nimport math\nimport sys\nfrom pathlib import Path\n\nimport numpy as np\nimport pandas as pd\nfrom iapws import IAPWS97\nfrom loguru import logger\n\nimport matplotlib.pyplot as plt\n\n# One colour per role, the same in every notebook of this run and in the paper's figures.\nCOLOURS = {\n \n== cell 5 [markdown] outputs=0 exec=None\n## Load the data\n\nThe data are read from the GitHub raw URL. If that is unavailable (for example before the repository is published), the local `mini_demo_data.json` next to this notebook is used.\n== cell 6 [code] outputs=0 exec=3\nGITHUB_DATA_URL = \"https://raw.githubusercontent.com/ai-inventor-papers/ai-invention-fde7b3-simple-barometric-model-vs-boiling-point/main/round-2/experiment-2/demo/mini_demo_data.json\"\nimport http.client\nimport json\nimport urllib.request\nfrom pathlib import Path\n\ndef load_data():\n    try:\n        wi\n== cell 7 [code] outputs=1 exec=4\ndata = load_data()\nprint(\"datasets:\", [(d[\"dataset\"], len(d[\"examples\"])) for d in data[\"datasets\"]])\n== cell 8 [markdown] outputs=0 exec=None\n## Config\n\n`N_ROWS` is the number of reference rows used. The rows are spread evenly across the table. It starts at the smallest value that gives output, and is raised step by step in testing.\n== cell 9 [code] outputs=0 exec=5\n# Tunable parameters\nN_ROWS = 100  # number of computed reference rows used (all 100 rows in the mini file)\n== cell 10 [markdown] outputs=0 exec=None\n## Constants and model functions\n\nThese are the original constants and functions, unchanged. The only change is that `WS` is the notebook's folder, because `__file__` does not exist in a notebook.\n== cell 11 [code] outputs=0 exec=6\nWS = Path.cwd()  # the notebook's folder (__file__ is not defined in a notebook)\nRES = WS / \"results\"\nRES.mkdir(parents=True, exist_ok=True)\n\n# Constants (plan section STEP 3/4)\nG = 9.80665\nM_AIR = 0.028964\nR_GAS = 8.314462\nT0 = 288.15\nP0 = 101325.0\nLAPSE = 0.0065\nH_SCALE = R_GAS * T0 / (M_AIR * G) \n== cell 12 [markdown] outputs=0 exec=None\n## Logger and unit checks\n\nThe original `main()` function is split into cells. Its body is kept in order, and the logger is set up here. The sanity checks confirm the constants and the IAPWS-IF97 value at 101.325 kPa.\n== cell 13 [code] outputs=1 exec=7\nlogger.remove()\nlogger.add(sys.stdout, level=\"INFO\")\nlogger.add(RES / \"run.log\", level=\"DEBUG\", rotation=\"5 MB\")\n\n# Constant sanity checks (T1, T3, T4)\nassert abs(t_ce(PB_PA) - TB_K) < 1e-9, \"T1 failed\"\nassert abs(p_isa(0.0) - P0) < 1e-6, \"T3 failed (sea level)\"\nassert abs(p_isa(11000.0) - 22632.0) \n== cell 14 [markdown] outputs=0 exec=None\n## Measured set and computed reference rows\n\nThe measured set comes from the `measured_pairs` list in the mini file. It is empty in this round, so no measured comparison is made. The computed reference rows are used as context only and are never labelled as measured.\n== cell 15 [code] outputs=2 exec=8\n# Measured set (may be empty): zero rows in this round\nmeasured = pd.DataFrame(data[\"measured_pairs\"])\nn_measured = len(measured)\nlogger.info(\"Measured rows: {}\", n_measured)\n\n# Computed reference rows (context only). Rows are spread evenly across each dataset, N_ROWS of them.\nref_rows = []\nfor ds i\n== cell 16 [markdown] outputs=0 exec=None\n## Sea-level confirmation\n\nAt 101.325 kPa, all four variants must agree with 373.124 K within 0.05 K.\n== cell 17 [code] outputs=1 exec=9\n# Sea-level confirmation (T7): all variants at 101.325 kPa must match 373.124 K within 0.05 K\nsea = {v: model_T(v, PB_PA) for v in VARIANTS}\nsea_ok = all(abs(t - TB_K) <= 0.05 for t in sea.values())\nlogger.info(\"Sea-level confirmation: {} {}\", {k: round(v, 3) for k, v in sea.items()}, \"PASS\" if sea_\n== cell 18 [markdown] outputs=0 exec=None\n## Per-row residuals and band statistics (computed context)\n\nEach variant's predicted boiling temperature is compared with the reference at each row's altitude, using the model pressure for that altitude. The residuals are then summarised per altitude band. These are computed-context statistics, not\n== cell 19 [code] outputs=0 exec=10\n# Per-row residuals on the computed reference (context)\nrows_out = []\nfor _, r in ref.iterrows():\n    h = r[\"altitude_m\"]\n    rec = {\n        \"data_type\": r[\"data_type\"],\n        \"source_id\": r[\"source_id\"],\n        \"altitude_m\": h,\n        \"band\": band_of(h),\n        \"T_ref_K\": r[\"T_ref_K\"],\n    }\n\n== cell 20 [markdown] outputs=0 exec=None\n## Anchor check and sign counts\n\nThe anchor check moves the boiling-point anchor from 373.124 K to 373.15 K, for V1 and V3. The sign count compares V1 with V3 row by row.\n== cell 21 [code] outputs=0 exec=11\n# Anchor check (V1 and V3 with 373.15 K), computed reference only\nanchor = {}\nfor v in (\"V1\", \"V3\"):\n    diffs = []\n    for _, r in per_row.iterrows():\n        p = model_P(v, r[\"altitude_m\"])\n        diffs.append(t_ce(p, TB_ALT_K) - t_ce(p, TB_K))\n    anchor[v] = float(np.mean(diffs))\n\n# V1 minus V3\n== cell 22 [markdown] outputs=0 exec=None\n## Summary and output files\n\nThe source log is read from the mini file (its `sources` list), not from a `sources/` folder. The outputs are written to `results/`.\n== cell 23 [code] outputs=1 exec=12\nsources = {\"sources\": data[\"sources\"]}  # source log, carried in mini_demo_data.json\nsummary = {\n    \"n_measured\": n_measured,\n    \"sources_retained\": sum(1 for s in sources[\"sources\"] if s.get(\"rows_retained\", 0) > 0),\n    \"measured_claim\": \"none\" if n_measured == 0 else \"see band_stats.csv, eviden\n== cell 24 [markdown] outputs=0 exec=None\n## Results: table and figures\n\nThe table shows the bias (model minus reference, in kelvin) for each variant and altitude band. The row counts are shown beside it. Everything here is computed context, because no measured rows exist in this round. The variants are coloured by role: V1 (the simple isot\n== cell 25 [code] outputs=2 exec=13\n# Key results, computed context only (no measured rows in this round)\nctx = band_df[band_df[\"evidence\"] == \"computed_context\"]\ntable = ctx.pivot_table(index=\"band\", columns=\"variant\", values=\"bias_K\", aggfunc=\"first\")\nprint(\"Bias (model minus computed reference), K. Context only, not measured:\")\npri\n== cell 26 [markdown] outputs=0 exec=None\n## Interpreting the results\n\n**What the numbers show (computed context only).** Each bias is the model's boiling temperature minus the Engineering ToolBox value, in kelvin. A positive bias means the model is hotter than the table.\n\n- **V1 (isothermal pressure, constant-enthalpy step)**, the simple b\n--- URL check\n1\ntotal 156\ndrwx------ 10 s20005 s20005   320 Nov 19 18:06 .\ndrwx------  8 s20005 s20005   256 Nov 19 18:06 ..\n-rw-------  1 s20005 s20005  1433 Dec 31  1969 band_stats.csv\n-rw-------  1 s20005 s20005 54046 Dec 31  1969 full_method_out.json\n-rw-------  1 s20005 s20005 54046 Dec 31  1969 method_out.json\n-rw-------  1 s20005 s20005  5946 Dec 31  1969 mini_method_out.json\n-rw-------  1 s20005 s20005 15496 Dec 31  1969 per_row_residuals.csv\n-rw-------  1 s20005 s20005  6929 Dec 31  1969 preview_method_out.json\n-rw-------  1 s20005 s20005  1851 Dec 31  1969 run.log\n-rw-------  1 s20005 s20005   537 Dec 31  1969 sources_summary.json", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [12] ASSISTANT · 2026-11-20 02:07:02 UTC

```
The notebook, mini data, URL and manifest are all in place from the earlier pass. Nothing has written the structured output file yet, and I want a fresh clean-venv run to confirm the notebook still passes before I report it done.
```

### [13] TOOL CALL — Bash · 2026-11-20 02:07:02 UTC

```
Clean-venv end-to-end notebook execution test:
UV_VENV_CLEAR=1 UV_CACHE_DIR=/tmp/aii_nb_test_envs/uv-cache uv venv -q --seed --python /usr/local/bin/python3.12 /tmp/aii_nb_test_envs/art_e7cQzFbFiEBS-dfe09672d5d0 && UV_CACHE_DIR=/tmp/aii_nb_test_envs/uv-cache uv pip install -q --python /tmp/aii_nb_test_envs/art_e7cQzFbFiEBS-dfe09672d5d0/bin/python jupyter ipykernel && timeout 600 /tmp/aii_nb_test_envs/art_e7cQzFbFiEBS-dfe09672d5d0/bin/jupyter nbconvert --to notebook --execute --ExecutePreprocessor.timeout=600 code_demo.ipynb --output code_demo.ipynb; echo "EXIT=$?"
```

### [14] TOOL RESULT — Bash · 2026-11-20 02:07:02 UTC

```
{"stdout": "  × No interpreter found for path `/usr/local/bin/python3.12` in managed\n  │ installations or search path\nEXIT=1", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [15] TOOL CALL — Bash · 2026-11-20 02:07:02 UTC

```
Locate a Python 3.12 interpreter:
which python3.12 python3; ls /usr/local/bin | grep -i python | head; uv python find 3.12 2>&1 | head -2
```

### [16] TOOL RESULT — Bash · 2026-11-20 02:07:02 UTC

```
{"stdout": "/opt/aii/venv/bin/python3.12\n/opt/aii/venv/bin/python3\nls: cannot access '/usr/local/bin': No such file or directory\n/opt/aii/venv/bin/python3", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [17] ASSISTANT · 2026-11-20 02:07:06 UTC

```
The configured interpreter path doesn't exist on this machine, so I'll use the available Python 3.12 instead.
```

### [18] TOOL CALL — Bash · 2026-11-20 02:07:07 UTC

```
Clean-venv end-to-end notebook execution test:
/opt/aii/venv/bin/python3.12 --version && UV_VENV_CLEAR=1 UV_CACHE_DIR=/tmp/aii_nb_test_envs/uv-cache uv venv -q --seed --python /opt/aii/venv/bin/python3.12 /tmp/aii_nb_test_envs/art_e7cQzFbFiEBS-dfe09672d5d0 && UV_CACHE_DIR=/tmp/aii_nb_test_envs/uv-cache uv pip install -q --python /tmp/aii_nb_test_envs/art_e7cQzFbFiEBS-dfe09672d5d0/bin/python jupyter ipykernel && timeout 600 /tmp/aii_nb_test_envs/art_e7cQzFbFiEBS-dfe09672d5d0/bin/jupyter nbconvert --to notebook --execute --ExecutePreprocessor.timeout=600 code_demo.ipynb --output code_demo.ipynb; echo "EXIT=$?"
```

### [19] TOOL RESULT — Bash · 2026-11-20 02:08:15 UTC

```
{"stdout": "Python 3.12.14\n[NbConvertApp] Converting notebook code_demo.ipynb to notebook\n[IPKernelApp] WARNING | Kernel is running over TCP without encryption. All communication (including code and outputs) is sent in plain text and is susceptible to eavesdropping. Use IPC transport or launch with kernel manager-provisioned CurveZMQ keys to enable transport encryption.\n[NbConvertApp] Writing 115445 bytes to code_demo.ipynb\nEXIT=0", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [20] ASSISTANT · 2026-11-20 02:08:17 UTC

```
The clean-venv run passed. Next I'll confirm no cell logged an error and that the checks hold, then write the required output file.
```

### [21] TOOL CALL — Bash · 2026-11-20 02:08:17 UTC

```
Check notebook for errors and confirm results written:
python3 -c "
import json
nb=json.load(open('code_demo.ipynb'))
errs=[i for i,c in enumerate(nb['cells']) for o in c.get('outputs',[]) if o.get('output_type')=='error']
print('error cells:', errs)
print('exec counts:', [c.get('execution_count') for c in nb['cells'] if c['cell_type']=='code'])
" && grep -c 'HF_HOME\|os.environ\[' code_demo.ipynb; ls -la results/band_stats.csv results/run.log && tail -3 results/run.log
```

### [22] TOOL RESULT — Bash · 2026-11-20 02:08:17 UTC

```
{"stdout": "error cells: []\nexec counts: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]\n0\n-rw------- 1 s20005 s20005 1433 Nov 19 18:08 results/band_stats.csv\n-rw------- 1 s20005 s20005 2470 Nov 19 18:08 results/run.log\n2026-11-19 18:08:10.061 -08:00 | INFO     | __main__:<module>:21 - Computed reference rows: 100 ({'computed_unknown_method': 100})\n2026-11-19 18:08:10.100 -08:00 | INFO     | __main__:<module>:4 - Sea-level confirmation: {'V1': 373.124, 'V2': 373.124, 'V3': 373.124, 'V4': 373.124} PASS\n2026-11-19 18:08:11.827 -08:00 | INFO     | __main__:<module>:75 - Wrote outputs. Status: untested, examples: 100", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [23] ASSISTANT · 2026-11-20 02:08:21 UTC

```
Everything checks out. Writing the structured output file the task requires.
```

### [24] TOOL CALL — Write · 2026-11-20 02:08:21 UTC

```
File: /Volumes/aii-s20005/work/run_ek8xZiRG71Qn/4_gen_paper_repo/_4_gen_demo_art/notebook_workspaces/iter_2/art_e7cQzFbFiEBS/.terminal_claude_agent_struct_out.json

{
  "out_expected_files": {
    "notebook": "code_demo.ipynb",
    "mini_data_file": "mini_demo_data.json"
  }
}
```

### [25] TOOL RESULT — Write · 2026-11-20 02:08:21 UTC

```
{"type": "create", "filePath": "/Volumes/aii-s20005/work/run_ek8xZiRG71Qn/4_gen_paper_repo/_4_gen_demo_art/notebook_workspaces/iter_2/art_e7cQzFbFiEBS/.terminal_claude_agent_struct_out.json", "content": "{\n  \"out_expected_files\": {\n    \"notebook\": \"code_demo.ipynb\",\n    \"mini_data_file\": \"mini_demo_data.json\"\n  }\n}\n", "structuredPatch": [], "originalFile": null, "userModified": false}
```

### [26] ASSISTANT · 2026-11-20 02:08:25 UTC

```
The demo notebook passes end to end in a clean Python 3.12 venv, and the structured output file is written.

**What was already in place from the earlier pass:** `code_demo.ipynb`, `mini_demo_data.json` (100 evenly spaced rows of the ToolBox table, plus the source log and an empty `measured_pairs` list), `README.md`, and `.aii/manifest.yaml` with no heavy entries.

**What I checked or did in this pass:**
- **Clean-venv run:** `nbconvert --execute` exits 0. No cell produced an error output. All 13 code cells executed.
- **Sea-level check:** all four variants return 373.124 K at 101.325 kPa, so it passes.
- **Data loading:** the notebook uses the GitHub raw URL with the local `mini_demo_data.json` fallback. The URL matches the one you specified exactly, and the notebook sets no `HF_HOME` or other cache overrides.
- **Output file:** wrote `.terminal_claude_agent_struct_out.json` with `notebook: code_demo.ipynb` and `mini_data_file: mini_demo_data.json`.

**Choices and deviations:**
- **Scaling:** `N_ROWS = 100` is the full mini file, so there was nothing larger to scale to. I did not run the 2–3 scaling rounds from TODO 5.
- **Interpreter:** the configured `/usr/local/bin/python3.12` does not exist on this machine. I used `/opt/aii/venv/bin/python3.12` (Python 3.12.14) instead.
- **Manifest:** `.aii/manifest.yaml` has `entries: []`. Nothing in the workspace is a large binary or cache, so no decisions are needed.
- **Status:** the artifact is labelled untested. There are no measured rows, so the notebook makes no accuracy claim. The computed reference is shown as context only.
```
