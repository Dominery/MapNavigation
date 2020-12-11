import pygame
from MapNavigation_v1_0.Common.AbstractClass import AbstractWindowComponents


class Photo(AbstractWindowComponents):
    def __init__(self, image_file, location=(0, 0)):
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location

    def draw(self, screen):
        screen.blit(self.image,(self.rect.left,self.rect.top))

    def set_location(self,location):
        self.rect.left, self.rect.top = location

    def put_center(self,size):
        self.rect.left,self.rect.top = ((size[0]-self.rect.width)/2,(size[1]-self.rect.height)/2)
