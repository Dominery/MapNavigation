import pygame


from MapNavigation_v1_0.Common.AbstractClass import InterfaceState
from MapNavigation_v1_0.Common.Photo import Photo
from MapNavigation_v1_0.Common.Button import Button
from MapNavigation_v1_0.Common.Label import Label
from MapNavigation_v1_0.settings import Settings, Request


class StartState(InterfaceState):
    name = 'start'

    def __init__(self):
        self.settings = Settings()
        self.size = self.settings.window_size
        self.background = Photo(self.settings.start_background)
        self.title = Label(self.settings.start_title,size=70,font=self.settings.font['start'],color=(255,255,255))
        self.menu = []
        self.create_menu_choice("START")
        self.init_location()
        self.request = Request()

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
            clock.tick(self.settings.clock)
            self.background.draw(screen)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return self.request.send('quit')
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1 :
                        for button in self.menu:
                            if button.on_click():
                                return self.request.send('navigator')
            self.title.draw(screen)
            for i in self.menu:
                i.draw(screen)
            pygame.display.flip()



