import pygame

from MapNavigation_v1_0.StateServer import StateServer
from MapNavigation_v1_0.settings import Settings


class App(object):
    def __init__(self):
        self.settings = Settings()
        self.set_up_window()
        self.state_server = StateServer(self.screen, self.clock)

    def set_up_window(self):
        pygame.init()
        pygame.mixer.init()
        self.screen = pygame.display.set_mode(self.settings.window_size)
        self.background = pygame.Surface(self.screen.get_size())
        self.background.fill([255, 255, 255])
        self.clock = pygame.time.Clock()
        pygame.display.set_caption(self.settings.caption)

    def execute(self):
        self.state_server.execute()


def main():
    app = App()
    app.execute()


if __name__ == '__main__':
    main()