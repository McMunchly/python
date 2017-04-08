# check a tic-tac-toe winner

import random

game = []

count = 0

# create a random board
while count < 3:
    incount = 0
    game.append([])
    
    while incount < 3:
        game[count].append(random.randint(0, 2))
        incount = incount + 1
        
    count = count + 1

for row in game:
    print(row)

# 0 - tie, 1 - player 1, 2 - player 2
winner = 0

def CheckRows(board):
    
    for row in board:

        num = row[1]
        same = True

        if num != 0:
            for element in row:
                if num != element:
                    same = False
                    break

            if same == True:
                return num

    return 0

def CheckCols(board):
    cols = []
    count = 0
    templist = []
    
    while count < len(board):
        
        templist = []
        incount = 0
        
        while incount < len(board):
            templist.append(board[incount][count])
            incount = incount + 1

        cols.append(templist)
        count = count + 1
        
    return CheckRows(cols)

def CheckDiagonal(board):
    return CheckRows([[board[0][0], board[1][1], board[2][2]], [board[0][2], board[1][1], board[2][0]]])

test = CheckRows(game)

if test == 0:
    test = CheckCols(game)
    if test == 0:
        test = CheckDiagonal(game)
        
if test != 0:
    print("Player " + str(test) + " is the winner!")
else:
    print("This game is a tie")
    
