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

import utils

# Build the game board
game_board = [
    ["-|", "-|", "-"],
    ["-|", "-|", "-"],
    ["-|", "-|", "-"]
]

# when player is True, it refers to 'x', on the contrary, it means 'o'
player = True

# Variable to count the turns
turns = 0

# Game Loop for a single game of Tic Tac Toe
while turns >= 0 and turns < 9:
    active_player = utils.current_player((player))
    utils.display_board(game_board)
    player_input = input("Enter a position 1 through 9, or enter \"e\" to exit game: ") 
    if utils.exit_game(player_input):
        break
    if not utils.check_play(player_input):
        print("Please try again")
        continue
    player_input = int(player_input) - 1
    coordinates = utils.position(player_input)
    if utils.is_taken(coordinates, game_board):
        print("Please choose another position")
        continue
    utils.add_position(coordinates, game_board, active_player)
    if utils.win_game(active_player, game_board):
        print(f"{active_player.upper()} won!")
        break
    turns += 1
    if turns == 9:
        print("It's a Tie!")
    player = not player
