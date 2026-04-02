import json
from pathlib import Path


def load(path):
    raw = Path(path).read_text()
    if not raw.strip():
        return {}
    return json.loads(raw)
