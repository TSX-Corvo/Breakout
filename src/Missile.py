import random
from typing import Any, Tuple, Optional
from gale.particle_system import ParticleSystem
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

        def cleanup():
            self.in_play =  False

        self.particle_system = ParticleSystem(
            self.x + 4, 20, 64, cleanup
        )
        self.particle_system.set_life_time(0.4, 0.8)
        self.particle_system.set_linear_acceleration(-0.6, .5, 0.6, 1)
        self.particle_system.set_area_spread(14, 14)

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
        self.particle_system.update(dt)

    def render(self, surface):
        surface.blit(
            self.texture, (self.x, self.y), settings.FRAMES["cannon"][self.frame]
        )
        self.particle_system.render(surface)

    def explode(self) -> None:
        r, g, b = (205, 41, 0)
        self.particle_system.set_colors([(r, g, b, 10), (r, g, b, 50)])
        self.particle_system.generate()
        # self.in_play = False
