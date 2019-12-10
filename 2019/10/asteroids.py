import math
with open("input.txt") as f:
    content = f.readlines()
content = [x.strip() for x in content]
print(content)


def get_coords(grid):
    coords = []
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == '#':
                coords.append((j, i))
    return coords


def point_is_between_2_point(x, y, x1, y1, x2, y2):
    d1 = dist_two_p(x, y, x1, y1)
    d2 = dist_two_p(x, y, x2, y2)
    d3 = dist_two_p(x1, y1, x2, y2)
    if math.isclose(d1 + d2, d3, abs_tol=0.04):
        return True
    else:
        return False


def dist_two_p(x1, y1, x2, y2):
    return math.sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2))


my_asteroid_map = content
map_coords = get_coords(my_asteroid_map)
print(map_coords)





def get_optimal_station_pos(asteroid_map):

    ast_grid = asteroid_grid(asteroid_map)
    max_asteroid_count = 0
    curr_asteroid_count = 0
    optimal_location = [0, 0]
    coords = get_coords(asteroid_map)
    valid_measurement = False

    for potential in coords:
        for asteroid in coords:
            no_obstacles_between = True
            for obstacle in coords:
                dist1 = dist_two_p(potential[0], potential[1], asteroid[0], asteroid[1])
                dist2 = dist_two_p(potential[0], potential[1], obstacle[0], obstacle[1])
                dist3 = dist_two_p(obstacle[0], obstacle[1], asteroid[0], asteroid[1])
                if dist1 != 0 and dist2 != 0 and dist3 != 0:
                    valid_measurement = True
                    collision = point_is_between_2_point(obstacle[0], obstacle[1], potential[0], potential[1], asteroid[0], asteroid[1])
                    if collision:
                        no_obstacles_between = False
            if no_obstacles_between and valid_measurement:
                curr_asteroid_count += 1
            ast_grid[potential[1]][potential[0]] = curr_asteroid_count
        if curr_asteroid_count > max_asteroid_count:
            max_asteroid_count = curr_asteroid_count
            optimal_location[0] = potential[0]
            optimal_location[1] = potential[1]
        curr_asteroid_count = 0
        valid_measurement = False

    return {"grid":  ast_grid, "optimal_location": optimal_location, "count": max_asteroid_count}


def asteroid_grid(content):
    grid = []
    for line in content:
        arr = split(line)
        grid.append(arr)
    return grid


def show2DGridNicely(grid):
    line = ''
    for i in range(len(grid)):
        for j in range(len(grid)):
            line += str(grid[i][j])
        print(line)
        line = ''

def split(word):
    return [char for char in word]


show2DGridNicely(my_asteroid_map)
my_grid = get_optimal_station_pos(my_asteroid_map)
print(my_grid['optimal_location'])
print(my_grid['count'])

# my_grid = asteroid_grid(content)
show2DGridNicely(my_grid['grid'])

# print(point_is_between_2_point(3, 2, 1, 0, 4, 3))







