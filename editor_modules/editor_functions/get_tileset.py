from __future__ import annotations
import pygame
from editor_modules.globals import TilemapData, EditorData
<<<<<<< HEAD
from editor_modules.editor_classes.tileset.tileset_chunk import TilesetChunk
=======
from editor_modules.editor_classes.tileset_chunk import TilesetChunk
>>>>>>> f2364a09e958a98a14037439d03a7513214d2db9



def get_tileset(tileset : str) -> list[TilesetChunk]:
    tileset_chunks : list[TilesetChunk] = []
    tileset_image = pygame.image.load(tileset).convert_alpha()
    EditorData.TILESET_IMAGE = tileset_image
    tiles_rows = tileset_image.get_width() // TilemapData.TILES_WIDTH
    tiles_cols = tileset_image.get_height() // TilemapData.TILES_HEIGHT


    for col in range(tiles_cols):
        for row in range(tiles_rows):
            x = row * TilemapData.TILES_WIDTH
            y = col * TilemapData.TILES_HEIGHT
            image = tileset_image.subsurface(x, y, TilemapData.TILES_WIDTH, TilemapData.TILES_HEIGHT).get_abs_offset()
            tileset_chunks.append(TilesetChunk(pos=(x,y),
                                               size=(TilemapData.TILES_WIDTH, TilemapData.TILES_HEIGHT),
                                               image=image))
    return tileset_chunks