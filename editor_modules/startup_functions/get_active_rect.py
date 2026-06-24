from __future__ import annotations
from typing import TYPE_CHECKING, Tuple, Union
if TYPE_CHECKING:
    from ..startup_ui.input_box import InputBox
    from ..startup_ui.ok_box import OKBox
from editor_modules.startup_ui.input_box import InputBox
from editor_modules.startup_ui.ok_box import OKBox
from .launch_editor import launch_editor


def get_active_rect(mouse_pos : Tuple[int], input_boxes : list[Union[InputBox, InputBox, InputBox, InputBox, InputBox, InputBox, OKBox]]) -> Union[InputBox | OKBox] | None:
    for box in input_boxes:
        if box.rect.collidepoint(mouse_pos):
            if isinstance(box, OKBox):
                launch_editor(input_boxes)
                return None
            elif isinstance(box, InputBox):
                return box