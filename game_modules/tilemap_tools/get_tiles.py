from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from ..tilemap import Tilemap
import pygame, json
from ..objects.tile import Tile
from ..objects.player import Player
from ..globals import TilesProperties
from .get_images import get_images


def get_tiles(tilemap : Tilemap) -> None:
    with open(f'assets/tilemap/{tilemap.tilemap_name}.json', 'r') as file:
        data : dict = json.load(file)
    tileset : pygame.surface.Surface = pygame.image.load(f"{data["tileset_name"]}.png").convert_alpha()

    for tile in (data["tiles"]):
        tile_x : int = data["tiles"][tile]["pos_x"]
        tile_y : int = data["tiles"][tile]["pos_y"]
        tile_pos = pygame.Vector2(tile_x, tile_y)
        tile_suft = pygame.surface.Surface((TilesProperties.TILE_SIZE, TilesProperties.TILE_SIZE))
        for layer in data["tiles"][tile]["layers_data"]:
            layer_img_pos : list[int] = (data["tiles"][tile]["layers_data"][layer]["pos_x"], data["tiles"][tile]["layers_data"][layer]["pos_y"])
            layer_img : pygame.surface.Surface = tileset.subsurface(layer_img_pos, (TilesProperties.TILE_SIZE, TilesProperties.TILE_SIZE))
            tile_suft.blit(layer_img, (0,0))
        tile : pygame.sprite.Sprite = Tile(tile_pos, tile_suft)
        tilemap.visible_tiles.add(tile)

    
    # Here should be tile OBJECTS loading logic
    for obj in data["objects"]:
        if data["objects"][obj]["type"] == "player":
            rect_values_str : str = data["objects"][obj]["rect"].split(",")
            rect_values : list[int] = []
            for i, value in enumerate(rect_values_str):
                rect_values.append(int(value))
            x, y, w, h = rect_values
            pos = pygame.Vector2(x, y)
            img : list[pygame.surface.Surface] = get_images(data["objects"][obj]["type"], 1)
            player : pygame.sprite.Sprite = Player(pos, img)
            tilemap.player.add(player)
