# import pprint as pp
# import numpy as np

path = '/Users/akikot/advent_of_code_2021/advent_of_code_2021/Day6/input.txt'

raw_data_array = open(path, "r").readlines()

# raw_data_array -> ['4,1,4,1,3']
# data_str -> '4,1,4,1,3'
# fish_str -> '4'
# fish -> 4

for data_str in raw_data_array:
    fish_str = data_str.split(',')
    fish = [int(i) for i in fish_str]


day_num = 0

# print('start fish: ')
# print(fish)

for day_num in range(256):
	# day_num = day_num + 1
	start_size = len(fish)
	# print('day number: '+ str(day_num))
	for index, value in enumerate(fish):
		if index < start_size:
			if 1 <= value <= 8:
				fish[index] = value - 1
			if value == 0:
				fish[index] = 6
				fish.append(8)

print(len(fish))