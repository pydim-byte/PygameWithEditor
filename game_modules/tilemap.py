import pygame,os
from pytmx import load_pygame
from .globals import *
from .tilemap_tools.get_tiles import get_tiles



class Tilemap:
    def __init__(self, tilemap_name="tilemap"):
        self.tilemap_name : str = tilemap_name
        self.all_sprites = pygame.sprite.Group()
        self.visible_tiles = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()
        self.barriers = []
        self.static_objects = []
        self.dynamic_objects = []

        if os.path.isfile(f'assets/tilemap/{self.tilemap_name}.json'):
            get_tiles(self)
            self.all_sprites.add(self.visible_tiles)
            self.all_sprites.add(self.player)
            self.dynamic_objects.append(self.player.sprite)