import pprint

pp = pprint.PrettyPrinter(indent=4)

lines_data_all = open("/Users/akiko/Documents/advent_of_code_2021/Day5/input.txt", "r").readlines()


# lines_data_all -> ['1,2 -> 3,4', '5,6 -> 7,8']
# line_str -> '1,2 -> 3,4'
# points -> ['1,2', '3,4']
# xy_str -> '1,2'
# xy -> ['1', '2']

#range(x) - up to but not including x

lines = []

for line_str in lines_data_all:
    line = []
    points = line_str.split(' -> ')
    for xy_str in points:
        xy = xy_str.split(',')
        xy_ints = [int(i) for i in xy]
        line.append(xy_ints)
    lines.append(line)

straight_lines = []

for line in lines:
    if line[0][0] == line[1][0]:
        straight_lines.append(line)
    if line[0][1] == line[1][1]:
        straight_lines.append(line)

grid = []

for i in range(10000):
    grid_row = []
    for i in range(10000):
        grid_row.append(0)
    grid.append(grid_row)

for straight_line in straight_lines:
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

# pp.pprint(grid)

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