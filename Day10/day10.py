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


# raw_data = ['{([(<{}[<>[]}>{[]{[(<()>','[({(<(())[]>[[{[]{<()<>>)', '[({(<(())[]>[[{[]{<()<>>', '[(()[<>])]({[<{<<[]>>(']
raw_data = ['[']
incomplete_lines = []
required_parenthesis = []

stack = [] #push/append things onto the end, pop things off the end
for string in raw_data:
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


# print(syn_err_count)

# total_score = syn_err_count[')']*syn_err_score[')']+syn_err_count[']']*syn_err_score[']']+syn_err_count['}']*syn_err_score['}']+syn_err_count['>']*syn_err_score['>']

# # part 1
# print(total_score)
# 343863

print(incomplete_lines)
print(required_parenthesis)

temp = []
for index, string in enumerate(incomplete_lines):
    for i, requirements in enumerate(required_parenthesis):
        var = required_parenthesis[index].pop() #strings ['<','<','['']
        # print(var)
        temp.append(parenthesis_pair[var])
        # print(incomplete_lines[index])

print(temp)
# [[')', '>', '>'],[')', '>', '>'],[')', '>', '>']]

