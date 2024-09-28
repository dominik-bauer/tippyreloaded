"""This module provides functionality to read and process tips from a file."""

from dataclasses import dataclass
from pathlib import Path

from stringmatching import convert_teamnames_to_enum, splice_list
from teamnames import Teams


@dataclass
class Tip:
    """Represents a player and what he/she tipped."""

    name: str
    tipps: list[list[Teams]]


def read_tipps_file(file_path: Path) -> list[list[str]]:
    """Reads tipps file and returns blocks of lines seperated by one or more blank lines.

    The input file should be formatted as follows:
    - For each participating player a block of consecutive lines is created
    - Blocks are separated by at least one newline
    - The first line of each block is the player name
    - The following lines are the team names the player has tipped
    - The team names must be ranked in the order the player expects them to finish
    - 1. Bundesliga tipps are first, followed by 2. Bundesliga tipps
    - All Teams must be tipped
    - No need to add the position, i.e. 1., 2. or 3. to the team names
    """
    txt = file_path.read_text()

    # remove leading and trailing whitespace from any line
    txt = "\n".join([line.strip() for line in txt.split("\n")])

    # account for one or more empty lines between blocks
    while "\n\n\n" in txt:
        txt = txt.replace("\n\n\n", "\n\n")

    return [s.strip() for s in txt.split("\n\n") if s.strip()]


def get_tips(tipps_file: Path, number_of_teams_per_url: list[int]) -> list[Tip]:
    """Read tips file and return a list of Tip objects."""
    all_tips = []
    for block in read_tipps_file(tipps_file):
        tip = [s.strip() for s in block.split("\n")]
        name = tip.pop(0)
        tip_enum = convert_teamnames_to_enum(tip)
        tip_enum_splitted = splice_list(tip_enum, number_of_teams_per_url)

        all_tips.append(Tip(name, tip_enum_splitted))

    return all_tips
