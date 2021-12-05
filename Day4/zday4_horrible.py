import numpy as np

board_1 = [
    [1, 0, 50, 0, 0],
    [3, 0, None, 0, 0],
    [0, 0, None, 0, 0],
    [0, 0, None, 0, 0],
    [0, 0, None, 0, 0],
]

boards = [board_1]

callouts = [3, 4, 5, 50]
# callouts = [23,30,70,61,79,49,19,37,64,48,72,34,69,53,15,74,89,38,46,36,28,32,45,2,39,58,11,62,97,40,14,87,96,94,91,92,80,99,6,31,57,98,65,10,33,63,42,17,47,66,26,22,73,27,7,0,55,8,56,29,86,25,4,12,51,60,35,50,5,75,95,44,16,93,21,3,24,52,77,76,43,41,9,84,67,71,83,88,59,68,85,82,1,18,13,78,20,90,81,54]
match = False

for c in callouts:
    for board in range(0, len(boards)):
        for row in range(0, len(boards[board])):
            for item in range(0, len(boards[board][row])):
                if boards[board][row][item] == c:
                    boards[board][row][item] = None
                    print(boards[board][row][item])
            if np.any(boards[board][row]) == None:
                match = True
                match_callout = c
                match_board = boards[board]
                break
        boards[board] = np.array(boards[board]).T.tolist()
        for row in range(0, len(boards[board])):
            if np.any(boards[board][row]) == None:
                match = True
                match_callout = c
                match_board = boards[board]
                break

if match:
    total = 0
    for row in match_board:
        for item in row:
            if item != None:
                total = total + item
    print(total * match_callout)
    print(match_board)