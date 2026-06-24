<<<<<<< HEAD:editor_modules/editor_classes/tilegrid/tile.py
from __future__ import annotations
from typing import TYPE_CHECKING, Tuple, Dict
=======
>>>>>>> f2364a09e958a98a14037439d03a7513214d2db9:editor_modules/editor_classes/tile.py
import pygame
from editor_modules.globals import TilemapData, EditorData


class Tile():
    def __init__(self, pos : Tuple[int, int], size : Tuple[int, int]):
        self.origin_pos = pos
        self.rect = pygame.Rect(pos[0], pos[1], size[0], size[1])
        self.images : Dict[int, Tuple[int, int]] = {}
        self.top_layer = 1
        self.valid = True

    def serialize(self) -> dict[str, any]:
        tile_data : dict[str, any] = {}
        if not self.images:
            return
        pos_x = self.origin_pos[0]
        pos_y = self.origin_pos[1]

        images = list(self.images.items())
        images = sorted(images, key=lambda x:x[0])
        images = [i for i in images if i[0]<=self.top_layer]

        tile_data["pos_x"] = pos_x
        tile_data["pos_y"] = pos_y
        tile_data["top_layer"] = self.top_layer
        layers_data : dict[str, dict[str, int]] = {}
        for layer, img in images:
            layers_data.update({f"layer_{layer}" : {"pos_x" : img[0], "pos_y" : img[1]}})
        tile_data.update({"layers_data" : layers_data})
        return tile_data

    def get_image(self) -> list[Tuple[int, int]]:
        refs_to_images : list[Tuple[int, int]] = []
        if self.images:
            images = list(self.images.items())
            images = sorted(images, key=lambda x:x[0])
            images = [i for i in images if i[0]<=self.top_layer]
<<<<<<< HEAD:editor_modules/editor_classes/tilegrid/tile.py
            for image_ref in images:
                refs_to_images.append((image_ref[1][0], image_ref[1][1]))
        return refs_to_images
=======
            for image in images:
                tmp_image = EditorData.TILESET_IMAGE.subsurface(image[1][0], image[1][1], TilemapData.TILES_WIDTH, TilemapData.TILES_HEIGHT)
                img.blit(pygame.transform.scale(tmp_image, (self.rect.width, self.rect.height)), (0,0))
        return img
>>>>>>> f2364a09e958a98a14037439d03a7513214d2db9:editor_modules/editor_classes/tile.py
           