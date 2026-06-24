from __future__ import annotations
from typing import TYPE_CHECKING, Tuple, Dict
import pygame


class BaseButton():
    def __init__(self, pos : Tuple[int, int], menu, text : str):
        self.pos = pos
        self.menu = menu
        self.font = pygame.font.Font(None, 36)
        self.rect : pygame.Rect | None = None
        self.text = text
        self.get_text_rect()
        menu.buttons.append(self)

    def get_text_rect(self) -> None:
        self.text_surf = self.font.render(self.text, True, "black")
        self.rect = self.text_surf.get_rect()
        if self.rect.width >= self.rect.height:
            self.rect.height = self.rect.width
        else:
            self.rect.width = self.rect.height
        self.rect.x = self.pos[0]
        self.rect.centery = self.pos[1]

    def action(self) -> None:
        pass

    def draw_bounding_box(self, screen : pygame.surface.Surface) -> None:
        pygame.draw.rect(screen, "grey", self.rect)
        pygame.draw.rect(screen, "black", self.rect, width=1)

    def draw_button_text(self, screen : pygame.surface.Surface) -> None:
        text_rect = self.rect.copy()
        text_rect.x = self.rect.centerx - self.text_surf.get_width()//2
        screen.blit(self.text_surf, text_rect)

    def draw(self, screen : pygame.surface.Surface) -> None:
        self.draw_bounding_box(screen)
        self.draw_button_text(screen)



class PlusButton(BaseButton):
    def __init__(self, pos : Tuple[int, int], menu):
        self.text : str = "+"
        super().__init__(pos, menu, self.text)

    def action(self) -> None:
        self.menu.scale +=1
        self.menu.scale = max(0, self.menu.scale)

class MinusButton(BaseButton):
    def __init__(self, pos : Tuple[int, int], menu):
        self.text : str = "-"
        super().__init__(pos, menu, self.text)

    def action(self) -> None:
        self.menu.scale -=1
        self.menu.scale = max(0, self.menu.scale)

class LeftButton(BaseButton):
    def __init__(self, pos : Tuple[int, int], menu):
        self.text : str = "<"
        super().__init__(pos, menu, self.text)

    def action(self) -> None:
        self.menu.shift[0] -= 20

class RightButton(BaseButton):
    def __init__(self, pos : Tuple[int, int], menu):
        self.text : str = ">"
        super().__init__(pos, menu, self.text)

    def action(self):
        self.menu.shift[0] += 20

class UpButton(BaseButton):
    def __init__(self, pos : Tuple[int, int], menu):
        self.text : str = "^"
        super().__init__(pos, menu, self.text)

    def action(self):
        self.menu.shift[1] -= 20

class DownButton(BaseButton):
    def __init__(self, pos : Tuple[int, int], menu):
        self.text : str = "v"
        super().__init__(pos, menu, self.text)

    def action(self) -> None:
        self.menu.shift[1] += 20

class SaveButton(BaseButton):
    def __init__(self, pos : Tuple[int, int], menu):
        self.text : str = "S"
        super().__init__(pos, menu, self.text)

    def action(self) -> None:
        pass

class LoadButton(BaseButton):
    def __init__(self, pos : Tuple[int, int], menu):
        self.text : str = "L"
        super().__init__(pos, menu, self.text)

    def action(self) -> None:
        pass

class UpdateButton(BaseButton):
    def __init__(self, pos : Tuple[int, int], menu):
        self.text : str = "U"
        super().__init__(pos, menu, self.text)

    def action(self) -> None:
        pass


        