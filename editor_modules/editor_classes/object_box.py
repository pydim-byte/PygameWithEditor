import pygame
from editor_modules.editor_classes.propery_box import PropertyBox
from .size_buttons import PlusButton, MinusButton, UpButton, DownButton


class ObjectBox():
    def __init__(self, pos, size, boxes):
        self.scale = 1
        self.shift = [0,0]
        self.rect = pygame.Rect(pos[0], pos[1], size[0], size[1])
        self.setting_rect = pygame.Rect(self.rect[0], self.rect[1], self.rect[2], 40)
        self.setting_rect.top = self.rect.bottom - 1
        
        self.properties_boxes = []
        self.viable_properties_boxes = []
        self.property_box_1 = PropertyBox(
                              pos=(self.rect.left + 40, self.rect.top + 10),
                              size=(self.rect.width - 60, 20),
                              boxes=self.properties_boxes)
        self.property_box_1.user_text = "color___"
        self.property_box_2 = PropertyBox(
                        pos=(self.rect.left + 40, self.property_box_1.rect.bottom + 10),
                        size=(self.rect.width - 60, 20),
                        boxes=self.properties_boxes)
        self.property_box_2.user_text = "rect___"

        self.buttons = []
        self.plus_button = PlusButton(pos=(self.setting_rect.left + 10, self.setting_rect.centery), menu=self)
        self.plus_button.action = self.plus_layer
        self.minus_button = MinusButton(pos=(self.plus_button.rect.right + 10, self.setting_rect.centery), menu=self)
        self.minus_button.action = self.minus_layer
        self.up_button = UpButton(pos=(self.minus_button.rect.right + 10, self.setting_rect.centery), menu=self)
        self.down_button = DownButton(pos=(self.up_button.rect.right + 10, self.setting_rect.centery), menu=self)
        boxes.append(self)

    def serialize(self):
        property_list = {}
        for prop in self.properties_boxes:
            prop_text = prop.user_text.split("___")
            if len(prop_text) < 2 or prop_text[1] == str(): 
                continue
            property_list[prop_text[0]] = prop_text[1]
        return property_list

    def plus_layer(self):
        propery_box = PropertyBox(
                      pos=(self.rect.left + 40, self.properties_boxes[-1].rect.bottom + 10),
                      size=(self.rect.width - 60, 20),
                      boxes=self.properties_boxes)

    
    def minus_layer(self):
        if len(self.properties_boxes) == 2:
            return
        self.properties_boxes = self.properties_boxes[:-1]

    def draw(self, screen):
        pygame.draw.rect(screen, "grey", self.rect)
        pygame.draw.rect(screen, "black", self.rect, width=1)
        pygame.draw.rect(screen, (50, 50, 255), self.setting_rect)
        pygame.draw.rect(screen, "black", self.setting_rect, width=1)

        for vb in self.viable_properties_boxes: vb.draw(screen)
        for b in self.buttons: b.draw(screen)
        