# Task 2
def CreateBoard():
    board = [[4, 3, 2, 1], \
             [1, 2, 4, 3], \
             [3, 4, 1, 2], \
             [2, 1, 3, 4]]
    return board

def OutputBoard(board):
    output = ""
    for i in range(4):                  # for each row in the board
        for j in range(4):              # for each cell in the row
            cell = str(board[i][j])
            if j == 3 and i == 3:       # last cell on the last row
                output += cell
            elif j == 3:                # last cell in the row
                output += cell + "\n"
            else:
                output += cell + " "
    return output

def DisplayBoard(board):
    print(OutputBoard(board))

# Task 3
import random

# Transformation 1: Swaps two rows in the same quadrant
def Transform1(board):
    PossibleSwaps = [(0, 1), (2, 3)]
    
    # randomly chooses the rows to swap
    RowsToSwap    = PossibleSwaps[random.randint(0, 1)]

    # swaps the two rows
    board[RowsToSwap[0]], board[RowsToSwap[1]] = board[RowsToSwap[1]], board[RowsToSwap[0]]

    return board

# Transformation 2: Swaps two columns in the same quadrant
def Transform2(board):
    PossibleSwaps = [(0, 1), (2, 3)]
    
    # randomly chooses the columns to swap
    ColumnsToSwap = PossibleSwaps[random.randint(0, 1)]

    # for every row
    for i in range(4):

        # swaps the two columns/cells in each row
        board[i][ColumnsToSwap[0]], board[i][ColumnsToSwap[1]] = board[i][ColumnsToSwap[1]], board[i][ColumnsToSwap[0]]

    return board
        
# Transformation 3: Swaps the top and bottom quadrant rows entirely
def Transform3(board):
    board[0], board[2] = board[2], board[0]     # swaps 1st and 3rd rows
    board[1], board[3] = board[3], board[1]     # swaps 2nd and 4th rows
    return board

# Transformation 4: Swaps the left and right quadrant columns entirely
def Transform4(board):

    # for every row
    for i in range(4):
        board[i][0], board[i][2] = board[i][2], board[i][0]     # swaps 1st and 3rd column/cell in row
        board[i][1], board[i][3] = board[i][3], board[i][1]     # swaps 2nd and 4th column/cell in row

    return board

def Transform(board):
    Transformations = []                    # list of transformations
    while len(Transformations) < 2:
        ToAdd = random.randint(1, 4)
        if ToAdd in Transformations:        # is already a transformation to be performed
            continue                        # do not add to list of transformations
        else:
            Transformations += [ToAdd]

    # display original board
    DisplayBoard(board)
    
    # for each transformation to be done
    for i in range(2):
        print()
        if Transformations[i] == 1:
            print("Transformation 1: Swaps two rows in the same quadrant")
            board = Transform1(board)
            DisplayBoard(board)             # display board after each transformation done
        elif Transformations[i] == 2:
            print("Transformation 2: Swaps two columns in the same quadrant")
            board = Transform2(board)
            DisplayBoard(board)             # display board after each transformation done
        elif Transformations[i] == 3:
            print("Transformation 3: Swaps the top and bottom quadrant rows entirely")
            board = Transform3(board)
            DisplayBoard(board)             # display board after each transformation done
        else:
            print("Transformation 4: Swaps the left and right quadrant columns entirely")
            board = Transform4(board)
            DisplayBoard(board)             # display board after each transformation done
            
    return board
