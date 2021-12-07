def mode_data(data):
	counter = 0
	num = data[0]

	for i in data:
		current_freq = data.count(i)
		if (current_freq > counter):
			counter = current_freq
			num = i
	return num

def total_fuel_req(some_list, mode):
	total_fuel_req = []

	for h_pos in h_pos_list:
		total_fuel_req.append(abs(h_pos - mode)) 

	return total_fuel_req


# path = '/Users/akikot/advent_of_code_2021/advent_of_code_2021/Day7/input.txt'
path = '/Users/akiko/advent_of_code_2021/advent_of_code_2021/Day7/sample_input.txt'

raw_data = open(path, "r").readlines()

for data_str in raw_data:
    h_pos_str = data_str.split(',')
    h_pos_list = [int(i) for i in h_pos_str]

h_pos_mode = mode_data(h_pos_list)

fuel_req = total_fuel_req(h_pos_list, h_pos_mode)

print(fuel_req)

# total_fuel_req = []

# for h_pos in h_pos_list:
# 	total_fuel_req.append(abs(h_pos - h_pos_mode)) 
