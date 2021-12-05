import numpy as np

#load bingo callouts
callouts = [23,30,70,61,79,49,19,37,64,48,72,34,69,53,15,74,89,38,46,36,28,32,45,2,39,58,11,62,97,40,14,87,96,94,91,92,80,99,6,31,57,98,65,10,33,63,42,17,47,66,26,22,73,27,7,0,55,8,56,29,86,25,4,12,51,60,35,50,5,75,95,44,16,93,21,3,24,52,77,76,43,41,9,84,67,71,83,88,59,68,85,82,1,18,13,78,20,90,81,54]

#load boards input file
boards = [[]]
board_num = 0

lines = open("/Users/akiko/Documents/advent_of_code_2021/Day4/input_boards.txt", "r").readlines()

for i in lines:
    row = i.split()
    if row == []:
        board_num = board_num + 1
        boards.append([])
    else:
        row_ints = [int(item) for item in row]
        boards[board_num].append(row_ints)

match = False
winning_boards = set()

class Done( Exception ):
    pass

try:
    for c in callouts:
        for board in range(0, len(boards)):
            for row in range(0, len(boards[board])):
                for item in range(0, len(boards[board][row])):
                    if boards[board][row][item] == c:
                        boards[board][row][item] = None
                if np.any(boards[board][row]) == None:
                    match = True
                    match_callout = c
                    match_board = boards[board]
                    final_board_number = board
                    winning_boards.add(final_board_number)
                    if len(winning_boards) == 100:
                        raise Done
            boards[board] = np.array(boards[board]).T.tolist()
            for row in range(0, len(boards[board])):
                if np.any(boards[board][row]) == None:
                    match = True
                    match_callout = c
                    match_board = boards[board]
                    final_board_number = board
                    winning_boards.add(final_board_number)
                    if len(winning_boards) == 100:
                        raise Done
except Done:
    pass

if match:
    total = 0
    for row in match_board:
        for item in row:
            if item != None:
                total = total + item
    print(final_board_number)
    print(winning_boards)
    print(total * match_callout)