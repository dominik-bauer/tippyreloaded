"""Cntains the game logic, i.e. functions and classes for calculating points."""

from dataclasses import dataclass

from rankings import Ranking
from teamnames import Teams
from tips import Tip


@dataclass
class PlayerDataSet:
    """Represents a player with their tips and points in the TippyTippsen game."""

    name: str
    tipps: list[list[Teams]]
    _ref: list[list[Teams]]
    _points_by_diff: dict[int, int]

    position: int = 0

    def __post_init__(self) -> None:
        """Check if the tips and reference rankings match."""
        for t, r in zip(self.tipps, self._ref):
            if set(t) != set(r):
                t_diff = set(t) - set(r)
                r_diff = set(r) - set(t)
                msg = f"Tipps and reference rankings do not match for {self.name}. TIP: {t_diff}, REF: {r_diff}"
                raise ValueError(msg)

    @property
    def attr_in_order(self):
        """Return the attributes in the order they should be displayed. This must match the headers defined in config"""
        return [self.position, self.name, *self.points_sum, self.points_total]

    @property
    def points_all(self) -> list[list[int]]:
        """Calculate points for all tips based on the reference rankings."""
        points = []
        for t, r in zip(self.tipps, self._ref):
            points.append(compute_points(t, r, self._points_by_diff))
        return points

    @property
    def points_sum(self) -> list[int]:
        """Calculate the sum of points for all tips."""
        return [sum(p) for p in self.points_all]

    @property
    def points_total(self) -> int:
        """Calculate the total points for the player."""
        return sum(self.points_sum)

    def __str__(self) -> str:
        """Return a string representation of the player's total points."""
        return f"{self.name}: {self.points_total} points"


def compute_points(
    tipps: list[Teams],
    ranks_reference: list[Teams],
    points_by_diff: dict[int, int],
) -> list[int]:
    """Calculate all points based on the difference in positions between tipps and reference ranks."""
    points = []
    for position_tipp, team in enumerate(tipps):
        position_ref = ranks_reference.index(team)
        # lookup each position difference and the according points
        position_diff = abs(position_tipp - position_ref)
        if position_diff in points_by_diff:
            points.append(points_by_diff[position_diff])
        else:
            points.append(0)
    return points


def get_game_data(
    ranks: Ranking, tips: list[Tip], points_by_diff: dict[int, int]
) -> list[PlayerDataSet]:
    """Combine rankings and tips to compute the points and the ranking of each player."""
    game_data = []
    for tip in tips:
        pds = PlayerDataSet(
            name=tip.name,
            tipps=tip.tipps,
            _ref=ranks.rankings_ref,
            _points_by_diff=points_by_diff,
        )
        game_data.append(pds)

    # determine ranking position of each player. using sets to account for same points
    points = {player.points_total for player in game_data}
    for final_rank, point in enumerate(sorted(points, reverse=True), 1):
        for player in game_data:
            if player.points_total == point:
                player.position = final_rank

    # sort the list by position and by name
    return sorted(game_data, key=lambda x: (x.position, x.name))
