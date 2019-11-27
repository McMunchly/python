# start with 'A' and walk randomly around a grid, until 'Z' or becoming trapped
import random
random.seed

grid = []
size = 10
alpha = 'A'
blank = '.'
coord = 0

for x in range(0, size * size):
    grid.append(blank)

grid[coord] = alpha
alpha = chr(ord(alpha) + 1)

# loop to Z
for x in range(ord(alpha), ord('Z') + 1):
    walk = False
    direction = 0
    directions = [0, 1, 2, 3]
    
    while walk == False:
            
        direction = directions[random.randint(0, len(directions) - 1)]
        directions.remove(direction)   
        
        if direction == 0:
            if coord % size != 0 and grid[coord - 1] == blank:
                coord = coord - 1
                walk = True
        elif direction == 1:
            if coord > size and grid[coord - size] == blank:
                coord = coord - size
                walk = True
        elif direction == 2:
            if (coord + 1) % size != 0 and grid[coord + 1] == blank:
                coord = coord + 1
                walk = True
        elif direction == 3:
            if x < (size * size) - size and grid[coord + size] == blank:
                coord = coord + size
                walk = True

        if len(directions) == 0:
            break

    if walk == True:
        grid[coord] = alpha
        alpha = chr(ord(alpha) + 1)
    else:
        break

# print the grid
for x in range(0, len(grid)):
    if x != 0 and (x + 1) % size == 0:
        print(grid[x])

    else:
        print(grid[x], end =" ")

