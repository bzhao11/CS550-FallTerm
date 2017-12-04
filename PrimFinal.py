#Prim's Algorithm Maze 
#Ben Zhao
#November 15, 2017
#I've used Prim's Algorithm to generate a maze via the extended Ascii Code. The first few lines are error checking for negative and small numbers, Also, 
#the first few lines are error checking strings. Then, the code uses the concept of frontier cells to clear up passage ways for the maze, since the 
#code in the first few lines already create a 2d arraw of walls. 
#Since same numbers for width and height of the maze will produce different mazes, please try the same number multiple times if it initally doesn't work. 
#Thanks!
#On my honor, I have neither given nor received any unauthorized aid. 

import random

#Asks the user for the desired dimensions of the maze and checks for strings. 
while True:
    try:  
        x = int(input('Height of maze:'))
        break
    except ValueError: 
        print("\nPlease only use integers!")
       

while True: 
    try:  
        y = int(input('Width of maze:'))
        break
    except ValueError: 
        print("\nPlease only use integers!")
   
    
#Error check for small or negative numbers
while x < 10 or y < 10:
    print("Sorry, your numbers are too small or is negative. Please try again. ")
    x = int(input('Height of maze:'))
    y = int(input('Width of maze:'))

# Fill the entire maze with walls in a 2d array
maze = [['▓' for j in range(0, y)] for i in range(0, x)]


# Empty wall list that will later compile all the walls.
wall_list = []

# Check if the position is in the maze and not on the walls that outline the entire maze
def mazeInterior(row, col):
    return row > 0 and row < y-1 and col > 0 and col < x-1

# Add the neighboring walls of the cell (row, col) to the wall list
def addWalls(row, col):
    #Global enables us to use maze and wall_list 'lists' within this definition
    global maze, wall_list

    # It's a 4way-connected grid maze, so we need a directory to identify the positions of different adjacent cells. Above, right,down, left
    dir = ((0, 1), (1, 0), (0, -1), (-1, 0))

    for z in range(0, len(dir)):
        # Find the neighboring wall position and the cell position. 
        wallRow = row + dir[z][0]
        wallCol = col + dir[z][1]
        cellRow = wallRow + dir[z][0]
        cellCol = wallCol + dir[z][1]


        # Make sure the wall grid is in the range of the maze
        if not mazeInterior(wallRow, wallCol) or not mazeInterior(cellRow, cellCol):
            continue

        # Add the wall and the neighboring cell to the list
        wall_list.append(((wallRow, wallCol), (cellRow, cellCol)))

# Pick a random cell first, so that we can start to create frontier cells and start the Prim's algorithm
cellCol = random.randint(1, y-2)
cellRow = random.randint(1, x-2)
maze[cellRow][cellCol] = ' '
addWalls(cellRow, cellCol)

 
# The repetition of finding frontier cells and carving out a passage with each frontier cell, as long as there are walls that are 
# currently in the list. 
while len(wall_list) > 0:
    
    # Pick a random wall, we use id because that one random wall picked in the very beginning needs to always stay the same, 
    # so that we can continue to find new frontier cells and expand the maze passage
    id = random.randint(0, len(wall_list)-1)
    wallRow, wallCol = wall_list[id][0]
    cellRow, cellCol = wall_list[id][1]
    #changes role of the primary cell to a different and one of the frontier cells
    wall_list.pop(id)
   
 
    # If the adjacent cells are no longer walls, then skip
    if maze[wallCol][wallRow] != '▓':
        continue
    # If the two cells that the wall divides are visited, then skip.
    if maze[cellCol][cellRow] == ' ':
        continue

    # Make the two cells as passages
    maze[wallCol][wallRow] = ' '
    maze[cellCol][cellRow] = ' '

    # Add neighboring walls
    addWalls(cellRow, cellCol)

# Print maze
for row in maze:
    print(''.join(row))