from MapNavigation_v1_0.Common.element import Spot


class Route:
    def __init__(self, distance, this_point, other_point):
        self.distance = distance
        self.this_point = this_point
        self.other_point = other_point

    def __eq__(self, other):
        return self.this_point == other.this_point and self.other_point == other.other_point


class Point(Spot):
    def __init__(self, name, location,radius=3):
        super(Point, self).__init__(radius,location)
        self.name = name
        self.nick_name = None
        self.routes = []
        self.former_point = None
        self.short_distance = float("inf")

    def add_route(self, route):
        if route not in self.routes:
            self.routes.append(route)

    def set_location(self, location):
        self.location = location
        self.rect.center = location

    def __eq__(self, other):
        return self.name == other.name





