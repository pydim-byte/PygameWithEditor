from __future__ import annotations
from typing import TYPE_CHECKING, Tuple, Dict, Union
if TYPE_CHECKING:
    from editor_modules.editor_classes.tileset.tileset_chunk import TilesetChunk
import pygame
from editor_modules.globals import TilemapData, EditorData
from editor_modules.editor_classes.base_menus.tile_menu import TileMenu
from editor_modules.editor_classes.ui_elements.size_buttons import UpdateButton
from editor_modules.editor_classes.ui_elements.input_field import InputField


class TilesetMenu(TileMenu):
    def __init__(self, pos : Tuple[int, int], size : Tuple[int, int]):
        super().__init__(pos, size)
        self.update_button = UpdateButton(pos=(self.down_button.rect.right + 10, self.setting_rect.centery), menu=self)
        self.input_field = InputField(pos=(self.update_button.rect.right + 10, self.update_button.rect.y), size=(self.update_button.rect.width*8, self.update_button.rect.height))
        self.input_field.user_text = EditorData.TILESET
        self.active_tile_img_ref : Tuple[int, int] = None

    def get_tiles(self) -> None:
        self.tiles = EditorData.TILELIST
    
    def draw(self, screen : pygame.surface.Surface) -> None:
        super().draw(screen)
        self.input_field.draw(screen)