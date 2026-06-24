import pygame
from editor_modules.editor_classes.layer_box import LayerBox
from .size_buttons import PlusButton, MinusButton, UpButton, DownButton


class LayerMenu():
    def __init__(self, pos, size):
        self.scale = 1
        self.shift = [0,0]
        self.rect = pygame.Rect(pos[0], pos[1], size[0], size[1])
        self.setting_rect = pygame.Rect(self.rect[0], self.rect[1], self.rect[2], 40)
        self.setting_rect.top = self.rect.bottom - 1

        self.layer_boxes = []
        self.viable_layer_boxes = []
        self.layer_box_1 = LayerBox(pos=(self.rect.left + 70, self.rect.top + 10),
                                    size=(self.rect.width - 90, 40),
                                    boxes=self.layer_boxes)
        self.layer_box_1.working_layer = True
        
        self.buttons = []
        
        self.plus_button = PlusButton(pos=(self.setting_rect.left + 10, self.setting_rect.centery), menu=self)
        self.plus_button.action = self.plus_layer
        self.minus_button = MinusButton(pos=(self.plus_button.rect.right + 10, self.setting_rect.centery), menu=self)
        self.minus_button.action = self.minus_layer
        self.up_button = UpButton(pos=(self.minus_button.rect.right + 10, self.setting_rect.centery), menu=self)
        self.down_button = DownButton(pos=(self.up_button.rect.right + 10, self.setting_rect.centery), menu=self)


    def plus_layer(self):
        next_layer = self.layer_boxes[-1].layer + 1
        layer_box = LayerBox(pos=(self.rect.left + 70, self.layer_boxes[-1].rect.bottom + 10),
                                  size=(self.rect.width - 90, 40),
                                  boxes=self.layer_boxes)
        layer_box.layer = next_layer
    
    def minus_layer(self):
        if len(self.layer_boxes) == 1:
            return
        self.layer_boxes = self.layer_boxes[:-1]

    def draw(self, screen):
        pygame.draw.rect(screen, "grey", self.rect)
        pygame.draw.rect(screen, "black", self.rect, width=1)
        pygame.draw.rect(screen, (50, 50, 255), self.setting_rect)
        pygame.draw.rect(screen, "black", self.setting_rect, width=1)

        self.viable_layer_boxes = []
        for b in self.layer_boxes:
            b_rect = pygame.Rect(b.rect[0], b.rect[1], b.rect[2], b.rect[3],)
            b_rect.move_ip(self.shift)
            if b_rect.top < self.rect.top:
                continue
            if b_rect.bottom > self.rect.bottom:
                continue
            b_active = b.active
            b_working_layer = b.working_layer
            b_layer = b.layer
            viable_box = LayerBox(pos=b_rect.topleft,
                                  size=(b_rect.width, b.rect.height),
                                  boxes=self.viable_layer_boxes)
            viable_box.active = b_active
            viable_box.working_layer = b_working_layer
            viable_box.layer = b_layer


        for vb in self.viable_layer_boxes: vb.draw(screen)
        for b in self.buttons: b.draw(screen)
        