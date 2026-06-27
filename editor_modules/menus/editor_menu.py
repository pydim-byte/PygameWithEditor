from __future__ import annotations
from typing import TYPE_CHECKING, Tuple, Union
if TYPE_CHECKING:
    from editor_modules.editor_classes.objects_menu_classes.property_box import PropertyBox
    from editor_modules.editor_classes.ui_elements.input_field import InputField
import pygame, os, json
from editor_modules.globals import EditorData
from editor_modules.editor_classes.tilegrid.tilegrid_menu import TilegridMenu
from editor_modules.editor_classes.tileset.tileset_menu import TilesetMenu
from editor_modules.editor_classes.layer_menu_classes.layer_menu import LayerMenu
from editor_modules.editor_classes.objects_menu_classes.objects_menu import ObjectsMenu
from editor_modules.editor_functions.tilemap_saver import TilemapSaver
from editor_modules.editor_functions.tilemap_loader import TilemapLoader
from editor_modules.editor_functions.get_active_rect import get_active_rect
from editor_modules.editor_functions.get_tileset import get_tileset
from editor_modules.editor_functions.visualize_property import visualize_property


class EditorMenu():
    def __init__(self):
        display_size : Tuple[int, int] = pygame.display.get_surface().get_size()
        W : int = display_size[0]
        H : int = display_size[1]
        self.tilegrid_menu = TilegridMenu(
                             pos=(0, 0),
                             size=(6*(W//10), H - 39))
        self.tilegrid_menu.save_button.action = TilemapSaver(self)
        self.tilegrid_menu.load_button.action = TilemapLoader(self)
        self.tileset_menu = TilesetMenu(
                            pos=(6*(W//10), 0),
                            size=(4*(W//10), H//3 - 39))
        self.tileset_menu.update_button.action = self.update_tileset
        self.layer_menu = LayerMenu(
                            pos=(6*(W//10), H//3),
                            size=(4*(W//10), H//3 - 39))
        self.objects_menu = ObjectsMenu(
                            pos=(6*(W//10), H - H//3),
                            size=(4*(W//10), H//3 - 39))
        self.buttons = self.tileset_menu.buttons + self.tilegrid_menu.buttons
        self.active_menu = self.tilegrid_menu
        TilemapLoader(self)()
    
    @property
    def working_layer(self) -> int | None:
        for b in self.layer_menu.boxes:
            if b.working_layer:
                return b.layer
        return None

    @property
    def active_propery_box(self) -> PropertyBox | None:
        for b in self.objects_menu.boxes:
            for p in b.boxes:
                if p.active:
                    return p
        return None

    @property
    def active_input_filed(self) -> InputField | None:  
        if self.tilegrid_menu.input_field.active:
            return self.tilegrid_menu.input_field
        elif self.tileset_menu.input_field.active:
            return self.tileset_menu.input_field
        return None

    def update_tileset(self) -> None: 
        if os.path.isfile(f"assets/tilemap/{self.tileset_menu.input_field.user_text}.png"):
            for i, t in enumerate(get_tileset(f"assets/tilemap/{self.tileset_menu.input_field.user_text}.png")):
                EditorData.TILELIST[i] = t

    def hanlde_inputs(self, inputs : pygame.event.Event) -> None:
        if inputs.type == pygame.MOUSEBUTTONDOWN:
            get_active_rect(inputs.pos, self)
        active_input_object : InputField | PropertyBox | None = None
        if self.active_input_filed and not self.active_propery_box:
            active_input_object = self.active_input_filed
        elif self.active_propery_box:
            active_input_object = self.active_propery_box
        if active_input_object:
            if active_input_object.pointer is None:
                active_input_object.pointer = len(active_input_object.user_text) - 1
            if inputs.type == pygame.KEYDOWN:
                if inputs.key == pygame.K_LEFT:
                    active_input_object.pointer -= 1
                    active_input_object.pointer = max(0, active_input_object.pointer)
                if inputs.key == pygame.K_RIGHT:
                    active_input_object.pointer += 1
                    active_input_object.pointer = min(len(active_input_object.user_text) - 1, active_input_object.pointer)
                if inputs.key == pygame.K_BACKSPACE:
                    if active_input_object.pointer == len(active_input_object.user_text) - 1:
                        active_input_object.user_text = active_input_object.user_text[:-1]
                        active_input_object.pointer = len(active_input_object.user_text) - 1
                    else:
                        active_input_object.user_text = active_input_object.user_text[:active_input_object.pointer] + active_input_object.user_text[active_input_object.pointer+1:]
                        active_input_object.pointer -= 1
                        active_input_object.pointer = max(0, active_input_object.pointer)
                else:
                    if active_input_object.pointer == len(active_input_object.user_text) - 1:
                        active_input_object.user_text += inputs.unicode
                        active_input_object.pointer = len(active_input_object.user_text) - 1
                    else:
                        active_input_object.user_text = active_input_object.user_text[:active_input_object.pointer+1] + inputs.unicode + active_input_object.user_text[active_input_object.pointer+1:]
                        if inputs.unicode:
                            active_input_object.pointer += 1

        if self.active_propery_box or self.active_input_filed:
            pygame.key.set_repeat(99999)
            return
        else:
            pygame.key.set_repeat(100)

        if inputs.type == pygame.KEYDOWN:
            if inputs.key == pygame.K_s:
                TilemapSaver(self)()
            if inputs.key == pygame.K_l:
                TilemapLoader(self)()
            if inputs.key == pygame.K_u:
                self.update_tileset()
            if inputs.key == pygame.K_EQUALS:
                self.active_menu.plus_button.action()
            if inputs.key == pygame.K_MINUS:
                self.active_menu.minus_button.action()
            if inputs.key == pygame.K_LEFT:
                self.active_menu.left_button.action()
            if inputs.key == pygame.K_RIGHT:
                self.active_menu.right_button.action()
            if inputs.key == pygame.K_UP:
                self.active_menu.up_button.action()
            if inputs.key == pygame.K_DOWN:
                self.active_menu.down_button.action()
            
    def update(self) -> None:
        for t in self.tilegrid_menu.tiles:
            t.top_layer = self.layer_menu.boxes[-1].layer

    def draw(self, screen : pygame.surface.Surface) -> None:
        self.tileset_menu.draw(screen)
        self.tilegrid_menu.draw(screen)
        self.layer_menu.draw(screen)
        self.objects_menu.draw(screen)

        for b in self.objects_menu.boxes:
            if len(b.boxes) < 2:
                return
            color_propery_data = b.boxes[0].user_text
            rect_propery_data = b.boxes[1].user_text
            visualize_property(color_propery_data,
                               rect_propery_data,
                               self.tilegrid_menu.scale,
                               self.tilegrid_menu.shift,
                               screen)

