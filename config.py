import json

from utils import read_text


def load(path):
    raw = read_text(path)
    if not raw.strip():
        return {}
    return json.loads(raw)
