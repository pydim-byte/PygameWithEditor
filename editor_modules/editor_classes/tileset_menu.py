import pygame
from editor_modules.globals import TilemapData, EditorData
from editor_modules.editor_classes.base_menu import BaseMenu
from editor_modules.editor_classes.size_buttons import UpdateButton
from editor_modules.editor_classes.input_field import InputField


class TilesetMenu(BaseMenu):
    def __init__(self, pos, size):
        super().__init__(pos, size)
        self.update_button = UpdateButton(pos=(self.down_button.rect.right + 10, self.setting_rect.centery), menu=self)
        self.input_field = InputField(pos=(self.update_button.rect.right + 10, self.update_button.rect.y), size=(self.update_button.rect.width*8, self.update_button.rect.height))
        self.input_field.user_text = EditorData.TILESET
        self.active_tile_img = None

    def get_tiles(self):
        return EditorData.TILELIST

    def get_tiles_rects(self, tiles):
        rows = TilemapData.TILES_X - 1
        current_row = 0
        current_col = 0
        tiles = EditorData.TILELIST
        self.tiles_rects = {}
        for t in tiles:
            if current_row > rows:
                current_row = 0
                current_col += 1
            img = t.get_image()

            temp_img = EditorData.TILESET_IMAGE.subsurface(img[0], img[1], TilemapData.TILES_WIDTH, TilemapData.TILES_HEIGHT)
            temp_img = pygame.transform.scale_by(temp_img, self.scale)
            width, height = temp_img.get_size()

            rect = pygame.Rect(self.rect[0] + width * current_row + 4 * current_row, self.rect[1] + height * current_col + 4 * current_col, width, height)
            self.tiles_rects[(rect[0], rect[1], rect[2], rect[3])] = img
            current_row += 1

    def get_viable_tiles_rects(self, screen):
        for rect, img in self.tiles_rects.items():
            rect = pygame.Rect(rect)
            rect.move_ip(self.shift[0], self.shift[1])
            if rect.right < self.rect.left:
                continue
            if rect.left > self.rect.right:
                continue
            if rect.bottom < self.rect.top:
                continue
            if rect.top > self.rect.bottom:
                continue
            self.viable_tiles_rects[(rect[0], rect[1], rect[2], rect[3])] = img
            temp_img = EditorData.TILESET_IMAGE.subsurface(img[0], img[1], TilemapData.TILES_WIDTH, TilemapData.TILES_HEIGHT)
            screen.blit(pygame.transform.scale_by(temp_img, self.scale), rect)
            pygame.draw.rect(screen, "black", rect, width=1)

    def draw(self, screen):
        super().draw(screen)
        self.input_field.draw(screen)