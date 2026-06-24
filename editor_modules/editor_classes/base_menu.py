import pygame
from editor_modules.globals import TilemapData
from .size_buttons import PlusButton, MinusButton, LeftButton, RightButton, UpButton, DownButton


class BaseMenu():
    def __init__(self, pos, size):
        self.scale = 8 if TilemapData.TILES_WIDTH < 32 else 1
        self.shift = [0,0]
        self.rect = pygame.Rect(pos[0], pos[1], size[0], size[1])
        self.setting_rect = pygame.Rect(self.rect[0], self.rect[1], self.rect[2], 40)
        self.setting_rect.top = self.rect.bottom - 1

        self.buttons = []
        self.plus_button = PlusButton(pos=(self.setting_rect.left + 10, self.setting_rect.centery), menu=self)
        self.minus_button = MinusButton(pos=(self.plus_button.rect.right + 10, self.setting_rect.centery), menu=self)
        self.left_button = LeftButton(pos=(self.minus_button.rect.right + 10, self.setting_rect.centery), menu=self)
        self.right_button = RightButton(pos=(self.left_button.rect.right + 10, self.setting_rect.centery), menu=self)
        self.up_button = UpButton(pos=(self.right_button.rect.right + 10, self.setting_rect.centery), menu=self)
        self.down_button = DownButton(pos=(self.up_button.rect.right + 10, self.setting_rect.centery), menu=self)

        self.tiles = []
        self.tiles_rects = {}
        self.viable_tiles_rects = {}

    def get_tiles(self):
        pass

    def get_tiles_rects(self, tiles):
        rows = TilemapData.TILES_X - 1
        current_row = 0
        current_col = 0
        for t in tiles:
            if current_row > rows:
                current_row = 0
                current_col += 1
            img = t.get_image()
            img = pygame.transform.scale_by(img, self.scale)
            width, height = img.get_size()
            rect = pygame.Rect(self.rect[0] + width * current_row, self.rect[1] + height * current_col, width, height)
            self.tiles_rects[(rect[0], rect[1], rect[2], rect[3])] = (img, t)
            current_row += 1


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
        pygame.draw.rect(screen, "grey", self.rect)
        tiles = self.get_tiles()
        self.tiles_rects = {}
        self.get_tiles_rects(tiles)
        self.viable_tiles_rects = {}
        self.get_viable_tiles_rects(screen)

        pygame.draw.rect(screen, "black", self.rect, width=1)
        pygame.draw.rect(screen, (50, 50, 255), self.setting_rect)
        pygame.draw.rect(screen, "black", self.setting_rect, width=1)
        for b in self.buttons: b.draw(screen)
        