# play battleship against the computer

from random import randint
import os
clear = lambda: os.system('clear')

print("Let's play Battleship!")

board = []
ships = []
board_size = int(input("How big of a board do you want?: "))
ship_count = int((board_size ** 2) / 4)
turn_count = int(ship_count * 3)

# create the board grid
for x in range(board_size):
    board.append(["~"] * board_size)

# print the board visual
def print_board(board):
    for row in board:
        print(" ".join(row))

# get a random coordinate for a ship
def random_cord(board):
    return [randint(0, len(board) - 1), randint(0, len(board[0]) - 1)]

# place the correct number of ships
def place_ships(board, ships, ship_count):
    count = 0
    ship_row = 0
    ship_col = 0

    while count < ship_count:

        # find a random spot
        ship_cord = random_cord(board)
        ship_row = ship_cord[0]
        ship_col = ship_cord[1]

        # only count the ship if it's a new spot
        if [ship_row, ship_col] not in ships:
            ships.append([ship_row, ship_col])
            board[ship_row][ship_col] = "S"
            count = count + 1

# mark all ships that aren't destroyed
def fill_ships(board, ships):
    for cord in ships:
        if board[cord[0]][cord[1]] != "*":
            board[cord[0]][cord[1]] = "S"

# check for user input to quit game
def check_quit(command):
    command = command.lower()
    
    if command[0] == "q":
        print("Goodbye")
        exit()
        
place_ships(board, ships, ship_count)
clear()
print()

# game loop
for turn in range(turn_count):
    #print(ships)
    print("Turns remaining: " + str(turn_count - turn) + " | Ships remaining: " + str(ship_count))
    print_board(board)

    while True:
        guess_row = input("Guess Row ('q' to quit): ")
        check_quit(guess_row)
            
        guess_col = input("Guess Column ('q' to quit): ")
        check_quit(guess_col)
        
        try:
            val = int(guess_row)
        except ValueError:
            print("Invalid row input")
            continue

        try:
            val = int(guess_col)
        except ValueError:
            print("Invalid column input")
            continue

        # if the program gets here, both row and column are valid ints
        guess_row = int(guess_row)
        guess_col = int(guess_col)
        break

    clear()
    
    # currect guess
    if [guess_row, guess_col] in ships:
        print("Congratulations! You sunk my battleship!")
        board[guess_row][guess_col] = "*"
        ships.remove([guess_row, guess_col])
        ship_count = ship_count - 1

        # win if all ships are destroyed
        if ship_count <= 0:
            print("All ships destroyed!")
            break;

    # incorrect guess
    else:
        # guess was out of bounds
        if (guess_row < 0 or guess_row > board_size - 1) or (guess_col < 0 or guess_col > board_size - 1):
            print("Oops, that's not even in the ocean.")
            
        # spot was already guessed
        elif(board[guess_row][guess_col] == "X" or board[guess_row][guess_col] == "*"):
            print("You guessed that one already.")
        # missed
        
        else:
            # check for near misses
            if([guess_row - 1, guess_col] in ships or [guess_row + 1, guess_col] in ships
               or [guess_row, guess_col - 1] in ships or [guess_row, guess_col + 1] in ships):
                print("Near miss!")
            else:
                print("You missed my battleship!")

            board[guess_row][guess_col] = "X"

    # turns are over
    if(turn >= turn_count - 1):
        print("Game Over")

# mark all ships and display the board
fill_ships(board, ships)
print_board(board)
