#Done
            #£ Connect 4:                    
            elif gameSelecte == 3:
                board = [] 

                for x in range(6):
                    board.append(["O"] * 7) 

                def print_board(board):  
                    for row in board:
                        print (" ".join(row))

                print ('Welcome To Connect Four')

                player_one = input('Player 1. Enter your name: ')
                player_two = input('Player 2. Enter your name: ') 

                print ('%s vs. %s' % (player_one, player_two))
                print ('--------------')
                print (print_board(board))
                print ('Player 1 is @ and Player 2 is #')
                print ('Let\'s play!') 

                turn = 0 

                while turn < 42: 

                    if turn % 2 == 0:  

                        print ('%s. Choose A Column To Drop Your Chip' % (player_one))
                        one_choice = int(input('Column: ')) 

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
                            print ("Column Is Full.")      
                    else:         

                        print ('%s. Choose A Column To Drop Your Chip' % (player_two))
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
                            print ("Column Is Full.")

                if turn == 42:
                    print ('Game Over.')

                else:
                    print("Error core: 1")
                    Menu()