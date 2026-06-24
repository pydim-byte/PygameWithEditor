from __future__ import annotations
from typing import TYPE_CHECKING, Tuple, Union
import pygame
from ..ui_elements.size_buttons import BaseButton, PlusButton, MinusButton, UpButton, DownButton


class BoxMenu():
    def __init__(self, pos : Tuple[int, int], size : Tuple[int, int]):
        self.scale = 1
        self.shift = [0,0]
        self.rect = pygame.Rect(pos[0], pos[1], size[0], size[1])
        self.setting_rect = pygame.Rect(self.rect[0], self.rect[1], self.rect[2], 40)
        self.setting_rect.top = self.rect.bottom - 1

        self.boxes = []
        self.buttons : list[BaseButton] = []
        self.plus_button = PlusButton(pos=(self.setting_rect.left + 10, self.setting_rect.centery), menu=self)
        self.minus_button = MinusButton(pos=(self.plus_button.rect.right + 10, self.setting_rect.centery), menu=self)
        self.up_button = UpButton(pos=(self.minus_button.rect.right + 10, self.setting_rect.centery), menu=self)
        self.down_button = DownButton(pos=(self.up_button.rect.right + 10, self.setting_rect.centery), menu=self)

    def draw_bounding_box(self, screen : pygame.surface.Surface) -> None:
        pygame.draw.rect(screen, "grey", self.rect)
        pygame.draw.rect(screen, "black", self.rect, width=1)

    def draw_underlying_rect(self, screen : pygame.surface.Surface) -> None:
        pygame.draw.rect(screen, (50, 50, 255), self.setting_rect)
        pygame.draw.rect(screen, "black", self.setting_rect, width=1)

    def draw_viable_boxes(self, screen : pygame.surface.Surface) -> None:
        pass

    def draw(self, screen : pygame.surface.Surface) -> None:
        self.draw_bounding_box(screen)
        self.draw_underlying_rect(screen)
        self.draw_viable_boxes(screen)
        for b in self.buttons: b.draw(screen)
        