"""hello."""

from tippyreloaded import create_app

if __name__ == "__main__":
    from tippyreloaded.config import CONF
    from tippyreloaded.game import get_game_data
    from tippyreloaded.rankings import get_rankings
    from tippyreloaded.tips import get_tips

    ranks = get_rankings(CONF.scrape_targets)
    tips = get_tips(CONF.)
    game_data = get_game_data(ranks, tips)
    for player in game_data:
        print(player)
        print(player.points_all)
        print(player.points_sum)
        print(player.points_total)
    exit()
app = create_app()
app.run()
