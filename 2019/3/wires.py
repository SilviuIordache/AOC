wires = open('input.txt', 'r').read().strip().split('\n')
print(wires)



def create_grid(size):
    grid = []
    for i in range(0, size):
        row = []
        for j in range(0, size):
            row.append('.  ')
        grid.append(row)
    return grid


def mark_grid_center(grid):
    grid_size = len(grid)
    grid[round(grid_size / 2)][round(grid_size / 2)] = 'O  '


def show_grid(grid):
    mark_grid_center(grid)
    for i in range(0, len(grid)):
        row = ''
        for j in range(0, len(grid[i])):
            row += grid[i][j]
            if j == len(grid[i]) - 1:
                print(row)


def get_man_dist(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)


def mark_if_overlap(element, wire_type):
    if element == '-- ' or element == '|  ':
        element = 'X  '
    else:
        if wire_type == 'h':
            element = '-- '
        else:
            element = '|  '
    return element


def trace_wires(grid, data):
    wire_data = data.split(',')
    center_x = round(len(grid) / 2)
    center_y = round(len(grid) / 2)
    curr_x = center_x
    curr_y = center_y

    for item in wire_data:
        direction = item[0]
        steps = int(item[1:5])

        if direction == 'R':
            target_x = curr_x + steps
            for i in range(curr_x + 1, target_x):
                grid[curr_y][i] = mark_if_overlap(grid[curr_y][i], 'h')
            grid[curr_y][curr_x] = '+  '
            curr_x += steps

        if direction == 'L':
            target_x = curr_x - steps
            for i in range(target_x, curr_x ):
                grid[curr_y][i] = mark_if_overlap(grid[curr_y][i], 'h')
            grid[curr_y][curr_x] = '+  '
            curr_x -= steps

        if direction == 'U':
            target_y = curr_y - steps
            for i in range(target_y, curr_y):
                grid[i][curr_x] = mark_if_overlap(grid[i][curr_x], 'v')
            grid[curr_y][curr_x] = '+  '
            curr_y -= steps

        if direction == 'D':
            target_y = curr_y + steps
            for i in range(curr_y, target_y + 1):
                grid[i][curr_x] = mark_if_overlap(grid[i][curr_x], 'v')
            grid[curr_y][curr_x] = '+  '
            curr_y += steps


def get_min_manhattan_dist(grid):
    center_x = round(len(grid) / 2)
    center_y = round(len(grid) / 2)

    min_manhattan = 100000

    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if grid[i][j] == 'X  ':
                cross_dist = get_man_dist(center_x, center_y, i, j)
                if( cross_dist < min_manhattan):
                    min_manhattan = cross_dist
    print(min_manhattan)


my_grid = create_grid(500)

wire_1 = wires[0]
wire_2 = wires[1]

trace_wires(my_grid, wire_1)
trace_wires(my_grid, wire_2)

get_min_manhattan_dist(my_grid)
show_grid(my_grid)

# print(get_man_dist(2, 9, 5, 6))
