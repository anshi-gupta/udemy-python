# The board
def display_board(board):
    
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('---|---|---')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('---|---|---')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])

test_board = ['#', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X']



# Taking a player input.
def player_input():
    marker = ''

    while marker != 'X' and marker != 'O':
        marker = input("Player 1: Choose X or O: ").upper()

    if marker == 'X':
        print('Player 1 is X. \nPlayer 2 is O')
    else:
        print('Player 1 is O. \nPlayer 2 is X')



# Taking the board list object, a marker ('X' or 'O'), at a desired position (number 1-9).
def place_marker(board, marker, position):
    board[position] = marker




# Check who has won
def  win_check(board, mark):

    return ((board[1] == board[2] == board[3] == mark) or   #first_row
    (board[3] == board[4] == board[5] == mark) or           #second_row 
    (board[7] == board[8] == board[9] == mark) or           #third_row
    (board[1] == board[4] == board[7] == mark) or           #first_column
    (board[2] == board[5] == board[8] == mark) or           #second_column 
    (board[3] == board[6] == board[9] == mark) or           #third_column
    (board[1] == board[5] == board[9] == mark) or           #diagonal
    (board[3] == board[5] == board[7] == mark))             #diagonal

# Checking which player goes first
import random

def choose_first_player():
    if random.randint(1, 2) == 1:
        print('Player 2')
    else:
        print('Player 1')




# To check if there is any space on the board 
def space_check(board, position):
    board_position = ' '
    return board_position




# To check if the board is full or not.
def board_check(board):
    for i in range(1, 10):
        if space_check(board, i):
            return True
        else:
            return False


# Asks for a player's next position (as a number 1-9) 
def player_choice(board):
    position = 0
    while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not space_check(board, position):
        position = int(input("Choose your next position: "))
    print(position)


# Asks the player if they want to play again 
def replay():
    print(input("Do you want to play again? \n Enter Yes or No: ").lower().startswith('y'))



# Run the game!!!
print("Welcome to Tic Tac Toe!!!")

while True:
    # Reset the board
    the_board = [' '] * 10
    player1_marker, player1_marker = player_input()
    turn = choose_first_player()
    print(turn + 'will go first.')

    play_game = input("Are you ready to play? Enter Yes or No: ")
    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == 'Player 1':

            # player1's turn
            display_board(the_board)
            position = player_choice(the_board)
            place_marker(the_board, player1_marker, position)

            if win_check(the_board, player1_marker):
                display_board(the_board)
                print("Congrats!!! Player 1 has won the game.")
                game_on = False
            else:
                if board_check(the_board):
                    display_board(the_board)
                    print("The game is draw.")
                    break
                else:
                    turn = 'Player 2'
        else:

            # player2's turn
            display_board(the_board)
            position = player_choice(the_board)
            place_marker(the_board, player2_marker, position)

            if win_check(the_board, player2_marker):
                display_board(the_board)
                print("Congrats!!! Player 2 has won the game.")
                game_on = False
            else:
                if board_check(the_board):
                    display_board(the_board)
                    print("The game is draw.")
                    break
                else:
                    turn = 'Player 1'

    if not replay():
        break





         
