
def print_board(board): #defines a function; as a named box of instructions
    print() #prints a blank line for spacing.
    print(board[0], "|", board[1], "|", board[2]) #Gives the value stored at position 0 in the list
    print("--+---+--") #prints separator lines.
    print(board[3], "|", board[4], "|", board[5])
    print("--+---+--")
    print(board[6], "|", board[7], "|", board[8])
    print()

def player_move(board, player): #function that: Takes the board, Takes the current player ("X" or "O")
    while True:
        move = input(f"Player {player}, choose a position (0-8): ") #accept user input, Stores the input as a string
        if move.isdigit(): #Is the input made only of digits?
            move = int(move) #Convert user input to integ
            if 0 <= move <= 8 and board[move] == " ": #Two checks: Is the number between 0 and 8?, Is that board spot empty? Both must be true.
                board[move] = player #add "X" or "O" into the board list.
                break
            else:
                print("Invalid move. Try again.")
        else:
            print("Please enter a number.")

def check_winner(board, player): #function check if someone won.
    win_conditions = [
        (0,1,2), (3,4,5), (6,7,8),  # rows # a list of tuples representing all possible winning lines.
        (0,3,6), (1,4,7), (2,5,8),  # columns
        (0,4,8), (2,4,6)            # diagonals
    ]
    for a, b, c in win_conditions: #Loops through each winning combination
        if board[a] == board[b] == board[c] == player: #Are all three positions equal to the player symbol?
            return True
    return False

def check_draw(board): #Defines draw check, If there are no empty spaces left, it’s a draw.
    return " " not in board

#-------Main Game Logic-------
def play_game():
    board = [" " for _ in range(9)] #Creates a list called board, serves as a container that holds values
    current_player = "X" #Player X starts

    while True:
        print_board(board) #Shows the board
        player_move(board, current_player) #Lets the player make a move.

        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break

        if check_draw(board):
            print_board(board)
            print("It's a draw!")
            break

        current_player = "O" if current_player == "X" else "X" #Switch players

play_game() #Starts game 




