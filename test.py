import random
    
def CoinFlip():
    NumCoinFlips = int(input("How many times do you want to play?: "))
    print()

    score = 0   

    for x in range(NumCoinFlips):
        HeadsOrTails = input("Heads or Tails: ")
        print()
        FlipResult = random.randint(1, 2)
        if FlipResult == 1 and HeadsOrTails == "Heads" or HeadsOrTails =="heads":
            print()
            print("You where right")
            score = score + 1
            print ("Your score is: " + str(score))
            print()
            
        elif FlipResult == 2 and HeadsOrTails == "Tails" or HeadsOrTails == "tails":
            print()
            print("You where right")
            score = score + 1
            print ("Your score is: " + str(score))
            print()
        
        else:
            print()
            print("Wrong")
            print("Your score is: " + str(score))
            print()
    
    print("Yes / No")
    PlayAgain = input("Do you want to play again: ")
    
    if PlayAgain == "Yes":
        CoinFlip()

    elif PlayAgain == "No":
        menu()
    

CoinFlip()
