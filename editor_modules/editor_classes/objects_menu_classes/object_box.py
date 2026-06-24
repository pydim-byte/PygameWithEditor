from __future__ import annotations
from typing import TYPE_CHECKING, Tuple, Dict, Union
import pygame
from editor_modules.editor_classes.base_menus.box_menu import BoxMenu
from editor_modules.editor_classes.objects_menu_classes.property_box import PropertyBox
from editor_modules.editor_classes.objects_menu_classes.property_box import PropertyBox


class ObjectBox(BoxMenu):
    def __init__(self, pos : Tuple[int, int], size : Tuple[int, int], bounding_points : Tuple[int, int, int, int], boxes : list[ObjectBox]):
        super().__init__(pos, size)
        self.bounding_points = bounding_points
        self.boxes : list[PropertyBox] = []
        self.box_1 = PropertyBox(
                              pos=(self.rect.left + 40, self.rect.top + 10),
                              size=(self.rect.width - 60, 20),
                              bounding_points = (self.rect.left, self.rect.right, self.rect.top, self.rect.bottom),
                              boxes=self.boxes)
        self.box_1.user_text = "color___"
        self.box_2 = PropertyBox(
                              pos=(self.rect.left + 40, self.box_1.rect.bottom + 10),
                              size=(self.rect.width - 60, 20),
                              bounding_points = (self.rect.left, self.rect.right, self.rect.top, self.rect.bottom),
                              boxes=self.boxes)
        self.box_2.user_text = "rect___"
        self.box_3 = PropertyBox(
                              pos=(self.rect.left + 40, self.box_2.rect.bottom + 10),
                              size=(self.rect.width - 60, 20),
                              bounding_points = (self.rect.left, self.rect.right, self.rect.top, self.rect.bottom),
                              boxes=self.boxes)
        self.box_3.user_text = "type___"
        self.plus_button.action = self.plus_property
        self.minus_button.action = self.minus_property
        self.up_button.action = self.scroll_up
        self.down_button.action = self.scroll_down
        boxes.append(self)

    def plus_property(self) -> None:
        propery_box = PropertyBox(
                      pos=(self.rect.left + 40, self.boxes[-1].rect.bottom + 10),
                      size=(self.rect.width - 60, 20),
                      bounding_points = (self.rect.left, self.rect.right, self.rect.top, self.rect.bottom),
                      boxes=self.boxes)
    
    def minus_property(self) -> None:
        if len(self.boxes) == 3:
            return
        self.boxes = self.boxes[:-1]

    def scroll_up(self) -> None:
        self.shift[1] -= 20

    def scroll_down(self) -> None:
        self.shift[1] += 20

    def serialize(self) -> Dict[str, str]:
        property_dict : Dict[str, str] = {}
        for prop in self.boxes:
            prop_text = prop.user_text.split("___")
            if len(prop_text) < 2 or prop_text[1] == str(): 
                continue
            property_dict[prop_text[0]] = prop_text[1]
        return property_dict
    
    @property
    def valid(self) -> bool:
        within_bounds = {"left" : True, "right" : True, "top" : True, "bottom" : True}
        if self.rect.left < self.bounding_points[0]: within_bounds["left"] = False
        if self.rect.right > self.bounding_points[1] : within_bounds["right"] = False
        if self.rect.top < self.bounding_points[2] : within_bounds["top"] = False
        if self.rect.bottom > self.bounding_points[3] : within_bounds["bottom"] = False
        return all(within_bounds.values())

    def draw_viable_boxes(self, screen):
        for b in self.boxes:
            b.rect.move_ip(self.shift)
            b.setting_rect.move_ip(self.shift)
            if not b.valid: 
                continue
            b.draw(screen)
        self.shift = [0, 0]
