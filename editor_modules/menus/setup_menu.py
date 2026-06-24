import pygame
from editor_modules.globals import SetupData
from editor_modules.startup_functions.get_ui import get_ui
from editor_modules.startup_functions.get_active_rect import get_active_rect
from editor_modules.startup_functions.launch_editor import launch_editor


class SetupMenu():
    def __init__(self):
        self.input_boxes, self.result_text = get_ui()

<<<<<<< HEAD
    def hanlde_inputs(self, inputs : pygame.event.Event) -> None:
=======
    def hanlde_inputs(self, inputs : pygame.event) -> None:
>>>>>>> f2364a09e958a98a14037439d03a7513214d2db9
        if inputs.type == pygame.KEYDOWN:
            if inputs.key == pygame.K_SPACE:
                launch_editor(self.input_boxes)
                return

        if inputs.type == pygame.MOUSEBUTTONDOWN:
            box = get_active_rect(inputs.pos, self.input_boxes)
            if box:
                SetupData.ACTIVE_BOX = box 

        if SetupData.ACTIVE_BOX:
            if inputs.type == pygame.KEYDOWN:
                if inputs.key == pygame.K_BACKSPACE:
                    SetupData.ACTIVE_BOX.user_text = SetupData.ACTIVE_BOX.user_text[:-1]
                else:
                    SetupData.ACTIVE_BOX.user_text += inputs.unicode

    def update(self) -> None:
        pass

    def draw(self, screen : pygame.surface.Surface) -> None:
        for box in self.input_boxes: box.draw(screen)
        self.result_text.draw(screen)