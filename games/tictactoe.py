# glorious complete tic tac toe game

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
    diagonals =[[],[]]

    count = 0
    while count < len(board):
        diagonals[0].append(board[count][count])
        count = count + 1

    count = 0
    while count < len(board):
        diagonals[1].append(board[count][len(board) - count - 1])
        count = count + 1
                            
    return CheckRows(diagonals)

# create an empty board
def CreateBoard(size):
    
    game = []
    count = 0
    
    while count < size:
        incount = 0
        game.append([])
    
        while incount < size:
            game[count].append(0)
            incount = incount + 1
        
        count = count + 1

    return game
        
def DrawBoard(size, nums):
    vert = " ---"
    horiz = "|   "

    count = 0
    rowcount = 0
    while count < size * 2 + 1:
        if count % 2 == 0:
            print(vert * size)
        else:
            incount = 0
            row = ""
            while incount < size:
                if(nums[rowcount][incount] != 0):
                    row = row + "| " + str(nums[rowcount][incount]) + " "
                else:
                    row = row + horiz
                incount = incount + 1

            print(row + horiz)
            rowcount = rowcount + 1

        count = count + 1
        
def CheckWinner(game):
    test = CheckRows(game)
        
    if test == 0:
        test = CheckCols(game)
        if test == 0:
            test = CheckDiagonal(game)

    return test

def Game():
    
    boardsize = int(input("What size board? "))

    if(boardsize < 3):
        print("Board size cannot be smaller than 3")
        boardsize = 3
        
    game = CreateBoard(boardsize)

    player1 = True
    player = "Player 1"
    validmoves = len(game[0]) * len(game)
    validinput = False

    
    while validmoves > 0:
        DrawBoard(boardsize, game)
        print(player + "\'s turn.")
    
        row = 0
        col = 0
    
        while validinput == False:
            coord = input("Enter coordinates in x,x format: ")
            coords = coord.split(",")
            row = int(coords[0])
            col = int(coords[1])

            if row < 0 or row > boardsize - 1 or col < 0 or col > boardsize - 1 or game[row][col] != 0:
                print("input is invalid")
            else:
                validinput = True

        if player1 == True:
            game[row][col] = "X"
            player1 = False
            player = "Player 2" 
        else:
            game[row][col] = "O"
            player1 = True
            player = "Player 1"
        
        validmoves = validmoves - 1
        validinput = False

        check = CheckWinner(game)
        
        if check != 0:
            print("Player " + str(check) + " is the winner!")
            break

    
    checkagain = CheckWinner(game)

    if checkagain == 0:
        print("It's a tie game")
        
    DrawBoard(boardsize, game)

if __name__ == "__main__":
    Game()
