
## TASK 4.1
def GenerateGrid(size = 5):
    grid = [[0 for i in range(size)] for j in range(size)]
    return grid

def DisplayGrid(grid):
    output = ""
    size   = len(grid)
    for i in range(size):
        for j in range(size):
            output += str(grid[i][j])
            if j != size - 1:      # not the last column
                output += " "

        if i != size - 1:          # not the last row
            output += "\n"
    print(output)

## TASK 4.2
import random
def IncrementCell(grid, row, col):
    size = len(grid)
    # only increment when row/col is within range (0 to size - 1)
    if row >= 0 and col >= 0 and row <= size - 1 and col <= size - 1:
        
        # increment only if cell is not a bomb
        if grid[row][col] != "X":
            grid[row][col] += 1
    return grid

def PlaceOneBomb(grid):
    size = len(grid)
    RandomRow = random.randint(0, size - 1)
    RandomCol = random.randint(0, size - 1)
    grid[RandomRow][RandomCol] = "X"
    
    # populate surrounding cells
    grid = IncrementCell(grid, RandomRow-1, RandomCol-1)
    grid = IncrementCell(grid, RandomRow-1, RandomCol)
    grid = IncrementCell(grid, RandomRow-1, RandomCol+1)
    grid = IncrementCell(grid, RandomRow, RandomCol-1)
    grid = IncrementCell(grid, RandomRow, RandomCol+1)
    grid = IncrementCell(grid, RandomRow+1, RandomCol-1)
    grid = IncrementCell(grid, RandomRow+1, RandomCol)
    grid = IncrementCell(grid, RandomRow+1, RandomCol+1)

    return grid

## TASK 4.3
def PlaceTwoBombs(grid):
    size = len(grid)
    ValidBombs = 0
    while ValidBombs != 2:
        RandomRow = random.randint(0, size - 1)
        RandomCol = random.randint(0, size - 1)

        # bomb is not already present in that position
        if grid[RandomRow][RandomCol] != "X":
            grid[RandomRow][RandomCol] = "X"
        
            # populate surrounding cells
            grid = IncrementCell(grid, RandomRow-1, RandomCol-1)
            grid = IncrementCell(grid, RandomRow-1, RandomCol)
            grid = IncrementCell(grid, RandomRow-1, RandomCol+1)
            grid = IncrementCell(grid, RandomRow, RandomCol-1)
            grid = IncrementCell(grid, RandomRow, RandomCol+1)
            grid = IncrementCell(grid, RandomRow+1, RandomCol-1)
            grid = IncrementCell(grid, RandomRow+1, RandomCol)
            grid = IncrementCell(grid, RandomRow+1, RandomCol+1)
            ValidBombs += 1
        
    return grid

## TASK 4.4
def PlaceBombs(grid, bombs = 3):
    size = len(grid)
    ValidBombs = 0
    while ValidBombs < bombs:
        RandomRow = random.randint(0, size - 1)
        RandomCol = random.randint(0, size - 1)

        # bomb is not already present in that position
        if grid[RandomRow][RandomCol] != "X":
            grid[RandomRow][RandomCol] = "X"
        
            # populate surrounding cells
            grid = IncrementCell(grid, RandomRow-1, RandomCol-1)
            grid = IncrementCell(grid, RandomRow-1, RandomCol)
            grid = IncrementCell(grid, RandomRow-1, RandomCol+1)
            grid = IncrementCell(grid, RandomRow, RandomCol-1)
            grid = IncrementCell(grid, RandomRow, RandomCol+1)
            grid = IncrementCell(grid, RandomRow+1, RandomCol-1)
            grid = IncrementCell(grid, RandomRow+1, RandomCol)
            grid = IncrementCell(grid, RandomRow+1, RandomCol+1)
            ValidBombs += 1
        
    return grid

def GenerateGridWithBombs(size = 5, bombs = 3):
    grid = GenerateGrid(size)
    grid = PlaceBombs(grid, bombs)
    return grid

