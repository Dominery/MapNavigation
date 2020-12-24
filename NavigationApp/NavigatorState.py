import pygame


from MapNavigation_v1_0.NavigationApp.MapManger import MapManger
from MapNavigation_v1_0.NavigationApp.FileInit import MapInfoFileCreate
from MapNavigation_v1_0.NavigationApp.TextManger import TextManger
from MapNavigation_v1_0.Common.AbstractClass import InterfaceState
from MapNavigation_v1_0.settings import Settings, Request


class NavigatorState(InterfaceState):
    name = 'navigator'

    def __init__(self):
        self.settings = Settings()
        self.map_manager = MapManger("../resources/BaseMap.bmp",self.settings.window_size)
        self.text_manager = None
        self.initialize()
        self.request = Request()

    def import_data(self):
        file = MapInfoFileCreate("../resources/Location.txt", "../resources/Organization.txt", self.map_manager,
                                 "../resources/Locorg.txt")
        file.init_points()
        file.init_route("../resources/Edge.txt")

    def initialize(self):
        self.import_data()
        self.text_manager = TextManger(self.map_manager.points, self.map_manager)
        self.map_manager.direct_move((-500, 0))

    def show(self,screen,clock):
        while True:
            clock.tick(30)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return self.request.send('quit')
                self.map_manager.event(event)
                return_type = self.text_manager.event(event)
                if return_type:
                    return self.request.send('start')
            self.map_manager.move()
            self.map_manager.draw(screen)
            self.text_manager.draw(screen)
            pygame.display.flip()