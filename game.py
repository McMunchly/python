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

    if move == "up":
        coord = coord - size
    elif move == "down":
        coord = coord + size
    elif move == "left":
        coord = coord - 1
    elif move == "right":
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

    elif command == "w":
        if coord >= size:
            print("move up")
            bounds = Move("up", coord, bounds)
    elif command == "s":
        if coord < len(bounds) - size:
            print("move down")
            bounds = Move("down", coord, bounds)
    elif command == "a":
        if coord % size != 0:
            print("move left")
            bounds = Move("left", coord, bounds)
    elif command == "d":
        if (coord + 1) % size != 0:
            print("move right")
            bounds = Move("right", coord, bounds)
            
    coord = bounds.index("@")
