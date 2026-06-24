from __future__ import annotations
from typing import TYPE_CHECKING, Tuple, Dict
from editor_modules.editor_classes.base_menus.map_data_box import MapDataBox
import pygame


class LayerBox(MapDataBox):
    def __init__(self, pos : Tuple[int, int], size : Tuple[int, int], bounding_points : Tuple[int, int, int, int], boxes : list[LayerBox]):
        self.bounding_points = bounding_points
        self.working_layer = False
        self.layer = 1
        super().__init__(pos, size, boxes)
    
    @property
    def valid(self) -> bool:
        within_bounds = {"left" : True, "right" : True, "top" : True, "bottom" : True}
        if self.rect.left < self.bounding_points[0]: within_bounds["left"] = False
        if self.rect.right > self.bounding_points[1] : within_bounds["right"] = False
        if self.rect.top < self.bounding_points[2] : within_bounds["top"] = False
        if self.rect.bottom > self.bounding_points[3] : within_bounds["bottom"] = False
        return all(within_bounds.values())

    @property
    def background_color(self) -> pygame.color.Color:
        return self.active_background if self.working_layer else self.inavtive_background

    @property
    def settings_color(self) -> pygame.color.Color:
        return  self.active_color if self.working_layer else self.inavtive_color

    def draw_text(self, screen : pygame.surface.Surface) -> None:
        input_text_surface = self.font.render(f"{self.layer}", True, "black")
        input_text_rect = input_text_surface.get_rect()
        input_text_rect.centery = self.rect.centery
        input_text_rect.left = self.rect.left + 4
        screen.blit(input_text_surface, input_text_rect)






