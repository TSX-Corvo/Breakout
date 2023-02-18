import random
from typing import Any, Tuple, Optional

import pygame

import settings
from src.Paddle import Paddle


class Missile:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y
        self.width = 8
        self.height = 16

        self.vx = 0
        self.vy = -settings.MISSILE_SPEED

        self.texture = settings.TEXTURES["cannon"]
        self.frame = 1
        self.in_play = True

    def get_collision_rect(self) -> pygame.Rect:
        return pygame.Rect(self.x, self.y, self.width, self.height)

    def solve_world_boundaries(self) -> None:
        r = self.get_collision_rect()

        if r.top < 0:
            #destroy missile
            self.explode()
       

    def collides(self, another: Any) -> bool:
        return self.get_collision_rect().colliderect(another.get_collision_rect())

    def update(self, dt: float) -> None:        
        self.y += self.vy * dt

    def render(self, surface):
        surface.blit(
            self.texture, (self.x, self.y), settings.FRAMES["cannon"][self.frame]
        )

    def explode(self) -> None:
        self.in_play = False
