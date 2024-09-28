"""Generic file operations."""

import json
from pathlib import Path


def load_json(file_path: Path, root_node: str) -> dict:
    """Load JSON file, given its root node."""
    txt = file_path.read_text(encoding="utf-8")
    data = json.loads(txt)
    if root_node not in data:
        msg = f"Root node '{root_node}' not found in JSON data '{file_path.name}')."
        raise ValueError(msg)
    return data[root_node]
