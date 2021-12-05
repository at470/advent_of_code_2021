import pprint

pp = pprint.PrettyPrinter(indent=4)

grid_limit = 5000
grid = []

for i in range(grid_limit):
    grid_row = []
    for i in range(grid_limit):
        grid_row.append(0)
    grid.append(grid_row)

data = open("/Users/akiko/Documents/advent_of_code_2021/Day5/input.txt", "r").readlines()


# data -> ['1,2 -> 3,4', '5,6 -> 7,8']
# line_str -> '1,2 -> 3,4'
# points -> ['1,2', '3,4']
# xy_str -> '1,2'
# xy -> ['1', '2']

#range(x) - up to but not including x

all_lines = []

for line_str in data:
    line = []
    points = line_str.split(' -> ')
    for xy_str in points:
        xy = xy_str.split(',')
        xy_ints = [int(i) for i in xy]
        line.append(xy_ints)
    all_lines.append(line)

all_straight_lines = []
all_diagonal_lines = []

for line in all_lines:
    if line[0][0] == line[1][0]:
        all_straight_lines.append(line)
    if line[0][1] == line[1][1]:
        all_straight_lines.append(line)
    #part2: find the 45 degree diagonal line inputs
    if abs(line[1][0]-line[0][0]) == abs(line[1][1]-line[0][1]):
        all_diagonal_lines.append(line)


# pp.pprint(all_straight_lines)
# pp.pprint(all_diagonal_lines)


if all_straight_lines != None:
    for straight_line in all_straight_lines:
        #for horizontal lines
        if straight_line[0][1] == straight_line[1][1]:
            y_static = straight_line[0][1]
            # print(row_num)
            min_x = min([straight_line[0][0], straight_line[1][0]])
            max_x = max([straight_line[0][0], straight_line[1][0]])
            for i in range(min_x, max_x + 1):
                grid[y_static][i] = grid[y_static][i] + 1
        #for vertical lines
        if straight_line[0][0] == straight_line[1][0]:
            x_static = straight_line[0][0]
            min_y = min([straight_line[0][1], straight_line[1][1]])
            max_y = max([straight_line[0][1], straight_line[1][1]])
            for i in range(min_y, max_y + 1):
                grid[i][x_static] = grid[i][x_static] + 1
# lambda <arguments> : <Return Value if condition is True> if <condition> 
#                               else <Return Value if condition is False>

if all_diagonal_lines != None:
    for diagonal_line in all_diagonal_lines:
        # pp.pprint(diagonal_line)
        min_x_point = min([diagonal_line[0][0], diagonal_line[1][0]])
        max_x_point = max([diagonal_line[0][0], diagonal_line[1][0]])
        min_y_point = min([diagonal_line[0][1], diagonal_line[1][1]])
        max_y_point = max([diagonal_line[0][1], diagonal_line[1][1]])

        positive_gradient = (diagonal_line[1][1]-diagonal_line[0][1]) / (diagonal_line[1][0]-diagonal_line[0][0]) > 0

        x = min_x_point

        if positive_gradient == True:
            y = min_y_point
            for x in range(min_x_point, max_x_point + 1):
                grid[y][x] = grid[y][x] + 1
                y = y + 1
        else:
            y = max_y_point
            for x in range(min_x_point, max_x_point + 1):
                grid[y][x] = grid[y][x] + 1
                y = y - 1

count = 0
for row in grid:
    for col in row:
        if col > 1:
            count = count + 1

print(count)


# grid = [
#     [0, 0, 0, 0 ,0],
#     [0, 0, 0, 0 ,0],
#     [0, 10, 0, 0 ,0],
#     [0, 0, 0, 8 ,0],
#     [0, 0, 0, 0 ,0],
# ]


# ['414,379 -> 827,379\n', '683,947 -> 183,947\n']
# [
#     [
#         [414,379],
#         [827,379]
#     ],
#     [
#         [683,947],
#         [827,37]
#     ]
# ]