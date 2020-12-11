import pygame

from MapNavigation_v1_0.Common.AbstractClass import AbstractWindowComponents


class Button(AbstractWindowComponents):
    def __init__(self, msg, size=30, font_color=(0, 0, 0), back_color=(0, 255, 0),
                 location=(0,0), font="SimHei"):
        self.msg = msg
        self.width, self.height = 200, 50
        self._font = pygame.font.SysFont(font, size)
        self.font_color = font_color
        self.button_color = back_color
        self.rect = pygame.Rect(0,0,self.width,self.height)
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

    def on_click(self):
        mouse_pos = pygame.mouse.get_pos()
        button_clicked = self.rect.collidepoint(*mouse_pos)
        if button_clicked:
            return True
        return False

