from __future__ import annotations
from typing import TYPE_CHECKING, Union
if TYPE_CHECKING:
    import pygame
<<<<<<< HEAD
    from editor_modules.editor_classes.base_menus.tile_menu import TileMenu
    from editor_modules.editor_classes.tileset.tileset_chunk import TilesetChunk
    from editor_modules.startup_ui.input_box import InputBox
    from editor_modules.startup_ui.ok_box import OKBox
=======
    from editor_classes.base_menu import BaseMenu
    from editor_classes.tileset_chunk import TilesetChunk
>>>>>>> f2364a09e958a98a14037439d03a7513214d2db9
from .namings import ModeName

class Mode():
    CURRENT : ModeName | None = ModeName.SETUP
    NEXT : ModeName | None = None

class TilemapData():
    TILES_WIDTH : int = 0
    TILES_HEIGHT : int = 0
    TILES_X : int = 0
    TILES_Y : int = 0 

class SetupData():
<<<<<<< HEAD
    ACTIVE_BOX : InputBox | OKBox | None = None
=======
    ACTIVE_BOX : BaseMenu | None = None
>>>>>>> f2364a09e958a98a14037439d03a7513214d2db9

class EditorData():
    TILEMAP : str = ""
    TILESET : str = ""
    TILESET_IMAGE : pygame.surface.Surface | None = None
    TILELIST : list[TilesetChunk] = []

