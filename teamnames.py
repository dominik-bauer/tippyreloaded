"""Functions related to team names."""

import enum
from pathlib import Path

from fileops import load_json

TEAM_SYNONYMES = load_json(
    Path("team_synonymes.json"),
    "german_soccer_team_name_synonymes",
)


def clean_teamname(team_name: str) -> str:
    """Clean and normalize the team name."""
    # strip leading numbers (i.e. rank places) and whitespace
    tn1 = team_name.strip().lstrip("1234567890").strip()

    # replace synonymes word by word
    tn2 = " ".join([TEAM_SYNONYMES.get(w.upper(), w) for w in tn1.split()])

    return tn2.replace("_", " ")


class Teams(enum.Enum):
    """German soccer teams (not limited to 1./2./3. Bundesliga)."""

    Arminia_Bielefeld = enum.auto()
    Bayer_Leverkusen = enum.auto()
    Bayern_München = enum.auto()
    Borussia_Dortmund = enum.auto()
    Borussia_Dortmund_II = enum.auto()
    Borussia_Mönchengladbach = enum.auto()
    Dynamo_Dresden = enum.auto()
    Eintracht_Braunschweig = enum.auto()
    Eintracht_Frankfurt = enum.auto()
    Erzgebirge_Aue = enum.auto()
    Fc_Augsburg = enum.auto()
    FC_Hansa_Rostock = enum.auto()
    Fc_Heidenheim_1846 = enum.auto()
    FC_Ingolstadt_04 = enum.auto()
    FC_Kaiserslautern = enum.auto()
    FC_Köln = enum.auto()
    FC_Magdeburg = enum.auto()
    FC_Nürnberg = enum.auto()
    FC_Saarbrücken = enum.auto()
    FC_Schalke_04 = enum.auto()
    Fc_St_Pauli = enum.auto()
    Fc_Union_Berlin = enum.auto()
    Fsv_Mainz_05 = enum.auto()
    Fortuna_Düsseldorf = enum.auto()
    Hallescher_FC = enum.auto()
    Hamburger_SV = enum.auto()
    Hannover_96 = enum.auto()
    Hertha_BSC = enum.auto()
    Hoffenheim = enum.auto()
    Holstein_Kiel = enum.auto()
    Jahn_Regensburg = enum.auto()
    Karlsruher_SC = enum.auto()
    MSV_Duisburg = enum.auto()
    Preußen_Münster = enum.auto()
    Rb_Leipzig = enum.auto()
    Rot_Weiss_Essen = enum.auto()
    Sc_Freiburg = enum.auto()
    SC_Freiburg_II = enum.auto()
    SC_Paderborn_07 = enum.auto()
    SC_Verl = enum.auto()
    SSV_Ulm_1846 = enum.auto()
    SV_07_Elversberg = enum.auto()
    SV_Darmstadt_98 = enum.auto()
    SV_Sandhausen = enum.auto()
    SV_Wehen_Wiesbaden = enum.auto()
    SpVgg_Greuther_Fürth = enum.auto()
    SpVgg_Unterhaching = enum.auto()
    TSV_1860_München = enum.auto()
    VfB_Lübeck = enum.auto()
    VfB_Stuttgart = enum.auto()
    VfL_Bochum = enum.auto()
    VfL_Osnabrück = enum.auto()
    VfL_Wolfsburg = enum.auto()
    Viktoria_Köln = enum.auto()
    Waldhof_Mannheim = enum.auto()
    Werder_Bremen = enum.auto()
