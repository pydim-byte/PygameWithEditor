import pygame
from editor_modules.globals import TilemapData, EditorData
from editor_modules.editor_classes.base_menu import BaseMenu
from editor_modules.editor_classes.tile import Tile
from editor_modules.editor_classes.size_buttons import SaveButton, LoadButton
from editor_modules.editor_classes.input_field import InputField


class TilegridMenu(BaseMenu):
    def __init__(self, pos, size):
        super().__init__(pos, size)
        self.save_button = SaveButton(pos=(self.down_button.rect.right + 10, self.setting_rect.centery), menu=self)
        self.load_button = LoadButton(pos=(self.save_button.rect.right + 10, self.setting_rect.centery), menu=self)
        self.input_field = InputField(pos=(self.load_button.rect.right + 10, self.save_button.rect.y), size=(self.load_button.rect.width*8, self.load_button.rect.height))
        self.input_field.user_text = EditorData.TILESET
        self.get_tiles()

    def get_tiles(self):
        if self.tiles:
            return self.tiles
        for y in range(TilemapData.TILES_Y):
            for x in range(TilemapData.TILES_X):
                self.tiles.append(Tile(pos=(x * TilemapData.TILES_WIDTH, y * TilemapData.TILES_HEIGHT),
                                  size=(TilemapData.TILES_WIDTH, TilemapData.TILES_HEIGHT)))
        return self.tiles
    
    def get_viable_tiles_rects(self, screen):
        for rect, img_t in self.tiles_rects.items():
            rect = pygame.Rect(rect)
            rect.move_ip(self.shift[0], self.shift[1])
            if rect.right > self.rect.right:
                continue
            if rect.right < self.rect.left:
                continue
            if rect.bottom > self.rect.bottom:
                continue
            if rect.top > self.rect.bottom:
                continue
            self.viable_tiles_rects[(rect[0], rect[1], rect[2], rect[3])] = img_t
            screen.blit(img_t[0], rect)
            pygame.draw.rect(screen, "black", rect, width=1)
    
    def draw(self, screen):
        super().draw(screen)
        self.input_field.draw(screen)
        