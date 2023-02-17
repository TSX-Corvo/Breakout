"""
ISPPJ1 2023
Study Case: Breakout

Author: Alejandro Mujica
alejandro.j.mujic4@gmail.com

This file contains the specialization of PowerUp, StickyBall.
"""
from typing import TypeVar
from gale.timer import Timer

import settings
from src.powerups.PowerUp import PowerUp


class StickyBall(PowerUp):
    """
    Power-up to add the sticky behavior to the ball.
    """

    def __init__(self, x: int, y: int) -> None:
        super().__init__(x, y, 4)

    def take(self, play_state: TypeVar("PlayState")) -> None:
        play_state.flags['sticky_ball_active'] = True
        balls = play_state.balls

        for ball in balls:
            ball.sticky = True
        
        def cleanup():
            for ball in balls:
                ball.sticky = False
            play_state.flags['sticky_ball_active'] = False
            

        Timer.after(settings.STICKY_BALL_DURATION, cleanup)

        self.in_play = False
