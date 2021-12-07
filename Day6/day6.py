# import pprint as pp
# import numpy as np

# path = '/Users/akikot/advent_of_code_2021/advent_of_code_2021/Day6/sample_input.txt'
path = '/Users/akiko/advent_of_code_2021/advent_of_code_2021/Day6/input.txt'

raw_data = open(path, "r").readlines()

# raw_data_array -> ['4,1,4,1,3']
# data_str -> '4,1,4,1,3'
# fish_str -> '4'
# fish -> [4,1,4,1,3]

for data_str in raw_data:
    fish_str = data_str.split(',')
    fish = [int(i) for i in fish_str]

# Part 1: after 80 days
# day_num = 0

# # print('start fish: ')
# # print(fish)

# for day_num in range(80):
# 	# day_num = day_num + 1
# 	start_size = len(fish)
# 	# print('day number: '+ str(day_num))
# 	for index, value in enumerate(fish):
# 		if index < start_size:
# 			if 1 <= value <= 8:
# 				fish[index] = value - 1
# 			if value == 0:
# 				fish[index] = 6
# 				fish.append(8)
# print(len(fish))

## answer: 350149


# Part 2: after 256 days
data_store = [0,0,0,0,0,0,0,0,0]

# load day 0 fish
for i in fish:
	data_store[i] = data_store[i] + 1


for day_num in range(256):
	print(day_num)
	item_zero = data_store[0]
	data_store.pop(0)
	data_store.append(item_zero)
	data_store[6] = data_store[6] + item_zero

print(data_store)

print(sum(data_store))

## answer: 1590327954513





