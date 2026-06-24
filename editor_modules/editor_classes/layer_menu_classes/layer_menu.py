from __future__ import annotations
from typing import TYPE_CHECKING, Tuple, Union
import pygame
from editor_modules.editor_classes.base_menus.box_menu import BoxMenu
from .layer_box import LayerBox


class LayerMenu(BoxMenu):
    def __init__(self, pos : Tuple[int, int], size : Tuple[int, int]):
        super().__init__(pos, size)
        self.boxes : list[LayerBox] = []
        self.layer_box_1 = LayerBox(pos=(self.rect.left + 70, self.rect.top + 10),
                                    bounding_points = (self.rect.left, self.rect.right, self.rect.top, self.rect.bottom),
                                    size=(self.rect.width - 90, 40),
                                    boxes=self.boxes)
        self.layer_box_1.working_layer = True
        self.plus_button.action = self.plus_layer
        self.minus_button.action = self.minus_layer

    def plus_layer(self) -> None:
        next_layer = self.boxes[-1].layer + 1
        layer_box = LayerBox(pos=(self.rect.left + 70, self.boxes[-1].rect.bottom + 10),
                                  size=(self.rect.width - 90, 40),
                                  bounding_points = (self.rect.left, self.rect.right, self.rect.top, self.rect.bottom),
                                  boxes=self.boxes)
        layer_box.layer = next_layer

    def minus_layer(self) -> None:
        if len(self.boxes) == 1:
            return
        self.boxes = self.boxes[:-1]

    def draw_viable_boxes(self, screen : pygame.surface.Surface) -> None:
        for b in self.boxes:
            b.rect.move_ip(self.shift)
            b.setting_rect.move_ip(self.shift)
            if not b.valid: 
                continue
            b.draw(screen)
        self.shift = [0, 0]
