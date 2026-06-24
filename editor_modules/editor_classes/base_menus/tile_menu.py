from __future__ import annotations
from typing import TYPE_CHECKING, Tuple, Dict, Union
if TYPE_CHECKING:
    from editor_modules.editor_classes.tilegrid.tile import Tile
    from editor_modules.editor_classes.tileset.tileset_chunk import TilesetChunk
import pygame
from ...globals import EditorData
from editor_modules.globals import TilemapData
from ..ui_elements.size_buttons import BaseButton, PlusButton, MinusButton, LeftButton, RightButton, UpButton, DownButton


class TileMenu():
    def __init__(self, pos : Tuple[int, int], size : Tuple[int, int]):
        self.scale = 8 if TilemapData.TILES_WIDTH < 32 else 1
        self.shift = [0,0]
        self.rect = pygame.Rect(pos[0], pos[1], size[0], size[1])
        self.setting_rect = pygame.Rect(self.rect[0], self.rect[1], self.rect[2], 40)
        self.setting_rect.top = self.rect.bottom - 1

        self.buttons : list[BaseButton] = []
        self.plus_button = PlusButton(pos=(self.setting_rect.left + 10, self.setting_rect.centery), menu=self)
        self.minus_button = MinusButton(pos=(self.plus_button.rect.right + 10, self.setting_rect.centery), menu=self)
        self.left_button = LeftButton(pos=(self.minus_button.rect.right + 10, self.setting_rect.centery), menu=self)
        self.right_button = RightButton(pos=(self.left_button.rect.right + 10, self.setting_rect.centery), menu=self)
        self.up_button = UpButton(pos=(self.right_button.rect.right + 10, self.setting_rect.centery), menu=self)
        self.down_button = DownButton(pos=(self.up_button.rect.right + 10, self.setting_rect.centery), menu=self)

        self.tiles : list[Tile | TilesetChunk] = []

    def get_tiles(self) -> None:
        pass

    def get_viable_tiles(self) -> None:
        rows = TilemapData.TILES_X - 1
        current_row = 0
        current_col = 0
        self.tiles_rects = {}
        for tile in self.tiles:
            if current_row > rows:
                current_row = 0
                current_col += 1
            width, height = TilemapData.TILES_WIDTH * self.scale, TilemapData.TILES_HEIGHT * self.scale
            tile.rect = pygame.Rect(self.rect[0] + width * current_row, self.rect[1] + height * current_col, width, height)
            tile.rect.move_ip(self.shift[0], self.shift[1])
            within_bounds = {"left" : True, "right" : True, "top" : True, "bottom" : True}
            if tile.rect.left < self.rect.left: within_bounds["left"] = False
            if tile.rect.right > self.rect.right : within_bounds["right"] = False
            if tile.rect.top < self.rect.top : within_bounds["top"] = False
            if tile.rect.bottom > self.rect.bottom : within_bounds["bottom"] = False
            tile.valid = all(within_bounds.values())
            current_row += 1

    def draw_background(self, screen : pygame.surface.Surface) -> None:
        pygame.draw.rect(screen, "grey", self.rect)
        pygame.draw.rect(screen, "black", self.rect, width=1)

    def draw_viable_tiles(self, screen : pygame.surface.Surface) -> None:
        for tile in self.tiles:
            if not tile.valid:
                continue
            img_surf = pygame.surface.Surface((TilemapData.TILES_WIDTH, TilemapData.TILES_HEIGHT))
            img_surf.fill("grey")
            img_refs = tile.get_image()
            for img_ref in img_refs:
                blit_img = EditorData.TILESET_IMAGE.subsurface(img_ref[0], img_ref[1], TilemapData.TILES_WIDTH, TilemapData.TILES_HEIGHT)
                img_surf.blit(blit_img, (0,0))
            img_surf = pygame.transform.scale_by(img_surf, self.scale)
            screen.blit(img_surf, tile.rect)
            pygame.draw.rect(screen, "black", tile.rect, width=1)

    def draw_underlying_rect(self, screen : pygame.surface.Surface) -> None:
        pygame.draw.rect(screen, (50, 50, 255), self.setting_rect)
        pygame.draw.rect(screen, "black", self.setting_rect, width=1)

    def draw_buttons(self, screen : pygame.surface.Surface) -> None:
        for b in self.buttons: b.draw(screen)

    def draw(self, screen : pygame.surface.Surface) -> None:
        # get surfaces to draw
        self.get_tiles()
        self.get_viable_tiles()
        # draw surfaces
        self.draw_background(screen)
        self.draw_viable_tiles(screen)
        self.draw_underlying_rect(screen)
        self.draw_buttons(screen)



        


        