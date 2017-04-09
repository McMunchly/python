# move around a little play area

import random

blank = "."

def DisplayMap(area, size):
    for x in range(0, size):
        row = ""
        for y in range(0, size):
            row = row + area[y + (size * x)] + " "
        print(row)

def Move(move, coord, board):
    
    board[coord] = blank
    
    if command == "w" and coord >= size:
        print("move up")
        coord = coord - size
    elif command == "s" and coord < len(bounds) - size:
        print("move down")
        coord = coord + size
    elif command == "a" and coord % size != 0:
        print("move left")
        coord = coord - 1
    elif command == "d" and (coord + 1) % size != 0:
        print("move right")
        coord = coord + 1
        
    board[coord] = "@"

    return board
size = int(input("Enter size of area: "))
bounds = [blank for _ in range(size ** 2 - 1)]
bounds.append("@")
coord = bounds.index("@")

play = True
while play == True:
    DisplayMap(bounds, size)
    command = input("Enter command (w, a, s, d, or quit): ")

    command = command[0]
    command = command.lower()
    
    if command == "q":
        play = False

    else:
        bounds = Move(command, coord, bounds)
            
    coord = bounds.index("@")
