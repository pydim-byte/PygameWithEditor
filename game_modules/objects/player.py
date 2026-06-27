import pygame
from ..globals import GameScreen, PlayerStats
from .dynamic_object import DynamicObject


class Player(DynamicObject):

    def __init__(self, pos : pygame.Vector2 , images : list[pygame.surface.Surface]):
        super().__init__(pos, images)
        self.type : str = 'player'
        self.speed = PlayerStats.PLAYER_MOVEMENT_SPEED

    def fixed_update(self) -> None:
        self.rect.clamp_ip(0, 0, GameScreen.SCREEN_WIDTH, GameScreen.SCREEN_HEIGHT)
        super().fixed_update()

    def update(self, dt : float) -> None:
        pass

    def draw(self,surf : pygame.surface.Surface, alpha : float) -> None:
        alpha_pos = self.pos * alpha + self.prev_pos * (1 - alpha)
        draw_rect = self.rect.copy()
        draw_rect.topleft = alpha_pos
        surf.blit(self.image,draw_rect)


    