"""
ISPPJ1 2023
Study Case: Breakout

Author: Alejandro Mujica
alejandro.j.mujic4@gmail.com

This file contains the specialization of PowerUp, StickyBall.
"""
from typing import TypeVar
from src.powerups.PowerUp import PowerUp


class StickyBall(PowerUp):
    """
    Power-up to add the sticky behavior to the ball.
    """

    def __init__(self, x: int, y: int) -> None:
        super().__init__(x, y, 4)

    def take(self, play_state: TypeVar("PlayState")) -> None:
        balls = play_state.balls

        for ball in balls:
            ball.sticky = True        

        self.in_play = False
