import pygame


from MapNavigation_v1_0.Common.Photo import Photo
from MapNavigation_v1_0.Common.Label import Label
from MapNavigation_v1_0.Common.AbstractClass import InterfaceState
from MapNavigation_v1_0.settings import Settings, Request


class QuitState(InterfaceState):
    name = 'quit'

    def __init__(self):
        self.settings = Settings()
        self.image = Photo(self.settings.quit_background)
        self.label = Label("欢迎使用", size=100, font=self.settings.font[self.name], color=(255, 255, 255))
        self.window_size = self.settings.window_size
        self.request = Request()

    def show(self,screen,clock):
        self.set_location()
        self.image.draw(screen)
        self.label.draw(screen)
        pygame.display.flip()
        pygame.time.wait(500)
        pygame.quit()

    def set_location(self):
        self.image.put_center(self.window_size)
        label_loc = ((self.window_size[0]-self.label.rect.width)/2,(self.window_size[1]-self.label.rect.height)/2)
        self.label.set_location(label_loc)