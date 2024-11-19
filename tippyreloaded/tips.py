"""Read and map tips from a file."""

from tippyreloaded.config import CONF
from tippyreloaded.config.datamodels import GameConfig, LeagueTip, PlayersTip
from tippyreloaded.stringmatching import convert_teamnames_to_enum, splice_list


def get_tips() -> list[PlayersTip]:
    """Read tips (str from CONF) and return a list of Tip objects."""
    all_tips = []
    for playertip in CONF.tips:
        for league_tip in playertip.predicted_rankings:
            tip_enum = convert_teamnames_to_enum(league_tip.predicted_ranking)
            all_tips.append(
                PlayersTip(
                    playertip.player_name,
                    LeagueTip(league_tip.league_name, tip_enum),
                ),
            )
        tip = [s.strip() for s in block.split("\n")]
        name = tip.pop(0)
        tip_enum = convert_teamnames_to_enum(tip)
        tip_enum_splitted = splice_list(tip_enum, number_of_teams_per_url)

        all_tips.append(Tip(name, tip_enum_splitted))

    return all_tips


def read_tips_from_conf(config: GameConfig):
    """Read tips from the configuration file."""
    return get_tips(config.tips_file, config.number_of_teams_per_url)


if __name__ == "__main__":
    for t in CONF.tips:
        print(t)
    print("-" * 100)
