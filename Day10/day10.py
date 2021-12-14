import pprint as pp

# input = '{([(<{}[<>[]}>{[]{[(<()>' #problem
# input = '[({(<(())[]>[[{[]{<()<>>'

path = '/Users/akiko/advent_of_code_2021/advent_of_code_2021/Day10/input.txt'
raw_data = open(path, "r").read().splitlines()

# print(raw_data)

parenthesis_type = {
    '(': 'opening',
    '[': 'opening',
    '{': 'opening',
    '<': 'opening',
    ')': 'closing',
    ']': 'closing',
    '}': 'closing',
    '>': 'closing'
}

parenthesis_pair = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>',
    ')': '(',
    ']': '[',
    '}': '{',
    '>': '<'
}

syn_err_score = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137 
}

syn_err_count = {
    ')': 0,
    ']': 0,
    '}': 0,
    '>': 0 
}

completion_count = {
    ')': 0,
    ']': 0,
    '}': 0,
    '>': 0 
}

points = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4 
}



incomplete_lines = []
required_parenthesis = []


for string in raw_data:
    stack = [] #push/append things onto the end, pop things off the end
    for index, chara in enumerate(string):
        if parenthesis_type[chara] == 'opening':
            stack.append(chara)
        elif parenthesis_type[chara] == 'closing':
            if stack.pop() != parenthesis_pair[chara]:
                syn_err_count[chara] = syn_err_count[chara] + 1
                # stop at the first illegal character
                break #stop the current for/while loop
        if index == len(string)-1:
            incomplete_lines.append(string)
            required_parenthesis.append(stack)
print(required_parenthesis)


# print(syn_err_count)

# total_score = syn_err_count[')']*syn_err_score[')']+syn_err_count[']']*syn_err_score[']']+syn_err_count['}']*syn_err_score['}']+syn_err_count['>']*syn_err_score['>']

# # part 1
# print(total_score)
# 343863

score_list =[]
for line in required_parenthesis:
    score = 0
    for index, value in enumerate(reversed(line)):
        closing_chara = parenthesis_pair[value]
        score = score*5 + points[closing_chara]
    score_list.append(score)

print(score_list)

score_list.sort()
mid = len(score_list) // 2
res = (score_list[mid] + score_list[~mid]) / 2

print(res)
