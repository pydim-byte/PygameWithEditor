from __future__ import annotations
from typing import TYPE_CHECKING, Tuple, Dict
import pygame


class NumbersDisplay():
    def __init__(self, pos : Tuple[int, int], size : Tuple[int, int]):
        self.font = pygame.font.Font(None, 16)
        self.user_text : str = ""
        self.rect = pygame.Rect(pos[0], pos[1], size[0], size[1])
        self.background_color = "grey"

    def draw_bounding_box(self, screen : pygame.surface.Surface) -> None:
        pygame.draw.rect(screen, self.background_color, self.rect)
        pygame.draw.rect(screen, "black", self.rect, width=1)

    def draw_layers_amount_text(self, screen : pygame.surface.Surface) -> None:
        input_text_surface = self.font.render(self.user_text, True, "black")
        input_text_rect = input_text_surface.get_rect()
        input_text_rect.centery = self.rect.centery
        input_text_rect.left = self.rect.left + 4
        screen.blit(input_text_surface, input_text_rect)


    def draw(self, screen : pygame.surface.Surface):
        self.draw_bounding_box(screen)
        self.draw_layers_amount_text(screen)



