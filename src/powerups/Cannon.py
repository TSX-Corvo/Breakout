"""
ISPPJ1 2023
Study Case: Breakout

Author: Alejandro Mujica
alejandro.j.mujic4@gmail.com

This file contains the specialization of PowerUp, Cannon.
"""
from typing import TypeVar
from gale.timer import Timer

import settings
from src.powerups.PowerUp import PowerUp


class Cannon(PowerUp):
    """
    Power-up to create two cannon at the edges of the paddle that can shot once, the projectiles destroy
    every brick in their way until they reach the ceiling of the stage.
    """

    def __init__(self, x: int, y: int) -> None:
        super().__init__(x, y, 5)

    def take(self, play_state: TypeVar("PlayState")) -> None:
        play_state.flags['cannon_active'] = True

              

        self.in_play = False
