# play tic tac toe

game = [[0, 0, 0],
	[0, 0, 0],
	[0, 0, 0]]

def PrintBoard(board):

    for row in board:
        rowstring = ""

        for element in row:
            rowstring = rowstring + str(element) + " "
            
        print(rowstring)

player1 = True
player = "Player 1"
validmoves = len(game[0]) * len(game)
validinput = False
while validmoves > 0:
    PrintBoard(game)
    print(player + "s turn.")
    
    row = 0
    col = 0
    
    while validinput == False:
        coord = input("Enter coordinates in x,x format: ")
        coords = coord.split(",")
        row = int(coords[0])
        col = int(coords[1])

        if row < 0 or row > 2 or col < 0 or col > 2 or game[row][col] != 0:
            print("input is invalid")
        else:
            validinput = True

    if player1 == True:
        game[row][col] = "X"
        player1 = False
        player = "Player 1"
    else:
        game[row][col] = "O"
        player1 = True
        player = "Player 2"
        
    validmoves = validmoves - 1
    validinput = False

PrintBoard(game)
