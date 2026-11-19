"""Write mini (3 examples per dataset group) and preview (10 per group, strings cut to 200 chars) variants of full_data_out.json."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def truncate(obj):
    if isinstance(obj, str):
        return obj[:200]
    if isinstance(obj, dict):
        return {k: truncate(v) for k, v in obj.items()}
    if isinstance(obj, list):
        return [truncate(x) for x in obj]
    return obj


def subset(full: dict, n: int) -> dict:
    return {"metadata": full["metadata"],
            "datasets": [{"dataset": g["dataset"], "examples": g["examples"][:n]} for g in full["datasets"]]}


def main() -> None:
    full = json.loads((ROOT / "full_data_out.json").read_text(encoding="utf-8"))
    (ROOT / "mini_data_out.json").write_text(json.dumps(subset(full, 3), indent=1, ensure_ascii=False), encoding="utf-8")
    (ROOT / "preview_data_out.json").write_text(json.dumps(truncate(subset(full, 10)), indent=1, ensure_ascii=False), encoding="utf-8")


if __name__ == "__main__":
    main()
