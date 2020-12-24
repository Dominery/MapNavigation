import pygame
import random
from pygame.color import THECOLORS


from MapNavigation_v1_0.NavigationApp.Location import Point, Route, Spot
from MapNavigation_v1_0.Common.Photo import Photo
from MapNavigation_v1_0.NavigationApp.Dijkstra import dijkstra
from MapNavigation_v1_0.Common.Label import Label


class MapManger():
    def __init__(self, map_file, window_size):
        self.map = Photo(map_file)
        self.spot = Spot
        self.points = []
        self.location = [0, 0]
        self.move_x, self.move_y = [0, 0]
        self.flag = False
        self.window_size = window_size
        self.two_point = []

    def add_point(self, name, location):
        if name not in [point.name for point in self.points]:
            self.points.append(Point(name, location))

    def add_route(self, point_A, point_B, distance):
        if point_A not in self.points or point_B not in self.points:
            raise ValueError("Not found the route")
        if Route(distance, point_A, point_B) not in point_A.routes:
            point_A.routes.append(Route(distance, point_A, point_B))
            point_B.routes.append(Route(distance, point_B, point_A))

    def direct_move(self, location):
        self.location[0] = location[0] + self.location[0]
        self.location[1] = location[1] + self.location[1]
        for point in self.points:
            point.set_location((location[0] + point.location[0], location[1] + point.location[1]))
        self.map.set_location(tuple(self.location))

    def is_in_point(self, location):
        for point in self.points:
            area = self.spot(point)
            if area.in_rect_x(location[0]) and area.in_rect_y(location[1]):
                return point
        return False

    @staticmethod
    def show_point_name(point, screen):
        point_label = Label(point.name,size=20,font="SimHei",color=(0,0,0))
        point_label.set_location((point.location[0] - point_label.rect.width / 2, point.location[1] + point_label.rect.height))
        point_label.draw(screen)

    def draw_points(self, screen):
        for i in self.points:
            if i not in self.two_point:
                pygame.draw.circle(screen, "RED", i.location, 3, 3)
            else:
                pygame.draw.circle(screen, random.choice(list(THECOLORS.values())), i.location, 4, 4)

    def add_goal_point(self, point):
        if point and len(self.two_point) < 2:
            self.two_point.append(point)
        if not point:
            self.two_point.clear()
            for point in self.points:
                point.former_point = None
                point.short_distance = float("inf")
        if len(self.two_point) == 2:
            dijkstra(self.two_point)

    def on_click_point(self):
        point = self.is_in_point(pygame.mouse.get_pos())
        self.add_goal_point(point)

    @staticmethod
    def draw_dijkstra_lines(last_point, screen):
        point_A = last_point.former_point
        point_B = last_point
        while point_A:
            pygame.draw.aaline(screen, [0, 255, 0], point_A.location, point_B.location, 10)
            point_B = point_A
            point_A = point_B.former_point

    def draw(self, screen):
        self.map.draw(screen)
        self.draw_points(screen)
        point = self.is_in_point(pygame.mouse.get_pos())
        if point:
            self.show_point_name(point, screen)
        for i in self.two_point:
            self.show_point_name(i, screen)
        if len(self.two_point) == 2:
            self.draw_dijkstra_lines(self.two_point[1], screen)

    def move(self):
        self.move_increment_limit(*self.window_size)
        self.direct_move((self.move_x, self.move_y))

    def event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LSHIFT:
                self.flag = True
        elif event.type == pygame.KEYUP:
            self.move_x = 0
            self.move_y = 0
            self.flag = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 4:
                if self.flag:
                    self.move_x += 5
                else:
                    self.move_y += 10
            elif event.button == 5:
                if self.flag:
                    self.move_x -= 5
                else:
                    self.move_y -= 10
            elif event.button == 1:
                self.on_click_point()

    def move_increment_limit(self, width, height):  # 限制地图移动范围，使超过该范围的移动增量设为0
        if self.move_x + self.location[0] > 0:
            self.move_x = 0
        elif self.move_x + self.location[0] < width - self.map.rect.width:
            self.move_x = 0
        if self.move_y + self.location[1] > 0:
            self.move_y = 0
        elif self.move_y + self.location[1] < height - self.map.rect.height:
            self.move_y = 0
