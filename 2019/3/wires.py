file_path = './input.txt'
with open(file_path) as fp:
    line = fp.readline()
    cnt = 1
    while line:
        # print("Line %s: %s" % (cnt, line.strip()))
        line = fp.readline()
        cnt += 1


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



def trace_wires(grid, data):
    wire_data = data.split(',')
    center_x = round(len(grid) / 2)
    center_y = round(len(grid) / 2)
    curr_x = center_x
    curr_y = center_y
    for item in wire_data:
        print(item)
        direction = item[0]
        steps = int(item[1])

        if direction == 'R':
            target_x = curr_x + steps
            for i in range(curr_x + 1, target_x):
                if grid[curr_y][i] == '-- ' or grid[curr_y][i] == '| ':
                    grid[curr_y][i] = 'X '
                else:
                    grid[curr_y][i] = '-- '
            grid[curr_y][curr_x] = '+  '
            curr_x += steps

        if direction == 'L':
            target_x = curr_x - steps
            for i in range(target_x, curr_x):
                if grid[curr_y][i] == '-- ' or grid[curr_y][i] == '| ':
                    grid[curr_y][i] = 'X '
                else:
                    grid[curr_y][i] = '-- '
            grid[curr_y][curr_x] = '+  '
            curr_x -= steps

        if direction == 'U':
            target_y = curr_y - steps
            for i in range(target_y, curr_y):
                if grid[i][curr_x] == '-- ' or grid[i][curr_x] == '| ':
                    grid[i][curr_x] = 'X  '
                else:
                    grid[i][curr_x] = '|  '
            grid[curr_y][curr_x] = '+  '
            curr_y -= steps

        if direction == 'D':
            target_y = curr_y + steps
            for i in range(curr_y, target_y + 1):
                if grid[i][curr_x] == '-- ' or grid[i][curr_x] == '| ':
                    grid[i][curr_x] = 'X  '
                else:
                    grid[i][curr_x] = '|  '
            grid[curr_y][curr_x] = '+  '
            curr_y += steps




my_grid = create_grid(20)

# wire_data = 'R75,D30,R83,U83,L12,D49,R71,U7,L72'
wire_1 = 'R8,U5,L5,D3'
wire_2 = 'U7,R6,D4,L4'

trace_wires(my_grid, wire_1)
trace_wires(my_grid, wire_2)

show_grid(my_grid)
