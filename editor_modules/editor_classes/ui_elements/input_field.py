from __future__ import annotations
from typing import TYPE_CHECKING, Tuple, Dict
import pygame


class InputField():
    def __init__(self, pos : Tuple[int, int], size : Tuple[int, int]):
        self.active = False
        self.font = pygame.font.Font(None, 16)
        self.user_text : str = ""
        self.pointer : int = None
        self.rect = pygame.Rect(pos[0], pos[1], size[0], size[1])
        self.collision_rect = None
        self.inavtive_background : str = "grey"
        self.active_background : str = "white"

    def draw_bounding_box(self, screen : pygame.surface.Surface) -> None:
        background_color = self.active_background if self.active else self.inavtive_background
        pygame.draw.rect(screen, background_color, self.rect)
        pygame.draw.rect(screen, "black", self.rect, width=1)

    def get_user_text(self) -> str:
        user_text = self.user_text
        if self.pointer is not None:
            pointer = self.pointer + 1
        if self.active and self.pointer is not None:
            user_text = self.user_text[:pointer] + "|" + self.user_text[pointer:]
        else:
            user_text = self.user_text
        return user_text

    def draw_user_text(self, screen : pygame.surface.Surface) -> None:
        user_text = self.get_user_text()
        input_text_surface = self.font.render(user_text, True, "black")
        input_text_rect = input_text_surface.get_rect()
        input_text_rect.centery = self.rect.centery
        input_text_rect.left = self.rect.left + 4
        screen.blit(input_text_surface, input_text_rect)

    def draw(self, screen : pygame.surface.Surface) -> None:
        self.draw_bounding_box(screen)
        self.draw_user_text(screen)


