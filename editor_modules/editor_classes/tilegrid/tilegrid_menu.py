from __future__ import annotations
from typing import TYPE_CHECKING, Tuple, Dict
import pygame
from editor_modules.globals import TilemapData, EditorData
from editor_modules.editor_classes.base_menus.tile_menu import TileMenu
from editor_modules.editor_classes.tilegrid.tile import Tile
from editor_modules.editor_classes.ui_elements.size_buttons import SaveButton, LoadButton
from editor_modules.editor_classes.ui_elements.input_field import InputField


class TilegridMenu(TileMenu):
    def __init__(self, pos : Tuple[int, int], size : Tuple[int, int]):
        super().__init__(pos, size)
        self.save_button = SaveButton(pos=(self.down_button.rect.right + 10, self.setting_rect.centery), menu=self)
        self.load_button = LoadButton(pos=(self.save_button.rect.right + 10, self.setting_rect.centery), menu=self)
        self.input_field = InputField(pos=(self.load_button.rect.right + 10, self.save_button.rect.y), size=(self.load_button.rect.width*8, self.load_button.rect.height))
        self.input_field.user_text = EditorData.TILEMAP
        self.get_tiles()

    def get_tiles(self) -> list[Tile]:
        if self.tiles:
            return self.tiles
        for y in range(TilemapData.TILES_Y):
            for x in range(TilemapData.TILES_X):
                self.tiles.append(Tile(pos=(x * TilemapData.TILES_WIDTH, y * TilemapData.TILES_HEIGHT),
                                  size=(TilemapData.TILES_WIDTH, TilemapData.TILES_HEIGHT)))
        return self.tiles
    
    def draw(self, screen : pygame.surface.Surface) -> None:
        super().draw(screen)
        self.input_field.draw(screen)