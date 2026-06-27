from __future__ import annotations
from typing import TYPE_CHECKING, Tuple, Dict
if TYPE_CHECKING:
    from editor_modules.menus.editor_menu import EditorMenu
import pygame
from editor_modules.editor_classes.tileset.tileset_chunk import TilesetChunk
from editor_modules.editor_classes.tilegrid.tile import Tile
from editor_modules.namings import MenuName
from editor_modules.editor_classes.ui_elements.size_buttons import BaseButton
from editor_modules.editor_classes.layer_menu_classes.layer_box import LayerBox
from editor_modules.editor_classes.objects_menu_classes.property_box import PropertyBox
from editor_modules.editor_classes.ui_elements.input_field import InputField


def get_active_rect(mouse_pos, editor : EditorMenu) -> None:
    if mouse_pos[0] < editor.tilegrid_menu.rect.right:
        editor.active_menu = editor.tilegrid_menu
    else:
        editor.active_menu = editor.tileset_menu
    rects : list = []
    rects.extend(editor.tileset_menu.buttons) 
    for t in editor.tileset_menu.tiles:
        if t.valid: rects.append(t)
    rects.extend(editor.tilegrid_menu.buttons)
    for t in editor.tilegrid_menu.tiles:
        if t.valid: rects.append(t)
    for b in editor.layer_menu.boxes:
        if b.valid: rects.append(b)
    rects.extend(editor.layer_menu.buttons)
    rects.extend(editor.objects_menu.buttons)
    if editor.objects_menu.boxes:
        rects.extend(editor.objects_menu.boxes[0].buttons)
        for b in editor.objects_menu.boxes[0].boxes:
            if b.valid: rects.append(b)
    rects.append(editor.tileset_menu.input_field)
    rects.append(editor.tilegrid_menu.input_field)
    for r in rects:
        if isinstance(r, TilesetChunk):
            if r.rect.collidepoint(mouse_pos):
                editor.tileset_menu.active_tile_img_ref = r.get_image()
                print(editor.tileset_menu.active_tile_img_ref)
            continue
        if isinstance(r, Tile):
            if r.rect.collidepoint(mouse_pos) and editor.tileset_menu.active_tile_img_ref:
                r.images[editor.working_layer] = (editor.tileset_menu.active_tile_img_ref[0][0], editor.tileset_menu.active_tile_img_ref[0][1])
            continue
        if isinstance(r, LayerBox):
            if r.rect.collidepoint(mouse_pos):
                for box in editor.layer_menu.boxes:
                    if box.layer == r.layer:
                        r_box = box
                r_box.working_layer = not r_box.working_layer
                for b in editor.layer_menu.boxes:
                    if b != r_box:
                        b.working_layer = False
            continue
        if isinstance(r, PropertyBox):
            if r.rect:
                if r.rect.collidepoint(mouse_pos):
                    r.active = not r.active
                    for obj in editor.objects_menu.boxes:
                        for prop in obj.boxes:
                            if prop != r:
                                prop.active = False
                            if prop.active == False:
                                prop.pointer = None
            continue
        if isinstance(r, InputField):
            if r.rect.collidepoint(mouse_pos):
                r.active = not r.active
                r.pointer = len(r.user_text) - 1
                if r == editor.tileset_menu.input_field:
                    editor.tilegrid_menu.input_field.active = False
                else:
                    editor.tileset_menu.input_field.active = False
            continue 
        if isinstance(r, BaseButton):
            if r.rect.collidepoint(mouse_pos):
                r.action()