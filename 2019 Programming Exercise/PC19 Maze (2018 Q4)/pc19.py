## TASK 1

def generate_grid():
    # grid is a 2-dimensional array with 10 columns and 11 rows
    grid = [["" for i in range(10)] for j in range(11)]
    maze_file = open("MAZE.TXT", "r")

    for row in range(11):
        line = maze_file.readline()
        if line[-1] == "\n":
            line = line[:-1]
        for col in range(10):
            grid[row][col] = line[col]

    maze_file.close()
    return grid

def display_grid(grid):
    s = ""  # string representation of the grid
    for row in range(11):
        for col in range(10):
            s += grid[row][col] + " "
        s += "\n"
    print(s)

## TASK 2
import random
def clear_grid(grid):

    # remove prize and player already present
    for row in range(11):
        for col in range(10):
            if grid[row][col] == "P" or grid[row][col] == "O":
                grid[row][col] = "."
    return grid

def place_prize(grid):
    # has the prize been successfully placed on the maze?
    prize_placed = False
    while prize_placed == False:
        prize_row = random.randint(0, 11 - 1)
        prize_col = random.randint(0, 10 - 1)

        # not the wall or player position
        if grid[prize_row][prize_col] != "X" and grid[prize_row][prize_col] != "O":
            grid[prize_row][prize_col] = "P"
            prize_placed = True
    return grid

## TASKS 3 AND 4
def place_player(grid):
    # has the player been successfully placed on the maze?
    player_placed = False
    while player_placed == False:

        # restrict player position to central 4x5 area
        player_row = random.randint(3, 6)
        player_col = random.randint(3, 7)

        # not the wall or prize position
        if grid[player_row][player_col] != "X" and grid[player_row][player_col] != "P":
            grid[player_row][player_col] = "O"
            player_placed = True

    return grid

# returns the player position as a tuple of (y, x) or (row, col).
def player_pos(grid):
    for row in range(11):
        for col in range(10):
            if grid[row][col] == "O":
                return (row, col)

# returns the prize position as a tuple of (y, x) or (row, col).
def prize_pos(grid):
    for row in range(11):
        for col in range(10):
            if grid[row][col] == "P":
                return (row, col)

# handles the movement of the player in the maze.
# previous represents the previous move made.
def move(grid, direction, previous):
    
    # player's current x and y position before moving
    row, col = player_pos(grid)
    if direction == "":
        direction = previous

    if direction == "U":
        # collide with wall
        if grid[row - 1][col] == "X":
            print("Cannot move, player collides with wall!")
            print()
        else:
            grid[row - 1][col] = "O"
            grid[row][col]     = "."
    elif direction == "D":
        # collide with wall
        if grid[row + 1][col] == "X":
            print("Cannot move, player collides with wall!")
            print()
        else:
            grid[row + 1][col] = "O"
            grid[row][col]     = "."
    elif direction == "L":
        # collide with wall
        if grid[row][col - 1] == "X":
            print("Cannot move, player collides with wall!")
            print()
        else:
            grid[row][col - 1] = "O"
            grid[row][col]     = "."
    elif direction == "R":
        # collide with wall
        if grid[row][col + 1] == "X":
            print("Cannot move, player collides with wall!")
            print()
        else:
            grid[row][col + 1] = "O"
            grid[row][col]     = "."
    elif previous == "":
        # do nothing
        pass
    else:
        print("Cannot move, direction not valid!")
        print()
        
    return grid

# main game function
def main_game():
    grid = generate_grid()
    grid = clear_grid(grid)
    grid = place_prize(grid)
    grid = place_player(grid)

    # prize position is fixed.
    prize = prize_pos(grid)
    
    previous = ""
    while player_pos(grid) != prize:
        display_grid(grid)
        print("Enter a direction to move (U: up, D: down, L: left, R: right).")
        direction = input(">>> ")
        print()
        grid = move(grid, direction, previous)

        if direction in "UDLR" and direction != "":
            previous = direction

    ## TASK 4
    if player_pos(grid) == prize:
        print("Player has won the game!")
        print()
