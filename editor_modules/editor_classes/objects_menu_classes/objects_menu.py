from __future__ import annotations
from typing import TYPE_CHECKING, Tuple, Union
import pygame
from editor_modules.editor_classes.base_menus.box_menu import BoxMenu
from editor_modules.editor_classes.objects_menu_classes.object_box import ObjectBox
from editor_modules.editor_classes.ui_elements.numbers_display import NumbersDisplay


class ObjectsMenu(BoxMenu):
    def __init__(self, pos : Tuple[int, int], size : Tuple[int, int]):
        super().__init__(pos, size)
        self.object_page = 0
        self.boxes : list[ObjectBox] = []
        self.plus_button.action = self.plus_object
        self.minus_button.action = self.minus_object
        self.up_button.action = self.up_object
        self.down_button.action = self.down_object
        self.numbers_display = NumbersDisplay(pos=(self.down_button.rect.right + 10, self.down_button.rect.y), size=(self.down_button.rect.width*4, self.down_button.rect.height))

    def plus_object(self) -> None:
        objects_box = ObjectBox(pos=(self.rect.left + 30, self.rect.top + 10),
                                size=(self.rect.width - 50, 240),
                                bounding_points = (self.rect.left, self.rect.right, self.rect.top, self.rect.bottom),
                                boxes=self.boxes)
    
    def minus_object(self) -> None:
        if len(self.boxes) == 1:
            return
        self.boxes = self.boxes[:-1]

    def up_object(self) -> None:
        old_page = self.object_page
        self.object_page -= 1
        self.object_page = max(0, self.object_page)
        if old_page != self.object_page:
            for obj in self.boxes:
                for prop in obj.boxes:
                    prop.active = False
        self.boxes[self.object_page].shift = [0, 0]

    def down_object(self) -> None:
        old_page = self.object_page
        self.object_page += 1
        self.object_page = min(len(self.boxes)-1,self.object_page)
        if old_page != self.object_page:
            for obj in self.boxes:
                for prop in obj.boxes:
                    prop.active = False
        self.boxes[self.object_page].shift = [0, 0]

    def draw_viable_boxes(self, screen : pygame.surface.Surface) -> None:
        for b in self.boxes:
            b.rect.move_ip(self.shift)
            b.setting_rect.move_ip(self.shift)
            if not b.valid: 
                continue
            b.draw(screen)
        self.shift = [0, 0]

    def draw_number_display(self, screen : pygame.surface.Surface) -> None:
        self.numbers_display.user_text = f"{self.object_page+1}/{len(self.boxes)}"
        self.numbers_display.draw(screen)

    def draw(self, screen : pygame.surface.Surface) -> None:
        super().draw(screen)
        self.draw_number_display(screen)

