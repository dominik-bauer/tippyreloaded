"""Defines the routes for the Flask app."""

from config import CONF
from flask import render_template

from tippyreloaded import app
from tippyreloaded.config import QUOTES
from tippyreloaded.game import get_game_data
from tippyreloaded.rankings import get_rankings
from tippyreloaded.tips import get_tips

PLAYERS_TIPS = get_tips(
    CONF.file_tips,
    [x.number_of_teams for x in CONF.scrape_targets],
)

# TODO check all occurences of CONF
# make use of ScrapeTarget and the given name
# improve get rankings include chekcs


@app.route("/")
def index() -> str:
    """Render the index page with game data, configuration, and a random quote."""
    ranks = get_rankings(CONF.scrape_targets)
    quote = get_random_quote(QUOTES)

    game_data = get_game_data(
        ranks=ranks,
        tips=PLAYERS_TIPS,
        points_by_diff=CONF.points_by_difference,
    )

    # Pass the Pydantic models to the template
    return render_template(
        "table.html",
        game_data=game_data,
        conf=CONF,
        quote=quote,
        data_date=ranks.time_scraped.strftime("%d.%m.%Y %H:%M:%S"),
    )
