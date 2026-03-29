import json
import tempfile
from pathlib import Path

from config import load


def test_load_roundtrip():
    data = {"key": "value", "n": 3}
    with tempfile.TemporaryDirectory() as d:
        p = Path(d) / "c.json"
        p.write_text(json.dumps(data))
        assert load(p) == data
