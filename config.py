"""Contains the configuration for the Bundesliga tipping game.

It uses pydantic_settings to define the configuration, a config per season can be found.
"""

from pathlib import Path

from pydantic import BaseModel, FilePath, HttpUrl


class ScrapeTarget(BaseModel):
    """Represent a URL to scrape from and some metadata for checking."""

    league_name: str  # used as header on the homepage
    url: HttpUrl
    number_of_teams: int  # used to check scraping


class Config(BaseModel):
    """Configuration model for the Bundesliga tipping game.

    Values that do not change quite often are given as defaults.
    The defaults can be overwritten during instantiation.
    """

    file_tips: FilePath
    scrape_targets: list[ScrapeTarget]
    points_by_difference: dict[int, int]

    file_quotes: FilePath = Path("soccer_quotes.json")
    file_quotes_key: str = "soccer_quotes"
    file_synonyms: FilePath = Path("team_synonyms.json")
    file_synonyms_key: str = Path("german_soccer_team_name_synonymes")

    page_title: str = "TippyReloaded"
    page_heading: str = "Tabellen Tippspiel"
    page_header_rank: str = "#"
    page_header_name: str = "Name"
    page_header_points_total: str = "Punktzahl"

    @property
    def page_headers(self) -> list[str]:
        """Return the page headers."""
        return [
            self.page_header_rank,
            self.page_header_name,
            *[x.league_name for x in self.scrape_targets],
            self.page_header_points_total,
        ]

    # @model_validator(mode="after")
    # def check_matching_urls_and_no_of_teams(self) -> Self:
    #     """Check if the number of URLs matches the numbers of teams per URL."""
    #     if len(self.scrape_urls) != len(self.number_of_teams_per_url):
    #         msg = "Length of number_of_teams_per_url must match the length of scrape_urls."
    #         raise ValueError(msg)
    #     return self

    # @model_validator(mode="after")
    # def check_number_of_urls_matches_table_headers(self) -> Self:
    #     """Check if the number of URLs matches the headings specified."""
    #     if len(self.scrape_urls) != len(self.page_header_points_per_url):
    #         msg = "Length of page_header_points_per_url must match the length of scrape_urls."
    #         raise ValueError(msg)
    #     return self


configuration_season_2425 = {
    "file_tips": Path("tipps2425.txt"),
    "scrape_targets": [
        ScrapeTarget(
            league_name="1. BL",
            url="https://www.sportschau.de/live-und-ergebnisse/fussball/deutschland-bundesliga/tabelle",
            number_of_teams=18,
        ),
        ScrapeTarget(
            league_name="2. BL",
            url="https://www.sportschau.de/live-und-ergebnisse/fussball/deutschland-2-bundesliga/tabelle",
            number_of_teams=18,
        ),
    ],
    "points_by_difference": {0: 3, 1: 2, 2: 1},
    "page_heading": "Tabellen Tippspiel 24/25",
}
configuration_season_2324 = {
    "file_tips": Path("tipps2324.txt"),
    "scrape_targets": [
        ScrapeTarget(
            league_name="1. BL",
            url="https://www.sportschau.de/live-und-ergebnisse/fussball/deutschland-bundesliga/se51884/2023-2024/tabelle",
            number_of_teams=18,
        ),
        ScrapeTarget(
            league_name="2. BL",
            url="https://www.sportschau.de/live-und-ergebnisse/fussball/deutschland-2-bundesliga/se51885/2023-2024/tabelle",
            number_of_teams=18,
        ),
    ],
    "points_by_difference": {0: 3, 1: 2, 2: 1},
    "page_heading": "Tabellen Tippspiel 23/24",
    "page_header_points_per_url": ["1. BL", "2. BL"],
}
