from __future__ import annotations
from typing import TYPE_CHECKING, Union
import pygame


def visualize_property(color_propery_data : str, rect_propery_data : str, scale : int, shift : list[int,int], screen : pygame.surface.Surface) -> None:
    try:
        color_propery_text = color_propery_data.split("___")
        color_rgb = color_propery_text[1].split(",")
        color = pygame.color.Color(int(color_rgb[0]), 
                                    int(color_rgb[1]), 
                                    int(color_rgb[2]))
    except:
        color = None

    try:
        rect_propery_text = rect_propery_data.split("___")
        rect_points = rect_propery_text[1].split(",")
        rect = pygame.Rect(int(rect_points[0]),
                            int(rect_points[1]),
                            int(rect_points[2]),
                            int(rect_points[3]))
    except:
        rect = None

    if color and rect:
        x = rect[0] * scale + shift[0]
        y = rect[1] * scale + shift[1]
        w = rect[2] * scale
        h = rect[3] * scale
        scaled_rect = pygame.Rect(x,y,w,h)
        pygame.draw.rect(screen, color, scaled_rect, width=1)