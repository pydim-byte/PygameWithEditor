import pygame
from typing import Tuple


class OKBox:
    def __init__(self, pos : Tuple[int], size : Tuple[int]):
        self.data_type = None
        self.font = pygame.font.Font(None, 36)
        self.text : str = 'OK'
        self.rect = pygame.Rect(pos[0], pos[1], size[0], size[1])
        self.color : Tuple[int] = (200,200,200)

    def draw_bounding_box(self, screen : pygame.surface.Surface) -> None:
        pygame.draw.rect(screen, self.color, self.rect)
        pygame.draw.rect(screen, "black", self.rect, width=1)

    def draw_ok_text(self, screen : pygame.surface.Surface) -> None:
        ok_text = self.font.render(self.text, True, "black")
        ok_text_rect = ok_text.get_rect()
        ok_text_rect.center = self.rect.center
        screen.blit(ok_text, ok_text_rect)

    def draw(self, screen : pygame.surface.Surface) -> None:
        self.draw_bounding_box(screen)
        self.draw_ok_text(screen)

