import pygame

from MapNavigation_v1_0.NavigationApp.SearchBox import SearchBox
from MapNavigation_v1_0.Common.Button import Button


class TextManger:
    def __init__(self,points,map_manager):
        self.search_box = SearchBox(points,map_manager)
        self.back_Button = Button("BACK TO MENU",size=15,location=(200,20),font_color=(0,0,0),back_color=(39,41,45))

    def draw(self,screen):
        self.back_Button.draw(screen)
        self.search_box.draw(screen)

    def event(self,event):
        if event.type == pygame.KEYDOWN:
            self.search_box.event(event)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if self.back_Button.on_click():
                    return self.back_Button.world


