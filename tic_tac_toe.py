# Tic Tac Toe Game

board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]
player = "X"
winner = None
gamerunning = True

def printBoard(board):
    print("\n")
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("---------")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("---------")
    print(board[6] + " | " + board[7] + " | " + board[8])
    print("\n")

def playerInput(board):
    inp = int(input(f"Player {player}, enter a number (1-9): "))
    if inp >= 1 and inp <= 9 and board[inp-1] == "-":
        board[inp-1] = player
    else:
        print("Oops! That spot's taken or invalid.")

def checkWin(board):
    # Rows
    for i in range(0, 9, 3):
        if board[i] == board[i+1] == board[i+2] != "-":
            return board[i]
    # Columns
    for i in range(3):
        if board[i] == board[i+3] == board[i+6] != "-":
            return board[i]
    # Diagonals
    if board[0] == board[4] == board[8] != "-":
        return board[0]
    if board[2] == board[4] == board[6] != "-":
        return board[2]
    return None

def checkTie(board):
    return "-" not in board

def switchPlayer(current):
    return "O" if current == "X" else "X"

# Game Loop
while gamerunning:
    printBoard(board)
    playerInput(board)
    winner = checkWin(board)
    if winner:
        printBoard(board)
        print(f"🎉 Player {winner} wins!")
        break
    elif checkTie(board):
        printBoard(board)
        print("🤝 It's a tie!")
        break
    player = switchPlayer(player)