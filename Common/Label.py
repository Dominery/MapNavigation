import pygame
import os
from MapNavigation_v1_0.Common.AbstractClass import AbstractWindowComponents


class Label(AbstractWindowComponents):
    def __init__(self, world, size, position=(0, 0), font="SimHei", color=(0, 0, 0)):
        if os.path.splitext(font)[1]:
            self.surf = pygame.font.Font(font, size).render(world, True, color)
        else:
            self.surf = pygame.font.SysFont(font, size).render(world, True, color)
        self.rect = self.surf.get_rect()
        self.rect.left, self.rect.top = position

    def draw(self, screen):
        screen.blit(self.surf, [self.rect.left, self.rect.top])

    def set_location(self, location):
        self.rect.left, self.rect.top = location
