def InitialiseBoard():
    # 6 rows, 7 columns
    board = [["-" for col in range(7)] for row in range(6)]
    return board

def SetUpGame():
    GameFinished = False
    ThisPlayer   = "O"
    return (GameFinished, ThisPlayer)

def OutputBoard(board):
    output = "{:7}".format("")

    # heading row
    for i in range(7):
        output += "{:<7}".format(i + 1)

    output += "\n"

    for row in range(6):

        # heading column
        output += "{:<7}".format(row + 1)

        for col in range(7):
            output += "{:<7}".format(board[row][col])

        output += "\n"

    print(output)

def MoveValid(board, colno):
    # returns:
    #  1 if valid!
    # -1 if not valid move number
    # -2 if top row is full
    
    if (colno.isdigit() and int(colno) >= 1 and int(colno) <= 7):
        if board[0][int(colno) - 1] != "-":  # top row has been filled
            return -2
        else:
            return 1
    else:
        return -1
            

def ThisPlayerMakesMove(board, player):
    print("Player {}'s turn".format(player))
    colno = ""  # column number
    while MoveValid(board, colno) != 1:
        colno = input("Enter a valid column number (1 - 7): ")
        if MoveValid(board, colno) == -1:
            print("The move entered is invalid.")
            print()
        elif MoveValid(board, colno) == -2:
            print("The column to insert to is full!")
            print()
            
    colno = int(colno)
    
    # check where to put the new token
    for i in range(6):  # number of rows = 6
        rowno = 5 - i
        if board[rowno][colno - 1] == "-":
            board[rowno][colno - 1] = player
            break

    # returns board and the position of the new token added
    return (board, (rowno, colno - 1)) 

def CheckIfThisPlayerHasWon(board, LastMove):
    # RETURNS:
    #  0: drawn game
    #  1: player has won
    # -1: player has not won
    row, col = LastMove
    player   = board[row][col]
    IsDrawn  = True

    # check for drawn game
    for i in range(6):
        for j in range(7):
            if board[i][j] == "-":
                IsDrawn = False
                break

    if IsDrawn:
        return 0
    
    # check the row
    LastCol = 0
    LastRow = 0
    InACol  = 1
    InARow  = 1
    for i in range(7):  # number of columns = 7
        if board[row][i] == player:
            if i - LastCol == 1:
                InARow += 1
            else:
                InARow =  1
            LastCol = i
        if InARow == 4:
            return 1

    # check the column
    for i in range(6):  # number of rows = 6
        if board[i][col] == player:
            if i - LastRow == 1:
                InACol += 1
            else:
                InACol =  1
            LastRow = i
        if InACol == 4:
            return 1
        
    return -1
    

def SwapThisPlayer(player):
    if player == "X":
        player = "O"
    else:
        player = "X"
    return player


board = InitialiseBoard()
GameFinished, ThisPlayer = SetUpGame()
LastMove = (-1, -1)  # last token made
OutputBoard(board)
while GameFinished == False:
    board, LastMove = ThisPlayerMakesMove(board, ThisPlayer)
    OutputBoard(board)
    GameStatus = CheckIfThisPlayerHasWon(board, LastMove)
    if GameStatus == 1 or GameStatus == 0:  # drawn or won game
        GameFinished = True
    if GameStatus == 1:
        print("Player {} has won!!".format(ThisPlayer))
        print()
    elif GameStatus == 0:
        print("The game is drawn.")
        print()
    if GameFinished == False:
        ThisPlayer = SwapThisPlayer(ThisPlayer)
