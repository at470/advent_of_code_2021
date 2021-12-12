import pprint as pp

def is_minimum(n, *data):
    is_minimum = True
    for i in data:
        if n >= i:
            is_minimum = False
    return is_minimum

def floodfill(start, grid, counter=0):
    r = start[0]
    c = start[1]
    max_r = len(grid)-1
    max_c = len(grid[0])-1
    if grid[r][c] == 9:
        return counter
    else:
        grid[r][c] = 9
        counter =  counter + 1
        if r > 0: counter = floodfill([r-1,c], grid, counter)
        if r < max_r: counter = floodfill([r+1,c], grid, counter)
        if c > 0: counter = floodfill([r,c-1], grid, counter)
        if c < max_c: counter = floodfill([r,c+1], grid, counter)
        return counter

path = '/Users/akiko/advent_of_code_2021/advent_of_code_2021/Day9/input.txt'

raw_data = open(path, "r").read().splitlines()

grid = []
for row in raw_data:
    point = list(row)
    point_int = [int(i) for i in point]
    grid.append(point_int)

# print(grid)

# part 1
max_row = len(grid)-1
max_col = len(grid[0])-1

risk_level = []
low_points = []

# grid[row][col]

for row, row_list in enumerate(grid):
    one_row_up = row-1
    one_row_down = row+1
    for col, point_value in enumerate(row_list):
        l_col = col-1
        r_col = col+1
        # top left corner
        if row == 0 and col == 0:
            # print("top left")
            right = grid[row][r_col]
            down = grid[one_row_down][col]
            if is_minimum(point_value, right, down):
                low_points.append([row,col])
                risk_level.append(point_value+1)
        # top right corner
        elif row == 0 and col == max_col:
            # print("top right")
            left = grid[row][l_col]
            down = grid[one_row_down][col]
            if is_minimum(point_value, left, down):
                low_points.append([row,col])
                risk_level.append(point_value+1)
        # bottom left corner
        elif row == max_row and col == 0:
            # print("bottom left")
            up = grid[one_row_up][col]
            right = grid[row][r_col]
            if  is_minimum(point_value, up, right):
                low_points.append([row,col])
                risk_level.append(point_value+1)
        # bottom right corner
        elif row == max_row and col == max_col:
            # print("bottom right")
            up = grid[one_row_up][col]
            left = grid[row][l_col]
            if is_minimum(point_value, left, up):
                low_points.append([row,col])
                risk_level.append(point_value+1)
        # bottom row
        elif row == max_row:
            # print("bottom row")
            up = grid[one_row_up][col]
            left = grid[row][l_col]
            right = grid[row][r_col]
            if is_minimum(point_value, left, right, up):
                low_points.append([row,col])
                risk_level.append(point_value+1)
        # top row
        elif row == 0:
            # print("top row")
            down = grid[one_row_down][col]
            left = grid[row][l_col]
            right = grid[row][r_col]
            if is_minimum(point_value, left, right, down):
                low_points.append([row,col])
                risk_level.append(point_value+1)
        # right col
        elif col == max_col:
            # print("right col")
            up = grid[one_row_up][col]
            down = grid[one_row_down][col]
            left = grid[row][l_col]
            if is_minimum(point_value, left, up, down):
                low_points.append([row,col])
                risk_level.append(point_value+1)
        # left col
        elif col == 0:
            # print("left col")
            up = grid[one_row_up][col]
            down = grid[one_row_down][col]
            right = grid[row][r_col]
            if is_minimum(point_value, right, up, down):
                low_points.append([row,col])
                risk_level.append(point_value+1)
        # everything else
        else:
            # print("innies")
            up = grid[one_row_up][col]
            down = grid[one_row_down][col]
            right = grid[row][r_col]
            left = grid[row][l_col]
            if is_minimum(point_value, right, up, down, left):
                low_points.append([row,col])
                risk_level.append(point_value+1)

# print(low_points)
# print(risk_level)
print(sum(risk_level))

# part 2
for row, row_list in enumerate(grid):
    for col, point_value in enumerate(row_list):
            if point_value != 9:
                grid[row][col] = 0

# print(grid)

counter_keep = []
for low_point in low_points:
    counter = floodfill(low_point, grid)
    counter_keep.append(counter)

counter_keep.sort(reverse=True)

print(counter_keep[0]*counter_keep[1]*counter_keep[2])