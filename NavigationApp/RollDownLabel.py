import pygame


def sort(point):
    return len(point.name)


class RollDownLabel:
    def __init__(self, x, y, points):
        self.suit_points = []
        self.font = pygame.font.SysFont('SimHei', 16)
        self.x = x
        self.y = y
        self.points = points
        self.world_surf_list = []
        self.__width = 10

    def create_suit_point_surf(self):
        world_list = [str(index + 1) + "." + self.suit_points[index].name for index in range(len(self.suit_points))]
        self.world_surf_list = [self.font.render(world, True, (0, 0, 0)) for world in world_list]

    def _get_with(self):
        for i in range(len(self.world_surf_list)):
            width = self.world_surf_list[i].get_rect().width
            self.__width = width if width > self.__width else self.__width

    def _get_height(self):
        self.__height = 10+len(self.world_surf_list)*20

    def create_background(self):
        self._get_with()
        self._get_height()
        background_surface = pygame.Surface([self.__width, self.__height])
        background_surface.fill([161, 196, 253])
        self.background = background_surface.convert()
        self.background.set_alpha(80)

    def reset(self):
        self.world_surf_list = []
        self.suit_points = []
        self.__width = 10
        self.__height = 10

    def draw(self, screen):
        self.create_background()
        screen.blit(self.background,[self.x,self.y-10])
        for i in range(len(self.world_surf_list)):
            screen.blit(self.world_surf_list[i], [self.x, self.y + 20 * i])

    def set_location(self,location):
        self.x,self.y = location

    def create_surf(self, point_name):
        if point_name:
            self.suit_points = [i for i in self.points if i.name.startswith(point_name)]
            self.suit_points = sorted(self.suit_points,key=sort)
            self.create_suit_point_surf()
        else:
            self.suit_points = []
            self.world_surf_list = []

    def get_point(self, event, state):
        if event.key in range(49, len(self.suit_points) + 49) and not state:  # 输入框上无提示的状态
            return self.suit_points[event.key - 49]



