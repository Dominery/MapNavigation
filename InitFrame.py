import pygame


class InitFrame:
    def __init__(self,widow_size,app_name):
        self.window_size = widow_size
        self.init_app(app_name)

    def init_app(self,app_name):
        pygame.init()
        pygame.mixer.init()
        self.screen = pygame.display.set_mode(self.window_size)
        self.background = pygame.Surface(self.screen.get_size())
        self.background.fill([255, 255, 255])
        self.clock = pygame.time.Clock()
        pygame.display.set_caption(app_name)