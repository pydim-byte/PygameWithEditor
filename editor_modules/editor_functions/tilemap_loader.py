from __future__ import annotations
from typing import TYPE_CHECKING, Tuple, Dict
if TYPE_CHECKING:
    from editor_modules.menus.editor_menu import EditorMenu
import os, json
    

class TilemapLoader:
    def __init__(self, editor_data : EditorMenu):
        self.editor_data = editor_data

    def __call__(self):
        if not os.path.isfile(f"assets/tilemap/{self.editor_data.tilegrid_menu.input_field.user_text}.json"):
            return
        with open(f"assets/tilemap/{self.editor_data.tilegrid_menu.input_field.user_text}.json", 'r') as file:
            data = json.load(file)

        for old_tile in self.editor_data.tilegrid_menu.tiles:
            old_tile.images.clear()
 
        for tile in (data["tiles"]):
            new_tile_x = data["tiles"][tile]["pos_x"]
            new_tile_y = data["tiles"][tile]["pos_y"]
            for old_tile in self.editor_data.tilegrid_menu.tiles:
                if old_tile.origin_pos != (new_tile_x, new_tile_y):  
                    continue
                tile_images = old_tile.images
                old_tile.top_layer = data["tiles"][tile]["top_layer"]
                while len(self.editor_data.layer_menu.boxes) < data["tiles"][tile]["top_layer"]:
                    self.editor_data.layer_menu.plus_layer()
                while len(self.editor_data.layer_menu.boxes) > data["tiles"][tile]["top_layer"]:
                    self.editor_data.layer_menu.minus_layer()
                for layer in data["tiles"][tile]["layers_data"]:
                    tile_layer = {int(layer[-1]) :
                                    (data["tiles"][tile]["layers_data"][layer]["pos_x"],
                                    data["tiles"][tile]["layers_data"][layer]["pos_y"])}
                    tile_images.update(tile_layer)
        tilemap_path = data["tileset_name"].split("/")
        self.editor_data.tileset_menu.input_field.user_text = tilemap_path[-1]
        self.editor_data.update_tileset()

        while len(self.editor_data.objects_menu.boxes) < len(data["objects"]):
            self.editor_data.objects_menu.plus_object()
        while len(self.editor_data.objects_menu.boxes) > len(data["objects"]):
            self.editor_data.objects_menu.minus_object()
        for i, obj in enumerate(data["objects"]):
            obj_properties = self.editor_data.objects_menu.boxes[i].boxes

            if len(data["objects"][obj]) < 2:
                continue

            while len(obj_properties) < len(data["objects"][obj]):
                self.editor_data.objects_menu.boxes[i].plus_layer()
            while len(obj_properties) > len(data["objects"][obj]):
                self.editor_data.objects_menu.boxes[i].minus_layer()

            for j, new_prop in enumerate(data["objects"][obj]):
                obj_properties[j].user_text = f'''{new_prop}___{data["objects"][obj][new_prop]}'''