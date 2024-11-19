"""Provides functions for string matching.

Parsing the send-in tips or the scraped rankings to the according enumerations.
"""

from collections.abc import Iterable

from rapidfuzz import fuzz
from rapidfuzz.process import cdist
from scipy.optimize import linear_sum_assignment

from tippyreloaded.config import TEAM_SYNONYMES
from tippyreloaded.config.datamodels import Ranking
from tippyreloaded.config.enumerations import Team


def best_string_pairing(
    a: list[str],
    b: list[str],
) -> dict[str, str]:
    """Find the best pairing between two lists of strings."""
    cost_matrix = cdist(a, b, scorer=fuzz.ratio)
    row_ind, col_ind = linear_sum_assignment(-cost_matrix)
    return {a[r]: b[c] for r, c in zip(row_ind, col_ind, strict=False)}


def remove_leading_chars(alist: list[str], leading_characters: str) -> list[str]:
    """Remove leading_characters only if every string starts with them."""
    if all(x.strip()[0] in leading_characters for x in alist):
        return [x.strip().lstrip(leading_characters).strip() for x in alist]
    return alist


def replace_words_via_dict(
    input_string: str,
    replacement_dict: dict,
    word_delimiter: str = " ",
) -> list[str]:
    """Replace words in a list of strings with a dictionary."""
    output = []

    for word in input_string.strip().split(word_delimiter):
        # either get lookup value or keep the word
        replacement = replacement_dict.get(word.upper(), word)
        output.append(replacement)

    return word_delimiter.join(output)


def convert_teamnames_to_ranking(
    teamnames: list[str],
    reference: Iterable[Team],
) -> Ranking:
    """Convert a list of team names to a Ranking object."""
    # remove leading numbers (i.e. rank places) and whitespace
    tns = remove_leading_chars(teamnames, "1234567890")

    # replace synonymes word by word
    tns_expanded = [replace_words_via_dict(tn, TEAM_SYNONYMES) for tn in tns]

    tns_reference = [t.value for t in reference]

    # Find the best pairing between two lists of strings.
    map_tns_to_ref = best_string_pairing(tns_expanded, tns_reference)

    # convert to the correct team enum
    new_ranking = [Team(map_tns_to_ref[s]) for s in tns_expanded]

    return Ranking(league_name=reference.league_name, ranking=new_ranking)


