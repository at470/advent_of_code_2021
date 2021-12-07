import numpy as np
import pprint as pp

# IGNORE
# def mode_data(data):
# 	counter = 0
# 	num = data[0]

# 	for i in data:
# 		current_freq = data.count(i)
# 		if (current_freq > counter):
# 			counter = current_freq
# 			num = i
# 	return num

# part 1
def total_h_movement_simple(some_list):
	total_h_movement = []
	sorted_list = sorted(some_list)
	mid_position = len(sorted_list)/2
	median_value = sorted_list[mid_position]

	for h_pos in h_pos_list:
		total_h_movement.append(abs(h_pos - median_value)) 

	return total_h_movement

# part 2
def triangle(number):
	return number * (number+1) * 0.5

def total_h_movement_complex(some_list, axis):
	total_h_movement = []
	for h_pos in h_pos_list:
		total_h_movement.append(triangle(abs(h_pos - axis)))
	return total_h_movement




def total_fuel_req(some_list, mode):
	total_fuel_req = []

	for h_pos in h_pos_list:
		total_fuel_req.append(abs(h_pos - mode)) 

	return total_fuel_req



# path = '/Users/akikot/advent_of_code_2021/advent_of_code_2021/Day7/input.txt'
path = '/Users/akiko/advent_of_code_2021/advent_of_code_2021/Day7/input.txt'

raw_data = open(path, "r").readlines()

for data_str in raw_data:
    h_pos_str = data_str.split(',')
    h_pos_list = [int(i) for i in h_pos_str]

# part 1
# fuel_req = sum(total_h_movement_simple(h_pos_list))

# print(fuel_req)




# part 2
avg = np.mean(h_pos_list) #axis set at avg
axis_around_here = [round(avg)-1, round(avg), round(avg)+1, avg]

answers = []

for i in axis_around_here:
	fuel_req = sum(total_h_movement_complex(h_pos_list,i))
	answers.append([i,fuel_req])

pp.pprint(answers)

# [[467.0, 89791146.0],
#  [468.0, 89791190.0],
#  [469.0, 89792235.0],
#  [467.55000000000001, 89791046.449999765]]
