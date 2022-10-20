#Done
#? Imports:
import time
import random
import sys
import platform

#Done 
#! Username and Password System:
def UserPass():
    #@ Who It Was Made By:
    print("All-In-One By Imre Kiss And Oliver Boucher")
    print(" ")
    print("Verstion 2.2.3 REV-1 2022")
    print(" ")
    username = input("Username: ")
    if username == "Ollie" or username == "Admin" or username == "Imre" or username == "Guest":
        password = input("Password: ")
        if username == "Ollie" and password == "#008701Boucher":
            Menu()
        elif username == "Imre" and password == "#008803Kiss":
            Menu()
        elif username == "Admin" and password == "abc":
            Menu()
        elif username == "Guest" and password == "123":
            Menu()
        else:
            print("Error code 2")
            UserPass()
    else:
        print("Error code 3")
        UserPass()

#Done
#? Select Menu:
def Menu():
    while True:
        print(" ")
        print("Selection Menu: Please Select One Of The Options:")
        print("▣───────────────────────────────────────────────▣")
        print("│                                               │")
        print("│   1. = Personal                               │")
        print("│                                               │")
        print("│   2. = Calculations                           │")
        print("│                                               │")
        print("│   3. = Games                                  │")
        print("│                                               │")
        print("│   4. = Error Codes                            │")
        print("│                                               │")
        print("│   5. = Close                                  │")
        print("│                                               │")
        print("▣───────────────────────────────────────────────▣")

        unit = int(input("Please Select One Of The Following Options 1,2,3,4: "))
        print()

        #Done
        #* Personal:
        if unit == 1:
            print("Selection Menu: Please Select One Of The Options: ")
            print("▣─────────────────▣")
            print("│                 │")
            print("│   1. = Name     │")
            print("│                 │")
            print("│   2. = Age      │")
            print("│                 │")
            print("│   3. = Address  │")
            print("│                 │")
            print("│   4. = Back     │")
            print("│                 │")
            print("▣─────────────────▣")

            PersonlMenu = int(input("Please Select One Of The Following Options 1,2,3: "))

            #Done
            #£ Name:
            if PersonlMenu == 1:
                name1 = input("What Is Your Forename: ")
                name2 = input("What Is Your Surname: ")
                print("Your Name Is " + name1 + " " + name2)
                time.sleep(1)

            #Done
            #£ Age:
            elif PersonlMenu == 2:
                userAge = int(input("What Is Your Age: "))
                yearBorn = 2022-userAge
                if yearBorn < 0:
                    print("Nice Try Kid.")
                else:
                    print("So You Were Born In " + str(yearBorn))
                    time.sleep(1)

            #Done
            #£ Address:
            elif PersonlMenu == 3:
                F3 = input("What Is The First 3 Digits Of Your Postcode ?")
                L4 = input("What Is The Last 4 Digits Of Your Postcode ?")
                print("Your Postcode Is: " +str(F3) + " " +str(L4))
                time.sleep(1)

            #Done
            #£ Go back to menu
            elif PersonlMenu == 3:
                Menu()

            #Done
            #£ Goes Back To The Main Menu
            else:
                Menu()
        #Done
        #* Calculations:
        elif unit == 2:
            print("Selection Menu: Please Select One Of The Options: ")
            print("▣─────────────────────────▣")
            print("│                         │")
            print("│   1. = Standard         │")
            print("│                         │")
            print("│   2. = Converter        │")
            print("│                         │")
            print("│   3. = Rectangle Area   │")
            print("│                         │")
            print("│   4. = Voting System    │")
            print("│                         │")
            print("│   5. = Riding System    │")
            print("│                         │")
            print("│   6. = Battery Charge   │")
            print("│                         │")
            print("│   7. = Rounding         │")
            print("│                         │")
            print("│   8. = Back             │")
            print("│                         │")
            print("▣─────────────────────────▣")

            CalculationMenu = int(input("Please Select One Of The Following Options 1,2,3,4,5,6: "))

            #Done
            #£ Standard:
            if CalculationMenu == 1:

                N1 = int(input("Enter First Number: "))
                N2 = int(input("Enter Second Number: "))

                print("Enter Which Operation Would You Like To Perform?:")
                OP = input("Enter One Of These Operations: | + | - | * | / | ")

                Result = 0
                if OP == '+':
                    Result = N1 + N2
                elif OP == '-':
                    Result = N1 - N2
                elif OP == '*':
                    Result = N1 * N2
                elif OP == '/':
                    Result = N1 / N2
                else:
                    print("Input Character Is Not Recognized.")

                print(N1, OP, N2, "=", Result)
                time.sleep(1)

            #Done
            #£ Converter:
            elif CalculationMenu == 2:
       
                    print("What Would You Like To Covnert?: ")
                    print("▣───────────────────▣")
                    print("│                   │")
                    print("│  1 = Km - Miles   │")
                    print("│                   │")
                    print("│  2 = Mi - Km      │")
                    print("│                   │")
                    print("│  3 = Kg - Lbs     │")
                    print("│                   │")
                    print("│  4 = Lb - Kg      │")
                    print("│                   │")
                    print("│  5 = Cm - Inches  │")
                    print("│                   │")
                    print("│  6 = In - Cm      │")
                    print("│                   │")
                    print("│  7 = Back         │")
                    print("│                   │")
                    print("▣───────────────────▣")

                    unit = int(input("Please Select One Of The Following Options: 1,2,3,4,5,6: "))

                    if unit == 1:
                        Km = int(input("How Many Km Do You Want To Convert?: "))
                        print(str(Km) + " Km is " + str(Km / 1.609) + " Mi.")
                        time.sleep(1)

                    elif unit == 2:
                        Mi = int(input("How Many Miles Do You Want To Convert?: "))
                        print(str(Mi) + " Mi is " + str(Mi * 1.609) + " Km.")
                        time.sleep(1)

                    elif unit == 3:
                        Kg = int(input("How Many Kg Do You Want To Convert?: "))
                        print(str(Kg) + " Kg is " + str(Kg * 2.205) + " Lb.")
                        time.sleep(1)

                    elif unit == 4:
                        Lb = int(input("How Many Lb Do You Want To convert?: "))
                        print(str(Lb) + " Lb is " + str(Lb / 2.205) + " Kg.")
                        time.sleep(1)

                    elif unit == 5:
                        Cm = int(input("How Many Cm Do You Want To Convert?: "))
                        print(str(Cm) + " Cm is " + str(Cm / 2.540) + " In.")
                        time.sleep(1)

                    elif unit == 6:
                        In = int(input("How Many In Do You Want To Convert?: "))
                        print(str(In) + " In is " + str(In * 2.540) + " Cm.")
                        time.sleep(1)

                    #Done
                    #£ Go back to menu
                    elif unit == 7:
                        Menu()

                    #Done
                    #£ Goes Back To The Main Menu
                    else:
                        Menu()


            #Done
            #£ Rectangle Area:
            elif CalculationMenu == 3:

                    Width = float(input('Please Enter The Width Of A Rectangle: '))
                    Height = float(input('Please Enter The Height Of A Rectangle: '))

                    Area = Width * Height

                    Perimeter = 2 * (Width + Height)

                    print("Area Of A Rectangle Is: %.2f" % Area)
                    print("Perimeter Of Rectangle Is: %.2f" % Perimeter)

            #Done
            #£ Voting System:
            elif CalculationMenu == 4:

                    TotalA = 0
                    TotalB = 0
                    TotalC = 0
                    TotalD = 0
                    TotalE = 0
                    TotalAll = 0
                    Vote = True

                    while Vote == True:

                        Cast = input("Please Case Your Vote For Candidate A, B, C, D or E: ")
                        if Cast == "A" or Cast == "a":
                            TotalA = TotalA + 1
                        elif Cast == "B" or Cast == "b":
                            TotalB = TotalB + 1
                        elif Cast == "C" or Cast == "c":
                            TotalC = TotalC + 1
                        elif Cast == "D" or Cast == "d":
                            TotalD = TotalD + 1
                        elif Cast == "E" or Cast == "e":
                            TotalE = TotalE + 1
                        elif Cast == "End" or Cast == "end":
                            Vote = False

                    print("Votes Cast For Candidate A: " + str(TotalA))
                    print("Votes Cast For Candidate B: " + str(TotalB))
                    print("Votes Cast For Candidate C: " + str(TotalC))
                    print("Votes Cast For Candidate D: " + str(TotalD))
                    print("Votes Cast For Candidate E: " + str(TotalE))
                    print("Total Amount Of Votes Cast: " + str(TotalA + TotalB + TotalC + TotalD + TotalE))
                    if TotalA > TotalB and TotalC and TotalD and TotalE:
                        print("Candidate A Wins The Poll.")
                    elif TotalB > TotalA and TotalC and TotalD and TotalE:
                        print("Candidate B Wins The Poll.")
                    elif TotalC > TotalA and TotalB and TotalD and TotalE:
                        print("Candidate C Wins The Poll.")
                    elif TotalD > TotalA and TotalB and TotalC and TotalE:
                        print("Candidate D Wins The Poll.")
                    elif TotalE > TotalA and TotalB and TotalC and TotalD:
                        print("Candidate E Wins The Poll.")
                    elif TotalA == TotalB and TotalC and TotalD and TotalE:
                        print("They All Draw.")
                        Menu()

            #Done
            #£ Riding System:
            elif CalculationMenu == 5:
                                ride = 0

                                def progressbar(it, prefix="", size=120, out=sys.stdout): # Python3.3+
                                    count = len(it)
                                    def show(j):
                                        x = int(size*j/count)
                                        print("{}[{}{}] {}/{}".format(prefix, "█"*x, "."*(size-x), j, count), 
                                                end='\r', file=out, flush=True)
                                    show(0)
                                    for i, item in enumerate(it):
                                        yield item
                                        show(i+1)
                                    print("\n", flush=True, file=out)

                                def count():
                                    ride = 0
                                    while ride < 8:
                                        print(" ")
                                        rider = int(input("Please Enter Your Height In Cm: "))

                                        if rider >= 140:
                                            print("Please Ride.")
                                            ride = ride + 1
                                        elif rider >= 120 and rider < 140:
                                            adult = input("Are You An Adult y/n: ")
                                            if adult == "y":
                                                print("Please Both Ride!")
                                                ride = ride + 2
                                            else:
                                                print("No Ride!")
                                        else:
                                            print("No Ride!")
                                    print("The Ride Is Full Please Wait.")
                                    print(" ")

                                    for i in progressbar(range(120), "Time Left: ", 60):
                                        time.sleep(2)

                                count()

            #Done
            #£ Battery:
            elif CalculationMenu == 6:

                BatteryCharge = int(input("Please Enter The Remaining Charge: "))
                if BatteryCharge == 100:
                    print("Fully Charged.")
                elif BatteryCharge < 100 and BatteryCharge > 0:
                    print("Battery Low.")

            #Done
            #£ Rounding caculator:
            elif CalculationMenu == 7:
                numIn = float(input("Please enter your number: "))
                numOut = round(numIn)
                print("Your rounded number is: ", numOut)

            #Done
            #£ Go back to menu
            elif CalculationMenu == 8:
                Menu()

            #Done
            #£ Goes Back To The Main Menu
            else:
                Menu()


        #Done
        #* Games:
        elif unit == 3:
            print("What Game would you like to play?:")
            print("▣──────────────────────────▣")
            print("│                          │")
            print("│  1 = Battle Ships        │")
            print("│                          │")
            print("│  2 = Coin Flip           │")
            print("│                          │")
            print("│  3 = Connect Four        │")
            print("│                          │")
            print("│  4 = Noughts And Crosses │")
            print("│                          │")
            print("│  5 = Doom                │")
            print("│                          │")
            print("│  6 = Back                │")
            print("│                          │")
            print("▣──────────────────────────▣")

            gameSelecte = int(input("Please Choose A Game From The Menu Above 1,2,3,4: "))

            #Done
            #£ Battle Ships:
            if gameSelecte == 1:
                
                from random import randint

                class Ship:
                    def __init__(self, size, orientation, location):
                        self.size = size

                        if orientation == 'Horizontal' or orientation == 'Vertical':
                            self.orientation = orientation
                        else:
                            raise ValueError("Value Must Be 'Horizontal' Or 'Vertical'.")

                        if orientation == 'Horizontal':
                            if location['Row'] in range(row_size):
                                self.coordinates = []
                                for index in range(size):
                                    if location['Col'] + index in range(col_size):
                                        self.coordinates.append({'Row': location['Row'], 'Col': location['Col'] + index})
                                    else:
                                        raise IndexError("Column Is Out Of Range.")
                            else:
                                raise IndexError("Row Is Out Of Range.")
                        elif orientation == 'Vertical':
                            if location['Col'] in range(col_size):
                                self.coordinates = []
                                for index in range(size):
                                    if location['Row'] + index in range(row_size):
                                        self.coordinates.append({'Row': location['Row'] + index, 'Col': location['Col']})
                                    else:
                                        raise IndexError("Row Is Out Of Range.")
                            else:
                                raise IndexError("Column Is Out Of Range.")

                        if self.filled():
                            print_board(board)
                            print(" ".join(str(coords) for coords in self.coordinates))
                            raise IndexError("A Ship Already Occupies That Space.")
                        else:
                            self.fillBoard()

                    def filled(self):
                        for coords in self.coordinates:
                            if board[coords['Row']][coords['Col']] == 1:
                                return True
                        return False

                    def fillBoard(self):
                        for coords in self.coordinates:
                            board[coords['Row']][coords['Col']] = 1

                    def contains(self, location):
                        for coords in self.coordinates:
                            if coords == location:
                                return True
                        return False

                    def destroyed(self):
                        for coords in self.coordinates:
                            if board_display[coords['Row']][coords['Col']] == 'O':
                                return False
                            elif board_display[coords['Row']][coords['Col']] == '*':
                                raise RuntimeError("Board Display Inaccurate")
                        return True

                row_size = 9  
                col_size = 9  
                num_ships = 4
                max_ship_size = 5
                min_ship_size = 2
                num_turns = 40

                ship_list = []

                board = [[0] * col_size for x in range(row_size)]

                board_display = [["O"] * col_size for x in range(row_size)]

                def print_board(board_array):
                    print("\n  " + " ".join(str(x) for x in range(1, col_size + 1)))
                    for r in range(row_size):
                        print(str(r + 1) + " " + " ".join(str(c) for c in board_array[r]))
                    print()


                def search_locations(size, orientation):
                    locations = []

                    if orientation != 'Horizontal' and orientation != 'Vertical':
                        raise ValueError("Orientation Must Have A Value Of Either 'Horizontal' Or 'Vertical'.")

                    if orientation == 'Horizontal':
                        if size <= col_size:
                            for r in range(row_size):
                                for c in range(col_size - size + 1):
                                    if 1 not in board[r][c:c + size]:
                                        locations.append({'Row': r, 'Col': c})
                    elif orientation == 'Vertical':
                        if size <= row_size:
                            for c in range(col_size):
                                for r in range(row_size - size + 1):
                                    if 1 not in [board[i][c] for i in range(r, r + size)]:
                                        locations.append({'Row': r, 'Col': c})

                    if not locations:
                        return 'None'
                    else:
                        return locations


                def random_location():
                    size = randint(min_ship_size, max_ship_size)
                    orientation = 'Horizontal' if randint(0, 1) == 0 else 'Vertical'

                    locations = search_locations(size, orientation)
                    if locations == 'None':
                        return 'None'
                    else:
                        return {'Location': locations[randint(0, len(locations) - 1)], 'Size': size,
                                'Orientation': orientation}


                def get_row():
                    while True:
                        try:
                            guess = int(input("Row Guess: "))
                            if guess in range(1, row_size + 1):
                                return guess - 1
                            else:
                                print("\nOops, That's Not Even In The Ocean.")
                        except ValueError:
                            print("\nPlease Enter A Number")


                def get_col():
                    while True:
                        try:
                            guess = int(input("Column Guess: "))
                            if guess in range(1, col_size + 1):
                                return guess - 1
                            else:
                                print("\nOops, That's Not Even In The Ocean.")
                        except ValueError:
                            print("\nPlease Enter A Number")

                temp = 0
                while temp < num_ships:
                    ship_info = random_location()
                    if ship_info == 'None':
                        continue
                    else:
                        ship_list.append(Ship(ship_info['Size'], ship_info['Orientation'], ship_info['Location']))
                        temp += 1
                del temp


                def play_game():
                    print_board(board_display)

                    for turn in range(num_turns):
                        print("Turn:", turn + 1, "Of", num_turns)
                        print("Ships Left:", len(ship_list))
                        print()

                        guess_coords = {}
                        while True:
                            guess_coords['Row'] = get_row()
                            guess_coords['Col'] = get_col()
                            if board_display[guess_coords['Row']][guess_coords['Col']] == 'X' or \
                                    board_display[guess_coords['Row']][guess_coords['Col']] == '*':
                                print("\nYou Guessed That One Already.")
                            else:
                                break

                        ship_hit = False
                        for ship in ship_list:
                            if ship.contains(guess_coords):
                                print("Hit!")
                                ship_hit = True
                                board_display[guess_coords['Row']][guess_coords['Col']] = 'X'
                                if ship.destroyed():
                                    print("Ship Destroyed!")
                                    ship_list.remove(ship)
                                break
                        if not ship_hit:
                            board_display[guess_coords['Row']][guess_coords['Col']] = '*'
                            print("You Missed!")

                        print_board(board_display)

                        if not ship_list:
                            break

                    if ship_list:
                        print("You Lose!")
                    else:
                        print("All The Ships Are Sunk. You win!")

                play_game()

            #Done
            #£ Coin Flip:
            elif gameSelecte == 2:
                
                import random
                    
                def CoinFlip():
                    NumCoinFlips = int(input("How Many Times Do You Want To Play?: "))
                    print()

                    score = 0   

                    for x in range(NumCoinFlips):
                        HeadsOrTails = input("Heads Or Tails: ")
                        print()
                        FlipResult = random.randint(1, 2)
                        if FlipResult == 1 and HeadsOrTails == "Heads" or HeadsOrTails =="heads":
                            print()
                            print("You Where Right")
                            score = score + 1
                            print ("Your Score Is: " + str(score))
                            print()
                            
                        elif FlipResult == 2 and HeadsOrTails == "Tails" or HeadsOrTails == "tails":
                            print()
                            print("You Where Right")
                            score = score + 1
                            print ("Your Score Is: " + str(score))
                            print()
                        
                        else:
                            print()
                            print("Wrong")
                            score = score - 1
                            print("Your Score Is: " + str(score))
                            print()
                    
                    print("Yes / No")
                    PlayAgain = input("Do You Want To Play Again: ")
                    
                    if PlayAgain == "Yes":
                        CoinFlip()

                    elif PlayAgain == "No":
                        Menu()
                    

                CoinFlip()

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
            #Done
            #£ Noughts And Crosses:
            elif gameSelecte == 4:
                import random

                class TicTacToe:

                    def __init__(self):
                        self.board = []

                    def create_board(self):
                        for i in range(3):
                            row = []
                            for j in range(3):
                                row.append('-')
                            self.board.append(row)

                    def get_random_first_player(self):
                        return random.randint(0, 1)

                    def fix_spot(self, row, col, player):
                        self.board[row][col] = player

                    def is_player_win(self, player):
                        win = None

                        n = len(self.board)

                        for i in range(n):
                            win = True
                            for j in range(n):
                                if self.board[i][j] != player:
                                    win = False
                                    break
                            if win:
                                return win

                        for i in range(n):
                            win = True
                            for j in range(n):
                                if self.board[j][i] != player:
                                    win = False
                                    break
                            if win:
                                return win

                        win = True
                        for i in range(n):
                            if self.board[i][i] != player:
                                win = False
                                break
                        if win:
                            return win

                        win = True
                        for i in range(n):
                            if self.board[i][n - 1 - i] != player:
                                win = False
                                break
                        if win:
                            return win
                        return False

                        for row in self.board:
                            for item in row:
                                if item == '-':
                                    return False
                        return True

                    def is_board_filled(self):
                        for row in self.board:
                            for item in row:
                                if item == '-':
                                    return False
                        return True

                    def swap_player_turn(self, player):
                        return 'X' if player == 'O' else 'O'

                    def show_board(self):
                        for row in self.board:
                            for item in row:
                                print(item, end=" ")
                            print()

                    def start(self):
                        self.create_board()

                        player = 'X' if self.get_random_first_player() == 1 else 'O'
                        while True:
                            print(f"Player {player} Turn")

                            self.show_board()

                            row, col = list(
                                            map(int, input("Enter Row And Column Numbers To Fix Spot e.g 1 1 or 3 3: ").split()))
                            print()

                            self.fix_spot(row - 1, col - 1, player)

                            if self.is_player_win(player):
                                print(f"Player {player} Wins The Game!")
                                break

                            if self.is_board_filled():
                                print("Match Draw!")
                                break

                            player = self.swap_player_turn(player)

                        print()
                        self.show_board()


                tic_tac_toe = TicTacToe()
                tic_tac_toe.start()

            #Done
            #£ Doom and Doom inports:
            elif gameSelecte == 5:
                try:
                    import main
                    import pygames
                    import numba
                    print("To Change Settings Open settings.py")
                    print("in running")
                    import main
                except ModuleNotFoundError:
                    print("'Doom' is not installed")
                    print("Download From: link")
                    print("You may need to install pygame and numba")
                    print("pip install pygame")
                    print("pip install numba")
                    time.sleep(1)

                
                


            #Done
            #£ Go back to menu
            elif gameSelecte == 6:
                Menu()

            #Done
            #£ Goes Back To The Main Menu
            else:
                Menu()

        #Done
        #* Error Codes:
        elif unit == 4:

            print("▣──────────────────────────────────▣")
            print("│                                   │")
            print("│   1. = Invalid option/chose       │")
            print("│                                   │")
            print("│   2. = Invalid Username or Pass   │")
            print("│                                   │")
            print("│   3. = Invalid input              │")
            print("│                                   │")
            print("▣──────────────────────────────────▣")
            
            print()
            print("Please Wait")
            time.sleep(2)
            Menu()

        #Done
        #£ Exits AIO
        elif unit == 5:
            sys.exit()

def versionChecker():
    version = platform.python_version()
    part1 = version[2]
    part2 = version[3]
    part3 = version[0]

    if int(part1) <= 6 and int(part2) == "." and int(part3) == 3:
        UserPass()

    else:
        print("please use AIO 3.7 Edition or Python 3.6")
versionChecker()