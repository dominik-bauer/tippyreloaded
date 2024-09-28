"""Loads and selects quotes."""

import random
from dataclasses import dataclass
from pathlib import Path

from fileops import load_json


@dataclass
class Quote:
    """Represents a soccer quote."""

    quote: str
    author: str


def get_random_quote(quotes: list[Quote]) -> Quote:
    """Return a random quote."""
    return random.choice(quotes)  # noqa: S311


def load_quotes(file_path: Path, root_node: str) -> list[Quote]:
    """Load quotes from a JSON file."""
    quotes = load_json(file_path, root_node)
    return [Quote(**d) for d in quotes]
