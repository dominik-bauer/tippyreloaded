"""Contains all pydantic data models."""

from pydantic import BaseModel, HttpUrl

from tippyreloaded.config.enumerations import League


class ScrapeTarget(BaseModel):
    """Represent a URL to scrape from and some metadata for checking."""

    league_name: League
    url: HttpUrl
    number_of_teams: int  # used to check scraping


class Ranking(BaseModel):
    """Represent the actual or predicted ranking of a league."""

    league_name: League
    ranking: list[str]
    # ranking: list[Team]


class PlayersTip(BaseModel):
    """Represent the tips for a player."""

    player_name: str
    predicted_rankings: list[Ranking]


class GameConfig(BaseModel):
    """Configuration model for the Bundesliga tipping game.

    Values that do not change quite often are given as defaults.
    The defaults can be overwritten during instantiation.
    """

    scrape_targets: list[ScrapeTarget]
    points_by_difference: dict[int, int]
    tips: list[PlayersTip]

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


class FlaskConfig(BaseModel):
    """Configure Flask."""

    SECRET_KEY: str
    DEBUG: bool = False
    TESTING: bool = False


class Quote(BaseModel):
    """Represents a soccer quote."""

    quote: str
    author: str
