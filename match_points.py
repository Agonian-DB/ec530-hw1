from gps_distance import gps_distance


def match_points(array_a, array_b):
    if not array_b:
        raise ValueError("array_b cannot be empty")
    closest_indices = []

    for point_a in array_a:
        min_distance = float('inf')
        closest_index = -1

        for j, point_b in enumerate(array_b):
            distance = gps_distance(point_a, point_b)
            if distance < min_distance:
                min_distance = distance
                closest_index = j

        closest_indices.append(closest_index)

    return closest_indices


