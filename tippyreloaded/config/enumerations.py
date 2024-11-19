"""Contains any enumerations."""

from enum import Enum


class StrEnum(str, Enum):
    """Enum for string values."""

    def __str__(self) -> str:
        """Return the string representation of the enum value."""
        return self.value


class League(StrEnum):
    """Enum for the league names."""

    Bundesliga1 = "1. Bundesliga"
    Bundesliga2 = "2. Bundesliga"
    Bundesliga3 = "3. Bundesliga"


class Team(StrEnum):
    """German soccer teams (not limited to 1./2./3. Bundesliga)."""

    Arminia_Bielefeld = "Arminia Bielefeld"
    Bayer_Leverkusen = "Bayer 04 Leverkusen"
    Bayern_Muenchen = "FC Bayern München"
    Borussia_Dortmund = "Borussia Dortmund"
    Borussia_Dortmund_II = "Borussia Dortmund II"
    Borussia_Moenchengladbach = "Borussia Mönchengladbach"
    Dynamo_Dresden = "Dynamo Dresden"
    Eintracht_Braunschweig = "Eintracht Braunschweig"
    Eintracht_Frankfurt = "Eintracht Frankfurt"
    Erzgebirge_Aue = "Erzgebirge Aue"
    FC_Augsburg = "FC Augsburg"
    FC_Hansa_Rostock = "FC Hansa Rostock"
    FC_Heidenheim_1846 = "1. FC Heidenheim 1846"
    FC_Ingolstadt_04 = "FC Ingolstadt 04"
    FC_Kaiserslautern = "1. FC Kaiserslautern"
    FC_Koeln = "1. FC Köln"
    FC_Magdeburg = "1. FC Magdeburg"
    FC_Nuernberg = "1. FC Nürnberg"
    FC_Saarbruecken = "1. FC Saarbrücken"
    FC_Schalke_04 = "FC Schalke 04"
    FC_St_Pauli = "FC St. Pauli"
    FC_Union_Berlin = "1. FC Union Berlin"
    FSV_Mainz_05 = "1. FSV Mainz 05"
    Fortuna_Duesseldorf = "Fortuna Düsseldorf"
    Hallescher_FC = "Hallescher FC"
    Hamburger_SV = "Hamburger SV"
    Hannover_96 = "Hannover 96"
    Hertha_BSC = "Hertha BSC"
    Hoffenheim = "TSG 1899 Hoffenheim"
    Holstein_Kiel = "Holstein Kiel"
    Jahn_Regensburg = "SSV Jahn Regensburg"
    Karlsruher_SC = "Karlsruher SC"
    MSV_Duisburg = "MSV Duisburg"
    Preussen_Muenster = "Preußen Münster"
    RB_Leipzig = "RB Leipzig"
    Rot_Weiss_Essen = "Rot-Weiss Essen"
    SC_Freiburg = "SC Freiburg"
    SC_Freiburg_II = "SC Freiburg II"
    SC_Paderborn_07 = "SC Paderborn 07"
    SC_Verl = "SC Verl"
    SSV_Ulm_1846 = "SSV Ulm 1846"
    SV_07_Elversberg = "SV 07 Elversberg"
    SV_Darmstadt_98 = "SV Darmstadt 98"
    SV_Sandhausen = "SV Sandhausen"
    SV_Wehen_Wiesbaden = "SV Wehen Wiesbaden"
    SpVgg_Greuther_Fuerth = "SpVgg Greuther Fürth"
    SpVgg_Unterhaching = "SpVgg Unterhaching"
    TSV_1860_Muenchen = "TSV 1860 München"
    VfB_Luebeck = "VfB Lübeck"
    VfB_Stuttgart = "VfB Stuttgart"
    VfL_Bochum = "VfL Bochum"
    VfL_Osnabrueck = "VfL Osnabrück"
    VfL_Wolfsburg = "VfL Wolfsburg"
    Viktoria_Koeln = "FC Viktoria Köln"
    Waldhof_Mannheim = "SV Waldhof Mannheim"
    Werder_Bremen = "SV Werder Bremen"
