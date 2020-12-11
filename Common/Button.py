import pygame
import random


from MapNavigation_v1_0.Common.AbstractClass import AbstractWindowComponents


class Button(AbstractWindowComponents):
    def __init__(self, world, size=30,location=(0,0),font_color=(255,255,255),back_color=(255,255,255),font = "SimHei"):
        self.world = world
        self._font = pygame.font.SysFont(font, size)
        self._font_color = font_color
        self._back_color = back_color
        self.surf = self._font.render(world, True, self._font_color)
        self.rect = self.surf.get_rect()
        self.rect.left, self.rect.top = location
        background_surface = pygame.Surface([self.rect.width+40,self.rect.height+20])
        background_surface.fill(self._back_color)
        self.background = background_surface.convert()
        self.background.set_alpha(50)

    def draw(self,screen):
        screen.blit(self.background,(self.rect.left-20,self.rect.top-10))
        screen.blit(self.surf,(self.rect.left,self.rect.top))

    def set_location(self,location):
        self.rect.left,self.rect.top = location

    def on_click(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.width > mouse_pos[0] - self.rect.left > 0 and self.rect.height > mouse_pos[
            1] - self.rect.top > 0:
            self._font_color = tuple(int(random.randint(0,255)) for i in range(3))
            self.surf = self._font.render(self.world,True,self._font_color)
            self._back_color = tuple(int(random.randint(0,255)) for i in range(3))
            self.background.fill(self._back_color)
            return True
        else:
            return False