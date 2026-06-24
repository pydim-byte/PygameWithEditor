import pygame
from typing import Tuple

class InputBox():
    def __init__(self, pos : Tuple[int], size : Tuple[int], data_type : str):
        self.data_type = data_type
        self.font = pygame.font.Font(None, 128)
        self.small_font = pygame.font.Font(None, 72)
        self.user_text : str = ''
        self.color : Tuple[int] = (200,200,200)
        self.rect = pygame.Rect(pos[0], pos[1], size[0], size[1])

    def draw_bounding_box(self, screen : pygame.surface.Surface) -> None:
        pygame.draw.rect(screen, self.color, self.rect)
        pygame.draw.rect(screen, "black", self.rect, width=1)

    def draw_input_text(self, screen : pygame.surface.Surface) -> None:
        input_text_surface = self.font.render(self.user_text, True, "black")
        input_text_rect = input_text_surface.get_rect()
        input_text_rect.centery = self.rect.centery
        input_text_rect.left = self.rect.left + 10
        screen.blit(input_text_surface, input_text_rect)

    def draw_data_type_text(self, screen : pygame.surface.Surface) -> None:
        data_type_text = self.small_font.render(self.data_type, True, "black")
        data_type_text_rect = data_type_text.get_rect()
        data_type_text_rect.bottom = self.rect.top - 2
        data_type_text_rect.left = self.rect.left + 2
        screen.blit(data_type_text, data_type_text_rect)

    def draw_underlying_rect(self, screen : pygame.surface.Surface) -> None:
        self.setting_rect = pygame.Rect(self.rect[0], self.rect[1], self.rect[2], 40)
        self.setting_rect.top = self.rect.bottom - 1
        pygame.draw.rect(screen, (50, 50, 255), self.setting_rect)
        pygame.draw.rect(screen, "black", self.setting_rect, width=1)

    def draw(self, screen : pygame.surface.Surface) -> None:
        self.draw_bounding_box(screen)
        self.draw_input_text(screen)
        self.draw_data_type_text(screen)
        self.draw_underlying_rect(screen)

