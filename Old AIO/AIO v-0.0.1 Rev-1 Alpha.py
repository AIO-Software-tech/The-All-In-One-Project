#All In One By Imre Kiss And Oliver Boucher

#Imports

import time
import random
import sys

#Select Menu:

while True:
    print("Selection Menu: Please Select One Of The Options: ")
    print("▣────────────────────────────────────────────────▣")
    print("│                                                │")
    print("│   1. = Name                                    │")
    print("│                                                │")
    print("│   2. = Age                                     │")
    print("│                                                │")
    print("│   3. = Address                                 │")
    print("│                                                │")
    print("│   4. = Coin Flip                               │")
    print("│                                                │")
    print("│   5. = Calculator: Simple                      │")
    print("│                                                │")
    print("│   6. = Calculator: Rectangle Area              │")
    print("│                                                │")
    print("│   7. = Calculator: Converter                   │")
    print("│                                                │")
    print("│   8. = Calculator: Voting System               │")
    print("│                                                │")
    print("▣────────────────────────────────────────────────▣")

     #Select Menu Enter:
    
    unit = int(input("Please Select One Of The Following Options 1,2,3,4,5,6,7,8: "))

     #Name:
    
    if unit == 1:
        Name1 = input ("What Is Your Forename: ")
        Name2 = input ("What Is Your Surname: ")
        print("Your Name Is " + Name1 + " " + Name2)
        time.sleep(1)
        
    #_______________________________________________________________________________________________________________________________________________________________________

     #Age:
    
    elif unit == 2:
        UserAge = int(input("What Is Your Age: "))
        YearBorn = 2022-UserAge      
        print("So You Were Born In " + str(YearBorn))
        time.sleep(1)
        
    #_______________________________________________________________________________________________________________________________________________________________________

     #Address:
    
    elif unit == 3:
        F3 = input ("What Is The First 3 Digits Of Your Postcode ?")
        L3 = input ("What Is The Last 3 Digits Of Your Postcode ?")
        print ("Your Postcode Is: " +str(F3) + " " +str(L3))
        time.sleep(1)

    #_______________________________________________________________________________________________________________________________________________________________________

     #Coin Flip:

    elif unit == 4:

        def CoinFlip():
            Result0 = ""
            Flip = random.choice(["Heads","Tails"])
            Player = input("What Would You Guess Heads Or Tails ?: ")
            print ("The Computer Throws The Coin And It's " +Flip)
            if Player == Flip:
                Result0 = "Win"
            else:
                Result0 = "Lose"
            return Result0

        def Score():
            Score = 0
            Result0 = CoinFlip()
            if Result0 == "Win":
                Score = Score +1
            else:
                Score = Score -1
                Score = Score
            return Score

        def Game():
            ScoreY = 0
            Turns = int(input("How Many Rounds Would You Like To Play ? "))
            for i in range (Turns):
                ScoreX = Score()
                ScoreY = ScoreY + ScoreX
                print (ScoreY)
            Again()

        def Again():
            Yes = "Yes"
            No = "No"
            Again = str(input("Do you want to play again: "))
            if Again == str(Yes):
                Game()
            elif Again == str(No):
                sys.exit()
            elif Again == str(Menu):
                Menu()

        Game()

    #_______________________________________________________________________________________________________________________________________________________________________

     #Calculator: Addition / Subtraction

    if unit == 5:
        N1 = int(input("Enter First Number: "))
        N2 = int(input("Enter Second Number: "))

        print("Enter which operation would you like to perform?")
        OP = input("Enter any of these char for specific operation + | - | * | / : ")

        Eesult = 0
        if OP == '+':
          Result = N1 + N2
        elif OP == '-':
            Result = N1 - N2
        elif OP == '*':
            Result = N1 * N2
        elif OP == '/':
            Eesult = N1 / N2
        else:
            print("Input character is not recognized!")

        print(N1, OP , N2, ":", Result)
        time.sleep(1)

    #_______________________________________________________________________________________________________________________________________________________________________

     #Calculator: Rectangle Area

    if unit == 6:
        Width = float(input('Please Enter the Width of a Rectangle: '))
        Height = float(input('Please Enter the Height of a Rectangle: '))
        
        Area = Width * Height
         
        Perimeter = 2 * (Width + Height)
         
        print("Area of a Rectangle is: %.2f" %Area)
        print("Perimeter of Rectangle is: %.2f" %Perimeter)
        sys.exit()

    #_______________________________________________________________________________________________________________________________________________________________________

     #Calculator: Converter

    if unit ==7:
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
            print(str(km) + " is " + str(km*0.621) + " Miles")
            time.sleep(1)
        
        elif unit == 2:
            miles = int(input("How Many Miles Do You Want To Convert? "))
            print(str(miles) + " is " + str(miles*1.609) + " Km")
            time.sleep(1)
        
        elif unit == 3:
            kg = int(input("How Many Kg Do You Want To Convert ? "))
            print(str(kg) + " is " + str(kg*0.453) + " Lbs")
            time.sleep(1)
        
        elif unit == 4:
            pounds = int(input("How Many Pounds Do You Want To convert ? "))
            print(str(pounds) + " is " + str(pounds*2.2) + " Kg")
            time.sleep(1)
        
        elif unit == 5:
            cm = int(input("How Many Cm Do You Want To Convert ? "))
            print(str(cm) + " is " + str(cm/2.54) + " Inches")
            time.sleep(1)
        
        elif unit == 6:
            inch = int(input("How Many Inch Do You Want To Convert ? "))
            print(str(inch) + " is " + str(inch*2.54)+ " Cm")
            time.sleep(1)
        
        else:
            print("Please Only Enter 1,2,3,4,5,6")
            time.sleep(1)

    #_______________________________________________________________________________________________________________________________________________________________________

     #Calculator: Voting System

    if unit == 8:
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

        print("Votes Cast For Candidate A: "+str(TotalA))
        print("Votes Cast For Candidate B: "+str(TotalB))
        print("Votes Cast For Candidate C: "+str(TotalC))
        print("Votes Cast For Candidate D: "+str(TotalD))
        print("Votes Cast For Candidate E: "+str(TotalE))
        print("Total Amount Of Votes Cast: "+str(TotalA  + TotalB + TotalC + TotalD + TotalE))
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