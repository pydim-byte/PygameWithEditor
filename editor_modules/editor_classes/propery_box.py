import pygame


class PropertyBox():
    def __init__(self, pos, size, boxes, parrent_propery=None):
        self.active = False
        self.font = pygame.font.Font(None, 16)
        self.user_text = ""
        self.pointer = None

        self.rect = pygame.Rect(pos[0], pos[1], size[0], size[1])
        self.setting_rect = pygame.Rect(self.rect[0], self.rect[1], self.rect[3], self.rect[3])
        self.setting_rect.right = self.rect.left + 1
        self.collision_rect = None

        self.inavtive_background = "grey"
        self.active_background = "white"

        self.inavtive_color = "red"
        self.active_color = "blue"

        if parrent_propery:
            self.parrent_propery = parrent_propery
            self.active = parrent_propery.active
            self.user_text = parrent_propery.user_text

        boxes.append(self)

    def draw(self, screen):
        if self.parrent_propery:
            self.parrent_propery.active = self.active
            self.parrent_propery.user_text = self.user_text
            self.parrent_propery.collision_rect = self.rect
            if self.active:
                pointer = self.parrent_propery.pointer + 1

        background_color = self.active_background if self.active else self.inavtive_background
        pygame.draw.rect(screen, background_color, self.rect)
        pygame.draw.rect(screen, "black", self.rect, width=1)

        user_text = self.user_text
        if self.active:
            if self.parrent_propery:
                user_text = self.user_text[:pointer] + "|" + self.user_text[pointer:]

        input_text_surface = self.font.render(user_text, True, "black")
        input_text_rect = input_text_surface.get_rect()
        input_text_rect.centery = self.rect.centery
        input_text_rect.left = self.rect.left + 4
        screen.blit(input_text_surface, input_text_rect)

        settings_color = self.active_color if self.active else self.inavtive_color

        pygame.draw.rect(screen, settings_color, self.setting_rect)
        pygame.draw.rect(screen, "black", self.setting_rect, width=1)


