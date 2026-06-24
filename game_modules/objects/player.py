import pygame
from ..globals import GameScreen, PlayerStats
<<<<<<< HEAD
from .dynamic_object import DynamicObject


class Player(DynamicObject):

    def __init__(self, pos : pygame.Vector2 , images : list[pygame.surface.Surface]):
        super().__init__(pos, images)
        self.type : str = 'player'
        self.speed = PlayerStats.PLAYER_MOVEMENT_SPEED

    def fixed_update(self) -> None:
        self.rect.clamp_ip(0, 0, GameScreen.SCREEN_WIDTH, GameScreen.SCREEN_HEIGHT)
        super().fixed_update()

=======


class Player(pygame.sprite.Sprite):
    def __init__(self,pos : pygame.Vector2 ,images : list[pygame.surface.Surface]):
        super().__init__()
        self.type : str = 'player'
        self.images : list[pygame.surface.Surface] = images
        self.image : pygame.surface.Surface = self.images[0]
        self.rect = self.image.get_rect(topleft = pos)

        self.pos : pygame.Vector2 = pos
        self.prev_pos : pygame.Vector2 = self.pos.copy()
        self.direction = pygame.Vector2(0,0)
        self.movement_direction = pygame.Vector2(0,0)
        self.vel = pygame.Vector2(0,0)

    def set_direction(self,direction : int) -> None:
        self.movement_direction.xy = direction.xy

    def calculate_velocity(self) -> None:
        self.direction.xy = self.movement_direction.xy
        self.vel.xy = self.direction.xy * PlayerStats.PLAYER_MOVEMENT_SPEED

    def fixed_update(self) -> None:
        self.rect.clamp_ip(0, 0, GameScreen.SCREEN_WIDTH, GameScreen.SCREEN_HEIGHT)
        self.pos.xy = self.rect.topleft
        self.prev_pos.xy = self.pos.xy

>>>>>>> f2364a09e958a98a14037439d03a7513214d2db9
    def update(self, dt : float) -> None:
        pass

    def draw(self,surf : pygame.surface.Surface, alpha : float) -> None:
        alpha_pos = self.pos * alpha + self.prev_pos * (1 - alpha)
        draw_rect = self.rect.copy()
        draw_rect.topleft = alpha_pos
        surf.blit(self.image,draw_rect)


    