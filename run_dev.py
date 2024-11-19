from pathlib import Path
from pprint import pprint as print

import ruamel.yaml as yaml1

from tippyreloaded.config import CONF

if __name__ == "__main__":
    yml = yaml1.YAML(typ="safe", pure=True)

    print(CONF)

    with Path("./tippyreloaded/config/config_game_2425.yaml").open() as f:
        x = yml.load(f)

    for k in x["tips"]:
        print(k)
        # print(v)
        print("-" * 80)