def TASK44():
    print("Beginner grid: ")
    beginner = GenerateGridWithBombs(5, 3)
    DisplayGrid(beginner)
    print()
    print("Intermediate grid: ")
    intermediate = GenerateGridWithBombs(6, 8)
    DisplayGrid(intermediate)
    print()
    print("Advanced grid: ")
    advanced = GenerateGridWithBombs(8, 20)
    DisplayGrid(advanced)
    print()

## TASK 4.5
def GenerateBlankedGrid(size = 5):
    grid = [["-" for i in range(size)] for j in range(size)]
    return grid

# validation function for x and y, not needed in program code
def ValidXandY(x, y, size):
    if x.isdigit() and y.isdigit():
        x = int(x)
        y = int(y)
        if x > 0 and y > 0 and x <= size and y <= size:
            return True
    return False

def TASK45():
    TryAgain = True             # does the player wish to try again after game over?
    while TryAgain == True:
        DifficultyInput = ""
        Grid            = None      # the grid containing the bombs
        BlankGrid       = None      # the blanked-out grid
        GameOver        = False     # is the game finished?
        Score           = 0         # current game score
        MaxScore        = 0         # maximum possible score (score required to win)
        while DifficultyInput not in ["B", "I", "A"]:
            print("Select a level of difficulty here:")
            print("B - beginner     (5x5,  3 bombs)")
            print("I - intermediate (6x6,  8 bombs)")
            print("A - advanced     (8x8, 20 bombs)")
            DifficultyInput = input(">>> ")
            if DifficultyInput == "B":
                Grid = GenerateGridWithBombs(5, 3)
                BlankGrid = GenerateBlankedGrid(5)
                MaxScore = 5 * 5 - 3
            elif DifficultyInput == "I":
                Grid = GenerateGridWithBombs(6, 8)
                BlankGrid = GenerateBlankedGrid(6)
                MaxScore = 6 * 6 - 8
            elif DifficultyInput == "A":
                Grid = GenerateGridWithBombs(8, 20)
                BlankGrid = GenerateBlankedGrid(8)
                MaxScore = 8 * 8 - 20
            else:
                print("Level of difficulty entered is invalid.")
                print()

        while GameOver == False:
            DisplayGrid(BlankGrid)
            print("Enter your cell you want to open: ")
            x = ""
            y = ""
            while ValidXandY(x, y, len(Grid)) == False:
                x = input("X (1 to " + str(len(Grid)) + "): ")
                y = input("Y (1 to " + str(len(Grid)) + "): ")
                if ValidXandY(x, y, len(Grid)) == False:
                    print("The coordinates entered are invalid, please try again.")
                    print()
            x = int(x)
            y = int(y)
            if Grid[x - 1][y - 1] == "X":
                DisplayGrid(Grid)
                print()
                print("Game Over! You've hit the bomb at (" + str(x) + ", " + str(y) + ").")
                print("Your score is:", Score)
                TryA = input("Do you want to try again? (Y/N) ")
                print()
                GameOver = True
                if TryA == "Y" or TryA == "y":
                    TryAgain = True
                else:
                    TryAgain = False
            elif BlankGrid[x - 1][y - 1] != "-":
                # cell has already been opened.
                print("The cell at (" + str(x) + ", " + str(y) + ") has already been opened.")
                print("Your score is:", Score)
                print()
            else:
                Score += 1
                # all the possible cells have been opened
                if Score == MaxScore:
                    DisplayGrid(Grid)
                    print()
                    print("You have Won!")
                    print("Your score is:", Score)
                    print()
                    GameOver = True
                    TryAgain = False
                else:
                    BlankGrid[x - 1][y - 1] = Grid[x - 1][y - 1]
                    DisplayGrid(BlankGrid)
                    print("Your score is:", Score)
                    print()
            

        

        
                

