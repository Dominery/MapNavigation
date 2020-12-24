import pygame

from MapNavigation_v1_0.NavigationApp.SearchBox import SearchBox
from MapNavigation_v1_0.Common.element import Button, Label


class TextManger:
    def __init__(self, points, map_manager):
        self.search_box = SearchBox(points, map_manager)
        self.back_Button = Button("BACK", font_size=15, location=(250, 20), font_color=(255, 255, 255),
                                  back_color=(39, 41, 45), size=(100, 30))
        self.points_label = [Label(size=20, location=(20, 560)),
                             Label(size=20, location=(20, 600))]
        self.two_point = map_manager.two_point

    def draw(self, screen):
        for i in range(2):
            if i < len(self.two_point):
                self.points_label[i].prep_msg(['Start: ', 'End: '][i] + self.two_point[i].name)
            else:
                self.points_label[i].prep_msg(['Start: ', 'End: '][i])
            self.points_label[i].set_location((20, 560 + 40 * i))
            self.points_label[i].draw(screen)
        self.back_Button.draw(screen)
        self.search_box.draw(screen)

    def event(self, event):
        if event.type == pygame.KEYDOWN:
            self.search_box.event(event)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1 and self.back_Button.in_area():
                return self.back_Button.msg
