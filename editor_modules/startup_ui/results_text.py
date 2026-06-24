from __future__ import annotations
from typing import TYPE_CHECKING, Tuple, Union
if TYPE_CHECKING:
    from input_box import InputBox
    from ok_box import OKBox
import pygame

class ResultsText:
    def __init__(self, input_boxes : list[Union[InputBox | OKBox]]):
        self.input_boxes = input_boxes
        self.font = pygame.font.Font(None, 128)
        self.text : str = "Not a number"
        self.color : Tuple[int]  = (200,200,200)
        self.rect = pygame.Rect(0, 0, 20, 20)

    def get_result_text_from_data(self) -> None:
        data = {"tile width" : None, "tile height" : None, "horizontal tiles" : None, "vertical tiles": None}
        for box in self.input_boxes:
            for key, item in data.items():
                if box.data_type == key:
                    data[key] = box.user_text

        try:
            width = int(data["tile width"])
            height = int(data["tile height"])
            x = int(data["horizontal tiles"])
            y = int(data["vertical tiles"])
            self.text = f"{width * x}x{height * y}"
        except:
            self.text = "Not a number"

    def get_display_size(self) -> Tuple[int]:
        display_size = pygame.display.get_surface().get_size()
        w = display_size[0]
        h = display_size[1]
        return w, h

    def draw_results_text(self, screen : pygame.surface.Surface) -> None:
        self.get_result_text_from_data()
        w, h = self.get_display_size()
        result_text = self.font.render(self.text, True, "black")
        result_text_rect = result_text.get_rect(bottom=(h-50),centerx=(w//2))
        screen.blit(result_text, result_text_rect)

    def draw(self, screen : pygame.surface.Surface) -> None:
        self.draw_results_text(screen)
        


