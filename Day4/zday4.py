#the board has a structure with rows and columns
#for each item in the draw then 
#for each board, check each number for the item in the board


import pandas as pd

#bingo calls
#bingo_callouts = [23,30,70,61,79,49,19,37,64,48,72,34,69,53,15,74,89,38,46,36,28,32,45,2,39,58,11,62,97,40,14,87,96,94,91,92,80,99,6,31,57,98,65,10,33,63,42,17,47,66,26,22,73,27,7,0,55,8,56,29,86,25,4,12,51,60,35,50,5,75,95,44,16,93,21,3,24,52,77,76,43,41,9,84,67,71,83,88,59,68,85,82,1,18,13,78,20,90,81,54]
bingo_callouts = [50,98,65,14,35,28,74,5,93,47]

#input boards
board_1 = pd.read_csv('/Users/akiko/Documents/Advent of Code 2021/Day4/board_1.csv', header = None, sep = '\s+', names = ['0','1','2','3','4'])
board_2 = pd.read_csv('/Users/akiko/Documents/Advent of Code 2021/Day4/board_2.csv', header = None, sep = '\s+', names = ['0','1','2','3','4'])

#create list of boards
boards = [board_1, board_2]





# lambda <arguments> : <Return Value if condition is True> if <condition> 
#                               else <Return Value if condition is False>

#iterate over each bingo call out
for i in bingo_callouts:
    #iterate for each board
    for item in range(0, len(boards)):
        boards[item] = boards[item].applymap(lambda x: None if x == i else x)
        #for each item in the board, check if matching to call out item

# for i in boards:
#     print(i)

print(boards[0])

boards[0].apply(lambda x: print(x.all())

if x.all is False then everything in the row is NaN
