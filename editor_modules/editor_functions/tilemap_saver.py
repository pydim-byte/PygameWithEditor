from __future__ import annotations
from typing import TYPE_CHECKING, Tuple, Dict
if TYPE_CHECKING:
    from editor_modules.menus.editor_menu import EditorMenu
import json
    

class TilemapSaver:
    def __init__(self, editor_data : EditorMenu):
        self.editor_data = editor_data

    def __call__(self):
        data_to_json = {
            "tileset_name" : f"assets/tilemap/{self.editor_data.tileset_menu.input_field.user_text}",
            "tiles" : {},
            "objects" : {}
        }
        tile_id = 0
        object_id = 0
        for tile in self.editor_data.tilegrid_menu.tiles:
            tile_data = (tile.serialize())
            if not tile_data:
                continue
            data_to_json["tiles"][f"tile_{tile_id}"] = tile_data
            tile_id += 1
        for obj in self.editor_data.objects_menu.boxes:
            obj_data = obj.serialize()
            if not obj_data:
                continue
            data_to_json["objects"][f"object_{object_id}"] = obj_data
            object_id += 1
        with open(f"assets/tilemap/{self.editor_data.tilegrid_menu.input_field.user_text}.json", "w") as write:
            json.dump(data_to_json, write, indent=4)