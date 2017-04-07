# draw a tic tac toe board

def DrawBoard(size):
    vert = " ---"
    horiz = "|   "

    count = size * 2 + 1

    while count > 0:
        if count % 2 != 0:
            print((vert) * size)
        else:
            print(horiz * (size + 1))

        count = count - 1

def Game():
    boardsize = int(input("What size board? "))
    DrawBoard(boardsize)

if __name__ == "__main__":
    Game()
