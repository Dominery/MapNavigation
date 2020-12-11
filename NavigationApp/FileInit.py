from math import sqrt


class MapInfoFileCreate:
    def __init__(self,point_location_file,point_name_file,map_manager,point_nick_name_file):
        self.location_file = point_location_file
        self.name_file = point_name_file
        self.map_manager = map_manager
        self.point_nick_name_file = point_nick_name_file

    def init_points(self):
        loc_file = open(self.location_file,"r",encoding="utf-8")
        with open(self.name_file,"r",encoding="utf-8") as name_file:
            name = name_file.readlines()
        name_index_file = open(self.point_nick_name_file,"r",encoding="utf-8")
        name_index = name_index_file.readline().split(",")[0].strip()
        loc = loc_file.readline().strip()
        while loc and name_index:
            loc = loc.split("，")
            point_name = name[int(name_index)].strip()
            self.map_manager.add_point(point_name,(int(loc[0]),int(loc[1])))
            loc = loc_file.readline().strip()
            name_index = name_index_file.readline().split(",")[0].strip()
        loc_file.close()
        name_index_file.close()

    def init_route(self,route_file):
        with open(route_file,"r",encoding="utf-8")as f:
            route_indexes = f.readline().strip().split(",")
            while route_indexes[0] and route_indexes[1]:
                pre_index = int(route_indexes[0])
                post_index = int(route_indexes[1])
                pre_point = self.map_manager.points[pre_index]
                post_point =self.map_manager.points[post_index]
                distance = sqrt((pre_point.location[0]-post_point.location[0])**2+(pre_point.location[1]-post_point.location[1])**2)
                self.map_manager.add_route(self.map_manager.points[pre_index],self.map_manager.points[post_index],distance)
                route_indexes = f.readline().strip().split(",")




