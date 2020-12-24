import os

import pygame

from MapNavigation_v1_0.Common.AbstractClass import AbstractWindowComponents


class Button(AbstractWindowComponents):
    def __init__(self, msg, font_size=30, font_color=(0, 0, 0), back_color=(0, 255, 0),
                 location=(0, 0), font="SimHei", size=(200, 50)):
        self.msg = msg
        self.width, self.height = size
        self._font = pygame.font.SysFont(font, font_size)
        self.font_color = font_color
        self.button_color = back_color
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.set_location(location)
        self.prep_msg()

    def draw(self, screen):
        screen.fill(self.button_color, self.rect)
        screen.blit(self.msg_image, self.msg_image_rect)

    def set_location(self, location):
        self.rect.center = location

    def prep_msg(self):
        self.msg_image = self._font.render(self.msg, True, self.font_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def in_area(self):
        mouse_pos = pygame.mouse.get_pos()
        button_clicked = self.rect.collidepoint(*mouse_pos)
        if button_clicked:
            return True
        return False


class Spot(AbstractWindowComponents):
    def __init__(self, radius,location=(0,0)):
        self.rect = pygame.Rect(0, 0, radius, radius)
        self.set_location(location)

    def set_location(self, location):
        self.rect.center = location

    def draw(self, screen,color,radius):
        pygame.draw.circle(screen, color, self.rect.center, radius, radius)

    def in_area(self):
        mouse_pos = pygame.mouse.get_pos()
        touch = self.rect.collidepoint(*mouse_pos)
        if touch:
            return True
        return False


class Label(AbstractWindowComponents):
    def __init__(self, msg='', size=10, location=(0, 0), font="SimHei", color=(0, 0, 0)):
        if os.path.splitext(font)[1]:
            self._font = pygame.font.Font(font, size)
        else:
            self._font = pygame.font.SysFont(font, size)
        self.font_color = color
        self.prep_msg(msg)
        self.set_location(location)

    def prep_msg(self,msg):
        self.msg_image = self._font.render(msg, True, self.font_color)
        self.rect = self.msg_image.get_rect()

    def draw(self, screen):
        screen.blit(self.msg_image, self.rect)

    def set_location(self, location):
        self.rect.left,self.rect.top = location


class Photo(AbstractWindowComponents):
    def __init__(self, image_file, location=(0, 0)):
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location

    def draw(self, screen):
        screen.blit(self.image, (self.rect.left, self.rect.top))

    def set_location(self, location):
        self.rect.left, self.rect.top = location

    def put_center(self, size):
        self.rect.left, self.rect.top = ((size[0] - self.rect.width) / 2, (size[1] - self.rect.height) / 2)
