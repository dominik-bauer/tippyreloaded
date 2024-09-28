"""Runs the TippyTippsen tipping game.

Scrapes current bundesliga rankins from sportschau and calculates
the points for each player based on their tips and the scraped rankings.
"""

from flask import Flask, render_template
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

from config import Config, configuration_season_2425
from game import get_game_data
from quotes import get_random_quote, load_quotes
from rankings import get_rankings
from tips import get_tips

CONF = Config(**configuration_season_2425)

SOCCER_QUOTES = load_quotes(CONF.file_quotes, CONF.file_quotes_key)
PLAYERS_TIPS = get_tips(
    CONF.file_tips,
    [x.number_of_teams for x in CONF.scrape_targets],
)

# TODO check all occurences of CONF
# make use of ScrapeTarget and the given name
# improve get rankings include chekcs

app = Flask(__name__)
limiter = Limiter(
    get_remote_address,
    app=app,
    default_limits=["6 per minute"],
    storage_uri="memory://",
)


@app.route("/")
def index():
    ranks = get_rankings(CONF.scrape_targets)
    quote = get_random_quote(SOCCER_QUOTES)

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


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)
