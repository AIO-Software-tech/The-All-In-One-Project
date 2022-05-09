# All-In-One By Imre Kiss And Oliver Boucher

# Imports

import time
import random
import sys

# Select Menu:

def menu():
    while True:
        print("Selection Menu: Please Select One Of The Options:")
        print("▣───────────────────────────────────────────────▣")
        print("│                                               │")
        print("│   1. = Personal                               │")
        print("│                                               │")
        print("│   2. = Calculations                           │")
        print("│                                               │")
        print("│   3. = Games                                  │")
        print("│                                               │")
        print("│   4. = List error codes                       │")
        print("│                                               │")
        print("▣───────────────────────────────────────────────▣")

        # Select Menu Enter:

        unit = int(input("Please Select One Of The Following Options 1,2,3,4: "))

        #Personal:
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
            print("▣─────────────────▣")

            PersonlMenu = int(input("Please Select One Of The Following Options 1,2,3: "))

            if PersonlMenu == 1:

                name1 = input("What Is Your Forename: ")
                name2 = input("What Is Your Surname: ")
                print("Your Name Is " + name1 + " " + name2)
                time.sleep(1)

            elif PersonlMenu == 2:
                userAge = int(input("What Is Your Age: "))
                yearBorn = 2022-userAge
                print("So You Were Born In " + str(yearBorn))
                time.sleep(1)

            elif PersonlMenu == 3:
                F3 = input("What Is The First 3 Digits Of Your Postcode ?")
                L3 = input("What Is The Last 3 Digits Of Your Postcode ?")
                print("Your Postcode Is: " +str(F3) + " " +str(L3))
                time.sleep(1)

        # Calculation
        elif unit == 2:
            print("Selection Menu: Please Select One Of The Options: ")
            print("▣─────────────────────────▣")
            print("│                         │")
            print("│   1. = Simple           │")
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
            print("▣─────────────────────────▣")

            CalculationMenu = int(input("Please Select One Of The Following Options 1,2,3,4,5,6: "))

            if CalculationMenu == 5:

         # Calculator: Riding System


                    ride = 0

                    def countdown(t):

                        while t:
                            mins, secs = divmod(t, 60)
                            timer = '{:02d}:{:02d}'.format(mins, secs)
                            print(timer, end="\r")
                            time.sleep(1)
                            t -= 1
                        count()

                    t = int(120)

                    def count():
                        ride = 0
                        while ride < 8:
                            print(" ")
                            rider = int(input("Please enter height in cm: "))

                            if rider >= 140:
                                print("Please ride")
                                ride = ride + 1
                            elif rider >= 120 and rider < 140:
                                adult = input("Are you an adult y/n: ")
                                if adult == "y":
                                    print("Please both ride!")
                                    ride = ride + 2
                                else:
                                    print("No ride!")
                            else:
                                print("No ride!")
                        print("The ride is full please wait")
                        print(" ")

                        countdown(int(t))

                    count()

            if CalculationMenu == 4:

                # Calculator: Voting System

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
                        sys.exit()

            elif CalculationMenu == 2:
       
                # Calculator: Converter

                    print("What Would You Like To covnert")
                    print("▣───────────────────▣")
                    print("│                   │")
                    print("│  1 = Km - Miles   │")
                    print("│                   │")
                    print("│  2 = Miles - Km   │")
                    print("│                   │")
                    print("│  3 = Kg - Lbs     │")
                    print("│                   │")
                    print("│  4 = Lbs - Kg     │")
                    print("│                   │")
                    print("│  5 = Cm - Inches  │")
                    print("│                   │")
                    print("│  6 = Inches - Cm  │")
                    print("│                   │")
                    print("▣───────────────────▣")

                    unit = int(input("Please Select One Of The Following Options 1,2,3,4,5,6: "))

                    if unit == 1:
                        km = int(input("How Many Km Do You Want To Convert? "))
                        print(str(km) + " is " + str(km * 0.621) + " Miles")
                        time.sleep(1)

                    elif unit == 2:
                        miles = int(input("How Many Miles Do You Want To Convert? "))
                        print(str(miles) + " is " + str(miles * 1.609) + " Km")
                        time.sleep(1)

                    elif unit == 3:
                        kg = int(input("How Many Kg Do You Want To Convert ? "))
                        print(str(kg) + " is " + str(kg * 0.453) + " Lbs")
                        time.sleep(1)

                    elif unit == 4:
                        pounds = int(input("How Many Pounds Do You Want To convert ? "))
                        print(str(pounds) + " is " + str(pounds * 2.2) + " Kg")
                        time.sleep(1)

                    elif unit == 5:
                        cm = int(input("How Many Cm Do You Want To Convert ? "))
                        print(str(cm) + " is " + str(cm / 2.54) + " Inches")
                        time.sleep(1)

                    elif unit == 6:
                        inch = int(input("How Many Inch Do You Want To Convert ? "))
                        print(str(inch) + " is " + str(inch * 2.54) + " Cm")
                        time.sleep(1)

                    else:
                        print("Please Only Enter 1,2,3,4,5,6")
                        time.sleep(1)

            elif CalculationMenu == 3:

                # Calculator: Rectangle Area

                    Width = float(input('Please Enter the Width of a Rectangle: '))
                    Height = float(input('Please Enter the Height of a Rectangle: '))

                    Area = Width * Height

                    Perimeter = 2 * (Width + Height)

                    print("Area Of A Rectangle Is: %.2f" % Area)
                    print("Perimeter Of Rectangle Is: %.2f" % Perimeter)

            elif CalculationMenu == 1:

                N1 = int(input("Enter First Number: "))
                N2 = int(input("Enter Second Number: "))

                print("Enter Which Operation Would You Like To Perform?")
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
                    print("Input character is not recognized!")

                print(N1, OP, N2, "=", Result)
                time.sleep(1)

            elif CalculationMenu == 6:

                BatteryCharge = int(input("Please Enter The Remaining Charge: "))
                if BatteryCharge == 100:
                    print("Fully Charged")
                    if BatteryCharge < 100 and BatteryCharge > 30:
                        print("Battery Low")

        #Games
        elif unit == 3:
            print("What Game would you like to play?")
            print("▣─────────────────────▣")
            print("│                     │")
            print("│  1 = Battle Ships   │")
            print("│                     │")
            print("│  2 = Coin Flip      │")
            print("│                     │")
            print("│  3 = Connect 4      │")
            print("│                     │")
            print("│  4 = Blank          │")
            print("│                     │")
            print("▣─────────────────────▣")

            gameSelecte = int(input("Please choose a game from the menu above 1,2,3,4: "))

            if gameSelecte == 1:
                from random import randint

                # Ship Class
                class Ship:
                    def __init__(self, size, orientation, location):
                        self.size = size

                        if orientation == 'horizontal' or orientation == 'vertical':
                            self.orientation = orientation
                        else:
                            raise ValueError("Value must be 'horizontal' or 'vertical'.")

                        if orientation == 'horizontal':
                            if location['row'] in range(row_size):
                                self.coordinates = []
                                for index in range(size):
                                    if location['col'] + index in range(col_size):
                                        self.coordinates.append({'row': location['row'], 'col': location['col'] + index})
                                    else:
                                        raise IndexError("Column is out of range.")
                            else:
                                raise IndexError("Row is out of range.")
                        elif orientation == 'vertical':
                            if location['col'] in range(col_size):
                                self.coordinates = []
                                for index in range(size):
                                    if location['row'] + index in range(row_size):
                                        self.coordinates.append({'row': location['row'] + index, 'col': location['col']})
                                    else:
                                        raise IndexError("Row is out of range.")
                            else:
                                raise IndexError("Column is out of range.")

                        if self.filled():
                            print_board(board)
                            print(" ".join(str(coords) for coords in self.coordinates))
                            raise IndexError("A ship already occupies that space.")
                        else:
                            self.fillBoard()

                    def filled(self):
                        for coords in self.coordinates:
                            if board[coords['row']][coords['col']] == 1:
                                return True
                        return False

                    def fillBoard(self):
                        for coords in self.coordinates:
                            board[coords['row']][coords['col']] = 1

                    def contains(self, location):
                        for coords in self.coordinates:
                            if coords == location:
                                return True
                        return False

                    def destroyed(self):
                        for coords in self.coordinates:
                            if board_display[coords['row']][coords['col']] == 'O':
                                return False
                            elif board_display[coords['row']][coords['col']] == '*':
                                raise RuntimeError("Board display inaccurate")
                        return True


                # Settings Variables
                row_size = 9  # number of rows
                col_size = 9  # number of columns
                num_ships = 4
                max_ship_size = 5
                min_ship_size = 2
                num_turns = 40

                # Create lists
                ship_list = []

                board = [[0] * col_size for x in range(row_size)]

                board_display = [["O"] * col_size for x in range(row_size)]


                # Functions
                def print_board(board_array):
                    print("\n  " + " ".join(str(x) for x in range(1, col_size + 1)))
                    for r in range(row_size):
                        print(str(r + 1) + " " + " ".join(str(c) for c in board_array[r]))
                    print()


                def search_locations(size, orientation):
                    locations = []

                    if orientation != 'horizontal' and orientation != 'vertical':
                        raise ValueError("Orientation must have a value of either 'horizontal' or 'vertical'.")

                    if orientation == 'horizontal':
                        if size <= col_size:
                            for r in range(row_size):
                                for c in range(col_size - size + 1):
                                    if 1 not in board[r][c:c + size]:
                                        locations.append({'row': r, 'col': c})
                    elif orientation == 'vertical':
                        if size <= row_size:
                            for c in range(col_size):
                                for r in range(row_size - size + 1):
                                    if 1 not in [board[i][c] for i in range(r, r + size)]:
                                        locations.append({'row': r, 'col': c})

                    if not locations:
                        return 'None'
                    else:
                        return locations


                def random_location():
                    size = randint(min_ship_size, max_ship_size)
                    orientation = 'horizontal' if randint(0, 1) == 0 else 'vertical'

                    locations = search_locations(size, orientation)
                    if locations == 'None':
                        return 'None'
                    else:
                        return {'location': locations[randint(0, len(locations) - 1)], 'size': size,
                                'orientation': orientation}


                def get_row():
                    while True:
                        try:
                            guess = int(input("Row Guess: "))
                            if guess in range(1, row_size + 1):
                                return guess - 1
                            else:
                                print("\nOops, that's not even in the ocean.")
                        except ValueError:
                            print("\nPlease enter a number")


                def get_col():
                    while True:
                        try:
                            guess = int(input("Column Guess: "))
                            if guess in range(1, col_size + 1):
                                return guess - 1
                            else:
                                print("\nOops, that's not even in the ocean.")
                        except ValueError:
                            print("\nPlease enter a number")


                # Create the ships

                temp = 0
                while temp < num_ships:
                    ship_info = random_location()
                    if ship_info == 'None':
                        continue
                    else:
                        ship_list.append(Ship(ship_info['size'], ship_info['orientation'], ship_info['location']))
                        temp += 1
                del temp


                def play_game():
                    print_board(board_display)

                    for turn in range(num_turns):
                        print("Turn:", turn + 1, "of", num_turns)
                        print("Ships left:", len(ship_list))
                        print()

                        guess_coords = {}
                        while True:
                            guess_coords['row'] = get_row()
                            guess_coords['col'] = get_col()
                            if board_display[guess_coords['row']][guess_coords['col']] == 'X' or \
                                    board_display[guess_coords['row']][guess_coords['col']] == '*':
                                print("\nYou guessed that one already.")
                            else:
                                break

                        ship_hit = False
                        for ship in ship_list:
                            if ship.contains(guess_coords):
                                print("Hit!")
                                ship_hit = True
                                board_display[guess_coords['row']][guess_coords['col']] = 'X'
                                if ship.destroyed():
                                    print("Ship Destroyed!")
                                    ship_list.remove(ship)
                                break
                        if not ship_hit:
                            board_display[guess_coords['row']][guess_coords['col']] = '*'
                            print("You missed!")

                        print_board(board_display)

                        if not ship_list:
                            break

                    # End Game
                    if ship_list:
                        print("You lose!")
                    else:
                        print("All the ships are sunk. You win!")


                # Play Game
                play_game()

            elif gameSelecte == 2:-
                
                # Coin Flip:

                def CoinFlip():
                    Result0 = ""
                    Flip = random.choice(["Heads", "Tails"])
                    Player = input("What Would You Guess Heads Or Tails ?: ")
                    print("The Computer Throws The Coin And It's " + Flip)
                    if Player == Flip:
                        Result0 = "Win"
                    else:
                        Result0 = "Lose"
                    return Result0

                def Score():
                    Score = 0
                    Result0 = CoinFlip()
                    if Result0 == "Win":
                        Score = Score + 1
                    else:
                        Score = Score - 1
                        Score = Score
                    return Score

                def Game():
                    ScoreY = 0
                    Turns = int(input("How Many Rounds Would You Like To Play ? "))
                    for i in range(Turns):
                        ScoreX = Score()
                        ScoreY = ScoreY + ScoreX
                        print(ScoreY)
                    Again()

                def Again():
                    Yes = "Yes"
                    No = "No"
                    Again = str(input("Do you want to play again: "))
                    if Again == str("Yes"):
                        Game()
                    elif Again == str("No"):
                        sys.exit()
                    elif Again == str("Menu"):
                        menu()

                Game()
            elif gameSelecte == 3:
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

                        else:
                            print("Error core: 1")
                            menu()

        # Errors
        elif unit == 4:

            print("▣────────────────────────────────▣")
            print("│                                │")
            print("│   1. = Invalid option/chose    │")
            print("│                                │")
            print("│   2. = Blank                   │")
            print("│                                │")
            print("│   3. = Blank                   │")
            print("│                                │")
            print("│   4. = Blank                   │")
            print("│                                │")
            print("▣────────────────────────────────▣")

            BackToMenu = input("Type 'Y or y' to go back to menu: ")
            if BackToMenu == "Y" or BackToMenu == "y":
                menu()

username = input("Username: ")
if username == "Ollie" or username == "Admin" or username == "Imre":
    password = input("Password: ")
    if username == "Ollie" and password == "#008701Boucher":
        menu()
    elif username == "Imre" and password == "n@KoRi<£":
        menu()
    elif username == "Admin" and password == "abc":
        menu()
    else:
        sys.exit()
else:
    sys.exit()


