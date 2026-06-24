import pygame
from ..globals import GameScreen, PlayerStats


class DynamicObject(pygame.sprite.Sprite):
    def __init__(self,pos : pygame.Vector2 ,images : list[pygame.surface.Surface]):
        super().__init__()
        self.images : list[pygame.surface.Surface] = images
        self.image : pygame.surface.Surface = self.images[0]
        self.rect = self.image.get_rect(topleft = pos)

        self.pos : pygame.Vector2 = pos
        self.prev_pos : pygame.Vector2 = self.pos.copy()
        self.direction = pygame.Vector2(0,0)
        self.movement_direction = pygame.Vector2(0,0)
        self.vel = pygame.Vector2(0,0)
        self.speed = 1

    def set_direction(self,direction : pygame.Vector2) -> None:
        self.movement_direction.xy = direction.xy

    def calculate_velocity(self) -> None:
        self.direction.xy = self.movement_direction.xy
        self.vel.xy = self.direction.xy * self.speed

    def fixed_update(self) -> None:
        self.pos.xy = self.rect.topleft
        self.prev_pos.xy = self.pos.xy



    