import pprint as pp

path = '/Users/akiko/advent_of_code_2021/advent_of_code_2021/Day11/input.txt'
raw_data = open(path, "r").read().splitlines()

grid = []
for row in raw_data:
    point = list(row)
    point_int = [int(i) for i in point]
    grid.append(point_int)

def update_energy(row, col, grid, counter=0):
    max_r = len(grid)-1
    max_c = len(grid[0])-1
    if row < 0 or col < 0 or row > max_r or col > max_c:
        return counter
    else:
        energy = grid[row][col]
        prev_row = row - 1
        next_row = row + 1
        prev_col = col - 1
        next_col = col + 1
        if energy == -1:
            return counter
        if energy == 9:
            grid[row][col] = -1
            counter = counter + 1
            counter = update_energy(prev_row, prev_col, grid, counter)
            counter = update_energy(prev_row, col, grid, counter)
            counter = update_energy(prev_row, next_col, grid, counter)
            counter = update_energy(row, prev_col, grid, counter)
            counter = update_energy(row, next_col, grid, counter)
            counter = update_energy(next_row, prev_col, grid, counter)
            counter = update_energy(next_row, col, grid, counter)
            counter = update_energy(next_row, next_col, grid, counter)
            return counter
        else:
            grid[row][col] = grid[row][col] + 1
            return counter

class Done( Exception ):
    pass

i = 0
flash_count = 0
currently_flashing = 0

try:
    while i < 1000:
        i = i + 1
        currently_flashing = 0
        for row, row_list in enumerate(grid):
            for col, energy in enumerate(row_list):
                flash_count = update_energy(row, col, grid, flash_count)
        for row, row_list in enumerate(grid):
            for col, energy in enumerate(row_list):
                if energy == -1:
                    grid[row][col] = 0
                    currently_flashing = currently_flashing + 1
                    if currently_flashing == len(grid[0])*len(grid):
                        raise Done


except Done:
    pass

# part 1
print(flash_count) #for 100 steps
# 1647

# part 2
print(i)
