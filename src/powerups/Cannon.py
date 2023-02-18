"""
ISPPJ1 2023
Study Case: Breakout

Author: Alejandro Mujica
alejandro.j.mujic4@gmail.com

This file contains the specialization of PowerUp, Cannon.
"""
from typing import TypeVar
from gale.factory import Factory


import settings
from src.powerups.PowerUp import PowerUp
from src.Cannon import Cannon as CannonVisuals


class Cannon(PowerUp):
    """
    Power-up to create two cannon at the edges of the paddle that can shot once, the projectiles destroy
    every brick in their way until they reach the ceiling of the stage.
    """

    def __init__(self, x: int, y: int) -> None:
        super().__init__(x, y, 7)
        self.cannon_factory = Factory(CannonVisuals)

    def take(self, play_state: TypeVar("PlayState")) -> None:
        play_state.flags['cannon_active'] = True
        paddle = play_state.paddle
        prev_cannons = play_state.cannons

        if not prev_cannons:
            cannon1 = self.cannon_factory.create(paddle.x + 4, paddle.y - 16)
            cannon2 = self.cannon_factory.create(paddle.x + paddle.width - 12, paddle.y - 16)

            play_state.cannons.append(cannon1)
            play_state.cannons.append(cannon2)

        self.in_play = False
