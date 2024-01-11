import random

def display_board(board):
    print(board[7]+' | '+board[8]+' | '+board[9])
    print('---'*3)
    print(board[4]+' | '+board[5]+' | '+board[6])
    print('---'*3)
    print(board[1]+' | '+board[2]+' | '+board[3])

def player_input():
    accepted_markers = ['x', 'X', 'o', 'O']
    marker = ''
    
    while marker not in accepted_markers:
        marker = input("Player 1, please select your marker: X or O?")
        if marker not in accepted_markers:
            print("Sorry! That is not a valid marker option")
    
    player1 = marker.upper()
    
    if player1 == 'X':
        player2 = 'O'
    else:
        player2 = 'X'
    
    return (player1,player2)

def choose_first():
    first_player = ''
    
    result = random.randint(0,1)
    
    if result == 0:
        first_player = player1_marker
    else:
        first_player = player2_marker
    
    return first_player

def player_choice(board):
    accepted_choices = ['1','2','3','4','5','6','7','8','9']
    
    position = ''
    while position not in accepted_choices:
        position = input("Where would you like to place your marker? (1-9)")
        if position not in accepted_choices:
            print("Sorry! That is not a valid position")
    
    while space_check(board, int(position)) == False:
        position = input("Sorry! That space is taken. Please select a different place")
    
    return int(position)

def place_marker(board, marker, position):  
    board[position] = marker

def space_check(board, position): 
    if board[position] == 'X' or board[position] == 'O':
        return False
    else:
        return True

def full_board_check(board):
    board_positions = list(range(1,10))
    
    is_full = True
    
    for cell in board_positions:
        if space_check(board, cell):
            is_full = False
    return is_full

def win_check(board, mark): 
    winning_cells = [[1,2,3],[4,5,6],[7,8,9], [1,4,7],[2,5,8],[3,6,9], [1,5,9],[3,5,7]]
    
    for cell_set in winning_cells:
        is_winner = []
        for cell in cell_set:
            if board[cell] == mark:
                is_winner.append(True)
            else:
                is_winner.append(False)
        
        if False not in is_winner:
            return True

def replay():
    accepted_inputs = ['Y','y','N','n']
    
    replay = ''
    while replay not in accepted_inputs:
        replay = input("Do you want to play again? y/n")
        if replay not in accepted_inputs:
            print("Sorry! That is not a valid response. Please enter 'y' or 'n'")
    
    if replay.lower() == 'y':
        return True

if __name__ == '__main__':
    print('Welcome to Tic Tac Toe')

    # WHILE LOOP to keep running the game
    while True:
        
        # Play the game
        
        ## Set everything up
        the_board = [' ']*10
        player1_marker,player2_marker = player_input()
        
        turn = choose_first()
        print(turn + ' will go first')
        
        play_game = input('Ready to play? y/n')
        if play_game == 'y':
            game_on = True
        else:
            game_on = False
        
        ## Game play
        while game_on:
            if turn == 'X':
                # Show board
                display_board(the_board)
                # Choose position
                position = player_choice(the_board)
                # Place marker
                place_marker(the_board,'X',position)
                # Check if win
                if win_check(the_board,'X'):
                    display_board(the_board)
                    print('X has won!')
                    game_on = False
                # Check if tie
                else:
                    if full_board_check(the_board):
                        display_board(the_board)
                        print('Tie game')
                        game_on = False
                    #If no tie and no win, next turn
                    else:
                        turn = 'O'
                    
            else:
                # Show board
                display_board(the_board)
                # Choose position
                position = player_choice(the_board)
                # Place marker
                place_marker(the_board,'O',position)
                # Check if win
                if win_check(the_board,'O'):
                    display_board(the_board)
                    print('O has won!')
                    game_on = False
                # Check if tie
                else:
                    if full_board_check(the_board):
                        display_board(the_board)
                        print('Tie game')
                        game_on = False
                    #If no tie and no win, next turn
                    else:
                        turn = 'X'
        
        if not replay():
            print("Thanks for playing!")
            break