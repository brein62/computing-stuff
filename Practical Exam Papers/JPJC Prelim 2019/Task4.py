puzzle1 = [[8,2,5,4,7,1,3,9,6],
           [1,9,4,3,2,6,5,7,8],
           [3,7,6,9,8,5,2,4,1],
           [5,1,9,7,4,3,8,6,2],
           [6,3,2,5,9,8,4,1,7],
           [4,8,7,6,1,2,9,3,5],
           [2,6,3,1,5,9,7,8,4],
           [9,4,8,2,6,7,1,5,3],
           [7,5,1,8,3,4,6,2,9]]

puzzle2 = [[2,4,8,3,9,5,7,1,6],[5,7,1,6,2,8,3,4,9],[9,3,6,7,4,1,5,8,2],
[6,8,2,5,3,9,1,7,4],[3,5,9,1,7,4,6,2,8],[7,1,4,8,6,9,2,5,3],
[8,6,3,4,1,7,2,9,5],[1,9,5,2,8,6,4,3,7],[4,2,7,9,5,3,8,6,1]]

puzzle3 = [[1,7,5,8,3,9,4,2,6],[6,3,8,2,7,4,9,1,5],[4,2,9,6,5,1,3,7,8],[8,1,6,3,9,5,7,4,2],
[5,4,7,1,6,2,8,3,9],[2,9,3,4,7,8,6,5,1],[7,5,4,9,2,6,1,8,3],[9,8,1,5,4,3,2,6,7],[3,6,2,7,1,5,8,9,4]]

## TASK 4.1
print("TASK 4.1")
def displayboard(board):
    # output string
    output = ""
    for i in range(9):
        for j in range(9):
            output += str(board[i][j])
            output += " "
        output += "\n"
    
    print(output)

print("puzzle1 as a 9 x 9 Sudoku puzzle:")
displayboard(puzzle1)

## TASK 4.2
# function checks whether there is exactly one of 1 to 9 in the array
def checkArray(array):
    for i in range(1, 9 + 1):
        count = 0
        for element in array:
            if element == i:
                count += 1
        if count != 1:
            return False
    return True
    
def checkRow(board):
    for row in board:
        result = checkArray(row)
        if result == False:
            return False
    return True

## TASK 4.3
def checkColumn(board):
    for columnNo in range(9):
        col = []
        for rowNo in range(9):
            col.append(board[rowNo][columnNo])
        result = checkArray(col)
        if result == False:
            return False
    return True

## TASK 4.4
def checkBlock(board):

    # in a 3x3 block, the indices are:
    # [3i][3j]       [3i][3j + 1]       [3i][3j + 2]
    # [3i + 1][3j]   [3i + 1][3j + 1]   [3i + 1][3j + 2]
    # [3i + 2][3j]   [3i + 2][3j + 1]   [3i + 2][3j + 2]
    
    for i in range(3):
        for j in range(3):
            block = []
            for k in range(3):
                for l in range(3):
                    block.append(board[3 * i + k][3 * j + l])
            
            result = checkArray(block)
            if result == False:
                return False
    return True

## TASK 4.5
print("\nTASK 4.5")
def checkSudoku(board):
    print("Preview of board: ")
    displayboard(board)
    RowResult   = checkRow(board)
    ColResult   = checkColumn(board)
    BlockResult = checkBlock(board)
    if RowResult == True and ColResult == True and BlockResult == True:
        print("The puzzle is valid!")
    else:
        print("This puzzle is invalid due to invalidity in the:")
        if RowResult == False:
            print("- row")
        if ColResult == False:
            print("- column")
        if BlockResult == False:
            print("- block")
    print()

print("PUZZLE1:")
checkSudoku(puzzle1)
print("PUZZLE2:")
checkSudoku(puzzle2)
print("PUZZLE3:")
checkSudoku(puzzle3)
