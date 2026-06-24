from __future__ import annotations
from typing import TYPE_CHECKING, Tuple, Union
if TYPE_CHECKING:
    from ..startup_ui.input_box import InputBox
    from ..startup_ui.ok_box import OKBox
    from ..startup_ui.results_text import ResultsText
import pygame
from editor_modules.startup_ui.input_box import InputBox
from editor_modules.startup_ui.ok_box import OKBox
from editor_modules.startup_ui.results_text import ResultsText

def get_width_box(w : int, h : int) -> InputBox:
    width_box = InputBox(pos=(2*(w//10) - (w//20), 100),
                         size=(3*(w//10), 1*(h//10)),
                         data_type="tile width")
    width_box.user_text = "4"
    return width_box

def get_height_box(w : int, h : int) -> InputBox:
    height_box = InputBox(pos=(2*(w//10) - (w//20), 240 + 1*(h//10)),
                          size=(3*(w//10), 1*(h//10)),
                          data_type="tile height")
    height_box.user_text = "4"
    return height_box

def get_tile_x_box(w : int, h : int) -> InputBox:
    tile_x_box = InputBox(pos=(5*(w//10) + (w//20), 100),
                          size=(3*(w//10), 1*(h//10)),
                          data_type="horizontal tiles")
    tile_x_box.user_text = "20"
    return tile_x_box

def get_tile_y_box(w : int, h : int) -> InputBox:
    tile_y_box = InputBox(pos=(5*(w//10) + (w//20), 240 + 1*(h//10)),
                          size=(3*(w//10), 1*(h//10)),
                          data_type="vertical tiles")
    tile_y_box.user_text = "15"
    return tile_y_box

def get_tilemap_name(w : int, h : int) -> InputBox:
    tilemap_name = InputBox(pos=(2*(w//10) - (w//20), 480 + 1*(h//10)),
                            size=(3*(w//10), 1*(h//10)),
                            data_type="tilemap name")
    tilemap_name.user_text = "tilemap"
    return tilemap_name

def get_tileset_name(w : int, h : int) -> InputBox:
    tileset_name = InputBox(pos=(5*(w//10) + (w//20), 480 + 1*(h//10)),
                            size=(3*(w//10), 1*(h//10)),
                            data_type="tileset name")
    tileset_name.user_text = "tileset"
    return tileset_name

def get_ok_box(w : int, h : int) -> OKBox:
    ok_box = OKBox(pos=(20, h - 35),
                   size=(w - 40, 30))
    return ok_box

def get_ui() -> Tuple[list[Union[InputBox, InputBox, InputBox, InputBox, InputBox, InputBox, OKBox]], ResultsText]:
    display_size : Tuple[int] = pygame.display.get_surface().get_size()
    w : int = display_size[0]
    h : int = display_size[1]
    width_box = get_width_box(w, h)
    height_box = get_height_box(w, h)
    tile_x_box = get_tile_x_box(w, h)
    tile_y_box = get_tile_y_box(w, h)
    tilemap_name = get_tilemap_name(w, h)
    tileset_name = get_tileset_name(w, h)        
    ok_box = get_ok_box(w, h)
    input_boxes = [width_box, height_box, tile_x_box, tile_y_box, tilemap_name, tileset_name, ok_box]
    result_text = ResultsText(input_boxes)
    return input_boxes, result_text