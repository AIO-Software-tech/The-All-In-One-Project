board = [] #List for holding the board

for x in range(6):
    board.append(["O"] * 7) #builds 7 x 6 board (rows x columns)

#function for printing the board
def print_board(board):  
    for row in board:
        print (" ".join(row))

print ('Welcome to Connect Four')

player_one = input('Player 1. Enter your name: ')
player_two = input('Player 2. Enter your name: ') #Gets players names

print ('%s vs. %s' % (player_one, player_two))
print ('--------------')
print (print_board(board))
print ('Player 1 is @ and Player 2 is #')
print ('Let\'s play!!') # Game's 'Opening'

turn = 0 #Keeps track of turn


while turn < 8: #debugging purposes

    if turn % 2 == 0: #Determines whose turn it is by checking for even or odd turn 

        print ('%s. Choose a column to drop your chip' % (player_one))
        one_choice = int(input('Column: ')) #Determines what column player will drop chip

       #Checks for 'empty slot' from bottom up and fills it with players 'chip'

        if (board[5][one_choice - 1] == 'O'):             
            board[5][one_choice - 1] = '@'
            print_board(board)
            turn += 1

        elif(board[4][one_choice - 1] == 'O'):
            board[4][one_choice - 1] = '@'
            print_board(board)
            turn += 1

        elif(board[3][one_choice - 1] == 'O'):
            board[3][one_choice - 1] = '@'
            print_board(board)
            turn += 1

        elif (board[2][one_choice - 1] == 'O'):
            board[2][one_choice - 1] = '@'
            print_board(board)
            turn += 1

        elif (board[1][one_choice - 1] == 'O'):
            board[1][one_choice - 1] = '@'
            print_board(board)
            turn += 1

        elif (board[0][one_choice - 1] == 'O'):
            board[0][one_choice - 1] = '@'
            print_board(board)
            turn += 1

        else:
            print ("Column is full!!")      
    else:         

        #Same as above for player 2
        print ('%s. Choose a column to drop your chip' % (player_two))
        one_choice = int(input('Column: '))

        if (board[5][one_choice - 1] == 'O'):
            board[5][one_choice - 1] = '#'
            print_board(board)
            turn += 1

        elif(board[4][one_choice - 1] == 'O'):
            board[4][one_choice - 1] = '#'
            print_board(board)
            turn += 1

        elif(board[3][one_choice - 1] == 'O'):
            board[3][one_choice - 1] = '#'
            print_board(board)
            turn += 1

        elif (board[2][one_choice - 1] == 'O'):
            board[2][one_choice - 1] = '#'
            print_board(board)
            turn += 1

        elif (board[1][one_choice - 1] == 'O'):
            board[1][one_choice - 1] = '#'
            print_board(board)
            turn += 1

        elif (board[0][one_choice - 1] == 'O'):
            board[0][one_choice - 1] = '#'
            print_board(board)
            turn += 1

        else:
            print ("Column is full!!")

     #Gets me out of loop for debugging
    if turn == 8:
        print ('Game Over man!')
