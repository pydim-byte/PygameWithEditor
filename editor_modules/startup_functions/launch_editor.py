from __future__ import annotations
from typing import TYPE_CHECKING, Tuple, Union
if TYPE_CHECKING:
    from ..startup_ui.input_box import InputBox
    from ..startup_ui.ok_box import OKBox
import pygame
from editor_modules.globals import Mode, TilemapData, EditorData
from editor_modules.namings import ModeName
from editor_modules.editor_functions.get_tileset import get_tileset



def launch_editor(input_boxes :list[Union[InputBox, InputBox, InputBox, InputBox, InputBox, InputBox, OKBox]]) -> None:
    data = {"tile width" : None, "tile height" : None, "horizontal tiles" : None, "vertical tiles": None, "tilemap name" : None, "tileset name" : None}
    for box in input_boxes:
        for key, item in data.items():
            if box.data_type == key:
                data[key] = box.user_text

    try:
        width = int(data["tile width"])
        height = int(data["tile height"])
        x = int(data["horizontal tiles"])
        y = int(data["vertical tiles"])
        pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        Mode.NEXT = ModeName.EDITOR
        TilemapData.TILES_WIDTH = width
        TilemapData.TILES_HEIGHT = height
        TilemapData.TILES_X = x
        TilemapData.TILES_Y = y
        EditorData.TILEMAP = data["tilemap name"]
        EditorData.TILESET = data["tileset name"]
        for t in get_tileset(f"assets/tilemap/{EditorData.TILESET}.png"):
            EditorData.TILELIST.append(t)
    except:
        print("Something went wrong")
        return