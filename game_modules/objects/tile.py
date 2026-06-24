import pygame


class Tile(pygame.sprite.Sprite):
    def __init__(self,pos : pygame.Vector2, img : pygame.surface.Surface):
        super().__init__()
        self.type : str = 'tile'
        self.image = img
        self.rect = self.image.get_rect(topleft = pos)

    def update(self, dt : float) -> None:
        pass

    def draw(self, surf : pygame.surface.Surface, alpha : float) -> None:
        surf.blit(self.image,self.rect)