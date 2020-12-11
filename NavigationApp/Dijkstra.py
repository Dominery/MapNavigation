def dijkstra(two_points):
    start_point = two_points[0]
    start_point.short_distance = 0
    visited_point = [start_point]
    while two_points[1] not in visited_point:
        short_distance_point = None
        distance = float("inf")
        for point in visited_point:
            for route in point.routes:
                if route.other_point not in visited_point:
                    if route.distance + point.short_distance < distance:
                        short_distance_point = route.other_point
                        distance = route.distance + point.short_distance
                        distance = distance if distance<short_distance_point.short_distance else short_distance_point.short_distance
                        short_distance_point.former_point = point
                        short_distance_point.short_distance = distance
        if short_distance_point:
            visited_point.append(short_distance_point)
        else:
            break
    if two_points[1].former_point:
        return True
    else:
        return False
