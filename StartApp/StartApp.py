import pygame


from MapNavigation_v1_0.Common.AbstractClass import AbstractFrame
from MapNavigation_v1_0.Common.Photo import Photo
from MapNavigation_v1_0.Common.Button import Button
from MapNavigation_v1_0.Common.Label import Label
from MapNavigation_v1_0.settings import QUIT


class StartApp(AbstractFrame):
    def __init__(self,size):
        self.size = size
        self.background = Photo("../resources/index.jpg")
        self.title = Label("北斗导航系统",size=70,font="../resources/李旭科书法.ttf",color=(255,255,255))
        self.menu = []
        self.create_menu_choice("START")
        self.init_location()

    def create_menu_choice(self, *world):
        for i in world:
            button = Button(i)
            self.menu.append(button)

    def init_location(self):
        self.title.set_location((-(self.title.rect.width - self.size[0]) / 2,
                                 (self.size[1] / 2 - self.title.rect.height) / 2))
        self.background.put_center(self.size)
        for index in range(len(self.menu)):
            self.menu[index].set_location(((self.size[0])/2,
                                          (self.size[1])/2+index*20))
            self.menu[index].prep_msg()

    def show(self, screen, clock):
        running = True
        while running:
            clock.tick(30)
            self.background.draw(screen)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return QUIT
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1 :
                        for button in self.menu:
                            if button.on_click():
                                return button.msg
            self.title.draw(screen)
            for i in self.menu:
                i.draw(screen)
            pygame.display.flip()



