from __future__ import annotations
<<<<<<< HEAD
from typing import TYPE_CHECKING, Dict
=======
from typing import TYPE_CHECKING
>>>>>>> f2364a09e958a98a14037439d03a7513214d2db9
import pygame, sys
from game_modules.globals import GameScreen, GameUpdate, PlayerStats
from game_modules.tilemap import Tilemap
from game_modules.player_controller import PlayerController
from game_modules.physic_manager import PhysicManager


class Game:
    def __init__(self) -> None:
        pygame.init()
        self.screen = pygame.Surface((GameScreen.SCREEN_WIDTH,GameScreen.SCREEN_HEIGHT))
        self.display = pygame.display.set_mode((GameScreen.DISPLAY_WIDTH,GameScreen.DISPLAY_HEIGHT))
        self.clock = pygame.time.Clock()
        self.inputs = {pygame.K_LEFT : False, pygame.K_RIGHT : False, pygame.K_UP : False, pygame.K_DOWN : False, pygame.K_SPACE : False}
        self.held_keys = [pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN]
        self.tilemap = Tilemap()
        self.physic_manager = PhysicManager(self.tilemap)
        self.player_controller = PlayerController(self.tilemap.player.sprite)

<<<<<<< HEAD
    def handle_events(self, event : pygame.event.Event) -> None:
=======
    def handle_events(self, event : pygame.event) -> None:
>>>>>>> f2364a09e958a98a14037439d03a7513214d2db9
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type in [pygame.KEYUP, pygame.KEYDOWN]:
            self.handle_key_events(event) 

<<<<<<< HEAD
    def handle_key_events(self, event : pygame.event.Event) -> None:
=======
    def handle_key_events(self, event : pygame.event) -> None:
>>>>>>> f2364a09e958a98a14037439d03a7513214d2db9
        if event.type == pygame.KEYDOWN:
            for inpput_key in self.inputs:
                if event.key == inpput_key:
                    self.inputs[inpput_key] = True

        if event.type == pygame.KEYUP:
            for inpput_key in self.inputs:
                if event.key == inpput_key:
                    self.inputs[inpput_key] = False

    def handle_inputs(self) -> None:
        self.player_controller.handle_inputs(self.inputs)
        for k in self.inputs:
            if k not in self.held_keys:
                self.inputs[k] = False

    def fixed_update(self) -> None:
        self.physic_manager.fixed_update()
        for obj in self.tilemap.dynamic_objects:
            obj.fixed_update()

    def update(self,dt : float) -> None:
        self.tilemap.all_sprites.update(dt)

    def draw(self, alpha : float) -> None:
        self.screen.fill("black")
        for sprite in self.tilemap.all_sprites:
            sprite.draw(self.screen,alpha)
        self.display.blit(pygame.transform.scale(self.screen,self.display.get_size()),(0,0))
        pygame.display.flip()

    def run(self) -> None:
        accumulator = 0
        while True:
            dt = self.clock.tick(GameUpdate.FPS) / 1000
            dt = min(dt,0.1)
            accumulator += dt

            while accumulator >= dt:
                for event in pygame.event.get() : self.handle_events(event)
                self.handle_inputs()
                self.fixed_update()
                accumulator -= 1/GameUpdate.FIXED_TPS

            alpha = accumulator / dt

            self.update(dt)
            self.draw(alpha)

game = Game()
game.run()