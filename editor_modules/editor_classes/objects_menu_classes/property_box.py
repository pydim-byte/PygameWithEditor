from __future__ import annotations
from typing import TYPE_CHECKING, Tuple, Dict
import pygame
from editor_modules.editor_classes.base_menus.map_data_box import MapDataBox



class PropertyBox(MapDataBox):
    def __init__(self, pos : Tuple[int, int], size : Tuple[int, int], bounding_points : Tuple[int, int, int, int], boxes : list[PropertyBox]):
        self.bounding_points = bounding_points
        self.user_text = ""
        self.pointer : int | None = None
        self.inavtive_background = "grey"
        self.active_background = "white"
        self.inavtive_color = "red"
        self.active_color = "blue"
        super().__init__(pos, size, boxes)
        self.font = pygame.font.Font(None, 16)     
        self.setting_rect.width = 20
        self.setting_rect.right = self.rect.left

    @property
    def valid(self) -> bool:
        within_bounds = {"left" : True, "right" : True, "top" : True, "bottom" : True}
        if self.rect.left < self.bounding_points[0]: within_bounds["left"] = False
        if self.rect.right > self.bounding_points[1] : within_bounds["right"] = False
        if self.rect.top < self.bounding_points[2] : within_bounds["top"] = False
        if self.rect.bottom > self.bounding_points[3] : within_bounds["bottom"] = False
        return all(within_bounds.values())

    def draw_text(self, screen : pygame.surface.Surface) -> None:
        if self.active:
            pointer = self.pointer + 1
            user_text = self.user_text[:pointer] + "|" + self.user_text[pointer:]
        else:
            user_text = self.user_text
        input_text_surface = self.font.render(user_text, True, "black")
        input_text_rect = input_text_surface.get_rect()
        input_text_rect.centery = self.rect.centery
        input_text_rect.left = self.rect.left + 4
        screen.blit(input_text_surface, input_text_rect)





