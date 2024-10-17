"""Provides functions for string matching.

Parsing the send-in tips or the scraped rankings to the according enumerations.
"""

import enum
from itertools import islice

from rapidfuzz import fuzz
from rapidfuzz.process import cdist
from scipy.optimize import linear_sum_assignment

from tippyreloaded.config import TEAM_SYNONYMES
from tippyreloaded.config.enumerations import Teams


def convert_enum_name_to_string(anyenum: enum.EnumMeta) -> list[str]:
    """Convert the names of an enum to a list of strings with spaces instead of underscores."""
    return [x.name.replace("_", " ") for x in anyenum]


def best_string_pairing(
    a: list[str],
    b: list[str],
    strict: bool = True,
) -> dict[str, str]:
    """Find the best pairing between two lists of strings."""
    if strict and (len(a) != len(b)):
        msg = "list1 and list2 must be of same lenght"
        raise ValueError(msg)
    cost_matrix = cdist(a, b, scorer=fuzz.ratio)
    row_ind, col_ind = linear_sum_assignment(-cost_matrix)
    return {a[row]: b[col] for row, col in zip(row_ind, col_ind, strict=False)}


def best_string_enum_pairing(
    list_str: list[str],
    anyenum: enum.EnumMeta,
    strict: bool = True,
) -> dict[str, enum.Enum]:
    """Find the best pairing between a list of strings and an enum."""
    list_enum = convert_enum_name_to_string(anyenum)
    result = best_string_pairing(list_str, list_enum, strict)
    return {k: anyenum[v.replace(" ", "_")] for k, v in result.items()}


def clean_teamname(team_name: str) -> str:
    """Clean and normalize the team name."""
    # strip leading numbers (i.e. rank places) and whitespace
    tn1 = team_name.strip().lstrip("1234567890").strip()

    # replace synonymes word by word
    tn2 = " ".join([TEAM_SYNONYMES.get(w.upper(), w) for w in tn1.split()])

    return tn2.replace("_", " ")


def convert_teamnames_to_enum(teamnames: list[str]) -> list[Teams]:
    tn_clean = [clean_teamname(tn) for tn in teamnames]
    amap = best_string_enum_pairing(tn_clean, Teams, strict=False)
    return [amap[s] for s in tn_clean]


def splice_list(lst: list, lengths: list[int]) -> list[list]:
    """Splice a list into sublists of specified lengths."""
    if sum(lengths) != len(lst):
        msg = "Sum of lengths must match the length of the list."
        raise ValueError(msg)
    # Make an iterator so that islice can work correctly
    it = iter(lst)
    return [list(islice(it, i)) for i in lengths]
