"""
ISPPJ1 2023
Study Case: Breakout

Author: Alejandro Mujica
alejandro.j.mujic4@gmail.com

This file contains the specialization of PowerUp, Armageddon.
"""
from typing import TypeVar
from gale.timer import Timer

import settings
from src.powerups.PowerUp import PowerUp


class Armageddon(PowerUp):
    """
    Power-up that destroys all bricks on the current level.
    """

    def __init__(self, x: int, y: int) -> None:
        super().__init__(x, y, 3)

    def take(self, play_state: TypeVar("PlayState")) -> None:
        bricks = play_state.brickset.bricks

        for brick in bricks.values():
            while(not brick.broken):
                brick.hit()
                play_state.score += brick.score()

        play_state.state_machine.change(
            "victory",
            lives=play_state.lives,
            level=play_state.level,
            score=play_state.score,
            paddle=play_state.paddle,
            balls=play_state.balls,
            points_to_next_live=play_state.points_to_next_live,
            live_factor=play_state.live_factor,
        )


        self.in_play = False
