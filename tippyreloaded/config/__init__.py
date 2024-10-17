"""Contains the configuration for the Bundesliga tipping game.

It uses pydantic_settings to define the configuration, a config per season can be found.
"""

import json
from pathlib import Path

from pydantic_yaml import parse_yaml_raw_as

from tippyreloaded.config.datamodels import FlaskConfig, GameConfig, Quote


def load_json(file_path: Path, root_node: str) -> dict:
    """Load JSON file, given its root node."""
    txt = file_path.read_text(encoding="utf-8")
    data = json.loads(txt)
    if root_node not in data:
        msg = f"Root node '{root_node}' not found in JSON data '{file_path.name}')."
        raise ValueError(msg)
    return data[root_node]


PATH_THIS_FILE = Path(__file__).resolve().parent
FILE_GAME_CONFIG = PATH_THIS_FILE / "config_game_2425.yaml"
FILE_FLASK_CONFIG = PATH_THIS_FILE / "config_flask_dev.yaml"
FILE_QUOTES = PATH_THIS_FILE / "soccer_quotes.json"
FILE_SYNONYMS = PATH_THIS_FILE / "team_synonymes.json"
FILE_QUOTES_KEY = "soccer_quotes"
FILE_SYNONYMS_KEY = "german_soccer_team_name_synonymes"

CONF = parse_yaml_raw_as(GameConfig, Path(FILE_GAME_CONFIG).read_text())
CONF_FLASK = parse_yaml_raw_as(FlaskConfig, Path(FILE_FLASK_CONFIG).read_text())
QUOTES = [Quote(**d) for d in load_json(FILE_QUOTES, FILE_QUOTES_KEY)]
TEAM_SYNONYMES = load_json(FILE_SYNONYMS, FILE_SYNONYMS_KEY)
