import pygame


def get_images(name : str,count : int) -> list[pygame.surface.Surface]:
    images : list[pygame.surface.Surface] = []
    for i in range(count):
        img : pygame.surface.Surface = pygame.image.load(f'assets/images/{name}/{i}.png').convert_alpha()
        images.append(img)
    return images 