"""Scrape bundesliga tables from sportschau.de."""

from dataclasses import dataclass
from datetime import datetime

import bs4
import requests

from tippyreloaded.config.datamodels import ScrapeTarget, Ranking
from tippyreloaded.config.enumerations import Team
from tippyreloaded.stringmatching import convert_teamnames_to_ranking


def scrape_sportschau(url: str, timeout: int = 10) -> list[str]:
    """Scrapes a bundesliga tabelle from sportschau URL."""
    ranks = []

    # retrieve html code and load into bs4
    soup = bs4.BeautifulSoup(requests.get(url, timeout=timeout).text, "html.parser")

    for td in soup.find_all("td"):
        try:
            class_str = td["class"]
        except KeyError:
            class_str = []

        s = " ".join(class_str)

        if "team-name" in s.lower():
            ranks.append(td.a.text)
    return ranks


def get_ranking(target: ScrapeTarget) -> Ranking:
    """Scrapes and converts a table from a sportschau URL."""
    ranks_str = scrape_sportschau(target.url)
    ranks_enum = convert_teamnames_to_ranking(ranks_str, Team)
    return Ranking(league_name=target.league_name, ranking=ranks_enum)
    

def get_rankings(targets: list[ScrapeTarget]) -> list[Ranking]:
    """Scrapes and converts the bundesliga tabellen from multiple sportschau URLs."""
    urls = [t.url for t in targets]
    names = [t.league_name for t in targets]
    lengths = [t.number_of_teams for t in targets]
    scrapings = scrape_sportschau_multiple(urls)
    time_scraped = datetime.now().astimezone()
    rankings = convert_scrapings_to_ranking(scrapings)
    return Ranking(
        target_urls=urls,
        league_names=names,
        rankins_lengths=lengths,
        rankings_ref=rankings,
        time_scraped=time_scraped,
    )
