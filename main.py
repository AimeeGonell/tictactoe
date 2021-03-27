# Tic Tac Toe Game

"""

How does it work?
The game has a board with 9 even squares (3 x 3).
The players must choose one position, from 1-9.
board = 
    |-1-|-2-|-3-|
    -------------
    |-4-|-5-|-6-|
    -------------
    |-7-|-8-|-9-|

* If the players enter anything different from 1-9: tell them to try again.
* Check if the player chose a position that is already taken or not:
    - if yes, player must try again,
    - if not, mark it in the board.
* Check if any of the players won: checking complete rows, complete columns, or complete diagonals.
* Each player should play after the other player's turn, until one of 
the two wins, or there is a tie (after 9 turns).

"""

# Build the game board
game_board = [
    ["-|", "-|", "-"],
    ["-|", "-|", "-"],
    ["-|", "-|", "-"]
]

# Display the game board
def display_board(game_board):
    for row in game_board:
        for value in row:
            print(value, end="")
        print()

# when player is True, it refers to 'x', on the contrary, it means 'o'
player = True

# Variable to count the turns
turns = 0

# How to exit the game
def exit_game(player_input):
    if player_input == "e":
        print("Goodbye!")
        return True
    else:
        return False

# check if it is a valid play(if the player_input is a number from 1 to 9)
def check_play(player_input):
    if not play_number(player_input):
        return False
    player_input = int(player_input)
    if not valid_number(player_input):
        return False
    return True

# PLayer's time to choose a position and play
def play_number(player_input):
    if not player_input.isnumeric():
        print("Please enter a valid number (1 - 9)")
        return False
    else:
        return True

# Check if the player input is a valid number
def valid_number(player_input):
    if player_input > 9 or player_input < 1:
        print("This is not a valid number.")
        return False
    else:
        return True

# Check if the position is already taken or not
def is_taken(coordinates, game_board):
    row = coordinates[0]
    column = coordinates[1]
    if game_board[row][column] != "-" and game_board[row][column] != "-|":
        print("This position is already taken.")
        return True
    else:
        return False

def position(player_input):
    row = int(player_input / 3)
    column = (player_input)
    if column > 2: 
        column = int(column % 3)
    return (row,column)


def add_position(coordinates, game_board, active_player):
    row = coordinates[0]
    column = coordinates[1]
    game_board[row][column] = active_player

# player's turn
def current_player(player):
    if player:
        return "x "
    else:
        return "o "

# check possible ways to win: complete row, column or diagonal
def check_row(player, game_board):
    for row in game_board:
        complete_row = True
        for position in row:
            if position != player:
                complete_row = False
                break
        if complete_row:
            return True
    return False

def check_column(player, game_board):
    for column in range(3):
        complete_column = True
        for row in range(3):
            if game_board[row][column] != player:
                complete_column = False
                break
        if complete_column:
            return True
    return False

def check_diagonal(player, game_board):
    # From top left to bottom right
    if game_board[0][0] == player and game_board[1][1] == player and game_board[2][2] == player:
        return True
    # From bottom left to top right
    elif game_board[0][2] == player and game_board[1][1] == player and game_board[2][0] == player:
        return True
    else:
        return False

# Check if any player won the game
def win_game(player, game_board):
    if check_row(player, game_board):
        return True
    if check_column(player, game_board):
        return True
    if check_diagonal(player, game_board):
        return True
    return False 

# Game Loop for a single game of Tic Tac Toe
while turns >= 0 and turns < 9:
    active_player = current_player((player))
    display_board(game_board)
    player_input = input("Enter a position 1 through 9, or enter \"e\" to exit game: ") 
    if exit_game(player_input):
        break
    if not check_play(player_input):
        print("Please try again")
        continue
    player_input = int(player_input) - 1
    coordinates = position(player_input)
    if is_taken(coordinates, game_board):
        print("Please choose another position")
        continue
    add_position(coordinates, game_board, active_player)
    if win_game(active_player, game_board):
        print(f"{active_player.upper()} won!")
        break
    turns += 1
    if turns == 9:
        print("It's a Tie!")
    player = not player
