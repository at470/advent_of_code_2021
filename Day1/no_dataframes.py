path = '/Users/akiko/advent_of_code_2021/advent_of_code_2021/Day1/input.csv'
raw_data = open(path, "r").read().splitlines()

input = [int(i) for i in raw_data]

counter = 0

for index, value in enumerate(input):
    if index == 0:
        continue
    if value > input[index-1]:
        counter = counter + 1

print(counter)

# 1696  