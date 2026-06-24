from __future__ import annotations
from typing import TYPE_CHECKING, Tuple, Dict
if TYPE_CHECKING:
    from editor_modules.editor_classes.base_menus.box_menu import BoxMenu
import pygame


class MapDataBox():
    def __init__(self, pos : Tuple[int, int], size : Tuple[int, int], boxes : list[MapDataBox]):
        self.active = False
        self.font = pygame.font.Font(None, 42)        
        self.rect = pygame.Rect(pos[0], pos[1], size[0], size[1])
        self.setting_rect = pygame.Rect(self.rect[0], self.rect[1], 40, self.rect[3])
        self.setting_rect.right = self.rect.left + 1
        self.inavtive_background = "grey"
        self.active_background = "white"
        self.inavtive_color = "red"
        self.active_color = "blue"
        boxes.append(self)

    @property
    def background_color(self) -> pygame.color.Color:
        return self.active_background if self.active else self.inavtive_background
    
    @property
    def settings_color(self) -> pygame.color.Color:
        return  self.active_color if self.active else self.inavtive_color

    def draw_bounding_box(self, screen : pygame.surface.Surface) -> None:
        pygame.draw.rect(screen, self.background_color, self.rect)
        pygame.draw.rect(screen, "black", self.rect, width=1)

    def draw_settings_box(self, screen : pygame.surface.Surface) -> None:
        pygame.draw.rect(screen, self.settings_color, self.setting_rect)
        pygame.draw.rect(screen, "black", self.setting_rect, width=1)

    def draw_text(self, screen : pygame.surface.Surface) -> None:
        pass

    def draw(self, screen : pygame.surface.Surface) -> None:
        self.draw_bounding_box(screen)
        self.draw_settings_box(screen)
        self.draw_text(screen)






