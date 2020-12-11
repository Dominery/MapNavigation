class Route:
    def __init__(self, distance, this_point, other_point):
        self.distance = distance
        self.this_point = this_point
        self.other_point = other_point

    def __eq__(self, other):
        return self.this_point == other.this_point and self.other_point == other.other_point


class Point:
    def __init__(self, name, location):
        self.name = name
        self.nick_name = None
        self.location = location
        self.routes = []
        self.former_point = None
        self.short_distance = float("inf")

    def add_route(self, route):
        if route not in self.routes:
            self.routes.append(route)

    def set_location(self, location):
        self.location = location

    def __eq__(self, other):
        return self.name == other.name


class Spot:
    def __init__(self, point):
        self.rect_x_left = point.location[0] - 3
        self.rect_x_right = point.location[0] + 3
        self.rect_y_top = point.location[1] - 3
        self.rect_y_down = point.location[1] + 3

    def in_rect_x(self, x):
        return self.rect_x_right > x > self.rect_x_left

    def in_rect_y(self, y):
        return self.rect_y_top < y < self.rect_y_down


