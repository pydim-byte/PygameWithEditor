import pygame
from editor_modules.editor_classes.object_box import ObjectBox
from editor_modules.editor_classes.propery_box import PropertyBox
from .size_buttons import PlusButton, MinusButton, UpButton, DownButton
from editor_modules.editor_classes.numbers_display import NumbersDisplay


class ObjectsMenu():
    def __init__(self, pos, size):
        self.scale = 1
        self.shift = [0,0]
        self.object_page = 0
        self.rect = pygame.Rect(pos[0], pos[1], size[0], size[1])
        self.setting_rect = pygame.Rect(self.rect[0], self.rect[1], self.rect[2], 40)
        self.setting_rect.top = self.rect.bottom - 1

        self.objects_boxes = []
        self.layer_box_1 = ObjectBox(pos=(self.rect.left + 30, self.rect.top + 10),
                                     size=(self.rect.width - 50, 240),
                                     boxes=self.objects_boxes)
        self.object_draw_pos = (self.rect.left + 30, self.rect.top + 10)
        
        self.buttons = []
        
        self.plus_button = PlusButton(pos=(self.setting_rect.left + 10, self.setting_rect.centery), menu=self)
        self.plus_button.action = self.plus_layer
        self.minus_button = MinusButton(pos=(self.plus_button.rect.right + 10, self.setting_rect.centery), menu=self)
        self.minus_button.action = self.minus_layer
        self.up_button = UpButton(pos=(self.minus_button.rect.right + 10, self.setting_rect.centery), menu=self)
        self.up_button.action = self.up_object
        self.down_button = DownButton(pos=(self.up_button.rect.right + 10, self.setting_rect.centery), menu=self)
        self.down_button.action = self.down_object
        self.numbers_display = NumbersDisplay(pos=(self.down_button.rect.right + 10, self.down_button.rect.y), size=(self.down_button.rect.width*4, self.down_button.rect.height))


    def plus_layer(self):
        objects_box = ObjectBox(pos=(self.rect.left + 30, self.rect.top + 10),
                                     size=(self.rect.width - 50, 240),
                                     boxes=self.objects_boxes)
    
    def minus_layer(self):
        if len(self.objects_boxes) == 1:
            return
        self.objects_boxes = self.objects_boxes[:-1]

    def up_object(self):
        old_page = self.object_page
        self.object_page -= 1
        self.object_page = max(0, self.object_page)
        if old_page != self.object_page:
            for obj in self.objects_boxes:
                for prop in obj.properties_boxes:
                    prop.active = False

    def down_object(self):
        old_page = self.object_page
        self.object_page += 1
        self.object_page = min(len(self.objects_boxes)-1,self.object_page)
        if old_page != self.object_page:
            for obj in self.objects_boxes:
                for prop in obj.properties_boxes:
                    prop.active = False

    def draw(self, screen):
        pygame.draw.rect(screen, "grey", self.rect)
        pygame.draw.rect(screen, "black", self.rect, width=1)
        pygame.draw.rect(screen, (50, 50, 255), self.setting_rect)
        pygame.draw.rect(screen, "black", self.setting_rect, width=1)

        self.object_page = max(0, self.object_page)
        self.object_page = min(len(self.objects_boxes)-1, self.object_page)

        self.viable_objects_box = self.objects_boxes[self.object_page]
        for p in self.viable_objects_box.properties_boxes:
            p_rect = pygame.Rect(p.rect[0], p.rect[1], p.rect[2], p.rect[3])
            viable_property = PropertyBox(pos=p_rect.topleft,
                                            size=(p_rect.width, p_rect.height),
                                            boxes=self.viable_objects_box.viable_properties_boxes,
                                            parrent_propery=p)

        self.viable_objects_box.draw(screen)
        for b in self.buttons: b.draw(screen)
        self.numbers_display.user_text = f"{self.object_page+1}/{len(self.objects_boxes)}"
        self.numbers_display.draw(screen)
        