from __future__ import annotations
from typing import TYPE_CHECKING, Union
import pygame


class TilesetChunk():
    def __init__(self, pos : tuple[int, int], size : tuple[int, int], image : tuple[int, int]):
        self.rect = pygame.Rect(pos[0], pos[1], size[0], size[1])
        self.color = pygame.color.Color(0, 0, 0, 255)
        self.image = image

    def get_image(self) -> tuple[int, int]:
        return self.image