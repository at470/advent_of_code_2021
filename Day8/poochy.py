import pprint

pp = pprint.PrettyPrinter(indent=4)

def difference_in_strings(a, b):
    result = ''
    for i in a:
        if i not in b:
            result += i
    return result

def same_in_strings(a, b):
    result = ''
    for i in a:
        if i in b:
            result += i
    return result

path = '/Users/akiko/advent_of_code_2021/advent_of_code_2021/Day8/input.txt'
raw_data = open(path, "r").read().splitlines()

all_data = []
for line in raw_data:
    num = line.split(' | ')
    all_data.append(num)

all_inputs = []
all_outputs = []

for i in all_data:
    for index, value in enumerate(i):
        if index % 2 == 1:
            all_outputs.append(value)
        else:
            all_inputs.append(value)

inputs = []
for index, value in enumerate(all_inputs):
    inputs.append([])
    inputs[index] = value.split(' ')

outputs = []
for index, value in enumerate(all_outputs):
    outputs.append([])
    outputs[index] = value.split(' ')

total = 0

for index, innies in enumerate(inputs):
    strings_by_length = [[], [], [], [], [], [], [], []]

    for i in innies:
        strings_by_length[len(i)].append(i)

    number_strings = {
        "0": None,
        "1": None,
        "2": None,
        "3": None,
        "4": None,
        "5": None,
        "6": None,
        "7": None,
        "8": None
    }

    segment_mapping = {
        "a": None,
        "b": None,
        "c": None,
        "d": None,
        "e": None,
        "f": None,
        "g": None
    }

    for i in strings_by_length:
        for j in i:
            if len(j) == 2:
                number_strings["1"] = j
            if len(j) == 3:
                number_strings["7"] = j
            if len(j) == 4:
                number_strings["4"] = j
            if len(j) == 7:
                number_strings["8"] = j

    # segment_mapping["a"] = difference_in_strings(number_strings["7"], number_strings["1"])

    missing_from_strings_of_length_6 = ''
    for i in strings_by_length[6]:
        diff = difference_in_strings(number_strings["8"], i)
        missing_from_strings_of_length_6 += diff

    segment_mapping["e"] = difference_in_strings(missing_from_strings_of_length_6, number_strings["4"])
    for i in strings_by_length[6]:
        if segment_mapping["e"] not in i:
            number_strings["9"] = i
            strings_by_length[6].remove(i)

    segment_mapping["c"] = same_in_strings(missing_from_strings_of_length_6, number_strings["1"])
    for i in strings_by_length[6]:
        if segment_mapping["c"] not in i:
            number_strings["6"] = i
            strings_by_length[6].remove(i)

    number_strings["0"] = strings_by_length[6][0]
    # segment_mapping["d"] = difference_in_strings(number_strings["8"], number_strings["0"])

    for i in strings_by_length[5]:
        if segment_mapping["c"] not in i:
            if segment_mapping["e"] not in i:
                number_strings["5"] = i
                strings_by_length[5].remove(i)

    combined_string_of_length_5 = ''
    for i in strings_by_length[5]:
        combined_string_of_length_5 = combined_string_of_length_5 + i

    # myset = set()
    # for i in combined_string_of_length_5:
    #     myset.add(i)
    # segment_mapping["b"] = difference_in_strings(number_strings["8"], "".join(myset))

    for i in strings_by_length[5]:
        if segment_mapping["e"] in i:
            number_strings["2"] = i
            strings_by_length[5].remove(i)

    number_strings["3"] = strings_by_length[5][0]

    for key in number_strings:
        number_strings[key] = "".join(sorted(number_strings[key]))

    number_str = ''
    for i in outputs[index]:
        i = "".join(sorted(i))
        
        for key in number_strings:
            if number_strings[key] == i:
                number_str = number_str + key

    total = total + int(number_str)

pp.pprint(total)