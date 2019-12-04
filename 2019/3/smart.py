import math
wires = open('input.txt', 'r').read().strip().split('\n')


def get_coordinates(wire):
    curr_x = 0
    curr_y = 0
    wire_coordinates = []
    wire_data = wire.split(',')
    for item in wire_data:
        direction = item[0]
        steps = int(item[1:3])

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

        on_line_1 = False
        on_line_2 = False
        if dist_two_p(l1x1, l1y1, x, y) + dist_two_p(l1x2, l1y2, x, y) == dist_two_p(l1x1, l1y1, l1x2, l1y2):
            on_line_1 = True
        if dist_two_p(l2x1, l2y1, x, y) + dist_two_p(l2x2, l2y2, x, y) == dist_two_p(l2x1, l2y1, l2x2, l2y2):
            on_line_2 = True

        if on_line_1 and on_line_2:
            intersection = [x, y]
            return intersection
        else:
            intersection = [0, 0]
            return intersection


def dist_two_p(x1, y1, x2, y2):
    return math.sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2))


def get_intersection_list(line1, line2):
    intersections = []
    for i in line1:
        for j in line2:
            result = get_cross_coords(i, j)
            if result[0] != 0 and result[1] != 0:
                intersections.append(result)
    return intersections


def min_manhattan(points):
    min_man = 100000
    for point in points:
        if point[0] + point[1] < min_man:
            min_man = point[0] + point[1]
    return min_man


w1_coords = get_coordinates((wires[0]))
w2_coords = get_coordinates((wires[1]))


print(w1_coords)
print(w2_coords)

line1_data = get_line_data(w1_coords)
line2_data = get_line_data(w2_coords)

print(line1_data)
print(line2_data)


print(get_intersection_list(line1_data, line2_data))

intersection_points = get_intersection_list(line1_data, line2_data)


print(min_manhattan(intersection_points))


