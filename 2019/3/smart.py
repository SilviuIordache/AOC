import math
wires = open('input.txt', 'r').read().strip().split('\n')


def get_coordinates(wire):
    curr_x = 0
    curr_y = 0
    wire_coordinates = []
    wire_data = wire.split(',')
    for item in wire_data:
        direction = item[0]
        steps = int(item[1:5])

        if direction == 'R':
            curr_x += steps
        if direction == 'L':
            curr_x -= steps
        if direction == 'U':
            curr_y += steps
        if direction == 'D':
            curr_y -= steps
        wire_coordinates.append([curr_x, curr_y])

    return wire_coordinates


def get_line_data(coords):
    last_x = 0
    last_y = 0
    data = []
    for item in coords:
        data.append([last_x, last_y, item[0], item[1]])
        last_x = item[0]
        last_y = item[1]
    return data


def get_cross_coords(line1, line2):
    l1x1 = line1[0]
    l1y1 = line1[1]
    l1x2 = line1[2]
    l1y2 = line1[3]

    l2x1 = line2[0]
    l2y1 = line2[1]
    l2x2 = line2[2]
    l2y2 = line2[3]

    A1 = l1y2 - l1y1
    B1 = l1x1 - l1x2
    C1 = A1 * l1x1 + B1 * l1y1

    A2 = l2y2 - l2y1
    B2 = l2x1 - l2x2
    C2 = A2 * l2x1 + B2 * l2y1

    det = A1 * B2 - A2 * B1

    if det == 0:
        intersection = [0, 0]
        return intersection
    else:
        x = int((B2 * C1 - B1 * C2) / det)
        y = int((A1 * C2 - A2 * C1) / det)

        on_line_1 = check_point_between_2_point(x, y, l1x1, l1y1, l1x2, l1y2)
        on_line_2 = check_point_between_2_point(x, y, l2x1, l2y1, l2x2, l2y2)

        if on_line_1 and on_line_2:
            intersection = [x, y]
            return intersection
        else:
            intersection = [0, 0]
            return intersection


def check_point_between_2_point(x, y, x1, y1, x2, y2):
    if dist_two_p(x, y, x1, y1) + dist_two_p(x, y, x2, y2) == dist_two_p(x1, y1, x2, y2):
        return True
    else:
        return False


def dist_two_p(x1, y1, x2, y2):
    return math.sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2))


def get_intersection_list(line1, line2):
    intersections = []
    for i in line1:
        for j in line2:
            result = get_cross_coords(i, j)
            if result[0] + result[1] > result[0] or result[0] + result[1] > result[1]:
                intersections.append(result)
    return intersections


def min_manhattan(points):
    min_man = 100000
    min_x = 100000
    min_y = 100000
    for point in points:
        if abs(point[0]) + abs(point[1]) < min_man:
            min_man = abs(point[0]) + abs(point[1])
            min_x = abs(point[0])
            min_y = abs(point[1])
    return [min_x, min_y, min_man]


def get_min_distance_to_intersection(wire_data, intersections):
    wire1 = wire_data[0]
    wire2 = wire_data[1]

    print('NEW LINE')
    min_dist = 100000
    for item in intersections:
        curr_dist = get_steps_to_intersection(wire1, item) + get_steps_to_intersection(wire2, item)
        if curr_dist < min_dist:
            min_dist = curr_dist
            print('new min dist: ', min_dist)
        # else:
        #     print('min dist not beaten: ', curr_dist)
    return min_dist


def get_steps_to_intersection(wire_data, intersection):
    int_x = intersection[0]
    int_y = intersection[1]
    steps = 0
    print('new dist attempt')
    for line in wire_data:
        x1 = line[0]
        y1 = line[1]
        x2 = line[2]
        y2 = line[3]
        if check_point_between_2_point(int_x, int_y, x1, y1, x2, y2):
            steps += dist_two_p(x1, y1, int_x, int_y)
            print(dist_two_p(x1, y1, int_x, int_y))
            return int(steps)
        else:
            steps += dist_two_p(x1, y1, x2, y2)
            print(dist_two_p(x1, y1, x2, y2))



w1_coords = get_coordinates((wires[0]))
w2_coords = get_coordinates((wires[1]))


# print(w1_coords)
# print(w2_coords)

line1_data = get_line_data(w1_coords)
line2_data = get_line_data(w2_coords)

print(line1_data)
print(line2_data)
print(get_intersection_list(line1_data, line2_data))

intersection_points = get_intersection_list(line1_data, line2_data)

min_manhattan_data = min_manhattan(intersection_points)
print(min_manhattan_data)

target_x = min_manhattan_data[0]
target_y = min_manhattan_data[1]
shortest_dist = min_manhattan_data[2]

print('shortest dist to intersection: ', shortest_dist)

min_dist_to_intersection = get_min_distance_to_intersection([line1_data, line2_data], intersection_points)
print('total steps to closest intersection: ', min_dist_to_intersection)

