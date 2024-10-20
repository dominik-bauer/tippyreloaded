"""Scrape bundesliga tables from sportschau.de."""

from dataclasses import dataclass
from datetime import datetime

import bs4
import requests

from tippyreloaded.config.datamodels import ScrapeTarget
from tippyreloaded.config.enumerations import Teams
from tippyreloaded.stringmatching import best_string_enum_pairing


@dataclass
class Ranking:
    """Stores the rankings scraped from sportschau.de."""

    target_urls: list[str]
    league_names: list[str]
    rankins_lengths: list[int]
    rankings_ref: list[list[Teams]]
    time_scraped: datetime


def scrape_sportschau(url: str, timeout: int = 10) -> list[str]:
    """Scrapes the bundesliga tabelle from sportschau URL."""
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


def scrape_sportschau_multiple(urls: list[str]) -> list[list[str]]:
    """Scrapes the bundesliga tabellen from multiple sportschau URLs."""
    return [scrape_sportschau(url) for url in urls]


def convert_scrapings_to_ranking(scrapings: list[list[str]]) -> list[list[Teams]]:
    """Scrapes the bundesliga tabelle from multiple sportschau URLs."""
    ranks: list[list[Teams]] = []
    for ranks_str in scrapings:
        map_str_enum = best_string_enum_pairing(ranks_str, Teams, strict=False)
        ranks.append([map_str_enum[s] for s in ranks_str])
    return ranks


def get_rankings(targets: list[ScrapeTarget]) -> Ranking:
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
