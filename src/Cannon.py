import pygame

import settings


class Cannon:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y
        self.width = 8
        self.height = 16


        self.texture = settings.TEXTURES["cannon"]
        self.frames = settings.FRAMES["cannon"]

        self.vx = 0

    # def get_collision_rect(self) -> pygame.Rect:
    #     return pygame.Rect(self.x, self.y, self.width, self.height)

    def update(self, dt: float) -> None:
        self.x += self.vx * dt

    def render(self, surface: pygame.Surface) -> None:
        surface.blit(self.texture, (self.x, self.y), self.frames[0])
