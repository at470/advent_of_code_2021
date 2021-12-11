from collections import Counter


# path = '/Users/akikot/advent_of_code_2021/advent_of_code_2021/Day8/input.txt'
path = '/Users/akiko/advent_of_code_2021/advent_of_code_2021/Day8/input.txt'

raw_data = open(path, "r").read().splitlines()

# Each entry consists of ten unique signal patterns, a | delimiter, and finally the four digit output value.

all_data = []
for line in raw_data:
    num = line.split(' | ')
    all_data.append(num)

output_num = []
# input_num = []


for i in all_data:
    for index, value in enumerate(i):
        if index % 2 == 1: #get only odd indexes
            output_num.append(value)
        # if index % 2 == 0: #get only even indexes
        #     input_num.append(value)

total_output_num = []
total_output_num_lengths = []

for i in output_num:
    num = i.split(' ')
    total_output_num.append(num)
    for j in num:
        total_output_num_lengths.append(len(j))

print(total_output_num_lengths)

# part 1
one = four = seven = eight = 0

for i in total_output_num_lengths:
    if i == 2:
        one = one + 1
    elif i == 4:
        four = four + 1
    elif i == 3:
        seven = seven + 1
    elif i == 7:
        eight = eight + 1

answer = [one, four, seven, eight]

print(answer)
print(sum(answer))


# digit_display = [[0, 'abcefg'], [1, 'cf'], [2, 'acdeg'], [3, 'acdfg'], [4, 'bcdf'], [5, 'abdfg'], [6, 'abdefg'], [7, 'acf'], [8, 'abcdefg'], [9, 'abcdfg']]
# digit_display = [[0, 6], 
                    # [1, 2], #
                    # [2, 5],
                    # [3, 5], 
                    # [4, 4], #
                    # [5, 5], 
                    # [6, 6], 
                    # [7, 3], #
                    # [8, 7], #
                    # [9, 6]]

#   0:      1:      2:      3:      4:
#  aaaa    ....    aaaa    aaaa    ....
# b    c  .    c  .    c  .    c  b    c
# b    c  .    c  .    c  .    c  b    c
#  ....    ....    dddd    dddd    dddd
# e    f  .    f  e    .  .    f  .    f
# e    f  .    f  e    .  .    f  .    f
#  gggg    ....    gggg    gggg    ....

#   5:      6:      7:      8:      9:
#  aaaa    aaaa    aaaa    aaaa    aaaa
# b    .  b    .  .    c  b    c  b    c
# b    .  b    .  .    c  b    c  b    c
#  dddd    dddd    ....    dddd    dddd
# .    f  e    f  .    f  e    f  .    f
# .    f  e    f  .    f  e    f  .    f
#  gggg    gggg    ....    gggg    gggg



