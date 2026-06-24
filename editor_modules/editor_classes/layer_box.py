import pygame


class LayerBox():
    def __init__(self, pos, size, boxes):
        self.active = False
        self.working_layer = False
        self.font = pygame.font.Font(None, 42)
        self.layer = 1
        self.rect = pygame.Rect(pos[0], pos[1], size[0], size[1])
        self.setting_rect = pygame.Rect(self.rect[0], self.rect[1], 40, self.rect[3])
        self.setting_rect.right = self.rect.left + 1
        self.passive_layer_color = (200,200,200)
        self.working_layer_color = "white"
        self.inavtive_color = "red"
        self.active_color = "blue"
        boxes.append(self)

    def draw(self, screen):
        background_color = self.working_layer_color if self.working_layer else self.passive_layer_color
        pygame.draw.rect(screen, background_color, self.rect)
        pygame.draw.rect(screen, "black", self.rect, width=1)


        if isinstance(self.layer, int):
            input_text_surface = self.font.render(f"{self.layer}", True, "black")
            input_text_rect = input_text_surface.get_rect()
            input_text_rect.centery = self.rect.centery
            input_text_rect.left = self.rect.left + 4
            screen.blit(input_text_surface, input_text_rect)

        settings_color = self.active_color if self.working_layer else self.inavtive_color

        pygame.draw.rect(screen, settings_color, self.setting_rect)
        pygame.draw.rect(screen, "black", self.setting_rect, width=1)


