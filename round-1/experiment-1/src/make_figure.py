"""Build the chart spec for the residual-vs-altitude figure from results/residuals.json (rendered by aii-data-fig-gen)."""
import json
from pathlib import Path

WS = Path(__file__).resolve().parent
res = json.loads((WS / "results" / "residuals.json").read_text())["residuals"]
names = {
    "V1": "V1 iso + const. H",
    "V2": "V2 iso + IAPWS",
    "V3": "V3 ISA + const. H",
    "V4": "V4 ISA + IAPWS",
}
spec = {
    "type": "line",
    "title": "Boiling-point residual vs altitude",
    "xlabel": "Altitude (m)",
    "ylabel": "Residual (K)",
    "aspect": "4:3",
    "series": [
        {"label": names[v], "x": res[v]["altitude_m"], "values": [round(x, 4) for x in res[v]["residual_K"]]}
        for v in ("V1", "V2", "V3", "V4")
    ],
}
out = WS / "results" / "residual_vs_altitude_spec.json"
out.write_text(json.dumps(spec, indent=1))
print(out)
